# aws-s3-large-file-upload

```

https://ianwhitestone.work/zappa-serverless-docker
# per above, manually create `zappa_settings.json`, zdf/*.py and docker file 

zappa save-python-settings-file lambda_docker_flask
# above line creates zappa_settings.py


docker run -p 9000:8080 lambda-docker-flask:latest

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/", "httpMethod": "GET", "requestContext": {}, "body": null}'

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/time", "httpMethod": "GET", "requestContext": {}, "body": null}'



docker build -t lambda-docker-flask:latest .
aws ecr describe-repositories --repository-names lambda-docker-flask

aws ecr create-repository --repository-name lambda-docker-flask

docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

region=$(aws configure get region)
aws ecr get-login-password | docker login --username AWS --password-stdin 535328050074.dkr.ecr."${region}".amazonaws.com

docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest


zappa save-python-settings-file lambda_docker_flask
docker build -t lambda-docker-flask:latest .
docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest
docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest


#zappa init
#zappa deploy prod
#zappa update prod

zappa update lambda_docker_flask -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest



https://medium.com/@support_58351/generate-pre-signed-url-using-python-for-file-upload-in-aws-s3-e661653a304a


GET /my-large-file-app/home
GET /my-large-file-app/v1/upload-link
POST /my-large-file-app/v1/delete-s3
GET /my-large-file-app/review


```