#!/bin/sh

alembic revision --autogenerate -m "create tables"
alembic upgrade head

if [ "$IS_DEBUG" = "true" ]; then
    fastapi dev ./main.py --host 0.0.0.0 --port "$EXPOSE_PORT"
elif [ "$IS_DEBUG" != "true" ]; then
    fastapi run ./main.py --host 0.0.0.0 --port "$EXPOSE_PORT"
else
    echo "algo salió mal XD"
fi