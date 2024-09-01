from lib import gif, png

def convert_to_byte_array(file: str):
    if file.endswith(".gif"):
        print("converting gif to byte_array")
        gif.convert_to_byte_array(path=file)
    else:
        print("Unimplemented file type")

def convert_sprite_sheet_to_byte_array(file: str, row_sprites: int = None, column_sprites: int = None):
    if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
        print("converting file to byte_array")
        png.convert_sprite_sheet_to_byte_array(path=file, row_sprites=row_sprites, column_sprites=column_sprites)
    else:
        print("Unimplemented file type")

from PIL import Image

def resize_image(path: str, size: tuple[int, int]):
    png.resize_image(path=path, size=size)