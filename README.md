# api-sample

## Description
Simple API to manage samples.

## Requirements
Install requirements:
```bash
pip install -r requirements.txt
```

## Docs
Visit [url]/docs to see the API documentation.

## References
https://fastapi.tiangolo.com/fr/tutorial/first-steps/

## lancer l'API en local
```sh
docker run -d \
--name api-sample \
-p 8000:8000 \
-v $(pwd):/app \
-e KEYCLOAK_HOST=https://iam.karned.bzh \
-e KEYCLOAK_REALM=Karned \
-e KEYCLOAK_CLIENT_ID=karned \
-e KEYCLOAK_CLIENT_SECRET=chut! \
-e REDIS_HOST=redis \
-e REDIS_PORT=6379 \
-e REDIS_DB=0 \
-e REDIS_PASSWORD=chut! \
killiankopp/api-sample:latest
```
`
## lancer un MongoDB en local
```sh 
docker run -d \
--name mongodb-api-sample \
-p 27017:27017 \
-v ./_mongo_data:/data/db \
mongo
```