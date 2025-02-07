from .py.show_text import ShowText
from .py.format_filename_prefix_by_date import FormatFilenamePrefixByDate
from .py.clip_encode_positive_prompt_only import CLIPEncodePositivePromptOnly
NODE_CLASS_MAPPINGS = {
    "ShowText": ShowText,
    "FormatFilenamePrefixByDate": FormatFilenamePrefixByDate,
    "CLIPEncodePositivePromptOnly": CLIPEncodePositivePromptOnly,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText": "Show Text",
    "FormatFilenamePrefixByDate": "FilenamePrefix By Date",
    "CLIPEncodePositivePromptOnly": "Positive Only (CLIP Encode Prompt)",
}

WEB_DIRECTORY = "./js"

__all__ = [
    'NODE_CLASS_MAPPINGS',
    'NODE_DISPLAY_NAME_MAPPINGS',
    'WEB_DIRECTORY',
]
