import datetime

class FilenamePrefixFormatter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "format_string": ("STRING", {
                    "multiline": False,
                    "default": "%Y%m%d_%H%M%S",
                }),
            },
            "optional": {
                "seed": ("INT", {
                    "default": None,
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format_filename_prefix"
    CATEGORY = "String Assistant"
    IS_CHANGED = True

    def format_filename_prefix(self, format_string, seed):
        try:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime(format_string)

            results: list[str] = []

            if seed is not None:
                results.append(f"{formatted_time}_{seed}")
            else:
                results.append(formatted_time)

            return ("".join(results),)
        except Exception as e:
            return (str(e),)