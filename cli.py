import argparse
from lib import files


def run():
    parser = argparse.ArgumentParser(
        description="A CLI to convert image files to byte arrays"
    )
    parser.add_argument(
        "command", choices=["bytes", "sprites", "resize"], help="Specify the action to perform"
    )
    parser.add_argument("--file", "-f")
    parser.add_argument("--rows", "-r", type=int)
    parser.add_argument("--cols", "-c", type=int)
    parser.add_argument("--width", "-w", type=int)
    parser.add_argument("--height", "-H", type=int)
    args = parser.parse_args()
    cmd = args.command
    file = args.file
    row_sprites = args.rows or 1
    col_sprites = args.cols or 1
    width = args.width or 0
    height = args.height or 0
    if cmd == "bytes":
        files.convert_to_byte_array(file=file)
    elif cmd == "sprites":
        files.convert_sprite_sheet_to_byte_array(
            file=file, row_sprites=row_sprites, column_sprites=col_sprites
        )
    elif cmd == "resize":
        files.resize_image(path=file, size=(width, height))
    else:
        pass


if __name__ == "__main__":
    run()
