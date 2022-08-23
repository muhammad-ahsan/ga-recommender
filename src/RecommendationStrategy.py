import abc


# TODO Concrete implementation of the Recommender

class RecommendationStrategy(metaclass=abc.ABCMeta):

    # TODO: change the return type to dictionary <movie_reference, rank>
    @abc.abstractmethod
    def get_recommendations(self):
        raise NotImplementedError("WTH! why calling abstract method?")


class RecommenderA(RecommendationStrategy):
    def __init__(self):
        pass

    def get_recommendations(self):
        return ["RA_Movie_1", "RA_Movie_2", "RA_Movie_3"]


class RecommenderB(RecommendationStrategy):
    def __init__(self):
        pass

    def get_recommendations(self):
        return ["RB_Movie_1", "RB_Movie_2", "RB_Movie_3"]
