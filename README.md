stacker_blueprints
==================

[![circleci](https://circleci.com/gh/cloudtools/stacker_blueprints.svg?style=shield)](https://circleci.com/gh/cloudtools/stacker_blueprints)
[![pypi package](https://badge.fury.io/py/stacker_blueprints.svg)](https://badge.fury.io/py/stacker_blueprints)
[![slack](https://empire-slack.herokuapp.com/badge.svg)](https://empire-slack.herokuapp.com)

An attempt at a common Blueprint library for use with [stacker](https://github.com/cloudtools/stacker).

# Quick start

>NOTES: it will create aws resources and generate cost on your aws account. `make destroy` them all if not required any more.

If you're new to stacker you may use [stacker_cookiecutter](https://github.com/cloudtools/stacker_cookiecutter) to setup your project.

1) Make sure you [set up authentication credentials to access aws](http://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration)

2) Review files [conf/stage.env](conf/stage.env) and [conf/example.yaml](conf/example.yaml)

3) Adjust namespace in [conf/stage.env](conf/stage.env) to a global unique name

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
