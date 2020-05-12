import glob, os

chars = 0
lines = 0
for _file in glob.glob('./thesis/**/*.py', recursive=True):
	print(_file)

	text = open(_file).read().strip().split()
	chars = chars + sum(len(word) for word in text)
	lines = lines + sum(1 for line in open(_file))

print('Lines: ' + str(lines))
print('Chars: ' + str(chars))
