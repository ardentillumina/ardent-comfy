from .py.show_text import ShowText
from .py.format_filename_prefix_by_date import FormatFilenamePrefixByDate

NODE_CLASS_MAPPINGS = {
    "ShowText": ShowText,
    "FormatFilenamePrefixByDate": FormatFilenamePrefixByDate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText": "Show Text",
    "FormatFilenamePrefixByDate": "FilenamePrefix By Date",
}

WEB_DIRECTORY = "./js"

__all__ = [
    'NODE_CLASS_MAPPINGS',
    'NODE_DISPLAY_NAME_MAPPINGS',
    'WEB_DIRECTORY',
]
