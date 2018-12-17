######## Developed by Md Ajraf Rakib #######
import os, sys, glob
import stat
import subprocess
import shutil
from distutils.dir_util import copy_tree

direct_output = subprocess.check_output('which python', shell=True)
head, tail = os.path.split(direct_output)
stext = "#!"+ direct_output + "\n"

py_source_dir = os.listdir(os.getcwd())

for scriptfiles in py_source_dir:
	if scriptfiles.endswith(".py"):
		scriptfile = open(scriptfiles,"r+")
		lines = scriptfile.readlines()
		scriptfile.seek(0,0)
		scriptfile.write(stext)
		for line in lines:
			scriptfile.write(line)
		scriptfile.close()

for pyfiles in py_source_dir:
    if pyfiles.endswith(".py"):
        shutil.copy(pyfiles,head)

        ##### Give Permission ######
        st = os.stat(pyfiles)
    	os.chmod(pyfiles, st.st_mode | stat.S_IRWXU)

for pyfiles in py_source_dir:
    if pyfiles.endswith(".py"):
        os.remove(pyfiles)
    	
#### Get all files from the ocrolib folder #####
ocrolib_source_dir = os.getcwd()+"/ocrolib/"

if not os.path.isdir(head+'/ocrolib'):
	bin_dir = head+"/ocrolib"
	shutil.copytree(ocrolib_source_dir,bin_dir)
else:
	print "Ocrolib Directory Exists"

os.remove(head+"/setup.py")
