<!-- font check: Wingdings is not a standard text face; glyphs "" on pages 20-21, 28-29, 35, 42, 45, 50-51, 60, 63-64, 73, 93, 114, 136-137. Verify against the rendered page before trusting or mapping. -->

<!-- font check: U+F06C (private-use code from Wingdings) on pages 114; the character carries no meaning as text, read the rendered page -->

<!-- font check: U+F09F (private-use code from Wingdings) on pages 20-21, 28-29, 35, 42, 45, 50-51, 60, 63-64, 73, 93, 136-137; the character carries no meaning as text, read the rendered page -->

<!-- pdf page 1 -->

              Software Manual
RobustOS Product User Guide

               MG460
      Software Manual

                  Guangzhou Robustel Co., Ltd.
                          www.robustel.com

<!-- figure 1 on pdf page 1 at 55,77-170,122 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 48) -->
<!-- figure 2 on pdf page 1 at 0,185-536,341 pt | caption: none | text-layer labels: MG460 Software Manual | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 1 at 301,703-531,751 pt | caption: none; nearest centred text below: "Guangzhou Robustel Co., Ltd. www.robustel.com" | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 94) -->
robust
<!-- end of figure 3 -->

<!-- pdf page 2 | printed page 2 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

About this Document
This document provides web interface information of the RobustOS Pro based gateway products, including gateway
configuration and operation.

Related Products
MG460

Copyright©2025 Guangzhou Robustel Co., Ltd.
All rights reserved.

Trademarks and Permissions
            &                 are trademarks of Guangzhou Robustel Co., Ltd.. All other trademarks and trade

names mentioned in this document are the property of their respective owners.

Disclaimer
No part of this document may be reproduced in any form without the written permission of the copyright owner.
The contents of this document are subject to change without notice due to continued progress in methodology,
design and manufacturing. Robustel shall have no liability for any error or damage of any kind resulting from the
failing use of this document.

Technical Support
Tel: +86-20-82321505
Email: support@robustel.com
Web: www.robustel.com

<!-- pdf page 3 | printed page 3 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Document History
Updates between document versions are cumulative. Therefore, the latest document version contains all updates
made to previous versions.

 Date                    Firmware Version     Document Version     Change Description
 June 17, 2024           2.1.3                1.0.0                Initial release.
 December 23, 2024       2.1.7                1.0.1                1. Separated HBT and ALF into two tabs in
                                                                         BAM.
                                                                   2. Removed IPV6-related features.
                                                                   3. Added a multi-destination address
                                                                         option in Traffic Rules.
                                                                   4. Included a VPN toggle option in DIDO.
                                                                   5. Added COM1/2 options for the USR light
                                                                         in the Advanced Configuration.
                                                                   6. Changed GPS to GNSS on the web
                                                                         interface.
                                                                   7. Added an Overridden DNS option on the
                                                                         WAN interface.

<!-- figure 1 on pdf page 3 at 33,137-559,377 pt | caption: none | text-layer labels: Date June 17, 2024 December 23, 2024 | Firmware Version 2.1.3 2.1.7 | Document Version 1.0.0 1.0.1 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 4 | printed page 4 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

                                                                              Contents
Chapter 1 Initial Configuration ..............................................................................................................................6
    1.1 PC Configuration .................................................................................................................................................. 6
    1.2 Factory Default Settings .......................................................................................................................................9
    1.3 Factory Reset ....................................................................................................................................................... 9
    1.4 Log in the Device ................................................................................................................................................10
    1.5 Control Panel ..................................................................................................................................................... 11
Chapter 2 WebUI Descriptions ............................................................................................................................ 13
    2.1 Dashboard ..........................................................................................................................................................13
          2.1.1 Overview .................................................................................................................................................13
          2.1.2 Modem ................................................................................................................................................... 13
          2.1.3 Ethernet .................................................................................................................................................. 14
          2.1.4 Internet Status ........................................................................................................................................ 14
          2.1.5 LAN Status ...............................................................................................................................................14
          2.1.6 System Resource .....................................................................................................................................15
          2.1.7 System Information .................................................................................................................................15
          2.1.8 Cellular Status ......................................................................................................................................... 16
          2.1.9 RCMS Status ............................................................................................................................................16
    2.2 Interface .............................................................................................................................................................17
          2.2.1 Ethernet .................................................................................................................................................. 17
          2.2.2 Cellular .................................................................................................................................................... 18
          2.2.3 Bridge ......................................................................................................................................................24
          2.2.4 Wi-Fi ........................................................................................................................................................24
          2.2.5 USB ..........................................................................................................................................................25
          2.2.6 VLAN ....................................................................................................................................................... 26
          2.2.7 DI/DO ...................................................................................................................................................... 27
          2.2.8 Serial Port ................................................................................................................................................30
          2.2.9 BAM ........................................................................................................................................................ 37
    2.3 Network ............................................................................................................................................................. 40
          2.3.1 WAN ........................................................................................................................................................ 40
          2.3.2 LAN ..........................................................................................................................................................44
          2.3.3 Route .......................................................................................................................................................46
          2.3.4 Policy Route ............................................................................................................................................ 48
          2.3.5 Firewall ....................................................................................................................................................49
          2.3.6 QoS ..........................................................................................................................................................56
    2.4 VPN .................................................................................................................................................................... 58
          2.4.1 IPsec ........................................................................................................................................................ 58
          2.4.2 OpenVPN ................................................................................................................................................ 66
          2.4.3 GRE ..........................................................................................................................................................74
          2.4.4 PPTP ........................................................................................................................................................ 76
          2.4.5 L2TP .........................................................................................................................................................80
          2.4.6 DMVPN ................................................................................................................................................... 83
    2.5 Services .............................................................................................................................................................. 88
          2.5.1 Syslog ...................................................................................................................................................... 88
          2.5.2 Event ....................................................................................................................................................... 89

<!-- pdf page 5 | printed page 5 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

         2.5.3 NTP ..........................................................................................................................................................94
         2.5.4 SMS ......................................................................................................................................................... 95
         2.5.5 Email ....................................................................................................................................................... 97
         2.5.6 DDNS ....................................................................................................................................................... 98
         2.5.7 VRRP ......................................................................................................................................................100
         2.5.8 SSH ........................................................................................................................................................ 101
         2.5.9 GNSS ..................................................................................................................................................... 101
         2.5.10 RCMS ...................................................................................................................................................105
         2.5.11 SNMP .................................................................................................................................................. 109
         2.5.12 Web Server ......................................................................................................................................... 113
         2.5.13 Advanced ............................................................................................................................................ 113
    2.6 System ..............................................................................................................................................................115
         2.6.1 Debug ....................................................................................................................................................115
         2.6.2 Certificate Manager .............................................................................................................................. 118
         2.6.3 Resource Graph .................................................................................................................................... 122
         2.6.4 App Center ............................................................................................................................................ 127
         2.6.5 Tools ......................................................................................................................................................127
         2.6.6 Flash Manager ...................................................................................................................................... 131
         2.6.7 Service Management ............................................................................................................................132
         2.6.8 Profile ....................................................................................................................................................133
         2.6.9 User Management ................................................................................................................................ 134
         2.6.10 DEB Management ............................................................................................................................... 136
         2.6.11 Role Management .............................................................................................................................. 137
Chapter 3 Configuration Examples .................................................................................................................... 141
    3.1 Cellular ............................................................................................................................................................. 141
         3.1.1 Cellular APN Manual Setting and Cellular Dial-up. ...............................................................................141
         3.1.2 SMS Remote Control .............................................................................................................................143
    3.2 VPN Configuration Examples ........................................................................................................................... 146
         3.2.1 IPsec VPN .............................................................................................................................................. 146
         3.2.2 OpenVPN .............................................................................................................................................. 150
         3.2.3 GRE VPN ................................................................................................................................................153
Chapter 4 Introductions for CLI ......................................................................................................................... 156
    4.1 What Is CLI ....................................................................................................................................................... 156
    4.2 How to Configure the CLI .................................................................................................................................157
    4.3 Commands Reference ......................................................................................................................................157
    4.4 Quick Start with Configuration Examples ........................................................................................................ 158
    Example 1: Show current version .......................................................................................................................... 158
    Example 2: CLI for setting Cellular ......................................................................................................................... 158
Chapter 5 Glossary ........................................................................................................................................... 161

<!-- pdf page 6 | printed page 6 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Chapter 1 Initial Configuration
The device can be configured through your web browser that including Microsoft Edge, Chrome and Firefox, etc. A
web browser is included as a standard application in the following operating systems: Linux, Mac OS, Windows. It
provides an easy and user-friendly interface for configuration. There are various ways to connect the device, either
through an external repeater/hub or connect directly to your PC. However, make sure that your PC has an Ethernet
interface properly installed prior to connecting the device. You must configure your PC to obtain an IP address
through a DHCP server or a fixed IP address that must be in the same subnet as the device. If you encounter any
problems accessing the device web interface, it is advisable to uninstall your firewall program on your PC, as this
tends to cause problems accessing the IP address of the device.

1.1 PC Configuration

There are two ways to get an IP address for the computer. One is to obtain an IP address automatically from “Local
Area Connection”, and another is to configure a static IP address manually within the same subnet of the router.
Please refer to the steps below.

Here take Windows 10 as an example.The configuration for Windows 7 or newer is similar.
1. Right-click “Windows LOGO” on the taskbar, select “Run”, and type "Control" to launch the Control panel, then
    Click “View network status and tasks”.

<!-- figure 1 on pdf page 6 at 55,437-440,674 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 90/95 words >= 60, mean confidence 92) -->
x
Panel
4 Control Panel
o
Search Control Panel
v
Adjust your computer's settings
View by: Category
System and Security
User Accounts
Review your computer's status
9 Change account type
Save backup copies of your files with File History
Back up and Restore (Windows 7)
Appearance and Personalisation
Network and Internet
Clock and Region
Hardware and Sound
Change date, time or number formats
View devices and printers
Ease of Access
Add a device
Let Windows suggest settings
Adjust commonly used mobility settings
Optimise visual display
6)
Programs
Uninstall a program
<!-- end of figure 1 -->

<!-- pdf page 7 | printed page 7 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.   After entering “Network and Sharing Center", click "Ethernet" connections status.

3.   Click Properties in the window of Network Connection status.

<!-- figure 1 on pdf page 7 at 55,84-442,329 pt | caption: none | text-layer labels: none | nearby labels: 2. | 3. | OCR text follows (tesseract, unverified; 104/110 words >= 60, mean confidence 92) -->
x
Network and Sharing Centre
4 All Control Panel Items Network and Sharing Centre
v
View your basic network information and set up connections
Control Panel Home
View your active networks
Change adapter settings
Network 8
Access type:
Internet
Change advanced sharing
settings
Private network
Connections:
Media streaming options
Network 13
Access type:
No Internet access
Public network
Connections: Test LAN
Change your networking settings
Set up a new connection or network
Set up a broadband, dial-up or VPN connection, or set up a router or access point.
Troubleshoot problems
Diagnose and repair network p
or get
See also
Internet Options
Windows Defender Firewall
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 7 at 55,369-246,597 pt | caption: none | text-layer labels: none | nearby labels: 3. | OCR text follows (tesseract, unverified; 30/36 words >= 60, mean confidence 83) -->
Ethernet 2 Status
General
Connection
IPv4 Connectivity:
Internet
IPv6 Connectivity:
No Internet access
Media State:
Enabled
13 days 05:40:54
Duration:
1.0 Gbps
Speed:
Activity
Sent Received
Bytes:
828,675,176
2,751,829,674
Close
<!-- end of figure 2 -->

<!-- pdf page 8 | printed page 8 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

4.   Choose Internet Protocol Version 4 (TCP/IPv4) and click Properties.

5.   Two ways to configure the IP address of the computer.
     (1) Auto obtain from the DHCP server, click "Obtain an IP address automatically".

<!-- figure 1 on pdf page 8 at 55,89-241,326 pt | caption: none | text-layer labels: none | nearby labels: 4. | 5. | OCR text follows (tesseract, unverified; 62/67 words >= 60, mean confidence 88) -->
Ethernet 2 Properties
Networking Sharing
Connect using:
Intel(R) 1211 Gigabit Network Connection
This connection uses the following items:
for Microsoft Networks
and Printer Sharing for Microsoft Networks
Packet Driver (NPCAP)
Microsoft Network Adapter Multiplexor Protocol
Microsoft LLDP Protocol Driver
Uninstall
Install
ins
Description
Transmission Control Protocol/Intemet Protocol. The default
wide area network protocol that provides communication
across diverse interconnected networks.
OK
Cancel
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 8 at 55,386-261,612 pt | caption: none | text-layer labels: none | nearby labels: 5. | OCR text follows (tesseract, unverified; 65/70 words >= 60, mean confidence 89) -->
Internet Protocol Version 4 Properties
General Alternative Configuration
You can get IP settings assigned automatically if your network supports
this capability. Otherwise, you need to ask your network administrator
for the appropriate IP settings.
Obtain an IP address automatically
the following IP address:
IP address:
Subnet mask:
Default
at
lly:
the following DNS server addresses:
Preferred Dh
er
Alter
DNS server:
Validate settings upon exit
<!-- end of figure 2 -->

<!-- pdf page 9 | printed page 9 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

     (2) Manually configuration the PC with a static IP address on the same subnet as the device address, click and
configure "Use the following IP address";

6.   Click OK to finish the configuration.

1.2 Factory Default Settings

Before configuring your device, you need to know the following default settings.
 Item                     Description
 Username                 admin
 Password                 See the information from the product label
 ETH0                     WAN mode
 ETHn                      192.168.0.1/255.255.0.0, LAN mode
 DHCP Server               Enabled

1.3 Factory Reset

 Function                  Operation
 Reboot                    Press and hold the RST button for 2~5 seconds under the operating status.
 Restore to default        Press and hold the RST button for 5 ~10 seconds under the operating status. The RUN
 configuration             light flashes quickly, and then release the RST button, and the device will restore to the
                           default configuration.
 Restore to factory        Once the operation of restoring the default configuration is performed twice within one
 configuration             minute, the device will restore to the factory default settings.

<!-- figure 1 on pdf page 9 at 53,106-258,331 pt | caption: none | text-layer labels: none | nearby labels: 6. | Click OK to finish the configuration. | OCR text follows (tesseract, unverified; 74/79 words >= 60, mean confidence 92) -->
Internet Protocol Version 4 (TCP/IPv4) Properties
General
You can get IP settings assigned automatically if your network supports
this capability. Otherwise, you need to ask your network administrator
for the appropriate IP settings.
Obtain an IP address automatically
Use the following IP address:
IP address:
168.
2
Subnet mask:
Default gateway:
Obtain DNS server address automatically
Use the following DNS server addresses:
Preferred DNS server:
8
Alternative DNS server:
(Validate settings upon exit
Advanced.
<!-- end of figure 1 -->

<!-- pdf page 10 | printed page 10 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

1.4 Log in the Device

To log in to the management page and view the configuration status of your device, please follow the steps below.
1. On your PC, open a web browser such as Microsoft Edge, Google Chrome or Firefox, etc.
2. From your web browser, type the IP address of the device into the address bar and press enter. The default IP
     address of the device is https://192.168.0.1/24 ,though the actual address may vary.
     Note: If a SIM card with a public IP address is inserted in the device , enter this corresponding public IP address
     in the browser’s address bar to access the device wirelessly.

3.   In the login page, enter the username and password, you can check the login information from the device’s stick,
     and then click LOGIN. See the information on the product label for default username and password.
     Note: If enter the wrong password over 6 times, the user account will be locked for 5 minutes.

<!-- figure 1 on pdf page 10 at 53,321-313,487 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/7 words >= 60, mean confidence 68) -->
admin
Enter Passwo d
<!-- end of figure 1 -->

<!-- pdf page 11 | printed page 11 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

1.5 Control Panel

After logging in, the home page of the web interface is displayed.

From the homepage, users can find the model information and perform operations such as saving the configuration,
restarting the device , and logging out.
                                                      Control Panel
 Item             Description                                                                        Icon
 Save & Apply The icon is in gray by default, and will turn red if any modifications on
                  configuration, then click to save the current configuration into device’s flash
                  and apply the modification on every configuration page, to make the                  or
                  modification taking effect.
 Restart          Click to restart all the RobustOS Pro operating system based
                  applications(applications controlled by 11ystem are not included), then switch
                  to the login page.
 Reboot           Click to reboot the device, then switch to the login page.

 Logout          Click to log the current user out safely. After logging out, it will switch to login
                 page. Shut down web page directly without logout, the next one can login web
                 on this browser without a password before timeout.

<!-- figure 1 on pdf page 11 at 41,146-124,508 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/10 words >= 60, mean confidence 56) -->
Interface
=o
Network
Services
System
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 11 at 339,173-552,499 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 65/71 words >= 60, mean confidence 89) -->
Internet Traffic
CPU Temperature
39.0°C
OKB
Ethernet
ETH1 ETH2
ETHO
ETH3
ETH4
Lan Status
IP Address
192.168.0.1
MAC Address
34:FA:40:25:25:08
System Information
Operating System
Debian GNU/Linux 11.2
Mon Dec 23 15:42:20 2024 (NTP not
System Time
updated)
Firmware Version
2.1.7
Hardware Version
1.0
Kernel Version
Serial Number
01470000624100001
RCMS Status
RobustLink Status
ILink Last C:
RobustVPN Status
RobustVPN Last Connected
RobustVPN Virtual IP
Add:
VPN
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 11 at 129,259-332,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
Internet Status
Active Link
IP Address
Gateway
DNS
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 11 at 129,345-335,422 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 85) -->
System Resource
0%
CPU
Storage
Quad Core
242M/55798M
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 11 at 129,429-332,499 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/12 words >= 60, mean confidence 88) -->
Cellular Status
Modem Model
Network Registration
RSRP(dBm)
RSRQ(dB)
ENDC state
Inactive
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 11 at 33,710-110,770 pt | caption: none | text-layer labels: Logout | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 11 at 471,710-559,770 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 53) -->

<!-- pdf page 12 | printed page 12 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Note: The steps of how to modify configuration are as bellow:
      1. Modify in one page;

      2. Click              under this page;

      3. Modify in another page;

      4. Click              under this page;

      5. Complete all modification;

      6. Click      for save and apply.

<!-- pdf page 13 | printed page 13 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Chapter 2 WebUI Descriptions

2.1      Dashboard

2.1.1 Overview

 Item                       Description
 System Uptime              Show the current amount of time the router has been powered on.
 Internet Uptime            Show the current amount of time the router has been connected to internet.
 CPU Temperature            Show the CPU temperature.
 Traffic                    Show the amount of WWAN data traffic usage.

2.1.2 Modem

This page shows the status of SIM card.

       Item         Description

                    Not connected.

                    Weak signal.

                    Medium signal.

                    Strong signal.

<!-- figure 1 on pdf page 13 at 514,271-559,355 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 13 at 33,470-411,513 pt | caption: none | text-layer labels: none | nearby labels: Item | Description | OCR text follows (tesseract, unverified; 7/8 words >= 60, mean confidence 80) -->
4 (-105dBm)
SIM1 al
WCDMA
SIM2
CHN-UNICOM
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 13 at 33,532-409,688 pt | caption: none | text-layer labels: Item | Description | Not connected. | Weak signal. | Medium signal. | Strong signal. | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 72) -->
al
il
<!-- end of figure 3 -->

<!-- pdf page 14 | printed page 14 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.1.3 Ethernet

This page shows the device’s Ethernet status

     Icon      Description

               Port disable or link down.

               Link up.

2.1.4 Internet Status

This page shows the device’s Internet status information.

 Item                        Description
 Active Link                 Show the currently online link.
 IP Address                  Show the address of current link.
 Gateway                     Show the gateway address of the current link.
 DNS                         Show the current DNS server.

2.1.5 LAN Status

This page shows the device’s LAN status

 Item                        Description
 IP Address                  Show the IP address of the LAN.
 MAC Address                 Show the MAC address of the LAN.

<!-- figure 1 on pdf page 14 at 33,187-316,271 pt | caption: none | text-layer labels: Icon | Description | Port disable or link down. | Link up. | OCR: no legible text (0/1 words >= 60, mean confidence 31) -->
<!-- figure 2 on pdf page 14 at 96,465-163,549 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 14 at 380,465-559,549 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 14 at 108,712-163,765 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 14 at 330,712-559,765 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 15 | printed page 15 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.1.6 System Resource

This page shows the device’s system resources usage information.
When the usage is more than 95%, the icon will be in Red.
When the usage is between 80% and 95%, the icon will be in Yellow.
When the usage is less than 80%，the icon will be in Green.

2.1.7 System Information

This page shows the device’s system information.

 Item                       Description
 Operating System           Show the operating system information.
 System Time                Show the current system time.
 Firmware Version           Show the firmware version running on the device.
 Hardware Version           Show the current hardware version.
 Kernel Version             Show the current kernel version.
 Serial Number              Show the serial number of your device.

<!-- figure 1 on pdf page 15 at 33,180-316,278 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/10 words >= 60, mean confidence 81) -->
29%
CPU
RAM
Storage
Solo Core
2.6G/7.1G
192M/448M
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 15 at 33,401-371,473 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 22/22 words >= 60, mean confidence 94) -->
Operating System
Debian GNU/Linux 11.2
System Time
Mon Jun 19 05:06:53 2023 (NTP not
updated)
2.1.3 (4f342e97)
Firmware Version
Hardware Version
13
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 15 at 394,525-559,643 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 16 | printed page 16 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.1.8 Cellular Status

This page shows the device’s cellular status.

 Item                        Description
 Modem Vendor                Show the radio module vendor information.
 Modem Model                 Show the model of the radio module.
 Network Registration        Show the current network registration information.
 IMEI                        Show the IMEI (International Mobile Equipment Identity) number of the radio module.
 IMSI                        Show the IMSI (International Mobile Subscriber Identity) number of the current SIM.

2.1.9 RCMS Status

This page shows the device’s RCMS status.

 Item                             Description
 RobustLink Status                Show the status of RobustLink
 RobustelLink Last Connected      Show the last connected times of RobustLink
 RobustVPN Status                 Show the status of RobustVPN
 RobustVPN Last Connected         Show the last connected times of RobustVPN
 RobustVPN Virtual IP             Show the virtual IP of RobustVPN
 RobustVPN SubNet Address         Show the subnet address of RobustVPN

<!-- figure 1 on pdf page 16 at 390,624-559,739 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 17 | printed page 17 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.2      Interface

2.2.1 Ethernet

This section allows you to set the related parameters for Ethernet. There are 5 Ethernet ports in the device. The ETH0
is the WAN port, and others are the LAN port.

Ports

Click   to configure its parameters, and modify the port assignment parameters in the pop-up window.

 Item               Description                                                                            Default
 Name               Name of the port.                                                                      --
 Port               Show the editing port, read only.                                                      --
 Enable Ethernet    Click the toggle button to enable/disable the Ethernet port.                           ON

<!-- figure 1 on pdf page 17 at 43,297-543,463 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 14/23 words >= 60, mean confidence 70) -->
Name
Port
MTU
1500
port2
1500
port3
eth2
1500
port4
eth3
1500
eth4
1500
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 17 at 33,499-545,696 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 10/12 words >= 60, mean confidence 87) -->
Name
porti
Port
Enable Ethernet
Port Speed
Auto
MTU
1500
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 17 at 399,712-504,782 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 18 | printed page 18 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Port Speed         Select from “Auto”, “10M-half”, “10M-full”,“100M-half”, “100M-full”,“1000M-half”,    Auto
                    “1000M-full”.
 MTU                Enter the value of the maximum transmission unit(MTU).                               1500

Status

This page allows you to view the status of Ethernet port.

2.2.2 Cellular

This section allows you to set the related parameters of Cellular. The device supports one cellular modem and two
SIM slots, but only one SIM slot is activated at any time.

Cellular

<!-- figure 1 on pdf page 18 at 69,65-122,118 pt | caption: none | text-layer labels: none | nearby labels: Port Speed | MTU | Status | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 18 at 45,249-540,413 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 86) -->
Index
Link
Port
Down
Down
eth2
Down
eth3
Up
eth4
Down
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 18 at 41,640-557,770 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/16 words >= 60, mean confidence 75) -->
v]
Primary Sim
Enable Auto Switching
Enable Auto Revert
[30
Revert Interval
<!-- end of figure 3 -->

<!-- pdf page 19 | printed page 19 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                    Description                                                                            Default
 Primary Sim             Select one Sim card as primary Sim card                                                SIM1
 Enable Auto Switching   When auto switching is enabled, the SIM card will be automatically switched            ON
                         to another one when there is SIM card error or connection error or ping fails
                         by default.
 Enable Auto Revert      When auto switching is enabled, the backup SIM card will be automatically switched     OFF
                         to primary sim card when backup SIM card online time is greater than revert interval
                         time.
 Revert Interver         Duation of auto revert, the unit is minuts.                                            30

 Item                    Description                                                                            Default
 Weak Signal             Switch to another SIM card when the signal is poor, only used for dual SIM             ON
                         backup.
 While Roaming           Switch to another SIM card while roaming, only used for dual SIM backup.               OFF

Click   to configure its parameters in the pop-up window.

<!-- figure 1 on pdf page 19 at 36,249-557,329 pt | caption: none | text-layer labels: none | nearby labels: Revert Interver | 30 | Item Weak Signal | Default ON | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 85) -->
Additional Switching Rules
Weak Signal
While Roaming
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 19 at 100,333-148,403 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 19 at 33,415-559,520 pt | caption: none | text-layer labels: none | nearby labels: While Roaming | Click | OFF | OCR text follows (tesseract, unverified; 17/20 words >= 60, mean confidence 89) -->
Index
SIM Card
Phone Number
Network Type
Band Select Type
All
1
SIM1
Auto
All
SIM2
Auto
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 19 at 33,556-557,770 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 17/19 words >= 60, mean confidence 84) -->
[1
Index
SIM Card
Automatic APN Selection
Phone Number
PIN Code
Extra AT Cmd
lo
Telnet Port
<!-- end of figure 4 -->

<!-- pdf page 20 | printed page 20 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                        Description                                                                   Default
 Index                       Indicate the ordinal of the list.                                             --
 SIM Card                    Show the currently editing SIM card.                                          --
 Automatic APN Selection     Click the toggle button to enable/disable the “Automatic APN Selection”       ON
                             option. After enabling, the device will recognize the access point name
                             automatically. Alternatively, users can disable this option and manually
                             add the access point name.
 Phone Number                Enter the phone number of the SIM card.                                       Null
 PIN Code                    Enter a 4-8 characters PIN code used for unlocking the SIM.                   Null
 Extra AT Cmd                Enter the AT commands used for cellular initialization.                       Null
 Telnet Port                 Specify the Port listening of telnet service, used for AT over Telnet. 0      0
                             means not supported.

When the Automatic APN Selection is off, users can specify their own APN setting.

 Item                        Description                                                                   Default
 APN                         Enter the Access Point Name for cellular dial-up connection, provided by      internet
                             local ISP.
 Username                    Enter the username for cellular dial-up connection, provided by local ISP.    Null
 Password                    Enter the password for cellular dial-up connection, provided by local ISP.    Null
 Authentication Type         Select the authentication type. Select from “None”, “CHAP”, “PAP”.            None
                              None: None.
                              CHAP: Challenge-Handshake Authentication Protocol.
                              PAP: Password Authentication Protocol.

This page allows you to configure cellular network settings. type and network band. You can specify a specific
frequency band or network type for device.

 Item                        Description                                                                   Default
 Network Type                Select the cellular network type, which is the network access order. Select   Auto

<!-- figure 1 on pdf page 20 at 492,82-559,276 pt | caption: none | text-layer labels: Default -- -- ON | Null Null Null 0 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 20 at 33,84-160,276 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 20 at 33,461-160,607 pt | caption: none | text-layer labels: Item APN | Username Password Authentication Type | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 20 at 497,461-559,607 pt | caption: none | text-layer labels: Default internet | Null Null None | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 20 at 33,616-559,693 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 87) -->
Cellular Network Settings
Network Type
Auto
Band Select Type
<!-- end of figure 5 -->

