FROM ubuntu:18.04

# Update packages
RUN apt-get update -y

# Install Python Setuptools
RUN apt-get install -y python3-setuptools python3-pip python3-dev

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip3 install -r requirements.txt

# Bundle app source
ADD . /src

# Expose
EXPOSE  5000

# Run the pipeline
RUN python3 /src/pipeline.py

# Run
CMD ["python3", "/src/awesomeapp/api.py"]
