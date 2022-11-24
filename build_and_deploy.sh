region=$(aws configure get region)
aws ecr get-login-password | docker login --username AWS --password-stdin 535328050074.dkr.ecr."${region}".amazonaws.com

docker build -t lambda-docker-flask:latest .

docker tag lambda-docker-flask:latest 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

docker push 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

zappa save-python-settings-file prod
zappa deploy prod -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest

#zappa update prod -d 535328050074.dkr.ecr.us-east-1.amazonaws.com/lambda-docker-flask:latest