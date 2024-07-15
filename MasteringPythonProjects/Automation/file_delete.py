#delete a file in a folder with specific size  > given_size

import os
try:

 os.chdir("C:\\Users\\codig\\OneDrive\\Documents\\Documents\\Read\\Codigo\\ptyhon\\videos")
 given_size=88
 for file in os.listdir():
    if file.endswith('.txt'):
        os.remove(file)
        print(f"deleted file {file}!")
except Exception as ex:
       print(f"the exeception is{ex}")