import abc

import pandas as pd
from lenskit.algorithms.basic import Popular
from lenskit.datasets import ML100K


class MovieRecommendation:
    def __init__(self, title, release, imdb, score):
        self.title = title
        self.release = release
        self.imdb = imdb
        self.score = score


class RecommendationStrategy(metaclass=abc.ABCMeta):

    def __init__(self):
        self.ml_dataset = ML100K('ml-100k')

    @abc.abstractmethod
    def recommend(self) -> pd.DataFrame:
        raise NotImplementedError("WTH! why calling abstract method?")


class RecommenderA(RecommendationStrategy):
    def __init__(self):
        super().__init__()
        self.baseline = Popular().fit(self.ml_dataset.ratings[:-1000])

    # TODO: fix the hardcoded user. Option 1: match online users with known users based in age, gender and occupation
    def recommend(self) -> pd.DataFrame:
        # Hardcode -> User 14 is a scientist
        recommendations_df = self.baseline.recommend(14, n=20)
        response = self.ml_dataset.movies.join(recommendations_df.set_index("item"), on="item", how="inner")
        return response[["title", "release", "imdb", "score"]]


class RecommenderB(RecommendationStrategy):
    def __init__(self):
        super().__init__()
        # TODO: Advanced recommendation model implementation
        raise NotImplementedError

    def recommend(self) -> pd.DataFrame:
        return pd.DataFrame()
