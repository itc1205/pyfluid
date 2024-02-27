from setuptools import setup, find_packages


setup (name='pyfluid',
        version='0.0.1',
        author='Aksenov Ivan',
        author_email='ivan120536@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        url='https://github.com/itc1205/pyfluid',
        description='Fluidsynth bindings for Python'
)
