# INPUT, OUTPUT FUNCS

def read_input(path):
    with open(path, 'r') as f:
        arg1, arg2, arg3 = [int(i) for i in f.readline().split(" ")]

        """
        INPUT PARSING
        """

def write_output(path, *args):
    with open(path, 'w') as f:
        f.write("best output")
        f.write('\n')
