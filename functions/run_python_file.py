import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    try:    
        work_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(work_path, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([work_path, target]) == work_path
        print(os.path.isdir(target))
    
        if valid_target_dir == False:
            return (f'Result for "{file_path}" directory: \n Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        elif os.path.isfile(target) == False:
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        elif target.endswith(".py") == False:
            return (f'Error: "{file_path}" is not a Python file')
        
        command = ["python", target]
        if args != None:
            command.extend(args)

        status = subprocess.run(command, cwd = work_path, capture_output= True, text = True, timeout = 30)
        
        if status.returncode != 0:
            return f"Process exited with code {status.returncode}"
        elif len(status.stdout) == 0 and len(status.stderr) == 0:
            return "No output produced"
        
        return f"STDOUT: {status.stdout} \n STDERR: {status.stderr}"
    
    except Exception as e:
        return Exception(f"Error: executing Python file: {e}")

