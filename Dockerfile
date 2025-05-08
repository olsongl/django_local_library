# Use the official Python 3.12 image
FROM python:3.12

# Environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the codebase
COPY . .

# Run migrations, collect static files, and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn locallibrary.wsgi:application"]
