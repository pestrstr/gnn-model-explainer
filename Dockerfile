FROM ubuntu
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
FROM python:3.9

RUN python -m venv /opt/venv 
RUN /opt/venv/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ADD . .

# Test application with example
SHELL [ "./example.sh" ]