<!-- pdf page 21 | printed page 21 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

                       from “Auto”, “2G Only”, “3G Only”, “4G Only”, “5G Only”.
                        Auto: Connect to the best signal network automatically
                        2G Only: Only the 2G network is connected
                        3G Only: Only the 3G network is connected
                        4G Only: Only the 4G network is connected
                        5G Only: Only the 5G network is connected

                       Note:
                            1) There may be some different optional network types due to the
                       different cellular module.
Band Select Type       Select from “All” or “Specify”. You may choose certain bands if choosing      All
                       “Specify”.

                       Note:
                       There may be some differences in Band Setting due to the different cellular
                       module.

Item                   Description                                                                   Default
Debug Enable           Click the toggle button to enable/disable this option. Enable for debugging   ON
                       information output.
Verbose Debug Enable   Click the toggle button to enable/disable this option. Enable for verbose     OFF
                       debugging information output.
RSSI Threshold         Is used to judge whether the signal is too weak to switch SIM, unit: dbm.     -87
RSRP Threshold         Is used to judge whether the signal is too weak to switch SIM, unit: dbm.     -105
Timeout For Network    The timeout required for the module to register to the network. Unit:         150
Registration           seconds. 0 means the default setting is used.

<!-- figure 1 on pdf page 21 at 33,65-160,321 pt | caption: none | text-layer labels: Band Select Type | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 21 at 438,65-559,321 pt | caption: none | text-layer labels: All | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 21 at 33,338-557,499 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/19 words >= 60, mean confidence 79) -->
Debug Enable
Verbose Debug Enable
RSSI Threshold
RSRP Threshold
E
Timeout For Network Registration
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 21 at 108,518-158,667 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 22 | printed page 22 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Status

This page allows you to view the status of the cellular connection.

Click the row of status, the detailed status information will be displayed under the row.

<!-- figure 1 on pdf page 22 at 36,163-555,206 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 81) -->
Status
Index
Modem Status
Modem Model
Registration
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 22 at 36,295-519,780 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 89/91 words >= 60, mean confidence 94) -->
Index
Modem Status
Modem Model
IMSI
Registration
Ready
EG25
46001
0493
Registered to home network
Index
1
Modem Status
Ready
Modem Vendor
quectel
Modem Model
EG25
Current SIM
SIM1
Phone Number
+8613268
46001
0493
ICCID
89860121
379743
Registration
Registered to home network
Network Provider
CHN-UNICOM
Network Type
LTE
Band
3
24 (-65dBm)
Signal Strength
RSRP
-101 dBm
-17 dB
RSRQ
SINR
-5 dB
Bit Error Rate
99
PLMN ID
46001
Local Area Code
Cell ID
6B20D02
Tracking Area Code
251B
Physical Cell ID
73
IMEI
8653260
382
Firmware Version
<!-- end of figure 2 -->

<!-- pdf page 23 | printed page 23 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                        Description
 Index                       Indicate the ordinal of the list.
 Modem Status                Show the status of the radio module.
 Modem Vendor                Show the vendor of the radio module.
 Modem Model                 Show the model of the radio module.
 Current SIM                 Show the SIM card that your router is using.
 Phone Number                Show the phone number of the current SIM.
 IMSI                        Show the IMSI number of the current SIM.
 ICCID                       Show the ICCID number of the current SIM.
 Registration                Show the current network status.
 Network Provider            Show the name of Network Provider.
 Network Type                Show the current network service type, e.g. WCDMA.
 Band                        Show the band information.
 Signal Strength             Show the signal strength detected by the mobile.
 RSRP                        Show the current RSRP when you register to the 4G network.
 RSRQ                        Show the current RSRQ when you register to the 4G network.
 SINR                        Show the current SINR when you register to the 5G network.
 Bit Error Rate              Show the current bit error rate.
 PLMN ID                     Show the current PLMN ID.
 Local Area Code             Show the current local area code used for identifying different area.
 Cell ID                     Show the current cell ID used for locating the router.
 Physical Cell ID            Show the current physical cell ID used for locating the router.
 IMEI                        Show the IMEI (International Mobile Equipment Identity) number of the radio
                             module.
 Firmware Version            Show the current firmware version of the radio module.

AT Debug

This page allows you to send an AT command for device debugging.

<!-- figure 1 on pdf page 23 at 124,82-170,487 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 23 at 33,604-557,729 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 96) -->
AT Debug
Command
Result
<!-- end of figure 2 -->

<!-- pdf page 24 | printed page 24 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.2.3 Bridge

Bridge is used to create a single network consisting of multiple devices. The default bridge(br_lan) interface is always
available.

Click    to add a new Bridge. The maximum count is 10.

Click   to delete the Bridge.

Click   to configure the Bridge’s parameters in the pop-up window.

 Item                           Description
 Interface                      The interface of Bridge.
 Description                    The description of the Bridge.
 Sub Interface                  Select and enable the related Ethernet port.

2.2.4 Wi-Fi

This router cannot support WiFi AP mode, User can configure the device as Wi-Fi client by following steps.

Click “Network> WAN>Link> Setting”, click        to add a new WAN link, then configure the related parameters.

<!-- figure 1 on pdf page 24 at 38,177-555,218 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/3 words >= 60, mean confidence 96) -->
Interfaces
Interface
Description
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 24 at 33,362-557,463 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 6/10 words >= 60, mean confidence 71) -->
Interface
Description
bridge
Sub Interface
eth1
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 24 at 105,485-170,554 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 24 at 380,485-559,554 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 25 | printed page 25 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.2.5 USB

This section allows you to configure the USB parameters. The router has two USB Host type A and one USB OTG type
C ports available, the router's USB interface can be used to upgrade firmware and upgrade configuration. The users
can disable all the USB ports for safety if needed.

 Item                     Description                                                                      Default
 Enable USB1 Host         Click the toggle button to enable/disable the USB1 Host option.                  OFF
 Enable USB2 Host         Click the toggle button to enable/disable the USB2 Host option.                  OFF
 Enable Automatic         Click the toggle button to enable/disable this option. Enable to automatically   OFF
 Upgrade                  update the firmware of the router when inserting a USB storage device with a
                          router firmware.
 Enable USB3 OTG          Click the toggle button to enable/disable the USB3 OTG option, to access to      OFF
                          the microSD embedded.

<!-- figure 1 on pdf page 25 at 36,72-555,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/19 words >= 60, mean confidence 75) -->
Name
wwan
[wart
Type
Interface
SSID
Password
default wan
Description
Weight
[external
Firewall Zone
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 25 at 48,458-552,561 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/14 words >= 60, mean confidence 77) -->
Enable USB1 Host
Ke
Enable USB2 Host
Ke
Enable Automatic Upgrade
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 25 at 48,568-552,621 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/8 words >= 60, mean confidence 82) -->
USB OTG Settings
Enable USB3 OTG
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 25 at 33,652-148,784 pt | caption: none | text-layer labels: Enable USB3 OTG | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 25 at 509,652-559,784 pt | caption: none | text-layer labels: Default OFF OFF OFF | OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 26 | printed page 26 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                      Description                                                                        Default
 USB Automatic                                                                                                --
                           Click             to generate and click              to download the key.
 Upgrade Key

Note: when using the USB automatic upgrade function, the LEDs start blinking one by one, it means that the upgrade
is in progress. When LEDs stop blinking one by one, and the USR Indicators is on, it means that the upgrade is
completed. After upgrading, the device will not restart automatically. If there is no LEDs start blinking one by one all
the time, it means there is an exception, and it does not enter into the automatic upgrade process.

2.2.6 VLAN

VLAN stands for Virtual LAN, allows splitting a single physical LAN into separate Virtual LANs, to reduce broadcast
traffic on the LAN.

Click    to add a new Interface. The maximum count is 10.

<!-- figure 1 on pdf page 26 at 33,84-557,158 pt | caption: none | text-layer labels: none | nearby labels: Description | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 97) -->
USB Automatic Upgrade Key
USB Automatic Upgrade Key
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 26 at 33,175-559,235 pt | caption: none | text-layer labels: Item USB Automatic Upgrade Key | Description | Click | to generate and click | to download the key. | Default -- | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 90) -->
Download
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 26 at 38,461-555,511 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 96) -->
Name
Description
VLAN Tag
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 26 at 33,576-557,734 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 10/11 words >= 60, mean confidence 87) -->
Name
Description
VLAN Tag
[Ethernet
Parent Type
[etho
Parent Interface
<!-- end of figure 4 -->

<!-- pdf page 27 | printed page 27 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                     Description                            Default
 Name                     The name of VLAN.                      Null
 Description              Enter a description for this VLAN.     Null
 VLAN Tag                 Enter a tag for this VLAN.             1
 Parent Type              Select from “Ethernet” or “Bridge”.    Ethernet
 Parent Interface         Select the related parent interface.   eth0

2.2.7 DI/DO

This section allows you to set the DI/Relay output parameters.

DIDO

Click   to configure the parameters in the pop-up window.

<!-- figure 1 on pdf page 27 at 318,65-476,168 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 27 at 38,341-536,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 91) -->
Index
PHY Mode
Enable
false
DI
false
DI
false
Relay
false
Relay
<!-- end of figure 2 -->

<!-- pdf page 28 | printed page 28 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

DI

 Item                    Description                                                                     Default
 Index                   Indicate the ordinal of the list.                                               --
 PHY Mode                DI, fixed, read only.                                                           --
 Enable                  Click the toggle button to enable/disable the digital input function.           OFF
 Mode                    Select from “ON-OFF” or “Counter”.                                              ON-OFF
                          ON-OFF: Alarm mode can be triggered at the DI access ON-OFF.
                          Counter: Event counter mode
 Inversion               The count is divided into a rising edge count of the level or a falling edge    OFF
                         count. If the current rising edge count, the reverse edge is the falling edge
                         count.
 Threshold Value         The threshold value is a unique parameter when the mode is Count. Set the       0
                         threshold value to trigger the DI alarm when the count value reaches the
                         threshold value.
 Alarm On Content        Show the content when alarm on.                                                 Alarm On
 Alarm Off Content       Show the content when alarm off.                                                Alarm Off
 VPN Toggle              Select from “Disable”, “OpenVPN”, “RVPN” to enable the VPN option by DI         Disable
Note: It defaults as high alarm, while turns to low alarm after enabling the “Inversion” button.

<!-- figure 1 on pdf page 28 at 36,96-555,336 pt | caption: none | text-layer labels: none | nearby labels: DI | OCR text follows (tesseract, unverified; 21/27 words >= 60, mean confidence 74) -->
[2
Index
[pr
PHY Mode
Enable
on-oFF
Mode
Inversion
[Alarm On
Alarm On Content
Alarm Off Content
Off
v|
VPN Toggle
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 28 at 514,355-559,614 pt | caption: none | text-layer labels: none | nearby labels: OFF | 0 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 29 | printed page 29 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Relay Output

Item              Description                                                                              Default
Index             Indicate the ordinal of the list.                                                        --
PHY Mode          Relay only on Relay Output device                                                        Relay
Enable            Click the toggle button to enable/disable this Relay Output.                             OFF
Alarm On Action   Relay Output initiates when there is an alarm. Selected from “High”, “Low” or “Pulse”.   Relay
                   Relay On: The relay will connect                                                       On
                   Relay Off :The relay will disconnect
Alarm Off         Relay Output initiates when alarm removed. Selected from “High”, “Low” or “Pulse”.       Relay
Action             Relay On: The relay will connect                                                       Off
                   Relay Off :The relay will disconnect
Initial State     Specify the Relay Output status when powered on. Selected from “Last”, “High” or         Relay
                  “Low”.                                                                                   On
                   Relay On: The relay will connect
                   Relay Off :The relay will disconnect
Delay             Set the delay time for DO alarm start-up. The first pulse will be generated after a      0
(unit: 100ms)     “Delay”. Enter from 0 to 3000 (0=generate pulse without delay).
Hold Time         Set the hold time of DO status (Alarm On Action/Alarm Off Action). When the action       0
(unit: s)         time reach this specified time, DO will stop the action. Enter from 0 to 3000 seconds.
                  (0=keep on until the next action)
Triggered by DI   Click the toggle button to enable/disable the relay output triggered by digital input.   ON
Alarm Source      Digital output activation can be activated by this alarm.                                None

<!-- figure 1 on pdf page 29 at 36,94-559,384 pt | caption: none | text-layer labels: none | nearby labels: Relay Output | OCR text follows (tesseract, unverified; 28/35 words >= 60, mean confidence 79) -->
Index
PHY Mode
Relay
Enable
[Relay On
Alarm On Action
Alarm Off Action
Off
[Relay On
Initial State
E
Delay
E
Hold Time
Triggered by DI
Alarm Source
<!-- end of figure 1 -->

<!-- pdf page 30 | printed page 30 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Status

This window allows you to view the status of DI/DO interface. It can also clear the counter alarm of DI in here. Click
the          button to clear DI 1 or DI 2 monthly usage statistics info for counter alarm. Click the        button to
switch the electrical level output.

2.2.8 Serial Port

This section allows you to set the serial port parameters. The device supports two serial ports, which might be
configured as RS232 or RS422 or RS485 according to requirements . The serial data can be converted into IP data or
through IP data into serial data, and then the data can be transmitted through wired or wireless network, so as to
realize the function of transparent data transmission.

<!-- figure 1 on pdf page 30 at 33,168-557,273 pt | caption: none | text-layer labels: none | nearby labels: the | button to | switch the electrical level output. | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 92) -->
Index
Name
Level
Status
Count
High
Alarm off
DI2
High
Alarm off
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 30 at 33,283-557,360 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/14 words >= 60, mean confidence 87) -->
Action Of Clear
Counter Alarm Of DI 1
Counter Alarm Of DI 2
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 30 at 36,365-555,470 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 17/17 words >= 60, mean confidence 95) -->
Index
Relay Action
Level
Low-level Width
High-level Width
Name
Off
Relay1
1
Low
Relay2
Off
2
Low
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 30 at 36,480-555,556 pt | caption: none | text-layer labels: none | nearby labels: 2.2.8 Serial Port | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 94) -->
DO Control
Level Of Relay1
Level Of Relay2
<!-- end of figure 4 -->

<!-- pdf page 31 | printed page 31 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Serial Port

Click     to configure the parameters in the pop-up window.

 Item                Description                                                                               Default
 Index               Indicate the ordinal of the list.                                                         --
 Port                Show the current serial’s name, read only.                                                COM1
 Type                Select from “RS232”, “RS422” “RS485”.                                                     --
 Enable              Click the toggle button to enable/disable this serial port. When the status is OFF, the
                                                                                                               OFF
                     serial port is not available.
 Baud Rate           Select from “300”, “600”, “1200”, “2400”, “4800”, “9600”, “19200”, “38400”, “57600”       115200
                     or “115200”.
 Data Bits           Select from “7” or “8”.                                                                   8
 Stop Bits           Select from “1” or “2”.                                                                   1
 Parity              Select from “None”, “Odd” or “Even”.                                                      None
 Flow control        Select from “None”, “Software” or “Hardware”.                                             None

<!-- figure 1 on pdf page 31 at 33,113-557,218 pt | caption: none | text-layer labels: none | nearby labels: Serial Port | OCR text follows (tesseract, unverified; 23/25 words >= 60, mean confidence 91) -->
Serial Port Settings
Index
Port
Enable
Type
Baud Rate
Application Mode
1
COM1
false
RS232
115200
Transparent
2
COM2
false
RS232
115200
Transparent
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 31 at 33,269-557,528 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 18/24 words >= 60, mean confidence 79) -->
Index
[coma
Port
Enable
Type
[115200
Baud Rate
[s
Data Bits
Stop Bits
Parity
None
[None
Flow Control
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 31 at 72,532-120,734 pt | caption: none | text-layer labels: none | nearby labels: Enable | Baud Rate | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 31 at 320,532-516,734 pt | caption: none | text-layer labels: none | nearby labels: -- | OFF | 115200 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 32 | printed page 32 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item               Description                                                                               Default
 Packing Timeout    Set the packing timeout. The serial port will queue the data in the buffer and send the   50
                    data to the Cellular WAN/Ethernet WAN when it reaches the Interval Timeout in the
                    field. The unit is milliseconds.
                    Note: Data will also be sent as specified by the packet length even when data is not
                    reaching the interval timeout in the field.
 Packing Length     Set the packet length. The Packet length setting refers to the maximum amount of          1200
                    data that is allowed to accumulate in the serial port buffer before sending. When a
                    packet length between 1 and 3000 bytes is specified, data in the buffer will be sent as
                    soon it reaches the specified length.

In the "Server Settings" column, when "Transparent” is selected as the application mode and "TCP Client" as the
protocol, the window is as follows:

When "Transparent” is selected as the application mode and "TCP Server" as the protocol, the window is as follows:

When "Transparent” is selected as the application mode and "UDP" is used as the protocol, the window is as follows:

<!-- figure 1 on pdf page 32 at 33,72-555,154 pt | caption: none | text-layer labels: none | nearby labels: Item Packing Timeout | Default 50 | OCR text follows (tesseract, unverified; 7/8 words >= 60, mean confidence 88) -->
Data Packing
E
Packing Timeout
Packing Length
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 32 at 33,161-120,321 pt | caption: none | text-layer labels: Item Packing Timeout | Packing Length | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 32 at 516,199-562,321 pt | caption: none | text-layer labels: 1200 | nearby labels: Default 50 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 32 at 33,367-555,499 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/11 words >= 60, mean confidence 89) -->
[Transparent
Application Mode
[Tce Client
Protocol
Server Address
Server Port
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 32 at 36,544-555,669 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 83) -->
[Transparent
Application Mode
Server
Protocol
Local IP
Local Port
<!-- end of figure 5 -->

<!-- pdf page 33 | printed page 33 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

When “Modbus RTU Gateway” is selected as the application mode and “TCP Client” as the protocol, the window is as
follows:

When "Modbus RTU Gateway" is selected as the application mode and "TCP Server" as the protocol, the window is
as follows:

When selecting "Modbus RTU Gateway" as the application mode and "UDP" as the protocol, the window is as
follows:

<!-- figure 1 on pdf page 33 at 36,65-557,249 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/15 words >= 60, mean confidence 91) -->
Server Setting
[Transparent
Application Mode
Protocol
Local IP
Local Port
Server Address
Server Port
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 33 at 33,293-559,422 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 88) -->
[Modbus RTU Gateway
Application Mode
Protocol
Client
Server Address
Server Port
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 33 at 33,475-555,607 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 89) -->
Application Mode
Modbus RTU Gateway
Protocol
Server
Local IP
Local Port
<!-- end of figure 3 -->

<!-- pdf page 34 | printed page 34 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

When “Modbus ASCII Gateway” is selected as the application mode and “TCP Client” as the protocol, the window is
as follows:

<!-- figure 1 on pdf page 34 at 33,65-555,249 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/16 words >= 60, mean confidence 88) -->
[Modbus RTU Gateway
Application Mode
Protocol
Local IP
Local Port
Server Address
Server Port
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 34 at 33,307-555,437 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 90) -->
Application Mode
Modbus ASCII Gateway
[tcp Client
Protocol
Server Address
Server Port
<!-- end of figure 2 -->

<!-- pdf page 35 | printed page 35 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

When selecting "Modbus ASCII Gateway" as the application mode and "TCP Server" as the protocol, the window is as
follows:

When selecting "Modbus ASCII Gateway" as the application mode and "UDP" as the protocol, the window is as
follows:

 Item              Description                                                                               Default
 Application       Select from “Transparent”, “Modbus RTU Gateway” or “Modbus ASCII Gateway”.                Transp
 Mode               Transparent: Device will transmit the serial data transparently                         arent
                    Modbus RTU Gateway: Device will translate the Modbus RTU data to Modbus
                        TCP data and sent out, and vice versa
                    Modbus ASCII Gateway: Device will translate the Modbus ASCII data to Modbus
                        TCP data and sent out, and vice versa
 Protocol          Select from “TCP Client”, “TCP Server”, or “UDP”.                                         TCP
                    TCP Client: Device works as TCP client, initiate TCP connection to TCP server.          Client
                        Server address supports both IP and domain name
                    TCP Server: Device works as TCP server, listening for connection request from
                        TCP client
                    UDP: Device works as UDP client
 Server Address    Enter the address of server which will receive the data sent from device’s serial port.   Null
                   IP address or domain name will be available.
 Server Port       Enter the specified port of server which is used for receiving the serial data.           Null
 Local IP @        Enter device’s LAN IP which will forward to the internet port of device.                  Null
 Transparent

<!-- figure 1 on pdf page 35 at 33,106-555,235 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 85) -->
Application Mode
Modbus ASCII Gateway
Protocol
Server
Local IP
Local Port
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 35 at 33,283-559,470 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/15 words >= 60, mean confidence 89) -->
[Modbus ASCII Gateway
Application Mode
Protocol
Local IP
Local Port
Server Address
Server Port
<!-- end of figure 2 -->

<!-- pdf page 36 | printed page 36 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item               Description                                   Default
 Local Port @       Enter the port of device’s LAN IP.            Null
 Transparent
 Local IP @         Enter the local IP of under Modbus mode.      Null
 Modbus
 Local Port @       Enter the local port of under Modbus mode.    Null
 Modbus

Status

Click the "Status" column to view the current serial port type.

<!-- figure 1 on pdf page 36 at 33,300-555,405 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/14 words >= 60, mean confidence 89) -->
Index
Type
TX
RX
Connection Status
1
RS232
OB
0B
2
RS232
OB
OB
<!-- end of figure 1 -->

<!-- pdf page 37 | printed page 37 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.2.9 BAM

This section allows you to set the BAM(Bridge Alarm Management) parameters.

HBT

  Item                         Description                                                  Default
  Enable                       Click the toggle button to enable or disable the function.   OFF
  Interface                    Set the message outgoing interface                           br_lan
  Server IP address/domain     Set the Server IP address and domain                         Null
  Server Port                  Set the Server port                                          Null
  Message Quantity             Set the message quantity                                     1
  Period                       Set the heart beat peride                                    10sec

<!-- figure 1 on pdf page 37 at 48,269-540,444 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 91) -->
Enable
Interface
br_lan
Server IP address/domain
Server Port
E
Message Quantity
Period
10sec
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 37 at 497,451-567,568 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 38 | printed page 38 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

ALF

 Item                       Description                                                  Default
 Enable                     Click the toggle button to enable or disable the function.   OFF
 Interface                  Set the message outgoing interface                           br_lan
 Server IP address/domain   Set the Server IP address and domain                         Null
 Server Port                Set the Server port                                          Null
 Message Quantity           Set the message quantity                                     1
 HBT period                 Set the heart beat period                                    10sec
 Action                     Click the toggle button to enable or disable the function.   ON
                            ON: Send ALF message when VPN session is connected.
                            OFF: Do not send ALF message.

<!-- figure 1 on pdf page 38 at 43,194-538,398 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/17 words >= 60, mean confidence 83) -->
Enable
interface
Server IP address/domain
Server Port
[2
Message Quantity
v]
Period
10sec
Gi
Action
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 38 at 38,408-177,573 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 38 at 442,408-567,573 pt | caption: none | text-layer labels: Default OFF br_lan Null Null 1 10sec ON | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 39 | printed page 39 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Status

You can view detailed information here.

<!-- figure 1 on pdf page 39 at 43,189-538,266 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 94) -->
Sending counter
Index
IP Addreess
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 39 at 43,273-538,353 pt | caption: none | text-layer labels: none | nearby labels: You can view detailed information here. | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Sending counter
Index
IP Addreess
<!-- end of figure 2 -->

<!-- pdf page 40 | printed page 40 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.3       Network

2.3.1 WAN

WAN stands for Wide Area Network, provides connectivity to the internet. You can configure WAN based on Ethernet,
Cellular modem or Wi-Fi(if supported).

Link

Click    to add a new WAN link.

Click    to delete the link.

Press     to drag the WAN link into the required order to switch between WAN connections, the topper one has

higher priority.

Click     to edit the link.

Users can manage link connections in this section. It provides four types of connectivity interface to internet
including Modem, Ethernet, VLAN and Wi-Fi.

<!-- figure 1 on pdf page 40 at 43,329-538,405 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
Settings
Firewall Zone
Description
Weight
Name
Type
Modem(4G/5G)
WWAN
default wan
0
external
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 40 at 43,415-538,516 pt | caption: none | text-layer labels: none | nearby labels: Click | to add a new WAN link. | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 95) -->
Overrided DNS Enable
Overrided Primary DNS
Overrided Secondary DNS
<!-- end of figure 2 -->

<!-- pdf page 41 | printed page 41 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->



