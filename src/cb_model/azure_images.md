
# Whitelisted Images

## Import Whitelisted Images
To enable whitelisted Azure images, go to the "THEN" clause for the Rule titled "Fetch and Cache Available Azure Images", and click the the pencil icon to edit and set "Default value for Use whitelist" to TRUE.

Click the "Run" icon to start the image import process. It will complete in a matter of seconds, and the whitelist zure images will appear in the image import UI for the Azure Resource Handler

## Available Whitelisted Images

This list was generated from running the following in `shell_plus`:
```python
from resourcehandlers.azure_arm.azure_constants import azure_image_whitelist
for i in azure_image_whitelist:
    print(f"| {i[0]} | {i[1]} | {i[2]} | {i[3]} |")
```

| | | | |
|-|-|-|-|
| Publisher | Offer | SKU | Version | 
| redhat | RHEL | 7-LVM | latest |
| redhat | RHEL | 7.2 | latest |
| redhat | RHEL | 7.3 | latest |
| redhat | RHEL | 7.4 | latest |
| redhat | RHEL | 7.5 | latest |
| redhat | RHEL | 7.6 | latest |
| redhat | RHEL | 7.7 | latest |
| redhat | RHEL | 7.8 | latest |
| redhat | RHEL | 7_9 | latest |
| redhat | RHEL | 8 | latest |
| redhat | RHEL | 8-LVM | latest |
| redhat | RHEL | 8.1 | latest |
| redhat | RHEL | 8.2 | latest |
| redhat | RHEL | 8_3 | latest |
| redhat | RHEL | 8_4 | latest |
| redhat | RHEL | 8_5 | latest |
| openlogic | CentOS | 6.9 | latest |
| openlogic | CentOS | 6.10 | latest |
| openlogic | CentOS | 7.2 | latest |
| openlogic | CentOS | 7.3 | latest |
| openlogic | CentOS | 7.4 | latest |
| openlogic | CentOS | 7.5 | latest |
| openlogic | CentOS | 7.6 | latest |
| openlogic | CentOS | 7.7 | latest |
| openlogic | CentOS | 7_8 | latest |
| openlogic | CentOS | 7_9 | latest |
| openlogic | CentOS | 8.0 | latest |
| openlogic | CentOS | 8_1 | latest |
| openlogic | CentOS | 8_2 | latest |
| openlogic | CentOS | 8_3 | latest |
| openlogic | CentOS | 8_4 | latest |
| openlogic | CentOS | 8_5 | latest |
| canonical | UbuntuServer | 12.04.5-LTS | latest |
| canonical | UbuntuServer | 14.04.5-LTS | latest |
| canonical | UbuntuServer | 16.04.0-LTS | latest |
| canonical | UbuntuServer | 18.04-LTS | latest |
| canonical | 0001-com-ubuntu-server-focal | 20_04-lts | latest |
| MicrosoftWindowsServer | WindowsServer | 2008-R2-SP1 | latest |
| MicrosoftWindowsServer | WindowsServer | 2012-Datacenter | latest |
| MicrosoftWindowsServer | WindowsServer | 2012-R2-Datacenter | latest |
| MicrosoftWindowsServer | WindowsServer | 2016-Datacenter | latest |
| MicrosoftWindowsServer | WindowsServer | 2019-Datacenter | latest |
| MicrosoftWindowsServer | WindowsServer | 2022-Datacenter | latest |


