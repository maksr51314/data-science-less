import urllib.request
import threading
import queue

q = queue.Queue()


def request():
    while True:
        url = q.get()
        if url is None:
            break
        r = urllib.request.urlopen(url)
        print(len(r.read()))
        q.task_done()


for i in range(5):
    t = threading.Thread(target=request)
    t.start()

for i in range(50):
    q.put('http://maksr51314.zz.mu/')

q.join()

for i in range(5):
    q.put(None)
