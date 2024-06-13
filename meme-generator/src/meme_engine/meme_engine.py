"""Meme generator."""

import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme generator."""

    def __init__(self, output_dir: str):
        """Initialize object."""
        self.output_dir = output_dir

    def prepare_image(self, path: str, width: int) -> Image.Image:
        """Load image and resize."""
        try:
            img = Image.open(path)
        except FileNotFoundError:
            raise Exception(f'File not found {path}, use another filename.')

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        new_size = (width, height)

        img = img.resize(new_size, Image.NEAREST)

        return img

    def include_quote(self, img: Image.Image, quote: str) -> None:
        """Write a quote on the image."""
        draw = ImageDraw.Draw(img)

        font_name = "./fonts/arial.ttf"
        font_size = 20
        font = ImageFont.truetype(font_name, font_size)

        text_bbox = draw.textbbox((0, 0), quote, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        center_x = (img.width - text_width) // 2
        center_y = (img.height - text_height) // 2

        text_x = center_x + random.randint(-100, 100)
        text_y = center_y + random.randint(-100, 100)

        draw.text((text_x , text_y), quote, font=font, fill="white")


    def make_meme(self, img_path: str, text: str, author: str, width: int=500) -> str:
        """Produce the meme and save as an image."""
        quote = f'{text} \n {author}'

        img = self.prepare_image(img_path, width)
        self.include_quote(img, quote)

        tmp_path = f'./tmp/{random.randint(0,100000000)}.jpg'
        img.save(tmp_path)

        return tmp_path


