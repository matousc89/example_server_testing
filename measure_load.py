import queue
import threading
import time
import requests

URL = "127.0.0.1"
PORT = "8000"
address = "http://{}:{}".format(URL, PORT)
query = "sum?numbers=1,2,3"
url = "{}/{}".format(address, query)

def thread_function(q, k):
    t = time.time()
    r = requests.get(url)
    elapsed_time = time.time() - t
    q.put((elapsed_time, k))

N = 10000

q = queue.Queue()

if __name__ == "__main__":
    for k in range(N):
        threading.Thread(target=thread_function, args=(q, k), daemon=True).start()
        print("Started: {}".format(k))

    results = []
    while not len(results) == N:
        if not q.empty():
            outcome = q.get()
            results.append(outcome[0])
            # print(*outcome)
            print("Collected: {}".format(len(results)))
        time.sleep(0.0001)

    print("Avg time: ", sum(results) / len(results))

