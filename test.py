import sys
import os
import numpy as np

#print sys.argv

def walker(src, dest):
	for item in os.walk(src):
		#print item[0]
		add = item[0].split(sys.argv[1])
		add_str = ''.join(add)
		dest = dest + add_str
		print dest

		#os.makedirs()

walker(sys.argv[1],sys.argv[2] )
