from setuptools import setup, find_packages

setup(
    name='tetris',
    version='0.0.1.dev',
    description='Tetris game for BaseCase application.',
    maintainer='Julian Kuhlmann',
    maintainer_email='jlnkuhlmann@gmail.com',
    install_requires=['numpy'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'play_tetris=tetris.main:run_from_command_line'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering'
    ]
)
