__author__ = 'andrew'
import re
import sys

package = '/home/andrew/work/java-package'

if __name__ == "__main__":
    p =re.compile(r'"(\w+)"')
    p1 = re.compile(r'propOrder')
    files_count = len(sys.argv)-1
    if files_count == 0:
        print("change package variable to your dir and pass output of `ls /directory`, for example `python3 prop_order_to_xml.py A.java B.java`")
    else:
        for file in range(1, files_count+1):
            with open(package+sys.argv[file], 'r') as f:
                content = f.readlines()
                for line in content:
                    a = re.search(p1, line)
                    if a is not None:
                        b = re.findall(p, line)
                        print('file: %s \n <xml-type prop-order="%s"/>' % (sys.argv[file], ' '.join(b)))

