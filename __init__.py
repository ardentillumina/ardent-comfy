from .py.format_filename_prefix_by_date import FormatFilenamePrefixByDate

NODE_CLASS_MAPPINGS = {
    "FormatFilenamePrefixByDate": FormatFilenamePrefixByDate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FormatFilenamePrefixByDate": "FilenamePrefix By Date",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
