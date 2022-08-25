# Hackathon 2022 - GA Recommender
Recommender service for Movie Lens dataset

# How to run docker

docker build -t ga-recommender . 

docker run -p 5001:5001 docker.io/library/ga-recommender

# Other Resources

### Dataset
https://movielens.org/

### Machine Learning Framework  

https://surpriselib.com/

### Connexion (RESTful API with OpenAPI 3.0)
https://connexion.readthedocs.io/en/latest/quickstart.html
### Swagger UI
<localhost:5000>/api

### REST API Healthcheck
<localhost:5000>/health

### REST API Healthcheck
<localhost:5000>/render_recommendation




