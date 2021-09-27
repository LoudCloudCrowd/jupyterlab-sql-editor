
import json
from pathlib import Path

from .sparksql import SparkSql

def load_ipython_extension(ipython):
    ipython.register_magics(SparkSql)
