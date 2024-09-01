FROM python:3.12-slim-bookworm
WORKDIR /flask-api-app/.venv
copy ..
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]