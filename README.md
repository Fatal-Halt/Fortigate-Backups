Fortigate-Backups
=================

Simple python script to backup a fortigate device using the admin-scp feature. 

=================

* Needs to have a reference to the pscp executable from putty or another scp client (and maybe some tweaking).
* The destination folder (by default C:\config\common name\ will need to exist before you run the script.
* You'll need to run the backup command once manually before this script will work, as the Firewalls key needs to be accepted. 

USAGE:
=================
* Replace <FirewallName>, <FirewallIP> with your devices to be backed up.
* Replace <PORT> with your device's SSH port.
* Replace <PRIVATE KEY> with the location of your private key
  * NOTE: if not using SSH Keys (WHICH YOU SHOULD), just remove the following: 
    * '-i', '\<PRIVATE KEY\>',
* Replace <USERNAME> with the username you're connecting with
* Replace <PASSWORD> with the password to unlock the SSH key. 
