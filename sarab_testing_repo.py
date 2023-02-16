"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_aws_disable_user_accounts_1' block
    playbook_aws_disable_user_accounts_1(container=container)

    return

def playbook_aws_disable_user_accounts_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_aws_disable_user_accounts_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.dest_mac"])

    container_artifact_fields_item_0 = [item[0] for item in container_artifact_data]

    inputs = {
        "aws_username": container_artifact_fields_item_0,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "name ALSKDJ 1928312398/aws_disable_user_accounts", returns the playbook_run_id
    playbook_run_id = phantom.playbook("name ALSKDJ 1928312398/aws_disable_user_accounts", container=container, inputs=inputs)

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return