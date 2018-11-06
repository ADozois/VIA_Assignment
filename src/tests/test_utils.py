from src.utils import get_split_line, read_data_csv, extract_data_from_categorical_feature, create_histogram_from_feature
from src.utils import calculate_column_width, bar_coordinate
import numpy as np


def test_get_split_line():

    test_line = 'I, like, Python'
    split_line = get_split_line(test_line)

    assert(split_line[0] == 'I')
    assert(split_line[1] == 'like')
    assert(split_line[2] == 'Python')


def test_extract_data_from_categorical_feature():
    file_path_data = '../../data/test_data.csv'
    file_path_men = '../../data/test_data_men.csv'
    file_path_women = '../../data/test_data_women.csv'
    data = read_data_csv(file_path_data)

    test_men_data = read_data_csv(file_path_men)
    test_women_data = read_data_csv(file_path_women)

    men_data = extract_data_from_categorical_feature(data, 'gender', 'M').reset_index(drop=True)
    women_data = extract_data_from_categorical_feature(data, 'gender', 'F').reset_index(drop=True)

    assert (men_data.equals(test_men_data))
    assert (women_data.equals(test_women_data))


def test_create_histogram_from_feature():
    file_path = '../../data/test_data_men.csv'
    data = read_data_csv(file_path)

    test_count = np.array([2, 2])
    test_bin_edges = np.array([30, 31, 32])

    age_count, bin_edges = create_histogram_from_feature(data, 'age', 2)

    assert(np.array_equal(age_count, test_count))
    assert(np.array_equal(bin_edges, test_bin_edges))

def test_calculate_column_width():
    file_path = '../../data/test_data_women.csv'
    data = read_data_csv(file_path)

    test_value = 2.0

    age_count, bin_edges = create_histogram_from_feature(data, 'age', 10)
    value = calculate_column_width(bin_edges)

    assert (value == test_value)

def test_bar_coordinate():
    file_path = '../../data/test_data_women.csv'
    data = read_data_csv(file_path)

    test_coordinates = np.array([21.0,23.0,25.0,27.0,29.0,31.0,33.0,35.0,37.0,39.0])

    age_count, bin_edges = create_histogram_from_feature(data, 'age', 10)
    coordinates = bar_coordinate(bin_edges, 0.5)

    assert (np.array_equal(coordinates, test_coordinates))











