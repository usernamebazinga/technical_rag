# Actisense PRO-Range products

<!-- source: sources/DCU-2/PRO-Products-Configuration-Manual-Issue-1.2-1.pdf | extraction: extracted/DCU-2/PRO-Products-Configuration-Manual-Issue-1.2-1.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: no ToUnicode map in Roboto-Bold, Roboto-Regular; ligatures (fi, fl) or special glyphs may be missing from the text (pages none checked against the rendered page) -->

<!-- pdf page 1 | printed page 1 -->

Actisense PRO-Range products

## Configuration Manual

- PRO-BUF-2 - NMEA 0183 Buffer
- PRO-MUX-2 - NMEA 0183 Multiplexer
- PRO-NDC-1E - NMEA 0183 Multiplexer
- PRO-NDC-1E2K - NMEA 0183 Multiplexer

Issue 1.2 1                      Active Research Ltd 2025

<!-- figure 1 on pdf page 1 at 141,29-447,91 pt | caption: none; nearest centred text below: "Actisense PRO-Range products" | text-layer labels: none | nearby labels: Connect without limits | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 74) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 1 at 490,245-564,312 pt | caption: none | text-layer labels: none | OCR: no legible text (0/2 words >= 60, mean confidence 23) -->

<!-- figure 3 on pdf page 1 at 38,321-325,499 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 18/35 words >= 60, mean confidence 59) -->
BIA
BIA
BIA
BIA
BIA
BIA
ie)
Actisense
0183
NMEA 0183 Intelligent Buffer
[PWR] SERIAL
Ethernet
A\B
A\B
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 1 at 361,321-552,501 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/23 words >= 60, mean confidence 54) -->
IN2 IN3 IN4 INS
ISOLATED USTENERS
0183
NMEA 0183 Intelligent Multiplexer
de
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 1 at 0,513-593,839 pt | caption: none | text-layer labels: Issue 1.2 Active Research Ltd 2025 | OCR text follows (tesseract, unverified; 41/78 words >= 60, mean confidence 54) -->
BIA
BIA
2
e
e
IN2 IN3 IN4 INS
9
IN1
IN3 IN4
INS ING IN7| INS
ALARM
suns
LISTENERS
TALKERS
Actisense
Actisense 22
0183
0183
NMEA 0183 Multiplexer NMEA 2000
NMEA 0183 Intelligent Multiplexer
ISOLATED TALKERS
e
fe
Al]
Ethernet
<!-- end of figure 5 -->

<!-- pdf page 2 | printed page 2 | header: PRO-Range configuration manual -->

## PRO-Range configuration manual

can be found below the barcode on the label. Your

| Important Notices | registration will assist Actisense Support to link |
| --- | --- |
| The device to which this manual relates | your product to your details, simplifying any future |
| complies with the Electromagnetic Compatibility | assistance you may require. |
| requirements according to IEC 60945:2002-08, |  |
| DNVGL-CG-0339:2019 & IACS UR E10 Rev7. |  |
| The unit should always be used in conjunction | Product Guarantee |
| with appropriately approved, shielded cable | All Actisense products are provided with a 5 year |
| and connectors as per NMEA 0400 to ensure | guarantee upon registration. To register your |
| compliance. A declaration of conformity is | product, visit https://actisense.com/product- |
| available for download at www.actisense.com. | registration. |
| If the device to which this manual relates is to be   If you suspect that the unit is faulty please refer to |  |
| installed within five metres of a compass, please     the Troubleshooting Section of the User Manual |  |
| refer to the ‘Compass Safe Distance’ section in the   before |  |
| ‘Technical Specifications’ table. | contacting support. |
| Trademarks and Registered Trademarks | It is a requirement of the guarantee that all installations of electronic equipment follow the |
| Actisense® and the Actisense logo are registered | NMEA 0400 specification. Any connection to a |
| trademarks of Active Research Limited (Ltd). | battery or power supply must meet the mandatory |
| All other trademarks are the property of their | essential safety requirements that may be |
| respective owners. | imposed by local regulatory agencies. |
| The NMEA® name and NMEA logo are copyright | Actisense products are intended for use in a |
| held by the NMEA. All uses in this manual are by | marine environment, primarily for below deck |
| permission and no claim on the right to the NMEA | use. If a product is to be used in a more severe |
| name or logo are made in this manual. | environment, such use may be considered misuse under the Active Research Ltd guarantee. |

