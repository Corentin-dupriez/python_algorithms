import time

def calculate_time(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'Execution time: {end - start:.6f} seconds')
        return result
    return wrapper