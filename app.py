import connexion
from connexion import RestyResolver
from flask import render_template

from src import utils

options = {"swagger_ui": True,
           'swagger_url': '/api'}

connexion_app = connexion.App(__name__, specification_dir='swagger/', options=options)

connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@connexion_app.route('/', methods=['POST', 'GET'])
def io_html():
    recommendations = list()
    recommendations.append(utils.render_recommendations())
    # recommendations.append(["R1", "R1", "R3"])
    return render_template('recommender-ux.html', hints=recommendations)


if __name__ == '__main__':
    print("Going to run app ...")
    connexion_app.run(host="0.0.0.0", port=5000, debug=False)
