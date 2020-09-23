#Author: VIJAYALAKSHMI GUNASEKARAPANDIAN
# Here, I explore the use of the email.parser to print out summary
# of emails shared between and by a list of people  

import re
import os 
from email.parser import BytesParser, Parser
from email.policy import default

#Prints out a summary of all of the emails sent by persons 
def emails_from(persons):
    LIMIT = 0
    keys = [k for k,v in persons.items()]
    for key in keys:
        directory = os.path.join("C:/PythonProjects/",key)
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                with open(os.path.join(subdir,file), 'rb') as fp:
                    headers = BytesParser(policy=default).parse(fp)
                    sender = '{}'.format(headers['from'])
                    for k,v in persons.items():
                        for li in v:
                            if(li == sender):
                                email_dated = '{}'.format(headers['date'])
                                date = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}", email_dated)[0]
                                subject_line = '{}'.format(headers['subject'])
                                receiver = '{}'.format(headers['to']).split(',')[0]
                                LIMIT += 1
                                if(LIMIT <= 30): print('[',date,']', sender, ' -> ', receiver, \
                                      '\n\tSubject:', subject_line)


#Prints summaries of all emails between persons 
def emails_between(persons):
    keys = [k for k,v in persons.items()]
    red_flag = []
    for k,v in persons.items():
        [red_flag.append(li) for li in v]
    for key in keys:
        directory = os.path.join("C:/PythonProjects/",key)
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                with open(os.path.join(subdir,file), 'rb') as fp:
                    headers = BytesParser(policy=default).parse(fp)
                    sender = '{}'.format(headers['from'])
                    receiver = '{}'.format(headers['to']).split(',')
                    cc_receiver = '{}'.format(headers['cc']).split(',')
                    bcc_receiver = '{}'.format(headers['bcc']).split(',')
                    email_dated = '{}'.format(headers['date'])
                    date = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}", email_dated)[0]
                    subject_line = '{}'.format(headers['subject'])
                    if sender in red_flag:
                        for el in receiver:
                            if el.strip() in red_flag:
                                print('[',date,']', sender, ' -> ', el, \
                                      '\n\tSubject:', subject_line)
                        for el in cc_receiver:
                            if el.strip() in red_flag:
                                print('[',date,']', sender, ' -> ', el, \
                                      '\n\tSubject:', subject_line)
                        for el in bcc_receiver:
                            if el.strip() in red_flag:
                                print('[',date,']', sender, ' -> ', el, \
                                      '\n\tSubject:', subject_line)
