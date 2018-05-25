import os.path
from stacker.blueprints.testutil import BlueprintTestCase
from stacker.config import parse as parse_config
from stacker.context import Context
from stacker.util import load_object_from_string
from stacker.variables import Variable
from glob import glob


class YamlDirTestGenerator():
    def __init__(self):
        self.classdir = os.path.relpath(
            self.__class__.__module__.replace('.', '/'))
        if not os.path.isdir(self.classdir):
            self.classdir = os.path.dirname(self.classdir)

    @property
    def base_class(self):
        return BlueprintTestCase

    @property
    def yaml_dirs(self):
        return ['.']

    @property
    def yaml_filename(self):
        return 'test_*.yaml'

    def test_generator(self):
        # Search for tests in given paths
        configs = []
        for d in self.yaml_dirs:
            configs.extend(
                glob('%s/%s/%s' % (self.classdir, d, self.yaml_filename)))

        class ConfigTest(self.base_class):
            def __init__(self, config, stack, filepath):
                self.config = config
                self.stack = stack
                self.description = "%s (%s)" % (stack.name, filepath)

            def __call__(self):
                try:
                    ctx = self.context
                except AttributeError:
                    ctx = Context(config=self.config,
                                  environment={'environment': 'test'})

                configvars = self.stack.variables or {}
                variables = [Variable(k, v) for k, v in configvars.iteritems()]

                blueprint_class = load_object_from_string(
                    self.stack.class_path)
                blueprint = blueprint_class(self.stack.name, ctx)
                blueprint.resolve_variables(variables or [])
                blueprint.setup_parameters()
                blueprint.create_template()
                self.assertRenderedBlueprint(blueprint)

            def assertEquals(self, a, b, msg):
                assert a == b, msg

        for f in configs:
            with open(f) as test:
                try:
                    config = parse_config(test.read())
                except Exception as e:
                    raise Exception("Error loading %s: %s" % (f, e))
                config.validate()

                for stack in config.stacks:
                    # Nosetests supports "test generators", which allows us to
                    # yield a callable object which will be wrapped as a test
                    # case.
                    #
                    # http://nose.readthedocs.io/en/latest/writing_tests.html#test-generators
                    yield ConfigTest(config, stack, filepath=f)
