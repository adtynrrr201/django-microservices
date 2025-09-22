FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Collect static files (jika pakai)
RUN python manage.py collectstatic --noinput

# Gunakan gunicorn untuk production
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
