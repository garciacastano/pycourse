#-*- coding: utf-8 -*-
u'''
MOD 05: Iterators, generators and coroutines
'''


def repeat_items(sequence, num_times=2):
    '''Iterate the sequence returning each element repeated several times

    >>> list(repeat_items([1, 2, 3]))
    [1, 1, 2, 2, 3, 3]

    >>> list(repeat_items([1, 2, 3], 3))
    [1, 1, 1, 2, 2, 2, 3, 3, 3]

    >>> list(repeat_items([1, 2, 3], 0))
    []

    >>> list(repeat_items([1, 2, 3], 1))
    [1, 2, 3]

    :param sequence: sequence or iterable to iterate over
    :param num_times: number of times to repeat each item
    :returns: generator with each element of the sequence repeated
    '''
    for i in sequence:
        rep=num_times
        while rep>0:
            yield i
            rep-=1
            continue


def izip(*sequences):
    '''Return tuples with one element of each sequence
        It returns as many pairs as the shortest sequence
        The same than std lib zip function

    >>> list(izip([1, 2, 3], ['a', 'b', 'c']))
    [[1, 'a'], [2, 'b'], [3, 'c']]

    >>> list(izip([1, 2, 3], ['a', 'b', 'c', 'd']))
    [[1, 'a'], [2, 'b'], [3, 'c']]

    :param sequences: two or more sequences to loop over
    :returns: generator returning tuples with the n-th item of input sequences
    '''
    if len(sequences) > 0:
        tuples_len = min(int(i) for i in map(lambda x: len(x), sequences))
    else:
        yield []
        return

    for index in range(0, tuples_len):
        result_element = []
        for sequence in sequences:
            result_element.append(sequence[index])
        yield result_element


def merge(*sequences):
    '''Iterate over all sequences returning each time one item of one of them
        Always loop sequences in the same order

    >>> list(merge([None, True, False], ['a', 'e', 'i', 'o', 'u']))
    [None, 'a', True, 'e', False, 'i', 'o', 'u']

    >>> list(merge(['a', 'e', 'i', 'o', 'u'], [None, True, False]))
   ['a', None, 'e', True, 'i', False, 'o', 'u']

    >>> list(merge(['a', 'e', 'i', 'o', 'u'], [None, True, False], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    ['a', None, 0, 'e', True, 1, 'i', False, 2, 'o', 3, 'u', 4, 5, 6, 7, 8, 9]

    :param sequences: two or more sequences to loop over
    :returns: generator returning one item of each
    '''

    iterators = map(iter, sequences)
    while sequences:
        yield map(iter)


def flatten(L):
    '''flatten the input list of lists to a flattened list

    >>>list(flatten([1, 2, [3]])
    [1, 2, 3]

    >>>list(flatten([1, 2, [3, 4], [[5]])
    [1, 2, ,3 ,4 ,5]

    :param L: list of lists
    :returns: generator with flattened list
    '''
    yield None
