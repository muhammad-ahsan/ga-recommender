import connexion
from connexion import RestyResolver
from flask import render_template

from src import utils

options = {"swagger_ui": True,
           'swagger_url': '/api'}

connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
app = connexion_app.app
connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@app.route('/', methods=['POST', 'GET'])
def io_html():
    recommendations = list()
    recommendations.append(utils.render_recommendations().to_json(orient='index'))
    return render_template('recommender-ux.html', hints=recommendations)


if __name__ == '__main__':
    app.run(port=5000, debug=False)
