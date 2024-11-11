def read_data(file_name):

    text_file = open(file_name).read().splitlines()
    data = []

    for line in text_file:
        
        data.append(int(line))

    domain = set(data)
    domain_size = len(domain)

    return data, domain_size


