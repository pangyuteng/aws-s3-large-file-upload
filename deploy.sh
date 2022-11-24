#!/bin/bash

region=$(aws configure get region)
registryId=$(aws ecr describe-registry | jq -r .registryId)
registry_url=${registryId}.dkr.ecr."${region}".amazonaws.com/lambda-docker-flask:latest

if [ ! -f .bucket-name ]
then
    echo $(openssl rand -hex 8) > .bucket-name
fi
bucket_name=$(cat .bucket-name)
echo $bucket_name

text='
{
    "prod": {
        "app_function": "app.app",
        "project_name": "lambda-docker-flask",
        "s3_bucket": "lambda-docker-flask-'${bucket_name}'",
        "environment_variables": {
            "EXAMPLE_ENV_VAR": "prod"
        },
        "events": [
            {
               "function": "process.run_process",
               "expression": "cron(0 */2 * * *)"
            }
        ],
        "lambda_description": "Zappa + Docker + Flask"
    }
}
'
echo -e $text > zappa_settings.json

zappa save-python-settings-file prod
zappa deploy prod -d ${registry_url}
