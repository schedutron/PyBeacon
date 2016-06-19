from setuptools import setup

setup(
	name='PyBeacon',
	version='0.2',
	packages=['PyBeacon'],
    entry_points = {
        "console_scripts": ['PyBeacon = PyBeacon.PyBeacon:main']
    },

    description ='Python script for scanning and advertising urls over Eddystone-URL.',

    url='https://github.com/nirmankarta/PyBeacon',

    author='Nirmankarta',

    license='MIT',

	classifiers=[
       
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)