from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-TargetStep',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='Innuendo',
      author_email='innuendo_@gmx.de',
      url='https://github.com/InnuendoPi/cbpi4-TargetStep',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-TargetStep': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-TargetStep'],

	  long_description=long_description,
	  long_description_content_type='text/markdown'
     )
