def is_prime(number):
    return all(number % i != 0 for i in range(2, int(number / 2) + 1))
