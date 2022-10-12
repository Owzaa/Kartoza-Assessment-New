FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1 # Prevent writing .pyc files
ENV PYTHONUNBUFFERED 1 
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80