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

    train_dataset = dataset.shuffle(len(train)).batch(5)
    test_dataset = dataset_2.shuffle(len(test)).batch(5)

    # Building the model
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
    model.fit(train_dataset, epochs=1)

    test_loss, test_accuracy = model.evaluate(test_dataset)

    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))


    # Pick players to test
    # Making an empty dataframe for the pick and filling it with 0
    COLUMN_NAMES = list(numeric_train_df.columns)
    BASE_VALUES = list()
    for i in range(len(COLUMN_NAMES)):
        BASE_VALUES.append(0)

    BASE_VALUES = np.array(list(BASE_VALUES))

    picked_df = pd.DataFrame(columns = COLUMN_NAMES)
    picked_df.loc[0] = BASE_VALUES
    print(picked_df)

    p1 = str(input('Name Player 1: '))
    p2 = str(input('Name Player 2: '))
    surface = str(input('Name surface: '))
    picked_df['Player_1_' + p1].loc[picked_df['Player_1_' + p1] == picked_df['Player_1_' + p1]] = 1
    picked_df['Player_2_' + p2].loc[picked_df['Player_2_' + p2] == picked_df['Player_2_' + p2]] = 1
    picked_df['Surface_' + surface].loc[picked_df['Surface_' + surface] == picked_df['Surface_' + surface]] = 1

    print(picked_df)

    for i in picked_df.columns:
        picked_df[i] = pd.to_numeric(picked_df[i], downcast = 'integer')


    pick_target = picked_df.pop('Winner')
    picked_dataset = tf.data.Dataset.from_tensor_slices((picked_df.values, pick_target.values))

    picked_dataset = picked_dataset.shuffle(len(picked_df)).batch(1)

    predictions = model.predict(picked_dataset)

    print(predictions)

    # Show some results
    for prediction, Winner in zip(predictions[:10], list(picked_dataset)[0][1][:10]):
        print("Player 1 predicted win chance: {:.2%}".format(prediction[0]),
            " | Actual outcome: ",
            ("Player 1" if bool(Winner) else "Player 2"))

if __name__ == "__main__":
    main()