import time
import math
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/isPrime/<int:number>')
def isPrime(number):
    if (check_if_prime(number)):
        return '%d is prime.\n' % number
    return '%d is not prime.\n' % number

def check_if_prime(x):
    if 2 == x:
        return True
    if 0 == x % 2 or 1 >= x:
        return False
    sqRoot = int(math.sqrt(x)) + 1
    for factor in range(3, sqRoot, 2):
        if 0 == x % factor:
            return False
    return True

@app.route('/primesStored')
def primesStored():
    count = 2
    return '{} ~number list.\n'.format(count)