<!-- omitted: "Fair Use Statement" (pdf page 2; 6 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Technical Accuracy" (pdf page 2; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
#### Product Registration

Please register your product via the online form at https://actisense.com/product-registration Your product package includes a unit serial number. The serial number is six digits long and

Contents Page

Advanced Routing.....................................................................................................................17-18

<!-- figure 1 on pdf page 2 at 0,26-1188,67 pt | caption: none; nearest centred text below: "Contents Page" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- pdf page 3 | printed page 4 | header: PRO-Range configuration manual -->

#### Introduction

This manual contains instructions for configuring the following PRO range of products from Actisense.

| • | PRO-BUF-2 | NMEA0183 Intelligent Buffer |
| --- | --- | --- |
| • | PRO-MUX-2 | NMEA0183 Intelligent Multiplexer |
| • | PRO-NDC-1E | NMEA0183 Intelligent Multiplexer |
| • | PRO-NDC-1E2K | NMEA0183 Multiplexer / NMEA 2000 Gateway |

Please read through this manual carefully to realise the full potential of your new PRO product. This manual should be read in conjunction with the individual user/install manual available from the Actisense website at http://www.actisense.com

Built into the firmware of each PRO range products is a web-based configuration app. that allows the set-up to be tailored to your individual needs from any internet browser. Please Note : Since the products listed above have slightly different features, some of the screen shots contained within this manual will look different to the observed behaviour when a user configures their own PRO-range device, but the overall ‘look and feel’ will be the same as shown in the following pages. Specific features which are not available are highlighted in the table below. Each PRO range product has it’s own installation manual where all the technical specifications, information on connectivity, and wiring details for each device can be found. Please visit our website https://actisense.com for the individual install manuals relating to your own product.

##### PRO-Range products at a glance

| Product | PRO-BUF-2 | PRO-MUX-2 | PRO-NDC-1E | PRO-NDC-1E2K |
| --- | --- | --- | --- | --- |
| Inputs | 2 | 8 | 2 | 2 |
| Outputs | 12 | 6 | 5 | 5 |
| Serial Ports | 1 | 1 | 1 | 1 |
| Ethernet(servers) | YES(1) | YES(4) | YES(1) | YES(2) |
| NMEA 2000 | NO | NO | NO | YES |
| Alarms | YES | YES | NO | NO |

#### Accessing the PRO range of products via an ethernet network

The PRO range can be connected to your network in one of two ways.

#### 1: Standard Ethernet Networks

| • | If the PRO product is connected to an ethernet network containing both DHCP and DNS servers, launch any of the popular web browsers. |
| --- | --- |
| • | Replacing ‘xxxxxx’ with the serial number of your PRO product, found on the side of the case, type one of the following commands into the address bar depending on the product you have. |

#### http://probuf-xxxxxx • http://promux-xxxxxx • http://prondc-xxxxxx (NOTE : Both variants of PRO-NDC use the same wording)

#### 2: Direct connection or basic ethernet networks

- If the PRO product is connected directly to a PC or the ethernet network does not have a DHCP server, the device will communicate using the auto-IP by default.
- The auto-IP process can take up to 60 seconds to complete.
- The PC’s ‘Local Area Connection’ must also be set-up to use auto-IP in order to communicate on this network. Most PC’s are set-up to do this by default. If needed, instructions on how to do this using Windows 10 are given in the user/install manual (other Windows operating systems will be similar). These can be found by visiting https://actisense.com NOTE: PC administrator privileges are required to carry out these modifications.

| • | Once the PC and PRO product are using the same IP address range, launch any popular web browser. |
| --- | --- |
| • | Replacing ‘xxxxxx’ below with the serial number of your PRO product, type in one of the following commands into the address bar depending on the product you have. |

#### http://probuf-xxxxxx • http://promux-xxxxxx • http://prondc-xxxxxx (NOTE : Both variants of PRO-NDC use the same wording)

- The home-page for the PRO-MUX-2 will be as shown below.(Shown here for a PRO-MUX-2)
- NOTE: You may need to refresh your browser window if the web-app does not display immediately.
- NOTE: Clicking on any of the icons at this point will allow you to view the current settings of your PRO range device, but alterations are not possible until a user ‘Login’ is performed.

The Username is ‘admin’, and the default password can be found on the sticker located on the side of the product. If the password is changed, ensure to make a note of it. The password can be altered later. The username ‘admin’ is static and cannot be altered.

<!-- figure 1 on pdf page 3 at 0,26-1188,67 pt | caption: none | text-layer labels: none | nearby labels: Introduction | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 3 at 103,465-182,640 pt | caption: none | text-layer labels: none | nearby labels: Product | PRO-BUF-2 | Inputs | 2 | Outputs | 12 | 1 | YES(1) | NO | Alarms | YES | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 3 at 652,643-1131,806 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/24 words >= 60, mean confidence 85) -->
Actisense PRO-MUX-2 Combine 1
Information
Status
Settings
2022 Active Research Limited. All rights reserved. www.actisense.com
Version 2.478, Web Version 1.010
BETA
<!-- end of figure 3 -->

