import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'termdash/__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line.strip()) # will produce __version__
            break

setup(name='termdash',
      version=__version__,
      description="High-level terminal-based dashboard (improved from dashing library)",
      long_description="""\
Easily create dashboards""",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
      ],
      keywords='dashboard terminal',
      author='Federico Ceratto, Fang Zhang',
      author_email='federico@debian.org, thuzhf@gmail.com',
      url='https://github.com/thuzhf/termdash',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'blessed'
      ],
      )
