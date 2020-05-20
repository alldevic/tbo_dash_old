#! /usr/bin/env sh

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
            --reload
elif [[ ${DEBUG} == 'TRUE' ]] || [[ ${DEBUG} == 'True' ]] || [[ ${DEBUG} == '1' ]]; then
    echo >&2 "Starting dev server..."
    exec python3 -m uvicorn tbo_dash.asgi:application \
            --host 0.0.0.0 \
            --port 8000 \
            --access-log \
            --use-colors \
            --log-level debug \
            --lifespan off \
            --reload
else
    echo >&2 "Starting Gunicorn..."
    exec gunicorn tbo_dash.asgi:application \
        -k uvicorn.workers.UvicornWorker \
        --access-logfile - \
        --name checklists \
        --bind 0.0.0.0:8000 \
        --workers=3
fi
fi
