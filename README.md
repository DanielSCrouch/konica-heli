# Konica Minolta: Industrial Heloptoper Coordination Software  

## Heliport Overview

A REST API server that coordinates the landing of helicopter API requests onto one of multiple landing pands. 

### Registration and Authentication

All inbound helocopters must register with the Heliport before API access is granted uising the /register API termination point. The heliport registers the user in an SQLite3 database (local) using SQLAlchemy. Once registered a helicopter cient can then authorise using the /auth termination point. Suffcessful authentication grants the helicopter a time-sensitive authorisation token required for future (Stateless) API calls. Authentication is managed through the JWT library and an authentication and identification custom function. 

The heliport is exposed as a Flask Resource externally, and is modelled internally as a class object (Heliport) that is comprised of multiple Helipad objects. Inbound API requests are handled by the resource heloportR module. The module has a function for each termination point method and hands logic processing to the internal 'models' Heliport module.  

The Heliport object handles three requests (request_land, land and leave). The request_land function iterates through all pads on record and returns the id of the first that is free and avliable. The land and leave request both require this pad_id in order to either clear the respective landing pad, or store a helicopter within it. 

## Heliclient Overview

An API client that authenticates with the Heliport REST API and requests a port to land on. Then able to land and leave from port with POST and REMOVE api calls. The API requests are handled by python's 'requests' module allowing construction of the relevant url endpoints, payload (json) and header packaging. 

## Kubernetes deployment

The heliclient and helipad are separate packages. Each has a dedicated Dockerfile that installs the package onto a python-enabled linux container. Before containerisation, each package was created within python's 'venv' verison tool, and the imports exported to a requirements.txt file. This allows for easy installation of dependancies within the container by running a pip installation during the container build on the requirements.txt. 

The helipad is exposed via a nodeport yaml file. 

## Perfect Sort 

While the perfect-sort program is likely far from it computationally, it opperates in K-time. It iterates through the list once, splitting the cards into two lists before joining them. This program compromises memory (duplicate list stores) for computational efficiency. 



