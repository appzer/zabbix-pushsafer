zabbix-pushsafer
=======================

![Pushsafer](https://www.pushsafer.com/de/assets/logos/logo.png)

A python script for sending [pushsafer.com](https://www.pushsafer.com/) notifications in ZABBIX.

Forked from and original created by: [sriccio](https://github.com/sriccio/zabbix-alertscripts)

Pushsafer make it easy and safe to get push-notifications in real time on your
- Android device
- iOS device (incl. iPhone, iPad, iPod Touch)
- Windows 10 Phone & Desktop
- Browser (Chrome & Firefox)

### Requirements
```bash
pip install python-pushsafer
```
### Usage
```
usage: zabbix-pushsafer.py [-h] privatekey Subject Message

For CentOS 7 use zabbix-pushsafer-centOS.sh!

Send Zabbix notification to Pushsafer enabled devices.

positional arguments:
  PrivateKey        Pushsafer Private or Alias Key
  Subject           Subject you want to push to the device(s).
  Message           Message you want to push to the device(s).

optional arguments:
  -h, --help        show this help message and exit
```
### Getting started
You first need to register for an account at [Pushsafer](https://www.pushsafer.com/) and download/install the clients for your devices (Android/iOS/Windows 10).
You will then able to retrieve your *PrivateKey* or *AliasKey* that you will need to provide in your zabbix user media configuration.

Copy the *zabbix-pushsafer.py* script to your Zabbix alert scripts directory. Usually this is */usr/lib/zabbix/alertscripts* but configuration can differs depending on how you installed Zabbix. In doubt, check your *zabbix_server.conf*.

### Configure the media type

Go to your Zabbix *Administration / Media types* screen and add a new media.
Specify the name of the script in script name and check that the parameters are correct.

![Configuration screen](https://www.pushsafer.com/assets/examples/zabbix01.jpg)

### Configure the user media

You will need then to add the media to your users. For this just edit an user and add a media selecting the one you just created before.
Specify the Private or Alias Key in the *Send to* field.

![Configuration screen](https://www.pushsafer.com/assets/examples/zabbix02.jpg)
