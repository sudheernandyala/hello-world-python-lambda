# Hello World Python Lambda
Very simple AWS Lambda example, adated from https://github.com/aj-ali/my-app-repo and converted to Python. Used to support CodeBuild/CodePipeline setup.

Original AWS guidance included below... 

## Start from scratch starter project

This project contains source code and supporting files for the serverless application that you created in the AWS Lambda console. You can update your application at any time by committing and pushing changes to your AWS CodeCommit or GitHub repository.

This project includes the following files and folders:

- src - Code for the application's Lambda function.
- *TODO* - Unit tests for the application code.
- template.yml - A SAM template that defines the application's AWS resources.
- buildspec.yml -  A build specification file that tells AWS CodeBuild how to create a deployment package for the function.

Your Lambda application includes two AWS CloudFormation stacks. The first stack creates the pipeline that builds and deploys your application.

For a full list of possible operations, see the [AWS Lambda Applications documentation](https://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html).

## Try the application out

1. Go to the Lambda console.
2. Select **Applications** and select the one you created.
3. Select **helloFromLambdaFunction** in the **Resources** table.
4. Create a test event with the default settings. (Select **Select a test event** -> select **Configure test events** -> type in **Event name** -> select **Create**)
5. Select **Test** and you can see the result.
