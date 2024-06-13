"""Quote model."""



class QuoteModel:
    """Simple class to represent the quote."""

    def __init__(self, body: str, author: str):
        """Initialize object."""
        self.body = body
        self.author = author

    def __str__(self):
        """Text representation."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Object representation."""
        return f'{self.body} - {self.author}'