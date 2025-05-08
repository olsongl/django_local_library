#!/bin/bash
set -e

echo "⏳ Running database migrations..."
python manage.py migrate

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
exec gunicorn locallibrary.wsgi:application --bind 0.0.0.0:8080
