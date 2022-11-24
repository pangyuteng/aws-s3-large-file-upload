region=$(aws configure get region)
registryId=$(aws ecr describe-registry | jq -r .registryId)
registry_url=${registryId}.dkr.ecr."${region}".amazonaws.com/lambda-docker-flask:latest

aws ecr get-login-password | docker login --username AWS --password-stdin 

docker build -t lambda-docker-flask:latest .
docker tag lambda-docker-flask:latest ${registry_url}
docker push ${registry_url}
