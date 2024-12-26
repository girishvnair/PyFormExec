from flask import Flask, request, jsonify, render_template, send_file
from utils.code_executor import execute_code
from utils.pip_installer import install_libraries
from utils.graph_generator import generate_graph
from utils.markdown_renderer import render_markdown
from utils.form_saver import save_form
import os

app = Flask(__name__)

# Route to test the API
@app.route("/")
def home():
    return render_template("index.html")

# Route to execute Python code
@app.route("/execute", methods=["POST"])
def execute():
    code = request.json.get("code", "")
    output, error = execute_code(code)
    return jsonify({"output": output, "error": error})

# Route to install Python libraries
@app.route("/install", methods=["POST"])
def install():
    libraries = request.json.get("libraries", [])
    result = install_libraries(libraries)
    return jsonify(result)

# Route to generate a graph
@app.route("/generate-graph", methods=["POST"])
def graph():
    graph_data = request.json
    try:
        file_path = generate_graph(graph_data)
        return send_file(file_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to render Markdown
@app.route("/render-markdown", methods=["POST"])
def markdown():
    markdown_text = request.json.get("text", "")
    try:
        rendered_html = render_markdown(markdown_text)
        return jsonify({"html": rendered_html})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to save form as HTML/JS
@app.route("/save-form", methods=["POST"])
def save_form_route():
    form_data = request.json
    try:
        file_path = save_form(form_data)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure uploads directory exists
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "uploads/images")):
        os.makedirs(os.path.join(os.path.dirname(__file__), "uploads/images"))
    app.run(debug=True)
