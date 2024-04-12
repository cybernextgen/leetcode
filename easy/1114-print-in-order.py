import threading
from typing import List, Callable


res = []


def printFirst():
    res.append("first")


def printSecond():
    res.append("second")


def printThird():
    res.append("third")


class Foo:
    def __init__(self):
        self.semaphoreTwo = threading.Semaphore(0)
        self.semaphoreThree = threading.Semaphore(0)

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.semaphoreTwo.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.semaphoreTwo:
            printSecond()
            self.semaphoreThree.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.semaphoreThree:
            printThird()


threads = []

thread_handler = Foo()
threads.append(threading.Thread(target=thread_handler.first(printFirst)))
threads.append(threading.Thread(target=thread_handler.second(printSecond)))
threads.append(threading.Thread(target=thread_handler.third(printThird)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

assert "".join(res) == "firstsecondthird"
