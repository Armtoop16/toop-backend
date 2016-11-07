Toop
====

* [Requirements](#requirements)
* [Deploy on a Local Machine](#deploy-on-a-local-machine)
* [Deploy on a Remote Server](#deploy-on-a-remote-server)
* [Configurations](#configurations)
* [IMPORTANT](#important)

## Requirements

* <a href="https://www.vagrantup.com" target="_blank">Vagrant (1.8 or higher)</a> (only on local machine)
* <a href="https://www.virtualbox.org" target="_blank">VirtualBox (latest version)</a>  (only on local machine)
* <a href="https://git-scm.com" target="_blank">Git</a>  (only on remote server)

Install these requirements and continue.

## Deploy on a Local Machine

1. Clone project code from this repository.
2. Open **terminal** and change your working directory to the project directory.
3. Run `vagrant up`.
4. Run `vagrant hostmanager`.
5. Run `vagrant ssh`.
6. Set configurations. Follow the instructions in [config section](#configurations) for this step.
8. Run `cd /var/www`.
9. Make `provision.sh` file executable. Run `sudo chmod a+x provision.sh`.
10. Run `./provision.sh`.
12. Enjoy!


## Deploy on a Remote Server

1. Connect to your server using `ssh`.
2. Run `cd /var/www`. If the directory does not exist, create it with this command: `sudo mkdir /var/www`.
3. Clone project code from this repository to `/var/www` directory. Run `git clone <REPO_URL> .`. Checkout the appropriate git branch.
4. Set configurations. Follow the instructions in [config section](#configurations) for this step.
5. Install ***salt-minion*** and requirements.
  * `sudo apt-get -y install git-core`.
  * `sudo apt-get -y install python-setuptools`.
  * `sudo easy_install GitPython`.
  * `curl -L https://bootstrap.saltstack.com | sudo sh`.
6. Run `cd /var/www`.
7. Make `provision.sh` file executable. Run `sudo chmod a+x provision.sh`.
8. Run `./provision.sh`.
9. Enjoy!

> Future deployments do not need installing salt, so step #5 can be skipped.

## Configurations

Config is kept in environment variables. To setup your project environment variables copy `.env.dist` to `.env` in project root. In most cases values in `.env.dist` will work in a local environment.

## IMPORTANT

* It's important to be sure that environment variables are up to date, so please compare `.env.dist` file with the current `.env` file when deploying and add needed variables to `.env`.
* Always run `source /etc/environment` after provision, otherwise the environment variables will not be set. 
