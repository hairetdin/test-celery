#!/bin/bash

celery worker -E -l INFO -A testtask -Q import_value --hostname=localhost
celery worker -E -l INFO -A testtask -Q calc_value --hostname=localhost
celery worker -E -l INFO -A testtask -Q save_value --hostname=localhost
