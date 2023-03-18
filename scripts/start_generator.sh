#!/bin/bash

poetry install --sync
alembic upgrade head
python data_generator.py