import random
import os
import requests
import pathlib
from flask import Flask, render_template, request

from quote_engine import Importer
from meme_engine import MemeEngine


PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
print(PROJECT_ROOT)


app = Flask(__name__)

meme = MemeEngine('./static')




def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Importer.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, image) for image in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img_path = random.choice(imgs)
    quote = random.choice(quotes)

    print(img_path)
    meme_img_path = meme.make_meme(img_path, quote.body, quote.author)

    meme_img_path = pathlib.Path(meme_img_path)
    print(meme_img_path)

    return render_template('meme.html', path=meme_img_path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_path = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    img = requests.get(img_path)

    tmp_path = f'./tmp/{random.randint(0,100000000)}.jpg'
    with open(tmp_path, 'wb') as file:
        file.write(img.content)

    path = meme.make_meme(tmp_path, body, author)

    os.remove(tmp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(port=5002)
