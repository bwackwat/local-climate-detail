#!/bin/bash

sleep 60

./manage.py runserver 0.0.0.0:8000 >> runserver.log 2>&1

