# Week 1 — App Containerization

## Containerize Backend and Frontend

### Checked that the python works independent of Docker

```sh
cd backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
python3 -m flask run --host=0.0.0.0 --port=4567
cd ..
```

- port unlocked
- successfully opened port 4567
- got back JSON response


### Docker Config
- Added Dockerfiles for backend and frontend and DynamoDB Local and PostgreSQL to docker-compose.yml
[Link to commit 6e6e3e7](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/6e6e3e7b0de62537dc8b0b7188e661e3bb16cd277)
[Link to commit 378c7c5](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/378c7c553a8eee89e595a41a0f65b8cf30cdab67)


### Tried building the container

```sh
docker build -t  backend-flask ./backend-flask
```

### Tried Running the Container

Run 
```sh
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```

Tried returning the container id into an Env Var
```sh
CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
env | grep CONTAINER
```

### Get Container Images or Running Container Ids

```
docker ps
docker images
```

### Checked Container Logs

```sh
docker logs CONTAINER_ID -f
docker logs backend-flask -f
docker logs $CONTAINER_ID -f
```

### Tried attaching shell to a Container

```sh
docker exec CONTAINER_ID -it /bin/bash
```

### Added "npm install" to gitpod.yml to avoid running it manually
[Link to commit 87b6cc6](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/87b6cc64d576c26877b20b28627f777dd56ead99)

### Three ways of running Docker compose
```sh
docker compose up
docker-compose up
#Right-click on the file in VSC and choose "Compose UP"
```

## Updating the OpenAPI definitions
[Link to commit 98f758d](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/98f758df7928e28a49ad80e180291e8b4cab3a00)

## Updating the backend and frontend code to add notifications functionality
[Link to commit c966c8e](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/c966c8ec19df41e2e939096562c0dde4db4ffefc)
[Link to commit a348950](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/a34895091e3b4f8e7604e0314d2f14c1cd41f6da)

## added postgres to gitpod yaml
[Link to commit 8927745](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/892774589e3970ba86967e3fe1add0034c820305)


## DynamoDB Local and PostgreSQL



Used the "TablePlus" installed on Mac to connect to Postgres:
![TablePlus GUI](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/101ecf8731342be7e4fe4131b7ede358b5767b07/_docs/assets/week1/tableplus-gui.png)


Tried connecting via CLI client:
```sh
sudo apt-get install -y postgresql-client
psql -h localhost -U postgres
```

![Postgres CLI](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/101ecf8731342be7e4fe4131b7ede358b5767b07/_docs/assets/week1/postgres-cli.png)


## Homework Challenges
### Run the Dockerfile CMD as an external script
1. Created `run_flask.sh`
```bash
#!/bin/bash
python3 -m flash run --host=0.0.0.0 --port=4567
```
2. Built the container
```sh
docker build -t backend-flask ./backend-flask
```
3. Ran the container
```sh
docker run -d --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```
[Link to commit]()



## Docker Login
```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to xxxxx to create one.
Username: oewete
Password: 
WARNING! Your password will be stored unencrypted in /home/gitpod/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

## Docker Tag

```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ docker tag aws-bootcamp-cruddur-2023-backend-flask oewete/cruddur-backend-flask:1.0
```

## Docker Push

```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ docker push oewete/cruddur-backend-flask:1.0
The push refers to repository [docker.io/oewete/cruddur-backend-flask]
0c0a75948e28: Pushed 
f3107e05a0a6: Pushed 
944dd1c2589f: Pushed 
e298d729bcf5: Pushed 
223e3b83550e: Mounted from library/python 
53b2529dfca9: Mounted from library/python 
5be8f6899d42: Mounted from library/python 
8d60832b730a: Mounted from library/python 
63b3cf45ece8: Mounted from library/python 
1.0: digest: sha256:7f0f0c5fcf91a279eb0c6e57b5bc2bc65d137ce332a24ab2ec503cd26489d07e size: 2203
```

## Verify Docker image was pushed to Dockerhub
![Dockerhub](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/36bbf8766702108fd3f92a7be0c5c9f6c9dfb356/_docs/assets/week1/dockerhub.png)


#### 5. Deleting the Docker Hub credentials from the ~/.docker/config.json
```sh
docker logout
```

## MSB

```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ docker images aws-bootcamp-cruddur-2023-backend-flask
REPOSITORY                                TAG       IMAGE ID       CREATED          SIZE
aws-bootcamp-cruddur-2023-backend-flask   latest    79e8f320418c   54 minutes ago   129MB
```

