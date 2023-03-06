#!/usr/bin/env python3

import aws_cdk as cdk

from v2.v2_stack import V2Stack


app = cdk.App()
V2Stack(app, "v2")

app.synth()
