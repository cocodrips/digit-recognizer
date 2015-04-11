# -*- coding: utf-8 -*-
from sklearn.svm import LinearSVC


N = 28
def training(training_data, label_data):
    clf = LinearSVC(C=1.0)
    clf.fit(training_data, label_data)
    return clf


def classify(clf, test_data, label_data):
    result = clf.predict(test_data)

    length = 0
    correct = 0

    pos = 0
    pos_len = 0

    for l, r in zip(label_data, result):
        if l == r:
            correct += 1
        length += 1

        if l == 1:
            pos_len += 1
            if r == 1:
                pos += 1

    return correct, length, int(pos * 100.0 / pos_len)


with open('data/train.csv', 'r') as train, open('data/test.csv', 'r') as test:
    train.readline()

    data = []
    labels = []
    for line in train:
        l = map(int, line.split(','))
        data.append(l[1:])
        labels.append(l[0])

    for i in xrange(10):
        label = []
        for l in labels:
            label.append(1 if l == i else 0)

        m = 500
        clf = training(data[:m], label[:m])
        correct, length, pos = classify(clf, data[m:], label[m:])
        print i, "{}%".format(pos)


