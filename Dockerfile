FROM python:3.11.6-slim

WORKDIR /home/runner/work/
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "Jinja2Linter.py"]