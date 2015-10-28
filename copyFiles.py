import sys
import os
import shutil


#print sys.argv

def walker(src, dest): #copies directory structure of source file to destination folder
	for root, dirs, files in os.walk(src):
		dest_root = dest + ''.join(root.split(sys.argv[1]))
		#print dest_root
		if not os.path.exists(dest_root):
			os.makedirs(dest_root)
			#print 'created dir : '+dest_root 
	
	print '--directory structure copied--'

def copy_files(src_folder, dest_folder):		#copies files from source to destination according to the directory structure
	for root, dirs, files in os.walk(dest_folder):
		for root_item in root :
			src_root = src_folder + ''.join(root_item.split(sys.argv[2]))
			#print 'corr src : '+src_root
			for sroot, sdirs, sfiles in os.walk(src_root):
				#print 'entered source'
				for item in sfiles :
					#print 'entered source files'
					file_sep =  item.split('.')
					if (file_sep[len(file_sep)-1] == 'archive'and file_sep[len(file_sep)-2] == 'log'):
						src_path = os.path.join(sroot, item)
						dest_path = src_path.replace(src_folder, dest_folder)
						#print 'src_path : '+src_path
						#print 'dest_path was : '+dest_path
						shutil.copyfile(src_path, dest_path)
						#print 'copied----'
	print '--all files copied--'

def remove_files(src_folder, dest_folder):
	for root, dirs, files in os.walk(dest_folder):
		for item in files:
			dest_path = os.path.join(root,item)
			src_path = dest_path.replace(dest_folder, src_folder)
			if os.path.exists(src_path):
				os.remove(src_path)
				#print 'deleted : '+src_path
	print '--deleted files from source folder--'


walker(sys.argv[1],sys.argv[2])
copy_files(sys.argv[1],sys.argv[2])
remove_files(sys.argv[1],sys.argv[2])
