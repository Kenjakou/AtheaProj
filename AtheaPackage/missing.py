import pandas as pd
from .base import BaseCleaner

class MissingValueCleaner(BaseCleaner):

    def detect_missing(self):
        return self._df.isnull().sum()

    def fill_missing(self, strategy="mean", value=None):
        df = self._df

        if strategy == "mean":
            self._df = df.fillna(df.mean(numeric_only=True))
        elif strategy == "median":
            self._df = df.fillna(df.median(numeric_only=True))
        elif strategy == "mode":
            self._df = df.fillna(df.mode().iloc[0])
        elif strategy == "constant":
            self._df = df.fillna(value)
        else:
            raise ValueError("Invalid strategy")
        
        return self._df

    def drop_missing(self, threshold=0.5):
        missing_ratio = self._df.isnull().mean()
        cols_to_drop = missing_ratio[missing_ratio > threshold].index
        self._df = self._df.drop(columns=cols_to_drop)
        return self._df

    def clean(self):
        """Default behavior: fill missing values using mean."""
        return self.fill_missing(strategy="mean")
