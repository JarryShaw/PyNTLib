# -*- coding: utf-8 -*-


try:
    from setuptools     import setup
except ImportError:
    from distutils.core import setup


setup(

    name = 'pyntlib',

    version = '1.5.0',

    description =
        'A number theory library adapted from mathematic fundamentals of information security homework codes.',

    long_description =
        '       PyNTLib Archive\n'
        '================================\n\n'
        'The whole project is written in *Python*, with compatibility in both 2 & 3 versions.\n\n'
        '-  The ``pyntlib`` is an open sourse library for number theory.\n\n'
        '-  Header file is ``ntl.py``.\n\n'
        '-  Usage sample has been attached as ``sample.py``.\n\n'
        '-  Document can be found in ``MANUAL.md``.\n\n'
        '-  Some tips on this repository will be present later.',

    long_description_content_type = 'text/x-rst',

    author = 'Jarry Shaw',

    author_email = 'jarryshaw@icloud.com',

    url = 'https://github.com/JarryShaw/pyntlib/tree/release/src#pyntlib-manual',

    python_requires = '>=2.7',

    py_modules = ['ntlib'],

    packages = [
        'ntlib',
        'ntlib.NTLArchive',
        'ntlib.NTLArchive.__abc__',
    ],

    package_data = {
        '': [
            'LICENSE.txt',
            'README.rst',
            'sample.py',
        ],
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: English',

        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Security',
        'Topic :: Utilities',
    ],

    license = 'GPLv3',

    keywords = [
        'ntl',
        'number-theory',
        'mathematic-fundamentals',
    ],

    platforms = ['macOS', 'Windows', 'Linux', 'Unix',],

)
