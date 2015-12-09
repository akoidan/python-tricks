print("run this command in your git repo 'git status > lol7'")
print("CAUTION!!! It wil execute 'git reset' in the middle!!!!")
merge_only = "SKIP_THIS_PATH"

with open("/tmp/base/lol7") as f:
	content = f.readlines()
	actions = {}
	for line in content:
		if ":" not in line:
			continue
		action, dst = line.split(":")
		rsplit = dst.rsplit('/', 1)
		class_name = rsplit[-1].strip()
		path = rsplit[0].strip()
		if path.startswith(merge_only):
			continue
		if "new file" in action:
			actions.setdefault(class_name, {})['to'] = path
		elif "deleted" in action:
			actions.setdefault(class_name, {})['from'] = path
		# print(class_name)
	for action in actions:
		value = actions[action]
		if "from" in value and "to" in value:
			print("mkdir -p %s" % value['from'])
			print("mv %s/%s %s/%s" % (value['to'],action, value['from'], action))

	print('git reset')
	for action in actions:
		value = actions[action]
		if "from" in value and "to" in value:
			print("git mv %s/%s %s/%s" % (value['from'],action, value['to'], action))
