import uuid

from flask import jsonify

from src.RecommendationStrategy import RecommendationStrategy, RecommenderA


def health_check():
    """Response handler to api call"""
    return jsonify({'id': uuid.uuid1(), 'message': 'Congratulations! the recommender service is healthy'})


# TODO: Selection is based on click distribution of the recommenders coming from Dynamo DB or similar
def get_winning_recommender() -> RecommendationStrategy:
    # Read Leading Recommender Score from Dynamo DB and return a probabilistic
    return RecommenderA()


def render_recommendations():
    recommender = get_winning_recommender()
    return recommender.get_recommendations()
