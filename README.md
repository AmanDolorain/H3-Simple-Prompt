# H3 Simple Prompt — v1.2.0

Author: Aman Dolorain · 2026-10-28

One blank multiline textbox. One prompt STRING output. Resize the node to suit your writing space. The complete prompt is passed through exactly: line breaks, spaces, reference tags, Unicode, dialogue and punctuation are preserved. No translation, expansion, template injection or automatic reordering.

## Install and connect

Replace the complete AmanSimplePrompt folder in ComfyUI/custom_nodes. Restart ComfyUI and hard-refresh the browser. Search H3 Simple Prompt. Connect its prompt output to the prompt input of MiniMax H3 Reference to Video. CLIP, VAEs and references remain connected to the H3 connector.

## Improvements

- Return to one multiline textbox; no separate structured fields.
- Verified H3 reference prompt guidance in node help, textbox tooltip and H3_PROMPT_GUIDE.md.
- Approved header-colored internal footer, matching title font/inset, with ♪ Aman Dolorain.
- Hide the extra H3-Simple-Prompt Registry badge above the footer.
- Preserve version 1.0.x single-box prompts unchanged.
- Merge experimental 1.1.0 multi-field workflows into the single textbox using the same previous section order; no field contents deliberately discarded. This happens only during old-workflow loading, not during normal prompt execution.

web/fields.js now contains compatibility code only; upload the new version of this file too. Do not keep the old structured-fields JavaScript. Back up your workflow before upgrading. If the live frontend retains the old layout, add a fresh H3 Simple Prompt node and copy your complete prompt into it.

## Prompt structure

You can write normal paragraphs or paste the full six-section official R2V rewrite format into the same textbox. The official format is a writing guide; this node does not parse or enforce it. Keep shot-specific lighting, action, camera, dialogue and reference usage together so their timing remains clear. No compulsory trigger prefix is inserted.

## Verification

python -m unittest discover -s tests -v
node tests/test_fields.mjs
node --input-type=module --check < web/author.js

Local literal-text/schema and old-workflow migration checks pass. Live ComfyUI rendering and GPU generation remain untested in this update.

## GitHub / Registry

Version: 1.2.0. Upload the complete repository contents, including updated tests and both web files. Existing .gitignore, tests.yml and publish.yml are unchanged. Run the existing manual Publish to Comfy Registry workflow. Commit: Restore single multiline H3 prompt and fix footer badge. Release tag: v1.2.0; title: H3 Simple Prompt v1.2.0.
