# sam-lambda-bot

Comandos:

Link 1: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
Link 2: https://github.com/aws-samples/aws-twitterbot-workshop/blob/master/Bot1/README.md

> . .venv/bin/activate

> cd sam-app

Build:

> cd src

> sam build

In the hello_world directory, package code, first get the packages updated using pip3
pip3 install -r requirements.txt -t build/
cp hello_world/*.py build/


Package the Lambda and put it in your s3 bucket for deployment:

> sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket codigobot

Deploy the lambda with a proper stack name and enable IAM capability to create roles automatically

> sam deploy --template-file packaged.yaml --stack-name twitterpollerretweeter --capabilities CAPABILITY_IAM

Testar:

> curl https://stwnxksqng.execute-api.us-east-1.amazonaws.com/Prod/hello/

Logs:

> sam logs -n twitterpollerretweeter-RetweetFunction-7SNXR3U5LI8P


-------

Host Your API Locally

> sam local start-api

> curl https://localhost:3000/hello/

> sam local invoke "HelloWorldFunction" -e events/event.json

-------


Python Virtual environment
In case you're new to this, python3 comes with virtualenv library by default so you can simply run the following:

Create a new virtual environment
Install dependencies in the new virtual environment
> python3 -m venv .venv
> . .venv/bin/activate
> pip install -r requirements.txt
