/* Tweak panel for fine-tuning. Local only: http://localhost:8765/?tweak
   Save writes assets/css/tweaks.css through tweak/server.py.

   Adapt:
   1. SCOPE: the area whose CSS variables get adjusted (usually the opening).
   2. MEDIA: from which width the saved values apply (the phone keeps its layout).
   3. CONTROLS: one entry per slider. v = CSS variable already used in the CSS,
      label = label for the user, min/max/step, unit (default px),
      start = measured value, in case the variable has no value yet.
   4. THEME: adapt the panel colors to the brand. */
(function () {
  "use strict";

  var SCOPE = ".hero";
  var MEDIA = "(min-width: 821px)";
  var THEME = { main: "#1F2A44", accent: "#E4572E", soft: "#F1F3F6", text: "#1A1A1A" };

  var scope = document.querySelector(SCOPE);
  if (!scope) return;

  function px(el, prop) { return el ? Math.round(parseFloat(getComputedStyle(el)[prop]) || 0) : 0; }
  function q(sel) { return scope.querySelector(sel); }

  var controls = [
    { v: "--hero-top", label: "Top spacing", min: 0, max: 200, start: function () { return px(scope, "paddingTop"); } },
    { v: "--h1-size", label: "Headline size", min: 32, max: 120, start: function () { return px(q("h1"), "fontSize"); } },
    { v: "--h1-measure", label: "Headline width", unit: "ch", min: 8, max: 24, step: 0.5, start: function () { return 15; } },
    { v: "--h1-gap", label: "Space below the headline", min: 0, max: 200, start: function () { return px(q("h1"), "marginBottom"); } },
    { v: "--cta-y", label: "Button up / down", min: -80, max: 80, start: function () { return 0; } },
    { v: "--visual-h", label: "Image size", min: 120, max: 640, start: function () { var el = q("img, svg"); return el ? Math.round(el.getBoundingClientRect().height) : 300; } },
    { v: "--visual-x", label: "Image left / right", min: -300, max: 300, start: function () { return 0; } },
    { v: "--lead-size", label: "Intro text size", min: 14, max: 30, step: 0.5, start: function () { return px(q("p"), "fontSize"); } }
  ];

  /* Start value: the variable's saved value, otherwise the measured size.
     Without this step, the panel overwrites saved values when it opens. */
  function saved(name) {
    var v = getComputedStyle(scope).getPropertyValue(name).trim();
    return v && !/[a-z]\(/i.test(v) ? parseFloat(v) : null;
  }
  controls.forEach(function (c) {
    var measure = c.start;
    c.start = function () { var v = saved(c.v); return v === null || isNaN(v) ? measure() : v; };
  });

  var values = {};
  controls.forEach(function (c) { values[c.v] = c.start(); });

  function unit(c) { return c.unit || "px"; }
  function applyAll() {
    controls.forEach(function (c) { scope.style.setProperty(c.v, values[c.v] + unit(c)); });
    window.dispatchEvent(new Event("resize"));
  }

  var css = document.createElement("style");
  css.textContent = [
    ".tw{position:fixed;left:16px;bottom:16px;z-index:9999;width:320px;max-height:calc(100vh - 32px);overflow:auto;background:#fff;color:" + THEME.text + ";border-radius:10px;box-shadow:0 18px 50px -12px rgba(0,0,0,.45);font:14px/1.4 system-ui,sans-serif}",
    ".tw header{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;background:" + THEME.main + ";color:#fff;border-radius:10px 10px 0 0;position:sticky;top:0}",
    ".tw .bd{padding:10px 14px 14px}.tw.min .bd{display:none}.tw.right{left:auto;right:16px}",
    ".tw header button{background:transparent;border:1px solid rgba(255,255,255,.4);color:#fff;border-radius:6px;width:30px;height:28px;cursor:pointer;flex:none}",
    ".tw label{display:block;margin:10px 0 2px;font-weight:600;color:" + THEME.main + "}",
    ".tw .row{display:flex;gap:10px;align-items:center}.tw input[type=range]{flex:1;accent-color:" + THEME.accent + "}",
    ".tw output{width:62px;text-align:right;font-variant-numeric:tabular-nums}",
    ".tw .acts{display:flex;gap:8px;margin-top:14px}.tw .acts button{flex:1;height:38px;border:0;border-radius:999px;font-weight:700;cursor:pointer}",
    ".tw .save{background:" + THEME.accent + ";color:#fff}.tw .reset{background:" + THEME.soft + ";color:" + THEME.main + "}",
    ".tw .msg{margin-top:10px;font-size:13px;min-height:1em}"
  ].join("");
  document.head.appendChild(css);

  var panel = document.createElement("div");
  panel.className = "tw";
  panel.innerHTML = "<header><b>Fine-tuning</b><span><button class='side' type='button' title='Move the panel to the other side'>⇄</button> <button class='fold' type='button' title='Collapse and expand'>▾</button></span></header><div class='bd'></div>";
  var body = panel.querySelector(".bd");
  panel.querySelector(".fold").addEventListener("click", function () { panel.classList.toggle("min"); });
  panel.querySelector(".side").addEventListener("click", function () { panel.classList.toggle("right"); });

  controls.forEach(function (c) {
    var id = "tw" + c.v.replace(/[^a-z0-9]/gi, "");
    var wrap = document.createElement("div");
    wrap.innerHTML = "<label for='" + id + "'>" + c.label + "</label><div class='row'><input id='" + id + "' type='range'><output></output></div>";
    var input = wrap.querySelector("input");
    var out = wrap.querySelector("output");
    input.min = c.min; input.max = c.max; input.step = c.step || 1; input.value = values[c.v];
    out.textContent = values[c.v] + unit(c);
    input.addEventListener("input", function () {
      values[c.v] = parseFloat(input.value);
      out.textContent = values[c.v] + unit(c);
      scope.style.setProperty(c.v, values[c.v] + unit(c));
      window.dispatchEvent(new Event("resize"));
    });
    c.input = input; c.out = out;
    body.appendChild(wrap);
  });

  var acts = document.createElement("div");
  acts.className = "acts";
  acts.innerHTML = "<button class='reset' type='button'>Reset</button><button class='save' type='button'>Save</button>";
  var msg = document.createElement("p");
  msg.className = "msg";
  body.appendChild(acts);
  body.appendChild(msg);

  acts.querySelector(".reset").addEventListener("click", function () {
    controls.forEach(function (c) { scope.style.removeProperty(c.v); });
    window.dispatchEvent(new Event("resize"));
    requestAnimationFrame(function () {
      controls.forEach(function (c) {
        values[c.v] = c.start();
        c.input.value = values[c.v];
        c.out.textContent = values[c.v] + unit(c);
      });
      msg.textContent = "Reset to the saved values.";
    });
  });

  acts.querySelector(".save").addEventListener("click", function () {
    var lines = controls.map(function (c) { return "    " + c.v + ": " + values[c.v] + unit(c) + ";"; });
    var cssText = "/* Fine-tuning from the tweak panel (?tweak), saved " + new Date().toLocaleString() + ". Applies to " + MEDIA + ". */\n" +
      "@media " + MEDIA + " {\n  " + SCOPE + " {\n" + lines.join("\n") + "\n  }\n}\n";
    fetch("/__tweak", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ css: cssText, values: values }) })
      .then(function (r) { if (!r.ok) throw new Error(r.status); msg.textContent = "Saved to assets/css/tweaks.css."; })
      .catch(function () { msg.textContent = "Saving failed. Is tweak/server.py running?"; });
  });

  document.body.appendChild(panel);
  applyAll();
})();
