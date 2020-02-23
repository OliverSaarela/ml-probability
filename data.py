# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf

def main():
    train_data_path = 'data/2000-2018-supershort.csv'
    test_data_path = 'data/2019-2020-supershort.csv'

    
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)
    #print(train_df.head())
    #print(test_df.head())

    train_df.Player[ train_df.Player.isnull() ] = ''

    print(np.unique(train_df['surface']))

    LABEL_COLUMN =  'Winner'
    LABELS = np.unique(train_df['Player'])

    

    def get_dataset(file_path, **kwargs):

        dataset = tf.data.experimental.make_csv_dataset(
            file_path,
            batch_size = 5, #Small during testing, Make bigger when done.
            label_name = LABEL_COLUMN,
            na_value = '?',
            num_epochs = 1,
            ignore_errors = True,
            **kwargs
            )
        return dataset

    SELECT_COLUMNS = ['Player 1', 'Player 2', 'Winner', 'surface']

    raw_train_data = get_dataset(train_data_path, select_columns=SELECT_COLUMNS)
    raw_test_data = get_dataset(test_data_path, select_columns=SELECT_COLUMNS)

    def show_batch(dataset):
        for batch, label in dataset.take(1):
            for key, value in batch.items():
                print("{:20s}: {}".format(key,value.numpy()))

    show_batch(raw_train_data)

    example_batch = next(iter(raw_train_data))

    CATEGORIES = {
        'Player 1': LABELS,
        'Player 2': LABELS,
        'surface': np.unique(train_df['surface'])
    }

    categorical_columns = []
    for feature, vocab in CATEGORIES.items():
        cat_col = tf.feature_column.categorical_column_with_vocabulary_list(
            key = feature, vocabulary_list = vocab)
        categorical_columns.append(tf.feature_column.indicator_column(cat_col))

    print(categorical_columns)

    categorical_layer = tf.keras.layers.DenseFeatures(categorical_columns)
    print(categorical_layer(example_batch).np()[0])
    

if __name__ == "__main__":
    main()