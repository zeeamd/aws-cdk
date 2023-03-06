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


class V1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        b = s3.Bucket(
                self,
                'cdk-v1stack-qwert098b',
#                auto_delete_objects=True,
#                removal_policy=cdk.RemovalPolicy.DESTROY,
                bucket_name = 'cdk-v1stack-qwert098'
                )

        b.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

#        queue = sqs.Queue(
#            self, "V1Queue",
#            visibility_timeout=Duration.seconds(300),
#        )
#
#        topic = sns.Topic(
#            self, "V1Topic"
#        )
#
#        topic.add_subscription(subs.SqsSubscription(queue))
        
