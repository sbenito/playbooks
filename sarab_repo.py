"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'sdfsdfkjshkasdh_2934843_sldkfj' block
    sdfsdfkjshkasdh_2934843_sldkfj(container=container)

    return

def sdfsdfkjshkasdh_2934843_sldkfj(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("sdfsdfkjshkasdh_2934843_sldkfj() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "sarab SLDKFJ 12223/alert_deescalation_for_test_machines", returns the playbook_run_id
    playbook_run_id = phantom.playbook("sarab SLDKFJ 12223/alert_deescalation_for_test_machines", container=container)

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