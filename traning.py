N = 28

class Training():
    def __init__(self):
        pass

    def avg(self, train_data):
        matrix = [0 for i in xrange(N * N)]
        for data in train_data:
            for i, d in enumerate(data):
                matrix[i] += d

        matrix = map(lambda n: n / len(train_data), matrix)
        self.dump(matrix)
        return matrix

    def min_diff(self, matrixes, target):
        minimum = 0
        minimum_diff = 255 ** 2 * N * N
        for i in xrange(10):
            diff = self.diff(matrixes[i], target)
            if diff < minimum_diff:
                minimum_diff = diff
                minimum = i
        return minimum

    def diff(self, matrix, target):
        s = 0
        for i in xrange(N * N):
            s += (matrix[i] - target[i]) ** 2
        return s

    def dump(self, matrix):
        def chara(v):
            if v < 50:
                return ' '
            if 50 <= v < 100:
                return '.'
            if 100 <= v < 160:
                return 'o'
            return '@'


        for i in xrange(N):
            for j in xrange(N):
                v = matrix[i * N + j]
                print chara(v),
            print
        print



with open('data/simple.csv', 'r') as train, open('data/test.csv', 'r') as test, open('data/result.csv','w') as w:
    train.readline()
    data = [[] for i in xrange(10)]
    for line in train:
        l = map(int, line.split(','))
        data[l[0]].append(l[1:])

    train = Training()
    average = [train.avg(data[i]) for i in xrange(10)]

    test.readline()
    w.write('ImageId,Label\n')

    for i, line in enumerate(test):
        matrix = map(int, line.split(','))
        result = train.min_diff(average, matrix)
        print '{},{}'.format(i+1, result)
        w.write('{},{}\n'.format(i+1, result))










