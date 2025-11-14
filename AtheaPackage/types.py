import pandas as pd
from .base import BaseCleaner

class TypeCleaner(BaseCleaner):

    def to_numeric(self, cols):
        for col in cols:
            self._df[col] = pd.to_numeric(self._df[col], errors="coerce")
        return self._df

    def to_datetime(self, cols):
        for col in cols:
            self._df[col] = pd.to_datetime(self._df[col], errors="coerce")
        return self._df

    def clean(self):
        """Default behavior: do nothing to avoid forced conversions."""
        return self._df
