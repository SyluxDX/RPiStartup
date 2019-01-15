# Raspberry Pi Startup
Colection of files and configurations for a fresh Raspbian instilation.  
These configurtions include:
 - `.nanorc` and syntax highlight files for:
   - C
   - Json
   - Python
   - XML
   - YAML
 - Some RPi Python scripts
 - RPi's Notes in `notes.txt`
## Setting up a Raspberry Pi headless
Once an image is created on an SD card, by inserting it into a card reader on a Linux or Windows machines the boot folder can be accessed. Adding certain files to this folder will activate certain setup features on the first boot of the Pi itself.

### Notable Boot folder contents:

 - `cmdline.txt`: The kernel command line passed in to the kernel when it boots.

 - `config.txt`: Contains many configuration parameters for setting up the Pi. See the config.txt section.

### Setting up wireless networking
You will need to define a wpa_supplicant.conf file for your particular wireless network. Put this file in the boot folder, and when the Pi first boots, it will copy that file into the correct location in the Linux root file system and use those settings to start up wireless networking.  
More information on the wpa_supplicant.conf file can be found [here](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=PT

network={
	ssid="Network Name"
	psk="Network Password"
}
```

### Enabling SSH
SSH can be enabled by placing a file called ssh in to the boot folder. This flags the Pi to enable the SSH system on the next boot.

## Adding the network details to the Raspberry Pi
The password can be configured either as the ASCII representation, in quotes as per the example above, or as a pre-encrypted 32 byte hexadecimal number.
You can use the `wpa_passphrase` utility to generate an encrypted PSK. This takes the SSID and the password, and generates the encrypted PSK.
With the example from above, you can generate the PSK with `wpa_passphrase "Network Name" "Network Password"`. The output is as follows:
```
network={
	ssid="testing"
	#psk="testingPassword"
	psk=131e1e221f6e06e3911a2d11ff2fac9182665c004de85300f9cac208a6a80531
  }
```

### Unsecured networks

If the network you are connecting to does not use a password, the `wpa_supplicant` entry for the network will need to include the correct `key_mgmt` entry. e.g.
```
network={
	ssid="testing"
	key_mgmt=NONE
}
```
### Hidden networks

If you are using a hidden network, an extra option in the `wpa_supplicant file`, `scan_ssid`, may help connection.
```
network={
    ssid="yourHiddenSSID"
    scan_ssid=1
    psk="Your_wifi_password"
}
```
