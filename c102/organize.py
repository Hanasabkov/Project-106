import os
import shutil

from_dir="/Users/hana.sabkov/Desktop"
to_dir="Desktop/hana"
listofiles=os.listdir(from_dir)

for filename in listofiles:
    name,ext = os.path.splitext(filename)
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + filename                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Image_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Image_Files" + '/' + filename   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        print("path1 " , path1)
        print("path3 ", path3)
        if os.path.exists(path2):
          print("Moving " + filename + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + filename + ".....")
          shutil.move(path1, path3)