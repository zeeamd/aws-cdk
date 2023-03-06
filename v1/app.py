#!/usr/bin/env python3

import aws_cdk as cdk

from v1.v1_stack import V1Stack


app = cdk.App()
V1Stack(app, "v1")

app.synth()
