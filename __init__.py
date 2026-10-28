"""Simple, literal prompt text for ComfyUI. Author: Aman Dolorain."""

__version__ = "1.0.0"
__author__ = "Aman Dolorain"
WEB_DIRECTORY = "./web"


class AmanSimplePrompt:
    CATEGORY = "Aman Dolorain/Text"
    DESCRIPTION = (
        "Write a paragraph and connect the STRING output to H3 Reference to Video's prompt. "
        "Text is passed through unchanged. H3 reference tags: <Picture 1>, <Video 1>, <Audio 1>. "
        "Assign each connected reference a clear role. No random expansion or automatic rewriting."
    )
    FUNCTION = "get_prompt"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"text": ("STRING", {
            "default": "", "multiline": True, "dynamicPrompts": False,
            "tooltip": "Write scene, action, camera and sound in plain paragraphs. "
                       "For connected H3 references use <Picture 1>, <Video 1>, <Audio 1>. "
                       "The node outputs exactly what you type.",
        })}}

    def get_prompt(self, text):
        return (text,)


NODE_CLASS_MAPPINGS = {"AmanSimplePrompt": AmanSimplePrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"AmanSimplePrompt": "H3 Simple Prompt"}
