FROM python:3.11


WORKDIR /app


RUN pip install poetry


COPY pyproject.toml ./

ENV PATH="/root/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - && poetry install --no-interaction --no-ansi --no-root

COPY . .


EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


