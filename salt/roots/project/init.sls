migrate:
  cmd.run:
    - name: source {{ salt['environ.get']('APP_WORKING_DIR') }}venv/bin/activate && ./manage.py migrate --noinput
    - cwd: {{ salt['environ.get']('APP_WORKING_DIR') }}
    - order: last

collectstatic:
  cmd.run:
    - name: source {{ salt['environ.get']('APP_WORKING_DIR') }}venv/bin/activate && ./manage.py collectstatic --noinput --link
    - cwd: {{ salt['environ.get']('APP_WORKING_DIR') }}
    - order: last

create-or-update-superuser:
  cmd.run:
    - name: source {{ salt['environ.get']('APP_WORKING_DIR') }}venv/bin/activate && ./manage.py superuser
    - cwd: {{ salt['environ.get']('APP_WORKING_DIR') }}
    - order: last