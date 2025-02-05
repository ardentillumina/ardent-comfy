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
            },
        }

    def func(self, seed=None):
        path_delimiter = "\\" if sys.platform.startswith("win") else "/"

        try:
            current_time = datetime.datetime.now()
            formatted_date = current_time.strftime("%Y%m%d")
            formatted_time = current_time.strftime("%Y%m%d_%H%M")

            results: list[str] = []
            results.append(formatted_date)
            results.append(path_delimiter)
            results.append(f"{formatted_date}_{formatted_time}")

            if seed is not None:
                results.append(f"_{seed}")

            return ("".join(results),)
        except Exception as e:
            return (str(e),)
