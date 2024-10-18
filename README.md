# Best trail
This application allows users to filter trails based on various parameters such as biking and fishing accessibility.
It is composed of a cli client and an API service. 

## Features
- Filtering options for trails (e.g., bike trails, fishing authorized)
- Dockerized environment for easy deployment
- Nginx as a reverse proxy for production

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bvlkvss/BestTrail.git
   ```

2. To run the service you can do that easily by doing that:
   ```bash
   cd TrailService
   docker-compose up --build
   ```

3. You can now run the TrailClient to ask for the best trails
  There are two options: 
    --bike to get all parks with bike trails
    --fishing to get all parks where fishing is authorized
   ```bash
   cd TrailClient
   python BestTrail.py --bike --trail
   ```
## Information
    The nginx web server runs on localhost on port 80. 
    The api server runs on port 9000 but is not accessible from outside the container
    Logging on the app is done through print statements but having more time, I would've used a logging library. 
    The csv file is loaded and the data is stored in the service. 
    The filtering is done in the DBHandler class, and you have to provide the function with a list of predicates (boolean functions). This was done in order to easily add other filters
    The TrailService exposes a REST Api. A web client with data vizualisation could be a nice improvement.  
    The applications is containerized to allow easy deployment on the cloud. 
    We could easily deploy it in a Kubernetes environment.
    We would need to implement the following: 
    Deployment: trail-service image
    Deployment: nginx-web-server image
    Ingress: To access the nginx-web-server
    Cluster-IP service for the nginx-web-server
    Cluter-IP service for the trail-service

