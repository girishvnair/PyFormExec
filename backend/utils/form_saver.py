import os
import uuid

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../uploads")

def save_form(form_data):
    """
    Saves form configuration as an HTML file with embedded JavaScript to recreate the form.

    Args:
        form_data (dict): JSON data containing form configuration.
                          Example format:
                          {
                              "fields": [
                                  {"type": "text", "label": "Name", "placeholder": "Enter your name"},
                                  {"type": "number", "label": "Age", "placeholder": "Enter your age"}
                              ]
                          }

    Returns:
        str: Path to the saved HTML file.
    """
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    try:
        # Extract fields from form data
        fields = form_data.get("fields", [])
        form_id = uuid.uuid4().hex

        # HTML and JavaScript template
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Saved Form</title>
    <script>
        const formConfig = {fields};

        function createForm() {{
            const form = document.getElementById("dynamicForm");
            formConfig.forEach(field => {{
                const wrapper = document.createElement("div");
                const label = document.createElement("label");
                label.textContent = field.label;

                const input = document.createElement(field.type === "textarea" ? "textarea" : "input");
                input.type = field.type;
                input.placeholder = field.placeholder;

                wrapper.appendChild(label);
                wrapper.appendChild(input);
                form.appendChild(wrapper);
            }});
        }}

        window.onload = createForm;
    </script>
</head>
<body>
    <h1>Saved Form</h1>
    <form id="dynamicForm"></form>
</body>
</html>"""

        # Save to file
        file_name = f"form_{form_id}.html"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return file_path

    except Exception as e:
        raise RuntimeError(f"Error saving form: {str(e)}")
