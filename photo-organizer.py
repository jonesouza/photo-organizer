#!/usr/bin/python

import os
import shutil
import argparse
from datetime import datetime
from PIL import Image

VERSION = '0.1.0 DEV'

image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
#vector_extensions = ["eps", "ai", "pdf"]

config = {
    'path': '.',
    'exit': '.',
    'extensions': image_extensions,
    'verbose': True,
    'files': '*',
    'list': False,
    'copy': False
}

def version():
    print(VERSION)

def count_file(files):
    return len(files)


def get_metadata(file):
    path_file = config["path"] +'/'+ file
    
    photo = Image.open(path_file)
    info = photo._getexif()
    date = datetime.fromtimestamp(os.path.getmtime(path_file))
    if info:
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    return date


def list_files():

    if(config['files'] == '*'):
        files = os.listdir(config['path'])
    else:
        files = config['files']

    photos = [
        filename for filename in files if any(filename.endswith(ext) for ext in config['extensions'])
    ]

    return photos

def show_files(files):
    print 'Showing Files:'
    for filename in files:
        print(filename)

def get_new_path(file):
    date = get_metadata(file)
    return date.strftime('%Y') + '/' + date.strftime('%m') + '/' + date.strftime('%d')

def move_files(files):

    filecurrent = 1
    fileend = count_file(files)

    for filename in files:
        old_path = config["path"] +'/'+ filename
        new_path = config["exit"] +'/'+ get_new_path(filename)

        if not os.path.exists(new_path):
            #os.makedirs(new_path)
            if(config['verbose']):
                print 'creating', new_path, 'path'

        if not config['copy']:
            #shutil.move(old_path, new_path + '/' + filename)
            if(config['verbose']):
                print 'moving', filecurrent, 'of', fileend, 'FROM', old_path, 'TO', new_path
        else:
            #shutil.copy(old_path, new_path + '/' + filename)
            if(config['verbose']):
                print 'coping', filecurrent, 'of', fileend, 'FROM', old_path, 'TO', new_path
        
        filecurrent = filecurrent + 1

def set_args(args):
    config['path'] = args.path
    config['exit'] = args.exit
    config['extensions'] = args.ext
    config['verbose'] = args.verbose
    config['files'] = args.files
    config['list'] = args.list
    config['copy'] = args.copy


def main():
    
    parser = argparse.ArgumentParser(description='Config params')
    parser.add_argument('-p', '--path',  help='set the orign path from image files', default='.')
    parser.add_argument('-e', '--exit',  help='set the exit path from image files', default='.')
    parser.add_argument('-x', '--ext', nargs='*', help='set image extensions whitelist. EX.: png jpg (its works just image extensions)', default=image_extensions)
    parser.add_argument('-f', '--files', nargs='*', help='set specific images to move. EX.: 1.png 2.jpg 3.gif', default='*')
    parser.add_argument('-l', '--list',  action='store_true', help='just list images dont move', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='Allow verbose mode', default=False)
    parser.add_argument('-c', '--copy', action='store_true', help='Allow copy mode', default=False)
    parser.add_argument('--version', action='store_true', help='Show Version', dest=version())
    
    args = parser.parse_args()

    set_args(args)

    if(config['list']):
        show_files(list_files())
    else:
        move_files(list_files())

if __name__ == '__main__':
    main()