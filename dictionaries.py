# Dictionary is to store data in key value pair. Dictionary is a data type.
# duplicates are NOT allowed as a Key in dictionary

my_dic = {
    'name': 'Ganesh',
    'name': 'Bijoy',
    'id': '777',
    'address': 'bangalore',
    'mobile': '23299879',
    'friends': ['hansh','janu','chinu']
}
print('\n Ignoring first key and latest key of name value is ',my_dic['name'] )
print('\n', my_dic)
print('\n', len(my_dic))
print('\n', my_dic['friends'])

x = my_dic['name']
print('\n Variable value from dictionary',x, '\n')