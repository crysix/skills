# Phase 4: Design direction

Goal: A distinct visual world for exactly this site, chosen by the user and recorded as a direction contract. No template, no standard look.

This is the phase that decides between "looks like every AI website" and "looks like my brand".

## Flow

1. Start `/impeccable` with a clear brief: type of site (new landing page or redesign), brand profile from phase 1, chosen references from phase 2, a pointer to `copy.md`, and what the research says about the audience. Mention an old site or an old draft only as a counterexample. impeccable loads `PRODUCT.md` itself.
2. **Let impeccable run its direction process.** It derives directions from the audience's world, draws which one leads, deals challengers against the obvious choice and builds a selection page with cards. Follow the steps it prints. Don't replicate them by hand, skip the draw or preselect a favorite; the process exists so you don't end up with the standard.
3. **The user picks on the selection page.** Re-rolling and safer or bolder variants are possible there.
4. **Direction contract.** impeccable records the chosen direction as a contract in the project (currently under `.impeccable/surfaces/`). Note its path in the status file; phases 5 and 6 build and review against it.

## What makes a good direction

- **One idea carries the whole site.** For a garden nursery, for example, the gardening year: the sections follow the seasons, the process is a bed that grows while scrolling. Every element follows from the same metaphor.
- **The metaphor fits the offer.** It tells something about the service. A metaphor without a connection is decoration.
- **Not the most obvious idea.** For a brand called "Compass", a compass needle is the first thing anyone thinks of. It may be one candidate, not the whole selection.
- **One oversized element per section**, the rest calm.
- **The accent stays rare.** The accent color sits on a few words, not in every heading.

If a direction on the selection page breaks one of these points, say so when you present it.

## Sign-off

The user picks a direction on the selection page. Nothing gets built without a choice.

## Done when

- [ ] impeccable's direction process ran with the brand profile, references and copy as input.
- [ ] The user has picked a direction.
- [ ] The direction contract is in the project, its path in the status file.

Next: [Phase 5: Build](5-build.md).
