# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the entire Scrapy project folder into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Update the package manager and install wait-for-it
RUN apt-get update && \
    apt-get install -y wait-for-it && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
