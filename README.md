# RCE-Webmin1.58
Remote Command Execution for CMS Webmin v1.580

Python 3 code usine
Exploit CVE:2012-2982

This module exploits an arbitrary command execution vulnerability in 
Webmin 1.580. The vulnerability exists in the /file/show.cgi 
component and allows an authenticated user, with access to the File 
Manager Module, to execute arbitrary commands with root privileges. 
The module has been tested successfully with Webmin 1.580 over 
Ubuntu 10.04.

resource: https://www.exploit-db.com/exploits/21851
