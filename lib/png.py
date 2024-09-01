from PIL import Image

def convert_sprite_sheet_to_byte_array(path: str, row_sprites: int, column_sprites: int = 1):
    sprite_sheet = Image.open(path)
    name = path.replace(".", "_")
    output_path = name + ".h"
    file_content = "#include <Arduino.h>\n\n"

    total_width, total_height = sprite_sheet.size
    sprite_width = total_width // row_sprites
    sprite_height = total_height // column_sprites

    # Loop over each row and column
    for row in range(row_sprites):
        for col in range(column_sprites):
            # Crop the sprite from the sprite_sheet
            sprite = sprite_sheet.crop((col*sprite_width, row*sprite_height, (col+1)*sprite_width, (row+1)*sprite_height)).convert('RGB')

            file_content += f"#define {name.upper()}_WIDTH {sprite_width}\n"
            file_content += f"#define {name.upper()}_HEIGHT {sprite_height}\n\n"

            # Convert the image data to a 16-bit RGB565 byte array
            byte_array = []
            for y in range(sprite_height):
                for x in range(sprite_width):
                    r, g, b = sprite.getpixel((x, y))
                    rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                    byte_array.append(rgb565)

            sprite_title = name + "_" + str(row) + "_" + str(col)
            file_content += f"const uint16_t {sprite_title}[] PROGMEM = {{\n"

            for j in range(len(byte_array)):
                file_content += f"0x{byte_array[j]:04X}"
                if j != len(byte_array) - 1:
                    file_content += ", "
                    if j % 10 == 9:
                        file_content += "\n"
            file_content +="};\n\n"
    
    with open(output_path, mode='w') as f:
        f.write(file_content)

def resize_image(path: str, size: tuple[int, int]):
    ouput_path = path.split(".")[0] + "_resized" + path.split(".")[-1]
    original_image = Image.open(path)
    width, height = original_image.size
    
    if (width, height) != size:
        resized_image = original_image.resize(size)
        resized_image.save(ouput_path)
    else:
        original_image.save(ouput_path)