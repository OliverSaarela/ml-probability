# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

def main():
    train_data_path = 'data/2000-2020-supershort.csv'
    test_data_path = 'data/2019-2020-supershort.csv'

    
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)
    #print(train_df.head())
    #print(test_df.head())
    

    # Null changed to empty
    #train_df.Player[ train_df.Player.isnull() ] = ''
    # If Player 1 wins winner = 1 and if Player 2 wins winner = 0
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_1']] = 1
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_2']] = 0

    #test_df['Winner'].loc[test_df['Winner'] == test_df['Player_1']] = 1
    #test_df['Winner'].loc[test_df['Winner'] == test_df['Player_2']] = 0
    
    
    # Change Player_1, Player_2 and surface to onehotencoding
    numeric_train_df = pd.get_dummies(train_df, prefix=['Player_1', 'Player_2', 'Surface'], columns=['Player_1', 'Player_2', 'Surface'])

    #numeric_test_df = pd.get_dummies(test_df, prefix=['Player_1', 'Player_2', 'Surface'], columns=['Player_1', 'Player_2', 'Surface'])
    #numeric_test_df['Player'] = pd.Categorical(numeric_test_df['Player'])
    #numeric_test_df['Player'] = numeric_test_df.Player.cat.codes

    numeric_train_df['Winner'] = pd.to_numeric(train_df['Winner'], downcast = 'integer')
    #numeric_test_df['Winner'] = pd.to_numeric(test_df['Winner'], downcast = 'integer')
    print(numeric_train_df)

    train_target = numeric_train_df.pop('Winner')
    dataset = tf.data.Dataset.from_tensor_slices((numeric_train_df.values, train_target.values))

    train_dataset = dataset.shuffle(len(numeric_train_df)).batch(1)

    
    def get_compiled_model():
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer='adam',
                        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                        metrics=['accuracy']
                    )
        return model

    model = get_compiled_model()
    model.fit(train_dataset, epochs=1)

if __name__ == "__main__":
    main()