FROM python:3.8 as base
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
WORKDIR /app

FROM base as builder
# used for building
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.14
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin
COPY python_app ./python_app
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base as release
# most minimal
COPY --from=builder /venv /venv
COPY docker-entrypoint.sh python_app ./
CMD ["./docker-entrypoint.sh"]

FROM builder as ci
# install things needed for CI
RUN poetry install
COPY ./tests ./tests

FROM ci as dev
# install things needed for dev
RUN apt-get update && apt-get install -y \
    default-mysql-client
# workspace is where we will mount the code volume
WORKDIR /workspace