<!-- figure 1 on pdf page 41 at 33,65-555,254 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/15 words >= 60, mean confidence 84) -->
Name
WWAN
[Modem
Type
Interface
wwan
Description
defaut wan
Weight
[external
Firewall Zone
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 41 at 36,261-557,449 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/12 words >= 60, mean confidence 88) -->
Name
WAN
[Ethernet
Type
Interface
Description
[o
Weight
Firewall Zone
external
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 41 at 33,456-557,643 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 92) -->
Name
[viaN
Type
Interface
Description
lo
Weight
[external
Firewall Zone
<!-- end of figure 3 -->

<!-- pdf page 42 | printed page 42 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                   Description                                                        Default
Name                   The name of link.                                                  --
Type                   The types of connectivity.                                         --
                        Modem: connected by cellular network.
                        Ethernet: connected by Ethernet wired network.
                        VLAN: connected by VLAN network.
                        Wi-Fi: connected by Wi-Fi network.
Interface              Set the related interface.                                         --
                       If the type is Modem, please see the 2.2.2 Cellular.
                       If the type is Ethernet, please see the 2.2.1 Ethernet.
                       If the type is VLAN, please see the 2.2.6 VLAN.
Description            The description of the link.                                       --
SSID                   The name of Wi-Fi network.                                         --
Password               The Password of Wi-Fi network.                                     --
Weight                 The weight of this link among all links. 0 means not involved.     --
Firewall Zone          The chosen set of firewall rules, please see the 2.3.5 Firewall.   --

Item                   Description                                                        Default
IPv4 Connection Type   The type of IPv4 connection.                                       DHCP
                        DHCP.
                        PPPoE.
                        Manual.
                        Disable.
                       Enter the parameters accordingly.

<!-- figure 1 on pdf page 42 at 36,72-557,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/15 words >= 60, mean confidence 86) -->
Name
Type
Interface
wlanO
SSID
router
Password
Description
[o
Weight
[external
Firewall Zone
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 42 at 74,331-158,590 pt | caption: none | text-layer labels: none | nearby labels: Interface | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 42 at 445,331-500,590 pt | caption: none | text-layer labels: none | nearby labels: -- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 42 at 516,331-559,590 pt | caption: none | text-layer labels: none | nearby labels: -- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 42 at 33,604-555,657 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 72) -->
Settings
Connection Type
DHCP
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 42 at 33,662-158,777 pt | caption: none | text-layer labels: Item IPv4 Connection Type | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 42 at 323,662-559,777 pt | caption: none | text-layer labels: Default DHCP | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 43 | printed page 43 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                    Description                                                 Default
Enable                  Toggle the button to enable the health detection function   ON
IPv4 Primary Server     IPv4 Primary Server                                         8.8.8.8
IPv4 Secondary Server   IPv4 Secondary Server                                       114.114.114.114
Interval                Seconds to send next ping                                   30
Timeout                 Seconds to wait for ping response                           3
Reconnect Tries         Reconnect this link in case of sequential probes are        3
                        unsuccessful.
Recover Tries           Recovery this link in case of sequential probes are         3
                        successful.

Advanced DNS Settings

Item                    Description                                                 Default
Enable                  Toggle the button to enable the overrided DNS function      OFF
Overrided Primary DNS   Define a primary DNS server address used by the link        NULL
Overrided Primary DNS   Define a secondary DNS server address for the link          NULL

<!-- figure 1 on pdf page 43 at 33,86-559,463 pt | caption: none | text-layer labels: Recover Tries | 3 | OCR text follows (tesseract, unverified; 19/19 words >= 60, mean confidence 90) -->
Enable
[2.8.8.8
IPv4 Primary Server
[1.2.4.8
IPv4 Secondary Server
Interval
300
E
Timeout
E
Reconnect Tries
E
Recover Tries
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 43 at 36,537-545,645 pt | caption: none | text-layer labels: none | nearby labels: Advanced DNS Settings | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 89) -->
Overrided DNS Enable
Overrided Primary DNS
Overrided Secondary DNS
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 43 at 485,660-559,729 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 44 | printed page 44 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Status

This window allows you to view the link status of device.

2.3.2 LAN

A Local Area Network (LAN) connects network devices together, such as Ethernet or Bridge, in a logical Layer-2
network. The default link(br_lan) is always available.

Link

Click    to add a new LAN link.

Click    to delete the LAN link.

Click     to edit the LAN link.

Users can manage link connections in this section. It provides three types of connectivity interface to internet
including Bridge, Ethernet and VLAN.

<!-- figure 1 on pdf page 44 at 38,453-555,494 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 97) -->
Settings
Firewall Zone
Name
Type
Description
<!-- end of figure 1 -->

<!-- pdf page 45 | printed page 45 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item            Description                                                               Default
Name            The name of the LAN link.                                                 --
Type            The types of connectivity. Select from “Bridge”, “Ethernet” and “VLAN”.   Bridge
                 Bridge: connected by Bridge network.
                 Ethernet: connected by Ethernet wired network.
                 VLAN: connected by VLAN network.
Interface       Set the related interface.                                                --
                If the type is Bridge, please see the 2.2.3 Bridge.
                If the type is Ethernet, please see the 2.2.1 Ethernet.
                If the type is VLAN, please see the 2.2.6 VLAN.
Description     The description of the link.                                              --
Firewall Zone   The chosen set of firewall rules, please see the 2.3.5 Firewall.          internal

Item            Description                                              Default
IPv4 Address    Enter the IPv4 address with netmask.                     192.168.0.1/24
IP Pool Start   The start IP address in pool.                            192.168.0.2
IP Pool End     The end IP address in pool.                              192.168.0.100
Primary DNS     Enter the primary DNS.                                   Null

<!-- figure 1 on pdf page 45 at 33,72-559,228 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/13 words >= 60, mean confidence 82) -->
Name
[Bridge
Type
Interface
br_lan
Description
lan
[internal
Firewall Zone
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 45 at 74,252-158,449 pt | caption: none | text-layer labels: none | nearby labels: Description Firewall Zone | Interface | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 45 at 516,252-559,449 pt | caption: none | text-layer labels: none | nearby labels: -- | -- internal | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 45 at 36,465-555,506 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 83) -->
ip4 Settings
Address
192.168.0.1/24
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 45 at 36,528-555,568 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 87) -->
A DHCPV4 Settings
IP Pool Start
192.168.0.2
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 45 at 105,693-158,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 45 at 335,693-418,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 8 on pdf page 45 at 497,693-559,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 46 | printed page 46 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                       Description
 Secondary DNS              Enter the secondary DNS.
 Lease Time                 The lease time in minute.

Status

This window allows you to view the status of LAN link.

2.3.3 Route

Default
Null
120

Routes ensure that network traffic finds its path to a destination network. Static routes are fixed routing entries in
routing table.

Static Route

Click    to add static routes. The maximum count is 20.

<!-- figure 1 on pdf page 46 at 115,65-158,118 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 46 at 285,65-418,118 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 46 at 464,65-559,118 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 46 at 43,269-543,348 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 85) -->
Interface Status
Interface
IPv4 Address
MAC Address
34:FA:40:25:25:08
192.168.0.1
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 46 at 43,355-543,434 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/14 words >= 60, mean confidence 89) -->
Connected Devices
Inactive Time
Index
IP Address
MAC Address
Interface
192.168.0.75
br_lan
Os
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 46 at 41,645-555,686 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 94) -->
A Static Route Table
Index
Netmask
Interface
Description
Destination
Gateway
<!-- end of figure 6 -->

<!-- pdf page 47 | printed page 47 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                       Description                                                                 Default
 Index                      Indicate the ordinal of the list.                                           --
 Description                Enter a description for this static route.                                  Null
 Destination                Enter the IP address of destination host or destination network.            Null
 Netmask                    Enter the Netmask of destination host or destination network.               Null
 Gateway                    Define the gateway of the destination.                                      Null
 Metric                     Enter the Metric value. Metrics help the gateway choose the best route      0
                            among multiple feasible routes to a destination. The route will go in the
                            direction of the gateway with the lowest metric value.
 MTU                        Enter the MTU value, 1280~1500.                                             1500
 Interface                  Choose the corresponding port of the link that you want to configure.       br_lan

Status

This window allows you to view the status of route.

<!-- figure 1 on pdf page 47 at 33,72-555,309 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/12 words >= 60, mean confidence 82) -->
[2
Index
Description
Destination
Netmask
Gateway
E
Metric
MTU
Interface
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 47 at 88,331-158,511 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 48 | printed page 48 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.3.4 Policy Route

In this window, you can manage the outbound route based on the IP address, port number in the packet.

Policy Route

Click   to add a policy route. The maximum count is 20.

 Item                      Description                                                                  Default
 Index                     Indicate the ordinal of the list.                                            --
 Name                      Name of Policy Route.                                                        --
 Protocol                  The type of network protocol. Select from “Any”,                             TCP-UDP
                           “TCP”,”UDP”,”TCP-UDP”,”ICMP” and “IGMP”.
 Hooks                     Fixed setting.                                                               --
 Sources Address           Enter the source IP address.                                                 --
 Source Port               Enter the source port in TCP/UDP type.                                       --
 Source MAC                Enter the source mac address.                                                --
 Destination Address       Enter the destination IP address.                                            --
 Destination Port          Enter the destination port in TCP/UDP type.                                  --

<!-- figure 1 on pdf page 48 at 41,218-550,259 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 97) -->
Match settings
Index
Protocol
Source Address
Destination address
Interface
Name
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 48 at 33,309-559,573 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 15/17 words >= 60, mean confidence 90) -->
Index
Name
Protocol
Hooks
PREROUTING
Source Address
Source Port
Source MAC
Destination address
Destination port
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 48 at 84,590-158,772 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 48 at 390,590-500,772 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 48 at 516,590-559,772 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 49 | printed page 49 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                       Description                                                                 Default
 Destination                Enter the IP address of destination host or destination network.            --
 Netmask                    Enter the Netmask of destination host or destination network.               --
 Gateway                    Define the gateway of the destination.                                      --
 Interface                  Choose the corresponding port of the link that you want to configure.       br_lan

2.3.5 Firewall

Firewall makes use of Linux iptables to control inbound and outbound traffic, the router has already been configured
to meet IEC61162-460 requirements.

General Setting

