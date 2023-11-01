import time

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"time: {elapsed_time}")

# Пример использования
with cm_timer_1():
    time.sleep(5.5)

