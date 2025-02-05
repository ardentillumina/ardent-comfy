import sys
import datetime


class FormatFilenamePrefixByDate:
    CATEGORY = "String Assistant"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"
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
        path_delimiter = "\\" if sys.platform.startswith("win") else "/"

        try:
            current_time = datetime.datetime.now()
            formatted_date = current_time.strftime("%Y%m%d")
            formatted_date_and_time = current_time.strftime("%Y%m%d_%H%M")

            results: list[str] = []
            results.append(formatted_date)
            results.append(path_delimiter)
            results.append(formatted_date_and_time)

            if seed is not None:
                results.append(f"_{seed}")

            if suffix:
                results.append(f"_{suffix}")

            return ("".join(results),)
        except Exception as e:
            return (str(e),)
