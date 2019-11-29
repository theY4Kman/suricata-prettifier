FROM python:3.8-slim
MAINTAINER Zach "they4kman" Kanzler

RUN pip install gunicorn

WORKDIR /opt/suricata-prettifier
COPY . .
RUN pip install .[web]

CMD ["gunicorn", "--bind=0.0.0.0:80", "wsgi:application"]
