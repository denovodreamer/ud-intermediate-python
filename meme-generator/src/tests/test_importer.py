

import pathlib

import unittest

from quote_engine import CSVImporter, TXTImporter, PDFImporter, DOCXImporter


PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()


class TestIngestors(unittest.TestCase):
    def setUp(self):
        self.data_root = PROJECT_ROOT / '_data' / 'DogQuotes'
        self.csv_file = self.data_root / 'DogQuotesCSV.csv'

    def test_ingestor_csv(self):
        quote = CSVImporter().parse('_data/DogQuotes/DogQuotesCSV.csv')[0]
        self.assertTrue(quote.body == 'Chase the mailman')
        self.assertTrue(quote.author == 'Skittle')

    def test_ingestor_txt(self):
        quote = TXTImporter().parse('_data/DogQuotes/DogQuotesTXT.txt')[0]
        self.assertTrue(quote.body[1:] == 'To bork or not to bork')
        self.assertTrue(quote.author == 'Bork')

    def test_ingestor_docx(self):
        quote = DOCXImporter().parse('_data/DogQuotes/DogQuotesDOCX.docx')[0]
        self.assertTrue(quote.body == 'Bark like no one’s listening')
        self.assertTrue(quote.author == 'Rex')

    def test_ingestor_pdf(self):
        quote = PDFImporter().parse('_data/DogQuotes/DogQuotesPDF.pdf')[0]
        self.assertTrue(quote.body == 'Treat yo self')
        self.assertTrue(quote.author == 'Fluffles')

if __name__ == '__main__':
    unittest.main()