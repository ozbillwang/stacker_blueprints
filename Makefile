REGION ?= us-west-2
ENV ?= stage
ARGS ?= --interactive

.PHONY: all lint test build

all: lint test build

# run one time only
prerequisite:
	sudo python setup.py install

lint:
	flake8 stacker_blueprints

test:
	python setup.py test

build:
	stacker build --region ${REGION} ${ARGS} conf/${ENV}.env conf/example.yaml

diff:
	stacker diff --region ${REGION} ${ARGS} conf/${ENV}.env conf/example.yaml

info:
	stacker info --region ${REGION} ${ARGS} conf/${ENV}.env conf/example.yaml

destroy:
	stacker destroy --region ${REGION} ${ARGS} conf/${ENV}.env conf/example.yaml
