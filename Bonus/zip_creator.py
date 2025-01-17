import zipfile
import pathlib


def make_archieve(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip") # creating a variable that keeps path to archieve
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name) #we extract only filename from filepath

if __name__ == "__main__":
    make_archieve(filepaths=["bonus16.py"], dest_dir="dest")