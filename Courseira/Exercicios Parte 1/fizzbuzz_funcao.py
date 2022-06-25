def fizzbuzz(n):
    if(n%5==0)and(n%3==0):
        return 'FizzBuzz'
    elif(n%5==0):
        return 'Buzz'
    elif(n%3==0):
        return 'Fizz'
    else:
        return n

import pytest

def test_fizz():
    assert fizzbuzz(4) == 4
def test_fizz1():
    assert fizzbuzz(15) == ('FizzBuzz')
def test_fizz2():
    assert fizzbuzz(6) == ('Fizz')
def test_fizz3():
    assert fizzbuzz(5) == ('Buzz')

#print(test_fizz())

print(test_fizz(),test_fizz1(),test_fizz2(),test_fizz3())
