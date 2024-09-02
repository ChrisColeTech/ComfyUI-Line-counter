import os
class DirectoryFileCounter():
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory_path": ("STRING", {"default":""}),
            },
        }

    RETURN_TYPES = ("INT","FLOAT","STRING",)

    FUNCTION = "execute_file_counter"

    CATEGORY = "🤖 CCTech/Files"
    
    def execute_file_counter(self, directory_path: str) -> dict:
        # Expand environment variables in the directory path
        directory_path = os.path.expandvars(directory_path)
        
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"The path '{directory_path}' does not exist.")

        file_count = 0

        # Walk the directory tree
        for root, dirs, files in os.walk(directory_path):
            file_count += len(files)  # Count files in each directory

        count = file_count - 1
        return (count, float(count),  str(count))

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

    CATEGORY = "🤖 CCTech/Files"
    
    def execute_line_counter(self, file_path: str) -> dict:
        # Expand environment variables in the file path
        file_path = os.path.expandvars(file_path)
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at path '{file_path}' does not exist.")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        line_count = len([line for line in lines if line.strip() != ""]) - 1
        return (line_count, float(line_count),  str(line_count))


class SimpleNumberCounter:
    def __init__(self):
        self.counters = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_type": (["integer", "float"],),
                "mode": (["increment", "decrement", "increment_to_stop", "decrement_to_stop"],),
                "start": ("FLOAT", {"default": 0, "min": -18446744073709551615, "max": 18446744073709551615, "step": 0.01}),
                "stop": ("FLOAT", {"default": 0, "min": -18446744073709551615, "max": 18446744073709551615, "step": 0.01}),
                "step": ("FLOAT", {"default": 1, "min": 0, "max": 99999, "step": 0.01}),
            },
            "optional": {
                "reset_bool": ("NUMBER",),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
            }
        }

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    RETURN_TYPES = ("NUMBER", "FLOAT", "INT")
    RETURN_NAMES = ("number", "float", "int")
    FUNCTION = "increment_number"

    CATEGORY = "🤖 CCTech/Utilities"

    def increment_number(self, number_type, mode, start, stop, step, unique_id, reset_bool=0):

        counter = int(start) if mode == 'integer' else start
        if self.counters.__contains__(unique_id):
            counter = self.counters[unique_id]

        if round(reset_bool) >= 1:
            counter = start

        if mode == 'increment':
            counter += step
        elif mode == 'deccrement':
            counter -= step
        elif mode == 'increment_to_stop':
            counter = counter + step if counter < stop else counter
        elif mode == 'decrement_to_stop':
            counter = counter - step if counter > stop else counter

        self.counters[unique_id] = counter

        result = int(counter) if number_type == 'integer' else float(counter)

        return ( result, float(counter), int(counter) )


NODE_CLASS_MAPPINGS = {
"Text File Line Counter": TextFileLineCounter,
"Directory File Counter": DirectoryFileCounter,
"Simple Number Counter": SimpleNumberCounter
}

NODE_DISPLAY_NAME_MAPPINGS = {
"Text File Line Counter": "Text File Line Counter ⏲️",
"Directory File Counter": "Directory File Counter ⏲️",
"Simple Number Counter": "Simple Number Counter ⏲️"
}
