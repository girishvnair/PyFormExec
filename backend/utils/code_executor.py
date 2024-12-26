import sys
import io


def execute_code(code):
    """
    Executes Python code in a controlled environment.

    Args:
        code (str): Python code to execute.

    Returns:
        tuple: A tuple containing output (str) and error (str).
    """
    # Redirect standard output and error
    stdout = io.StringIO()
    stderr = io.StringIO()

    # Define a restricted global environment
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "str": str,
        }
    }

    try:
        sys.stdout = stdout
        sys.stderr = stderr

        # Execute the code within the restricted environment
        exec(code, restricted_globals)

        # Capture the output
        output = stdout.getvalue()
        error = stderr.getvalue()

    except Exception as e:
        # Handle any exceptions during execution
        output = ""
        error = str(e)

    finally:
        # Reset standard output and error
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    return output, error
