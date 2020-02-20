def parse_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        n_books, n_libraries, days = lines[0].split(' ')
        book_scores = [int(x) for x in lines[1].split(' ')]
        libraries = []
        for i in range(int(n_libraries)):
            n_b, p_l, b_p_d = lines[2 + i * 2].split(' ')
            books = [int(x) for x in lines[2 + i * 2 + 1].split(' ')]
            libraries.append({
                'lib_id': i,
                'n_b': int(n_b),
                'p_l': int(p_l),
                'b_p_d': int(b_p_d),
                'books': [int(x) for x in books]
            })
    return int(n_books), int(n_libraries), int(days), book_scores, libraries
