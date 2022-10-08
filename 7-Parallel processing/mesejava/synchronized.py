from threading import Thread, Lock

lock = Lock()

def synchronized(f):
    def inner(*args, **kwargs):
        global lock
        lock.acquire()
        f(*args, **kwargs)
        lock.release()
    return inner

a = 0

@synchronized
def f():
    global a
    for i in range(300000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()

print(" *** ", a)