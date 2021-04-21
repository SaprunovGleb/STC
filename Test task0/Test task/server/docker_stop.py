# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:57:47 2021

@author: Flyin
"""

import os

if __name__ == "__main__":
    os.system("docker stop run_server")
    os.system("docker rm  run_server")