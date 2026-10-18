# Phase 3: Copy

Goal: `copy.md` contains every text on the site, from the page title to the confirmation after the form is sent. Only then does design start.

Why before the design: with real copy you see right away whether a heading needs three lines, whether a section is needed at all and how much space the form takes. Placeholders produce layouts that later don't fit the content.

## Approach

1. **Set the structure.** Derive the sections from `PRODUCT.md` and `research/competitors.md`. The topics all top pages cover are included. Every gap the top pages leave open gets a section or an FAQ question. Typical for a service page: opening, stance or problem, services, process, about me, questions, inquiry. Only sections that answer a real visitor question.
2. **Derive copy rules.** What do the strong competitor pages have in common? Often: H1 with service and audience, below it one concrete sentence about the audience, buttons that say what happens, a numbered process, one sentence with a stance.
3. **Write section by section**, with the keyword map next to you. The main term belongs in the page title, the H1 or the opening, and one H2. Not in every sentence. Variants and related terms from the top-page analysis spread naturally across the sections. The text length stays roughly within the range of the top pages. Competitors' wording is never adopted.
4. **Collect fact sentences.** Separately at the end of `copy.md`: one sentence per fact, without advertising language, so that an AI can quote it. Example: "X is an AI consultant and owner of Y. X advises mid-sized companies on introducing AI and is responsible for implementation." Structured data and `llms.txt` are built from these later.
5. **Meta copy:** page title (up to about 60 characters, main term first), meta description (up to about 155 characters, with the next step), text for the preview image.
6. **Form copy:** field names, hints under fields, error messages, confirmation after sending. No promises the user didn't make (see below).
7. **Check** against [../writing-rules.md](../writing-rules.md), every text individually, including meta and form copy.
8. **Collect open questions** and ask them at the end. Invent nothing, no placeholder facts.

## The form as a pre-qualification

If the user doesn't take on every client, the form is more of an application than a contact form. Then add required fields for what's needed to assess the request (for example company size, budget range, description of the project), and a question asking where the visitor came from (including "ChatGPT or another AI", so GEO becomes measurable).

Careful with the tone: wording about high demand or long waiting times quickly sounds arrogant. Best let the user write these sentences themselves and adopt them verbatim.

## No invented promises

Sentences like "I'll get back to you within two business days with dates", "Reply within 24 hours", "free and without obligation" or "The first call takes 30 minutes" are on almost every contact page. That's why an agent writes them on its own, without the user ever having said so. They are promises in the user's name and fall under "invent nothing".

- Promises about response time, process, duration, cost or dates only if the user specified exactly that.
- Without such a specification, the copy only says what is certainly true, for example: "Thanks, your inquiry has arrived."
- If the user wants to say something about it, ask as an open question and adopt their answer verbatim.

## Result file

`copy.md` with this outline:
1. Meta (title, description, preview image text)
2. one section per page section, with heading, text, button labels
3. Form (fields, hints, errors, confirmation)
4. Fact sentences
5. Open questions

`copy.md` stays the source. Later copy changes are made there and on the site at the same time.

## Sign-off

The user reads `copy.md` and gives changes. Expect two to three rounds. The user's verbatim wording is adopted verbatim; only spelling and the writing rules may be applied.

## Done when

- [ ] `copy.md` complete, no placeholders.
- [ ] Keyword map applied (title, H1, H2, FAQ).
- [ ] Topics of the top pages covered, the gaps answered.
- [ ] No promises about response time, process or cost that the user didn't make.
- [ ] Fact sentences collected.
- [ ] Writing rules checked.
- [ ] The user has confirmed.

Next: [Phase 4: Design direction](4-design-direction.md).
