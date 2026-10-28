# Native H3 reference prompting

Research checked: 2026-10-28. This guide applies to ComfyUI's native MiniMaxH3ReferenceToVideo connector, not a separate hosted API.

## Write a normal paragraph

Describe the scene and subject, what happens, how the camera moves, the lighting, and the desired sound or speech. Assign each reference a clear purpose such as subject identity, clothes, environment, motion or voice. These are writing suggestions, not mandatory node fields.

## Native reference tags

| Connected input | Tag in prompt |
| --- | --- |
| ref_image_0 | <Picture 1> |
| ref_image_1 | <Picture 2> |
| ref_image_2 | <Picture 3> |
| ref_video_0 | <Video 1> |
| ref_audio_0, with no video soundtrack references connected | <Audio 1> |

Socket numbering starts at zero; prompt numbering starts at one. Pictures, videos and audio each have their own count. Connected video soundtracks are numbered before standalone audio, so adding a video soundtrack can shift the standalone audio label. Only mention references actually connected. The node does not inspect or renumber your references.

## Optional example for three images, a video and one standalone audio

Assumes Picture 1 is the person, Picture 2 is clothing, Picture 3 is the setting, Video 1 is camera/movement guidance, and no video soundtrack is connected. Adapt these roles to your actual files.

Use the man in <Picture 1> as the main character, with the clothing from <Picture 2>, in the setting shown in <Picture 3>. He walks slowly toward the camera and gives a restrained, natural performance. Follow the camera movement from <Video 1>. Keep his appearance and clothing consistent throughout the shot, with realistic lighting and natural facial movement. Use <Audio 1> as the vocal performance reference and match the visible singing to it.

This is an original writing example, not a quoted official prompt. A prompt can request appearance consistency or matched singing, but cannot guarantee exact identity, frame-perfect lip sync or bit-identical audio. If the exact source soundtrack is required, retain that audio for the final video assembly.

## Sources

- ComfyUI native H3 guide, Reference-to-Video prompting tips: https://github.com/Comfy-Org/docs/blob/main/tutorials/video/minimax/minimax-h3-native.mdx
- Native connector tag/schema implementation: https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_minimax_h3.py
- MiniMax H3 multimodal role assignment overview: https://www.minimax.io/blog/minimax-h3
