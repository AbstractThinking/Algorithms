from algorithms.matrix import Matrix;

class Vector(object):

    def __init__(self, vector):
        self.set_vector(vector);

    @staticmethod
    def create(size, val=0):
        return [val for i in range(size)];

    def get_vector(self):
        return self._vector;

    def set_vector(self, v):
        self._is_vector(v);
        self._vector = v;

    @staticmethod
    def add(v, w):
        return [v[i] + w[i] for i in range(len(v))];

    @staticmethod
    def subtract(v, w):
        return [v[i] - w[i] for i in range(len(v))];

    @staticmethod
    def opposite(v):
        return [-v[i] for i in range(len(v))];

    @staticmethod
    def scalar_multiply(c, v):
        return [c * v_i for v_i in v];
        
    @staticmethod
    def dot_product(v, w):
        return sum([v_i * w_i for v_i, w_i in zip(v,w)]);

    def _is_vector(self, v):
        check_errs = {
            'list': lambda obj: not isinstance(obj, list),
            'numeric': lambda obj: not isinstance(obj, (int, float)),
        }

        if check_errs['list'](v):
            raise TypeError;

        for i in range(len(v)):
            if check_errs['numeric'](v[i]):
                raise TypeError;
