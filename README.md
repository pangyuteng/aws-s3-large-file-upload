# aws-s3-large-file-upload

```

https://ianwhitestone.work/zappa-serverless-docker
https://medium.com/@support_58351/generate-pre-signed-url-using-python-for-file-upload-in-aws-s3-e661653a304a


curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/", "httpMethod": "GET", "requestContext": {}, "body": null}'

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/time", "httpMethod": "GET", "requestContext": {}, "body": null}'


region=$(aws configure get region)
aws ecr get-login-password | docker login --username AWS --password-stdin 535328050074.dkr.ecr."${region}".amazonaws.com


docker build -t lambda-docker-flask:latest .
docker run -p 9000:8080 lambda-docker-flask:latest


aws ecr describe-repositories --repository-names lambda-docker-flask

aws ecr create-repository --repository-name lambda-docker-flask

docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest


docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

zappa save-python-settings-file prod
docker build -t lambda-docker-flask:latest .
docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest
docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest
zappa deploy prod -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

zappa update prod -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest


curl https://g7jydjfbg4.execute-api.us-east-1.amazonaws.com/prod/file-upload?object_name=hello.tar.gz

# post
https://gist.github.com/alexdebrie/3e8b96217f5aff01227050b17a24e380

curl -v -F key=hello.tar.gz \
  -F x-amz-algorithm=*** \
  -F policy=*** \
  -F x-amz-credential=*** \
  -F x-amz-date=*** \
  -F x-amz-security-token=*** \
  -F x-amz-signature=*** \
  -F file=@hello.tar.gz \
  https://lambda-docker-flask-2405fd329144.s3.amazonaws.com/


GET /my-large-file-app/home
GET /my-large-file-app/v1/upload-link
POST /my-large-file-app/v1/delete-s3
GET /my-large-file-app/review


```