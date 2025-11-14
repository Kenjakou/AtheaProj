import pandas as pd
from abc import ABC, abstractmethod

class BaseCleaner(ABC):
    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()  # protected (encapsulation)

    def get_data(self):
        return self._df

    @abstractmethod
    def clean(self):
        """Method to be overridden by all subclasses."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(rows={len(self._df)}, cols={len(self._df.columns)})"
