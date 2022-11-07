FROM ubuntu

RUN apt-get update
RUN apt-get install python3

RUN python -m venv /opt/venv 
RUN /opt/venv/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ADD . .

# Test application with example
SHELL [ "./example.sh" ]
