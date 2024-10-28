import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected


def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == expected
    
def test_bubble_sort_ten_or_more():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 78, 56, 45] 
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1


def test_bubble_sort_no_numbers():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0

def test_bubble_sort_invalid_input():
    input_arr = [64, 34, 25, "abc", 22, 11] 
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2
