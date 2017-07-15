#!/bin/bash

until psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "select 1" > /dev/null 2>&1 ; do
  echo "Waiting for postgres server..."
  sleep 1
done

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
exec "$@"
