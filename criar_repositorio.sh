#!/bin/bash

# Create a Repository in CodeCommit Using the AWS CLI

aws codecommit create-repository --repository-name fiaprepo --repository-description "Repositorio codigo LABs." --region us-east-1

# Connect Your Environment to the Remote Repository

git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true

# To view a list of CodeCommit repositories

aws codecommit list-repositories

aws codecommit get-repository --repository-name fiaprepo

# git clone CLONE_URL
rm -rf .git

# Add the files to the Git staging area by running the git add command.

git add --all

# Confirm the files were successfully added to the Git staging area by running the git status command again. All three files are now listed as changes to commit.

git commit -m "Fiap Repo."

# Push the commit to your remote repository in CodeCommit by running the git push command.

git push -u origin master
