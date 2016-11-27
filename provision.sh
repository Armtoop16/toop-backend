#!/bin/sh

# ----------------------------------------------------------------------------------------------------------------------
# Change working directory
# ----------------------------------------------------------------------------------------------------------------------

cd $(dirname $0)

# ----------------------------------------------------------------------------------------------------------------------
# Set environment variables
# ----------------------------------------------------------------------------------------------------------------------

if [ ! -f ./.env ]; then
    echo "ERROR: .env file not found in project root. Please create it from .env.dist file."
    exit 1
fi

. ./.env && ENV_VARS=`cat ./.env`

# ----------------------------------------------------------------------------------------------------------------------
# Pull from SVC
# ----------------------------------------------------------------------------------------------------------------------

if [ "${APP_ENVIRONMENT}" != "local" ]; then
    git checkout .
    git pull
fi

# ----------------------------------------------------------------------------------------------------------------------
# Run SaltStack States
# ----------------------------------------------------------------------------------------------------------------------

sudo rm /etc/salt/minion
sudo rm -rf /srv/salt/

sudo cp salt/minion.conf /etc/salt/minion
sudo cp -a salt /srv/salt

sudo ${ENV_VARS} salt-call --local state.highstate

# ----------------------------------------------------------------------------------------------------------------------
# Restart apache
# ----------------------------------------------------------------------------------------------------------------------

if [ "${APP_ENVIRONMENT}" != "local" ]; then
    sudo service apache2 restart
fi