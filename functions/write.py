import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:    
        work_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(work_path, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([work_path, target]) == work_path

    
        if valid_target_dir == False:
            return (f'Result for "{file_path}" directory: \n Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        elif os.path.isfile(target) == False:
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
