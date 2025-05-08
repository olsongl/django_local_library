FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Make sure entrypoint.sh is executable
RUN chmod +x /app/entrypoint.sh

# Use it as both ENTRYPOINT and CMD
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
