region=$(aws configure get region)
aws ecr get-login-password | docker login --username AWS --password-stdin 535328050074.dkr.ecr."${region}".amazonaws.com

zappa save-python-settings-file lambda_docker_flask

docker build -t lambda-docker-flask:latest .

docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

# zappa deploy lambda_docker_flask -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest
zappa update lambda_docker_flask -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest