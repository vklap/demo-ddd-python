# http://flask.pocoo.org/docs/0.10/tutorial/

from setuptools import setup

setup(
    name='DDD Demo',
    version='1.0',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/vklap/demo-ddd-python',
    install_requires=[
        'Flask==0.10.1'
    ],
    test_requires=[]
)