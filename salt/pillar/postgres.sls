postgres:
  acls:
    - ['local', 'all', 'postgres']
    - ['local', 'all',  'all']
    - ['host', 'all', 'all', '127.0.0.1/32', 'md5']
    - ['host', 'all', 'all', '::1/128', 'md5']

  users:
    {{ salt['environ.get']('APP_DB_PGSQL_USERNAME') }}:
      ensure: present
      password: {{ salt['environ.get']('APP_DB_PGSQL_PASSWORD') }}
      createdb: True
      createroles: True
      createuser: True
      inherit: True
      replication: False
      superuser: True

  pkgs_extra:
    - postgresql-9.5-postgis-scripts

  databases:
    {{ salt['environ.get']('APP_DB_PGSQL_DATABASE') }}:
      owner: {{ salt['environ.get']('APP_DB_PGSQL_USERNAME') }}
    postgres:
      owner: {{ salt['environ.get']('APP_DB_PGSQL_USERNAME') }}

  extensions:
    postgis:
      maintenance_db: {{ salt['environ.get']('APP_DB_PGSQL_DATABASE') }}
