import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:    
        work_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(work_path, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([work_path, target]) == work_path
    
        if valid_target_dir == False:
            return (f'Result for "{directory}" directory: \n Error: Cannot list "{directory}" as it is outside the permitted working directory')
        elif os.path.isdir(target) == False:
            return (f'Error: "{directory}" is not a directory')
        
        contents: list[str] = os.listdir(target)
        list_of_results: list[str] = []
        for item in contents:
            name = item 
            size = os.path.getsize(target + "/" + item)
            status = os.path.isdir(target + "/" + item)
            result = (f"- {name}: file_size={size} bytes, is_dir={status}")
            list_of_results.append(result)
        final = "\n".join(list_of_results)
        return (f"Result for '{directory}' directory: \n{final}")
    except Exception as e:
          return Exception(f"Result for '{directory}' directory: \n Error: {e}")
