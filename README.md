# AztecA
Alexa Classroom interface
This project is meant to allow professors to control smart learning spaces with the alexa voice assistant.
1. The workflow starts with an "Alexa skill" that interprets the intent of the input voice commands.
2. The alexa skill inputs to a aws lambda function https://us-west-1.console.aws.amazon.com/lambda/home?region=us-west-1#/functions/AztecaLambda?tab=configuration
3. The lamba function processes the intent and sends the command to the SQS Queue https://us-west-1.console.aws.amazon.com/sqs/v2/home?region=us-west-1#/queues/https%3A%2F%2Fsqs.us-west-1.amazonaws.com%2F277872029364%2FAzteca-Tasks
4. The queue is read by a python boto3 script listening from a local class computer (this repo's code)
5. The script then calls the python interface for running the command
