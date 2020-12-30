FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
ENV APP_ENV='docker'
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml /app/
COPY ./poetry.lock* /app/
COPY ./api /app/api
WORKDIR /app/

RUN poetry install --no-root --no-dev
RUN ls
ENTRYPOINT poetry run uvicorn api.main:app --reload --host 0.0.0.0 --port 8054