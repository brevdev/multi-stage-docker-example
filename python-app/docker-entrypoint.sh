#!/bin/sh

set -e

. /venv/bin/activate

exec uvicorn python_app.main:app