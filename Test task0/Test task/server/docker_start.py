# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:59:17 2021

@author: Flyin
"""

import os

if __name__ == "__main__":
    dir_start = os.path.abspath(os.curdir)
    disk = "cd /" + dir_start[0] + ' ' + dir_start
    #print(disk)
    os.system(disk)
    os.system("docker build -t image-name:server_ubuntu .")
    os.system("docker run --name run_server -p 8080:8080 image-name:server_ubuntu")