<!-- figure 1 on pdf page 49 at 33,70-555,201 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 87) -->
Destination
Netmask
Gateway
Interface
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 49 at 98,221-158,307 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 49 at 41,504-555,660 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/16 words >= 60, mean confidence 93) -->
General Settings
Enable DOS protection
[4
Duration of direct connection
[accept
Input
[accept
Output
[Drop
Forward
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 49 at 41,669-555,772 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/16 words >= 60, mean confidence 91) -->
Zones
Forward
Name
Input
Output
[4
external
Drop
Accept
Drop
internal
Drop
Accept
Accept
<!-- end of figure 4 -->

<!-- pdf page 50 | printed page 50 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                             Description                                                          Default
 Enable DOS protection            click the toggle button to enable/disable.                           ON
 Duration of direct connection     The duration(hour) of direct connection                            4
                                  Each rule is valid for four hours
 Input                            Default action of the Input chain if a packet does not match any     Accept
                                  exist rule on that chain.
                                   Accept: Packet gets to continue to the next chain.
                                   Drop: Packet is stopped and deleted.
 Output                           Default action of the Output chain if a packet does not match any    Accept
                                  exist rule on that chain.
                                   Accept: Packet gets to continue to the next chain.
                                   Drop: Packet is stopped and deleted.
 Forward                          Default action of the Forward chain if a packet does not match any   Drop
                                  exist rule on that chain.
                                   Accept: Packet gets to continue to the next chain.
                                   Drop: Packet is stopped and deleted.
 Note: The general setting is used as a default firewall setting unless specified.

Zone is a set of firewall rules, users can define their own firewall zone.

Click    to add one firewall zone. The maximum count is 50

<!-- figure 1 on pdf page 50 at 33,384-557,487 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/15 words >= 60, mean confidence 90) -->
Forward
Name
Input
Output
[AX
external
Drop
Accept
Drop
[Ax
internal
Accept
Accept
Accept
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 50 at 33,537-555,722 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 80) -->
Name
external
Input
Drop
[Accept
Output
Forward
Drop
Masquerading
MSS clamping
<!-- end of figure 2 -->

<!-- pdf page 51 | printed page 51 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                            Description                                                              Default
 Name                            The name of the firewall zone.                                           --
 Input                           Default action of the Input chain if a packet does not match any         Drop
                                 exist rule on that chain.
                                  Accept: Packet gets to continue to the next chain.
                                  Drop: Packet is stopped and deleted.
 Output                          Default action of the Output chain if a packet does not match any        Accept
                                 exist rule on that chain.
                                  Accept: Packet gets to continue to the next chain.
                                  Drop: Packet is stopped and deleted.
 Forward                         Default action of the Forward chain if a packet does not match any       Drop
                                 exist rule on that chain.
                                  Accept: Packet gets to continue to the next chain.
                                  Drop: Packet is stopped and deleted.
 Masquerading                    Click the toggle button to enable/disable. MASQUERADE is an              ON
                                 iptables target that can be used instead of the SNAT (source NAT)
                                 target when the external IP of the network interface is not known at
                                 the moment of writing the rule (when the interface gets the
                                 external IP dynamically).
 MSS clamping                    Click the toggle button to enable/disable. MSS clamping is a             ON
                                 workaround used to change the maximum segment size (MSS) of all
                                 TCP connections passing through links with an MTU lower than the
                                 Ethernet default of 1500.

DMZ (Demilitarized Zone), also known as the demilitarized zone. It is a buffer between a non-secure system and a
secure system that is set up to solve the problem that users who access the external network cannot access the
internal network server after the firewall is installed. A DMZ host is an intranet host where all ports are open to the
specified address except the ports that are occupied and forwarded.

 Item                     Description                                                                       Default
 Enable DMZ               Click the toggle button to enable/disable DMZ. DMZ host is a host on the          OFF
                          internal network that has all ports exposed, except those ports otherwise
                          forwarded.
 Host IP Address          Enter the IP address of the DMZ host on your internal network.                    Null
 Source IP Address        Set the address which can talk to the DMZ host. Null means for any                Null

<!-- figure 1 on pdf page 51 at 33,463-545,508 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 94) -->
DNZ Settings
Enable DMZ
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 51 at 100,676-146,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 52 | printed page 52 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

                        addresses.
 Destination IP Address Set the address which the DMZ host can talk to . Null means for any                  Null
                        addresses.

 Item                       Description                                                                      Default
 Enable SSH Access          Click the toggle button to enable/disable this option. When enabled, the         OFF
                            zone user can access the device via SSH.
 Enable HTTP Access         Click the toggle button to enable/disable this option. When enabled, the         OFF
                            zone user can access the device via HTTP.
 Enable HTTPS Access        Click the toggle button to enable/disable this option. When enabled, the         OFF
                            zone user can access the device via HTTPS.
 Enable Ping Respond        Click the toggle button to enable/disable this option. When enabled, the         OFF
                            device will reply to the Ping requests from other hosts on the zone.

Port Forwards

This window allows you to view the port forward rules. Port forwarding is a way of redirecting an incoming
connection to another IP address, port or the combination of both.

Click    to add one.   The maximum count is 50.

<!-- figure 1 on pdf page 52 at 461,65-559,118 pt | caption: none | text-layer labels: Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 52 at 33,134-555,264 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/16 words >= 60, mean confidence 85) -->
Enable SSH Access
Enable HTTP Access
Enable HTTPS Access
Enable Ping Respond
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 52 at 33,535-557,595 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
Port Forwards Rules
Index
Protocol
Name
Source zone
Destination zone
<!-- end of figure 3 -->

<!-- pdf page 53 | printed page 53 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                       Description                                                                   Default
 Index                      Indicate the ordinal of the list.                                             --
 Name                       Name of the rule.                                                             Null
 IPv4 Source Address        IP address or network segment used by connecting hosts.                       Null
                            The rule will apply only to hosts that connect from IP addresses specified
                            in this field.
 Protocol                   Select from “TCP”, “UDP” or “TCP-UDP” as your application required.           TCP-UDP
 Source zone                The zone to which the third party will be connecting. Select a configured     external
                            zone.
 External Port              Match incoming traffic directed at the given destination port or port range   Null
                            on this host. Select a configured zone.
 Destination zone           The zone to which the incoming connection will be redirected.                 external
 Internal IP Address        The IP address to which the incoming connection will be redirected.           Null
 Internal Port              The port number to which the incoming connection will be redirected.          Null

Traffic Rules

This window allows you to view the traffic rules.

Click    to add one. The maximum count is 50.

<!-- figure 1 on pdf page 53 at 33,67-555,329 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 19/22 words >= 60, mean confidence 83) -->
Index
Name
IPv4 Source Address
Protocol
[external
Source zone
External Port
external
Destination zone
Internal IP Address
Internal port
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 53 at 100,345-153,573 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 53 at 33,662-557,720 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
Index
Address Family
Protocol
Name
Source zone
Action
<!-- end of figure 3 -->

<!-- pdf page 54 | printed page 54 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                     Description                                                            Default
Index                    Indicate the ordinal of the list.                                      --
Name                     The name of the rule.                                                  Null
Address family           Select “IPv4” as your application required.                            IPv4
Protocol                 Select from “TCP”, “UDP” or “TCP-UDP” as your application required.    TCP-UDP
Source zone              The zone to which the third party will be connecting.                  device_output
IPv4 Source Address      The IPv4 address or network segment used by connecting hosts.          Null
                         The rule will apply only to hosts that connect from IP addresses
                         specified in this field.
Source Port              Port number(s) used by the connecting host.                            Null
                         The rule will match the source port used by the connecting host with
                         the port number(s) specified in this field. Leave empty to make the
                         rule skip source port matching.
Source MAC               MAC address of connecting hosts.                                       Null
                         The rule will apply only to hosts that match MAC addresses specified
                         in this field. Leave empty to make the rule skip MAC address
                         matching.
Output zone              The zone to which the incoming connection will be redirected.          any_forward
IPv4 Destination Address The IP address to which the incoming connection will be redirected.    Null
Multi-Destination Option Click + to add more destination address, the max quantity is 20        Null
Destination port         The port number to which the incoming connection will be               Null
                         redirected.
Action                   Select from “Accept”, or “Drop” as your application required.          Null

<!-- figure 1 on pdf page 54 at 33,70-559,780 pt | caption: none | text-layer labels: Null | Null | any_forward Null Null Null | Null | OCR text follows (tesseract, unverified; 26/29 words >= 60, mean confidence 88) -->
index
Name
Address Family
4
TCP-UDP
Source zone
device_output
IPv4 Source Address
Source Port
Source MAC
Output zone
any_forward
IPv4 Destination Address
Destination port
Action
Drop
<!-- end of figure 1 -->

<!-- pdf page 55 | printed page 55 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Custom Rules

This window allows you to view the custom rules.

Click     to add one. The maximum count is 50.

 Item                      Description                                                 Default
 Index                     Indicate the ordinal of the list.                           --
 Name                      Enter a description for this.                               Null
 Family                    Select the “IPv4” as your application required.             IPv4
 Rule                      Users specify their own iptables rule in required format.   Null

Status

This window allows you to view the status of firewall.

<!-- figure 1 on pdf page 55 at 36,144-545,185 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Custom Iptables Rules
Index
Family
Rule
Name
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 55 at 36,259-543,305 pt | caption: none | text-layer labels: none | nearby labels: Click | to add one. The maximum count is 50. | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 80) -->
[2
Index
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 55 at 77,408-153,492 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 55 at 416,408-500,492 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 55 at 33,576-557,758 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 73/110 words >= 60, mean confidence 70) -->
General Settings
Port Forwards
Traffic Rules
Custom Rules
ACCEPT
tcp dpt:22
12
562 ACCEPT
tcp
tcp
tcp dpt:443
ACCEPT
tcp
icmp
icmptype 8
ACCEPT
all
ACCEPT
ctstate DNAT
10647 zone_internal_src_ACCEPT
all
86
Chain
zone_internal_output (1 references)
prot opt in
destination
pkts
bytes target
out
6776 output_internal_rule
all
28
6776 zone_internal_dest_ACCEPT
all
28
Chain
zone_internal_src_ACCEPT (1 references)
prot opt in
destination
pkts
bytes target
out
source
all
br_lan
86
10647 ACCEPT
ctstate NEW,UNTRACKED
/A
<!-- end of figure 5 -->

<!-- pdf page 56 | printed page 56 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.3.6 QoS

QoS provides the possibility to prioritize network traffic based on hosts, ports or services and limit download or
upload speeds on a selected interface.

General Setting

 Item                          Description                                                                 Default
 Enable QoS                    Click the toggle button to enable or disable.                               OFF
 Upload Bandwidth              Enter a value for the upload bandwidth, the unit is kbit.                   10000
 Download Bandwidth            Enter a value for the download bandwidth, the unit is kbit.                 10000

Priority Definition

Click   to set the priority.

<!-- figure 1 on pdf page 56 at 41,233-557,336 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/11 words >= 60, mean confidence 87) -->
General Settings
Enable QoS
Upload Bandwidth
10000
Download Bandwidth
10000
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 56 at 426,357-500,425 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 56 at 33,501-557,664 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 27/28 words >= 60, mean confidence 92) -->
Priority Definition
Index
Bandwidth
Borrow Spare Bandwidth
Priority
[4
Highest
20
true
High
20
true
4
Normal
20
true
[4
Low
20
true
4
Lowest
20
true
<!-- end of figure 3 -->

<!-- pdf page 57 | printed page 57 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                     Description                                                                 Default
Bandwidth                Percentage of total bandwidth. The sum of bandwidth of all the priorities   20
                         cannot be greater than 100.
Borrow Spare Bandwidth   The traffic associated with this priority will borrow unused bandwidth      ON
                         from other priorities when borrowing is enabled, and will be limited to
                         the specified bandwidth when borrowing is disabled.

IPv4 QoS Rules

Click    to add one. The maximum count is 10.

 Item                      Description
 Index                     Indicate the ordinal of the list.

Default
--

<!-- figure 1 on pdf page 57 at 33,70-555,199 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/12 words >= 60, mean confidence 74) -->
[1
Index
Priority
Highest
Bandwidth
Borrow Spare Bandwidth
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 57 at 33,221-160,321 pt | caption: none; nearest centred text below: "IPv4 QoS Rules" | text-layer labels: Item Bandwidth | Borrow Spare Bandwidth | nearby labels: IPv4 QoS Rules | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 57 at 497,221-562,321 pt | caption: none | text-layer labels: Default 20 | ON | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 57 at 33,379-557,437 pt | caption: none | text-layer labels: none | nearby labels: IPv4 QoS Rules | Click | to add one. The maximum count is 10. | OCR text follows (tesseract, unverified; 13/14 words >= 60, mean confidence 92) -->
QoS Rules
Index
Source Address
Target Address
Protocol
Source Port
Target Port
Priority
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 57 at 33,475-555,712 pt | caption: none | text-layer labels: none | nearby labels: Click | to add one. The maximum count is 10. | OCR text follows (tesseract, unverified; 15/16 words >= 60, mean confidence 90) -->
Index
Source Address
Source Port
Source MAC
Target Address
Target Port
[al
Protocol
Priority
Normal
<!-- end of figure 5 -->

<!-- pdf page 58 | printed page 58 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Source Address              The address of Host(s) from which data will be transmitted.                  Null
 Source Port                 The port of Host(s) from which data will be transmitted.                     Null
 Source MAC                  The MAC address of Host(s) from which data will be transmitted.              Null
 Target Address              The address of Host(s) to which data will be transmitted.                    Null
 Target Port                 The port of Host(s) to which data will be transmitted.                       Null
 Protocol                    Select from “All”, “TCP”, “UDP” or “ICMP” as your application required.      All
 Priority                    Select from “Highest”, “High”, “Normal”, “Low” or “Lowest” as your           Normal
                             application required.

2.4      VPN

2.4.1 IPsec

This section allows you to set the IPsec and the related parameters. Internet Protocol Security (IPsec) is a protocol
suite for secure Internet Protocol (IP) communications that works by authenticating and encrypting each IP packet of
a communication session.

General

 Item                       Description                                                                   Default
 Keepalive                  Set the time to live in seconds. The router sends keep-alive packets to the   20
                            NAT (Network Address Translation) server at regular intervals to prevent
                            the records on the NAT table from disappearing.
                            Click the toggle button to enable/disable this option. When enabled,          OFF
 Optimize DH Size           when using dhgroup17 or dhgroup18, it helps to shorten the time to
                            generate the dh key.
                            Click the toggle button to enable/disable this option. Enable for IPsec VPN   OFF
 Debug Enable
                            information output to the debug port.
 Enable Backup Gateway      Click the toggle button to enable/disable this option.                        OFF

<!-- figure 1 on pdf page 58 at 33,65-160,199 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 58 at 490,65-562,199 pt | caption: none | text-layer labels: Null Null Null Null Null All Normal | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 58 at 38,453-555,583 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/14 words >= 60, mean confidence 82) -->
Keepalive
Optimize DH Exponent Size
Debug Enable
Enable Backup Gateway
<!-- end of figure 3 -->

<!-- pdf page 59 | printed page 59 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Tunnel

Click   to add IPsec tunnel settings. The maximum count is 6.

General Setting

 Item                Description                                                    Default
 Index               Indicate the ordinal of the list.                              --
 Enable              Click the toggle button to enable/disable this IPsec tunnel.   ON
 Description         Enter a description for this IPsec tunnel.                     Null
 Link binding        Select the link to build IPSec.                                Unbound

<!-- figure 1 on pdf page 59 at 33,144-559,204 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
Tunnel Settings
Index
Enable
Description
Gateway
Local Subnet
Remote Subnet
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 59 at 36,321-555,535 pt | caption: none | text-layer labels: none | nearby labels: General Setting | OCR text follows (tesseract, unverified; 10/13 words >= 60, mean confidence 81) -->
Index
Enable
Description
[wwan
Link Binding
Gateway
Protocol
[Tunnel
Mode
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 59 at 402,693-497,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 60 | printed page 60 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Gateway              Enter the address of remote side IPsec VPN server. 0.0.0.0 represents for any     Null
                     address.
Mode                 Select from “Tunnel” and “Transport”.                                             Tunnel
                      Tunnel: Commonly used between routers, or at an end-station to a router,
                          the router acting as a proxy for the hosts behind it
                      Transport: Used between end-stations or between an end-station and a
                          router, if the router is being treated as a host-for example, an encrypted
                          Telnet session from a workstation to a router, in which the router is the
                          actual destination
Protocol             Select the security protocols from “ESP” and “AH”.                                ESP
                      ESP: Use the ESP protocol
                      AH: Use the AH protocol
Local Subnet         Enter the local subnet’s address with mask protected by IPsec, e.g.               Null
                     192.168.1.0/24
Remote Subnet        Enter the remote subnet’s address with mask protected by IPsec, e.g.              Null
                     10.8.0.0/24
IKE Type             Select from “IKEv1” and “IKEv2”.                                                  IKEv1
Negotiation Mode     Select from “Main” and “Aggressive” for the IKE negotiation mode in phase 1. If   Main
                     the IP address of one end of an IPsec tunnel is obtained dynamically, the IKE
                     negotiation mode must be aggressive. In this case, SAs can be established as
                     long as the username and password are correct.
Initial Mode         Select from “Always On” and “On Demand”.                                          Always On

Advanced Setting

Item                   Description                                                                     Default
Enable Compression     Click the toggle button to enable/disable this option. Enable to compress       OFF
                       the inner headers of IP packets.
Enable Forceencaps     Force UDP encapsulation for ESP packets even if no NAT situation is             OFF
                       detected.This may help to surmount restrictive firewalls.
Backup Gateway         Backup Address of remote peer to initiate connection, empty means disable.      Null
Expert Options         Add more PPP configuration options here, format: config-desc; config-desc,      Null
                       e.g. protostack=netkey; plutodebug=none

<!-- figure 1 on pdf page 60 at 74,65-129,314 pt | caption: none | text-layer labels: none | nearby labels: Gateway | Mode | Protocol | Local Subnet | Remote Subnet | IKE Type Negotiation Mode | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 60 at 33,468-557,600 pt | caption: none | text-layer labels: none | nearby labels: Advanced Setting | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 87) -->
Enable Compression
Eo
Enable Forceencaps
Backup Gateway
Expert Options
<!-- end of figure 2 -->

<!-- pdf page 61 | printed page 61 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

PHASE 1

The window is displayed as below when choosing “PSK” as the authentication type.

The window is displayed as below when choosing “CA” as the authentication type.

The window is displayed as below when choosing “PKCS#12” as the authentication type.

<!-- figure 1 on pdf page 61 at 33,127-555,362 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/27 words >= 60, mean confidence 78) -->
[ses
Encryption Algorithm
Authentication Algorithm
IKE DH Group
DHgroup2
Authentication Type
PSK Secret
Local ID Type
Remote ID Type
IKE Lifetime
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 61 at 36,403-557,698 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 28/32 words >= 60, mean confidence 85) -->
Encryption Algorithm
Authentication Algorithm
IKE DH Group
[ca
Authentication Type
Local Certificate
None
[None
Remote Certificate(Optional)
[None
Private Key
[None
CA Certificate
Private Key Password
IKE Lifetime
86400
<!-- end of figure 2 -->

<!-- pdf page 62 | printed page 62 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

The window is displayed as below when choosing “xAuth PSK” as the authentication type.

The window is displayed as below when choosing “xAuth CA” as the authentication type.

<!-- figure 1 on pdf page 62 at 36,70-555,309 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/29 words >= 60, mean confidence 76) -->
Encryption Algorithm
Authentication Algorithm
IKE DH Group
Authentication Type
[None
Remote Certificate(Optional)
PKCS#12 Certificate
None
Private Key Password
IKE Lifetime
86400
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 62 at 33,336-555,544 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/26 words >= 60, mean confidence 78) -->
Encryption Algorithm
Authentication Algorithm
IKE DH Group
[xauth PSK
Authentication Type
PSK Secret
Local ID Type
[Defauit
Remote ID Type
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 62 at 33,549-552,643 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 85) -->
Username
Password
IKE Lifetime
<!-- end of figure 3 -->

<!-- pdf page 63 | printed page 63 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                  Description                                                                   Default
Encrypt Algorithm     Select from “3DES”, “AES128”, “AES192”and “AES256”.                           3DES
                       3DES: Use 168-bit 3DES encryption algorithm in CBC mode
                       AES128: Use 128-bit AES encryption algorithm in CBC mode
                       AES128: Use 192-bit AES encryption algorithm in CBC mode
                       AES256: Use 256-bit AES encryption algorithm in CBC mode
Authentication        Select from “MD5”, “SHA1”, “SHA2 256”,“SHA2 384” or “SHA2 512” .              MD5
Algorithm
IKE DH Group          Select from “DHgroup1”,“DHgroup2”, “DHgroup5”, “DHgroup14”,                   DHgroup2
                      “DHgroup15”, “DHgroup16”, “DHgroup17” or “DHgroup18” .
Authentication Type   Select from “PSK”, “CA”, “xAuth PSK” ,”PKCS#12”and “xAuth CA” to be used in   PSK
                      IKE negotiation.
                       PSK: Pre-shared Key
                       CA: Certification Authority
                       xAuth: Extended Authentication to AAA server
                       PKCS#12: Exchange digital certificate authentication
PSK Secret            Enter the pre-shared key.                                                     Null
Local ID Type         Select from “Default”, “Address”, “FQDN” and “User FQDN” .                    Default
                       Default: Uses an IP address as the ID in IKE negotiation
                       FQDN: Uses an FQDN type as the ID in IKE negotiation. If this option is
                           selected, type a name without any at sign (@) for the local security

<!-- figure 1 on pdf page 63 at 33,65-555,300 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 22/29 words >= 60, mean confidence 78) -->
Encryption Algorithm
v
Authentication Algorithm
IKE DH Group
Authentication Type
xAuth CA
Local Certificate
Remote Certificate(Optional)
[None
Private Key
[None
CA Certificate
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 63 at 33,305-552,417 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
Private Key Password
Username
Password
IKE Lifetime
86400
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 63 at 461,439-504,564 pt | caption: none | text-layer labels: none | nearby labels: Default 3DES | MD5 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 63 at 504,590-559,775 pt | caption: none | text-layer labels: PSK | Null Default | nearby labels: DHgroup2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 64 | printed page 64 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

Item                   Description                                                                        Default
                            router, e.g., test.robustel.com
                        User FQDN: Uses a user FQDN type as the ID in IKE negotiation. If this
                            option is selected, type a name string with a sign “@” for the local
                            security router, e.g., test@robustel.com
Remote ID Type         Select from “Default”, “FQDN” and “User FQDN” for IKE negotiation.                 Default
                        Default: Uses an IP address as the ID in IKE negotiation
                        FQDN: Uses an FQDN type as the ID in IKE negotiation. If this option is
                            selected, type a name without any at sign (@) for the local security
                            router, e.g., test.robustel.com
                        User FQDN: Uses a user FQDN type as the ID in IKE negotiation. If this
                            option is selected, type a name string with a sign “@” for the local
                            security router, e.g., test@robustel.com
IKE Lifetime           Set the lifetime in IKE negotiation. Before an SA expires, IKE negotiates a new    86400
                       SA. As soon as the new SA is set up, it takes effect immediately and the old
                       one will be cleared automatically when it expires.
Private Key Password   Enter the private key under the “CA” and “xAuth CA” authentication types.          Null
Username               Enter the username used for the “xAuth PSK” and “xAuth CA” authentication          Null
                       types.
Password               Enter the password used for the “xAuth PSK” and “xAuth CA” authentication          Null
                       types.

PHASE 2

Item                   Description                                                                       Default
Encrypt Algorithm      Select from “3DES”, “AES128”, “AES192”or “AES256” when you select “ESP”           3DES
                       in “Protocol”. Higher security means more complex implementation and
                       lower speed. DES is enough to meet general requirements. Use 3DES when
                       high confidentiality and security are required.
Authentication         Select from “MD5”, “SHA1”, “SHA2 256” or “SHA2 512” to be used in SA              MD5
Algorithm              negotiation.
PFS Group              Select from “PFS(N/A)”, “DHgroup1”,“DHgroup2”, “DHgroup5”,                        DHgroup2

<!-- figure 1 on pdf page 64 at 33,451-555,636 pt | caption: none | text-layer labels: none | nearby labels: PHASE 2 | OCR text follows (tesseract, unverified; 15/19 words >= 60, mean confidence 84) -->
Encryption Algorithm
Authentication Algorithm
PFS Group
[28800
SA Lifetime
[30
DPD Interval
[150
DPD Failures
<!-- end of figure 1 -->

<!-- pdf page 65 | printed page 65 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

 Item                     Description                                                                      Default
                          “DHgroup14”, “DHgroup15”, “DHgroup16”, “DHgroup17” or “DHgroup18”
                          to be used in SA negotiation.
 SA Lifetime              Set the IPsec SA lifetime. When negotiating to set up IPsec SAs, IKE uses the    28800
                          smaller one between the lifetime set locally and the lifetime proposed by
                          the peer.
 DPD Interval             Set the interval after which DPD is triggered if no IPsec protected packets is   30
                          received from the peer. DPD is a Dead peer detection. DPD irregularly
                          detects dead IKE peers. When the local end sends an IPsec packet, DPD
                          checks the time the last IPsec packet was received from the peer. If the time
                          exceeds the DPD interval, it sends a DPD hello to the peer. If the local end
                          receives no DPD acknowledgment within the DPD packet retransmission
                          interval, it retransmits the DPD hello. If the local end still receives no DPD
                          acknowledgment after having made the maximum number of
                          retransmission attempts, it considers the peer already dead, and clears the
                          IKE SA and the IPsec SAs based on the IKE SA.
 DPD Failures             Set the timeout of DPD (Dead Peer Detection) packets.                            150

Status

This section allows you to view the status of the IPsec tunnel.

<!-- figure 1 on pdf page 65 at 69,65-143,338 pt | caption: none | text-layer labels: none | nearby labels: Item | SA Lifetime | DPD Interval | DPD Failures | Status | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 65 at 519,65-559,338 pt | caption: none | text-layer labels: none | nearby labels: Default | 28800 | 30 | 150 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 65 at 36,451-555,511 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/7 words >= 60, mean confidence 88) -->
Tunnel Status
Index
Description
Status
Uptime
<!-- end of figure 3 -->

<!-- pdf page 66 | printed page 66 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

2.4.2 OpenVPN

This section allows you to set the OpenVPN and the related parameters. OpenVPN is an open-source software
application that creates secures point-to-point or site-to-site connections.

OpenVPN

Tunnel Setting

Click   to add an OpenVPN tunnel settings. The maximum count is 5. The configure page might vary when choosing
different mode, and the Authentication Type might be fixed for using on specific mode.
By default, the mode is “P2P”. The window is displayed as below when choosing “P2P” as the mode.

<!-- figure 1 on pdf page 66 at 33,201-559,281 pt | caption: none | text-layer labels: none | nearby labels: OpenVPN | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 96) -->
Status
Tunnel Settings
Index
Enable
Mode
Peer Address
Description
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 66 at 36,290-559,350 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 97) -->
Password Manage
Index
Username
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 66 at 36,357-559,417 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 96) -->
Client Manage
Enable
Client IP Address
Index
Common Name
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 66 at 33,532-557,739 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/17 words >= 60, mean confidence 82) -->
General Settings
Index
Enable
Description
[pap
Mode
[None
TLS Mode
Protocol
Peer Address
<!-- end of figure 4 -->

<!-- pdf page 67 | printed page 67 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

The window is displayed as below when choosing “Client” as the mode.

<!-- figure 1 on pdf page 67 at 31,65-555,506 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 44/45 words >= 60, mean confidence 90) -->
[1194
Peer Port
Listen IP Address
[1194
Listen Port
[run
Interface Type
[None
v]
Authentication Type
[10.8.0.1
Local IP
[10.8.0.2
Remote IP
[20
Ke
Keepalive Interval
[120
Keepalive Timeout
[1500
TUN MTU
Max Frame Size
Enable Compression
Enable NAT
[o
Verbose Level
Expert Options
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 67 at 31,516-557,756 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/20 words >= 60, mean confidence 73) -->
[1
Index
Enable
Description
[ctient
Mode
Protocol
Peer Address
[1194
Peer Port
[Tun
Interface Type
<!-- end of figure 2 -->

<!-- pdf page 68 | printed page 68 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

The window is displayed as below when choosing “Server” as the mode.

<!-- figure 1 on pdf page 68 at 31,70-557,343 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 26/30 words >= 60, mean confidence 84) -->
[None
Authentication Type
Renegotiation Interval
[20
Keepalive Interval
[120
Keepalive Timeout
TUN MTU
Max Frame Size
Enable Compression
Enable NAT
Enable DNS overrid
[0
Verbose Level
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 68 at 36,379-557,614 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/17 words >= 60, mean confidence 87) -->
Index
Enable
Description
[Server
Mode
Protocol
Listen IP Address
[1194
Listen Port
[run
Interface Type
<!-- end of figure 2 -->

<!-- pdf page 69 | printed page 69 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

(no text layer on this page)

<!-- pdf page 70 | printed page 70 | header: MG460 Software Manual | footer: RT147_SM_v1.0.1 / Dec 23, 2024 -->

The window is displayed as below when choosing “None” as the authentication type.

The window is displayed as below when choosing “Preshared” as the authentication type.

<!-- figure 1 on pdf page 70 at 31,82-557,333 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 24/27 words >= 60, mean confidence 87) -->
Listen IP Address
[1194
Listen Port
[run
Interface Type
Authentication Type
None
Local IP
Remote IP
[20
Keepalive Interval
[120
Keepalive Timeout
TUN MTU
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 70 at 31,367-557,607 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 23/27 words >= 60, mean confidence 85) -->
[1194
Listen Port
[run
Interface Type
Authentication Type
Pre-Share Key
None
Local IP
10.8.0.1
Remote IP
Encrypt Algorithm
Authentication Algorithm
[20
Keepalive Interval
<!-- end of figure 2 -->

<!-- pdf page 71 | printed page 71 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

The window is displayed as below when choosing “Password” as the authentication type.

The window is displayed as below when choosing “X509CA” as the authentication type.

<!-- figure 1 on pdf page 71 at 31,84-557,329 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 26/29 words >= 60, mean confidence 83) -->
Listen IP Address
[1194
Listen Port
[run
Interface Type
Authentication Type
Password
[10.8.0.1
Local IP
[10.8.0.2
Remote IP
[pr
Encrypt Algorithm
Authentication Algorithm
[20
Keepalive Interval
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 71 at 31,360-557,628 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 24/36 words >= 60, mean confidence 73) -->
Listen Port
[ru N
Interface Type
Authentication Type
Root CA
Certificate File
Private Key
Private Key Password
Local IP
Remote IP
10.8.0.2
Encrypt Algorithm
<!-- end of figure 2 -->

<!-- pdf page 72 | printed page 72 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

The window is displayed as below when choosing “X509CA Password” as the authentication type.

 Item                   Description                                                               Default
 Index                  Indicate the ordinal of the list.                                         --
 Enable                 Click the toggle button to enable/disable this OpenVPN tunnel.            ON
 Description            Enter a description for this OpenVPN tunnel.                              Null
 Mode                   Select from “P2P”, “Client” or “Server”.                                  P2P
 TLS Mode               Select from “None”, “Client” or “Server”.                                 None
 Protocol               Select from “UDP”, “TCP-Client” or “TCP-Server”.                          UDP
 Peer Address           Enter the end-to-end IP address or the domain of the remote OpenVPN       Null
                        server.
 Peer Port              Enter the end-to-end listener port or the listener port of the OpenVPN    1194
                        server.
 Listen IP Address      Enter the IP address or domain name.                                      Null
 Listen Port            Enter the listener port at this end.                                      1194
 Interface Type         Select from “TUN”, “TAP” which are two different kinds of device          TUN
                        interface for OpenVPN. The difference between TUN and TAP device is
                        that a TUN device is a point-to-point virtual device on network while a
                        TAP device is a virtual device on Ethernet.
 Authentication Type    Select from “None”, “Preshared”, “Password”, “X509CA”, “X509CA
                        password”.
                        Note:None and Preshared types only used for P2P mode. It must to add      Null
                        account from the User Management, when using server mode with
                        password authentication.
 Private Key Password   Enter the private key password under "X509CA" and "X509CA
                                                                                                  Null
                        password" authentication.
 Local IP               Enter the local virtual IP.                                               10.8.0.1
 Remote IP              Enter the remote virtual IP.                                              10.8.0.2
 Encrypt Algorithm      Select from “BF”, “DES”, “DES-EDE3”, “AES-128”, “AES-192” and             BF

<!-- figure 1 on pdf page 72 at 33,84-562,331 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 25/28 words >= 60, mean confidence 86) -->
[1194
Listen Port
[run
Interface Type
Authentication Type
Password
[None
Root CA
Certificate File
None
[None
Private Key
Private Key Password
Local IP
Remote IP
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 72 at 88,345-143,780 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 73 | printed page 73 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                   Description                                                               Default
                        “AES-256”.
                         BF: Use 128-bit BF encryption algorithm in CBC mode
                         DES: Use 64-bit DES encryption algorithm in CBC mode
                         DES-EDE3: Use 192-bit 3DES encryption algorithm in CBC mode
                         AES128: Use 128-bit AES encryption algorithm in CBC mode
                         AES192: Use 192-bit AES encryption algorithm in CBC mode
                         AES256: Use 256-bit AES encryption algorithm in CBC mode
 Authentication         Select from "MD5", "SHA1", "SHA256" or "SHA512".                          SHA1
 Algorithm
 Keepalive Interval     Set keepalive (ping) interval to check if the tunnel is active.           20
 Keepalive Timeout      Set the keepalive timeout. Trigger OpenVPN restart after n seconds pass   120
                        without reception of a ping or other packet from remote.
 TUN MTU                Set the MTU for the tunnel.                                               1500
 Max Frame Size         Sets the shard size of the data to be transmitted through the tunnel.     Null
 Enable Compression     Click the switch button to enable/disable this option. When enabled,
                                                                                                  ON
                        this feature compresses the header of the IP packet.
 Enable NAT             Click the toggle button to enable/disable the NAT option. When            OFF
                        enabled, the source IP address of host behind router will be disguised
                        before accessing the remote OpenVPN client.
 Verbose Level          Select the level of the output log and values from 0 to 11.               0
                         0: No output except fatal errors
                         1~4: Normal usage range
                         5: Output R and W characters to the console for each packet read
                              and write
                         6~11: Debug info range

 Item                  Description                                                                Default
 Expert Options        Enter some other options of OpenVPN in this field. Each expression can     Null
                       be separated by a ‘;’.

Client Management

Click   to add client information. The maximum count is 20.

<!-- figure 1 on pdf page 73 at 33,497-557,549 pt | caption: none | text-layer labels: none | nearby labels: Item Expert Options | Default Null | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 97) -->
Advanced Settings
Expert Options
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 73 at 33,554-141,607 pt | caption: none | text-layer labels: Item Expert Options | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 73 at 473,554-559,607 pt | caption: none | text-layer labels: Default Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 73 at 33,655-559,715 pt | caption: none | text-layer labels: none | nearby labels: Client Management | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 97) -->
Client Manage
Enable
Client IP Address
Index
Common Name
<!-- end of figure 4 -->

<!-- pdf page 74 | printed page 74 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                    Description                                                                   Default
 Index                   Indicate the ordinal of the list.                                             --
 Enable                  Click the switch button to enable/disable this option.                        ON
 Common Name             Specify a common name for the client.                                         Null
 Client IP Address       Specify the client's virtual IP address.                                      Null

Status

This section allows you to view the status of the OpenVPN tunnel.

2.4.3 GRE

This section allows you to set the GRE and the related parameters. Generic Routing Encapsulation (GRE) is a
tunneling protocol that can encapsulate a wide variety of network layer protocols inside virtual point-to-point links
over an Internet Protocol network. There are two main uses of GRE protocol: internal protocol encapsulation and
private address encapsulation.

<!-- figure 1 on pdf page 74 at 33,67-559,290 pt | caption: none | text-layer labels: Default -- ON Null Null | nearby labels: Status | OCR text follows (tesseract, unverified; 7/8 words >= 60, mean confidence 90) -->
Index
Enable
Common Name
Client IP Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 74 at 36,398-555,458 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/12 words >= 60, mean confidence 94) -->
OpenVPN Tunnel Status
Mode
Description
Index
Status
Local IPv4
Local IPv6
Uptime
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 74 at 36,468-555,528 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 92) -->
OpenVPN Client List
Index
Common Name
Real IP
Port
Virtual IPv4
Virtual
<!-- end of figure 3 -->

<!-- pdf page 75 | printed page 75 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

GRE

Click     to add tunnel settings. The maximum count is 5.

 Item                           Description                                                                Default
 Index                          Indicate the ordinal of the list.                                          --
 Enable                         Click the toggle button to enable/disable this GRE tunnel. GRE (Generic    ON
                                Routing Encapsulation) is a protocol that encapsulates data packets so
                                that it can route packets of other protocols in an IP network.
 Description                    Enter a description for this GRE tunnel.                                   Null
 Remote IP Address              Set the remote real IP address of the GRE tunnel.                          Null
 Local Virtual IP Address       Set the local virtual IP address of the GRE tunnel.                        Null
 Local Virtual Netmask/Prefix   Set the local virtual Netmask of the GRE tunnel.                           Null
 Remote Virtual IP Address      Set the remote virtual IP Address of the GRE tunnel.                       Null
 Enable Default Route           Click the toggle button to enable/disable this option. When enabled, all   OFF
                                the traffics of the router will go through the GRE VPN.

<!-- figure 1 on pdf page 75 at 36,144-557,204 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
Tunnel Settings
Index
Enable
Remote IP Address
Description
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 75 at 33,254-559,775 pt | caption: none | text-layer labels: Item Index Enable | Default -- ON | Null Null Null Null Null OFF | nearby labels: Click | OCR text follows (tesseract, unverified; 27/29 words >= 60, mean confidence 92) -->
Index
Enable
Description
Remote IP Address
Local Virtual IP Address
Local Virtual Netmask/Prefix Length
Remote Virtual IP Address
Enable Default Route
Enable NAT
Secrets
Link Binding
an
<!-- end of figure 2 -->

<!-- pdf page 76 | printed page 76 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Enable NAT                     Click the toggle button to enable/disable this option. This option must   OFF
                                be enabled when router under NAT environment.
 Secrets                        Set the key of the GRE tunnel.                                            Null
 Link Binding                   Set the specified interface of the GRE Tunnel                             wwan

Status

This section allows you to view the GRE tunnel status.

2.4.4 PPTP

This section is used to set the parameters of PPTP, a type of VPN protocol that uses a TCP control channel and a
Generic Routing Encapsulation tunnel to encapsulate PPP packets.

General

 Item                    Description                                                                  Default
 Enable User LED         Click the toggle button to enable/disable the user LED. If User LED is       OFF
                         enable here, it will have a higher priority.

<!-- figure 1 on pdf page 76 at 98,65-175,134 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 76 at 33,252-555,314 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
GRE tunnel status
Index
Description
Status
Local IP Address
Remote IP Address
Uptime
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 76 at 38,516-555,564 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 96) -->
General Settings
Enable User LED
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 76 at 33,571-141,624 pt | caption: none | text-layer labels: Item Enable User LED | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 76 at 457,571-559,624 pt | caption: none | text-layer labels: Default OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 77 | printed page 77 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

PPTP Server

 Item                   Description                                                                   Default
 Enable PPTP Server     Click the toggle button to enable/disable the PPTP server.                    OFF
 Username               Enter the name for PPTP server.                                               Null
 Password               Enter the password for PPTP server.                                           Null
 Local IP               IP address of this PPTP network interface.                                    Null
 Start IP               PPTP IP address leases will begin from the address specified in this field.   Null
 End IP                 PPTP IP address leases will end with the address specified in this field.     Null
 Authentication         Select from “pap”, “chap”, “mschap v1”, “mschap v2”.                          pap
 Enable NAT             Click the toggle button to enable/disable NAT.                                ON
 Expert Options         Enter some other options of PPTP in this field. Each expression can be        Null
                        separated by a ‘;’.
 Debug Enable           Click the toggle button to enable/disable debug.                              OFF

Click   to add a static route for PPTP server. The maximum count is 20.

<!-- figure 1 on pdf page 77 at 33,144-557,437 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 23/25 words >= 60, mean confidence 88) -->
Enable PPTP Server
Username
Password
Local IP
Start IP
End IP
[pap
Authentication
Enable NAT
Expert Options
noaccomp nopcomp nodeflate nobsdcomp
Debug Enable
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 77 at 512,453-559,652 pt | caption: none | text-layer labels: none | nearby labels: OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 77 at 33,664-557,727 pt | caption: none | text-layer labels: none | nearby labels: Debug Enable | Click | OFF | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 90) -->
Static Route
Index
Remote Subnet Remote Subnet...
Client IP
<!-- end of figure 3 -->

<!-- pdf page 78 | printed page 78 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                   Description                                  Default
 Index                  Indicate the ordinal of the list.            --
 Description            Enter a description for this static route.   Null
 Remote Subnet          Enter the remote subnet’s address.           Null
 Remote Subnet Mask     Enter the remote mask of subnet address.     Null
 Client IP              Enter the client IP, empty means anywhere.   Null

PPTP Client

Click   to add a PPTP client. The maximum count is 5.

<!-- figure 1 on pdf page 78 at 36,70-555,233 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 91) -->
Index
Description
Remote Subnet
Remote Subnet Mask
Client IP
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 78 at 347,237-483,338 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 78 at 33,458-557,520 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
PPTP Client Settings
Index
Enable
Description
Server Address
Authentication Remote Subnet Remote Subnet...
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 78 at 33,568-555,782 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 89) -->
Index
Enable
Description
Server Address
Username
Password
Authentication
<!-- end of figure 4 -->

<!-- pdf page 79 | printed page 79 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                    Description                                                                 Default
 Index                   Indicate the ordinal of the list.                                           --
 Enable                  Click the toggle button to enable/disable the PPTP client.                  OFF
 Server Address          Enter the IP address or hostname of a PPTP server.
 Username                Enter the name for PPTP server                                              Null
 Password                Enter the password for PPTP server                                          Null
 Authentication          Select from “pap”, “chap”, “mschap v1”, “mschap v2”.                        pap
 Enable NAT              Click the toggle button to enable/disable NAT.                              ON
 All Traffic via This    Click the toggle button to enable/disable this function.                    OFF
 Interface
 Remote Subnet           Enter the remote subnet address.                                            Null
 Remote Subnet           Enter the remote subnet address mask.                                       Null
 Mask
 Expert Options          Enter some other options of PPTP in this field. Each expression can be      Null
                         separated by a ‘;’.

Status

The status bar allows to view PPTP connection status. Click on one of the rows and details of its link connection will
be displayed below the current row.

<!-- figure 1 on pdf page 79 at 33,221-143,465 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 79 at 36,604-557,667 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
PPTP Server Status
Index
Remote IP Address
Uptime
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 79 at 36,676-557,736 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
PPTP Client Status
Index
Description
Status
Local IP Address
Remote IP Address
Uptime
<!-- end of figure 3 -->

<!-- pdf page 80 | printed page 80 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.4.5 L2TP

L2TP is a tunneling protocol used to support virtual private networks. It is more secure than PPTP because it
encapsulates the transferred data twice, but it is slower and uses more CPU power.

General

 Item                  Description                                                              Default
 Enable User LED       Click the toggle button to enable/disable the user LED. If User LED is   OFF
                       enable here, it will have a higher priority.

L2TP Server

<!-- figure 1 on pdf page 80 at 41,252-555,305 pt | caption: none | text-layer labels: none | nearby labels: Item Enable User LED | Default OFF | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 90) -->
General Settings
Enable User LED
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 80 at 33,309-141,362 pt | caption: none | text-layer labels: Item Enable User LED | nearby labels: L2TP Server | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 80 at 457,309-559,362 pt | caption: none | text-layer labels: Default OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 80 at 33,451-557,636 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/11 words >= 60, mean confidence 95) -->
Enable L2TP Server
Username
Password
Local IP
Start IP
End IP
<!-- end of figure 4 -->

<!-- pdf page 81 | printed page 81 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                   Description                                                                   Default
 Enable L2TP Server     Click the toggle button to enable/disable the L2TP server.                    OFF
 Username               Enter the name for L2TP server                                                Null
 Password               Enter the password for L2TP server                                            Null
 Local IP               IP address of this L2TP network interface.                                    Null
 Start IP               L2TP IP address leases will begin from the address specified in this field.   Null
 End IP                 L2TP IP address leases will end with the address specified in this field.     Null
 Tunnel Secrets         Enter the tunnel password.                                                    Null
 Authentication         Select from “pap”, “chap”, “mschap v1”, “mschap v2”.                          pap
 Port                   Enter the port of this tunnel.                                                1701
 Enable NAT             Click the toggle button to enable/disable NAT.                                OFF
 Expert Options         Enter some other options of L2TP in this field. Each expression can be        Null
                        separated by a ‘;’.
 Debug Enable           Click the toggle button to enable/disable debug.                              OFF

Click   to add a static route for L2TP server. The maximum count is 20.

<!-- figure 1 on pdf page 81 at 512,252-559,482 pt | caption: none | text-layer labels: none | nearby labels: OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 81 at 33,494-557,554 pt | caption: none | text-layer labels: none | nearby labels: Debug Enable | OFF | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 93) -->
A Static Route
Index
Remote Subnet Remote Subnet...
Client IP
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 81 at 36,607-555,770 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 91) -->
Index
Description
Remote Subnet
Remote Subnet Mask
Client IP
<!-- end of figure 3 -->

<!-- pdf page 82 | printed page 82 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                   Description                                 Default
 Index                  Indicate the ordinal of the list.           --
 Description            Enter a description for this L2TP server.   Null
 Remote Subnet          Enter the remote subnet address             Null
 Remote Subnet Mask     Enter the remote subnet address mask        Null
 Client IP              Enter the Client IP                         Null

L2TP Client

Click   to add a L2TP client. The maximum count is 5.

<!-- figure 1 on pdf page 82 at 328,65-483,168 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 82 at 33,285-555,345 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 95) -->
L2TP Client Settings
Index
Enable
Server Address
Authentication Remote Subnet Remote Subnet...
Description
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 82 at 33,393-555,765 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 30/31 words >= 60, mean confidence 93) -->
[1
Index
Enable
Description
Server Address
Username
Password
[pap
Authentication
Tunnel Secrets
Enable NAT
All Traffic via This Interface
Remote Subnet
Remote Subnet Mask
Expert Options
noaccomp nopcomp nodeflate nobsdcomp
<!-- end of figure 3 -->

<!-- pdf page 83 | printed page 83 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                    Description                                                                 Default
 Index                   Indicate the ordinal of the list.                                           --
 Enable                  Click the toggle button to enable/disable the PPTP client.                  OFF
 Description             Enter a description for this L2TP client.                                   Null
 Server Address          Enter the IP address or hostname of a L2TP server.                          Null
 Username                Enter the name for PPTP server                                              Null
 Password                Enter the password for PPTP server                                          Null
 Authentication          Select from “pap”, “chap”, “mschap v1”, “mschap v2”.                        pap
 Tunnel Secrets          Enter the tunnel password.                                                  Null
 Enable NAT              Click the toggle button to enable/disable NAT.                              ON
 All Traffic via This    Click the toggle button to enable/disable this function.                    OFF
 Interface
 Remote Subnet           Enter the remote subnet address.                                            Null
 Remote Subnet Mask      Enter the remote subnet address mask.                                       Null
 Expert Options          Enter some other options of PPTP in this field. Each expression can be      Null
                         separated by a ‘;’.

Status

The status bar allows to view L2TP connection status. Click on one of the rows and details of its link connection will
be displayed below the current row.

2.4.6 DMVPN

DMVPN is a routing technique we can use to build a VPN network with multiple sites without having to statically
configure all devices. It is a hub and spoke network, where the spokes will be able to communicate with each other
directly without having to go through the hub.

<!-- figure 1 on pdf page 83 at 409,82-559,343 pt | caption: none | text-layer labels: Null Null Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 83 at 33,84-141,343 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 83 at 36,482-557,542 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
L2TP Server Status
Index
Remote IP Address
Uptime
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 83 at 36,552-557,612 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
L2TP Client Status
Index
Description
Status
Local IP Address
Remote IP Address
Uptime
<!-- end of figure 4 -->

<!-- pdf page 84 | printed page 84 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

DMVPN

 Item                   Description                                                   Default
 Enable                 Click the toggle button to enable/disable the DMVPN client.   OFF
 Description            Enter a description for DMVPN client.                         Null
 DMVPN Type             Select DMVPN Type                                             Default
                        Default: Single hub mode
                        Dual-hub: Dual hub mode
 Link Binding           Select a link binding with DMVPN                              Null
 Hub Address            Enter the DMVPN hub address. e.g. 172.16.8.198                Null
 GRE Local IP Address   Enter local tunnel address, e.g. 182.16.0.1                   Null
 GRE HUB IP Address     Enter hub tunnel address, e.g. 182.16.0.100                   Null
 GRE Netmask            Enter tunnel netmask.                                         Null
 GRE Secrets            Enter GRE tunnel secret key.                                  Null
 GRE MTU                Enter the maximum transmission unit.                          1436

<!-- figure 1 on pdf page 84 at 33,146-559,302 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/15 words >= 60, mean confidence 76) -->
Enable DMVPN
Description
al
DMVPN Type
Link Binding
v
Hub Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 84 at 33,314-559,473 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/16 words >= 60, mean confidence 91) -->
GRE Local IP Address
Ke
GRE HUB IP Address
GRE Netmask
GRE Secrets
GRE MTU
1436
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 84 at 426,485-488,698 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 85 | printed page 85 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Item               Description                                                               Default
IKE Type           Select IKE Type                                                           IKEv1
Negotiation Mode   Select from “Main” and “aggressive” for the IKE negotiation mode in       Main
                   phase 1. If the IP address of one end of an IPSec tunnel is obtained
                   dynamically, the IKE negotiation mode must be aggressive. In this case,
                   SAs can be established as long as the username and password are
                   correct.
Local ID Type      Select from “ID”, “FQDN” and “User FQDN” for IKE negotiation. “Default”   Default
                   stands for “Router’s extern IP”.
                   ID: Uses custom string as the ID in IKE negotiation.
                   FQDN: Uses an FQDN type as the ID in IKE negotiation. If this option is
                   selected, type a name without any at sign (@) for the local security
                   gateway, e.g., test.robustel.com.
                   User FQDN: Uses a user FQDN type as the ID in IKE negotiation. If this

<!-- figure 1 on pdf page 85 at 33,70-559,302 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 22/30 words >= 60, mean confidence 74) -->
IKE Type
[Main
Negotiation Mode
Local ID Type
IKE Encryption Algorithm
IKE Authentication Algorithm
IKE DH Group
[Psk
Authentication Type
PSK Secret
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 85 at 33,314-559,420 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/12 words >= 60, mean confidence 71) -->
SA Encryption Algorithm
SA Authentication Algorithm
PFS Group
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 85 at 33,427-559,535 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 85) -->
Enable Zebra VTY
Enable NHRP VTY
Nhrp Holdtime(s)
7200
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 85 at 33,549-136,775 pt | caption: none | text-layer labels: Item IKE Type Negotiation Mode | Local ID Type | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 85 at 473,549-555,775 pt | caption: none | text-layer labels: Default IKEv1 Main | Default | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 86 | printed page 86 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                Description                                                              Default
                     option is selected, type a name string with an sign “@” for the local
                     security gateway, e.g., test@robustel.com.
 IKE Encryption      Select from “DES”, “3DES” and “AES128” to be used in IKE negotiation.    3DES
 Algorithm           DES: Uses the DES algorithm in CBC mode and 56-bit key.
                     3DES: Uses the 3DES algorithm in CBC mode and 168-bit key.
                     AES128: Uses the AES algorithm in CBC mode and 128-bit key.
 IKE Authen          Select from “MD5” and “SHA1”to be used in IKE negotiation.               MD5
 Algorithm           MD5: Uses HMAC-SHA1.
                     SHA1: Uses HMAC-MD5.
 IKE DH Group        Select from “MODP768_1”, “MODP1024_2” and “MODP1536_5”to be              MODP1024_2
                     used in key negotiation phase 1.
                     MODP768_1: Uses the 768-bit Diffie-Hellman group.
                     MODP1024_2: Uses the 1024-bit Diffie-Hellman group.
                     MODP1536_5: Uses the 1536-bit Diffie-Hellman group.
 Authentication Type Select Authentication Type                                               PSK
 PSK Secrets         Enter PSK secret key.                                                    Null
 SA Encryption       Select the SA Encryption Algorithm from “DES”, “3DES”, “AES 128”, “AES   3DES
 Algorithm           192”, “AES 256”.
 SA Authentication   Select the SA Authentication Algorithm from “MD5”, “SHA1”, “SHA2 256”,   SHA1
 Algorithm           “SHA2 512”.
 PFS Group           Select the PFS Group.                                                    PFS(N/A)

Status

The status bar allows to view DMVPN connection status.

<!-- figure 1 on pdf page 86 at 509,65-555,417 pt | caption: none | text-layer labels: none | nearby labels: Default | 3DES | MD5 | MODP1024_2 | SHA1 | PFS(N/A) | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 86 at 38,525-559,595 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 97) -->
Status
Uptime
<!-- end of figure 2 -->

<!-- pdf page 87 | printed page 87 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

X509

       x509

Item   Description

Default

                                                   X509 Settings
Root CA             Click “Choose File” to locate Root CA file and then import this file into your   --
                    device.
Certificate File    Click “Choose File” to locate Certificate file, and then import this file into   --
                    your device.
Private Key         Click “Choose File” to locate Private Key file, and then import this file into   --
                    your device.
                                                  Certificate Files
Index               Indicate ordinal of list.                                                        --
Filename            Show imported certificate’s name.                                                Null
File Size           Show size of certificate file.                                                   Null
Modification Time   Show timestamp of that the last time to modify the certificate file.             Null

<!-- figure 1 on pdf page 87 at 33,115-559,213 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 23/24 words >= 60, mean confidence 93) -->
X509 Settings
Local Certificate
Choose File No file chosen
Private Key
Choose File No file chosen
CA Certificate
Choose File No file chosen
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 87 at 33,223-559,283 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 95) -->
Local Certificate
Index
File Name
File Size
Modification Time
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 87 at 33,293-559,353 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 95) -->
Private Key
Index
File Name
File Size
Modification Time
<!-- end of figure 3 -->

<!-- pdf page 88 | printed page 88 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5      Services

2.5.1 Syslog

This section allows you to set the syslog parameters. The system log of the router can be saved in the local, also
supports to be sent to remote log server and specified application debugging. By default, the “Log to Remote” option
is disabled.

The window is displayed as below when enabling the “Log to Remote” option.

 Item                  Description                                                                        Default
 Enable                Click the toggle button to enable/disable the Syslog settings option.              ON
 Syslog Level          Select from “Debug”, “Info”, “Notice”, “Warning” or “Error”, which from low to     Debug
                       high. The lower level will output more syslog in details.
 Save Position         Select the save position from “RAM”, “NVM” or “Console”. The data will be          NVM
                       cleared after reboot when choose “RAM”.
                       Note: It's not recommended that you save syslog to NVM (Non-Volatile Memory)

<!-- figure 1 on pdf page 88 at 38,237-557,285 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/6 words >= 60, mean confidence 68) -->
Syslog Settings
Enable
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 88 at 36,439-555,650 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 18/22 words >= 60, mean confidence 80) -->
Enable
[Debug
Syslog Level
Save Position
je
Log to Remote
To
Add Identifier
Remote IP Address
Remote Port
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 88 at 33,669-134,784 pt | caption: none | text-layer labels: Item Enable Syslog Level | Save Position | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 88 at 509,669-559,784 pt | caption: none | text-layer labels: Default ON Debug | NVM | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 89 | printed page 89 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

                       for a long time.
 Log to Remote         Click the toggle button to enable/disable this option. Enable to allow router         ON
                       sending syslog to the remote syslog server. You need to enter the IP and Port of
                       the syslog server.
 Add Identifier        Click the toggle button to enable/disable this option. When enabled, you can add      OFF
                       serial number to syslog message which used for loading Syslog to RCMS.
 Remote IP Address     Enter the IP address of syslog server when enabling the “Log to Remote” option.       Null
 Remote Port           Enter the port of syslog server when enabling the “Log to Remote” option.             514

2.5.2 Event

This section allows you to set the event parameters. Event feature provides an ability to send alerts by SMS or Email
when certain system events occur.

Event

 Item                         Description                                                                Default
 Signal Quality Threshold     Set the threshold for signal quality. Device will generate a log event     0
                              when the actual threshold is less than the specified threshold. 0 means
                              disable this option.
 Temperature Threshold        Set the threshold for temperature. Device will generate a log event        0
                              when the actual threshold is less than the specified threshold. 0 means
                              disable this option.
 Estimate Remaining Flash     Set the estimate of EMMC life. Device will generate a log event when       20%-30%
 Lifetime                     the actual estimate is in the specified parameter range.

<!-- figure 1 on pdf page 89 at 36,405-557,511 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/15 words >= 60, mean confidence 83) -->
General Settings
[o
Signal Quality Threshold
Temperature Threshold
[20%-30%
Estimated Remaining Flash Lifetime
<!-- end of figure 1 -->

<!-- pdf page 90 | printed page 90 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Notification

Click   button to add an Event parameters.

 Item              Description                                                                               Default
 Index             Indicate the ordinal of the list.                                                         --
 Description       Enter a description for this group.                                                       Null
 Sent SMS          Click the toggle button to enable/disable this option. When enabled, the router will      OFF
                   send notification to the specified phone numbers via SMS if event occurs. Set the
                   related phone number in “3.21 Services > Email”, and use ‘;’to separate each
                   number.
 Send Email        Click the toggle button to enable/disable this option. When enabled, the router will      OFF
                   send notification to the specified email box via Email if event occurs. Set the related
                   email address in “3.21 Services > Email”.
 DO Control        Click the toggle button to enable / disable this option. After it is turned on, the       OFF
                   event router will send it to the corresponding DO in the form of Low / High level.
 Save to NVM       Click the toggle button to enable/disable this option. Enable to save event to            OFF
                   nonvolatile memory.

<!-- figure 1 on pdf page 90 at 36,144-557,204 pt | caption: none | text-layer labels: none | nearby labels: Click | button to add an Event parameters. | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 96) -->
Event Notification Group Settings
Index
Send SMS
Send Email
DO Control
Description
Save to NVM
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 90 at 33,240-557,425 pt | caption: none | text-layer labels: none | nearby labels: Click | button to add an Event parameters. | OCR text follows (tesseract, unverified; 11/14 words >= 60, mean confidence 84) -->
Index
Description
Send SMS
Send Email
DO Control
Save to NVM
<!-- end of figure 2 -->

<!-- pdf page 91 | printed page 91 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->



<!-- figure 1 on pdf page 91 at 36,72-557,326 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 31/31 words >= 60, mean confidence 96) -->
Event Selection
System Startup
System Reboot
System Time Update
Configuration Change
Cellular Network Type Change
Cellular Data Stats Clear
Cellular Data Traffic Overflow
Poor Signal Quality
Wan data traffic stats clear
<!-- end of figure 1 -->

<!-- pdf page 92 | printed page 92 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Item    Description                                                        Default
Event   Click the toggle button to enable this option to generate a log.   OFF

<!-- figure 1 on pdf page 92 at 33,331-557,492 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 18/19 words >= 60, mean confidence 90) -->
DI 1 Counter Overflow
DI2 ON
DI 2 OFF
Di 2 Counter Overflow
Excessive Temperature
Life Time Alert
<!-- end of figure 1 -->

<!-- pdf page 93 | printed page 93 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Query

In the following window you can query various types of events record. Click          to query filtered events while
click        to clear the event records in the window.

 Item               Description                                                                           Default
 Save Position      Select the events’ save position from “RAM” or “NVM”.                                 NVM
                     RAM: Random-access memory
                     NVM: Non-Volatile Memory
 Filtering          Enter the filtering message based on the keywords set by users. Click the “Refresh”   Null
                    button, the filtered event will be displayed in the follow box. Use “&” to separate
                    more than one filter message, such as message1&message2.

<!-- figure 1 on pdf page 93 at 33,110-559,173 pt | caption: none | text-layer labels: click | to query filtered events while | nearby labels: Query | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 58) -->
Event
Notification
Query
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 93 at 33,180-559,556 pt | caption: none | text-layer labels: Item Save Position | Filtering | Default NVM | Null | OCR text follows (tesseract, unverified; 171/196 words >= 60, mean confidence 85) -->
Save Position
Filtering
switch link,
from WWAN1 to
Mar
27
17
54
12
switch link, from WWAN2 to
Mar
57
15
af
link down,
ethd
Mar
27
59
28,
LAN port
link
down,
Mar
17
59
2
LAN port
link
ethl
Mar
27
17
59:34.
LAN port
up,
H
link
ethd
Mar
17
59
40,
LAN port
up,
LAN port link
down,
Mar
27
59
40
link
ethl
Mar
27
59
LAN port
1
46,
up,
switch link,
from WWAN1 to
Mar
27
18
00
18,
WWANZ
LAN port link down
Mar
27
18
00
46,
switch
link,
fron
Mar
27
18
03
21,
WWANZ
to
fron
link,
switch
Mar
06
WWANZ
25:
18
to
switch
link,
from
27
18
28,
WWANZ
Mar
03
to
switch
link,
fron
12
WWANZ
Mar
18
af
t
switch
link,
from
Mar
27
18
15
WWAN2
to
switch
link,
from
Mar
18
18
to
of,
af
switch
link,
from
Mar
oF
18
40,
to
af
switch
from
link,
Mar
27
18
24
WWAN2
44,
to
<!-- end of figure 2 -->

<!-- pdf page 94 | printed page 94 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.3 NTP

This section allows you to set the related NTP (Network Time Protocol) parameters.

NTP

 Item                     Description                                                               Default
 Time Zone                Click the drop down list to select the time zone you are in.              UTC +08:00

 Item                     Description                                                               Default
 Enable                   Click the toggle button to enable/disable this option. Enable to          ON
                          synchronize time with the NTP server.
 Primary NTP Server       Enter primary NTP Server’s IP address or domain name.                     pool.ntp.org
 Secondary NTP Server     Enter secondary NTP Server’s IP address or domain name.                   Null
 NTP Update interval      Enter the interval (minutes) synchronizing the NTP client time with the   0
                          NTP server’s. Minutes wait for next update, and 0 means update only
                          once.

  Item                     Description                                                               Default

<!-- figure 1 on pdf page 94 at 33,221-559,317 pt | caption: none | text-layer labels: Item Time Zone | Default UTC +08:00 | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 96) -->
Timezone Settings
Time Zone
Asia-Shanghai
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 94 at 33,331-559,600 pt | caption: none | text-layer labels: Item Enable | Default ON | pool.ntp.org Null 0 | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 83) -->
Enable
Primary NTP Server
pool.ntp.org
Secondary NTP Server
NTP Update Interval
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 94 at 33,614-567,772 pt | caption: none | text-layer labels: Description | Default | Item | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 88) -->
Enable
Primary NTP Server
pool.ntp.org
Secondary NTP Server
lo
NTP Update Interval
<!-- end of figure 3 -->

<!-- pdf page 95 | printed page 95 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

  Enable                    Click the toggle button to enable/disable the NTP server option.             OFF
  Primary NTP Server        Enter the primary NTP server                                                 pool.ntp.org
  Secondary NTP Server      Enter the secondary NTP server                                               Null
  NTP Update Interval       Enter the NTP update interval, 0 means update only once.                     0

 Item                     Description                                                                   Default
 Enable                   Click the toggle button to enable/disable the NTP server option.              OFF

Status

This window allows you to view the current time of router and also synchronize the router time. Click         button
to synchronize the router time with the PC’s time.

2.5.4 SMS

This section allows you to set SMS parameters. Device supports SMS management, and user can control and
configure their devices by sending SMS. For more details about SMS control, refer to 3.1.2 SMS Remote Control.

SMS

<!-- figure 1 on pdf page 95 at 452,65-495,134 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 95 at 38,149-557,204 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 95) -->
NTP Server Settings
Enable
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 95 at 36,386-555,487 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
System Time
2022-05-07 16:27:05
PC Time
2022-05-07 16:27:07
Last Update Time
2022-05-07 08:48:25
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 95 at 38,674-559,782 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/8 words >= 60, mean confidence 84) -->
Enable
[Password
Authentication Type
v
Phone Number
<!-- end of figure 4 -->

<!-- pdf page 96 | printed page 96 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                     Description                                                                  Default
 Enable                   Click the toggle button to enable/disable the SMS Management option.         ON
                          Note: If this option is disabled, the SMS configuration is invalid.
 Authentication Type      Select Authentication Type from “Password”, “Phonenum” or “Both”.            Password
                          Password: Use the same username and password as WEB manager for
                          authentication. For example, the format of the SMS should be “username:
                          password; cmd1; cmd2; …”
                          Note: Set the WEB manager password in System > User Management section.
                          Phonenum: Use the Phone number for authentication, and user should set the
                          Phone Number that is allowed for SMS management. The format of the SMS
                          should be “cmd1; cmd2; …”
                          Both: Use both the “Password” and “Phonenum” for authentication. User
                          should set the Phone Number that is allowed for SMS management. The
                          format of the SMS should be “username: password; cmd1; cmd2; …”
 Phone Number                                                                                          Null
                          Set the phone number used for SMS management, and click       to add new
                          phone number.
                          Note: It can be null when choose “Password” as the authentication type.

SMS Testing

User can test the current SMS service whether it is available in this section.

 Item                  Description                                                                     Default
 Phone Number          Enter the specified phone number which can receive the SMS from router.         Null
 Message               Enter the message that router will send it to the specified phone number.       Null
 Result                The result of the SMS test will be displayed in the result box.                 Null
                       Click the button to send the test message.                                      --

<!-- figure 1 on pdf page 96 at 36,506-555,674 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 96) -->
Phone Number
Message
Result
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 96 at 33,691-127,777 pt | caption: none | text-layer labels: Item Phone Number Message Result | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 95) -->
Send
<!-- end of figure 2 -->

<!-- pdf page 97 | printed page 97 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.5 Email

Email function supports to send the event notifications to the specified recipient by ways of email.

 Item                 Description                                                                      Default
 Enable               Click the toggle button to enable/disable the Email option.                      OFF
 Enable TLS/SSL       Click the toggle button to enable/disable the TLS/SSL option.                    OFF
 Enable STARTTLS      Click the toggle button to enable / disable STARTTLS encryption.                 OFF
 Outgoing server      Enter the SMTP server IP Address or domain name.                                 Null
 Server port          Enter the SMTP server port.                                                      25
 Timeout              Set the max time for sending email to SMTP server. When the server doesn’t       10
                      receive the email over this time, it will try to resend.
 Auth Login           If the mail server supports AUTH login, you must enable this button and set a    OFF
                      username and password.
 Username             Enter the username which has been registered from SMTP server.                   Null
 Password             Enter the password of the username above.                                        Null
 From                 Enter the source address of the email.                                           Null
 Subject              Enter the subject of this email.                                                 Null

<!-- figure 1 on pdf page 97 at 36,185-557,501 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 18/22 words >= 60, mean confidence 81) -->
Enable
To
Enable TLS/SSL
Enable STARTTLS
Outgoing Server
Server Port
Timeout
To
Auth Login
Username
Password
From
Subject
<!-- end of figure 1 -->

<!-- pdf page 98 | printed page 98 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.6 DDNS

This section allows you to set the DDNS parameters. The Dynamic DNS function allows you to alias a dynamic IP
address to a static domain name, allows you whose ISP does not assign them a static IP address to use a domain
name. This is especially useful for hosting servers via your connection, so that anyone wishing to connect to you may
use your domain name, rather than having to use your dynamic IP address, which changes from time to time. This
dynamic IP address is the WAN IP address of the router, which is assigned to you by your ISP. The service provider
defaults to “DynDNS”, as shown below.

DDNS

Click   to add a new Dynamic Domain Name Server.

When “Custom” service provider chosen, the window is displayed as below.

<!-- figure 1 on pdf page 98 at 38,295-557,355 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 96) -->
DDNS Settings
Index
Enable
Service Provider
Link Binding
Hostname
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 98 at 33,410-559,650 pt | caption: none | text-layer labels: none | nearby labels: Click | to add a new Dynamic Domain Name Server. | OCR text follows (tesseract, unverified; 13/17 words >= 60, mean confidence 78) -->
Index
Enable
Service Provider
Hostname
Username
Password
Link Binding
wwan
[3
Max Tries
<!-- end of figure 2 -->

<!-- pdf page 99 | printed page 99 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                    Description                                                               Default
 Enable                  Click the toggle button to enable/disable the DDNS option.                OFF
 Service Provider        Select the DDNS service from “DynDNS”, “NO-IP”, “3322” or                 DynDNS
                         “Custom”.
                         Note: The DDNS service only can be used after registered by
                         Corresponding service provider.
 Hostname                Enter the hostname provided by the DDNS server.                           Null
 Username                Enter the username provided by the DDNS server.                           Null
 Password                Enter the password provided by the DDNS server.                           Null
 URL                     Enter the URL customized by user.                                         Null
 Max tries               Enter the maximum tries times                                             3

Status

The status bar allows to view DDNS connection status.

 Item                      Description
 Status                    Display the current status of the DDNS.
 Last Update Time          Display the date and time for the DDNS was last updated successfully.

<!-- figure 1 on pdf page 99 at 33,65-557,225 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/11 words >= 60, mean confidence 85) -->
[1
Index
Enable
[custom
Service Provider
URL
E
Max Tries
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 99 at 93,237-146,417 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 99 at 426,237-469,417 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 99 at 497,237-559,417 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 99 at 36,535-557,597 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
DDNS Status
Index
Last Update Time
Status
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 99 at 481,614-559,667 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 100 | printed page 100 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.7 VRRP

This section allows you to set the VRRP parameters. VRRP stands for Virtual Router Redundancy Protocol, is a
standard for device redundancy and failover that creates a virtual router with a floating IP address.

VRRP Settings

 Item                    Description                                                               Default
 Enable                  Click the toggle button to enable/disable the VRRP option.                OFF
 Interface               Selects which interface VRRP will operate on.                             --
 Group ID                The Virtual Router Identifier. Routers with identical IDs will be
                                                                                                   1
                         grouped in the same VRRP cluster.
 Priority                VRRP priority of the virtual router. Higher values equal higher
                                                                                                   100
                         priority.
 Interval                Interval value in second, must be the same for all routing platforms in
                                                                                                   1
                         the VRRP group.
 Virtual IP Address      Virtual IP address for the router's VRRP cluster.                         Null

Ping Detection Settings

 Item                    Description                                                               Default
 Enable                  Click the toggle button to enable/disable the option.                     OFF

<!-- figure 1 on pdf page 100 at 33,199-559,391 pt | caption: none | text-layer labels: none | nearby labels: VRRP Settings | OCR text follows (tesseract, unverified; 10/15 words >= 60, mean confidence 75) -->
Enable
Interface
Group ID
Priority
100
Interval
Virtual IP Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 100 at 81,403-146,568 pt | caption: none | text-layer labels: none | nearby labels: Priority | Interval | Virtual IP Address | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 100 at 33,624-557,734 pt | caption: none | text-layer labels: none | nearby labels: Ping Detection Settings | OCR text follows (tesseract, unverified; 3/6 words >= 60, mean confidence 60) -->
Enable
Server
Interval
<!-- end of figure 3 -->

<!-- pdf page 101 | printed page 101 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Server                    The ping detection sever address.                                      8.8.8.8
 Interval                  Interval value for ping detection in second.                           300

2.5.8 SSH

Device supports SSH password access and secret-key access.

 Item                        Description                                                                    Default
 Enable                      Click the toggle button to enable/disable this option. When enabled, you can   ON
                             access the router via SSH.
 Port                        Set the port of the SSH access.                                                22
 Disable Password Logins     Click the toggle button to enable/disable this option. When enabled, you       OFF
                             cannot use username and password to access the router via SSH. In this
                             case, only the key can be used for login.

2.5.9 GNSS

This section is used to configure the parameters of GNSS. The GNSS function of device can locate and acquire the
location information of the device and report it to the designated server.

GNSS

<!-- figure 1 on pdf page 101 at 38,223-555,355 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/12 words >= 60, mean confidence 78) -->
Enable
[22
Port
Disable Password Logins
Authorized Keys
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 101 at 33,374-155,489 pt | caption: none | text-layer labels: Item Enable | Port Disable Password Logins | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 101 at 512,374-559,489 pt | caption: none | text-layer labels: Default ON | 22 OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 101 at 41,688-550,768 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 84) -->
General Settings
Enable GNSS
Taal
Sync GNSS Time
<!-- end of figure 4 -->

<!-- pdf page 102 | printed page 102 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Click   to add a new GNSS Server. The maximum count is 5.

 Item                   Description                                              Default
 Index                  Indicate the ordinal of the list.                        --
 Enable                 Click the toggle button to enable/disable the server.    ON
 Protocol               Select from “TCP Client”, “TCP Server”, “UDP”.           TCP Client
 Server/Local Address   Server or local IP address.                              Null
 Server/Local Port      Server or local IP port.                                 Null
 Send GGA Sentence      Click the toggle button to enable/disable this option.   OFF
 Send VTG Sentence      Click the toggle button to enable/disable this option.   OFF
 Send RMC Sentence      Click the toggle button to enable/disable this option.   OFF
 Send GSV Sentence      Click the toggle button to enable/disable this option.   OFF

<!-- figure 1 on pdf page 102 at 38,65-557,223 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 94) -->
Report to RS232
Report GGA Sentence
Report VTG Sentence
Report RMC Sentence
Report GSV Sentence
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 102 at 36,230-552,293 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
GNSS Servers
Index
Enable
Protocol
Local Address
Local Port
Server Address
Server Port
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 102 at 36,331-555,595 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 21/22 words >= 60, mean confidence 92) -->
E
Index
Enable
Protocol
Client
Server Address
Server Port
Send GGA Sentence
Send VTG Sentence
Send RMC Sentence
Send GSV Sentence
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 102 at 392,612-469,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 103 | printed page 103 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                         Description                                              Default
 Add SN as GNSSID             Click the toggle button to enable/disable this option.   OFF
 Self-define GNSSID Prefix    Self-define GPSIS Prefix, four upper case.               Null

Status

Item                         Description
Status                       Shows the current GNSS status of the router.
                             Shows the UTC of satellite.
UTC Time
                             Note: UTC is the world's unified time, not local time.
Last Fixed Time              The time of the last successful positioning.
Satellites In Use            Number of satellites used
Satellites In View           Number of visible satellites
Latitude                     Shows the Latitude information of the router.
Longitude                    Shows the longitude information of the router.
Altitude                     Shows the height information of the router.
Speed                        Shows the speed information of the router.

<!-- figure 1 on pdf page 103 at 38,89-555,170 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/10 words >= 60, mean confidence 81) -->
Advanced Settings
Add SN as GNSSID
GNSSID Prefix
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 103 at 409,175-469,228 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 103 at 514,175-559,228 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 103 at 41,324-552,542 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/16 words >= 60, mean confidence 96) -->
Status
UTC Time
Last Fixed Time
Satellites In Use
Satellites In View
Latitude
Longitude
Altitude
Speed
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 103 at 74,564-155,746 pt | caption: none | text-layer labels: none | nearby labels: Item Status | UTC Time | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 6 on pdf page 103 at 399,564-559,746 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 104 | printed page 104 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Map

The Map page displays the device's current coordinates and position on the map. To see the device's location on the
map, make sure to attach the GNSS antenna on the device and enable GNSS in the GNSS page.

Click the                button to view in a new tab.

<!-- figure 1 on pdf page 104 at 33,166-552,530 pt | caption: none | text-layer labels: none | nearby labels: Click the | button to view in a new tab. | OCR text follows (tesseract, unverified; 10/128 words >= 60, mean confidence 30) -->
GPS
Map
Status
an
x
S15
OS
w
le
ve
<!-- end of figure 1 -->

<!-- pdf page 105 | printed page 105 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.10       RCMS

This section allows you to set the RCMS parameters. Robustel Cloud Manager Service (RCMS) is a modular IoT cloud
software platform compatible with all Robustel products.

RCMS

 Item                   Description                                                          Default
 Enable RCMS            Click the toggle button to enable/disable this option.               OFF
 Enable RobustLink      Click the toggle button to enable/disable this option.               OFF
 Enable RobustVPN       Click the toggle button to enable/disable this option.               OFF
 Paho log detail        Click the toggle button to enable/disable this option.
                                                                                             OFF
 enable
 RCMS Environment       Select RCMS Environment                                              RCMS Cloud
                                                                                             International

 Item                   Description                                                          Default
 KeepAlive              KeepAlive determines how long your device checks in with RCMS. A
                                                                                             600
                        shorter KeepAlive will update RCMS more frequently but consume

<!-- figure 1 on pdf page 105 at 36,233-559,389 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/18 words >= 60, mean confidence 82) -->
Enable RCMS
Enable RobustLink
Enable RobustVPN
Paho log detail enable
RCMS Environment
Cloud International
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 105 at 514,403-559,535 pt | caption: none | text-layer labels: none | nearby labels: RCMS Cloud International | OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 105 at 33,554-559,710 pt | caption: none | text-layer labels: none | nearby labels: Default | OCR text follows (tesseract, unverified; 20/25 words >= 60, mean confidence 79) -->
[600
KeepAlive
v]
Dynamic Report Capture
Dynamic Report Upload
[on GPS co-ordinate change
v}
GPS Reporting Settings
GPS Distance Threshold
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 105 at 33,720-146,770 pt | caption: none | text-layer labels: Item KeepAlive | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 105 at 459,720-559,770 pt | caption: none | text-layer labels: Default | 600 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 106 | printed page 106 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

                 more data.
Dynamic Report   Select the capture period of dynamic data is logged in the device
                                                                                      60min
Capture
Dynamic Report   Select the upload period of dynamic data is update in the device
                                                                                      60min
Upload
GPS Reporting    Select GPS Reporting way:
                                                                                      On GPS
Settings           - On GPS co-ordinate change - Report when GPS is updated
                                                                                      co-ordinate
                   - Only with Dynamic Report - Collect and report in sync with the
                                                                                      change
                        Data Collection Interval and Data Reporting Frequency
GPS Distance     GPS data will be updated when the current position exceeds this
Threshold        value; Unit:meters                                                   20
                 Valid Range:10-10000

Item             Description                                                          Default
Enable Ping      Click the toggle button to enable/disable this option.               OFF
Primary Server   Enter the ping server.                                               8.8.8.8
Ping Timeout     Enter the time of waiting for a ping response. Unit: seconds         5
Ping Count       Enter the number of pings conducted to calculate average.            3

<!-- figure 1 on pdf page 106 at 33,65-148,259 pt | caption: none | text-layer labels: GPS Distance Threshold | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 106 at 36,276-559,410 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/12 words >= 60, mean confidence 82) -->
Enable Ping
Primary Server
E
Ping Timeout
E
Ping Count
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 106 at 423,427-469,513 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 106 at 514,427-559,513 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 107 | printed page 107 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Event Selection

