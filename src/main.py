from src.utils import get_split_line, read_data_csv, extract_data_from_categorical_feature, create_histogram_from_feature
from src.utils import bar_coordinate, calculate_column_width
import matplotlib.pyplot as plt
import logging


def main():
    file_path = '../data/data.csv'
    try:
        dataset = read_data_csv(file_path)
    except Exception as err:
        print("Couldn't open file")
        logging.exception(err)
        return

    men_data = extract_data_from_categorical_feature(dataset, "gender", "M")
    women_data = extract_data_from_categorical_feature(dataset, "gender", "F")

    counts_men_age, bin_edges_men_age = create_histogram_from_feature(men_data, 'age')
    counts_men_height, bin_edges_men_height = create_histogram_from_feature(men_data, 'height')
    counts_women_age, bin_edges_women_age = create_histogram_from_feature(women_data, 'age')
    counts_women_height, bin_edges_women_height = create_histogram_from_feature(women_data, 'height')

    plt.bar(bar_coordinate(bin_edges_men_age, 0.5), counts_men_age, label='men\'s age', alpha=0.5,
            width=calculate_column_width(bin_edges_men_age))
    plt.bar(bar_coordinate(bin_edges_women_age, 0.5), counts_women_age, label='women\'s age', alpha=0.5,
            width=calculate_column_width(bin_edges_women_age))
    plt.legend(loc=0)
    plt.title('Age distribution of the individuals')
    plt.xlabel('Age of individuals')
    plt.ylabel('Frequency')
    plt.savefig('age_distribution.png')
    plt.close()

    plt.bar(bar_coordinate(bin_edges_men_height, 0.5), counts_men_height, label='men\'s height', alpha=0.5,
            width=calculate_column_width(bin_edges_men_height))
    plt.bar(bar_coordinate(bin_edges_women_height, 0.5), counts_women_height, label='women\'s height', alpha=0.5,
            width=calculate_column_width(bin_edges_women_height))
    plt.legend(loc=0)
    plt.title('Height distribution of the individuals')
    plt.xlabel('height of individuals (m)')
    plt.ylabel('Frequency')
    plt.savefig('height_distribution.png')


if __name__=="__main__":
    main()
