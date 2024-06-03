

import pathlib

import unittest

from quote_engine.ingestor import Importer


PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()


class TestIngestors(unittest.TestCase):
    def setUp(self):
        self.data_root = PROJECT_ROOT / '_data' / 'DogQuotes'
        self.csv_file = self.data_root / 'DogQuotesCSV.csv'

    def test_ingestor_csv(self):
        quote = Importer().parse('_data/DogQuotes/DogQuotesCSV.csv')[0]
        self.assertTrue(quote.body == 'Chase the mailman')
        self.assertTrue(quote.author == 'Skittle')

    def test_ingestor_txt(self):
        quote = Importer().parse('_data/DogQuotes/DogQuotesTXT.txt')[0]
        print('\n', quote.body + '-\n', 'To bork or not to bork-', '\n')
        self.assertTrue(quote.body[1:] == 'To bork or not to bork')
        self.assertTrue(quote.author == 'Bork')


if __name__ == '__main__':
    unittest.main()