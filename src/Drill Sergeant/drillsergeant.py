# Credits: https://github.com/danbornside/sorted_containers/blob/master/sortedcontainers/sortedlist.py
from bisect import *; from itertools import *; from collections.abc import *; from operator import *; from functools import *; from math import *; from functools import *; from array import *
class SortedList(MutableSequence):
    def __init__(self, iterable, load=1000):
        self._len, self._maxes, self._lists, self._index = 0, array('i'), [], []
        self._load, self._twice, self._half = load, load * 2, load >> 1
        self.update(iterable)
    def clear(self):
        self._len = 0
        del self._maxes[:]
        del self._lists[:]
        del self._index[:]
    def add(self, val):
        _maxes, _lists = self._maxes, self._lists
        if _maxes:
            pos = bisect_right(_maxes, val)
            if pos == len(_maxes):
                pos -= 1
                _maxes[pos] = val
                _lists[pos].append(val)
            else:
                insort(_lists[pos], val)
            self._expand(pos)
        else:
            _maxes.append(val)
            _lists.append([val])
        self._len += 1
    def _expand(self, pos):
        _lists, _index = self._lists, self._index
        if len(_lists[pos]) > self._twice:
            _maxes, _load = self._maxes, self._load
            half = _lists[pos][_load:]
            _lists[pos] = _lists[pos][:_load]
            _maxes[pos] = _lists[pos][-1]
            _maxes.insert(pos + 1, half[-1])
            _lists.insert(pos + 1, half)
            del _index[:]
        else:
            if len(_index) > 0:
                child = self._offset + pos
                while child > 0:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1
    def update(self, iterable):
        _maxes, _lists = self._maxes, self._lists
        values = sorted(iterable)
        if _maxes:
            if len(values) * 4 >= self._len:
                values.extend(chain.from_iterable(_lists))
                values.sort()
                self.clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return
        _load, _index = self._load, self._index
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _maxes.extend(sublist[-1] for sublist in _lists)
        self._len = len(values)
        del _index[:]
    def __contains__(self, val):
        _maxes = self._maxes
        if not _maxes:
            return False
        pos = bisect_left(_maxes, val)
        if pos == len(_maxes):
            return False
        _lists = self._lists
        idx = bisect_left(_lists[pos], val)
        return _lists[pos][idx] == val
    def discard(self, val):
        _maxes = self._maxes
        if not _maxes:
            return
        pos = bisect_left(_maxes, val)
        if pos == len(_maxes):
            return
        _lists = self._lists
        idx = bisect_left(_lists[pos], val)
        if _lists[pos][idx] == val:
            self._delete(pos, idx)
    def _delete(self, pos, idx):
        _maxes, _lists, _index = self._maxes, self._lists, self._index
        lists_pos = _lists[pos]
        del lists_pos[idx]
        self._len -= 1
        len_lists_pos = len(lists_pos)
        if len_lists_pos > self._half:
            _maxes[pos] = lists_pos[-1]
            if len(_index) > 0:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_lists) > 1:
            if pos == 0:
                pos += 1
            prev = pos - 1
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _lists[prev][-1]
            del _maxes[pos]
            del _lists[pos]
            del _index[:]
            self._expand(prev)
        elif len_lists_pos:
            _maxes[pos] = lists_pos[-1]
        else:
            del _maxes[pos]
            del _lists[pos]
            del _index[:]
    def _loc(self, pos, idx):
        if pos == 0:
            return idx
        _index = self._index
        if len(_index) == 0:
            self._build_index()
        total = 0
        pos += self._offset
        while pos:
            if not (pos & 1):
                total += _index[pos - 1]
            pos = (pos - 1) >> 1
        return total + idx
    def _pos(self, idx):
        _len, _lists = self._len, self._lists
        if idx < 0:
            last_len = len(_lists[-1])
            if (-idx) <= last_len:
                return len(_lists) - 1, last_len + idx
            idx += _len
            if idx < 0:
                raise IndexError
        elif idx >= _len:
            raise IndexError
        if idx < len(_lists[0]):
            return 0, idx
        _index = self._index
        if len(_index) == 0:
            self._build_index()
        pos = 0
        len_index = len(_index)
        child = (pos << 1) + 1
        while child < len_index:
            index_child = _index[child]
            if idx < index_child:
                pos = child
            else:
                idx -= index_child
                pos = child + 1
            child = (pos << 1) + 1
        return (pos - self._offset, idx)
    def _build_index(self):
        row0 = list(map(len, self._lists))
        if len(row0) == 1:
            self._index[:] = row0
            self._offset = 0
            return
        head = iter(row0)
        tail = iter(head)
        row1 = list(starmap(add, zip(head, tail)))
        if len(row0) & 1:
            row1.append(row0[-1])
        if len(row1) == 1:
            self._index[:] = row1 + row0
            self._offset = 1
            return
        size = 2 ** (int(log(len(row1) - 1, 2)) + 1)
        row1.extend(repeat(0, size - len(row1)))
        tree = [row0, row1]
        while len(tree[-1]) > 1:
            head = iter(tree[-1])
            tail = iter(head)
            row = list(starmap(add, zip(head, tail)))
            tree.append(row)
        reduce(iadd, reversed(tree), self._index)
        self._offset = size * 2 - 1
    def _slice(self, slc):
        start, stop, step = slc.start, slc.stop, slc.step
        if step == 0:
            raise ValueError('slice step cannot be zero')
        if step is None:
            step = 1
        if step > 0:
            if start is None:
                start = 0
            if stop is None:
                stop = len(self)
            elif stop < 0:
                stop += len(self)
        else:
            if start is None:
                start = len(self) - 1
            if stop is None:
                stop = -1
            elif stop < 0:
                stop += len(self)
        if start < 0:
            start += len(self)
        if step > 0:
            if start < 0:
                start = 0
            elif start > len(self):
                start = len(self)
            if stop < 0:
                stop = 0
            elif stop > len(self):
                stop = len(self)
        else:
            if start < 0:
                start = -1
            elif start >= len(self):
                start = len(self) - 1
            if stop < 0:
                stop = -1
            elif stop > len(self):
                stop = len(self)
        return start, stop, step
    def __delitem__(self, idx):
        if isinstance(idx, slice):
            start, stop, step = self._slice(idx)
            if ((step == 1) and (start < stop) and ((stop - start) * 8 >= self._len)):
                values = self[:start]
                if stop < self._len:
                    values += self[stop:]
                self.clear()
                self.update(values)
                return
            indices = range(start, stop, step)
            if step > 0:
                indices = reversed(indices)
            _pos, _delete = self._pos, self._delete
            for index in indices:
                pos, idx = _pos(index)
                _delete(pos, idx)
        else:
            pos, idx = self._pos(idx)
            self._delete(pos, idx)
    def __getitem__(self, idx):
        _lists = self._lists
        if isinstance(idx, slice):
            start, stop, step = self._slice(idx)
            if step == 1 and start < stop:
                if start == 0 and stop == self._len:
                    return self.as_list()
                start_pos, start_idx = self._pos(start)
                if stop == self._len:
                    stop_pos = len(_lists) - 1
                    stop_idx = len(_lists[stop_pos])
                else:
                    stop_pos, stop_idx = self._pos(stop)
                if start_pos == stop_pos:
                    return _lists[start_pos][start_idx:stop_idx]
                prefix = _lists[start_pos][start_idx:]
                middle = _lists[(start_pos + 1):stop_pos]
                result = reduce(iadd, middle, prefix)
                result += _lists[stop_pos][:stop_idx]
                return result
            if step == -1 and start > stop:
                result = self[(stop + 1):(start + 1)]
                result.reverse()
                return result
            indices = range(start, stop, step)
            return list(self[index] for index in indices)
        else:
            pos, idx = self._pos(idx)
            return _lists[pos][idx]
    def _check_order(self, idx, val):
        _lists, _len = self._lists, self._len
        pos, loc = self._pos(idx)
        if idx < 0:
            idx += _len
        if idx > 0:
            idx_prev = loc - 1
            pos_prev = pos
            if idx_prev < 0:
                pos_prev -= 1
                idx_prev = len(_lists[pos_prev]) - 1
            if _lists[pos_prev][idx_prev] > val:
                raise ValueError
        if idx < (_len - 1):
            idx_next = loc + 1
            pos_next = pos
            if idx_next == len(_lists[pos_next]):
                pos_next += 1
                idx_next = 0
            if _lists[pos_next][idx_next] < val:
                raise ValueError
    def __setitem__(self, index, value):
        _maxes, _lists, _pos = self._maxes, self._lists, self._pos
        _check_order = self._check_order
        if isinstance(index, slice):
            start, stop, step = self._slice(index)
            indices = range(start, stop, step)
            if step != 1:
                if not hasattr(value, '__len__'):
                    value = list(value)
                indices = list(indices)
                if len(value) != len(indices):
                    raise ValueError(
                        'attempt to assign sequence of size {0}'
                        ' to extended slice of size {1}'
                        .format(len(value), len(indices)))
                log = []
                _append = log.append
                for idx, val in zip(indices, value):
                    pos, loc = _pos(idx)
                    _append((idx, _lists[pos][loc], val))
                    _lists[pos][loc] = val
                    if len(_lists[pos]) == (loc + 1):
                        _maxes[pos] = val
                try:
                    for idx, oldval, newval in log:
                        _check_order(idx, newval)
                except ValueError:
                    for idx, oldval, newval in log:
                        pos, loc = _pos(idx)
                        _lists[pos][loc] = oldval
                        if len(_lists[pos]) == (loc + 1):
                            _maxes[pos] = oldval
                    raise
            else:
                if not hasattr(value, '__getitem__'):
                    value = list(value)
                ordered = all(value[pos - 1] <= value[pos]
                              for pos in range(1, len(value)))
                if not ordered:
                    raise ValueError
                if start == 0 or len(value) == 0:
                    pass
                else:
                    if self[start - 1] > value[0]:
                        raise ValueError
                if stop == len(self) or len(value) == 0:
                    pass
                else:
                    if self[stop] < value[-1]:
                        raise ValueError
                del self[index]
                _insert = self.insert
                for idx, val in enumerate(value):
                    _insert(start + idx, val)
        else:
            pos, loc = _pos(index)
            _check_order(index, value)
            _lists[pos][loc] = value
            if len(_lists[pos]) == (loc + 1):
                _maxes[pos] = value
    def __iter__(self):
        return chain.from_iterable(self._lists)
    def __reversed__(self):
        _lists = self._lists
        start = len(_lists) - 1
        iterable = (reversed(_lists[pos])
                    for pos in range(start, -1, -1))
        return chain.from_iterable(iterable)
    def __len__(self):
        return self._len
    def bisect_left(self, val):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_left(_maxes, val)
        if pos == len(_maxes):
            return self._len
        idx = bisect_left(self._lists[pos], val)
        return self._loc(pos, idx)
    def bisect(self, val):
        return self.bisect_right(val)
    def bisect_right(self, val):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_right(_maxes, val)
        if pos == len(_maxes):
            return self._len
        idx = bisect_right(self._lists[pos], val)
        return self._loc(pos, idx)
    def count(self, val):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos_left = bisect_left(_maxes, val)
        if pos_left == len(_maxes):
            return 0
        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], val)
        pos_right = bisect_right(_maxes, val)
        if pos_right == len(_maxes):
            return self._len - self._loc(pos_left, idx_left)
        idx_right = bisect_right(_lists[pos_right], val)
        if pos_left == pos_right:
            return idx_right - idx_left
        right = self._loc(pos_right, idx_right)
        left = self._loc(pos_left, idx_left)
        return right - left
    def copy(self):
        return SortedList(self, load=self._load)
    def __copy__(self):
        return self.copy()
    def append(self, val):
        _maxes, _lists = self._maxes, self._lists
        if not _maxes:
            _maxes.append(val)
            _lists.append([val])
            self._len = 1
            return
        pos = len(_lists) - 1
        if val < _lists[pos][-1]:
            raise ValueError
        _maxes[pos] = val
        _lists[pos].append(val)
        self._len += 1
        self._expand(pos)
    def extend(self, values):
        _maxes, _lists, _load = self._maxes, self._lists, self._load
        if not isinstance(values, list):
            values = list(values)
        if any(values[pos - 1] > values[pos]
               for pos in range(1, len(values))):
            raise ValueError
        offset = 0
        if _maxes:
            if values[0] < _lists[-1][-1]:
                raise ValueError
            if len(_lists[-1]) < self._half:
                _lists[-1].extend(values[:_load])
                _maxes[-1] = _lists[-1][-1]
                offset = _load
        len_lists = len(_lists)
        for idx in range(offset, len(values), _load):
            _lists.append(values[idx:(idx + _load)])
            _maxes.append(_lists[-1][-1])
        _index = self._index
        if len_lists == len(_lists):
            len_index = len(_index)
            if len_index > 0:
                len_values = len(values)
                child = len_index - 1
                while child:
                    _index[child] += len_values
                    child = (child - 1) >> 1
                _index[0] += len_values
        else:
            del self._index[:]
        self._len += len(values)
    def insert(self, idx, val):
        _maxes, _lists, _len = self._maxes, self._lists, self._len
        if idx < 0:
            idx += _len
        if idx < 0:
            idx = 0
        if idx > _len:
            idx = _len
        if not _maxes:
            _maxes.append(val)
            _lists.append([val])
            self._len = 1
            return
        if idx == 0:
            if val > _lists[0][0]:
                raise ValueError
            else:
                _lists[0].insert(0, val)
                self._expand(0)
                self._len += 1
                return
        if idx == _len:
            pos = len(_lists) - 1
            if _lists[pos][-1] > val:
                raise ValueError
            else:
                _lists[pos].append(val)
                _maxes[pos] = _lists[pos][-1]
                self._expand(pos)
                self._len += 1
                return
        pos, idx = self._pos(idx)
        idx_before = idx - 1
        if idx_before < 0:
            pos_before = pos - 1
            idx_before = len(_lists[pos_before]) - 1
        else:
            pos_before = pos
        before = _lists[pos_before][idx_before]
        if before <= val <= _lists[pos][idx]:
            _lists[pos].insert(idx, val)
            self._expand(pos)
            self._len += 1
        else:
            raise ValueError
    def pop(self, idx=-1):
        if (idx < 0 and -idx > self._len) or (idx >= self._len):
            raise IndexError
        pos, idx = self._pos(idx)
        val = self._lists[pos][idx]
        self._delete(pos, idx)
        return val
    def index(self, val, start=None, stop=None):
        _len, _maxes = self._len, self._maxes
        if not _maxes:
            raise ValueError
        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0
        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len
        if stop <= start:
            raise ValueError
        stop -= 1
        pos_left = bisect_left(_maxes, val)
        if pos_left == len(_maxes):
            raise ValueError
        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], val)
        if _lists[pos_left][idx_left] != val:
            raise ValueError
        left = self._loc(pos_left, idx_left)
        if start <= left:
            if left <= stop:
                return left
        else:
            right = self.bisect_right(val) - 1
            if start <= right:
                return start
        raise ValueError
    def as_list(self):
        return reduce(iadd, self._lists, [])
    def __add__(self, that):
        values = self.as_list()
        values.extend(that)
        return SortedList(values)
    def __iadd__(self, that):
        self.update(that)
        return self
    def __mul__(self, that):
        values = self.as_list() * that
        return SortedList(values)
    def __imul__(self, that):
        values = self.as_list() * that
        self.clear()
        self.update(values)
        return self
    def __eq__(self, that):
        return ((self._len == len(that)) and all(lhs == rhs for lhs, rhs in zip(self, that)))
    def __ne__(self, that):
        return ((self._len != len(that)) or any(lhs != rhs for lhs, rhs in zip(self, that)))
    def __lt__(self, that):
        return ((self._len <= len(that)) and all(lhs < rhs for lhs, rhs in zip(self, that)))
    def __le__(self, that):
        return ((self._len <= len(that)) and all(lhs <= rhs for lhs, rhs in zip(self, that)))
    def __gt__(self, that):
        return ((self._len >= len(that)) and all(lhs > rhs for lhs, rhs in zip(self, that)))
    def __ge__(self, that):
        return ((self._len >= len(that)) and all(lhs >= rhs for lhs, rhs in zip(self, that)))
    def _check(self):
        try:
            assert self._load >= 4
            assert self._half == (self._load >> 1)
            assert self._twice == (self._load * 2)
            if self._maxes == []:
                assert self._lists == []
                return
            assert len(self._maxes) > 0 and len(self._lists) > 0
            assert all(sublist[pos - 1] <= sublist[pos]
                       for sublist in self._lists
                       for pos in range(1, len(sublist)))
            for pos in range(1, len(self._lists)):
                assert self._lists[pos - 1][-1] <= self._lists[pos][0]
            assert len(self._maxes) == len(self._lists)
            assert all(self._maxes[pos] == self._lists[pos][-1]
                       for pos in range(len(self._maxes)))
            assert all(len(sublist) <= self._twice for sublist in self._lists)
            assert all(len(self._lists[pos]) >= self._half
                       for pos in range(0, len(self._lists) - 1))
            assert self._len == sum(len(sublist) for sublist in self._lists)
            if len(self._index):
                assert len(self._index) == self._offset + len(self._lists)
                assert self._len == self._index[0]
                def test_offset_pos(pos):
                    from_index = self._index[self._offset + pos]
                    return from_index == len(self._lists[pos])
                assert all(test_offset_pos(pos)
                           for pos in range(len(self._lists)))
                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if self._index[pos] == 0:
                        assert child >= len(self._index)
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert self._index[pos] == child_sum
        except:
            import sys
            import traceback
            traceback.print_exc(file=sys.stdout)
            print(self._len, self._load, self._half, self._twice)
            print(self._index)
            print(self._maxes)
            print(self._lists)
            raise
import os, io, sys; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, M = map(int, input().split()); G = set(); T = SortedList([-1, 0, N+1, N+2], 100); Z = L = 0; X = 10**9+7; P = (3, 32, 323, 3233); U = array('i')
for i in range(M): a, b = map(int, input().split()); G.add((a*X+b))
for _ in range(int(input())):
    c, x = map(int, input().split()); ZZ = 0
    if c&1: T.add(x); sx = T.index(x)+1; px = sx-2; L += 1
    else: T.pop(sx:=T.index(x)); px = sx-1; L -= 1
    x1 = (T[px-1]*X+T[px]) in G
    x2 = (T[px]*X+x) in G
    x3 = (x*X+T[sx]) in G
    x4 = (T[sx]*X+T[sx+1]) in G
    xm = (T[px]*X+T[sx]) in G
    ZZ += P[2*x1+x2]+P[2*x2+x3]+P[2*x3+x4]-P[2*x1+xm]-P[2*xm+x4]
    Z += ZZ if c&1 else -ZZ; U.append(Z)
sys.stdout.write('\n'.join(map(str, U)))