import time
import math
import redis
from flask import Flask

app = Flask(__name__)
storage = redis.Redis(host='redis', port=6379)


@app.route('/isPrime/<int:number>')
def isPrime(number):
    if (check_if_prime(number)):
        storage.lrem('primeList', 0, number)
        # Add prime number to the head of the list the redis object
        storage.lpush('primeList', number)
        return '%d is prime\n' % number
    return '%d is not prime\n' % number

# Return true if x is prime or false if not
def check_if_prime(x):
    if 2 == x:
        return True
    if 0 == x % 2 or 1 >= x:
        return False
    xSqRoot = int(math.sqrt(x)) + 1
    # Check for possible factors other than 2 and 1
    for possiblefactor in range(3, xSqRoot, 2):
        if 0 == x % possiblefactor:
            return False
    return True

@app.route('/primesStored')
def primesStored():
    # Print list of prime numbers in redis object
    primes = ""
    list = storage.lrange('primeList', 0, -1)
    for num in list:
            primes += str(int(num)) + " "
    return primes + '\n'
  
# Extra url to clear old prime numbers
@app.route('/clear')
def clearStored():
    storage.ltrim('primeList', 1, 0)
    return "Cleared stored prime numbers\n"

