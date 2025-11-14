import pandas as pd
import numpy as np
from .base import BaseCleaner

class OutlierCleaner(BaseCleaner):
    
    def detect_outliers(self, method="iqr"):
        df_num = self._df.select_dtypes(include="number")

        if method == "iqr":
            Q1 = df_num.quantile(0.25)
            Q3 = df_num.quantile(0.75)
            IQR = Q3 - Q1
            mask = (df_num < (Q1 - 1.5 * IQR)) | (df_num > (Q3 + 1.5 * IQR))
            return mask
        else:
            raise ValueError("Only 'iqr' supported.")

    def remove_outliers(self, method="iqr"):
        mask = ~self.detect_outliers(method).any(axis=1)
        self._df = self._df[mask]
        return self._df

    def clean(self):
        return self.remove_outliers()
