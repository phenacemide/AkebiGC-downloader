import time


def total_time(func):  # decorator for counting executable func time

    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Starting a {func.__name__} function...')
        result = func(*args, **kwargs)
        print(f'{func.__name__.capitalize()} is finished.')
        print(f"Execution took: {(time.time() - start)} seconds")
        return result

    return wrapper
