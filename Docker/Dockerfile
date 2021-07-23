FROM debian:bullseye-slim

RUN apt update && apt install -y python3 python3-pip
COPY ./requirements.txt /opt/file-hosting/requirements.txt
RUN pip3 install -r /opt/file-hosting/requirements.txt
COPY . /opt/file-hosting/

CMD ["python3", "/opt/file-hosting/app.py"]
