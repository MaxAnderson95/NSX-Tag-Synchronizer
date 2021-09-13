# NSX Tag Synchronizer

A Python program that synchronizes NSX-T tags between VMs in a local manager with their SRM (VMware Site Recovery Manager) placeholder counterparts in another local manager. It matches VMs simply using the display name of the VM.

Run this program using a scheduler on a frequency of your choice (ex. every hour)

**note this program currently only supports basic auth and only supports NSX-T**

## Usage

```
usage: sync.py [-h] -hS NSX_HOST_SOURCE -uS USER_SOURCE -pS PASSWORD_SOURCE -hD NSX_HOST_DESTINATION -uD
               USER_DESTINATION -pD PASSWORD_DESTINATION

optional arguments:
  -h, --help            show this help message and exit
  -hS NSX_HOST_SOURCE, --nsx_host_source NSX_HOST_SOURCE
                        NSX host to pull tags from
  -uS USER_SOURCE, --user_source USER_SOURCE
                        User to authenticate as to the source host
  -pS PASSWORD_SOURCE, --password_source PASSWORD_SOURCE
                        Password to authenticate with to the source host
  -hD NSX_HOST_DESTINATION, --nsx_host_destination NSX_HOST_DESTINATION
                        NSX host to replicate tags to
  -uD USER_DESTINATION, --user_destination USER_DESTINATION
                        User to authenticate as to the source host
  -pD PASSWORD_DESTINATION, --password_destination PASSWORD_DESTINATION
                        Password to authenticate with to the source host
```

## Example Output

```
python sync.py --nsx_host_source localmanager1.domain.local --user_source admin --password_source P@ssw0rd --nsx_host_destination localmanager2.domain.local --user_destination admin --password_destination S3cur3!

Connected to NSX manager localmanager1.domain.local.
Connected to NSX manager localmanager2.domain.local.

Syncing new tags found for VM01:
Prod:Environment
ITM:Application

Syncing new tags found for VM02:
Prod:Environment
Patching:Shared Service
Ivanti:Application
```
