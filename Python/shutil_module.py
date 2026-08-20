import shutil
import os
shutil.copy("main.py", "main2.py")

shutil.copytree("__pychas__","myfile.txt")
shutil.move(".tutorial/file.file","file.file/file.file")
shutil.rmtree("file.file")
shutil