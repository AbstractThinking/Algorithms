class Statistics(object):

    def __init__(self, dataset = None):
        self._dataset = dataset;
        self._length = len(dataset) if dataset else None;
        self.measures = {key: None for key in ['mean', 'std_dev', 'std_units', 'variance']}

        if dataset:
            self.measures['mean'] = self.mean(dataset);
            self.measures['variance'] = self.variance(dataset);
            self.measures['std_dev'] = self.std_dev(dataset);
            self.measures['std_units'] = self.std_units(dataset);

    def mean(self, dataset):
        """ Return arithmetic average (mean) taken from the dataset. """
        if self._is_eval(dataset, 'mean'):
            return self.measures['mean'];

        self._check_instance(dataset);

        length = self._length if self._is_equal(dataset) and dataset is not None else len(dataset);

        if length == 0:
            return 0;
        else:
            return sum(dataset)/ length;

    def std_units(self, dataset):
        """ Return standard units converted from the dataset. """

        if self._is_eval(dataset, 'std_units'):
            return self.measures['std_units'];

        self._check_instance(dataset);

        mean = self.mean(dataset);
        std_dev = self.std_dev(dataset);

        return [(value - mean) / std_dev for value in dataset];

    def variance(self, dataset, sample = True):
        """ Return variance taken from the dataset. """
        if self._is_eval(dataset, 'variance'):
            return self.measures['variance'];

        self._check_instance(dataset);

        length = self._length if self._is_equal(dataset) and dataset is not None else len(dataset);
        mean = self.mean(dataset);
        sqrd_errs = list(map(lambda var: (var - mean) ** 2, dataset));

        if sample == True:
            return sum(sqrd_errs) / (length - 1);
        else:
            return sum(sqrd_errs) / length;

    def std_dev(self, dataset, sample = True):
        """ Return standard deviation taken from the dataset. """
        if self._is_eval(dataset, 'std_dev'):
            return self.measures['std_dev'];

        self._check_instance(dataset);
        
        variance = self.variance(dataset, sample);

        return variance ** 0.5;

    def _check_instance(self, dataset):
        if not isinstance(dataset, list):
            raise TypeError('dataset is not a list');

        if not self._check_types(dataset, int, float):
            raise TypeError('some element is not int or float');

    def _check_types(self, items, *args):
        is_any_type = lambda x: any([isinstance(x, y) for y in args])

        return all(map(is_any_type, items))
    
    def _is_eval(self, dataset, descriptor):
        if not self._is_equal(dataset):
            return False;
        
        switch = {
            'mean' :
                self.measures['mean'] is not None,
            'variance' :
                self.measures['variance'] is not None,
            'std_dev' :
                self.measures['std_dev'] is not None,
            'std_units' :
                self.measures['std_units'] is not None,
        }

        return switch[descriptor];

    def _is_equal(self, dataset):
        return dataset == self._dataset;