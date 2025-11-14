import pandas as pd
from .base import BaseCleaner

class DuplicateCleaner(BaseCleaner):

    def find_duplicates(self):
        return self._df[self._df.duplicated()]

    def remove_duplicates(self, keep="first"):
        self._df = self._df.drop_duplicates(keep=keep)
        return self._df

    def clean(self):
        return self.remove_duplicates()
