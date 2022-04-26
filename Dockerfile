# FROM python:latest
# FROM sql_training_linux_machine
FROM python:3.9.7-slim-buster

RUN apt update && apt upgrade -y &&  pip install --upgrade pip
RUN pip install duckdb --pre --upgrade
RUN pip install virtualenv dask distributed bokeh



# COPY . /code
# WORKDIR /code


ENTRYPOINT ["/bin/bash"]




