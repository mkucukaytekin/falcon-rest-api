# -*- coding: utf-8 -*-

import os
import ConfigParser
from itertools import chain


BRAND_NAME = 'Backend REST API'

SECRET_KEY = 'xs4G5ZD9SwNME6nWRWrK_aq6Yb9H8VJpdwCzkTErFPw='
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

APP_ENV = os.environ.get('APP_ENV') or 'local'  # or 'live' to load live
INI_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../conf/{}.ini'.format(APP_ENV))

CONFIG = ConfigParser.ConfigParser()
CONFIG.read(INI_FILE)
MYSQLUSER = CONFIG.get('mysql','user')
MYSQLPASSWORD = CONFIG.get('mysql','password')
MYSQLHOST = CONFIG.get('mysql','host')
MYSQLDATABASE = CONFIG.get('mysql','database')

if APP_ENV == 'dev' or APP_ENV == 'live':
    DB_CONFIG = (MYSQLUSER, MYSQLPASSWORD, MYSQLHOST, MYSQLDATABASE)
    DATABASE_URL = "mysql+pymysql://%s:%s@%s/%s" % DB_CONFIG
else:
    DB_CONFIG = (MYSQLHOST, MYSQLDATABASE)
    DATABASE_URL = "mysql+pymysql://%s/%s" % DB_CONFIG

DB_ECHO = True if CONFIG.get('database','echo') == 'yes' else False
DB_AUTOCOMMIT = True

LOG_LEVEL = CONFIG.get('logging','level')
