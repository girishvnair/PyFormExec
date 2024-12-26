# PyFormExec

PyFormExec is a web-based application that allows users to dynamically create forms, render Markdown, generate graphs, and execute Python code securely. The application includes a React-based frontend and a Flask-based backend, orchestrated using Docker Compose.

---

## Features

1. **Dynamic Form Builder**:
   - Add and remove fields dynamically.
   - Save forms as reusable HTML files.

2. **Markdown Viewer**:
   - Render Markdown into HTML.
   - Supports headers, lists, links, and more.

3. **Graph Generator**:
   - Generate graphs from user-provided data.
   - Supports line and bar graphs.

4. **Python Code Execution**:
   - Securely execute Python code and capture outputs.

---

## Prerequisites

Ensure you have the following installed:
- **Docker** (20.x or higher)
- **Docker Compose** (1.29.x or higher)
- **AWS CLI** (for EKS deployment)
- **kubectl** (for Kubernetes management)

---

## Local Setup Instructions

### Clone the Repository
```bash
git clone <repository-url>
cd PyFormExec
```

### Build and Run Locally with Docker Compose

1. **Build and Start the Application**:
   ```bash
   docker-compose up --build
   ```

2. **Access the Application**:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:5000](http://localhost:5000)

### Test Endpoints Using cURL

#### Test `/execute` Endpoint:
```bash
curl -X POST http://127.0.0.1:5000/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "print(5 + 5)"}'
```
**Expected Response:**
```json
{
  "output": "10\n",
  "error": ""
}
```

#### Test `/install` Endpoint:
```bash
curl -X POST http://127.0.0.1:5000/install \
  -H "Content-Type: application/json" \
  -d '{"libraries": ["requests"]}'
```
**Expected Response:**
```json
{
  "success": ["requests installed successfully."],
  "errors": []
}
```

#### Test `/generate-graph` Endpoint:
```bash
curl -X POST http://127.0.0.1:5000/generate-graph \
  -H "Content-Type: application/json" \
  -d '{"type": "line", "x": [1, 2, 3], "y": [10, 20, 30], "title": "Sample Graph", "xlabel": "X-Axis", "ylabel": "Y-Axis"}' \
  --output graph.png
```
**Expected Outcome:** A graph is saved as `graph.png`.

#### Test `/render-markdown` Endpoint:
```bash
curl -X POST http://127.0.0.1:5000/render-markdown \
  -H "Content-Type: application/json" \
  -d '{"text": "# Heading\nThis is a test."}'
```
**Expected Response:**
```json
{
  "html": "<h1>Heading</h1>\n<p>This is a test.</p>"
}
```

#### Test `/save-form` Endpoint:
```bash
curl -X POST http://127.0.0.1:5000/save-form \
  -H "Content-Type: application/json" \
  -d '{"fields": [{"type": "text", "label": "Name", "placeholder": "Enter your name"}]}' \
  --output form.html
```
**Expected Outcome:** A form is saved as `form.html`.

---

## AWS EKS Deployment Instructions

### Prerequisites
- Set up an AWS EKS cluster.
- Configure `kubectl` to access the EKS cluster.
- Ensure AWS CLI is authenticated with appropriate permissions.

### Build Docker Images
1. **Build Backend Image**:
   ```bash
   docker build -t <your-dockerhub-username>/pyformexec-backend:latest ./backend
   docker push <your-dockerhub-username>/pyformexec-backend:latest
   ```

2. **Build Frontend Image**:
   ```bash
   docker build -t <your-dockerhub-username>/pyformexec-frontend:latest ./frontend
   docker push <your-dockerhub-username>/pyformexec-frontend:latest
   ```

### Deploy to EKS

1. **Create Kubernetes Deployment Files**:

   - **`backend-deployment.yaml`**:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: pyformexec-backend
     spec:
       replicas: 2
       selector:
         matchLabels:
           app: backend
       template:
         metadata:
           labels:
             app: backend
         spec:
           containers:
           - name: backend
             image: <your-dockerhub-username>/pyformexec-backend:latest
             ports:
             - containerPort: 5000
     ---
     apiVersion: v1
     kind: Service
     metadata:
       name: pyformexec-backend
     spec:
       selector:
         app: backend
       ports:
       - protocol: TCP
         port: 5000
         targetPort: 5000
       type: ClusterIP
     ```

   - **`frontend-deployment.yaml`**:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: pyformexec-frontend
     spec:
       replicas: 2
       selector:
         matchLabels:
           app: frontend
       template:
         metadata:
           labels:
             app: frontend
         spec:
           containers:
           - name: frontend
             image: <your-dockerhub-username>/pyformexec-frontend:latest
             ports:
             - containerPort: 80
     ---
     apiVersion: v1
     kind: Service
     metadata:
       name: pyformexec-frontend
     spec:
       selector:
         app: frontend
       ports:
       - protocol: TCP
         port: 80
         targetPort: 80
       type: LoadBalancer
     ```

2. **Apply Deployment Files**:
   ```bash
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
   ```

3. **Verify Deployments**:
   ```bash
   kubectl get pods
   kubectl get services
   ```

   Note the **EXTERNAL-IP** for the frontend service and use it to access the application.

---

## Contribution
Feel free to submit issues or pull requests. All contributions are welcome!

---

## License
This project is licensed under the Apache License. See the [LICENSE](./LICENSE) file for details.

