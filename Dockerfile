FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /jpydzr7-django-revise

COPY requirements.txt .
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /jpydzr7-django-revise

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
