# from __future__ import division
# import torch 
# import torch.nn as nn
# import torch.nn.functional as F 
# from torch.autograd import Variable
# import numpy as np

def parse_cfg(cfgfile):
    """
    Takes a configuration file
    
    Returns a list of blocks. Each blocks describes a block in the neural
    network to be built. Block is represented as a dictionary in the list
    
    """
    with open(cfgfile, "r") as f:
        lines = f.readlines()
    lines = [x for x in lines if x != '\n']
    lines = [x for x in lines if len(x) > 0]
    lines = [x for x in lines if x[0] != '#']
    lines = [x.rstrip().lstrip() for x in lines]
    
    block_list = []
    block_dict = {}
    for line in lines:
        if line[0] == '[': # new_block
            if len(block_dict) > 0:
                block_list.append(block_dict)
                block_dict = {}
            block_dict["type"] = line[1:-1].rstrip().lstrip()
        else:
            key , val = line.split('=')
            block_dict[key.rstrip()] = val.lstrip()
        block_list.append(block_dict)
    return block_list



if __name__ == '__main__':
    print(parse_cfg("cfg/yolov3.cfg"))
