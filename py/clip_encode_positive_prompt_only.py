from .base_node import BaseNodePromptAssistant


class CLIPEncodePositivePromptOnly(BaseNodePromptAssistant):
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING",)
    RETURN_NAMES = ("POSITIVE CONDITIONING", "NEGATIVE CONDITIONING",)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "clip": ("CLIP", {
                    "forceInput": True,
                }),
                "positive": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "POSITIVE PROMPT",
                }),
            },
        }

    def func(self, clip, positive):
        positive_tokens = clip.tokenize(positive)
        negative_tokens = clip.tokenize("")

        return (
            clip.encode_from_tokens_scheduled(positive_tokens),
            clip.encode_from_tokens_scheduled(negative_tokens),
        )
