#!/bin/bash
set -euo pipefail

source /venv/bin/activate

# Espera Postgres aceitar conexões
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST:$POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# Comandos do Django
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Substitui o shell pelo runserver
exec python manage.py runserver 0.0.0.0:8000
