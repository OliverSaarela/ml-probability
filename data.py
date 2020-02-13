# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from pathlib import Path
#import tensorflow_datasets as tfds
import os

def main():
    train_data = Path('data/2000-2018-supershort.csv')
    test_data = Path('data/2019-2020-supershort.csv')

    
    train_df = pd.read_csv(train_data)
    test_df = pd.read_csv(test_data)
    print(train_df.head())
    print(test_df.head())

    LABEL_COLUMN =  'Winner'
    LABELS = [train_df['Player']]

if __name__ == "__main__":
    main()