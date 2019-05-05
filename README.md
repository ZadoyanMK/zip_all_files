import glob
import sys
import os
import argparse


def check(path, symbol, is_index):
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
                        if is_index:
                            result_file.write(f"\n{index}. {x[2:]} {symbol}\n")
                        else:
                            result_file.write(f"\n{x[2:]} {symbol}\n")
                        result_file.write(f"{file_ctx}\n")
    result_file.close()


if __name__=="__main__":
    is_index = False
    
    parser = argparse.ArgumentParser(description='Group all file contents to one file.')
    parser.add_argument('--path', '-p', type=str, help='Base path', default='./')
    parser.add_argument('--symb', '-s', type=str, help='Symbol after filename at file', default='~')
    parser.add_argument('--index', '-i', help='Need index to each file?', default=False, action="store_true")
    args = parser.parse_args()

    check(args.path, args.symb, args.index)

