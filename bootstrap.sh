#!/bin/bash
export FLASK_APP=./invsys/application.py
pipenv run flask --debug run   -h 0.0.0.0