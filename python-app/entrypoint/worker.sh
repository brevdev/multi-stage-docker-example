#!/bin/sh

set -e

. /venv/bin/activate

exec python -c 'from python_app import worker; worker.run()'