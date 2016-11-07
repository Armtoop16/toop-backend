fqdn-conf:
  file.managed:
    - name: /etc/apache2/conf-available/fqdn.conf
    - source: salt://apache/templates/fqdn.conf
    - template: jinja
    - makedirs: True
    - mode: 755

enable-fqdb-conf:
  cmd.run:
    - name: sudo a2enconf fqdn
    - cwd: {{ salt['environ.get']('APP_WORKING_DIR') }}
    - order: last