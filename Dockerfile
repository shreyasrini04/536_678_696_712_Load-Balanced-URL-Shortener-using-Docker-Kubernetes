# Use an official lightweight Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only necessary files
COPY requirements.txt ./
COPY app.py ./
COPY templates/ templates/
COPY static/ static/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
