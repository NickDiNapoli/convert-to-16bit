import sys
import os
import argparse
import tifffile
import multiprocessing
import numpy as np

def argument_parser(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", required=True, help="The path to the data source")
    
    return parser.parse_args(args)

def read_write(file_path):
    dtype = np.uint16
    
    img = tifffile.imread(file_path)
    tifffile.imsave(str(file_path), img.astype(dtype))
    
    
def main(args=sys.argv[1:]):
    opts = argument_parser(args)
    path = opts.directory 
    
    with multiprocessing.Pool() as pool:
        pool.map(read_write, [os.path.join(path, filename) for filename in os.listdir(path)])
           
        
if __name__ == "__main__":
    main()

