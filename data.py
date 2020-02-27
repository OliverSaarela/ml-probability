# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

def main():

    # Making data easier to read
    np.set_printoptions(precision=3, suppress=True)

    train_data_path = 'data/2000-2020-supershort.csv'

    
    train_df = pd.read_csv(train_data_path)
    

    # If Player 1 wins winner = 1 and if Player 2 wins winner = 0
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_1']] = 1
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_2']] = 0

    
    
    # Change Player_1, Player_2 and surface to onehotencoding
    numeric_train_df = pd.get_dummies(train_df, prefix=['Player_1', 'Player_2', 'Surface'], columns=['Player_1', 'Player_2', 'Surface'])

    # Make Winner int from object
    numeric_train_df['Winner'] = pd.to_numeric(train_df['Winner'], downcast = 'integer')
    print(numeric_train_df)

    # Splitting dataframe to train and test data
    train, test = train_test_split(numeric_train_df, test_size = 0.2)


    target = train.pop('Winner')
    dataset = tf.data.Dataset.from_tensor_slices((train.values, target.values))

    test_target = test.pop('Winner')
    dataset_2 = tf.data.Dataset.from_tensor_slices((test.values, test_target.values))

    for feat, targ in dataset.take(5):
        print ('Features: {}, Target: {}'.format(feat, targ))

    train_dataset = dataset.shuffle(len(train)).batch(3)
    test_dataset = dataset_2.shuffle(len(test)).batch(3)

    
    def get_compiled_model():
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                        metrics=['accuracy']
                    )
        return model

    model = get_compiled_model()
    model.fit(train_dataset, epochs=2)

    test_loss, test_accuracy = model.evaluate(test_dataset)

    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

    predictions = model.predict(test_dataset)

    for prediction, winner in zip(predictions[:10], list(test_dataset)[0][1][:10]):
        print("Predicted P1 W: {:.2%}".format(prediction[0]),
            " | Actual outcome: ",
            ("P1" if bool(winner) else "P2"))

if __name__ == "__main__":
    main()