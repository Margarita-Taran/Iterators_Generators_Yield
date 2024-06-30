class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.external_list = 0
        self.internal_list = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.external_list < len(self.list):
            if self.internal_list < len(self.list[self.external_list]):
                item = self.list[self.external_list][self.internal_list]
                self.internal_list += 1
                return item
            self.internal_list = 0
            self.external_list += 1
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()