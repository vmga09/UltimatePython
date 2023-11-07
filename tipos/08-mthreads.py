import time
import string, random
import threading
from queue import Queue

q = Queue()
num_worker_threads = 4

def worker():
    while True:
        print("Waiting for Messages ... {thread}".format(thread=threading.get_native_id()))
        item = q.get()
        print(q.qsize())
        print("Message Recived ....{thread}---{msg}".format(msg=item, thread=threading.get_native_id()))
        if item is None:
            q.task_done()
            break
        do_work(item)
        q.task_done()

def do_work(item):
    print("Processing Message ....{thread}---{msg}".format(msg=item, thread=threading.get_native_id()))
    time.sleep(0.0805)
    item = item*2
    print("Message Processed ....{thread}---{msg}".format(msg=item, thread=threading.get_native_id()))

threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

if __name__ == "__main__":
    while True:
        time.sleep(0.02)
        rand = random.choice(string.ascii_letters)
        q.put(rand)
