# test_hashtable.py

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(capacity = 100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100
    # to handle len() correctly we require a __len__ method in our custom class

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)

    # When
    actual_values = hash_table.values

    # Then
    assert actual_values == expected_values