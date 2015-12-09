dir = "src"
to_dir = "dst"
""" find -type f > lol """

with open("%s/lol" % dir) as f:
	content = f.readlines()
	actions = {}
	for line in content:
		line = line.strip()
		rsplit = line.rsplit('/', 1)
		class_name = rsplit[-1].strip()
		path = rsplit[0].strip()
		print("mkdir -p %s/%s " % (to_dir, path))
		print("git mv %s/%s %s/%s" % (dir, line, to_dir, path))
