from PIL import Image
import numpy as np
import os

def convert_to_byte_array(path: str):
    gif = Image.open(path)
    name = path.replace(".", "_")
    output_path = name + ".h"
    file_content = "#include <Arduino.h>\n\n"
    
    # Loop over each frame
    for i in range(gif.n_frames):
        gif.seek(i)
        
        frame = gif.copy().convert('RGB')

        # Get the size of the image
        width, height = frame.size
        file_content += f"#define {name.upper()}_WIDTH {width}\n"
        file_content += f"#define {name.upper()}_HEIGHT {height}\n\n"

        # Convert the image data to a 16-bit RGB565 byte array
        byte_array = []
        for y in range(height):
            for x in range(width):
                r, g, b = frame.getpixel((x, y))
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                byte_array.append(rgb565)

        frame_title = name + "_" + str(i)
        file_content += f"const uint16_t {frame_title}[] PROGMEM = {{\n"

        for j in range(len(byte_array)):
            file_content += f"0x{byte_array[j]:04X}"
            if j != len(byte_array) - 1:
                file_content += ", "
                if j % 10 == 9:
                    file_content += "\n"
        file_content +="};\n\n"
    
    with open(output_path, mode='w') as f:
        f.write(file_content)