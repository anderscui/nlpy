import nltk
import os, os.path


def check_data_dir():
    dp = os.path.expanduser('~/nltk_data')
    if not os.path.exists(dp):
        os.mkdir(dp)

    assert os.path.exists(dp)

    sub_dp = os.path.join(dp, 'corpora/cookbook')
    if not os.path.exists(sub_dp):
        os.makedirs(sub_dp)

    return dp


data_dir = check_data_dir()
print(data_dir in nltk.data.path)

# test a file
import nltk.data
print(nltk.data.load('corpora/cookbook/mywords.txt', format='raw'))
