import re
from os import listdir
from os.path import join

src_dir = '/tmp/icons/'
dst_dir = '/home/andrew/AndroidStudioProjects/SnowHub/app/src/main/res/'

android = [
	'drawable-mdpi',
	'drawable-hdpi',
	'drawable-xhdpi',
	'drawable-xxhdpi',
	'drawable-xxxhdpi'
]

pattern = re.compile(r"^(?P<name>.*?)(?P<res>\d+)(?P<ext>\.\w+)$")

dirs = listdir(src_dir)
for directory in dirs:
	sub_path = src_dir + directory
	img_struct = {}
	l = listdir(sub_path)
	ext = ''
	name = ''
	for image in l:
		match_res = pattern.match(image)
		if not ext:
			ext = match_res.group('ext')
		else:
			assert ext == match_res.group('ext')
		if name:
			assert name == match_res.group('name')
		else:
			name = match_res.group('name')
		img_struct[match_res.group('res')] = join(src_dir, directory, image)
	i = 0
	for k in sorted(img_struct):
		print('cp -i {} {}'.format(img_struct[k], join(dst_dir, android[i], name+ext)))
		i += 1
