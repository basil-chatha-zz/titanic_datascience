from distutils.core import setup

setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/basil-chatha/titanic_datascience',
    author='Basil Chatha',  # Substitute your name
    author_email='basil.chatha8@gmail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
    install_requires=[
        'pypandoc>=1.4'
    ]
)