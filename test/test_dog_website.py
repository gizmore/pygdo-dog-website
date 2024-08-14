import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled
from gdotest.TestUtil import reinstall_module


class DogWebsiteTest(unittest.TestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        return self

    def test_00_install(self):
        reinstall_module('dog_website')
        self.assertTrue(module_enabled('irc'), 'Install irc does not work')

    def test_01_install2(self):
        pass




if __name__ == '__main__':
    unittest.main()
