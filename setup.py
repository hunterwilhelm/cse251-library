from setuptools import setup

setup(
    name='cse251',
    version='0.0.1',
    description='The package that contains common classes for the CSE 251 course',
    url='https://github.com/hunterwilhelm/cse251-library',
    author='Brother Comeau and Hunter Wilhelm',
    license='none',
    packages=['cse251'],
    install_requires=['matplotlib', 'numpy', 'pillow', 'opencv-python'],
    zip_safe=False
)