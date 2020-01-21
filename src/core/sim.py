import importlib
import sys
import os
import argparse
import glob

from runner import Runner

'''
    problem/
        active/
        paused/
        done/
        discarded/
        failed/
'''
def prepare_folders(directory):
    directory = os.path.expanduser(directory)
    print(f"preparing problem directory: {directory}")
    if not os.path.isdir(directory):
        os.makedirs(directory)
    next_id = 1
    next_id_file = os.path.join(directory, "next_id")
    if os.path.isfile(next_id_file):
        next_id = int(open(next_id_file).read())
    with open(next_id_file, 'w') as f:
        f.write(f"{next_id+1}")
    working_dir = os.path.join(directory, f"sim_{next_id}")
    for sub_dir in ['active', 'paused', 'done', 'discarded', 'failed']:
        os.makedirs(os.path.join(working_dir, sub_dir))
    return working_dir

def main():

    # parse argments
    parser = argparse.ArgumentParser(description='Simulation Based Learning and Search')
    parser.add_argument('app_module', help='the module name of the application')
    parser.add_argument('-d', '--directory', default='~/.sbls', help='working directory')
    parser.add_argument('-i', '--input', default='input.dat', help='input file name')
    parser.add_argument('-n', '--beam_width', default='1024', help='the beam width (the max of number of simulations)')
    parser.add_argument('-k', '--kb', default='trained.kb', help='the knowledge base file')
    args = parser.parse_args()

    # prepare the folder
    working_dir = prepare_folders(args.directory)
    print(f"Working directory: {working_dir}")

    # create model
    module = importlib.import_module(args.app_module)
    model = module.create_model(args.input, args.beam_width)
    if not model:
        print ("Fail to create the model")
        exit(1)
    model.save(os.path.join(working_dir, "active", "1.model")

    while True:

        while len(glob.glob("active/*.model")) > 0:
            model_file = glob.glob("active/*.model")[1]
            r = Runner(model_file, kb_file)
            r.run()

        # if paused is not empty:
        if len(glob.glob("paused/*.model")) > 0:
            pass
            # measure and filter the paused
            # move them to active
            # continue

        # if finished is not empty:
        if len(glob.glob("finished/*.model")) > int(args.beam_width):
            print ("Done")
            break

        # move N discarded into active
            # continue

if __name__ == '__main__':
    dir_name = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(os.path.join(dir_name, "core"))
    sys.path.append(os.path.join(dir_name, "applications"))
    main()

