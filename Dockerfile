FROM python:3.9

RUN python -m venv /opt/venv 
RUN /opt/venv/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# check our python environment
RUN /opt/venv/bin/python -–version

COPY . .