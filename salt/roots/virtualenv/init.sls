virtualenv:
  pip:
    - installed

{{ salt['environ.get']('APP_WORKING_DIR') }}venv:
  virtualenv.managed:
    - python: python3
    - system_site_packages: False
    - requirements: {{ salt['environ.get']('APP_WORKING_DIR') }}requirements.txt
    - no_chown: True
    - distribute: True
    - user: {{ salt['environ.get']('APP_SYSTEM_USER') }}
    - require:
      - virtualenv