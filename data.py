# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
import json

def main():
    train_data_path = 'data/2000-2018-supershort.csv'
    test_data_path = 'data/2019-2020-supershort.csv'

    
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)
    #print(train_df.head())
    #print(test_df.head())

    #Null changed to empty
    train_df.Player[ train_df.Player.isnull() ] = ''
    

    #print(pd.get_dummies(train_df))

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

    SELECT_COLUMNS = ['Player_1', 'Player_2', 'Winner', 'Surface']

    raw_train_data = get_dataset(train_data_path, select_columns=SELECT_COLUMNS)
    raw_test_data = get_dataset(test_data_path, select_columns=SELECT_COLUMNS)

    def show_batch(dataset):
        for batch, label in dataset.take(1):
            for key, value in batch.items():
                print("{:20s}: {}".format(key,value.numpy()))

    #print(raw_test_data)

    show_batch(raw_train_data)


    CATEGORIES = {
        'Player_1': LABELS,
        'Player_2': LABELS,
        'Surface': np.unique(train_df['Surface'])
    }

    categorical_columns = []
    for feature, vocab in CATEGORIES.items():
        cat_col = tf.feature_column.categorical_column_with_vocabulary_list(
            key = feature, vocabulary_list = vocab)
        categorical_columns.append(tf.feature_column.indicator_column(cat_col))

    #print(categorical_columns)
    example_batch = next(iter(raw_train_data))

    print(example_batch)
    categorical_layer = tf.keras.layers.DenseFeatures(categorical_columns)
    print(categorical_layer(example_batch).np()[0])
    

    #Building the model
    model = tf.keras.Sequential([
        categorical_layer,
        tf.keras.layers.Dense(128, activation = 'relu'),
        tf.keras.layers.Dense(128, activation = 'relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        loss = tf.keras.losses.BinaryCrossentropy(from_logits = True),
        optimizer = 'adam',
        metrics = ['accuracy']
    )

    train_data = raw_train_data.shuffle(500)
    test_data = raw_test_data

    model.fit(train_data, epochs = 5)

    test_loss, test_accuracy = model.evaluate(test_data)

    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

if __name__ == "__main__":
    main()