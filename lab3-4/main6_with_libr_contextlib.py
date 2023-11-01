import time
from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time}")

# Пример использования
with cm_timer_2():
    time.sleep(5.5)

