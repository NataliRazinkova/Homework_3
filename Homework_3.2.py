import time
import multiprocessing

def factorize_sync(*numbers):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def test_factorize():
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("Усі тести пройдено успішно.")

start_time = time.time()
factorize_sync(128, 255, 99999, 10651060)
sync_time = time.time() - start_time
print("Синхронна версія виконалася за {:.6f} секунд".format(sync_time))

test_factorize()


def factorize(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results

start_time = time.time()
factorize_parallel(128, 255, 99999, 10651060)
parallel_time = time.time() - start_time
print("Паралельна версія виконалася за {:.6f} секунд".format(parallel_time))

