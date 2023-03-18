import os
from os.path import dirname, join

from dotenv import load_dotenv

basedir = os.path.abspath(dirname(dirname(__file__)))
load_dotenv(join(basedir, ".env"))


DB_URL = os.getenv("DB_URL", "postgresql://user:password@db:5432/mydatabase")
