from copy import copy
from math import ceil

from helpers import parse_input


def get_best_books_for_lib(lib, n_days_left, modified_book_scores):
    if n_days_left <= lib['p_l']:
        return [], lib['p_l'], 0
    books_scored = sorted(
        list(zip(lib['books'], [modified_book_scores[y] for y in lib['books']])),
        key=lambda x: x[1], reverse=True)
    b_books = books_scored[:int(ceil((n_days_left - lib['p_l']) * lib['b_p_d'])) + 1]
    if int(ceil((n_days_left - lib['p_l']) * lib['b_p_d'])) > len(books_scored):
        days_unused = n_days_left - (len(b_books) / lib['b_p_d']) - lib['p_l']
    else:
        days_unused = 0
    return b_books, lib['p_l'], days_unused


def get_score_for_lib(lib, n_days, modified_book_scores):
    if lib is not None:
        b_books, p_l, days_unused = get_best_books_for_lib(lib, n_days, modified_book_scores)
        s = sum([x[1] for x in b_books]) / (p_l * p_l) / (n_days + days_unused * 2)
        return s, b_books, lib['lib_id']
    else:
        return 0, [], None


def get_next_best(libraries_left, n_days_left, modified_book_scores):
    best_lib = \
        max([get_score_for_lib(x, n_days_left, modified_book_scores) for x in libraries_left], key=lambda y: y[0])

    modified_book_scores = [x if i not in [y[0] for y in best_lib[1]] else 0 for i, x in
                            enumerate(modified_book_scores)]
    libraries_left = [x if x is not None and x.get('lib_id') != best_lib[2] else None for x in libraries_left]
    return best_lib, modified_book_scores, libraries_left


def get_best_sequence(libraries, n_days, book_scores):
    seq = []
    libraries_left = copy(libraries)
    modified_book_scores = copy(book_scores)
    while n_days > 0 and len([x for x in libraries_left if x is not None]) > 0:
        # print(n_days)
        best_lib, modified_book_scores, libraries_left = get_next_best(libraries_left, n_days, modified_book_scores)
        if len(best_lib[1]) > 0:
            seq.append(best_lib)
        n_days -= libraries[best_lib[2]]['p_l']
    return seq


def write_out(seq, file_name):
    with open('out/' + file_name, 'w') as f:
        f.write('{}\n'.format(str(len(seq))))
        for i in seq:
            f.write('{} {}\n'.format(str(i[2]), str(len(i[1]))))
            f.write(' '.join([str(x[0]) for x in i[1]]) + '\n')


def compute(path):
    n_books, n_libraries, days, book_scores, libraries = parse_input(path)
    best_seq = get_best_sequence(libraries, days, book_scores)
    print(len(best_seq))
    print(best_seq)
    write_out(best_seq, path)


input_file = 'data/e_so_many_books.txt'
print(input_file)
compute(input_file)
