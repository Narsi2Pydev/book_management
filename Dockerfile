# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