<!-- pdf page 4 | printed page 6 | header: PRO-Range configuration manual -->

#### Navigating the PRO range home-page (shown here for the PRO-MUX-2)

### Information Icon

| • | This icon will display all the relevant technical information relating to the device itself. |
| --- | --- |
| • | This information is important if you need to troubleshoot your device or require technical assistance at a future date. |

### Status Icon

- This icon displays the current status of all the various user controlled settings:

#### Data Servers: Displays the following information relating to the data server if enabled.

- Serial: Displays the current status of all the serial ports, including their baud rate, alias name if applied, port direction and the current data load on each port.

<!-- figure 1 on pdf page 4 at 0,26-1188,67 pt | caption: none; nearest centred text below: "Status Icon" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 4 at 721,74-762,115 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 4 at 57,110-537,273 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/24 words >= 60, mean confidence 85) -->
Actisense PRO-MUX-2 Combine 1
Information
Status
Settings
2022 Active Research Limited. All rights reserved. www.actisense.com
Version 2.478, Web Version 1.010
BETA
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 4 at 637,158-762,456 pt | caption: none | text-layer labels: none | nearby labels: • | • | • | OCR text follows (tesseract, unverified; 45/46 words >= 60, mean confidence 93) -->
4
Data Servers
Serial
Data Server 1
Enabled: Yes
Status: Open
Port: 60001
Protocol: TCP
Data Format: NMEA0183
Rx Avg Bytes/s: 0
Total Rx Bytes: 0
Rx Dropped Bytes/s: 0
Rx Total Dropped: 0
Tx Bytes Total: 0
TCP Client Connections: 0
Disconnect Count: 0
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 4 at 60,401-522,777 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 69/70 words >= 60, mean confidence 95) -->
Information
Status
Device
Ethernet Status
Operating Mode:
Model ID:
MAC Address:
Combine 1
PRO-MUX-2
70-B3-D5-6A-0D-8D
Serial Number:
Address:
Battery Voltage:
11.86
718
192.168.0.92
Log:
Date Time of manufacture
Subnet:
Disabled
05/05/2022, 10:37:42
255.255.255.0
Uptime:
Hardware ID:
Gateway:
0:04:15:25
080104
192.168.0.254
Firmware version:
Host Name:
2.434
promux-718
Date Time of Firmware:
HTTP Port:
01/09/2022, 06:45:44
80
Firmware CRC:
DHCP:
Enabled
Bootloader version:
1.080
Bootloader CRC:
0x12345678
Web UI version:
0.246
<!-- end of figure 5 -->

<!-- figure 6 on pdf page 4 at 637,501-1006,796 pt | caption: none | text-layer labels: none | nearby labels: • | OCR text follows (tesseract, unverified; 12/15 words >= 60, mean confidence 73) -->
f Data Servers
Detailed Stats
Alarms:
Speed
Direction
oad
115200
Manual
IN7
<!-- end of figure 6 -->

<!-- pdf page 5 | printed page 8 | header: PRO-Range configuration manual -->

- Detailed Stats: Once the PRO device is operational, this page will show the number of individual sentences being received or transmitted over a 10 second period. The picture below shows a simple case of GPS sentences being sent and received. Once the device has more inputs and outputs enabled this will contain all the sentences being routed through the device.

#### Messages being received from talkers

#### Messages being transmitted to listeners

#### Routing: Matrix showing data flow between inputs and outputs

- Alarms: Shows the status of any alarms which are currently set. See page 19 for further details regarding setting up alarms, and their requirements.

<!-- figure 1 on pdf page 5 at 0,26-1188,67 pt | caption: none; nearest centred text below: "•" | text-layer labels: none | nearby labels: • | • | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 5 at 620,103-1056,485 pt | caption: none; nearest centred text below: "• Alarms: Shows the status of any alarms which are currently set. See page 19 for further details" | text-layer labels: none | nearby labels: • | OCR below floor, text not used (5/13 words >= 60, mean confidence 51) -->

