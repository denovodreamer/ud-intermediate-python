
from typing import List
from abc import ABC, abstractmethod
from .quote_model import QuoteModel


class ImportInterface(ABC):

    allowed_extensions = ['csv', 'pdf', 'txt', 'docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass




import pandas as pd


class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path)

        for _, text in df.iterrows():
            quote = QuoteModel(text['body'], text['author'])
            quotes.append(quote)

        return quotes



class TXTImporter(ImportInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path, 'r') as file:
            for line in file:
                body, author = line.split(' - ')
                quote = QuoteModel(body.strip(), author.strip())
                quotes.append(quote)

        return quotes


class Importer(ImportInterface):
    importers = [CSVImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)


if __name__ == '__main__':
    res = Importer().parse('_data/DogQuotes/DogQuotesTXT.txt')
    print(res[0].body)