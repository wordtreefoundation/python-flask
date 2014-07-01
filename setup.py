from setuptools import setup, find_packages

setup(
    name = 'python-flask-docker',
    version = '0.1',
    packages = find_packages(),

    install_requires = [
        'Flask==0.9',
        'Flask-Mail==0.7.2',
        'Flask-SQLAlchemy==0.16',
        'Flask-WTF==0.8',
        'Flask-User==0.5.2',
        'Flask-Babel',
        'SQLAlchemy==0.7.8',
        'SQLAlchemy-Migrate==0.7.2',
        'itsdangerous==0.17',
        'decorator==3.3.3',
        'iso8601==0.1.4',
        'negotiate==0.0.1',
        'elasticsearch',
        'PyJWT==0.1.4'
    ],
)
