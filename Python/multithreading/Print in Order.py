import threading

class Foo:
    def __init__(self):
        self.printFirstDone = threading.Event()
        self.printSecondDone = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.printFirstDone.set();


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.printFirstDone.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.printSecondDone.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.printSecondDone.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()