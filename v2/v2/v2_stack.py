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

import aws_cdk as cdk

class V2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        b = s3.Bucket(
                self,
                'cdk-v2stack-qwert098',
                auto_delete_objects=True,
                removal_policy=cdk.RemovalPolicy.DESTROY,
                bucket_name = 'cdk-v2stack-qwert098'
                )

#        queue = sqs.Queue(
#            self, "V2Queue",
#            visibility_timeout=Duration.seconds(300),
#        )
#
#        topic = sns.Topic(
#            self, "V2Topic"
#        )
#
#        topic.add_subscription(subs.SqsSubscription(queue))
