class Queue():
    """ A Queue is a dynamic array-like data structure that follows
    the principle of FIFO (or first in, first out). All elements of
    the Queue must be of the same data type. Note that the Queue 
    will attempt to coerce inputs to the same type as the first
    element.

    Args:
        data: int, float, str, or array-like of same types
        dtype: specific data type for elements in the Queue

    Methods:
        push(x): adds x to end of Queue
        pop(): removes first element from Queue
        is_empty(): reports whether the Queue is empty or not
    """
    def __init__(self, data=None, dtype=None):
        self._data = []
        self._dtype = None
        if data:
            if isinstance(data, (list, tuple)):
                for element in data:
                    self.push(element)
            else:
                self.push(data)

    def push(self, x):
        x = self._check_type(x)
        self._data.append(x)

    def pop(self):
        return self._data.pop(0)

    def is_empty(self):
        return len(self) == 0
    
    def _check_type(self, x):
        if not isinstance(x, (int, float, str)):
            raise TypeError('Stack only supports int, float, and str types')
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