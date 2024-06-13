
from typing import List

from .quote_model import QuoteModel
from .import_interface import ImportInterface
from .importer_csv import CSVImporter
from .importer_docx import DOCXImporter
from .importer_pdf import PDFImporter
from .importer_txt import TXTImporter


class Importer(ImportInterface):
    """Iterates through all importers for the given file path."""

    importers: List[ImportInterface] = [CSVImporter, TXTImporter, DOCXImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file on the given path."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)