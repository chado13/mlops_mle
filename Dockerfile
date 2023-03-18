FROM amd64/python:3.10-slim
RUN apt-get update \
    && apt-get install -y wget build-essential curl
ENV PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=$HOME/.poetry \
    POETRY_VERSION=1.3.1 \
    WORKDIR=/workspace 
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PYTHONPATH=$PYTHONPATH:$WORKDIR
WORKDIR $WORKDIR
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --without dev 
