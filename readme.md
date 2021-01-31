# Green Medic

#### Environment Variables (Pre-requisites to run the project)
* Environment variables will be maintained: .env
* Pull the content of the repo into the .env folder

#### Project Run Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml up --build`. Append the args `-d` to have the docker build and run the project in the background

#### Accessing Project Shell
* Type `docker-compose -f local.yml exec <docker_compose_service_name> bash`. I.E: `docker-compose -f local.yml exec web bash`
* Pass the argument --user=root to access project shell as root user to install requirement dependencies. I.E: `docker-compose -f local.yml exec --user=root web bash`