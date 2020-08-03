FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
    &&  pip install -r requirements.txt
