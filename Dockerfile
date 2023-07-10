# Use the base Ubuntu image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    adb \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copy Streamlit config files
RUN mkdir -p ~/.streamlit
COPY config.toml ~/.streamlit/config.toml
COPY credentials.toml ~/.streamlit/credentials.toml

# Copy Streamlit app file
COPY Dockeroid.py /app/Dockeroid.py

# Set working directory
WORKDIR /app

# Expose port 80 for Streamlit
EXPOSE 80

# Set the entrypoint and default command
ENTRYPOINT ["streamlit", "run"]
CMD ["Dockeroid.py", "--server.enableCORS=false", "--server.enableWebsocketCompression=false", "--server.enableXsrfProtection=false"]
