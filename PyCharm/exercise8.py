# ========================== oh soldier prettify my folder=======================#
# folder path is given to u
# ek func banao
# func inputs are - path as str, dictionary_file (jo words ko change nai kerna he),file_format
#
# ex def soldier('c://', 'harry.txt', 'jpg')
# agar ye path k ander koi folder hoga toh dont touch it
# harry.txt has all words in small case
# first it will capitalise all files' names
# but if some filename is containing word that is present in harry.txt, do not change that filename
# jpg files ko b rename nai kerna he and jpg ko fol manner me rename kerna he -
# eg fggjdkds.jpg ko rename as 1.jpg, gdyuerefyut.jpg as 2.jpg , rename till 100

# C:\Users\Juilee\PycharmProjects\PythonTuts\THIS

import os


def soldier(take_path, file, file_format):
    n = 1
    path = os.chdir(take_path)   #catch
    f = open(file, "r")
    words = f.read().split('\n')
    print(f"folllowing files/folder names will not be changed: \n{words}")
    f.close()  # this is important

    for item in os.listdir(path):
        if item not in words:
            os.rename(item, item.capitalize())

        if item not in words and os.path.splitext(item)[1] == file_format:  # splittest gives tuple of ('filename', 'extension')
            new_filename2 = f"{n}{file_format}"
            os.rename(item, new_filename2)
            n += 1


if __name__ == '__main__':
    print("enter path where rename work needs to be done!: ")
    take_path = input()  # best to use raw string here = r"", why?- escaping nai krna pdega.
    # literally interpret krega python
    # jer raw str nai ghetli ter path la her ek thikani backslash add krava lagto
    soldier(take_path, 'harry.txt', '.png')
