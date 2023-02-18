#!/usr/bin/env python

import argparse
import sys

PERCEPTRONS_PER_CLASS = 15
DIMENSION = 51

def sign(x):
    return 1 if 0 < x else -1

class Matrix(object):
    def __init__(self, rows=1, cols=1, value=0):
        self._data = [[value] * cols for _ in range(rows)]
        self._transpose = False

    @classmethod
    def fromdata(cls, data):
        m = cls()
        m._data = data
        return m

    @classmethod
    def fromfile(cls, stream):
        m = cls()
        m._data = []
        for line in stream:
            m._data.append(list(map(int, line.split())))
            assert len(m._data[0]) == len(m._data[-1])
        return m

    def rows(self):
        if self._transpose:
            return len(self._data[0])
        return len(self._data)

    def cols(self):
        if self._transpose:
            return len(self._data)
        return len(self._data[0])

    def transpose(self):
        self._transpose = not self._transpose
        return self

    def __getitem__(self, row_col):
        row, col = row_col
        return self._data[col][row] if self._transpose else self._data[row][col]

    def __setitem__(self, row_col, val):
        row, col = row_col
        if self._transpose:
            self._data[col][row] = val
        else:
            self._data[row][col] = val

    def __mul__(self, other):
        assert self.cols() == other.rows()
        result = Matrix(self.rows(), other.cols())
        for r in range(self.rows()):
            for c in range(other.cols()):
                for i in range(self.cols()):
                    result._data[r][c] += self[r, i] * other[i, c]
        return result

    def __repr__(self):
        rows = self.rows()
        cols = self.cols()
        return '\n'.join(' '.join('{:+}'.format(self[r,c]) for c in range(cols)) for r in range(rows))

    def sign(self):
        for row in self._data:
            for col in range(len(row)):
                row[col] = sign(row[col])
        return self

    def __iter__(self):
        return iter(self._data)

def load_test_data(test_filename, num_classes=None):
    """Load in the testing data. It should be formatted as:
        <DIMENSION values> <label>
        <DIMENSION values> <label>
        ...
    where the labels are in the range [0, num_classes-1].

    This code strips the label from the last column and puts it in its own
    matrix.
    """
    with open(test_filename) as test_data_file:
        x = Matrix.fromfile(test_data_file)

    y = Matrix(x.rows())
    classes_seen = set()
    for i in range(x.rows()):
        y[i, 0] = x._data[i].pop() # remove the label, put it in the y matrix
        classes_seen.add(y[i, 0])

    assert 0 <= min(classes_seen)
    if num_classes is None:
        # NB: auto-detecting the number of classes will choose the wrong value
        # if the largest class does not appear in the data; in that case,
        # specify it from the command line
        num_classes = max(classes_seen) + 1
        print('auto-detected {} classes'.format(num_classes))
    else:
        assert max(classes_seen) < num_classes

    return x, y, num_classes

def load_weights(weights_file, num_perceptrons):
    global DIMENSION

    expected_num_weights = num_perceptrons * DIMENSION

    weights = []
    line = weights_file.readline()
    while line and len(weights) < expected_num_weights + 1:
        w = list([sign(float(x)) for x in line.split()])
        weights.extend(w)
        line = weights_file.readline()

    if len(weights) != expected_num_weights:
        sys.stderr.write('incorrect number of weights (expected {}, got {})\n'.format(expected_num_weights, len(weights)))
        sys.exit(1)

    assert set(weights) <= {-1, 1}

    weights_reshaped = [weights[i*DIMENSION:((i+1)*DIMENSION)] for i in range(num_perceptrons)]

    return Matrix.fromdata(weights_reshaped)

def summarize(confusion_matrix, correct, n):
    s = []

    accuracy = round(100.0 * float(correct) / n, 2)
    s.append('accuracy: {}/{} = {}%'.format(correct, n, accuracy))
    s.append('')

    s.append('confusion matrix (row: true label, column: predicted label):')
    for row in confusion_matrix:
        s.append(' '.join('{:4d}'.format(c) for c in row))

    return accuracy, '\n'.join(s)

def score_mnist():
    global PERCEPTRONS_PER_CLASS, DIMENSION

    p = argparse.ArgumentParser()
    p.add_argument('data_filename')
    p.add_argument('weights_filename')
    p.add_argument('num_classes', type=int, nargs='?')

    args = p.parse_args()

    x, y, args.num_classes = load_test_data(args.data_filename, args.num_classes)
    x.transpose()

    num_perceptrons = PERCEPTRONS_PER_CLASS * args.num_classes

    with open(args.weights_filename) as weights_file:
        perceptron_weights = load_weights(weights_file, num_perceptrons)

    sum_weights = Matrix(args.num_classes, num_perceptrons)
    for i in range(args.num_classes):
        for j in range(i*PERCEPTRONS_PER_CLASS, (i+1)*PERCEPTRONS_PER_CLASS):
            sum_weights[i, j] = 1

    # this matrix multiplication computes the sum node values
    sum_outputs = sum_weights * (perceptron_weights * x).sign()
    correct = 0
    confusion_matrix = [[0] * args.num_classes for _ in range(args.num_classes)]
    for i in range(sum_outputs.cols()):
        prediction = 0
        truth = y[i, 0]
        for j in range(1, sum_outputs.rows()):
            if sum_outputs[prediction,i] < sum_outputs[j,i]:
                prediction = j

        confusion_matrix[truth][prediction] += 1
        correct += int(truth == prediction)

    accuracy, summary = summarize(confusion_matrix, correct, y.rows())

    print(summary)

if __name__ == '__main__':
    score_mnist()

