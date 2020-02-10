# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
#import tensorflow_datasets as tfds
#import os

def main():
    TRAIN_DATA_URL = 'https://query.data.world/s/dhti3sicg5q7li6xdajagqhnwqiobl'
    TEST_DATA_URL = 'https://query.data.world/s/psj7w2yrq54ujznhyt4vawwmq44mi7'

    train_file_path = tf.keras.utils.get_file("atp_matches_2018.csv", TRAIN_DATA_URL)
    test_file_path = tf.keras.utils.get_file("atp_matches_2019.csv", TEST_DATA_URL)

    np.set_printoptions(precision=3, suppress=True)
    
    df = pd.read_csv(train_file_path)
    
    df['winner'] = pd.Categorical(df['winner'])
    df['winner'] = df.winner.cat.codes
    df['loser'] = pd.Categorical(df['loser'])
    df['loser'] = df.loser.cat.codes
    print(df['winner'].head(15))
    print(df['loser'].head(15))

if __name__ == "__main__":
    main()