#!/bin/bash

poetry install --sync
alembic upgrade head
python app/data_generator.py