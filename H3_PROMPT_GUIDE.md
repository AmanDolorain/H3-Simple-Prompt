# Writing native H3 Reference-to-Video prompts

Research checked 2026-10-28. Use this guide in the ONE multiline textbox; no separate form fields are needed. The node sends exactly what you type. It does not enforce a format or infer missing information.

## Practical writing order

Explain which connected references provide the character, clothing, setting, motion, camera or voice. Then describe the overall look and each shot in playback order. Inside each shot, keep subject appearance/placement, surroundings/lighting, actions, camera and the corresponding dialogue/sound together. Separate ambience from audience-only background score. This is an editorial recommendation derived from the official guide, not a compulsory keyword parser.

## Official full-reference rewrite format

For a detailed structured prompt, put these headings inside the same textbox:

```text
subject_definitions:
[Your reference definitions and subject characteristics.]

summary:
[Your task type and brief description of the intended video.]

retention_analysis:
[Your intended preservation, transfer or audio-reference relationships.]

detailed_description:
[Overall visual style.]
[Shot 1] [Your opening shot, including relevant lighting, action, camera and dialogue.]
[Shot 2] At [your actual cut time], [your next shot, if needed.]

overall_soundscape:
[Your intended ambience and physical sounds.]

non_diegetic_music:
[Your intended audience-only score, or N/A if you explicitly want none.]
```

Bracketed placeholder text above is explanatory, not ready-to-generate content. Replace it with your own instructions; do not include a second shot or sound you do not intend. The node never inserts this template automatically.

The six-section order is the official full-reference rewrite format, not a claim that every simple native prompt must contain all six headings. There is no universal compulsory H3 trigger word. Use a trigger/embedding only when required by a loaded asset and supported by that asset's documentation.

## Reference labels

| Connector input | Prompt label |
| --- | --- |
| ref_image_0 | <Picture 1> |
| ref_image_1 | <Picture 2> |
| ref_image_2 | <Picture 3> |
| ref_video_0 | <Video 1> |
| ref_audio_0 with no connected video soundtrack | <Audio 1> |

Pictures, videos and audio each have independent one-based numbering. Connected video soundtracks are numbered before standalone audio. Only mention actual connected references. Define each reference's role clearly and reuse labels consistently. Do not assume that video sound is connected just because the file has a soundtrack.

## Dialogue and language

The official rewrite convention uses English descriptions while keeping dialogue, lyrics and visible text in their original language. The textbox accepts all Unicode; this is not automatic translation. Follow the guide's speaker and <d>[Language] ...</d> rules when writing explicit speech/lyrics. Keep dialogue inside its shot. Do not reorder events solely to group all lighting or dialogue together across shots.

The model may interpret audio reference instructions; prompt text alone does not guarantee sample-identical audio, perfect face consistency or exact lip sync.

## Primary sources

- MiniMax official R2V rewrite guide: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md
- ComfyUI prompt guide: https://github.com/Comfy-Org/docs/blob/main/tutorials/video/minimax/minimax-h3-prompt-guide.mdx
- Native connector code: https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_minimax_h3.py
