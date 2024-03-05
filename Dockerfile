FROM python:3.11.6-slim

COPY . /action

WORKDIR /action

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "Jinja2Linter.py"]