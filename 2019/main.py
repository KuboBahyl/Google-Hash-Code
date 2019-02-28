'''
Usage:
python3 main.py data/example.in out.txt
'''

import sys
from tqdm import tqdm

# Data
files = ["../data/a_example.txt",
         "../data/b_lovely_landscapes.txt",
         "../data/c_memorable_moments.txt",
         "../data/d_pet_pictures.txt",
         "../data/e_shiny_selfies.txt"]

# Global variables
photos_len = 0
photos = []

# Classes
class Photo:
    def __init__(self, id, orientation, tag_count, tags):
        self.id = id
        self.orientation = orientation
        self.tag_count = tag_count
        self.tags = tags
        self.is_vertical = orientation == 'V'

    def __str__(self):
        return "id: {}, orientation: {}, tag_count: {}, tags: {}".format(self.id, self.orientation, self.tag_count, self.tags)

    # def __eq__(self, photo):
    #     return self.id == photo.id

    def intersection(self, photo):
        return self.tags.intersection(photo.tags)

    def intersection_len(self, photo):
        return len(self.intersection(photo))

# Functions
def find_min(a, b):
    intersection = len(a.intersection(b))
    a_not_b = len(a.difference(b))
    b_not_a = len(b.difference(a))
    return min(intersection, a_not_b, b_not_a)

def parse_input(file):
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            # TODO parsing

            if i == 0:
                global photos_len
                photos_len = int(line.strip())
                continue

            line_split = str(line).strip().split(' ')
            orientation = line_split[0]
            tag_count = line_split[1]
            tags = set(line_split[2:])
            photo = Photo(id=i-1, orientation=orientation, tag_count=tag_count, tags=tags)
            photos.append(photo)
    return photos


def write_out(file, slideshow):
    sli_len = 0
    is_vert = False
    for photo in slideshow:
        if photo.is_vertical:
            if is_vert:
                is_vert = False
                sli_len += 1
            else:
                is_vert = True
        else:
            sli_len += 1


    with open(file, 'w') as f:
        f.write('{}\n'.format(sli_len))

        is_vert = False
        for i, photo in enumerate(slideshow):
            f.write('{}'.format(photo.id))
            if photo.is_vertical:
                if is_vert:
                    f.write('\n'.format(photo.id))
                    is_vert = False
                else:
                    f.write(' '.format(photo.id))
                    is_vert = True
            else:
                if i == len(slideshow) - 1:
                    continue
                else:
                    f.write('\n'.format(photo.id))


def greedy(photos):
    best_1 = None
    best_2 = None
    best_score = 0
    score = 0
    for photo1 in photos:
        for photo2 in photos:
            score_temp = find_min(photo1.tags, photo2.tags)
            if score_temp > best_score:
                best_score = score_temp
                best_1 = photo1
                best_2 = photo2
    # best_1 = photos[0]
    # best_2 = photos[1]
    # best_score = find_min(best_1.tags, best_2.tags)

    slideshow = [best_1, best_2]
    score += best_score

    best_left = 0
    best_right = 0
    best_left_photo = None
    best_right_photo = None

    if slideshow[0].is_vertical:
        is_left_vert = True
    else:
        is_left_vert = False

    if slideshow[1].is_vertical:
        is_right_vert = True
    else:
        is_right_vert = False

    used_inds = set([best_1.id, best_2.id])

    for i in tqdm(range(photos_len)):
        # print('slideshow')
        # print(is_left_vert)
        # for photo in slideshow:
        #     print(photo)

        for photo in photos:
            if photo.id not in used_inds:

                # left
                if (is_left_vert and photo.is_vertical) or not is_left_vert:
                    score_temp = find_min(photo.tags, slideshow[0].tags)
                    if score_temp > best_left:
                        best_left = score_temp
                        best_left_photo = photo

                # right
                if (is_right_vert and photo.is_vertical) or not is_right_vert:
                    score_temp = find_min(photo.tags, slideshow[-1].tags)
                    if score_temp > best_right:
                        best_right = score_temp
                        best_right_photo = photo

        if best_right >= best_left and best_right_photo:
            slideshow.append(best_right_photo)
            score += best_right
            used_inds.add(best_right_photo.id)
            if best_right_photo.is_vertical:
                if is_right_vert:
                    is_right_vert = False
                else:
                    is_right_vert = True

        elif best_left_photo:
            slideshow.insert(0, best_left_photo)
            score += best_left
            used_inds.add(best_left_photo.id)
            if best_left_photo.is_vertical:
                if is_left_vert:
                    is_left_vert = False
                else:
                    is_left_vert = True

        best_left = 0
        best_right = 0
        best_left_photo = None
        best_right_photo = None


    if is_left_vert:
        slideshow = slideshow[1:]
    if is_right_vert:
        slideshow = slideshow[:-1]

    return slideshow, score

if __name__ == '__main__':
    photos = parse_input(files[2])
    # horizontal = [photo for photo in photos if not photo.is_vertical]
    #
    # slideshow_hor, score = greedy(horizontal)
    #
    # vertical = [photo for photo in photos if photo.is_vertical]
    # slideshow_ver, score = greedy(vertical)

    slideshow, score = greedy(photos)
    for photo in slideshow:
        print(photo)

    print(score)
    write_out(sys.argv[1], slideshow)
