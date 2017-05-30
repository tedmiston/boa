import os
from setuptools import find_packages, setup


def read(filename):
    """Load the contents of a file."""
    root_dir = os.path.dirname(__file__)
    filepath = os.path.join(root_dir, filename)
    return open(filepath).read()


setup(
    name='boa-str',
    version='1.0.1',
    description='Convert strings to snakecase',
    long_description=read('README.md'),
    url='https://github.com/astronomerio/boa',
    author='Taylor Edmiston',
    author_email='taylor@astronomer.io',
    license='MIT',
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
    keywords='boa snakecase snake_case snake case inflector astronomer astronomerio',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
)
