


from typing import List

from .quote_model import QuoteModel
from .import_interface import ImportInterface


class TXTImporter(ImportInterface):
    """Importer for TXT documents."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path, 'r') as file:
            for line in file:
                body, author = line.split(' - ')
                quote = QuoteModel(body.strip(), author.strip())
                quotes.append(quote)

        return quotes