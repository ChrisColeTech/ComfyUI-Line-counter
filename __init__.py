from .line_counter import *


NODE_CLASS_MAPPINGS = {
"TextFileLineCounter": TextFileLineCounter,
"DirectoryFileCounter": DirectoryFileCounter
}

NODE_DISPLAY_NAME_MAPPINGS = {
"TextFileLineCounter": "🤑 Text File Line Counter",
"DirectoryFileCounter": "🤑 Directory File Counter",
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']