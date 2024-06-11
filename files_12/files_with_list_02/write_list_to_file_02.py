# program to write list into a file

cities_list = ['Cairo', 'Alex', 'Mansoura', 'Luxor']

with open('C:\\my_files\\write_cities.txt', 'w') as f:
    for i in range(len(cities_list)):
        if i == len(cities_list) - 1: # here the last city
            f.write(cities_list[i])
        else:
            f.write(cities_list[i]+'\n')
