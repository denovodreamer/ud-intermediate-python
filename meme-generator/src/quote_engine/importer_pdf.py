
import random
import os
import subprocess
from typing import List

from .quote_model import QuoteModel
from .import_interface import ImportInterface



class PDFImporter(ImportInterface):
    """Importer for PDF documents."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        _ = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                body, author = line.split(' - ')
                quote = QuoteModel(body.strip().strip('"'), author.strip())
                quotes.append(quote)

        file_ref.close()
        os.remove(tmp)

        return quotes