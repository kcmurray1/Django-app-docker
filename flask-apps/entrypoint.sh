#!/bin/bash

sleep 10


# flask run -h 0.0.0.0
gunicorn --bind 0.0.0.0:5000 "app:create_app()"