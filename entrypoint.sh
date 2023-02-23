#!/bin/bash
alembic upgrade head

exec "$@"
