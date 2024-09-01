# bytes py

A python CLI for converting files to byte arrays for use in embedded projects

## Usage

```sh
# converts a gif to a series of byte arrays in a C header file
python cli.py bytes --file my_file.gif

# converts a sprite sheet image to a series of byte arrays in a C header file
python cli.py sprites --file my_file.png --rows 4 --cols 5

# resizes a gif or image
python cli.py resize --file my_file.png --width 10 --height 10
```