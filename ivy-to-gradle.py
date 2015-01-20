__author__ = 'andrew'
import re
import sys

def get_conf(conf):
    try:
        return {
            'default': 'compile',
            'runtime': 'compile',
            'test': 'testCompile',
            'compile': 'compile',
        }[conf]
    except KeyError as e:
        return None



if __name__ == "__main__":
    p = re.compile(r'<dependency(?=.*org="([.\-a-z0-9]+)")(?=.*name="([.\-a-z0-9]+)")(?=.*rev="([.\-a-z0-9]+))(?=.*conf="([.a-z0-9]+).*)')
    files_count = len(sys.argv)-1
    if files_count == 0:
        print("Pass files as parameters example `python3 converter.py ../lol/ivy.xml`")
    else:
        for file in range(1, files_count+1):
            with open(sys.argv[file], 'r') as f:
                print('Parsing file %s\n dependencies {\n ' % f.name)
                content = f.readlines()
                for line in content:
                    a = re.search(p, line)
                    if a is not None:
                        if get_conf(a.group(4)) is not None:
                            print("    %s \"%s:%s:%s\"" % (get_conf(a.group(4)), a.group(1), a.group(2), a.group(3)))
                        else:
                            print("    %s \"%s:%s:%s\"" % ('compile', a.group(1), a.group(2), a.group(3)))
                            print("can't parse line because of unknown conf" + line)
                print('\n}')