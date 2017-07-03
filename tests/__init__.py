"""
It didn't seem possible to run doctest on both the boa module and files
outside of that module with the nose2 doctests plugin
(nose2.plugins.doctests).

Instead, I've used the load_tests protocol loader plugin
(nose2.plugins.loader.loadtests), which is loaded by default, to load doctest
indirectly by supplying a custom test loader in tests/__init__.py to solve the
above problem.
"""

import doctest
import glob


def load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite('boa'))
    tests.addTests(doctest.DocFileSuite(*glob.glob('*.rst'),
                                        module_relative=False))
    return tests
