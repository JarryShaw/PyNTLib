# -*- coding: utf-8 -*-


try:
    from setuptools     import setup
except ImportError:
    from distutils.core import setup


setup(

    name = 'jsntlib',

    version = '1.4.2',

    description =
        'A number theory library adapted from mathematic fundamentals of information security homework codes.',

    long_description =
        '       JSNTLIB Archive\n\
        ================================\n\n\
        The whole project is written in *Python*, with compatibility in both 2 & 3 versions.\n\n\
        -  The ``jsntlib`` is an open sourse library for number theory.\n\n\
        -  Header file is ``jsntlib.py``.\n\n\
        -  Usage sample has been attached as ``sample.py``.\n\n\
        -  Document can be found in ``MANUAL.md``.\n\n\
        -  Some tips on this repository will be present later.',

    author = 'Jarry Shaw',

    author_email = 'jarryshaw@icloud.com',

    url = 'https://github.com/JarryShaw/jsntlib/tree/release',

    python_requires = '>=2.7',

    py_modules = ['jsntlib'],

    packages = [
        'jsntlib',
        'jsntlib.NTLArchive',
        'jsntlib.NTLArchive.__abc__',
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

    license = 'LICENSE.txt',

    keywords = [
        'ntl',
        'number-theory',
        'mathematic-fundamentals',
    ],

    platforms = ['macOS', 'Windows', 'Linux', 'Unix',],

)