<!-- figure 3 on pdf page 5 at 24,168-568,444 pt | caption: none | text-layer labels: none | nearby labels: • | Messages being received from talkers | • | Messages being transmitted to listeners | OCR text follows (tesseract, unverified; 26/27 words >= 60, mean confidence 93) -->
Data Servers
Serial
Detailed Stats
Alarms
Time Period: 10 secs
Receive Transmit
IN1-GPS
IN2
IN3
10
GPDTM
10
10
GPGLL
10
GPGSV
10
9
10
GPVTG
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 5 at 24,470-568,748 pt | caption: none | text-layer labels: none | nearby labels: • | Messages being transmitted to listeners | OCR text follows (tesseract, unverified; 24/27 words >= 60, mean confidence 88) -->
4
Data Servers
Detailed Stats
Routing
Alarms
Time Period: 10 secs
Receive i Transmit
MXTXT
GPGLL
10
GPRMC
10
10
10
10
10
10
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 5 at 620,532-1162,748 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 36/38 words >= 60, mean confidence 90) -->
Alarms
Data Servers
Serial
Detailed Stats
Routing
Event
Re-Arm
Action
State
Repeat
Autoswitch
60s
NMEA0183 Message
1min
Set Relay
NMEA0183 Message
Data Overload
Repeat
60s
1min
Set Relay
Repeat
12V
NMEA0183 Message
60s
1min
Set Relay
<!-- end of figure 5 -->

<!-- pdf page 6 | printed page 10 | header: PRO-Range configuration manual -->

### Settings Icon

| • | Provides access to the device for configuration. |
| --- | --- |
| • | Using any of these setting requires that the user ‘Login’ to the device (see page 5). |
| • | The settings page provides the following functionality: |

Administration: Facility to change password only (Username is always ‘admin’) Facility to re-start device. Firmware Update: Details current firmware version and provides the facility to update. Network: Allows the network to be configured correctly depending upon your particular set-up. Operating mode: Allows any pre-configured modes to be selected. Reset Password: Password can be reset to factory default Alarms: Allows the user to set up any required alarms. Data Server: Provides facility to turn server on/off as well as specifying data format output, direction and output protocol. Routing: Main configuration table to allow precise routing of data between inputs an outputs. Access to ‘autoswitch’ operation and set-up. Serial: Allows full configuration for each port including baud rate setting, data direction, an ‘alias’ naming facility and also shows the current data load on each port.

#### Planning your NMEA0183 network

| • | Your PRO range device allows you to input data from NMEA0183 talkers’ and direct these signals either individually, or in combination with other signals, to the various output ports which the de- vice provides (See page 4 for details on individual number of ports available of the PRO range). |
| --- | --- |
| • | In order for this to work correctly, the device must know at what baud rate the connected device is running. It is helpful to be able to name each device separately, so a facility to do this is provided. |

#### Configuring Input from ‘Talkers’

| • | Please read this section in conjunction with the install/user manual if unsure of the required steps |
| --- | --- |
| • | Adding an 0183 ‘talker’ device is a straight forward process. |
| • | Connect your NMEA 0183 ‘talker’ to one of the ‘Listener’ ports on the PRO product. |
| • | Pay attention to the wire-colours if your device follows the NMEA 0183 standard. |
| • | Connect the ‘talker’ pair of wires from your 0183 device to your PRO device “listener” port. |
| • | Configure the device from within ‘Serial Settings’ of the configuration tool. |
| • | Give the device a useful/meaningful name for future reference by filling in the blank ‘Name’ box next to its input. |

As an example, shown below, we have installed an AIS unit/two GPS units and a Speed sensor to the first four inputs of a PRO-MUX-2. We have set the baud rate (speed) of the AIS unit to 38400, which is the usual rate for an AIS unit. The remaining three devices have all been set to 4800 baud.

NOTE: The first four inputs of the PRO-MUX-2 can be set to ‘auto-baud’ between 4800 & 38400 if required. Auto-baud allows the PRO-MUX-2 to follow the baud rate of the connected talker, without the need to specify it. This is helpful if you are unsure of the ‘talker’ baud rate, or it can change during its normal operation. Inputs 5-8 are pre-set to 4800 baud only. Again, the number of inputs and outputs visible will depend on the product being configured. Auto-baud is a feature implemented on all PRO-range products.

#### Manual / Autobaud

