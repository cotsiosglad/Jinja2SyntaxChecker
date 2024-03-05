FROM python:3.9-slim

COPY . /action

WORKDIR /action

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "Jinja2Linter.py"]