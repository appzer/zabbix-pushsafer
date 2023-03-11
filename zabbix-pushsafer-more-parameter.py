#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pushsafer notification script for Zabbix
# 
# Author:
#   Pushsafer.com Kevin Siml - support@pushsafer.com
#
# Purpose:
#   Push zabbix notifications to Pushsafer enabled devices
#   See: https://www.pushsafer.com
#
# Requirements:
#   pip install python-pushsafer
#

import argparse
import sys
import time
import pushsafer
from pushsafer import init, Client

#
# Settings
#
ENABLE_LOG = True
LOG_FILE = "/var/log/zabbix/pushsafer.log"


#
# Functions
#
def l(msg):
    """
    Send log line to stdout and to LOG_FILE if logging is enabled
    """
    msg = "[%s] %s" % (logTimeStamp(), msg)

    # Print to stdout
    print(msg)

    # Output to logfile
    if ENABLE_LOG:
        try:
            lf = open(LOG_FILE, 'a')
            lf.write("%s\n" % (msg))

        except (OSError) as exc:
            print("Error while trying to log event: %s" % rlb(str(exc)))
            return False
        
        lf.close()    

    return True


def logTimeStamp():
    """
    Return current date/time formatted for log output
    """
    return  time.strftime('%a %b %d %H:%M:%S %Y')


def rlb(thing):
  """
  Return thing with line breaks replaced by spaces
  """
  return thing.replace("\r", " ").replace("\n", " ")

#
# Main code
#

# client.send_message("Message", "Title", "Device or Device Group ID", "Icon", "Sound", "Vibration", "URL", "URL Title", "Time2Live", "Priority", "Retry", "Expire", "Answer", "Image 1", "Image 2", "Image 3")

# Arguments parser
parser = argparse.ArgumentParser(description='Send Zabbix notification to Pushsafer')
parser.add_argument('privatekey', metavar=('Private or Alias Key'), type=str, help='Pushsafer Private or Alias Key')
parser.add_argument('subject', metavar=('Subject'), type=str, help='Subject you want to push to the device(s).')
parser.add_argument('message', metavar=('Message'), type=str, help='Message you want to push to the device(s).')
parser.add_argument('device', metavar=('device'), type=str, help='Device or device group id to send message to.')
parser.add_argument('icon', metavar=('icon'), type=str, help='Icon number 1-177.')
parser.add_argument('sound', metavar=('sound'), type=str, help='Sound number 0-50, 0=silent, empty=device default.')
parser.add_argument('vibration', metavar=('vibration'), type=str, help='vibration number 0-3, how often the device should vibrate')
parser.add_argument('url', metavar=('url'), type=str, help='Link, URL or URL Scheme')
parser.add_argument('urltitle', metavar=('urltitle'), type=str, help='Title of URL')
parser.add_argument('time2live', metavar=('time2live'), type=str, help='number 0-43200, Time in minutes, after which message automatically gets purged')
parser.add_argument('priority', metavar=('priority'), type=str, help='-2 = lowest priority, -1 = lower priority, 0 = normal priority, 1 = high priority, 2 = highest priority')
parser.add_argument('retry', metavar=('retry'), type=str, help='number 60-10800 (60s steps), Time in seconds, after a message shuld resend.')
parser.add_argument('expire', metavar=('expire'), type=str, help='number 60-10800, Time in seconds, after the retry/resend should stop.')
parser.add_argument('confirm', metavar=('confirm'), type=str, help='number 10-10800, Time in seconds a message resend unitl it confirmed.')
parser.add_argument('answer', metavar=('answer'), type=str, help='1 = Answer is possible, 0 = Answer is not possible.')
parser.add_argument('answeroptions', metavar=('answeroptions'), type=str, help='predefined answer options divided by a pipe character e.g. Yes|No|Maybe')
parser.add_argument('answerforce', metavar=('answerforce'), type=str, help='1 = Force Answer')

# Argument processing
args = parser.parse_args()
privatekey = args.privatekey
subject = args.subject
message = args.message
device = args.device
icon = args.icon
sound = args.sound
vibration = args.vibration
url = args.url
urltitle = args.urltitle
time2live = args.time2live
priority = args.priority
retry = args.retry
expire = args.expire
confirm = args.confirm
answer = args.answer
answeroptions = args.answeroptions
answerforce = args.answerforce

# Try to send the notification
init(privatekey)
Client("").send_message(message, subject, device, icon, sound, vibration, url, urltitle, time2live, priority, retry, expire, confirm, answer, answeroptions, answerforce, "", "", "")

# Exit with success
l("Success: Message sent with Private Key [%s]: " % (privatekey))
sys.exit(0)