<!-- figure 1 on pdf page 6 at 0,26-1188,67 pt | caption: none; nearest centred text below: "Planning your NMEA0183 network" | text-layer labels: none | nearby labels: Planning your NMEA0183 network | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 6 at 139,77-180,118 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 6 at 38,180-553,391 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/7 words >= 60, mean confidence 55) -->
(Settings
System
Data
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 6 at 618,492-1162,799 pt | caption: none | text-layer labels: none | nearby labels: Manual / Autobaud | OCR text follows (tesseract, unverified; 13/21 words >= 60, mean confidence 67) -->
Serial Settings
SERIAL
115200
v
Manual
IN1
#1
Manual
#2
Manual
Speed
Manual
<!-- end of figure 4 -->

<!-- pdf page 7 | printed page 12 | header: PRO-Range configuration manual -->

#### Configuring Output to ‘Listeners’

| • | Configuring outputs from the PRO device is performed in a similar way to configuring inputs. |
| --- | --- |
| • | Please read this section in conjunction with the install/user manual if unsure of the required steps |
| • | Pay attention to the wire-colours if your device follows the NMEA 0183 standard. |
| • | Connect the ‘talker’ pair of wires from your PRO device to your NMEA 0183 “listener” port. |
| • | Configure the device from within the ‘Serial Settings’ of the configuration tool. |
| • | Give the output stream a useful/meaningful name for future reference as shown previously. |

As an example below, we have installed an NGW-1-ISO, a Radar and an Autopilot to the first three outputs of a PRO-MUX-2. We have set the baud rate (speed) of the NGW-1-ISO unit to 38400 baud. The remaining devices have been set to 4800. Consult the manuals and datasheets for your individual devices to find the correct settings.

To confirm any changes made to the INPUTS and OUTPUTS on the device, click on the Serial tab of the ‘Status’ page.

The setting made above will result in the following page being displayed (p.13)

#### Serial ‘Status’ confirmation

| • | Below is the current state of INPUTS and OUTPUTS based on the previous examples. |
| --- | --- |
| • | With real devices connected and ‘talking’ to the network, there would be an indication of ‘Load’ displayed as well. |

#### Load Indicator

- Once the device is operational and combining data, each port in use will give an indictation of its current ‘load’ and sentences being passed as shown below.

<!-- figure 1 on pdf page 7 at 0,26-1188,67 pt | caption: none; nearest centred text below: "Serial ‘Status’ confirmation" | text-layer labels: none | nearby labels: Configuring Output to ‘Listeners’ | Serial ‘Status’ confirmation | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 86) -->
Actisense PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 7 at 620,151-1159,585 pt | caption: none | text-layer labels: none | nearby labels: Load Indicator | • | OCR text follows (tesseract, unverified; 48/55 words >= 60, mean confidence 87) -->
Data Servers
Serial
Detailed Stats
Routing
Alarms
Interface
Name
Mode
Direction
Load
Speed
115200
0%
Manual
0%
GPS #1
Manual
0%
GPS #2
Manual
4800
0%
Manual
4800
0%
0%
0%
0%
IN8
4800
0%
0%
0%
0%
Autopilot
OUT4
4800
0%
0%
OUT6
0%
0%
DS1
0%
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 7 at 26,285-565,566 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/17 words >= 60, mean confidence 70) -->
Serial Settings
O
IN7
4800
OUT1
38400
OUT2
4800
‘Autopilot
OUT3
4800
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 7 at 31,614-561,715 pt | caption: none; nearest centred text below: "The setting made above will result in the following page being displayed (p.13)" | text-layer labels: none | OCR text follows (tesseract, unverified; 3/7 words >= 60, mean confidence 49) -->
Information
Status
Settings
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 7 at 618,636-1162,777 pt | caption: none | text-layer labels: none | nearby labels: • | OCR text follows (tesseract, unverified; 22/31 words >= 60, mean confidence 73) -->
Settings
Name
Mode
Speed
Direction
Interface
Load
0%
SERIAL
115200
0%
IN1
GPS
Auto
4800
62%
GPDTM(0) GPGGA(10) GPGSA(10) GPGSV(0) GPRMC(9) GPVTG(10)
<!-- end of figure 5 -->

<!-- pdf page 8 | printed page 14 | header: PRO-Range configuration manual -->

#### Routing of INPUTS to OUTPUTS

| • | Once the required ‘talkers and ‘listeners’ are connected to the device, you need to decide how you wish the various input signals to be routed and/or combined to the required outputs. |
| --- | --- |
| • | When implementing this routing plan, there are baud rate issues that need to be considered. |

- An input signal being received at 4800 baud will not be output 4x faster if the output baud rate is set to 38400 baud. The device cannot replicate the messages it receives. The input signal of 4800 baud can be output at 38400 baud, but not repeated any faster than the original 4800 input baud rate frequency.

- An input signal being received at 38400 baud will result in a loss of data if it is tied to an output baud rate rate lower than the input. If the rate of messages being received is faster than the output port can transmit them, this will lead to signal loss, and sentences being dropped. This is quite a common scenario and is not necessarily an issue if its implications are understood.

#### The Routing Matrix (see page 15 for details of routing settings)

