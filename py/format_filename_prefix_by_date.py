import os
import datetime

from .base_node import BaseNodeStringAssistant


class FormatFilenamePrefixByDate(BaseNodeStringAssistant):
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename_prefix",)
    IS_CHANGED = True

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "seed": ("INT", {
                    "default": None,
                    "forceInput": True,
                }),
                "suffix": ("STRING", {
                    "default": "",
                }),
            },
        }

    def func(self, seed=None, suffix=""):
        current_time = datetime.datetime.now()
        formatted_date = current_time.strftime("%Y%m%d")
        formatted_date_and_time = current_time.strftime("%Y%m%d_%H%M")

        fragments: list[str] = []
        fragments.append(os.path.join(
            formatted_date,
            formatted_date_and_time,
        ))

        if seed is not None:
            fragments.append(f"_{seed}")

        if suffix != "":
            fragments.append(f"_{suffix}")

        return ("".join(fragments),)
