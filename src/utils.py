import pandas as pd
import numpy as np


def get_split_line(line):
    line = line.replace(" ","")
    return line.replace('\n', '').split(',')


def read_data_csv(file_path):
    data = pd.read_csv(file_path)
    return data


def extract_data_from_categorical_feature(data, feature, value):
    return data.loc[data[feature] == value]


def create_histogram_from_feature(data, feature, bins=100):
    return np.histogram(data[feature], bins=bins)


def calculate_column_width(bin_edges):
    return np.min(bin_edges[1:] - bin_edges[:-1])


def bar_coordinate(bin_edges, factor=1.0):
    return (bin_edges[1:] + bin_edges[:-1]) * factor