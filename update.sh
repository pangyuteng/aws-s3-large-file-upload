#!/bin/bash

region=$(aws configure get region)
registryId=$(aws ecr describe-registry | jq -r .registryId)
registry_url=${registryId}.dkr.ecr."${region}".amazonaws.com/lambda-docker-flask:latest

zappa update prod -d ${registry_url}