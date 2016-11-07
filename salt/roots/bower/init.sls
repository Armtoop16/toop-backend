bower:
  npm.installed

bower-install:
  cmd.run:
    - name: bower install --allow-root
    - cwd: {{ salt['environ.get']('APP_WORKING_DIR') }}
    - runas: root
    - order: last