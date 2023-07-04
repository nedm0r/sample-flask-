FROM python:3.8

# Set a directory for the app
WORKDIR /usr/src/app

# Copy only the app.py file to the container
COPY . .

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev
    
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Tell the port number the container should expose
EXPOSE 5000

# Run the command
CMD ["python", "./app.py"]
