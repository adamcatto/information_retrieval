import os
import itertools

from tqdm import tqdm


def get_files(in_dir, file_extensions):
	if isinstance(file_extensions, str):
		file_extensions = [file_extensions]

	for i, f in enumerate(file_extensions):
		if f[0] == '.':
			file_extensions[i] = f[1:]
	print(file_extensions)
	files = []
	for path, subdirs, filenames in os.walk(in_dir):
		for f in filenames:
			if f.rsplit('.', 1)[-1] in file_extensions:
				files.append(os.path.join(path, f))

	return files


def tokenize(in_dir, file_extensions):
	tokens = []
	#to_split_on = '.,()[]:#*<>?!&%$#\n '
	to_split_on = ['.', ',', '(', ')', '[', ']', '/ ', '\ ', ':', '#', '?', '!', '&', '%', '$', ' ', '//', '\n']
	files = get_files(in_dir, file_extensions)
	print(files)
	for _, filename in tqdm(enumerate(files)):
		with open(filename, 'r') as f:
			for x in f.readlines():
				x = [x]
				for s in to_split_on:
					for i, item in enumerate(x):
						x[i] = item.split(s)
					x = list(itertools.chain(*x))
			tokens += x
	tokens = set([x.lower() for x in tokens])
	return tokens


tokens = tokenize(in_dir='../', file_extensions='.md')
print(tokens)

