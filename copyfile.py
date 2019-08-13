import sys
import os

def parse_file(path):
	"""
	"""
	fd = open(path)
	i = 0
	spaces = 0
	tabs = 0
	for i,line in enumrate(fd):
		spaces += line.count(' ')
		tabs += line.count('\t')
    fd.close()

    return spaces, tabs, i + 1 

 def main(path):
 	if os.path.exists(path):
 		spaces, tabls, lines = parse_file(path)
 		print('Spaces {}. tabs {}. lines {}.'.format(spaces, tabls, lines))
 		return True
 	else:
 		return False