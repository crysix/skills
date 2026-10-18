/* Inquiry form: validation in the browser, sending as JSON to a webhook, otherwise mailto.

   Expected HTML (shortened):

   <div id="form-wrap">
     <form id="inquiry-form" data-endpoint="" data-mailto="contact@domain.tld" novalidate>
       <div class="field">
         <label for="name">Name</label>
         <input id="name" name="name" required>
         <p class="field-error" id="name-error">Please enter your name.</p>
       </div>
       ... more .field blocks, required fields with required ...
       <div class="field"><label><input type="checkbox" id="consent" name="consent" required> Privacy …</label>
         <p class="field-error" id="consent-error">Please agree.</p></div>
       <!-- Honeypot against spam bots, invisible via CSS -->
       <input type="text" name="website" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
       <button type="submit"><span class="btn-label">Send inquiry</span></button>
       <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
     </form>
     <div id="form-success" tabindex="-1" hidden>
       <h3>Thank you for your inquiry.</h3>
       <p id="form-success-text"></p>
     </div>
   </div>

   CSS: .field.has-error .field-error { display:block } (otherwise display:none),
        #form-wrap.is-sent form { display:none }, .hp { position:absolute; left:-9999px }

   Leave data-endpoint empty: the form then opens the email program.
   data-endpoint with an address: sending via fetch as JSON. Works with
   - own PHP script (templates/inquiry.php): data-endpoint="/inquiry.php"
   - Formspree: data-endpoint="https://formspree.io/f/<id>"
   - Web3Forms: data-endpoint="https://api.web3forms.com/submit" plus
     <input type="hidden" name="access_key" value="<key>"> in the form
   - n8n, Make or Zapier: the webhook's address. The webhook must allow the own domain via CORS.

   TEXT holds every message visitors see. Translate it into the site's language. */
(function () {
  "use strict";

  var TEXT = {
    sending: "Sending …",
    noAnswer: "not provided",
    subject: "Inquiry via ",
    mailtoOpened: "Your email program opens with the prepared message. Please send it from there.",
    sendFailed: "The inquiry couldn't be sent just now. Please try again or write directly to "
  };

  var form = document.getElementById("inquiry-form");
  if (!form) return;

  var wrap = document.getElementById("form-wrap");
  var statusEl = document.getElementById("form-status");
  var successEl = document.getElementById("form-success");
  var successText = document.getElementById("form-success-text");
  var submitBtn = form.querySelector('button[type="submit"]');
  var submitLabel = submitBtn.querySelector(".btn-label") || submitBtn;
  var idleLabel = submitLabel.textContent;
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function fieldValid(input) {
    if (input.type === "checkbox") return input.checked;
    var value = input.value.trim();
    if (!value) return false;
    if (input.type === "email") return emailPattern.test(value);
    return true;
  }

  function showError(input, show) {
    var field = input.closest(".field");
    if (field) field.classList.toggle("has-error", show);
    input.setAttribute("aria-invalid", String(show));
    var error = document.getElementById(input.id + "-error");
    if (!error) return;
    var described = (input.getAttribute("aria-describedby") || "").split(" ").filter(Boolean);
    var has = described.indexOf(error.id) !== -1;
    if (show && !has) described.push(error.id);
    if (!show && has) described.splice(described.indexOf(error.id), 1);
    if (described.length) input.setAttribute("aria-describedby", described.join(" "));
    else input.removeAttribute("aria-describedby");
  }

  var required = Array.prototype.slice.call(form.querySelectorAll("[required]"));

  /* Show errors only after leaving a field, remove them right away while correcting */
  required.forEach(function (input) {
    var evt = input.type === "checkbox" || input.tagName === "SELECT" ? "change" : "blur";
    input.addEventListener(evt, function () {
      var field = input.closest(".field");
      if ((field && field.classList.contains("has-error")) || input.value.trim()) {
        showError(input, !fieldValid(input));
      }
    });
    input.addEventListener("input", function () {
      var field = input.closest(".field");
      if (field && field.classList.contains("has-error") && fieldValid(input)) showError(input, false);
    });
  });

  function collect() {
    var data = {};
    new FormData(form).forEach(function (value, key) {
      data[key] = typeof value === "string" ? value.trim() : value;
    });
    if (form.elements.consent) data.consent = form.elements.consent.checked;
    data.page = window.location.href;
    data.submittedAt = new Date().toISOString();
    return data;
  }

  /* Label of a field for the mailto message */
  function labelFor(name) {
    var el = form.elements[name];
    var label = el && el.id ? form.querySelector('label[for="' + el.id + '"]') : null;
    return label ? label.textContent.replace(/\s*\(optional\)\s*/i, "").trim() : name;
  }

  function mailtoLink(data) {
    var lines = Object.keys(data)
      .filter(function (k) { return ["website", "consent", "page", "submittedAt", "message"].indexOf(k) === -1; })
      .map(function (k) { return labelFor(k) + ": " + (data[k] || TEXT.noAnswer); });
    if (data.message) lines.push("", labelFor("message") + ":", data.message);
    var subject = TEXT.subject + window.location.hostname + (data.company ? ": " + data.company : "");
    return "mailto:" + form.dataset.mailto +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(lines.join("\n"));
  }

  function showSuccess(text) {
    if (text) successText.textContent = text;
    wrap.classList.add("is-sent");
    successEl.hidden = false;
    successEl.focus();
  }

  function setLoading(loading) {
    submitBtn.disabled = loading;
    submitLabel.textContent = loading ? TEXT.sending : idleLabel;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    statusEl.className = "form-status";
    statusEl.textContent = "";

    var firstInvalid = null;
    required.forEach(function (input) {
      var ok = fieldValid(input);
      showError(input, !ok);
      if (!ok && !firstInvalid) firstInvalid = input;
    });
    if (firstInvalid) {
      firstInvalid.focus();
      return;
    }

    var data = collect();
    /* Honeypot filled in: pretend everything is fine, but send nothing */
    if (data.website) {
      showSuccess();
      return;
    }
    delete data.website;

    var endpoint = form.dataset.endpoint;
    if (!endpoint) {
      window.location.href = mailtoLink(data);
      showSuccess(TEXT.mailtoOpened);
      return;
    }

    setLoading(true);
    fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        showSuccess();
      })
      .catch(function () {
        statusEl.className = "form-status is-error";
        statusEl.innerHTML = TEXT.sendFailed + "<a href=\"" + mailtoLink(data) + "\">" + form.dataset.mailto + "</a>.";
      })
      .then(function () { setLoading(false); });
  });
})();
