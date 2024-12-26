import subprocess


def install_libraries(libraries):
    """
    Installs a list of Python libraries using pip.

    Args:
        libraries (list): A list of library names to install.

    Returns:
        dict: A dictionary containing success and error messages.
    """
    results = {"success": [], "errors": []}

    for library in libraries:
        try:
            # Run pip install command
            result = subprocess.run(
                ["pip", "install", library],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode == 0:
                # Installation succeeded
                results["success"].append(f"{library} installed successfully.")
            else:
                # Installation failed
                results["errors"].append(f"Failed to install {library}: {result.stderr.strip()}")

        except Exception as e:
            # Handle any unexpected exceptions
            results["errors"].append(f"Error installing {library}: {str(e)}")

    return results
