
from typing import List

from .quote_model import QuoteModel
from .import_interface import ImportInterface


class CSVImporter(ImportInterface):
    """Importer for CSV documents."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        import pandas as pd

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path)

        for _, text in df.iterrows():
            quote = QuoteModel(text['body'], text['author'])
            quotes.append(quote)

        return quotes
