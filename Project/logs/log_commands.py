import os,string,sys
sys.path.append(os.path.normpath(os.getcwd()))
import datetime
import re
import pandas as pd
from config import follow_up_path, location
from dateutil.relativedelta import relativedelta
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')

def process_log(log_line):
    
    with open(location + 'log_file.TXT', 'a') as f:
        f.write(log_line)
        
def followup_questions(log_line):
    
    with open(location + 'followup_file.TXT', 'a') as f:
        f.write(log_line)
    
if __name__ == "__main__":
    
    user_id = sys.argv[1]
    message_user = sys.argv[2]
    message = sys.argv[3]
    slack_output = sys.argv[4]
    team = sys.argv[5]
    channel = sys.argv[6]
    start_timestamp = sys.argv[7]
    end_timestamp = sys.argv[8]
    processing_time = sys.argv[9]
    follow_ind = sys.argv[10]
    
    log_line = user_id + '|' + message_user + '|' + message + '|' + REPLACE_BY_SPACE_RE.sub('',slack_output.replace('\n',',')) + '|' + team + '|' + channel + '|' + start_timestamp + '|' + end_timestamp + '|' + processing_time + '|' + follow_ind + '\n'
    process_log(log_line)
    
    if follow_ind == '1':
        followup_questions(message + '\n')
    
