from PIL import Image
import numpy as np
import os

def convert_to_byte_array(path: str):
    gif = Image.open(path)
    name = path.replace(".", "_")
    output_path = name + ".h"
    file_content = ""
    
    # Loop over each frame
    for i in range(gif.n_frames):
        gif.seek(i)
        
        frame = gif.copy()

        # Get the size of the image
        width, height = frame.size
        
        # Convert the image data to a byte array
        byte_array = np.array(frame).flatten().tolist()

        print(f"Frame {i}:")
        print(f"Dimensions: {width}x{height}")
        print(f"Size: {len(byte_array)}")
        frame_title = name + "_" + str(i)
        file_content += f"#define {frame_title}_size {len(byte_array)}\n\n"
        file_content += f"const uint8_t {frame_title}[] = {{\n"

        for j in range(len(byte_array)):
            file_content += f"0x{byte_array[j]:02X}"
            if j != len(byte_array) - 1:
                file_content += ", "
                if j % 25 == 0:
                    file_content += "\n"
        file_content +="};\n\n"
    with open(output_path, mode='w') as f:
        f.write(file_content)