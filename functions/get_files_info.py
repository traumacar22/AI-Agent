import os
import argparse


def get_files_info(working_directory: str, directory: str = ".") -> str:
    work_path = os.path.abspath(working_directory)
    target = os.path.normpath(os.path.join(work_path, directory))
    
    # Will be True or False
    valid_target_dir = os.path.commonpath([work_path, target]) == work_path
    try:
        if valid_target_dir == False:
            return (f'Cannot list "{directory}" as it is outside the permitted working directory')
        elif os.path.isdir(directory) == False:
            return (f'"{directory}" is not a directory')
        else:
            return (f'Success: "{directory}" is within the working directory')
    except:
        return  Exception(f'Error: idk')