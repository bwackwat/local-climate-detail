#!/bin/bash

./collect_data.py >> collect_data.log 2>&1 &

./manage.py runserver 0.0.0.0:8000 >> runserver.log 2>&1 &\