Shown below is an indication of the routing matrix which will be observed on the device.
- This screen shot shows the settings for a PRO-MUX-2 for example only.
- The inputs for the PRO-MUX-2 are located on the LHS of the matrix table.
- The outputs from the PRO-MUX-2 are shown on the horizontal orange bar.
- DS1(IP) input/output relates to the Ethernet port.
- ASW1 & ASW-2 provide access to the auto-switching functionality. These are inactive when auto-switching is not being used.

#### Basic Routing

| • | The basic routing of signals is a straight forward process of connecting inputs and outputs in the matrix table. |
| --- | --- |
| • | Inputs and outputs are connected by setting or clearing the point where they cross in the table. |
| • | As an example setting (shown below) the following routing connections have been made. |
| • | OUT-6 - Taking a feed from IN-2 and IN-7 |
| • | OUT-5 - Taking a feed from IN-2 and IN-7 |
| • | OUT-4 - Taking a feed from IN-1 and IN-7 |
| • | OUT-3 - Taking a feed from IN-5 only |
| • | OUT-2 - Taking a feed from IN-3 and IN-5 |
| • | OUT-1 - taking a feed from IN-3 only |

From your browser window, simply click the box where you wish a connection between input and output to be made and an orange arrow will indicate that this IN-OUT connection has been implemented. To disable the routing between and input & output, simply click the arrow again, and the connection will be removed.

<!-- figure 1 on pdf page 8 at 0,26-1188,67 pt | caption: none; nearest centred text below: "Basic Routing" | text-layer labels: none | nearby labels: Routing of INPUTS to OUTPUTS | Basic Routing | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 86) -->
Actisense PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 8 at 620,324-676,372 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 8 at 618,425-1054,808 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/23 words >= 60, mean confidence 55) -->
Routing Settings
sows
Destination
Source
4
+t
J
J
J
4
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 8 at 26,429-565,825 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/16 words >= 60, mean confidence 63) -->
Routing Settings
aswe
Destination
Source
la
Active Recearch td
<!-- end of figure 4 -->

<!-- pdf page 9 | printed page 16 | header: PRO-Range configuration manual -->

| Auto-switching | Advanced Routing |  |
| --- | --- | --- |
| •   For marine systems that have multiple NMEA devices of an identical type (e.g. two GPS’s or two | • | Advanced routing is a feature which allows the user to select which messages within an 0183 |
| depth sounders), automatic selection of the highest priority device with valid data is very im- |  | data stream are allowed to pass to the output and which sentences are not transmitted. |
| portant. However, the NMEA 0183 standard has no method of automatically switching between | • | It is an ideal feature if you only require certain sentences transmitted and helps to improve the |
| different devices, so this requirement is usually fulfilled with a manual changeover switch. |  | message bandwidth. |
| •   The PRO-MUX-2 has the provision for auto-switching between two devices, where the incoming | • | As an example of how this feature works, we have set up a feed from IN-1 to OUT-1 with a data |
| signal can be prioritised in case of signal loss on one of the channels. |  | stream containing 5 different 0183 sentences. |
| •   In practise, this means that should the signal on your GPS(1) be interrupted due to a malfunction | • | These sentences contain GPGGA, GPGSA, GPGSV, PGVTG & GPZDA. |
| of the GPS unit, the auto-switching facility will detect this and the signal from GPS(2) will automat-   • |  | On feeding this data into IN-1 and out from OUT-1 the following message stream would be availa- |
| ically replace it, giving you a seamless continuation of your data. |  | ble. |
| •   The PRO-MUX-2 allows for auto-switching of two devices (eg. GPS’s(x2) & Depth sounders(x2)). |  |  |
| •   Any NMEA 0183 device can be auto-switched if required. |  |  |

#### Auto-switch routing

| • | The auto-switch is configured in software to act as an INPUT even though it does not have a phys- ical direct input of its own. It is often described as a “virtual input.” |  |
| --- | --- | --- |
| • | To configure the ASW mode, you need to decide which inputs you wish to be auto-switched. It is very common to auto-switch a GPS signal, so the following description will assume that a GPS unit is attached to IN-1 and IN-2 as an example. |  |
| • | From within the routing matrix, enable ASW1 with the slider at the top of the window. This will change the ASW1 output row at the bottom of the screen to be active. |  |
| • | Press “Add” and select which of the physical inputs you would like to be the primary GPS source. |  |
| • | Repeat the above step, and add which GPS input will be the secondary source should the primary GPS fail. |  |
| • | On the active ASW-1 row at the bottom, select which output you require the auto-switched signal to be fed to (in this example OUT-1 is used). The ASW-1 will now feed IN-1 to OUT-1, and in the event of IN-1 failing, will autoswitch to feeding IN-2 to OUT-1. |  |
| • | NOTE: In the main matrix, DO NOT also feed IN-1 & IN-2 to OUT-1. This will by-pass the auto-switch • functionality. Leave these as X. IN-1 & IN-2 can however still be used to feed other outputs. | On viewing the Routing Settings page, shown below, clicking on the ‘+’ sign at the RHS in the ‘“Ad- vanced” column will display all of the message headers that this stream contains. |

