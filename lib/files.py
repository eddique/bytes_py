from lib import gif
def convert_to_byte_array(file: str):
    if file.endswith(".gif"):
        print("converting gif to byte_array")
        gif.convert_to_byte_array(path=file)
    else:
        print("Unimplemented file type")