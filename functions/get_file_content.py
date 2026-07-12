import os
from config import MAX_CHAR

schema_get_files_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lists the contents of a given file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read files contents, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
     try:    
        work_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(work_path, file_path))
        #print(os.path.normpath(os.path.join(work_path, file_path)))

        # Will be True or False
        valid_target_dir = os.path.commonpath([work_path, target]) == work_path
        #print(work_path, target, valid_target_dir)

    
        if valid_target_dir == False:
            return (f'Result for "{file_path}" directory: \n Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        elif os.path.isfile(target) == False:
            return (f'Error: File not found or is not a regular file: "{file_path}"')


        with open(target, "r") as f:
            content = f.read(MAX_CHAR)

            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'

        return content


     except Exception as e:
        return Exception(f"Result for '{file_path}' file: \n Error: {e}")