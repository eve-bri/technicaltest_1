FROM python:3.10-slim-buster
ADD app.py . 

CMD ["python3", "./app.py"]
