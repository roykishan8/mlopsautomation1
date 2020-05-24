programfile = open('/home/roykishan/task3/mlopsautomation1/maincnncode.py','r')	#connecting to the code file
code = programfile.read()				#reading the code file

if 'keras' or 'tensorflow' in code:						#because keras or tensorflow keyword is a cmust have for a dl program
	if 'Conv2D' in code:				#beacuse if a code is of CNN conv2D layer is a must have
		print('CNNcode')
	else:
		print('not CNNcode')
else:
	print('not deep learning model')
