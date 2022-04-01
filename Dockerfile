FROM python:latest
RUN apt-get update && apt-get install -y bash curl


COPY . /opt/code
WORKDIR /opt/code


ENTRYPOINT ["/bin/bash"]