<!-- pdf page 108 | printed page 108 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Status

Item                          Description
RobustLink Status             Show the status of RobustLink
RobustelLink Last Connected   Show the last connected times of RobustLink
RobustVPN Status              Show the status of RobustVPN
RobustVPN Last Connected      Show the last connected times of RobustVPN
RobustVPN Virtual IP          Show the virtual IP of RobustVPN
RobustVPN SubNet Address      Show the subnet address of RobustVPN

<!-- figure 1 on pdf page 108 at 33,144-559,432 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/20 words >= 60, mean confidence 95) -->
RobustLink Status
Connected
RobustLink Last Connected
2023-05-30 13:54:59
RobustVPN Status
RobustVPN Last Connected
Never
RobustVPN Virtual IP
RobustVPN SubNet Address
<!-- end of figure 1 -->

<!-- pdf page 109 | printed page 109 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.11       SNMP

This section allows you to set the SNMP parameters. Simple Network Management Protocol is a network
management protocol used for collecting information and configuring network devices.

SNMP Agent

 Item                   Description                                                          Default
 Enable SNMP Agent      Click the toggle button to enable/disable this option.               OFF
 Port                   SNMP service's port.                                                 161
 OEM Enable             Click the toggle button to enable/disable this option.               OFF
 OEM Enterprise         OEM enterprise information.                                          Null
 OEM Platform           OEM platform information.                                            Null
 Version                The SNMP version, select from “SNMPv3” or “SNMPv1v2v3”.              SNMPv3
 Location Info          System location information.                                         Null
 Contact Info           System contact information.                                          Null
 System Name            System name.                                                         Null
 Readonly Community     Access mode for current community.
                                                                                             Null
 Name
 Readwrite              Access mode for current community.                                   Null

