# INPUT, OUTPUT FUNCS

def read_input(path):
    with open(path, 'r') as f:
        line1 = f.readline().split(" ")
        line2 = f.readline().split(" ")

        """
        INPUT PARSING
        """

def write_output(path, *args):
    with open(path, 'w') as f:
        f.write("best output")
        f.write('\n')
