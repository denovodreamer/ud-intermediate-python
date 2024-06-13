

from typing import List
import docx

from .quote_model import QuoteModel
from .import_interface import ImportInterface


class DOCXImporter(ImportInterface):
    """Importer for DOCX documents."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(' - ')
                quote = QuoteModel(body.strip().strip('"'), author.strip())
                quotes.append(quote)

        return quotes