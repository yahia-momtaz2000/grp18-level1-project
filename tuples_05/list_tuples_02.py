print('---- program to show list of tuples ------')
ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print(ips_List)
print(type(ips_List))

#  ('192.168.0.22', 'y')
print(ips_List[1])

#  '192.168.0.22'
print(ips_List[1][0])
print('----- loop for each ----- print only ip has ( y )')
for item in ips_List:
    if item[1] == 'y':
        print(item, item[0][-2:] )

print('---- loop index -- print only ip has ( y ) ')
for i in range(len(ips_List)):
    if ips_List[i][1] == 'y':
        print(ips_List[i], ips_List[i][0][-2:])