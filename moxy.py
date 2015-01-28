import re
import sys

package = 'package'

__author__ = 'andrew'

if __name__ == "__main__":
    arg_count = len(sys.argv)-1
    if arg_count == 0:
        print("provide output of ls ./package/")
    else:
        for arg in range(1, arg_count+1):
            p = re.compile(r'(.*)\.java')
            a = re.search(p, sys.argv[arg])

            print('''%s.%s''' % (package, a.group(1)))