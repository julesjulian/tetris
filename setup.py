from setuptools import setup, find_packages

setup(name='tetris',
      version='0.0.1.dev',
      description='Tetris game for BaseCase application.',
      maintainer='Julian Kuhlmann',
      maintainer_email='jlnkuhlmann@gmail.com',
      url='',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      platforms='any',
      classifiers=['Environment :: Console',
                   'Operating System :: OS Independent',
                   'Intended Audience :: Science/Research',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3 :: Only',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Scientific/Engineering']
      )
