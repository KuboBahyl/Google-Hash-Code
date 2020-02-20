def parse_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        n_rows = lines[0]

        collection = []
        for line in lines[1:]:
            val_1, val_2 = line.strip().split(' ')
            # TODO
    return photos