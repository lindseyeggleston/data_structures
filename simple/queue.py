class Queue():
    """ A Queue is a dynamic array-like data structure that follows
    the principle of FIFO (or first in, first out). All elements of
    the Queue must be of the same data type. Note, the Queue will
    attempt to coerce inputs to the same type as the first element.

    Args:
        data: int, float, str, or array-like of same types
        max_size: int - max number of elements allowed in the Queue
        dtype: specific data type for elements in the Queue

    Methods:
        enqueue(x): adds x to the tail of Queue
        dequeue(): removes element at the head of the Queue
        peek(): views element at the head of the Queue without
            removing it
        is_empty(): reports whether the Queue is empty or not
        is_full(): checks if queue is full or not
    """
    def __init__(self, data=None, max_size: int = None, dtype=None):
        self._data = []
        self._max_size = max_size
        if dtype in {None, int, float, tuple}:
            self._dtype = dtype
        else:
            raise TypeError('Queue only supports int, float, and str types')
        if data:
            if isinstance(data, (list, tuple)):
                for element in data:
                    self.enqueue(element)
            else:
                self.enqueue(data)

    def enqueue(self, x):
        if not self.is_full():
            x = self._check_type(x)
            self._data.append(x)
        else:
            raise OverflowError('Queue is full and cannot be added to.')

    def dequeue(self):
        return self._data.pop(0)

    def peek(self):
        if not self.is_empty():
            return self._data[0]

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        if self._max_size:
            if len(self) >= self._max_size:
                return True
        return False
    
    def _check_type(self, x):
        if not isinstance(x, (int, float, str)):
            raise TypeError('Queue only supports int, float, and str types')
        if self.is_empty() and not self._dtype:
            self._dtype = type(x)
        try:
            return self._dtype(x)
        except:
            raise TypeError('Could not convert {} to type {}'.format(x, self._dtype.__name__))

    def __repr__(self):
        return '{}({})'.format(__class__.__name__, self._data)

    def __len__(self):
        return len(self._data)