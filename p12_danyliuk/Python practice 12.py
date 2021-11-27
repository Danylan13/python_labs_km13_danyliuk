dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]
 
# ВАШ КОД ТУТ

def res(func):
    def search(dirs, filename, the_way = None, the_way_now = '/'):

        """ 
        Using a substitution.
        """

        result = func(dirs, filename, the_way = [], the_way_now = '/')
        return result
    return search


def filter(lst, files = [], tuples = []):
    """ 
    Also i used shedule(it`s a list), but it`s difficult to use in code.
    Transferring everything that is in the folder.
    """
    for i in lst:
        if isinstance(i, tuple):
            tuples.append(i)
        else:
            files.append(i)
    result_1 = files[:]
    result_2 = tuples[:]
    files.clear()
    tuples.clear()
    return result_1, result_2


def read_tuple(Tupler):
    """
    Returning the name of the folder and content.
    """
    lst = list(Tupler)
    return lst[0], lst[1:]

def end(dirs, filename, the_way = None, the_way_now = '/'):
    files, tuples = filter(dirs)

    for i in files:
        if i == filename:
            if the_way_now == '/':
                the_way.append(filename)
            else:
                the_way.append(the_way_now + '/' + filename)
                
    for i in tuples:
        head, lst = read_tuple(i)
        if the_way_now == '/':
            the_way_now_ending = the_way_now + head
        else:    
            the_way_now_ending = the_way_now + '//' + head
        end(lst[0], filename, the_way, the_way_now_ending)
    
    return the_way

search = res(end)

# ПЕРЕВІРКА

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))
 
assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')