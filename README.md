stacker_blueprints
==================

[![circleci](https://circleci.com/gh/cloudtools/stacker_blueprints.svg?style=shield)](https://circleci.com/gh/cloudtools/stacker_blueprints)
[![pypi package](https://badge.fury.io/py/stacker_blueprints.svg)](https://badge.fury.io/py/stacker_blueprints)
[![slack](https://empire-slack.herokuapp.com/badge.svg)](https://empire-slack.herokuapp.com)

An attempt at a common Blueprint library for use with `stacker <https://github.com/cloudtools/stacker>`_.

If you're new to stacker you may use `stacker_cookiecutter <https://github.com/cloudtools/stacker_cookiecutter>`_ to setup your project.

# Quick start

>NOTES: it will create aws resources and generate cost on your aws account. `make destroy` them all if not required any more.

Make sure you have permission to access aws, review below files if you need change anything.

1) Adjust namespace to a global unique name, the name in example will be used in s3 bucket name, and has been used. 
2) I have issue to start with pre_build task, if you get same problem, comment that session. 

    config/stage.env
    config/example.yaml

### Build the stacks

Build full stacks (vpc, bastion, myDB, myWeb)

    $ git clone https://github.com/cloudtools/stacker_blueprints.git
    $ cd stacker_blueprints
    $ make build

    # If you have other environment files, such as prod.env
    $ make build ENV=prod

    # If you want to create stacks in other region
    $ make build REGION=ap-southeast-2

### Other commands

    $ make info
    $ make diff
    $ make destroy

### Try other examples

There are examples under folder `conf`, for example, you want to run test on rds stack, you can easily play with below command

    stacker build --region us-west-2 conf/rds/mysql.env conf/rds/mysql.yaml
