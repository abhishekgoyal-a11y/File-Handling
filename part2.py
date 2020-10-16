import os
import time
def get_no_of_files_folders(directory):
        if os.path.exists(directory):
                if os.path.isdir(directory):
                        all_files = 0
                        all_folders = 0


                        for parent_folder,child_folders,files in os.walk(directory):
                                all_folders+=1
                                for child_folder in child_folders:
                                        all_folders+=1

                                for file in files:
                                        all_files+=1

                        return all_files,all_folders-1
                elif os.path.isfile(directory):
                        return 0,0
        else:
                return "FileNotFoundError:- directory not found!"
print(get_no_of_files_folders("try5.py"))