import sys
import os

if len(sys.argv) != 2:
    print ('usage: project_name')
    sys.exit(1)

name = sys.argv[1]
name_no_hyphen = name.replace('-', '')

# Create project structure
os.mkdir(name)
for dir in ('bin', name_no_hyphen, 'tests', 'docs'):
    path = os.path.join(name, dir)
    os.mkdir(path)
    print ('mkdir {0}'.format(path))

# Create __init__.py files in module directories
for dir in (name_no_hyphen, 'tests'):
    path = os.path.join(name, dir, '__init__.py')
    open(path, 'a').close()
    print ('touch {0}'.format(path))

# Create setup.py script
SETUP_TEMPLATE="""\
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {{
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.0.1',
    'install_requires': [
        'nose'
    ],
    'packages': [
        '{0}'
    ],
    'scripts': [
    ],
    'name': '{0}'
}}
setup(**config)
""".format(name_no_hyphen)
setup_path = os.path.join(name, 'setup.py')
with open(setup_path, 'w') as f:
    f.write(SETUP_TEMPLATE)
print ('Wrote {0}'.format(setup_path))

# Create test template
TEST_TEMPLATE="""\
from nose.tools import *
import {0}
def setup():
    print 'SETUP!'
def teardown():
    print 'TEAR DOWN!'
def test_basic():
    print 'I RAN!'
""".format(name_no_hyphen)
test_path = os.path.join(name, 'tests', '{0}_tests.py'.format(name_no_hyphen))
with open(test_path, 'w') as f:
    f.write(TEST_TEMPLATE)
print ('Wrote {0}'.format(test_path))

print ('Done!')