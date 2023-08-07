# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set environment variables
ENV DB_VENDOR=sqlite \
    JANEWAY_PORT=8000

# Set working directory in the container
WORKDIR /app

# Copy the current directory (Janeway source code) into the container at /app
COPY ./src /app/src

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/src/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable (if needed)
# ENV NAME=Value

# Run the Janeway development server when the container launches
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
