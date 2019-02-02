import os
from setuptools import setup, find_packages

import haveibeenpwned_api as module


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


setup(
    name=module.__name__.replace("_", "-"),
    version='0.1.0',
    platforms="all",
    packages=find_packages(exclude=('tests','scripts')),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__)
        ),
    },
    entry_points={
        'console_scripts': [
            # FIXME: change entry-point name (this name of you main program)
            'haveibeenpwned-api = {}.api:main'.format(module.__name__),
        ]
    },
    install_requires=(
        'gevent',
        'flask',
    ),
)