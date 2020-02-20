def parse_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        n_books, n_libraries, days = lines[0].strip().split(' ')
        book_scores = lines[1].strip().split(' ')
        libraries = []
        for i in range(int(n_libraries)):
             n_b, p_l, b_p_d = lines[2+i*2].strip().split(' ')
             books = lines[2+i*2].strip().split(' ')
             libraries.append({
                 'n_b':n_b,
                 'p_l':p_l,
                 'b_p_d':b_p_d,
                 'books':books
             })
    return n_books,n_libraries, days ,book_scores, libraries
