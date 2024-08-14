import os
class TextFileLineCounter():
    def __init__(self):
        pass

    RETURN_TYPES = ("INT","NUMBER","STRING")  # Ensure this matches ComfyUI's expectations
    RETURN_NAMES = ()
    FUNCTION = "count_lines"

    CATEGORY = "line_counter"
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": "", "multiline": False}),
            },
        }

    @classmethod
    def OUTPUT_TYPES(cls):
        return {
            "outputs": {
                "line_count_int": ("INT",),
                "line_count_number": ("NUMBER",),
                "line_count_string": ("STRING",),
            },
        }

    def count_lines(self, file_path: str) -> dict:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at path '{file_path}' does not exist.")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        line_count = len([line for line in lines if line.strip() != ""]) - 1
        return {
            "line_count_int": line_count,           # Integer
            "line_count_number": float(line_count), # Number (float)
            "line_count_string": str(line_count)    # String
        }
    
    def test(self):
        return ()

NODE_CLASS_MAPPINGS = {
"TextFileLineCounter": TextFileLineCounter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
"TextFileLineCounter": "🤑 Text File Line Counter",
}
