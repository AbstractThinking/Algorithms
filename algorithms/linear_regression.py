from algorithms.statistics import Statistics;

class RegressionLine(object):

    def __init__(self, dataset):
        self._dataset = dataset;
        self._x_dataset, self._y_dataset = self._split(dataset);
        self._stats = {
            'x': Statistics(self._x_dataset).measures, 
            'y': Statistics(self._y_dataset).measures,
        };
        self._params = {}
        self._params['corr_coef'] = self._correlate();
        self._params['beta'] = self._beta();
        self._params['alpha'] = self._alpha();
        self._params['sse'] = self._sse();

    def predict(self, x):
        """ Return prediction from predictor."""
        if x in self._x_dataset:
            return self._y_dataset[self._x_dataset.index(x)];

        return self._params['beta'] * x + self._params['alpha'];

    def _alpha(self):
        """ Return the least squares alpha parameter. """
        return self._stats['y']['mean'] - self._params['beta'] * self._stats['x']['mean'];

    def _beta(self):
        """ Return the least squares beta parameter."""
        return self._params['corr_coef'] * self._stats['y']['std_dev'] / self._stats['x']['std_dev']

    def _correlate(self):
        """ Return the correlation coefficient. """
        return sum(x_star * y_star for x_star, y_star in zip(self._stats['x']['std_units'], self._stats['y']['std_units'])) / len(self._dataset);
    
    def _error(self, x, y):
        """ Return the error of a given prediction. """
        return y - self.predict(x);

    def _sse(self):
        """ Return the sum of squared errors for predictions over the dataset."""
        return sum(self._error(x_i, y_i) ** 2 for x_i, y_i in self._dataset);

    def _split(self, dataset):
        """ Return the lists taken from the splitted list of tuples."""
        return map(list, zip(*dataset));
