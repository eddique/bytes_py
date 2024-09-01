import argparse
from lib import files

def run():
    parser = argparse.ArgumentParser(description='A CLI to convert image files to byte arrays')
    parser.add_argument('command', choices=['bytes'], help='Specify the action to perform')
    parser.add_argument('--file', '-f')
    args = parser.parse_args()
    cmd = args.command
    file = args.file
    if cmd == "bytes":
        files.convert_to_byte_array(file=file)
    else:
        pass
if __name__ == "__main__":
    run()