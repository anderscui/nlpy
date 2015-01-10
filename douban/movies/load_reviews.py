# coding=utf-8

import os

from common.chinese import read_all, read_lines
from common.persistence import to_pickle, from_pickle

rating_dict = {u'力荐': 5,
               u'推荐': 4,
               u'还行': 3,
               u'较差': 2,
               u'很差': 1,
               u'未打分': 0}

title_sep = '********************'
review_sep = '**********'


def from_file(file_path):
    reviews = read_lines(file_path)

    i = 0
    while reviews[i].strip() != title_sep:
        i += 1
    reviews = reviews[i + 1:]

    review_found = False
    review = []
    result = []
    for r in reviews:
        line = r.strip()
        if line != review_sep:
            review.append(r.strip())
        else:
            review_found = True

        if review_found:
            # if len(review) < 2:
            # continue
            rating = rating_dict[review[1]]
            comment = '.'.join(review[2:])

            # if (rating > 0) and (len(comment.strip()) > 0):
            #     result.append((rating, comment))
            result.append((rating, comment))

            review = []
            review_found = False

    return result


def show_reviews(reviews):
    for r in reviews:
        print(r[0])
        print(r[1])


def save(reviews, pickle_file):
    to_pickle(reviews, pickle_file)


def read_save(file_path, pickle_file=None):
    data = from_file(file_path)
    if not pickle_file:
        # bname = os.path.basename(raw_data)
        fname = os.path.splitext(file_path)[0]
        pickle_file = fname + '.pkl'
    save(data, pickle_file)

    return pickle_file


def load(pickle_file):
    return from_pickle(pickle_file)

# # save to pickles
# if __name__ == '__main__':
#
# review_dir = './reviews'
#     raw_data_files = [review_dir + '/' + f for f in os.listdir(review_dir)
#                       if os.path.isfile(os.path.join(review_dir, f))]
#     print(raw_data_files)
#
#     for raw_data in raw_data_files:
#         # raw_data = 'moviews_25884822.txt'
#         data_file = read_save(raw_data)
#         print(data_file)
#
#         reloaded = load(data_file)
#         # show_reviews(reloaded)
#         print(len(reloaded))
#
#         # assert count
#         raw_views = read_lines(raw_data)
#         seps = [l for l in raw_views if l.strip() == review_sep]
#         assert len(reloaded) == len(seps)


# # merge pickles
# if __name__ == '__main__':
#     pickle_dir = './review_pkl'
#     pickle_files = [pickle_dir + '/' + f for f in os.listdir(pickle_dir)
#                     if os.path.isfile(os.path.join(pickle_dir, f))]
#     print(pickle_files)
#
#     whole = []
#     for pkl_data in pickle_files:
#         reloaded = load(pkl_data)
#         print(len(reloaded))
#
#         for r in reloaded:
#             whole.append([r[0], r[1]])
#
#     to_pickle(whole, 'all_reviews.pkl')

# test final pickle
