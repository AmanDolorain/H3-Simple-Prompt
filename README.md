# H3 Simple Prompt — v1.0.0

Author: Aman Dolorain · 2026-10-28

One large blank paragraph textbox. One STRING output named `prompt`. No models, API keys, extra Python packages, random tags, prompt enhancement, injected templates or extra controls.

## Install

Put the complete `AmanSimplePrompt` folder in `ComfyUI/custom_nodes/`. Keep `__init__.py` and `web/author.js` inside it. Restart ComfyUI, hard-refresh the browser, then search for **H3 Simple Prompt** (category: Aman Dolorain/Text).

Connect **H3 Simple Prompt → prompt (STRING)** to **MiniMax H3 Reference to Video → prompt**. This node does not encode text or accept CLIP. CLIP and references remain connected to the H3 connector.

You can also open `Simple_Prompt_Starter.json`, which contains just this node, then copy it into your workflow.

## Behavior

Text is passed through exactly, including punctuation, line breaks, spaces, Hindi/Punjabi text and H3 reference tags. Empty input remains empty. There is no automatic translation, random expansion or prefix/suffix. The textbox starts blank. Resize the node for a larger writing area. The footer uses the approved matching header color, title typography and left alignment.

For H3 reference assignment and an optional example, see H3_PROMPT_GUIDE.md. The example is documentation only; it is never inserted into your text.

## Validation

Run `python -m unittest discover -s tests -v`. JavaScript syntax can be checked with `node --input-type=module --check < web/author.js`. Tests verify literal text and the ComfyUI registration/schema. Live installed ComfyUI layout and GPU generation have not been tested here; the footer adapts the previously approved VideoControl implementation.

## GitHub

Upload the contents of this folder to a dedicated repository root. Include `.github` and `.gitignore` on the first upload. Commit: `Release v1.0.0: add H3 Simple Prompt node with branded footer`. Release tag: `v1.0.0`; release title: `H3 Simple Prompt v1.0.0`.
