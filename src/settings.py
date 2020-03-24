from os import getenv

SETTINGS = {
    "MYSQL_HOST" : getenv('MYSQL_HOST', 'localhost'),
    "MYSQL_USER" : getenv('MYSQL_USER', 'root'),
    "MYSQL_PASSWORD" : getenv('MYSQL_PASSWORD', '1234'),
    "MYSQL_DB" : getenv('MYSQL_DB', 'flaskcontacs'),
    "SECRET_KEY" : getenv('SECRET_KEY', 'mysecretkey'),
    "PORT" : getenv('PORT', 8000),
    "DEBUG" : getenv('DEBUG', True)
}