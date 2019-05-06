from typing import List, Dict, Union, Generator
import string, random
# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for elements in data:
        if type(elements.get('name')) == str:
            elements.update({'name': elements.get('name').capitalize()})
        else:
            elements.get('name')
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    mydict = [{k: v for k, v in y.items() if k not in redundant_keys} for y in data]
    return mydict


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [i for i in data if value in i.values()]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if data:
        return min(data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    if data:
        return min([str(x) for x in data], key=len)



def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:
        members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]

    """

    min_age = min([i for i in map(lambda x: x.get(key), data) if i])
    for i in data:
        if i[key] == min_age:
            return i


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    return max([list_number for list_in_list in data for list_number in list_in_list])



def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum([ord(x) for x in text if x])

def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for num in range(1, 201):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num



def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """

    return [random.choice(string.ascii_lowercase) for _ in range(20)]