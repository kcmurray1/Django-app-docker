FROM python:3.13


WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

# copies the contents of this directory into the app/ directory
COPY . .
# copies the file into the app/ directory
COPY ./entrypoint.sh .

