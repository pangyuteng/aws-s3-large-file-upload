# aws-s3-large-file-upload


### prior deploy

install: aws-cli, jq, zappa via pip
### deploy steps
```
# first time deploy
aws ecr create-repository --repository-name lambda-docker-flask
bash build_and_push.sh && bash deploy.sh

# update and deploy
bash build_and_push.sh && bash update.sh

# undeploy
bash undeploy.sh

```

### references
```

https://ianwhitestone.work/zappa-serverless-docker
https://medium.com/@support_58351/generate-pre-signed-url-using-python-for-file-upload-in-aws-s3-e661653a304a
```

### notes
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/", "httpMethod": "GET", "requestContext": {}, "body": null}'

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/time", "httpMethod": "GET", "requestContext": {}, "body": null}'

# upload to s3 via curl post 
https://gist.github.com/alexdebrie/3e8b96217f5aff01227050b17a24e380

curl -v -F key=${objectId} \
  -F x-amz-algorithm=*** \
  -F policy=*** \
  -F x-amz-credential=*** \
  -F x-amz-date=*** \
  -F x-amz-security-token=*** \
  -F x-amz-signature=*** \
  -F file=@${fileName} \
  ${url}


```