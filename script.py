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

def print_data(data):
    for row in data:
        print(row)

data = read_txt_data('population.txt')


sorted_by_area = sort_txt_data_by_area(data)
print('Країни,відсортовані за площею у порядку зростання:')
print_data(sorted_by_area)

sorted_by_population = sort_txt_data_by_population(data)
print('Країни,відсортовані за населенням у порядку зростання:')
print_data(sorted_by_population)