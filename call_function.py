#this will provide the list of functions the AI agent can call 
import json
from collections.abc import Callable
from functions.get_files_info import *
from functions.run_python_file import *
from functions.get_file_content import *
from functions.write import *


available_functions = [
    schema_get_files_info,
    schema_run_python_file,
    schema_get_files_content,
    schema_write_file,
]

def call_function(tool_call, verbose: bool = False) -> dict:
    try:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments or "{}")
        function_args["working_directory"] = "./calculator"
        if verbose == True:
            print(f" - Calling function: {function_name}({function_args})")
        else:
            print(f" - Calling function: {function_name}")

        function_map: dict[str: callable[..., str]] = {
            "get_file_content": get_file_content,
            "get_files_info": get_files_info,
            "run_python_file": run_python_file,
            "write_file": write_file,
        }

        result = function_map[function_name](**function_args)

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        }
    except:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }