import glob
import sys
import os

def check(path):
    result_file = open('zip_result.txt', 'w+')
    index = 0
    
    for path, subdirs, files in os.walk(path):
        for name in files:
            index += 1
            x = os.path.join(path, name).replace('\\', '/')
            print(x)
            if not x[2:] in ["zip_all.py", "zip_result"]:
                with open(x) as f:
                    file_ctx = f.read()
                    if file_ctx:
                        result_file.write(f"\n{index}. {x[2:]} ~\n")
                        result_file.write(f"{file_ctx}\n")
    result_file.close()


if __name__=="__main__":
    base_path = './'
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    check(base_path)
