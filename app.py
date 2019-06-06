import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/isPrime/<int:number>')
def isPrime(number):
    return '%d is prime.\n' % number

@app.route('/primesStored')
def primesStored():
    count = 2
    return '{} ~number list.\n'.format(count)

