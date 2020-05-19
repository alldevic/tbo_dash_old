#! /usr/bin/env sh

set -o errexit
set -o pipefail
cmd="$@"

function postgres_ready() {
    python3 <<END
import sys
import psycopg2
from os import environ as env
try:
    dbname = env.get('POSTGRES_DB')
    user = env.get('POSTGRES_USER')
    password = env.get('POSTGRES_PASSWORD')
    host = env.get('POSTGRES_HOST')
    port = 5432
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
    echo >&2 "Postgres is unavailable - sleeping"
    sleep 1
done

echo >&2 "Postgres is up - continuing..."

echo >&2 "Migrating..."
python3 manage.py migrate

echo >&2 "Collect static..."
python3 manage.py collectstatic --noinput

if [[ ${DEBUGPY} == 'TRUE' ]] || [[ ${DEBUGPY} == 'True' ]] || [[ ${DEBUGPY} == '1' ]]; then
    echo >&2 "Starting debug server..."
    exec python3 -m debugpy --listen 0.0.0.0:5678 \
            -m uvicorn tbo_dash.asgi:application \
            --host 0.0.0.0 \
            --port 8000 \
            --access-log \
            --use-colors \
            --log-level debug \
            --lifespan off \
            --reload \
            "$@"
elif [[ ${DEBUG} == 'TRUE' ]] || [[ ${DEBUG} == 'True' ]] || [[ ${DEBUG} == '1' ]]; then
    echo >&2 "Starting dev server..."
    exec python3 manage.py runserver 0.0.0.0:8000
else
    echo >&2 "Starting Gunicorn..."
    exec gunicorn tbo_dash.asgi:application \
        -k uvicorn.workers.UvicornWorker \
        --access-logfile - \
        --name checklists \
        --bind 0.0.0.0:8000 \
        --workers=3 \
        "$@"
fi
fi
