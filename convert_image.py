import os
import argparse


def main(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            new_filename = filename.rsplit('.', 1)[0] + '.png'
            
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="The folder that contain images")
    args = parser.parse_args()
    
    main(args.directory)