<!-- figure 1 on pdf page 9 at 0,24-1188,65 pt | caption: none; nearest centred text below: "Advanced Routing" | text-layer labels: none | nearby labels: Advanced Routing | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 72) -->
Actisense pRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 9 at 618,237-1162,470 pt | caption: none | text-layer labels: none | nearby labels: • | OCR below floor, text not used (35/133 words >= 60, mean confidence 42) -->

<!-- figure 3 on pdf page 9 at 618,511-1162,825 pt | caption: none | text-layer labels: none | nearby labels: • | OCR text follows (tesseract, unverified; 22/29 words >= 60, mean confidence 75) -->
f Routing Settings
ASW1
add
ASW2
add
Destination
Source
GPGGA
D
GPGSA
GPGSV
GPVTG
B
GPZDA
D
17
Active I td 9095
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 9 at 22,513-369,825 pt | caption: none | text-layer labels: none | OCR below floor, text not used (4/19 words >= 60, mean confidence 34) -->

<!-- pdf page 10 | printed page 18 | header: PRO-Range configuration manual -->

#### Advanced Routing (cont’d)

- If you wish, for example, to only allow sentence GPGGA to pass through to OUT-1, you need to perform the following three steps: 1: Enable the required message with the slider on the RHS (in this case GPGGA). 2: Disable the IN-1 to OUT-1 FULL data stream.This stops the entire stream being transmitted. 3: Enable the required message stream from within the header window (Tick beside GPGGA only).

| • | The setting shown above will automatically transmit GPGGA, and reject all other sentences from this data stream (as shown below). There is a small delay as buffers are emptied. |
| --- | --- |
| • | You are free to select other sentences for transmission, or by selecting all but one sentence, you can reject an individual sentence if required. |
| • | As shown below, only the GPGGA sentence is now being transmitted. |

#### Alarm Connections (PRO-BUF-2 & PRO-MUX-2) (See the user/install manual)

The PRO-range products feature alarm functionality which, depending on the condition being monitored, can output NMEA 0183 messages to display equipment / MFD’s etc. Currently, the PRO-range caters for three alarm conditions:

| • | Autoswitch: | Gives warning that an autoswitch occurance has occured. |
| --- | --- | --- |
| • | Data Overload: | Alerts the user that data overload has occured on a port |
| • | Low voltage: | Reports the status of the battery voltage. |

#### Alarm Relay

PRO-range products feature an alarm relay (Excludes PRO-NDC-1E & 1E2K) to allow electrical connections to be made to the device to trigger visual and/or audible signals. This will alert the user that an alarm condition has been met. The installed relay has the usual COM(Common), NC(Normally closed) & NO(Normally open) configuration. PLEASE NOTE: As written on the label of the device, the NC & NO legend refers to the de-energized state of the relay. i.e. The “powered off”/ ”power lost” state. When the device first receives power, you will hear a click as the relay energizes so that a “power lost” state can be detected by any alarm monitoring circuit. This implies that if you are connecting to a system which is monitoring a closed loop, then the COM and NO connections should be used so that the “power lost” state can be detected. Power loss is not an alarm event which can be sent as an 0183 sentence.

#### Setting the Alarm

The alarm has its own configuration menu accessed via the “Settings” page. Below we explain the process for setting up the “low voltage” alarm. There are three conditions that can be set with the “flag” icon.

| • | Output solely NMEA 1083 sentences |
| --- | --- |
| • | Activate the relay separately. |
| • | Activate both alarms together. |

| • | Event: Select the event you wish to monitor for. Here, we are setting the battery “low-voltage” alarm. Should it drop below 11v, the alarm will be triggered. |
| --- | --- |
| • | Re-Arm: The length of time you wish to elapse before the alarm is re-armed. |
| • | Action: This allows you to set the frequency of outputted messages. Uncheck “repeat” to allow a single message only. |
| • | To Activate the alarm simply click the “flag” icon in whichever position you require and this will change it’s colour from grey to green to indicate that the alarm is “enabled & inactive”. Should the alarm be activated, the flag will change colour to red to indicate an “enabled & active” status. |
| • | The “+” icon on the RHS gives access to an running alarm count. |
| • | To select which port you wish this alarm signal to be fed to, simply select the required output port in the small routing matrix at the bottom of the alarms window. |

