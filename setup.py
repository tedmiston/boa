import os
from setuptools import find_packages, setup


def read(filename):
    """Load the contents of a file."""
    root_dir = os.path.dirname(__file__)
    filepath = os.path.join(root_dir, filename)
    return open(filepath).read()


test_requirements = ['codecov', 'cov-core', 'nose2']

dev_requirements = [*test_requirements, 'flake8', 'pycodestyle', 'twine']

extras = {
    'dev': dev_requirements,
    'test': test_requirements,
}

setup(
    name='boa-str',
    version='1.0.1',
    description='Convert strings to snakecase',
    long_description=read('README.rst'),
    url='https://github.com/astronomerio/boa',
    author='Astronomer',
    author_email='taylor@astronomer.io',
    maintainer='Astronomer',
    maintainer_email='taylor@astronomer.io',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=('boa snakecase snake_case snake case inflector astronomer '
              'astronomerio'),
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require=extras,
)
