# Looks for similar java classes and removes duplicates


#subprocess.Popen(["""find""", """ `pwd` -type f -name *.java -printf "%h:%f \n"  > lol"""], cwd=r'/home/andrew/lol')
FILE = "/home/andrew/lol"
from os import remove

def get_file(file):
	with open (file, "r") as myfile:
		list = []
		for line in myfile:
			strip = line.strip()
			if strip:
				list.append(strip)
		return list


def get_end_import_line(lines):
	import_started = False
	current_index = 0
	while True:
		current_index += 1
		if current_index >= len(lines):
			return 0
		# if import section ended
		curren_line_is_import = lines[current_index].startswith('import')
		if curren_line_is_import:
			import_started = True
		if import_started and not curren_line_is_import:
			break
	return current_index

files = {}
with open(FILE) as f:
	for line in f:
		key, value = line.split(":")
		files.setdefault(value.strip(), []).append(key)

files_count = 0
commons = []
for file in files:
	if len(files[file]) > 1:
		file1 = files[file][0] + "/" + file
		file2 = files[file][1] + "/" + file
		all_line_first = get_file(file1)
		all_lines_second = get_file(file2)
		if all_line_first == all_lines_second:
			commons.append(file)
		else:
			print("="*10+file)
			found = 0
			f = get_end_import_line(all_line_first)
			s = get_end_import_line(all_lines_second)
			while f < len(all_line_first) and s < len(all_lines_second):
				if all_line_first[f].replace(" ", "") != all_lines_second[s].replace(" ", ""):
					found = 1
					print(str(f) + all_line_first[f])
					print(str(s) + all_lines_second[s])
				f += 1
				s += 1
			if found == 0:
				commons.append(file)
			else:
				files_count+=1

print(files_count)
print('='*9)


def remove_file(cmn, i):
	i_cmn = files[cmn][i] + "/" + cmn
	if "remove_in_this_folder" in i_cmn:
		print("Removing "+ i_cmn)
		remove(i_cmn)

for cmn in commons:
	# r1 = open(files[cmn][0] + "/" + cmn).readlines()
	# r2 = open(files[cmn][1] + "/" + cmn).readlines()
	# print("".join(difflib.ndiff(r1, r2)))
	remove_file(cmn, 0)
	remove_file(cmn, 1)


