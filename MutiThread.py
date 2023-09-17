import _thread
import time

def start(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(start, ("thread1", 1,))
    _thread.start_new_thread(start, ("thread2", 2,))
except:
    print("Error: 无法启动线程")
while True:
    pass
