mkdir PyFormExecPro
cd PyFormExecPro

# Backend
mkdir -p backend/utils
mkdir -p backend/templates
mkdir -p backend/static/css
mkdir -p backend/static/js
mkdir -p backend/uploads/images

# Frontend
mkdir -p frontend/public
mkdir -p frontend/src/components
mkdir -p frontend/src/services

# Files
touch backend/app.py
touch backend/utils/code_executor.py
touch backend/utils/pip_installer.py
touch backend/utils/graph_generator.py
touch backend/utils/markdown_renderer.py
touch backend/utils/image_processor.py
touch backend/utils/form_saver.py
touch backend/requirements.txt
touch backend/templates/index.html
touch backend/static/css/styles.css
touch backend/static/js/app.js
touch frontend/public/index.html
touch frontend/src/App.jsx
touch frontend/src/index.js
touch frontend/src/components/DynamicForm.jsx
touch frontend/src/components/SaveFormButton.jsx
touch frontend/src/components/MarkdownViewer.jsx
touch frontend/src/components/GraphViewer.jsx
touch frontend/src/services/api.js
touch .gitignore
touch Dockerfile
touch docker-compose.yml
echo "# PyFormExec Pro

A web-based dynamic form application to execute Python code, install libraries, and display results as graphs, images, and markdown, with the ability to save the form as reopenable HTML/JavaScript." > README.md
