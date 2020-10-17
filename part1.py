import os 
import shutil
import time

file_path = r"C:\Users\HP\Desktop\website"

all_files = set()
all_folders = set()


def create_directory(folder_name):
	if not os.path.exists(f"{os.getcwd()}\\{folder_name}"):
		try:
			os.mkdir(f"{os.getcwd()}\\{folder_name}")
		except Exception as e:print(e)

for parent_folder,child_folders,files in os.walk(file_path):
	all_folders.add(parent_folder)
	for child_folder in child_folders:
		all_folders.add(f"{parent_folder}\\{child_folder}")

	for file in files:
		all_files.add(f"{parent_folder}\\{file}")

# all folders

for all_folder in all_folders:
	if os.path.exists(all_folder) and os.path.isdir(all_folder):
		# print(all_folder)
		pass
	else:print(False)

# all files	

for all_file in all_files:
	if os.path.exists(all_file) and os.path.isfile(all_file):
		try:
			extension_name = all_file.split(".")[len(all_file.split("."))-1]

			# create_directory(extension_name)

			file_name = all_file.split("\\")[len(all_file.split("\\"))-1]
			# shutil.move(all_file, f"{os.getcwd()}\\{extension_name}\\{file_name}")
			
			# print( f"{os.getcwd()}\\{extension_name}\\{file_name}")
			
		except:
			try:
				# create_directory("unknown")

				# shutil.move(all_file, f"{os.getcwd()}\\unknown")
				pass

			except Exception as e:print(all_file,e)

def directory_size(directory):
	if os.path.exists(directory):

		if os.path.isdir(directory):
			total_size_in_bytes = 0

			for parent_folder,child_folders,files in os.walk(directory):

				for file in files:
					total_size_in_bytes+=os.path.getsize(f"{parent_folder}\\{file}")

			return total_size_in_bytes

		elif os.path.isfile(directory):
			return os.path.getsize(directory)
	else:
		return "FileNotFoundError:- directory not found!"

all_folders = sorted(all_folders,key=len,reverse=True)
all_files = sorted(all_files,key=len,reverse=True)


for index,all_file in enumerate(all_files):
	if directory_size(all_file)<=0:os.remove(all_file)

for index,all_folder in enumerate(all_folders):
	if directory_size(all_folder)<1:
		os.rmdir(all_folder)
		print("ds")
