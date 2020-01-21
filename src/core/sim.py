'''
    problem/
        active/
        paused/
        finished/
        discarded/
        failed/

'''

import importlib
import sys
import os
import argparse
import glob

from model import Model
from runner import Runner

def print_help():
    print ("python3 sim.py app_module [-i <input_file>] [-d <working_dir>] [-n <beam_width>] [-k <kb_file>]")

def main():

    if len(sys.argv) < 2:
        print_help()
        exit(1)

    # parse argments

    # prepare the folder

    # create model
    app_module = sys.argv[1]
    input_file = ""
    kb_file = ""
    beam_width = 100
    module = importlib.import_module(app_module)
    model = module.create_model(model, input_file)
    model.save("active/1.model")

    while True:

        while len(glob.glob("active/*.model")) > 0:
            model_file = glob.glob("active/*.model")[1]
            r = Runner(model_file, kb_file)
            r.run()

        # if paused is not empty:
        if len(glob.glob("paused/*.model")) > 0:
            # measure and filter the paused
            # move them to active
            # continue

        # if finished is not empty:
        if len(glob.glob("finished/*.model")) > beam_width:
            print ("Done")
            break

        # move N discarded into active
            # continue

if __name__ == '__main__':
    main()
