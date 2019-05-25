#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

./collect_data.py >> collect_data.log 2>&1 &

