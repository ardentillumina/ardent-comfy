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
                "enable_date_folder": ("BOOLEAN", {
                    "default": True,
                }),
            },
        }

    def func(self, seed=None, suffix="", enable_date_folder=True):
        current_time = datetime.datetime.now()
        formatted_date = current_time.strftime("%Y%m%d")
        formatted_date_and_time = current_time.strftime("%Y%m%d_%H%M")

        fragments: list[str] = []

        if enable_date_folder:
            fragments.append(os.path.join(
                formatted_date,
                formatted_date_and_time,
            ))
        else:
            fragments.append(formatted_date_and_time)

        if seed is not None:
            fragments.append(f"_{seed}")

        if suffix != "":
            fragments.append(f"_{suffix}")

        return ("".join(fragments),)
