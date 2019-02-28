'''
Usage:
python3 main.py data/example.in out.txt
'''

import sys

files = ["../data/a_example.txt",
         "../data/b_lovely_landscapes.txt",
         "../data/e_shiny_selfies.txt",
         "../data/d_pet_pictures.txt",
         "../data/c_memorable_moments.txt"]

collection_len = 0
photos = []

def find_min(a, b):
    intersection = len(a.intersection(b))
    a_not_b = len(a.difference(b))
    b_not_a = len(b.difference(a))
    return min(intersection, a_not_b, b_not_a)

class Photo:
    def __init__(self, orientation, tag_count, tags):
        self.orientation = orientation
        self.tag_count = tag_count
        self.tags = tags
        self.is_vertical = orientation == 'V'

    def __str__(self):
        return "orientation: {}, tag_count: {}, tags: {}".format(self.orientation, self.tag_count, self.tags)

    def intersection(self, photo):
        return self.tags.intersection(photo.tags)

    def intersection_len(self, photo):
        return len(self.intersection(photo))


def parse_input(file):
    nums = []
    collection = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            # TODO parsing

            if i == 0:
                collection_len = int(line.strip())
                continue

            line_split = str(line).strip().split(' ')
            orientation = line_split[0]
            tag_count = line_split[1]
            tags = set(line_split[2:])
            photo = Photo(orientation=orientation, tag_count=tag_count, tags=tags)
            print(photo)
            photos.append(photo)

    return nums


def write_out(file, data):
    with open(file, 'w') as f:
        for line in data:
            for val in line:
                f.write('{} '.format(val))
            f.write('\n')


if __name__ == '__main__':
    nums = parse_input(files[0])
    write_out(sys.argv[2] if len(sys.argv) > 2 else 'out.txt', nums)
