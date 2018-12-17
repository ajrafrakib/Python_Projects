### Developed by Md Ajraf Rakib ###
import urllib2
import glob, os, sys, os.path
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-htmld", "--html_path", required=True, help="path where groundtruth files(.gt.pf.png) are stored.")
parser.add_argument("-txtd", "--txt_path", required=True, help="path where groundtruth files(.gt.pf.png) are stored.")

args = parser.parse_args()
log_filename = "temp.txt"

for file in sorted(glob.glob(os.path.join(args.html_path,"*.html"))):
	filename, fileExtension = os.path.splitext(file)
	name = os.path.basename(file).split('.')[0]
	print args.html_path+ name + fileExtension
	f = open(filename + fileExtension,'r')
	soup = BeautifulSoup(f, "lxml")
	f.close()
	fw = open (os.path.join(args.html_path,log_filename),'w')
	fw.write(soup.get_text().encode('utf-8'))
	fw.close()
	title=1

	with open(os.path.join(args.html_path,log_filename),'r') as f:
		fw = open(os.path.join(args.txt_path,name + ".txt"),'w+')

		for i in f:
			if (i !="\n") and (i !=" \n") and (i !=" \t\n") and (i !=" \t\n\r"):
				if title==0: fw.write(i)
				title=0

	fw.close()
	f.close()
	#os.remove("temp.txt")
	os.system("rm " + os.path.join(args.html_path,log_filename))
	print  'Converted To->', args.txt_path+name+'.txt'
print "Process Complete !!!"
