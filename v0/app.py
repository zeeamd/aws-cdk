#!/usr/bin/env python3

import aws_cdk as cdk

from v0.v0_stack import V0Stack


app = cdk.App()
V0Stack(app, "v0")

app.synth()
