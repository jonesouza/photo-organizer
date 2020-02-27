# Photo Organizer

Photo Organizer is a program to move/copy your photos organizing by date.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  set the orign path from image files
  -e EXIT, --exit EXIT  set the exit path from image files
  -x [EXT [EXT ...]], --ext [EXT [EXT ...]]
                        set image extensions whitelist. EX.: png jpg (its
                        works just image extensions)
  -f [FILES [FILES ...]], --files [FILES [FILES ...]]
                        set specific images to move. EX.: 1.png 2.jpg 3.gif
  -l, --list            just list images dont move
  -v, --verbose         Allow verbose mode
  -c, --copy            Allow copy mode
  --version             Show Version

if path and exit it is not specified they are the current directory

# Example

**Copyng**
pyhton photo-organizer.py -c -p /home/user/images -e /home/pictures

**Moving** pyhton photo-organizer.py -p /home/user/images -e /home/pictures
