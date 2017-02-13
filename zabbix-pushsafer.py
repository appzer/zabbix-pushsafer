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

# Arguments parser
parser = argparse.ArgumentParser(description='Send Zabbix notification to Pushsafer')
parser.add_argument('privatekey', metavar=('Private or Alias Key'), type=str, help='Pushsafer Private or Alias Key')
parser.add_argument('subject', metavar=('Subject'), type=str, help='Subject you want to push to the device(s).')
parser.add_argument('message', metavar=('Message'), type=str, help='Message you want to push to the device(s).')

# Argument processing
args = parser.parse_args()
privatekey = args.privatekey
subject = args.subject
message = args.message

# Try to login with privatekey
try:
    po = pushsafer.Client(privatekey)
except (pushsafer.UserError) as exc:
    l("Error: Can't connect to Pushsafer with Private Key [%s]: " % privatekey)
    sys.exit(1)

# Try to send the notification
try:
    po.send_message(message, subject, "", "", "", "", "", "", "0", "", "", "")
except (pushsafer.RequestError) as exc:
    l("Error: Can't send notification to Pushsafer devices: %s" % rlb(str(exc)))
    sys.exit(1)

# Exit with success
l("Success: Message sent with Private Key [%s]: " % (privatekey))
sys.exit(0)