<!-- figure 1 on pdf page 109 at 33,206-557,547 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 28/31 words >= 60, mean confidence 89) -->
SNMP Agent
SNMP Trap
MIBS
Enable SNMP Agent
[161
Port
OEM Enable
OEM Enterprise
OEM Platform
Version
Location Info
Contact Info
System Name
[mos
Authentication Algorithm
Privacy Algorithm
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 109 at 323,559-469,772 pt | caption: none | text-layer labels: none | nearby labels: Null | Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 109 at 497,559-559,772 pt | caption: none | text-layer labels: none | nearby labels: Null | Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 110 | printed page 110 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Community Name
Authentication      Select from “MD5”, “SHA”.
Algorithm
Privacy Algorithm   Select from “DES”, “AES”.

SNMP Trap

MD5

DES

SNMP Trap Rules are alerts that trigger when certain user-specified events occur. When the trigger event happens,
the trap will notify known SNMP hosts.

 Item                    Description                                                             Default
 Enable SNMP Agent       Click the toggle button to enable/disable this option.                  OFF
 Receiver Address        Host name or IP address to transfer SNMP traffic to.                    Null
 Receiver Port           Trap host's port number.                                                162
 User name               The user name access to SNMP.                                           Null
 Authentication          Select from “MD5”, “SHA”.
                                                                                                 MD5
 Algorithm
 Authentication          Enter the authentication password.
                                                                                                 Null
 Password
 Privacy Algorithm       Select from “DES”, “AES”.                                               DES
 Privacy Password        Enter the privacy password.                                             Null

<!-- figure 1 on pdf page 110 at 33,257-550,389 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 82) -->
Enable SNMP Trap
Version
Receiver Address
Receiver Port
162
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 110 at 36,401-555,559 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/12 words >= 60, mean confidence 86) -->
Username
[mos
Authentication Algorithm
Authentication Password
[pes
Privacy Algorithm
Privacy Password
<!-- end of figure 2 -->

<!-- pdf page 111 | printed page 111 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Click the toggle button the enable or disable the related event.

<!-- figure 1 on pdf page 111 at 36,118-557,643 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 54/54 words >= 60, mean confidence 96) -->
System Startup
System Reboot
System Time Update
Configuration Change
Cellular Network Type Change
Cellular Data Stats Clear
Cellular Data Traffic Overflow
Poor Signal Quality
Link Switching
WAN Up
WAN Down
WWAN Up
WWAN Down
IPSec Connection Up
IPSec Connection Down
OpenVPN Connection Up
OpenVPN Connection Down
LAN Port Link Up
LAN Port Link Down
<!-- end of figure 1 -->

<!-- pdf page 112 | printed page 112 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

MIBS

MIB stands for Management Information Base, a MIB contains the variables that the managed device maintains and
can be queried or set by the agent. The MIB defines the attributes of the managed device, including the name, status,
access rights, and data type.

 Item                     Description                                                                     Default
 MIBS                                                                                                     --
                          Click            to generate and click             to download the device's

                          MIB file.

<!-- figure 1 on pdf page 112 at 36,67-557,413 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 32/37 words >= 60, mean confidence 83) -->
USB Device Connect
USB Device Remove
DDNS Update Success
DDNS Update Fail
Received SMS
SMS Command Execute
DI1ON
DI 1 OFF
DI 1 Counter Overflow
OFF
DI 2 Counter Overflow
Excessive Temperature
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 112 at 33,564-559,715 pt | caption: none | text-layer labels: Item MIBS | Description | Click | to generate and click | to download the device's | Default -- | MIB file. | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 92) -->
SNMP MIBS
SNMP MIBS
Download
<!-- end of figure 2 -->

<!-- pdf page 113 | printed page 113 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.5.12        Web Server

This section allows you to modify the parameters of Web Server.

 Item                    Description                                                                          Default
 HTTP Port               Enter the HTTP port number you want to change in router’s Web Server. On a           80
                         Web server, port 80 is the port that the server "listens to" or expects to receive
                         from a Web client. If you configure the router with other HTTP Port number
                         except 80, only adding that port number then you can login router’s Web
                         Server.
 HTTPS Port              Enter the HTTPS port number you want to change in router’s Web Server. On a          443
                         Web server, port 443 is the port that the server "listens to" or expects to
                         receive from a Web client. If you configure the router with other HTTPS Port
                         number except 443, only adding that port number then you can login router’s
                         Web Server.
                         Note: HTTPS is more secure than HTTP. In many cases, clients may be
                         exchanging confidential information with a server, which needs to be secured in
                         order to prevent unauthorized access. For this reason, HTTP was developed by
                         Netscape corporation to allow authorization and secured transactions.
 HTTPS CA Certificate    Select one once the certification is imported, see 2.6.2 Certificate Manager.
 HTTPS Private Keys      Select one once the certification is imported, see 2.6.2 Certificate Manager.

2.5.13        Advanced

This section allows you to set the Advanced and parameters. Advanced router settings include system settings and
reboot.

<!-- figure 1 on pdf page 113 at 38,161-555,295 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/19 words >= 60, mean confidence 79) -->
General Settings
HTTP Port
[443
HTTPS Port
HTTPS CA Certificate
[None
HTTPS Private Keys
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 113 at 91,312-143,585 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 113 at 512,312-559,585 pt | caption: none | text-layer labels: Default 80 | 443 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 114 | printed page 114 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Item                Description                                                                      Default
Device Name         Set the device name to distinguish different devices you have installed; valid   460-gateway
                    characters are a-z, A-Z, 0-9, @, ., -, #, $, and *.
USR LED Type         Specify the display type of your USR LED. Select from “None”, “OpenVPN”        OpenVPN
                         or “IPsec”,”SIM”, “PPTP”, “L2TP”, “RCMS”, “COM” .
                     None: Meaningless indication, and the LED is off
                     SIM:show the sim status.
                     OpenVPN: USR indicator showing the OpenVPN status
                     IPsec: USR indicator showing the IPsec status
                     PPTP: USR indicator showing the PPTP status
                     L2TP: USR indicator showing the L2TP status
                     RCMS: show the connect status of RCMS
                     COM1/2: show the connect status of Serial port

                                            Periodic Reboot Settings
Item                 Description                                                                     Default
Periodic Reboot      Set the reboot period of the router. 0 means disable.                           0
Daily Reboot Time    Set the daily reboot time of the router. You should follow the format as HH:    Null
                     MM, in 24h time frame, otherwise the data will be invalid. Leave it empty
                     means disable.
Reboot When No       Click the toggle button to enable/disable this option.                          OFF
Link Is Available

<!-- figure 1 on pdf page 114 at 33,101-559,415 pt | caption: none | text-layer labels: Item Device Name | USR LED Type | Default 460-gateway | OpenVPN | OCR text follows (tesseract, unverified; 11/11 words >= 60, mean confidence 95) -->
Device Name
460-gateway
USR1 LED Type
OpenVPN
USR2 LED Type
OpenVPN
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 114 at 36,473-555,554 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 92) -->
Periodic Reboot Settings
lo
Periodic Reboot
Daily Reboot Time
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 114 at 36,561-555,614 pt | caption: none; nearest centred text below: "Periodic Reboot Settings" | text-layer labels: none | nearby labels: Periodic Reboot Settings | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 88) -->
Emergency Reboot Settings
Reboot When No Link Is Available
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 114 at 33,628-559,760 pt | caption: none | text-layer labels: Periodic Reboot Settings | Item Periodic Reboot Daily Reboot Time | Reboot When No Link Is Available | Default 0 Null | OFF | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 115 | printed page 115 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.6      System

2.6.1 Debug

This section allows you to check and download the syslog details. Click “Service > Syslog > Syslog Settings” to enable
the syslog.

Syslog

Item     Description

Default

<!-- figure 1 on pdf page 115 at 38,254-559,710 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 378/531 words >= 60, mean confidence 74) -->
Netlog
VPNiog
jun
modem tor device
usb/38200000. 0. successfully created
Jun 19 10:45:37 460-zateway [480143]: opening device...
Jun 19 10:45:37 460-gateway [480143]: Read max control message size from descriptors file
4096
Jun 19 10:45:37 [480143]: <info>
check support for device
not supported by any plugin
couldn’t check support for device
Jun 19 10:45:37 <info>
ethernet” not supported by any plugin
Jun 19 10:45:37 <warn> couldn’t query SIM slots: NoDeviceSupport
Jun 19 10:45:39 460-zeteway [D] found no
couldn’t check support for device
Jun 19 10:45:41 460-gateway <info>
not supported by any plugin
Jun 19 10:45:41 [480143]: <info>
[base-manager] couldn’t check support for device
ethernet”: not supported by any plugin
Jun 19 10:45:44 [D] mmv_get_modem: found no modems!
Jun 19 10:45:44 460-zateway USB check status: host
couldn’t check support for device
Jun 19 10:45:46 <info>
not supported by any plugin
Jun 19 10:45:46 460-zateway [480143]: <info>
couldn’t check support for device
ethernet’: not supported by any plugin
Jun 19 10:45:49 460-zateway [480143]: <info>
state changed {unknown locked)
Jun 19 10:45:49 460-zateway [480143]
[modem0] modem couldn’t be initislized: check unlock status: SIM not
<warn>
inserted
Jun 19 10:45:49 [480143]
[modem0] state changed {locked failed)
<info>
Jun 19 10:45:49 460-gateway [D]
found no modems!
Jun 19 10:45:49 [1586]
<info>
manager: new Broadband device
Jun 19 10:45:49 NetworkWanager [1586]
4309]
<info>
device
State change: unmanaged
(reason ‘managed’,
Jun 19 10:45:49 460-zateway [1596]
4320)
modem state failed’
<info>
device
Jun 19 10:45:49 [1586]
4333]
<info>
device
old_state: unmanaged. state:
concheck_now: false
4334)
Jun 19 10:45:49
device
applicable
<warn>
interval is 0
4334]
Jun 19 10:45:49 460-zateway
<info>
device
state: NONE,
old state: dev state: unavailable, success count: 0, continuous failure count: 1
Jun 19 10:45:49 <warn>
device applicable
interval is 0
device concheck_update_state[IPv6], state: NONE.
Jun
19 10:45:49 <info>
43
37]
old
dev state: continuous success count: 0, continuous failure count: 1
4343] failed to retrieve SIM object: No
Jun
19 10:45:49 460-gateway <info>
SIM
object
Get modem path:
10:45:49 modemd[479802]
Jun
19
19
Jun
10:45:49 460-satevay
4
Jun
19
10:45:
50 460-seteway
EG25
Jun
19
10:45
50
Jun
19
50
Jun
19
10:4!
50 460-sateway
modemd[479802]
19
10:4
OK
Jun
50 460-satevar
19
10:45
50 460-setevar
Jun
Jun
19
10:45
50
Jun
i9
10:45
50
“usbnet”, 2
Jun
19
10:45
50
Manual Refresh
<!-- end of figure 1 -->

<!-- pdf page 116 | printed page 116 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Log Level   Select from “Debug”, “Info”, “Notice”, “Warn”, “Error” which from low to high.      Debug
            The lower level will output more syslog in detail.
Filtering   Enter the filtering message based on the keywords. Use “&” to separate more         Null
            than one filter message, such as “keyword1&keyword2”.
Refresh     Select from “Manual Refresh”, “5 Seconds”, “10 Seconds”, “20 Seconds” or “30        Manual
            Seconds”. You can select these intervals to refresh the log information displayed   Refresh
            in the follow box. If selecting “manual refresh”, you should click the refresh
            button to refresh the syslog.

Click the button to clear the syslog.
Click the button to refresh the syslog.

--
--

Item                     Description                                                         Default
System Journal File                                                                          --
                         Click              to generate and click   to download the system

                         journal file.

Item                     Description                                                         Default
System Diagnostic Data                                                                       --
                         Click              to generate and click   to download the system

                         diagnostic data.

<!-- figure 1 on pdf page 116 at 516,65-559,230 pt | caption: none | text-layer labels: none | nearby labels: Debug | -- | -- | Null | Manual Refresh | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 116 at 33,245-559,396 pt | caption: none | text-layer labels: Item System Journal File | Description | Click | to generate and click | to download the system | Default -- | journal file. | nearby labels: Click the button to refresh the syslog. | -- | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 95) -->
Syslog Journal File
System Journal File
System Journal File
Download
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 116 at 33,410-559,561 pt | caption: none | text-layer labels: Item System Diagnostic Data | Description | Click | to generate and click | to download the system | Default -- | diagnostic data. | nearby labels: journal file. | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
System Diagnostic Data
System Diagnostic Data
System Diagnostic Data
Download
<!-- end of figure 3 -->

<!-- pdf page 117 | printed page 117 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Netlog

<!-- figure 1 on pdf page 117 at 41,120-547,657 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 190/208 words >= 60, mean confidence 87) -->
Syslog
Netlog
ver
192.168.0.13
192.168.0.1
UDP
51214
2023-06-19 10:32:16
2023-06-19 10:32:46
192.168.0.13
192.168.0.1
UDP
61033
2023-06-19 10:32:16
2023-06-19 10:32:48
81
192.168.0.13
192.168.0.1
UDP
63234
53
2023-06-19 10:32:16
2023-06-19 10:32:50
192.168.0.13
192.168.0.1
UDP
55044
2023-06-19 10:32:16
2023-06-19 10:32:46
192.168.0.13
UDP
51235
2023-06-19 10:32:16
2023-06-19 10:32:48
192.168.0.13
192.168.0.1
UDP
61180
2023-06-19 10:32:16
2023-06-19 10:32:47
85
192.168.0.13
UDP
49712
2023-06-19 10:32:16
2023-06-19 10:32:47
192.168.0.13
192.168.0.1
UDP
57387
2023-06-19 10:32:16
2023-06-19 10:32:46
87
192.168.0.13
192.168.0.1
UDP
57033
2023-06-19 10:32:16
2023-06-19 10:32:46
192.168.0.13
192.168.0.1
UDP
50445
2023-06-19 10:32:16
2023-06-19 10:32:47
192.168.0.13
192.168.0.1
UDP
49563
2023-06-19 10:32:16
2023-06-19 10:32:49
192.168.0.13
192.168.0.1
UDP
62820
2023-06-19 10:32:16
2023-06-19 10:32:46
192.168.0.13
UDP
54326
2023-06-19 10:32:16
2023-06-19 10:32:48
91
92
192.168.0.13
192.168.0.1
UDP
64357
2023-06-19 10:32:16
2023-06-19 10:32:47
93
192.168.0.13
192.168.0.1
UDP
52804
2023-06-19 10:32:16
2023-06-19 10:32:46
192.168.0.13
192.168.0.1
UDP
2023-06-19 10:32:16
2023-06-19 10:32:47
95
UDP
2023-06-19 10:32:16
192.168.0.13
192.168.0.1
62699
2023-06-19 10:32:47
192.168.0.13
192.168.0.1
UDP
59098
2023-06-19 10:32:16
2023-06-19 10:32:47
97
192.168.0.13
192.168.0.1
UDP
54454
2023-06-19 10:32:16
2023-06-19 10:32:47
98
192.168.0.13
192.168.0.1
UDP
56096
2023-06-19 10:32:16
2023-06-19 10:32:49
192.168.0.13
192.168.0.1
UDP
56216
2023-06-19 10:32:16
2023-06-19 10:32:49
100
192.168.0.13
192.168.0.1
UDP
52434
2023-06-19 10:32:16
2023-06-19 10:32:47
100/page
1/289
Next
Pre
<!-- end of figure 1 -->

<!-- pdf page 118 | printed page 118 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

VPNlog

2.6.2 Certificate Manager

This section allows you to mange all of certificates here. If you want to manage a certificate for your custom
application, you can manage it through Other tab.

<!-- figure 1 on pdf page 118 at 41,122-555,429 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 29/32 words >= 60, mean confidence 88) -->
VPNIog
Syslog
Netlog
Filtering
Jan 25 14:09:48 460-gateway openvpn status is connected
Jan 25 14:10:54 460-gateway openvpn[40121]: openvpn status is
Jan 25 14:11:36 460-gateway openvpn[40083]: openvpn status is connected
<!-- end of figure 1 -->

<!-- pdf page 119 | printed page 119 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

OpenVPN

Item               Description                                                                               Default
Root CA                                                                                                      --
                   Click on               to locate the root ca file, and then click on       to
                   import this file into your device.
Certificate File                                                                                             --
                   Click on               to locate the certificate file, and then click on        to
                   import this file into your device.
