FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Run migrations and collect static during the image build
RUN python manage.py migrate && python manage.py collectstatic --noinput

CMD ["gunicorn", "locallibrary.wsgi:application", "--bind", "0.0.0.0:8080"]
