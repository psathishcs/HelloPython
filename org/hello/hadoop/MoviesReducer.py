#!/usr/bin/python
import sys

def reducer():
    num_ratings = {}
    oldRating = None
    oldMovie = None
    Ratings = 0

    for line in sys.stdin:
        data = line.split('::')
        if len(data) != 2:
            continue

        movieID, rating = data
        if oldMovie and oldMovie != movieID:
            if num_ratings.has_key(str(Ratings)):
                num_ratings[str(Ratings)] += 1
            else:
                num_ratings[str(Ratings)] = 1

            Ratings = 0
        Ratings += 1
        oldMovie = movieID

    for key in sorted(num_ratings, key=lambda x: int(x)):
        print "{0}\t{1}".format(key, num_ratings[key])

if __name__ == "__main__":
    reducer()
