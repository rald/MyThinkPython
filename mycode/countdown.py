import time

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n, end=" ", flush=True)
        time.sleep(1)
        countdown(n - 1)

countdown(10)
