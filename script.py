def read_txt_data(filename):
    with open(filename, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data

