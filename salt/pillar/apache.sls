apache:
  lookup:
    server: apache2
    service: apache2
    wwwdir: /srv/apache2
    mod_wsgi: libapache2-mod-wsgi-py3
    default_charset: 'UTF-8'

  name_virtual_hosts:
    - interface: '*'
      port: 80
    - interface: '*'
      port: 443

  modules:
    enabled:
      - ldap
      - ssl
      - rewrite
      - wsgi
      - env

  {% if salt['environ.get']('APP_ENVIRONMENT') != 'local' %}
  register-site:
    app:
      name: 'app'
      path: 'salt://apache/templates/app.conf'
      state: 'enabled'
      template: true
      defaults:
        some_var: "need to be passwed becuse of a bug in state :)"
  {% endif %}

  keepalive: 'On'
