# Initial Appliance Setup

* When a CloudBolt is first deployed there is a series up steps required to prepare the appliance for operation. 
* This process starts with the application of a license and confirmation of the appliance personality. 
* After applying the license, appliance setup will continue -- this usually takes 5-10 minutes.
* Once setup is complete, a login dialog is displayed where the user enters the default username/password.
* The EULA is displayed.
* User prompted for proxy settings. If no proxy, it's safe to skip
* The Administrator Setup form is displayed -- complete and submit
  * Supply: First, Last name, username, email address, password, select a reset question and supply an answer, and specify a root group name (usually name of the organization)
* Now we can select a Provider to setup.
    * Guided setup is available for vCenter, Azure, and AWS
    * Users can also jump straight to CMP dashboard, admin settings, or environments

vCenter Setup
* submit host, username, password
* select poc-cluster and click "import clusters"
* select all templates and click "import templates"
* select network poc-user-net-200 and click "Connect Default network"
* For the environment setup, just click "start using cloudbolt" to continue