Private Key                                                                                                  --
                   Click on               to locate the Private Key file, and then click on        to
                   import this file into your device.
DH
                   Click on               to locate the DH file, and then click on        to import
                   this file into your device.
TLS-Auth Key                                                                                                 --
                   Click on               to locate the TLS-Auth Key file, and then click on            to
                   import this file into your device.
CRL                                                                                                          --
                   Click on               to locate the CRL file, and then click on       to import
                   this file into your device.

<!-- figure 1 on pdf page 119 at 36,146-559,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 42/49 words >= 60, mean confidence 85) -->
[Choose File No file chosen
Root CA
[Choose File No file chosen
Certificate File
t
[Choose File No file chosen
Private Key
[Choose File No file chosen
DH
[Choose File No file chosen
TLS-Auth Key
[Choose File No file chosen
t
CRL
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 119 at 38,317-557,439 pt | caption: none | text-layer labels: none | nearby labels: Description | OCR text follows (tesseract, unverified; 33/34 words >= 60, mean confidence 89) -->
[Choose File No file chosen
TLS-Auth Key
[Choose File No file chosen
CRL
[Choose No file chosen
PKCS#12 Certificate
[Choose File No file chosen
Pre-Share Key
[Choose File No file chosen
Ovpn Config
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 119 at 33,453-141,758 pt | caption: none | text-layer labels: Item Root CA | Certificate File | Private Key | DH | TLS-Auth Key | CRL | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 120 | printed page 120 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

PKCS#12 Certificate                                                                                        --
                      Click on              to locate the PKCS#12 Certificate file, and then click on

                          to import this file into your device.
Pre-Share Key                                                                                              --
                      Click on              to locate the Pre-Share Key file, and then click on
                      to import this file into your device.
Ovpn Config                                                                                                --
                      Click on              to locate the Ovpn Configy file, and then click on
                      to import this file into your device.

IPsec

Item                  Description                                                                          Default
Local Certificate                                                                                          --
                      Click on              to locate the Local Certificate file, and then click on
                      to import this file into your device.
Remote Certificate                                                                                         --
                      Click on              to locate the Remote Certificate file, and then click on

                          to import this file into your device.
Private Key                                                                                                --
                      Click on              to locate the Private Key file, and then click on         to
                      import this file into your device.
CA Certificate                                                                                             --
                      Click on              to locate the CA Certificate file, and then click on
                      to import this file into your device.
PKCS#12 Certificate                                                                                        --
                      Click on              to locate the PKCS#12 Certificate file, and then click on

                          to import this file into your device.

<!-- figure 1 on pdf page 120 at 33,333-559,482 pt | caption: none | text-layer labels: none | nearby labels: Item Local Certificate | Description | Default -- | OCR text follows (tesseract, unverified; 32/41 words >= 60, mean confidence 79) -->
[Choose Fite No file chosen
Local Certificate
File No file chosen
Remote Certificate
File No file chosen
Private Key
w
File No file chosen
CA Certificate
[Choose No file chosen
PKCS#12 Certificate
<!-- end of figure 1 -->

<!-- pdf page 121 | printed page 121 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

SSH

Item                   Description                                                                        Default
Authorized Keys                                                                                           --
                       Click on              to locate the Authorized Keys file, and then click on
                       to import this file into your device.

Web

Item                   Description                                                                        Default
HTTPS Private Key                                                                                         --
                       Click on              to locate the Authorized Keys file, and then click on
                       to import this file into your device.
HTTPS CA Certificate
                       Click on              to locate the Certificate file, and then click on       to
                       import this file into your device.

<!-- figure 1 on pdf page 121 at 33,144-555,197 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
Authorized Keys Settings
Choose File No file chosen
Authorized Keys
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 121 at 33,206-559,336 pt | caption: none | text-layer labels: Item Authorized Keys | Description | Click on | Default -- | to import this file into your device. | nearby labels: Web | OCR text follows (tesseract, unverified; 10/13 words >= 60, mean confidence 84) -->
Authorized Keys
Index
File Name
File Size
Modification Time
File
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 121 at 38,425-555,501 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 19/20 words >= 60, mean confidence 94) -->
HTTPS Certificate Settings
HTTPS Private Key
Choose File No file chosen
HTTPS CA Certificate
Choose File No file chosen
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 121 at 38,508-555,568 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 97) -->
HTTPS Private Key
Index
File Name
File Size
Modification Time
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 121 at 38,578-555,636 pt | caption: none | text-layer labels: none | nearby labels: Item HTTPS Private Key | Description | Default -- | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 97) -->
HTTPS CA Certificate
Index
File Name
File Size
Modification Time
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 121 at 33,640-141,756 pt | caption: none | text-layer labels: Item HTTPS Private Key | HTTPS CA Certificate | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 121 at 189,640-559,756 pt | caption: none | text-layer labels: Default -- | to | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 76) -->
Choose File
Choose File
<!-- end of figure 7 -->

<!-- pdf page 122 | printed page 122 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

System Certificate

 Item                    Description                                                                      Default
 File                                                                                                     --
                         Click on             to locate the System certificate file, and then click on

                             to import this file into your device.

Other

 Item                    Description                                                                      Default
 Other Certificate                                                                                        --
                         Click on             to locate the Other Certificate file, and then click on

                             to import this file into your device.

2.6.3 Resource Graph

This section allows you to view the system resource such as CPU usage or cellular signal strength in recent 3 minutes,
last hour or last day.

<!-- figure 1 on pdf page 122 at 33,144-559,288 pt | caption: none | text-layer labels: Item File | Description | Click on | Default -- | to import this file into your device. | OCR text follows (tesseract, unverified; 10/12 words >= 60, mean confidence 83) -->
Certificate Import
f Choose File No file chosen
File
File
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 122 at 36,396-557,449 pt | caption: none | text-layer labels: none | nearby labels: Description | OCR text follows (tesseract, unverified; 10/11 words >= 60, mean confidence 87) -->
Other Certificate Settings
[Choose File No file chosen
Other Certificate
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 122 at 33,468-559,552 pt | caption: none | text-layer labels: Item Other Certificate | Description | Click on | Default -- | to import this file into your device. | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 75) -->
Choose
<!-- end of figure 3 -->

<!-- pdf page 123 | printed page 123 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

CPU Usage

<!-- figure 1 on pdf page 123 at 45,182-406,324 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/14 words >= 60, mean confidence 60) -->
IN
25
20
1S
N
v
10
W
y=
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 123 at 45,393-406,530 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 60) -->
25
20
15
10
<!-- end of figure 2 -->

<!-- pdf page 124 | printed page 124 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

RAM Usage

<!-- pdf page 125 | printed page 125 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

SIM Traffic

<!-- pdf page 126 | printed page 126 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

SIM Signal

<!-- figure 1 on pdf page 126 at 38,134-406,247 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/15 words >= 60, mean confidence 76) -->
Last 3 minutes SIM Signal
+139.0
139.2
139.4
139.6
39.8
140.0
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 126 at 38,341-406,453 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/10 words >= 60, mean confidence 72) -->
139.0
139.2
139.4
139.6
139.8
140.0
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 126 at 38,549-406,660 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/14 words >= 60, mean confidence 80) -->
Last Day SIM Signal
(55
139.0
139.2
139.4
139.6
139.8
40.0
<!-- end of figure 3 -->

<!-- pdf page 127 | printed page 127 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.6.4 App Center

This section allows you to add some required or customized applications to the router. Import and install your
applications to the App Center, and reboot the device according to the system prompts. Each installed application will
be displayed under the “Services” menu, while other applications related to VPN will be displayed under the “VPN”
menu.
Note: After importing the applications to the router, the page display may have a slight delay due to the browser
cache. It is recommended that you clear the browser cache first and log in the router again.

 Item                Description                                                                               Default
 File                Click on “Choose File” to locate the App file from your PC, and then click                --

                               to import this file into your device.

The successfully installed app will be displayed in the following list. Click   to uninstall the app.

 Item                Description                                                                               Default
 Index               Indicate the ordinal of the list.                                                         --
 Name                Show the name of the App.                                                                 Null
 Version             Show the version of the App.                                                              Null
 Status              Show the status of the App.                                                               Null
 Description         Show the description for this App.                                                        Null

2.6.5 Tools

This section provides users three tools: Ping, Traceroute and Sniffer. The Ping is used to check the network
connectivity.

<!-- figure 1 on pdf page 127 at 33,254-559,381 pt | caption: none | text-layer labels: Item File | Default -- | to import this file into your device. | nearby labels: to uninstall the app. | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 88) -->
App Install
Choose File No file chosen
File
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 127 at 33,393-559,619 pt | caption: none | text-layer labels: to uninstall the app. | Default -- Null Null Null Null | nearby labels: to import this file into your device. | 2.6.5 Tools | OCR text follows (tesseract, unverified; 22/22 words >= 60, mean confidence 95) -->
Index
Version
Status
Description
Name
linux-image-5.4.24-2.0.0
Running
Linux kernel, version 5.4.24-2.0.0
x
1
2.0.0
x
ros pro core deb
2.0.0-1
Running
rosp-core
<!-- end of figure 2 -->

<!-- pdf page 128 | printed page 128 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Ping

Item                 Description                                                                     Default
IP address           Enter the ping’s destination IP address or destination domain.                  Null
Number of Requests   Specify the number of ping requests.                                            5
Timeout              Specify the timeout of ping requests.                                           1
Local IP             Specify the local IP from cellular WAN, Ethernet WAN or Ethernet LAN. Null      Null
                     stands for selecting local IP address from these three automatically.
                     Click this button to start ping request, and the log will be displayed in the   --
                     follow box.
                     Click this button to stop ping request.                                         --

Traceroute

<!-- figure 1 on pdf page 128 at 33,113-533,441 pt | caption: none | text-layer labels: none | nearby labels: Ping | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 85) -->
Sniffer
Ping
Traceroute
IP Address
Number of Request
E
Timeout
Interface
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 128 at 33,453-559,619 pt | caption: none | text-layer labels: Default Null 5 1 Null | -- | -- | nearby labels: Traceroute | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 129 | printed page 129 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Item            Description                                                                      Default
Trace Address   Enter the trace’s destination IP address or destination domain.                  Null
Trace Hops      Specify the max trace hops. Router will stop tracing if the trace hops has met   30
                max value no matter the destination has been reached or not.
Trace Timeout   Specify the timeout of Traceroute request.                                       1
Interface       Select the trace interface.                                                      --
                Click this button to start ping request, and the log will be displayed in the    --
                follow box.
                Click this button to stop ping request.                                          --

<!-- figure 1 on pdf page 129 at 33,67-528,393 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/11 words >= 60, mean confidence 94) -->
Sniffer
Traceroute
Ping
Trace Address
E
Trace Hops
Trace Timeout
Interface
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 129 at 33,408-559,573 pt | caption: none | text-layer labels: Item Trace Address Trace Hops | Trace Timeout Interface | Default Null 30 | 1 -- -- | -- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 130 | printed page 130 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Sniffer

Item              Description                                                                           Default
Interface         Choose the interface according to your Ethernet configuration.                        All
Host              Filter the packet that contain the specify IP address.                                Null
Packets Request   Set the packet number that the router can sniffer at a time.                          1000
Protocol          Select from “All”, “IP”, “TCP”, “UDP” and “ARP”.                                      All
Status            Show the current status of sniffer.                                                   --
                  Click this button to start the sniffer.                                               --
                  Click this button to stop the sniffer. Once you click this button, a new log file     --
                  will be displayed in the following List.

Item              Description                                                                           Default
Capture Files     Every times of sniffer log will be saved automatically as a new file. You can find    --

                  the file from this Sniffer Traffic Data List and click   to download the log, click

                     to delete the log file. It can cache a maximum of 5 files.

<!-- figure 1 on pdf page 130 at 33,149-557,321 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/9 words >= 60, mean confidence 90) -->
[au
Interface
Host
Packets Request
1000
[ai
Protocol
Status
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 130 at 33,329-141,480 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 130 at 433,329-559,480 pt | caption: none | text-layer labels: Default All Null 1000 All -- | -- -- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 130 at 33,497-557,580 pt | caption: none; nearest centred text below: "Description Every times of sniffer log will be saved automatically as a new file. You can find" | text-layer labels: none | OCR text follows (tesseract, unverified; 17/17 words >= 60, mean confidence 95) -->
Capture Files
Index
File Name
File Size
Modification Time
1
22-05-09_13-45-11.cap
114101
Mon May 9 13:45:30 2022
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 130 at 33,600-155,684 pt | caption: none | text-layer labels: Item Capture Files | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 6 on pdf page 130 at 414,600-559,684 pt | caption: none | text-layer labels: Default -- | nearby labels: to download the log, click | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 131 | printed page 131 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

2.6.6 Flash Manager

This section allows you to manage the device’s flash memory life, you can easily check the flash status or thoughput
and start a period test on this section .

Status

This page shows the flash status and data throughput details.

<!-- figure 1 on pdf page 131 at 33,254-559,580 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 55/55 words >= 60, mean confidence 96) -->
Estimated Remaining Device Lifetime
90% 100%
Flash Total Erase Amount
303756.75 MB
Total Blocks Erased
12273
Block Size
24.75 MB
Total Number of Blocks
3000
Flash Avg Erase Count
18
Flash Avg Erase Rate
<1%
Flash Bad Block Count
Increase Bad Block Count
Power On Count
359 Times
Reserved Block Consumption
Normal
Capacity
14930 MB
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 131 at 33,590-559,696 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 17/17 words >= 60, mean confidence 95) -->
Item
Today
Yesterday
Last 7 Days
Total
Data Read(MB)
0
0
39040
Data Write(MB)
128
128
76928
<!-- end of figure 2 -->

<!-- pdf page 132 | printed page 132 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Flash Memory Tests

                                        Flash Memory Tests @ Flash Manager
  Item                    Description
  Test Mode               Manual: When choosing 'manual', click 'start' to run a test, you can click ‘stop’ to end the
                          test;
                          Scheduled: Input the 'start' and 'end' time for a scheduled test.
                          You can click 'stop' button under whatever mode.
  Start Time              Enter start time, format: yyyy/mm/dd, hh/mm/ss. E.g. 2023/04/24, 12:00:00
  End Time                Enter end time, format: yyyy/mm/dd, hh/mm/ss. E.g. 2023/04/24, 18:00:00

  You can click        to download the test log for viewing more information.

2.6.7 Service Management

This section allows you to modify the network services manage way.

                   View Status on RobustOS         Configure via
  Mode                                                                  Configure via Linux Shell
                   Pro                             RobustOS Pro

  Managed By
                   √                               √                    X
  RobustOS Pro

<!-- figure 1 on pdf page 132 at 36,144-559,417 pt | caption: none | text-layer labels: Flash Memory Tests @ Flash Manager | Item Test Mode | Start Time End Time | nearby labels: You can click | OCR text follows (tesseract, unverified; 7/12 words >= 60, mean confidence 71) -->
Test Mode
scheduled
Start Time
End Time
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 132 at 38,535-555,691 pt | caption: none; nearest centred text below: "Configure via RobustOS Pro" | text-layer labels: none | nearby labels: Mode | Configure via Linux Shell | OCR text follows (tesseract, unverified; 26/27 words >= 60, mean confidence 91) -->
[Managed by RobustOS Pro
WAN
[Managed by RobustOS Pro
LAN
[Managed by RobustOS Pro
Firewall
[Managed by RobustOS Pro
Route
Policy Route
Managed by RobustOS Pro
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 132 at 41,700-552,784 pt | caption: none | text-layer labels: Mode | View Status on RobustOS Pro | Configure via RobustOS Pro | Configure via Linux Shell | Managed By RobustOS Pro | √ | √ | X | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 133 | printed page 133 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

  Managed By
                    X                               X                    √
  Third-Party

2.6.8 Profile

This section allows you to import or export the configuration file, or rollback the device to a previous configuration.

Profile

 Item                           Description                                                                  Default
 Reset Other Settings to        Click the toggle button as “ON” to return other parameters to default        OFF
 Default                        settings.
 Ignore Invalid Settings        Click the toggle button as “ON” to ignore invalid settings.                  OFF
 XML Configuration File         Click on           to locate the XML configuration file from your PC, and    --

                                then click        to import this file into your device.

 Item                           Description                                                                  Default
 Ignore Disabled Features       Click the toggle button as “OFF” to ignore the disabled features.            OFF
 Add Detailed Information       Click the toggle button as “On” to add detailed information.                 OFF
 Encrypt Secret Data            Click the toggle button as “ON” to encrypt the secret data.                  ON
 XML Configuration File         Click          button to generate the XML configuration file, and            --

                                click         to export the XML configuration file.

<!-- figure 1 on pdf page 133 at 41,65-552,118 pt | caption: none | text-layer labels: Managed By Third-Party | X | X | √ | nearby labels: 2.6.8 Profile | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 133 at 33,278-555,501 pt | caption: none | text-layer labels: then click | OFF -- | to import this file into your device. | Default OFF | OCR text follows (tesseract, unverified; 21/23 words >= 60, mean confidence 85) -->
Eo
Reset Other Settings to Default
Eo
Ignore Invalid Settings
[impor
f Choose File No file chosen
XML Configuration File
File
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 133 at 33,520-559,770 pt | caption: none | text-layer labels: click | Default OFF OFF ON -- | to export the XML configuration file. | OCR text follows (tesseract, unverified; 13/17 words >= 60, mean confidence 79) -->
Ignore Disabled Features
Add Detailed Information
XML Configuration File
Export
XML Configuration File
<!-- end of figure 3 -->

<!-- pdf page 134 | printed page 134 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Item                       Description                                                                      Default
 Save Running Configuration                                                                                  --
 as Default                 Click         button to save the current running parameters as default
                            configuration.
 Restore to Default                                                                                          --
 Configuration              Click            button to restore the defaults configuration.
 Restore to Factory Default                                                                                  --
 Configuration              Click            button to restore the factory defaults configuration.
                            Note: The linux file system will be restored to the initialization state.

Rollback

 Item                     Description                                                                   Default
 Save as a Rollbackable   Create a save point manually. Additionally, the system will create a save     --
 Archive                  point every day automatically if configuration changes.
 Configuration Archive    View the related information about configuration archive files, including     --
 Files                    name, size and modification time.

2.6.9      User Management

This section allows you to change your username and password, and create or manage user accounts. One device has
only one super user who has the highest authority to modify, add and manage other common users.
The password need to be meet the requirement: 8-32 characters, must consist of at least three types of lowercase,
uppercase, digit, and special characters.
Special characters allowed: @, #, $, ., *, !, -

<!-- figure 1 on pdf page 134 at 33,70-559,321 pt | caption: none | text-layer labels: Default -- | -- | -- | nearby labels: Rollback | OCR text follows (tesseract, unverified; 16/20 words >= 60, mean confidence 81) -->
save
Save Running Configuration as Default
Restore to Default Configuration
Restore To Factory Default Configuration
Restore
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 134 at 36,410-555,463 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Configuration Rollback
Save as a Rollbackable Archive
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 134 at 36,470-555,530 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
Configuration Archive Files
Index
File Name
File Size
Modification Time
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 134 at 481,549-559,633 pt | caption: none | text-layer labels: Default -- | -- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 135 | printed page 135 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Item               Description                                                                    Default
New Username       Enter a new username you want to create; valid characters are a-z, A-Z, 0-9,   Null
                   @,., -, #, $, and *.
Old Password       Enter the old password of your router. The default password please see the     Null
                   product label.
New Password       Enter a new password you want to create; valid characters are a-z, A-Z, 0-9,   Null
                   @,., -, #, $, and *.
Confirm Password   Enter the new password again to confirm.                                       Null

Item               Description                                                                    Default
New Username       Enter a new username you want to create; valid characters are a-z, A-Z, 0-9,   Null
                   @,., -, #, $, and *.
Old Password       Enter the old password of your router. The default password please see the     Null
                   product label.
New Password       Enter a new password you want to create; valid characters are a-z, A-Z, 0-9,   Null
                   @,., -, #, $, and *.
Confirm Password   Enter the new password again to confirm.                                       Null

<!-- figure 1 on pdf page 135 at 36,115-552,249 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 97) -->
New Username
Old Password
New Password
Confirm Password
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 135 at 33,449-557,583 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
New Username
Old Password
New Password
Confirm Password
<!-- end of figure 2 -->

<!-- pdf page 136 | printed page 136 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Click    button to add a new common user. The maximum rule count is 5.

 Item            Description                                                                             Default
 Index           Indicate the ordinal of the list.                                                       --
 Role            Select from “Guest” and “User”.                                                         Guest
                  Guest: Guest only can view the configuration of router under this level
                  User: User can view and set the configuration of router under this level
 Username        Set the Username; valid characters are a-z, A-Z, 0-9, @, ., -, #, $, and *.             Null
 Password        Set the password which at least contains 5 characters; valid characters are a-z, A-Z,   Null
                 0-9, @, ., -, #, $, and *.

2.6.10          DEB Management

This section allows you to manage your own Debian packages.

 Item                Description                                                                         Default

<!-- figure 1 on pdf page 136 at 43,106-552,163 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 95) -->
Common User Settings
Userld
Role
Username
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 136 at 33,209-557,345 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 8/10 words >= 60, mean confidence 83) -->
Common Users Settings
Ke)
Userld
Role
Username
Password
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 136 at 33,362-105,494 pt | caption: none | text-layer labels: Item Index Role | Username Password | nearby labels: 2.6.10 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 136 at 488,362-559,494 pt | caption: none | text-layer labels: Default -- Guest | Null Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 136 at 38,597-557,732 pt | caption: none | text-layer labels: none | nearby labels: Item | Description | Default | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
[update
Apt Action
Package Name
Extra Parameters
<!-- end of figure 5 -->

<!-- pdf page 137 | printed page 137 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

 Apt Action             Select from “update”, “install”, “clean”, “remove”, “show”.                         --
                         update: to update the apt.
                         Install: to install the apt.
                         Remove: to remove the apt.
                         Clean: to clean the apt.
                         Show: to show the apt list.
 Package Name           Enter the package name to implement.                                                --
 Extra Parameters       More parameters of 'apt' command, such as '--purge', etc.                           Null

2.6.11          Role Management

This section is used to manage user roles and manage permissions for users in different roles.

                                               Role Names @ Role Management
  Item                   Description                                                                      Default
  Guest                  Enter a visitor name; valid characters are a-z, A-Z, 0-9, @,., -, #, $, and *.   Guest
  User                   Enter a editor name; valid characters are a-z, A-Z, 0-9, @,., -, #, $, and *.    User

Click     to edit Visitor/Editor permission.

<!-- figure 1 on pdf page 137 at 404,65-507,197 pt | caption: none | text-layer labels: none | nearby labels: -- | -- Null | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 137 at 36,314-555,420 pt | caption: none; nearest centred text below: "Role Names @ Role Management" | text-layer labels: none | nearby labels: Role Names @ Role Management | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 84) -->
Settings
Index
Role
Guest
1
2
User
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 137 at 38,437-218,506 pt | caption: none | text-layer labels: Item Guest User | nearby labels: Click | to edit Visitor/Editor permission. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 137 at 378,437-552,506 pt | caption: none | text-layer labels: Default Guest User | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 138 | printed page 138 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->



<!-- figure 1 on pdf page 138 at 36,74-555,180 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/10 words >= 60, mean confidence 80) -->
Index
Role
Guest
Vv
[Readonly
J
save and apply,reboot..
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 138 at 36,187-555,367 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/14 words >= 60, mean confidence 86) -->
[Readonly
Firewall
[Readonly
WAN
[Readonly
Route
[Readonly
QoS
[Readonly
Policy Route
[Readonly
LAN
<!-- end of figure 2 -->

<!-- pdf page 139 | printed page 139 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->



<!-- figure 1 on pdf page 139 at 36,74-459,283 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 23/26 words >= 60, mean confidence 82) -->
[Readonly
Service Management
[Readonly
Flash Manager
[Readonly
DEB Management
[Readonly
Profile
[Readonly
Tools
[Readonly
App Center
Certificate Manager
Debug
ReadOnly
[Readonly
User Management
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 139 at 36,293-459,477 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/18 words >= 60, mean confidence 84) -->
[Readonly
WiFi
[Readonly
VLAN
USB
[Readonly
Serial Port
[Readonly
Ethernet
[Readonly
DIDO
[Readonly
Cellular
[Readonly
Bridge
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 139 at 36,492-459,638 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/13 words >= 60, mean confidence 73) -->
[Readonly
DMVPN
[Readonly
PPTP
[Readonly
OpenVPN
[Readonly
IPsec
[Readonly
GRE
<!-- end of figure 3 -->

<!-- pdf page 140 | printed page 140 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

                                     User Permission @ Role Management
 Item                    Description
 None                    User have no permission to access or modify this setting.
 ReadOnly                User only have permission to read.
 Read/Write              User have permission to access or modify this setting.

Note:
    1.   When logging in with Guest/User, “Profile” is not available.
    2.   When Guest “Save and apply, reboot” permission was set to “ReadOnly”. After logging as Guest, “save and
         apply”, “reboot” buttons will not be displayed.

<!-- figure 1 on pdf page 140 at 36,72-459,389 pt | caption: none; nearest centred text below: "User Permission @ Role Management" | text-layer labels: none | nearby labels: User Permission @ Role Management | OCR text follows (tesseract, unverified; 28/32 words >= 60, mean confidence 82) -->
[Readonly
Captive Portal
[Readonly
Web Server
VRRP
[Readonly
Syslog
SSH
[Readonly
SNMP
[Readonly
SMS
[Readonly
Advanced
[Readonly
RCMS
[Readonly
NTP
[Readonly
GPS
[Readonly
Event
[Readonly
Email
[Readonly
DDNS
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 140 at 36,393-201,477 pt | caption: none | text-layer labels: Item None ReadOnly Read/Write | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 140 at 383,393-547,477 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 141 | printed page 141 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Chapter 3 Configuration Examples

3.1      Cellular

3.1.1 Cellular APN Manual Setting and Cellular Dial-up.

This section shows you how to configure the APN for Cellular Dial-up. Connect the device correctly and insert the SIM
card, then open the web configuration page. Under the homepage menu, click “Interface > Cellular > Cellular ” to go
to the cellular configuration page.

Click     to set its parameters according to the current ISP.

<!-- figure 1 on pdf page 141 at 38,353-557,432 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 79) -->
General Settings
Primary Sim
Enable Auto Switching
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 141 at 38,439-557,518 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 86) -->
Additional Switching Rules
Eo
Weak Signal
While Roaming
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 141 at 41,540-557,645 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 19/20 words >= 60, mean confidence 92) -->
Index
SIM Card
Phone Number
Network Type
Band Select Type
4%
All
SIM1
Auto
1
All
2
SIM2
Auto
<!-- end of figure 3 -->

<!-- pdf page 142 | printed page 142 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Then Click “Network> WAN> Link” go to the WAN configuration page.

Click    to add one link for cellular dial-up, select “Modem” as the link type, then click   to submit.

<!-- figure 1 on pdf page 142 at 33,67-559,389 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 24/26 words >= 60, mean confidence 89) -->
[1
Index
SIM Card
Automatic APN Selection
APN
internet
Username
Password
[None
Authentication Type
Phone Number
PIN Code
Extra AT Cmd
lo
Telnet Port
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 142 at 41,499-555,580 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/12 words >= 60, mean confidence 96) -->
Settings
Name
Type
Description
Weight
Firewall Zone
Wireless
WIFI
default wan
external
<!-- end of figure 2 -->

<!-- pdf page 143 | printed page 143 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

After save and apply, the new cellular WAN link will take effect.

3.1.2 SMS Remote Control

MG460 supports remote control via SMS. You can use following commands to get the status of the router, and set all
the parameters of the router.

SMS command have the following structures:
1. Password mode—Username: Password;cmd1;cmd2;cmd3; …cmdn (available for every phone number).
2. Phonenum mode-- Password; cmd1; cmd2; cmd3; … cmdn (available when the SMS was sent from the phone
   number which had been added in router’s phone group).
3. Both mode-- Username: Password;cmd1;cmd2;cmd3; …cmdn (available when the SMS was sent from the phone
   number which had been added in router’s phone group).
4. Note: All command symbols must be entered in the half-angle mode of the English input method.

SMS command Explanation:
1. Username and Password: Use the same username and password as WEB manager for authentication.
2. cmd1, cmd2, cmd3 to cmdn, the command format is the same as the CLI command, more details about CLI cmd

<!-- figure 1 on pdf page 143 at 36,70-552,254 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/14 words >= 60, mean confidence 88) -->
Name
[Modem
Type
Interface
wwan
Description
Backup WAN
lo
Weight
[external
Firewall Zone
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 143 at 36,261-557,345 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/9 words >= 60, mean confidence 60) -->
Health Detection Settings
Enable
IDwA
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 143 at 38,396-557,501 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/16 words >= 60, mean confidence 96) -->
Name
Type
Description
Weight
Firewall Zone
Wireless
WIFI
default wan
external
Cellular
Modem
Backup WAN
external
<!-- end of figure 3 -->

<!-- pdf page 144 | printed page 144 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

please refer to 4.1 What Is CLI.
Note: Download the configure XML file from the configured web browser. The format of SMS control command

      can refer to the data of the XML file.

Go to “System > Profile > Export Configuration File”, click

export the XML file.

XML command:
<lan>
<network max_entry_num="5">
<id>1</id>
<interface>lan0</interface>
<ip>172.16.24.24</ip>
<netmask>255.255.0.0</netmask>

to generate the XML file and click   to

     <mtu>1500</mtu>
     SMS cmd:
     set lan network 1 interface lan0
     set lan network 1 ip 172.16.24.24
     set lan network 1 netmask 255.255.0.0
     set lan network 1 mtu 1500
3.   The semicolon character (‘;’) is used to separate more than one commands packed in a single SMS.
4.   E.g.
     admin:admin;status system
     In this command, username is “admin”, password is “admin”, control command is “status system”, and the
     function of the command is to get the system status.
     SMS received:

<!-- figure 1 on pdf page 144 at 33,211-559,336 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/22 words >= 60, mean confidence 89) -->
J
Profile
Rollback
Reset Other Settings to Default
To
Ignore Invalid Settings
XML Configuration File
Choose File No file chosen
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 144 at 41,345-559,470 pt | caption: none | text-layer labels: none | nearby labels: XML command: | OCR text follows (tesseract, unverified; 12/14 words >= 60, mean confidence 84) -->
Ignore Disabled Features
Add Detailed Information
XML Configuration File
XML Configuration File
<!-- end of figure 2 -->

<!-- pdf page 145 | printed page 145 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

firmware_version = 2.0.0
firmware_version_full = "2.0.0 (60b55c0)"
kernel_version = 5.4.24-2.0.0
hardware_version = 0.0
operation_system = "Debian GNU/Linux 11.3"
device_model = ""
serial_number = 2204190667030003
temperature_interval = 53.0
uptime = "0 days, 00:12:06"
system_time = "Thu May 19 16:52:22 2022"
ram_usage = 392M/448M
cpu_usage = "22569s Idle/71405s Total /1 cpus"
disk_usage = 1.9G/7.1G
admin:admin;reboot
In this command, username is “admin”, password is “admin”, and the command is to reboot the Router.
SMS received:
OK

admin:admin;set firewall remote_ssh_access false;set firewall remote_telnet_access false
In this command, username is “admin”, password is “admin”, and the command is to disable the remote_ssh
and remote_telnet access.
SMS received:
OK
OK

admin:admin;set lan network 1 interface lan0;set lan network 1 ip 172.16.24.24;set lan network 1 netmask
255.255.0.0;set lan network 1 mtu 1500
In this command, username is “admin”, password is “admin”, and the commands is to configure the LAN
parameter.
SMS received:
OK
OK
OK
OK

<!-- pdf page 146 | printed page 146 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

3.2         VPN Configuration Examples

3.2.1 IPsec VPN

IPsec VPN topology (server-side and client-side IKE and SA parameters must be configured the same).
   PC1                                                                                         PC3
                            IpsecVPN-Server                IpsecVPN-Client
                     LAN                                                       LAN

                                                    Internet

                                 WAN:58.1.1.1

                   10.0.0.0/24                                          192.168.1.0/24

      PC2                                                                                       PC4

<!-- figure 1 on pdf page 146 at 328,185-512,326 pt | caption: none | text-layer labels: LAN | 192.168.1.0/24 | nearby labels: IpsecVPN-Client | PC4 | OCR: no legible text (0/1 words >= 60, mean confidence 48) -->
<!-- figure 2 on pdf page 146 at 36,197-320,326 pt | caption: none | text-layer labels: LAN | Internet | WAN:58.1.1.1 | 10.0.0.0/24 | nearby labels: IpsecVPN-Server | PC2 | OCR: no legible text (0/1 words >= 60, mean confidence 35) -->

<!-- pdf page 147 | printed page 147 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

IPsecVPN_Server:

Cisco 2811:

<!-- figure 1 on pdf page 147 at 38,137-344,362 pt | caption: none | text-layer labels: none | nearby labels: Cisco 2811: | OCR text follows (tesseract, unverified; 112/124 words >= 60, mean confidence 86) -->
Router>eneble
Configuring from terminal, memory,
or network [terminal]?
End with
Enter configuration commands,
one per line.
isakmp policy 10
Router (config-isakmp)
authentication Set authentication method for protection suite
Set encryption algorithm for protection suite
encryption
exit
Exit from ISAKMP protection suite configuration mode
Set the Diffie-Hellman group
group
hash
Set hash algorithm for protection suite
lifetime
Set lifetime for ISAKMP security association
Negate command or set its defaults
no
Router (config-isakmp) 3des
¢hesh md5
Router (config-isakmp) pre-share
Router 2
Router (config-isakmp)
isakmp
client
Set client configuration policy
enable
Enable ISAKMP
Set pre-shared key for remote peer
key
policy Set policy for an ISAKMP protection suite
Router(config)#crypto isakmp key cisco address 0.0.0.0 0.0.0.0
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 147 at 38,377-339,547 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 84/95 words >= 60, mean confidence 84) -->
Router (config)
dynamic-map Specify a dynamic crypto map template
ipsec
Configure IPSEC policy
isakmp
Configure ISAKMP policy
Long term key operations
key
Enter a crypto map
map
Router (config)#crypto ipsec
security-association Security association parameters
transform-set
Define transform and settings
ipsec transform-set Trans
ah-mdS-hmac
AH-HMAC-MDS transform
AH-HMAC-SHA transform
ah-sha-hmac
esp-3des
ESP
transform
using 3DES(EDE)
cipher (168 bits)
ESP
transform
using AES cipher
using DES cipher (56 bits)
esp-des
ESP
transform
ESP
transform
using HMAC-MDS auth
ESP
transform
esp-sha-hmac
using HMAC-SHA auth
ipsec transform-set Trans esp-3des
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 147 at 36,604-270,669 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 33/38 words >= 60, mean confidence 81) -->
Router (config)#crypto map cry-map 10 ipsec-isakmp
NOTE: This new crypto map will remain disabled until
and 4 valid access list have been configured.
Router address vpn
Router transform-set Trans
Router peer
Router (config-crypto-map)
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 147 at 36,693-268,741 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/22 words >= 60, mean confidence 63) -->
fastEthernet 0/0
address 58.1.1.1 255.255.255.0
Router (config-if)¢cr
map cry-map
*Jan 3 07:16:26.785: %CRYPTO-6-ISAKMP
ISAKMP
<!-- end of figure 4 -->

<!-- pdf page 148 | printed page 148 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

IPsec VPN_Client:
The window is displayed as below by clicking “VPN > IPsec > Tunnel.”

Click   button and set the parameters of IPsec Client as below.

<!-- figure 1 on pdf page 148 at 41,192-555,252 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 97) -->
Tunnel Settings
Index
Enable
Local Subnet
Remote Subnet
Description
Gateway
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 148 at 33,271-557,626 pt | caption: none | text-layer labels: Click | OCR text follows (tesseract, unverified; 26/32 words >= 60, mean confidence 78) -->
[1
Index
Enable
Description
[wiano
Link Binding
Gateway
[Ese
Protocol
[Tunnel
Mode
Local Subnet
192.168.1.0/24
[0.0.0.0/24
Remote Subnet
IKE Type
[main
Negotiation Mode
Initiation Mode
On
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 148 at 36,631-557,765 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/10 words >= 60, mean confidence 84) -->
Enable Compression
Enable Forceencaps
Backup Gateway
Expert Options
<!-- end of figure 3 -->

<!-- pdf page 149 | printed page 149 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

When finished, click   to submit and click

for the configuration to take effect.

<!-- figure 1 on pdf page 149 at 33,74-557,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/27 words >= 60, mean confidence 79) -->
Encryption Algorithm
Authentication Algorithm
IKE DH Group
[Psk
Authentication Type
PSK Secret
Local ID Type
Remote ID Type
IKE Lifetime
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 149 at 36,324-557,561 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 19/19 words >= 60, mean confidence 94) -->
Encryption Algorithm
3DES
v
Authentication Algorithm
SHA1
PFS Group
PFS(N/A)
SA Lifetime
28800
DPD Interval
30
DPD Failures
150
<!-- end of figure 2 -->

<!-- pdf page 150 | printed page 150 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

3.2.2 OpenVPN

OpenVPN supports two modes, including Client and P2P. Here takes Client as an example.
                      P                                                                      PC3
                      C     OpenVPN-Server               OpenVPN-Client
                      1
                    LAN
                                                                               LAN

                                                  Internet

                            WAN:202.96.1.100/24
                                                             WAN:59.1.1.1
                                                                            192.168.1.0/24
                 192.168.2.0/24

                        P                                                                     PC4
                        C
                        2

OpenVPN_Server:
Generate relevant OpenVPN certificate on the server side firstly, and refer to the following commands to
configuration the Server:
local 202.96.1.100
mode server
port 1194
proto udp
dev tun
tun-mtu 1500
fragment 1500
ca ca.crt
cert Server01.crt
key Server01.key
dh dh1024.pem
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
push "route 192.168.3.0 255.255.255.0"
client-config-dir ccd
route 192.168.1.0 255.255.255.0
keepalive 10 120
cipher BF-CBC
comp-lzo
max-clients 100
persist-key
persist-tun
status openvpn-status.log
verb 3
Note: For more configuration details, please contact your technical support engineer.

<!-- figure 1 on pdf page 150 at 36,139-172,276 pt | caption: none | text-layer labels: none | nearby labels: 192.168.2.0/24 | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 65) -->
Ly,
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 150 at 339,144-481,278 pt | caption: none | text-layer labels: LAN | 192.168.1.0/24 | nearby labels: PC3 | PC4 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 150 at 237,185-301,235 pt | caption: none | text-layer labels: Internet | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 151 | printed page 151 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

OpenVPN_Client:
Click “VPN > OpenVPN > OpenVPN” as below.

Click   to configure the Client01 as below.

<!-- figure 1 on pdf page 151 at 43,189-557,252 pt | caption: none | text-layer labels: none | nearby labels: Click | to configure the Client01 as below. | OCR text follows (tesseract, unverified; 8/8 words >= 60, mean confidence 96) -->
Tunnel Settings
Enable
Description
Index
Mode
Peer Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 151 at 36,290-557,547 pt | caption: none | text-layer labels: none | nearby labels: Click | to configure the Client01 as below. | OCR text follows (tesseract, unverified; 21/23 words >= 60, mean confidence 87) -->
General Settings
Index
Enable
Description
[ctient
Mode
[uoe
Protocol
Peer Address
202.96.1.100
[1194
Peer Port
[run
Interface Type
[xso9ca
Authentication Type
<!-- end of figure 2 -->

<!-- pdf page 152 | printed page 152 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

When finished, click   to submit and click

for the configuration to take effect.

<!-- figure 1 on pdf page 152 at 36,72-557,463 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 43/50 words >= 60, mean confidence 84) -->
[None
Root CA
[None
Certificate File
[None
Private Key
Private Key Password
[pe
Encrypt Algorithm
Authentication Algorithm
Renegotiation Interval
86400
[20
Keepalive Interval
[120
Keepalive Timeout
TUN MTU
1500
Max Frame Size
1400
Enable Compression
Enable NAT
Enable DNS overrid
[3
Verbose Level
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 152 at 36,473-555,597 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 85) -->
Enable HMAC Firewall
Enable PKCS#12
Enable nsCertType
Expert Options
<!-- end of figure 2 -->

<!-- pdf page 153 | printed page 153 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

3.2.3 GRE VPN

GRE VPN topology
   PC1                                                                       PC3
                                      GRE-1                    GRE-2

                     LAN                                               LAN

                                                    Internet

                                    WAN:58.1.1

                   192.168.2.0/24

   PC2                                                                       PC4

GRE-1：
The window is displayed as below by clicking “VPN > GRE > GRE”.

Click    button and set the parameters of GRE-1 as below.

<!-- figure 1 on pdf page 153 at 363,139-516,281 pt | caption: none | text-layer labels: LAN | nearby labels: PC3 | GRE-2 | PC4 | OCR: no legible text (0/7 words >= 60, mean confidence 8) -->
<!-- figure 2 on pdf page 153 at 36,149-184,281 pt | caption: none | text-layer labels: LAN | 192.168.2.0/24 | nearby labels: GRE VPN topology PC1 | PC2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 153 at 253,185-320,237 pt | caption: none | text-layer labels: Internet | nearby labels: GRE-2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 153 at 38,422-555,485 pt | caption: none | text-layer labels: none | nearby labels: Click | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 87) -->
Tunnel Settings
Index
Enable
Remote IP Address
Description
<!-- end of figure 4 -->

<!-- pdf page 154 | printed page 154 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

When finished, click   to submit and click

for the configuration to take effect.

<!-- figure 1 on pdf page 154 at 33,65-557,365 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 27/35 words >= 60, mean confidence 80) -->
[1
Index
Enable
Description
cre-1
Remote IP Address
Local Virtual IP Address
Local Virtual Netmask/Prefix Length
Remote Virtual IP Address
10.8.0.2
Enable Default Route
Enable NAT
Secrets
<!-- end of figure 1 -->

<!-- pdf page 155 | printed page 155 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

GRE-2:
On the remote side, click   button and set the parameters of GRE-2 as below.

When finished, click             to submit and click

The comparison between GRE-1 and GRE-2 is as below.

for the configuration to take effect.

<!-- figure 1 on pdf page 155 at 33,110-557,413 pt | caption: none | text-layer labels: none | nearby labels: GRE-2: | On the remote side, click | OCR text follows (tesseract, unverified; 27/32 words >= 60, mean confidence 83) -->
[1
Index
Enable
Description
Remote IP Address
Local Virtual IP Address
|255.255.255.0
Local Virtual Netmask/Prefix Length
[10.8.0.1
Remote Virtual IP Address
Enable Default Route
Enable NAT
Secrets
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 155 at 33,489-559,672 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 86/102 words >= 60, mean confidence 84) -->
(1
fa
Index
Index
a
Enable
Enable
Description
GRE-1
GRE-2
Exfernal IP address of another GRE instance
the initial connection between peers.
Remote IP Address
58.1.1.1
Remote IP Addr
59.1.1.1
Local Virtual IP Address
Local Virtual IP Address
10.8.0.2
Local Virtual Netmask/Prefix Length
Local Virtual Netmask/Prefix Length
255.255.255.0
address of the remote GRE Tunnel network interface.
N
Remote Virtual IP Address
10.8.0.2
Remote Virtual IP Address
Enable Default Route
Enable Default Route
Enable NAT
Enable NAT
Used the same password for the GRE peers
Secrets
submit
<!-- end of figure 2 -->

<!-- pdf page 156 | printed page 156 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Chapter 4 Introductions for CLI

4.1            What Is CLI

Command-line interface (CLI) is a software interface providing another way to set the parameters of equipment from
the SSH or through a telnet network connection. After establishing a Telnet or SSH connection with the router, enter
the login account and password (here take admin/admin for example) to enter the configuration mode of the router,
as shown below.
Route login:
Router login: admin
Password: admin(could be different)
#
CLI commands:
    #?
    #
        !                Comments
        add              Add a list entry of configuration
        clear           Clear statistics
        config          Configuration operation
        debug            Output debug information to the console
        del              Delete a list entry of configuration
        do               Set the level state of the do
        exit            Exit from the CLI
        help             Display an overview of the CLI syntax
        ovpn_cert_get Download OpenVPN certificate file via http or ftp
        ping             Send messages to network hosts
        reboot           Halt and perform a cold restart
        set             Set system configuration
        show              Show system configuration
        status          Show running system information
        tftpupdate      Update firmware or configuration file using tftp
        traceroute     Print the route packets trace to network host
        trigger        Trigger action
        urlupdate       Update firmware via http or ftp
        ver              Show version of firmware

<!-- pdf page 157 | printed page 157 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

4.2       How to Configure the CLI

Following is a table about the description of help and the error should be encountered in the configuring program.
 Commands /tips                          Description
 ?                                       Typing a question mark “?” will show you the help information.
                                         eg.
                                         # config（Press ‘?’）
                                            config Configuration operation

                                         # config（Press spacebar +’?’）
                                            commit                 Save the configuration changes and take effect
                                         changed configuration
                                            save_and_apply      Save the configuration changes and take effect
                                         changed configuration
                                            loaddefault       Restore Factory Configuration
 Ctrl+c                                  Press these two keys at the same time, except its “copy” function but also
                                         can be used for “break” out of the setting program.
 Syntax error: The command is not        Command is not completed.
 completed
 Tick space key+ Tab key                 It can help you finish you command.
                                         Example:
                                         # config (tick enter key)
                                         Syntax error: The command is not completed
                                         # config (tick space key+ Tab key)
                                         commit              save_and_apply loaddefault
 #config commit                          When your setting finished, you should enter those commands to make
 # config save_and_apply                 your setting take effect on the device.
                                         Note: Commit and save_and_apply plays the same role.

4.3       Commands Reference

 Commands           Syntax                    Description
 Debug              Debug parameters          Turn on or turn off debug function
 Show               Show parameters           Show current configuration of each function , if we need to see all
                                              please using “show running ”
 Set                Set parameters            All the function parameters are set by commands set and add, the
                                              difference is that set is for the single parameter and add is for the list
 Add                Add parameters
                                              parameter
Note: Download the config.XML file from the configured web browser. The command format can refer to the
config.XML file format.

<!-- pdf page 158 | printed page 158 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

4.4      Quick Start with Configuration Examples

The best and quickest way to master CLI is firstly to view all features from the web page and then read all CLI
commands at a time, finally learn to configure it with some reference examples.

Example 1: Show current version
# status system
firmware_version = 2.0.0
firmware_version_full = "2.0.0 (60b55c0)"
kernel_version = 5.4.24-2.0.0
hardware_version = 0.0
operation_system = "Debian GNU/Linux 11.3"
device_model = ""
serial_number = 2204190667030003
temperature_interval = 53.0
uptime = "0 days, 00:12:06"
system_time = "Thu May 19 16:52:22 2022"
ram_usage = 392M/448M
cpu_usage = "22569s Idle/71405s Total /1 cpus"
disk_usage = 1.9G/7.1G
#

Example 2: CLI for setting Cellular
# show cellular all
primary_sim = sim1
auto_switch = false
switch_by_signal = false
rssi_quality = -87
switch_while_roaming = false
sim {
      id = 1
      card = sim1
      phone_number = ""
      pin_code = ""
      extra_at_cmd = ""
      telnet_port = 0
      network_type = auto
      band_select_type = all
      band_settings {
            gsm_850 = false
            gsm_900 = false
            gsm_1800 = false
            gsm_1900 = false

<!-- pdf page 159 | printed page 159 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

          wcdma_800 = false
          wcdma_850 = false
          wcdma_900 = false
          wcdma_1900 = false
          wcdma_2100 = false
          wcdma_1700 = false
          wcdma_band19 = false
          lte_band1 = false
          lte_band2 = false
          lte_band3 = false
          lte_band4 = false
          lte_band5 = false
          lte_band7 = false
          lte_band8 = false
          lte_band13 = false
          lte_band17 = false
          lte_band18 = false
          lte_band19 = false
          lte_band20 = false
          lte_band21 = false
          lte_band25 = false
          lte_band28 = false
          lte_band31 = false
          lte_band38 = false
          lte_band39 = false
          lte_band40 = false
          lte_band41 = false
     }
     debug_enable = true
     verbose_debug_enable = false
}
# set(space+space)
ai              bridge               cellular
dmvpn           email               ethernet
gps             gre                 ipsec
ntp             openvpn              policy_router
qos              rcms                reboot
sms              snmp                ssh
Usb             syslog              user_management
web_server      wan_links            web_server

# set cellular(space+?)
  sim SIM Settings
# set cellular sim(space+?)
  Integer Index (1..1)

ddns            dido
event            firewall
l2tp             lan_links
 pppoe_bridge     pptp
 route           serial_port
 syslog         system
  vlan          vrrp
 wireless

<!-- pdf page 160 | printed page 160 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

# set cellular sim 1(space+?)
   card                       SIM Card
   phone_number               Phone Number
   pin_code                   PIN Code
   extra_at_cmd               Extra AT Cmd
   telnet_port                Telnet Port
   network_type               Network Type
   band_select_type           Band Select Type
   band_settings              Band Settings
   telit_band_settings        Band Settings
   debug_enable               Debug Enable
   verbose_debug_enable Verbose Debug Enable
# set cellular sim 1 phone_number 18620435279
OK
…
# config save_and_apply
OK                                           // save and apply current configuration, make you configuration effect

<!-- pdf page 161 | printed page 161 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Chapter 5 Glossary
Abbr.      Description
AC         Alternating Current
APN        Access Point Name
ASCII      American Standard Code for Information Interchange
CE         Conformité Européene (European Conformity)
CHAP       Challenge Handshake Authentication Protocol
CLI        Command Line Interface for batch scripting
CSD        Circuit Switched Data
CTS        Clear to Send
dB         Decibel
dBi        Decibel Relative to an Isotropic radiator
DC         Direct Current
DCD        Data Carrier Detect
DCE        Data Communication Equipment (typically modems)
DCS 1800   Digital Cellular System, also referred to as PCN
DI         Digital Input
DO         Digital Output
DSR        Data Set Ready
DTE        Data Terminal Equipment
DTMF       Dual Tone Multi-frequency
DTR        Data Terminal Ready
EDGE       Enhanced Data rates for Global Evolution of GSM and IS-136
EMC        Electromagnetic Compatibility
EMI        Electro-Magnetic Interference
ESD        Electrostatic Discharges
ETSI       European Telecommunications Standards Institute
EVDO       Evolution-Data Optimized
FDD LTE    Frequency Division Duplexing Long Term Evolution
GND        Ground
GPRS       General Packet Radio Service
GRE        generic route encapsulation
GSM        Global System for Mobile Communications
HSPA       High Speed Packet Access
ID         identification data
IMEI       International Mobile Equipment Identity
IP         Internet Protocol
IPsec      Internet Protocol Security
kbps       kbits per second
L2TP       Layer 2 Tunneling Protocol

<!-- figure 1 on pdf page 161 at 62,120-148,777 pt | caption: none | text-layer labels: none | nearby labels: Abbr. | AC APN | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 161 at 213,120-559,777 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 162 | printed page 162 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Abbr.         Description
LAN           local area network
LED           Light Emitting Diode
M2M           Machine to Machine
MAX           Maximum
Min           Minimum
MO            Mobile Originated
MS            Mobile Station
MT            Mobile Terminated
OpenVPN       Open Virtual Private Network
PAP           Password Authentication Protocol
PC            Personal Computer
PCN           Personal Communications Network, also referred to as DCS 1800
PCS           Personal Communication System, also referred to as GSM 1900
PDU           Protocol Data Unit
PIN           Personal Identity Number
PLCs          Program Logic Control System
PPP           Point-to-point Protocol
PPTP          Point to Point Tunneling Protocol
PSU           Power Supply Unit
PUK           Personal Unblocking Key
R&TTE         Radio and Telecommunication Terminal Equipment
RF            Radio Frequency
RTC           Real Time Clock
RTS           Request to Send
RTU           Remote Terminal Unit
Rx            Receive Direction
SDK           Software Development Kit
SIM           subscriber identification module
SMA antenna   Stubby antenna or Magnet antenna
SMS           Short Message Service
SNMP          Simple Network Management Protocol
TCP/IP        Transmission Control Protocol / Internet Protocol
TE            Terminal Equipment, also referred to as DTE
Tx            Transmit Direction
UART          Universal Asynchronous Receiver-transmitter
UMTS          Universal Mobile Telecommunications System
USB           Universal Serial Bus
USSD          Unstructured Supplementary Service Data
VDC           Volts Direct current
VLAN          Virtual Local Area Network
VPN           Virtual Private Network

<!-- pdf page 163 | printed page 163 | header: RobustOS Pro Software Manual | footer: RT_SM_v2.1.1 / September 14, 2023 -->

Abbr.        Description
VSWR         Voltage Stationary Wave Ratio
WAN          Wide Area Network

        Guangzhou Robustel Co., Ltd.
        Add:       501, Building#2, 63 Yongan Road, Huangpu District,
                   Guangzhou, China 511350
        Email:     info@robustel.com
        Web:       www.robustel.com

<!-- figure 1 on pdf page 163 at 33,65-559,127 pt | caption: none | text-layer labels: Abbr. | Description | VSWR WAN | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 163 at 74,317-593,470 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
