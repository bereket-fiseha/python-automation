import os
import shutil
def move_file(sub_folder,path1,path2):
    if not os.path.exists(sub_folder):
                  os.mkdir(sub_folder)
                  print(f"created sub forder {sub_folder}")
            
    shutil.move(path1,path2)
    print(f"moved file from to path {path2}")
def move_dir(sub_folder,main_folder):
      new_folder=os.path.join(main_folder,"all_folders")
      if(not os.path.exists(new_folder)):
               os.mkdir(new_folder)
      shutil.move(sub_folder,new_folder)         
def clean_dir(folder):
   for dest in os.listdir(folder):
       dest_path=os.path.join(folder,dest)
       if os.path.isdir(dest_path):
             print(dest_path)
             move_dir(dest_path,folder)   
       if os.path.isfile(dest_path) or os.path.islink(dest_path):
             print(os.path.join(folder,dest))
             ext= dest.split(".")[-1]
             sub_folder=os.path.join(folder,ext)
             #full path folder + file
             folder_path=os.path.join(folder,dest)
                #full path sub folder + file
             sub_folder_path=os.path.join(sub_folder,dest)
             move_file(sub_folder,folder_path,sub_folder_path)
             

def main():
    path= "C:\\Users\\codig\\OneDrive\\Desktop"
    try:
     if os.path.isdir(path):
         clean_dir(path)
         #os.close(path)
     else:
        print("not directory")      
    except FileNotFoundError as nf:
        print(nf.strerror())     

if __name__ =="__main__":
      main()        