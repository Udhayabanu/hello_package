from setuptools import setup

VERSION = '0.1'
DESCRIPTION = 'get teh string '
LONG_DESCRIPTION = 'this is my first pacakage'

# Setting up
setup(
    name="helloWorld",
    version=VERSION,
    author='Udhay',
    author_email='n.udhayabanu@gamil.com',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='ssh://git@github.com:Udhayabanu/hello_package.git',
    packages=['helloWorld'],
    license='MIT',
    install_requires=[],
    classifiers=[
        "Development Status :: It is in Development stage",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
