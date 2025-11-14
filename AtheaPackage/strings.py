import pandas as pd
import string
from .base import BaseCleaner

class StringCleaner(BaseCleaner):

    def strip_whitespace(self):
        df = self._df.select_dtypes(include="object")
        self._df[df.columns] = df.apply(lambda col: col.str.strip())
        return self._df

    def normalize_case(self, case="lower"):
        df = self._df.select_dtypes(include="object")

        if case == "lower":
            self._df[df.columns] = df.apply(lambda col: col.str.lower())
        elif case == "upper":
            self._df[df.columns] = df.apply(lambda col: col.str.upper())
        
        return self._df

    def remove_punctuation(self):
        df = self._df.select_dtypes(include="object")
        table = str.maketrans("", "", string.punctuation)
        self._df[df.columns] = df.apply(lambda col: col.str.translate(table))
        return self._df

    def clean(self):
        self.strip_whitespace()
        self.normalize_case()
        return self._df
