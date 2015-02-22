#!/usr/bin/env python

import numpy as np
import pandas as pd

from expandas.core.accessor import AccessorMethods, _attach_methods


class DecompositionMethods(AccessorMethods):
    _module_name = 'sklearn.decomposition'

    def fastica(self, *args, **kwargs):
        func = self._module.fastica
        data = self.data
        return_x_mean = kwargs.get('return_X_mean', False)

        if return_x_mean:
            K, W, S, X_mean = func(data.values, *args, **kwargs)
            K = pd.DataFrame(K, index=data.columns)
            W = pd.DataFrame(W)
            S = pd.DataFrame(S, index=data.index)
            return K, W, S, X_mean
        else:
            K, W, S = func(data.values, *args, **kwargs)
            K = pd.DataFrame(K, index=data.columns)
            W = pd.DataFrame(W)
            S = pd.DataFrame(S, index=data.index)
            return K, W, S

    def dict_learning(self, n_components, alpha, *args, **kwargs):
        func = self._module.dict_learning
        data = self.data
        code, dictionary, errors = func(data.values, n_components, alpha, *args, **kwargs)
        code = pd.DataFrame(code, index=data.index)
        dictionary = pd.DataFrame(dictionary, columns=data.columns)
        return code, dictionary, errors

    def dict_learning_online(self, *args, **kwargs):
        func = self._module.dict_learning_online
        data = self.data
        return_code = kwargs.get('return_code', True)
        if return_code:
            code, dictionary = func(data.values, *args, **kwargs)
            code = pd.DataFrame(code, index=data.index)
            dictionary = pd.DataFrame(dictionary, columns=data.columns)
            return code, dictionary
        else:
            dictionary = func(data.values, *args, **kwargs)
            dictionary = pd.DataFrame(dictionary, columns=data.columns)
            return dictionary

    def sparse_encode(self, dictionary, *args, **kwargs):
        func = self._module.sparse_encode
        data = self.data
        code = func(data.values, dictionary, *args, **kwargs)
        code = pd.DataFrame(code, index=data.index)
        return code
