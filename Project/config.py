import os
from slackclient import SlackClient
import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

location = "E:/recomendar/Project/"  
#Slack configuration

SLACK_BOT_TOKEN='xoxb-1667390057169-1805304387207-TdOODm7tjexgVkMxS26F6xyu'
SLACK_VERIFICATION_TOKEN='OOExqyq1Ql8EnTErwZT5azHA' 

#instantiate Slack client

slack_client = SlackClient(SLACK_BOT_TOKEN) 

#Watson service configuration


authenticator = IAMAuthenticator('7BgdQl0hZeMjL_f_ubzp8s3lCwO4h7cLc6Ug5SZcaiog')
service = AssistantV1(
    version='2018-09-20',
    authenticator=authenticator
)
service.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/9b35ddee-dda7-4a67-a61d-926e0f118096')
assistant_id = 'fb952170-4d15-40e1-b846-4231174f0859'

"""Testing"""
#print(type(assistant_id))
#session_id = service.create_session(assistant_id).get_result()
#service.set_disable_ssl_verification(True)
#session_id = json.dumps(session).encode('utf-8')
#print(type(session_id))

#Log files configuration 

log_commands_path = location + "logs/log_commands.py" 
follow_up_path = location + "logs/followup_email.py" 

#Temp files configuration

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" 
onetime_file = location + "nlp/nlp_solutions/onetime.txt" 
