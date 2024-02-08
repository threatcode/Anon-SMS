# Use an appropriate base image
FROM ubuntu:latest

# Install git and any other dependencies
RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository and navigate to Anon-SMS directory
RUN git clone https://github.com/threatcode/Anon-SMS.git \
    && cd Anon-SMS

# Set the working directory
WORKDIR /Anon-SMS

# Run the script
CMD ["bash", "Run.sh"]
