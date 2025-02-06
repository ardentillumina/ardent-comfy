from .base_node import BaseNodeStringAssistant


class ShowText(BaseNodeStringAssistant):
    RETURN_TYPES = ()
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "forceInput": True,
                }),
            },
        }

    def func(self, text=""):
        return {"ui": {"text": text}}
