from .nodes.filename_prefix_formatter import FilenamePrefixFormatter

NODE_CLASS_MAPPINGS = {
    "FilenamePrefixFormatter": FilenamePrefixFormatter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilenamePrefixFormatter": "Filename Prefix Formatter",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']