<!-- figure 1 on pdf page 10 at 0,19-1188,60 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 10 at 24,182-568,475 pt | caption: none | text-layer labels: none | nearby labels: • | OCR text follows (tesseract, unverified; 6/10 words >= 60, mean confidence 61) -->
f Routing Settings
Asw2
Destination
Source
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 10 at 1008,437-1157,508 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/8 words >= 60, mean confidence 66) -->
Disabled
Enabled Inactive
Enabled Active
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 10 at 618,513-1159,564 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/12 words >= 60, mean confidence 81) -->
Event
Re-Arm
Action
State
1V
Repeat 1s
NMFA0183 Message
Low Voltage
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 10 at 24,566-568,804 pt | caption: none | text-layer labels: none | nearby labels: • | OCR text follows (tesseract, unverified; 153/228 words >= 60, mean confidence 66) -->
4
32
84 338 98
3
GPGGA 080454
31
114
E,1
08
115
49
16,M
*68
GPGGA 080454
31
4329
114
E,1
08
115
49
16,M
GPGGA 080494
31
4329
N,
114
E,1
08
115
16,4
*68
GPGGA 080494
31
4329
114
E,1
08
115
49
16,M
GPGGA 080494
31
4329
N,
114
E,1
08
115
49
16,M
GPGGA 080454
31
4329
114
E,1
08
115
16,M
GPGGA 880495
31
4329
115
E,1
08
115
19,M
49
*62
GPGGA
31
4329
115
E,1
08
115
19,M
16,M
*62
GPGGA
31
4329
N,
115
E,1
08
115
19,4
*62
GPGGA
31
4329
115
E,1
08
115
19,M
49
16,M
*62
GPGGA
31
4329
115
E,1
08
115
19,M
49
*62
GPGGA 080456
31
4329
115
E,1
08
115
16,M
GPGGA 080456
31
4329
N,
115
E,1
08
115
49
GPGGA 080496
31
N,
115
E,1
08
115
49
16,M
496
J1
21
115
115
<!-- end of figure 5 -->

<!-- pdf page 11 | printed page 20 | header: PRO-Range configuration manual -->

#### Data Server Settings

These data servers can work concurrently and can be enabled independently. The Data Server Settings need to be configured to correspond to that of the connected application software. To configure a data server for your application, you can setup the “Protocol”, “Format”, “Direction” and “Port”. There is also an independent “Check box” which can enable or disable a data server. This will not cause the device to forget the other settings – it is an on/off switch which will start or stop that server.

Format Several data formats are provided. If the format required for your application is not currently available, please contact Actisense support to check availability – we might already have it on our development road map or be able to add it specifically for a customer application. The current formats are: NMEA 0183, ASCII RAW, ASCII N2K, Actisense N2K, Actisense NGT, Actisense RAW (The Format can be configured in the ‘Serial’ Menu)

Direction This sets whether this data server will transmit, receive, or both receive and transmit data.

Protocol This is the “IP” protocol. Both TCP and UDP are supported, and this should be set according to the connected applications’ capabilities. TCP is recommended as it has built-in error correction.

Port Number By default, these devices use Ports 60001 - 60003, but can be set to any value corresponding to that of the application software. IP Ports can be set in the range 1-65535, although ports 1-1024 should be avoided, as they are used by special internet services. Setting a data server to use those ports could result in network problems.

Note: Some applications use the default setting for NMEA 0183 over Wi-Fi as port 10110, so in this case the Data server settings should be set to 10110. Other vendors such as Navionics use port 2000 for the default NMEA Wi-Fi gateway.

#### Troubleshooting Guide

First level PRO range diagnostics/fault finding can be performed by observing the LED behaviour. Please consult the user/install manual for your own device for details regarding LED behaviour.

In addition to the above, please always check the following points.
- Connectors are fully inserted
- All pins of the connector are in the correct location (not overlapping into another port position)
- Wires are terminated firmly and correctly (check polarity)

Active Research Ltd 21 Harwell Road Poole, Dorset UK BH17 0GE

- Telephone: +44 (0)1202 746682
- Email: sales@actisense.com
- Web: www.actisense.com

<!-- figure 1 on pdf page 11 at 0,22-1188,62 pt | caption: none; nearest centred text below: "Troubleshooting Guide" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 90) -->
Actisense
PRO-Range configuration manual
<!-- end of figure 1 -->
