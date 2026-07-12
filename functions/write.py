import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "If target file is within the working directoey then the agent will be able to write to the file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to target file, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "This parameter contains what the Agent wants to write to the file",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:    
        work_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(work_path, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([work_path, target]) == work_path

    
        if valid_target_dir == False:
            return (f'Result for "{file_path}" directory: \n Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        elif os.path.isdir(target) == True:
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
        elif os.path.dirname(target) == False:
            os.makedirs(file_path, exist_ok=True )

        with open(target, "w") as r:
            r.write(content)

        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        return Exception(f"Result for '{file_path}' file: \n Error: {e}")