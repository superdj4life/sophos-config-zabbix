# sophos-config-Zabbix
Template to monitor the configuration of Sophos UTM v.9.6 by Zabbix > 6.2

Disclaimer:

This is forked from an 0.1alpha version of the template and script. I updated the code to run in Python 3.9, no changes were made to the template

This isn't an official template by Sophos Company or Zabbix SIA

Tested against Sophos v9.7 with REST API version 1.3

Tested on Zabbix 6.2

Usage: 
On your Sophos Firewall 
1. Enable REST service
2. Create an API key 

In Zabbix
1. Upload the template Configuration -> Templates -> import template
2. Copy the .py script to /usr/zabbix/externalscripts folder and adjust permissions 
      chmod 0755 sophos.py
3. *if needed, add pip requests dependency
      pip3 install requests    
4. Adjust template macros in Configuration -> Templates -> Sophos 9.6 Template -> Macros 
      {$SNMP_COMMUNITY} - Your SNMPv2 community string
      {$T_SOPHOS_API_PASSWORD} - API key configured in the Firewall section 
      {$T_SOPHOS_API_USER} - API user configured in the Firewall section
5. Press update to save changes 

