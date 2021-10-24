def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True
