"""Single-box native H3 prompt text. Author: Aman Dolorain."""

__version__ = "1.2.0"
__author__ = "Aman Dolorain"
WEB_DIRECTORY = "./web"


class AmanSimplePrompt:
    CATEGORY = "Aman Dolorain/Text"
    DESCRIPTION = (
        "One multiline prompt for MiniMax H3 Reference to Video. Text is sent unchanged. "
        "Official full-reference rewrite order: subject_definitions, summary, retention_analysis, "
        "detailed_description, overall_soundscape, non_diegetic_music. "
        "Keep each shot's subject, lighting, action, camera and dialogue together in playback order. "
        "Use connected <Picture 1>, <Video 1>, <Audio 1> references consistently. "
        "No universal trigger word is required. No automatic rewriting or translation."
    )
    FUNCTION = "get_prompt"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"text": ("STRING", {
            "default": "", "multiline": True, "dynamicPrompts": False,
            "tooltip": "Write or paste the complete H3 prompt here. Reference roles first, then "
                       "the scene/shot timeline with character, lighting, action, camera and dialogue; "
                       "describe ambience and background music clearly. Use <Picture 1>, <Video 1>, "
                       "<Audio 1> for connected references. See node help and H3_PROMPT_GUIDE.md "
                       "for the official six-section rewrite format. Your text is not modified.",
        })}}

    def get_prompt(self, text):
        return (text,)


NODE_CLASS_MAPPINGS = {"AmanSimplePrompt": AmanSimplePrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"AmanSimplePrompt": "H3 Simple Prompt"}
