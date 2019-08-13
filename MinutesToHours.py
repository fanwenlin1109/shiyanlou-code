import sys

def Hours(minute):
	if(minute <0):
		raise ValueError('Input number is less than zero')
	else:
		print('{} H, {} M'.format(minute // 60, minute % 60))

try:
	for p in enumerate(sys.argv):
		print('paramter {}'.format(p))

	print('int = {}'.format(sys.argv[1]))
	Hours(int(sys.argv[1]))
except:
	print('Parameter Error')