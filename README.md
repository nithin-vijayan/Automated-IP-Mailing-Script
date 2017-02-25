# Automated-IP-Mailing-Script

# Default mailing server : iCloud
Refer to bottom to see how to change mail server

Script for automatically mail your IP address from your mail account as per required interval( Useful for remote dynamic IP machines whose IP is allocated on random basis)

Script can be set on remote machines which uses dynamic ip allocation so that even when the IP address changes you will get the updated IP.

This script is useful in scenarios where you want to ssh into an remote machine which uses dynamic IP but you have no way of knowing the ip currently in use.

Script can be moved to cron folder in etc and set to execute as cronjob

ex:

0 * * * * /usr/bin/python /etc/cron/mail.py  --- If you wish the script to be executed every hour

Refer to cronjob manual for setting up your cronjobs.
https://crontab.guru/

Script uses iCLoud mail server for mailing the IP. If the sender account is on different domain you can use the corresponding mail server by changing 'server' string variable

For iCloud smtp.me.com
For Gmail smtp.gmail.com







