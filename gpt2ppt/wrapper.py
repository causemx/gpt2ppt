from collections.abc import Iterator


class IterWrapper(Iterator):  # need to subclass Iterator rather than object
    def __init__(self, it):
        self.it = iter(it)
        self._hasnext = None

    def __iter__(self):
        return self

    def __next__(self):  # __next__ vs next in python 2
        if self._hasnext:
            result = self._thenext
        else:
            result = next(self.it)
        self._hasnext = None
        return result

    def hasnext(self):
        if self._hasnext is None:
            try:
                self._thenext = next(self.it)
            except StopIteration:
                self._hasnext = False
            else:
                self._hasnext = True
        return self._hasnext