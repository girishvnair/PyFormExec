# Use Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the backend code
COPY ./backend /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
