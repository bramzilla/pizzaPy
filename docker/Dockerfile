# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files (including the virtual environment) into the container
COPY . /app

# Install any project-specific dependencies (if needed)
# For example, if you have a requirements.txt file:
RUN pip install -r requirements.txt

# Expose any ports that your application may use
# EXPOSE 8080

# Define the command to run your Python application
CMD ["python", "src/gen_test01.py"]