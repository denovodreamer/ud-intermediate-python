
from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel

class ImportInterface(ABC):
    """Import interface for all importers."""

    allowed_extensions = ['csv', 'pdf', 'txt', 'docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check extension of given path."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        pass