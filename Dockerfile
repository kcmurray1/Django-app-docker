FROM python:3.13


WORKDIR /usr/src/app

COPY /people/requirements.txt .

RUN pip install -r requirements.txt

# copies the contents of this directory into the app/ directory
COPY /people .
# copies the file into the app/ directory
COPY ./entrypoint.sh .

