def read_txt_data(filename):
    with open(filename, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data

def sort_txt_data_by_area(data):
    sorted_data = sorted(data, key=lambda x: int(x[1]))
    return sorted_data

def sort_txt_data_by_population(data):
    sorted_data = sorted(data, key=lambda x: int(x[2]))
    return sorted_data
