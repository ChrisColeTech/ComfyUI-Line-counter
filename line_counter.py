import os
class TextFileLineCounter():
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default":""}),
            },
        }

    RETURN_TYPES = ("INT","FLOAT","STRING",)

    FUNCTION = "execute_line_counter"

    CATEGORY = "CCTech/Files"
    
    def execute_line_counter(self, file_path: str) -> dict:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at path '{file_path}' does not exist.")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        line_count = len([line for line in lines if line.strip() != ""]) - 1
        return (line_count, float(line_count),  str(line_count))


NODE_CLASS_MAPPINGS = {
"TextFileLineCounter": TextFileLineCounter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
"TextFileLineCounter": "🤑 Text File Line Counter",
}
