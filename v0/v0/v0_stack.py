from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
)


class V0Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "aws-cdk-v0-fromv0App-Python")

#        queue = sqs.Queue(
#            self, "V0Queue",
#            visibility_timeout=Duration.seconds(300),
#        )
#
#        topic = sns.Topic(
#            self, "V0Topic"
#        )
#
#        topic.add_subscription(subs.SqsSubscription(queue))
