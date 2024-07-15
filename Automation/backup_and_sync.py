import os
import shutil

def main():
  try:
   src="C:\\Users\\codig\\OneDrive\\Documents\\file\\src"
   dest="C:\\Users\\codig\\OneDrive\\Documents\\test\\dest"

   take_backup(src,dest) 
  except Exception as ex:
      print(f"the error is {ex}")
def take_backup(src,dest):
   
    for item in os.listdir(src):
      src_path=os.path.join(src,item)
      if os.path.isfile(src_path) or os.path.islink(src_path):
         dest_path=os.path.join(dest,item)
         if(os.path.exists(dest_path)):
            os.remove(os.path.join(dest,item))
         shutil.copy(src_path,dest_path)
    print("backup done!")






if __name__=="__main__":
    main()    
