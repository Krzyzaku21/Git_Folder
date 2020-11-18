#ZAD1
#Dodawanie wartości dict
def met_add_dict_values1():
    options = {
    'env' : 'production',
    'db' : 'mysql',
    'version' : 1.0,
    'show_errors' : True
    }
    options['user'] = 'admin' #dopisanie właściwości klucz i values do dict
    options['version'] = 2.0 #dopisanie właściwości klucz i values do dict
    print(options['env'], options['version'], options['user'])
#ZAD2
def met_del_dict_values1():
    options = {
        'env' : 'production',
        'db' : 'mysql',
        'version' : 1.0,
        'show_errors' : True
    }
    del options['db'] #del - usówanie klucza z obiektu
    options.update({
        'user' : 'admin',
        'app' : 0,
        'version' : 2.2
        })
    print(options.values()) #values - zwraca wszystkie wartosci listy
    print(options.keys()) #keys - metoda zwracajaca wszystkie klucze
    print('version of key: ',options.get('version')) #get wyciaganie klucza
    for key in options:
        print(options[key])
#met_del_dict_values1()
#ZAD3
def met_convert_list_tuple_to_dict2():
    the_tuple = [('a', 'b', 'c'), ('d', 'f', 'g')]
    the_tuple2 = [('a', 'b', 'c', 'd', 'f', 'g')]
    the_list = [1, 2, 3, 4, 5, 6]
    dicts = [dict(zip(the_list, v)) for v in the_tuple]
    dicts2 = [dict(zip(the_list, v)) for v in the_tuple2]
    print(dicts)
    print(dicts2)
#met_change_list_tuple_to_dict2()
def met_convert_to_dict1(val_of_list_or_tuple, di): 
    di = dict(val_of_list_or_tuple) 
    return di
# m_tup = (1,2),(3,4)
# m_list = [1,2],[3,'a']
# dictionary = {}
# print(met_convert_to_dict1(m_tup,dictionary))
# print(met_convert_to_dict1(m_list,dictionary))

def met_convert_to_dict2(val_1, val_2): 
    dicts = [dict(zip(val_1, v)) for v in [val_2]]
    return dicts
# the_tuple2 = ('a', 'b', 'c', 'd', 'f', 'g')
# the_list = [1, 2, 3, 4, 5, 6]
# print(met_convert_to_dict2(the_list, the_tuple2))

#Konwertuje dane listy bądź dane tuple do tuple i
# def Convert_List_and_Tuple_to_Dict_values(value1, value2): 
#     di = {}
#     for a in value1:
#         for b in value2: 
#             di.setdefault(a, b)
#     return di
# t1 = [1,2,3,4,5]
# t2 = ('a', 'b', 'c', 'd', 'e')
# print (Convert_List_and_Tuple_to_Dict_values(t1, t2)) 
def Convert_Values_List_or_Tuple(tup): 
    di = {}
    for a, b in tup: 
        di.setdefault(a,b)
    return di    
# tups = [("akash", 10), ("gaurav", 12)] 
# print (Convert_Values_List_or_Tuple(tups))
a = ('y', 6)
b = ['z', 8]
c= {'d', 'dd'}
# d = dict({['xx', 'uu']})
e = (a)
# print(isinstance(dict()))
# s = dict("a", "b")
# print(s)
numbers1 = dict([('x', 5)])
numbers2 = dict([('x', 5)])
numbers3 = [('x', 5)]
numbers4 = ('x', 5)
print(iter(dict()))