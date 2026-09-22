# Professional Type Approved NMEA®

<!-- source: sources/DCU-2/pro-ndc-1e2k-user-manual-v1.01.pdf | extraction: extracted/DCU-2/pro-ndc-1e2k-user-manual-v1.01.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: SymbolMT is not a standard text face; glyphs "•" on pages 5, 7, 10, 12. Verify against the rendered page before trusting or mapping. -->
<!-- font check: no ToUnicode map in Aptos, ArialMT, Calibri, Roboto-Bold, Roboto-BoldItalic, Roboto-Regular, TimesNewRomanPSMT; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1-15 checked against the rendered page) -->

<!-- pdf page 1 | printed page 1 -->

Professional Type Approved NMEA®

## 0183 Multiplexer With NMEA 2000

## Gateway

<!-- figure 1 on pdf page 1 at 141,58-447,120 pt | caption: none | text-layer labels: none | nearby labels: Connect without limits | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 79) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 1 at 134,158-464,463 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 30/44 words >= 60, mean confidence 68) -->
BIA
BIA
IN1
IN3
IN4
TALKERS
ISOLATED LISTENERS
Actisense 22
0183
NMEA 0183 Multiplexer NMEA 2000 Gateway
PWR SERIAL
RxO
O
O
O
O
STATUS
IN fom OUT
NMEA
Ethernet
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 1 at 0,734-593,840 pt | caption: none | text-layer labels: Issue 1.01 | OCR: no legible text (0/3 words >= 60, mean confidence 14) -->

<!-- pdf page 2 | printed page 2 -->

### Important Notices

The device to which this manual relates complies with the Electromagnetic Compatibility requirements according to IEC 60945:2002-08, DNVGL-CG-0339:2019 & IACS UR E10 Rev7. The unit should always be used in conjunction with appropriately approved, shielded cable and connectors as per NMEA 0400 to ensure compliance. A declaration of conformity is available for download at www.actisense.com. If the device to which this manual relates is to be installed within five metres of a compass, please refer to the ‘Compass Safe Distance’ section in the ‘Technical Specifications’ table.

<!-- omitted: "Trademarks and Registered Trademarks" (pdf page 2; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair Use Statement" (pdf page 2; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Technical Accuracy" (pdf page 2; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
### Product Registration

Please register your product via the online form at https://actisense.com/product-registration Your product package includes a unit serial number. The serial number is six digits long and can be found below the barcode on the label. Your registration will assist Actisense Support to link your product to your details, simplifying any future assistance you may require.

### Product Guarantee

All Actisense products are provided with a 5 year guarantee upon registration. To register your product, visit https://actisense.com/productregistration. If you suspect that the unit is faulty please refer to the Troubleshooting Section of the User Manual before contacting support. It is a requirement of the guarantee that all installations of electronic equipment follow the NMEA 0400 specification. Any connection to a battery or power supply must meet the mandatory essential safety requirements that may be imposed by local regulatory agencies. Actisense products are intended for use in a marine environment, primarily for below deck use. If a product is to be used in a more severe environment, such use may be considered misuse under the Active Research Ltd guarantee.

### Product Disposal

Please dispose of this product in accordance with the WEEE Directive. The product should be taken to a registered establishment for the disposal of electronic equipment.

<!-- figure 1 on pdf page 2 at 0,17-593,60 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 3 | printed page 3 -->

<!-- figure 1 on pdf page 3 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Contents Page | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 4 | printed page 4 -->

### Introduction

The PRO-NDC-1E2K multiplexer is designed to suit the majority of NMEA 0183 systems and provides a web-based configuration tool for setting the device to suit your requirements. The device is a rugged, robust, Type Approved Multiplexer with built-in NMEA 2000 connectivity, high-speed Ethernet streaming of data, flexible configuration, auto-switching and advanced data routing capabilities. The web browser based configuration tool allows full customisation of the PRO-NDC-1E2K, and as it is web based it is compatible across all popular Operating Systems. The PRO-NDC-1E2K supports a direct Ethernet connection to a PC without the need for a specialised Ethernet crossover cable. The NMEA 2000 data can be converted bidirectionally into different formats including NMEA 0183, N2K ASCII and N2K Actisense (proprietary formats) and NGT Actisense (compatible with our NGT/NGX products). The Ethernet Port enables all NMEA data to be sent and received at high speed to connected networks.

Installation Warnings All warnings and notices must be followed to ensure the correct operation of the PRO-NDC-1E2K. Incorrect installation may invalidate the guarantee. It is highly recommended that all of the installation instructions are read before commencing the installation. There are important warnings and notes throughout the manual that should be considered before the installation is attempted.

Warning 1: Accuracy The Actisense PRO-NDC-1E2K is designed to accurately transfer data from input to output. The PRO-NDC-1E2K uses the sentence checksum (if available) to remove incomplete and corrupted data, however, the accuracy of the data fields in a valid sentence still remains the responsibility of the NMEA Talker that generated the data.

Warning 2: Installation and Operation This product must be installed and operated in accordance with the instructions provided. Failure to do so could result in personal injury, damage to your boat and/or poor product performance. The PRO-NDC-1E2K should only be used as an aid to vessel monitoring, control or navigation and should not be used as a replacement for traditional aids and techniques.

Warning 3: Installation Code of Practice When wiring the power supply to the PRO-NDC-1E2K ensure the isolation switch is off. Wiring the PRO-NCD-1E2K while the connection is live may damage the PRO-NDC-1E2K and is in breach of the guarantee. Any connection to a battery or power supply must meet the mandatory safety requirements that may be imposed by local regulatory agencies. All wiring should be in accordance with the requirements of the NMEA 0400 installation specification.

Warning 4: Mounting Requirements Select a flat location to mount the PRO-NDC-1E2K. Mounting on a contoured surface may cause damage to the case. Do not mount the PRO-NDC-1E2K while the device is powered, or the cable harness is connected. Note that the connectors are pluggable for easy disconnection when mounting or removing the PRO-NDC-1E2K.

Software Updates The PRO-NDC-1E2K units have built-in firmware which is held in flash memory, allowing quick and easy upgrades Via the Web browser configuration tool or the latest Actisense Toolkit. It is highly recommended that the firmware is kept up to date in the PRO-NDC-1E2K.

The current PRO-NDC-1E2K firmware version can be viewed on the configuration tool ‘Home’ page, in the ‘Main Application’ section. Details of the latest PRO-NDC-1E2K firmware version can be viewed on the Actisense website’s PRO-NDC-1E2K ‘Downloads’ page.

<!-- figure 1 on pdf page 4 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Introduction | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 5 | printed page 5 -->

## Features

| • | Type-Approved (RINA) |
| --- | --- |
| • | 5x Configurable Opto-isolated inputs. |
| • | 2x Configurable ISO-Drive™ isolated outputs. |
| • | 1x Bi-directional, configurable, isolated serial port. |
| • | 1x Bi-Directional NMEA 2000 Connection (M12 Male A Coded) |
| • | Automatic baud rate matching on inputs |
| • | Advanced data filtering/routing. |
| • | Free firmware updates making the device “future-proof” |
| • | Diagnostic LED’s on all inputs and outputs. |
| • | Bi-colour status LED. |
| • | Panel and DIN rail mountable with DIN kit. |
| • | Using the configuration tool, each NMEA 0183 output can be configured to communicate at independent baud rates. |
| • | Data statistics and load indication via web tool. |
| • | Designed for 12 and 24 Volt supply. |
| • | Pluggable connector system supports both screw and screwless terminals. |
| • | Double Galvanic isolation between all inputs and outputs. Galvanic isolation to battery supply. |

## NMEA wire colour coding

The wire colours used in this manual are in accordance with the NMEA 0183 specification (v.4.10, June 2014) and are for illustration purposes only. Please ensure you check the wiring colours given in the installation instructions for any devices you wish to interface with the PRO-MUX-2. Not all manufacturers follow this standard colour coding which can lead to confusion.

Currently, the specified NMEA0183 signal colour coding for individual wires is as follows:

Talker A - White Talker B - Brown Listener A - Yellow Listener B - Green

<!-- figure 1 on pdf page 5 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Features | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 6 | printed page 6 -->

## PRO-NDC-1E2K Overview

## PRO-NDC-1E2K Connections Terminals

The PRO-NDC-1E2K comes supplied with high quality 2-way and 3-way rising clamp connectors which are tightened with screws. Screwless spring-loaded connectors are also available as a optional extra and are available via your distributor.

## Power Supply Connections

The PRO-NDC-1E2K requires a power source providing between 10 to 35 Volts DC. The PRO-NDC-1E2K “+” terminal should be connected to the vessel power supply “+” terminal via the correctly rated fuse (in accordance with the NMEA 0400

| installation standard). | -ve |
| --- | --- |
| The PRO-NDC-1E2K “-” terminal should be connected to |  |
| the vessels DC ground plate. |  |
| The input supply connection has continuous reverse |  |
| polarity and ESD protection. | +ve |

Red and Black wires are shown here as they are the most common designation for power and ground.

<!-- figure 1 on pdf page 6 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: PRO-NDC-1E2K Overview | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 6 at 72,120-519,482 pt | caption: none | text-layer labels: none | nearby labels: PRO-NDC-1E2K Connections Terminals | OCR below floor, text not used (26/68 words >= 60, mean confidence 52) -->

<!-- figure 3 on pdf page 6 at 339,597-574,784 pt | caption: none | text-layer labels: - ve | + ve | OCR below floor, text not used (1/8 words >= 60, mean confidence 41) -->

<!-- pdf page 7 | printed page 7 -->

## Standard Serial Port Connections

The PRO-NDC-1E2K serial port connector allows a serial device/adapter to be connected easily. The Standard RS-232 wiring designation is as shown below; Connect the Tx (pin 3) terminal from your serial

| device to the “IN” terminal | Rx (pin2) |
| --- | --- |
| Connect the Rx (pin 2) terminal from your serial |  |
| device to the “OUT” terminal | GND (pin 5) |
| Connect the GND (pin 5) terminal from your |  |
| serial device to the “COM” terminal | Tx (pin3) |
| N.B Wire colours may vary between 3rd party cables/adapters |  |
| (Pin numbers refer to a standard DB9 connector ) |  |

## USB - Serial Port Connections

Should you require to connect your PRO-NDC-1 to a PC via a USB connection, Actisense have provided a way to achieve this using our USBKIT-PRO (Universal Serial adaptor) which contains a USB-SERIAL converter with the necessary Rx/Tx and GND connections.

## Ethernet Connection

An Ethernet port is provided as a means of correctly configuring your PRO-NDC-1E2K as well as providing high speed data streaming via the data servers. Use either a standard Ethernet patch cable with an RJ45 plug to connect directly to a PC. Alternatively, the PRO-NDC-1E2K can be connected to an Ethernet switch.

Insert the RJ45 plug into the PRO-NDC-1E2K “Ethernet” terminal until a click is heard. To remove the RJ45 plug, push down on the locking clip and gently pull the cable away from the “Ethernet” terminal.

## RF Ground Connection

| • | The PRO-NDC-1E2K must be properly grounded using the grounding stud provided. |
| --- | --- |
| • | This connection should be made using a robust crimped connection if possible and routed back to the vessel’s ‘boat’ ground. |

<!-- figure 1 on pdf page 7 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Standard Serial Port Connections | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 7 at 299,82-557,266 pt | caption: none | text-layer labels: Rx (pin2) | GND (pin 5) | nearby labels: Tx (pin3) | OCR: no legible text (0/6 words >= 60, mean confidence 28) -->

<!-- figure 3 on pdf page 7 at 380,434-557,564 pt | caption: none | text-layer labels: none | OCR below floor, text not used (1/5 words >= 60, mean confidence 32) -->

<!-- figure 4 on pdf page 7 at 380,612-557,775 pt | caption: none | text-layer labels: none | OCR below floor, text not used (2/9 words >= 60, mean confidence 27) -->

<!-- pdf page 8 | printed page 8 -->

## NMEA 2000 Connection

- An NMEA 2000 M12 Male Connector is available for connecting the PRO-NDC-1E2K to the NMEA 2000 bus.
- Connect the M12 port to an NMEA 2000 drop cable (max 6m in length), ensuring the key lines up. Hand tighten until connector is mated.

## NMEA 0183 Talker and Listener Designations

- The NMEA have updated the NMEA 0183 specifications to ensure a consistent naming convention is used for labelling ports. The designation follows the same rules as used for Rx and Tx labelling but uses the terminology “Talker” and “Listener” instead.

| • | The Input / Receiving (Rx) port will be labelled as a LISTENER port. |
| --- | --- |
| • | The Output / Transmitting(Tx) port will be labelled as a TALKER port. |

## NMEA “Talker” Input Connections

| • | The PRO-NDC-1E2K has 5 input connections, labelled IN-1 to IN-5. |
| --- | --- |
| • | Inputs are labelled ‘A’ and ‘B’ in line with the NMEA specification for labelling NMEA0183 signal pairs. |
| • | If your “talker” follows the NMEA wire colour convention, the wires should be coloured as follows: |
| • | TALKER ‘A’/+ : WHITE |
| • | TALKER ‘B’/- : BROWN |
| • | If your wire colours do not follow the NMEA convention, you will need to consult your device manual and find which wire colours correspond to ‘A’/+ and ‘B’/- and attach accordingly. |
| • | If your “talker” device has only ‘A’ and ‘GND’ output wires, connect the ‘GND’ wire to ‘B’/-. |

## NMEA “Listener” Output Connections

| • | The PRO-NDC-1E2K has 2 output connections, labelled OUT-1 & OUT-2. |
| --- | --- |
| • | Outputs are labelled ‘A’ and ‘B’ in line with the NMEA specification for labelling NMEA0183 signal pairs. |
| • | If your “listener” follows the NMEA wire colour convention, the wires should be coloured as follows: |
| • | LISTENER ‘A’/+ : YELLOW |
| • | LISTENER ‘B’/- : GREEN |
| • | If your wire colours do not follow the NMEA convention, you will need to consult your device manual and find which wire colours correspond to ‘A’/+ and ‘B’/- and attach accordingly. |
| • | The shield from each listener should be connected to the ‘GND’ connector on the output terminal. Note: Shield should only be connected at the Talker end. |

<!-- figure 1 on pdf page 8 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: NMEA 2000 Connection | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 8 at 378,309-557,473 pt | caption: none | text-layer labels: none | OCR below floor, text not used (2/12 words >= 60, mean confidence 34) -->

<!-- figure 3 on pdf page 8 at 409,600-555,729 pt | caption: none | text-layer labels: none | OCR below floor, text not used (2/7 words >= 60, mean confidence 35) -->

<!-- pdf page 9 | printed page 9 -->

## Web Browser Configuration

- The web-based configuration tool for the PRO-NDC-1E2K is built in, and can be accessed using the ethernet configuration port (see page 7).
- As it is web-based, the configuration tool is compatible with all popular web browsers and operating systems.
- NOTE: An internet connection is not required to access the configuration tool.

## Standard Ethernet Networks

- If the PRO-NDC-1E2K is connected to an ethernet network containing both DHCP and DNS servers, launch any of the popular web browsers.
- Replacing ‘xxxxxx’ with the serial number of your PRO-NDC-1E2K, type the following command into the address bar: http://prondc-xxxxxx
- The following web-page will now be displayed allowing configuration of the PRO-NDC-1E2K:

## Direct connection or basic ethernet networks

- If the PRO-NDC-1E2K is connected directly to a PC, or the ethernet network does not have a DHCP server, the PRO-NDC-1E2K will communicate using the auto-IP by default.
- A standard Ethernet cable can be used for the connection to your PC. The PRO-NDC-1E2K will automatically detect this. You do not require a cross-over cable.
- The auto-IP process can take up to 60 seconds to complete.
- The PC’s ‘Local Area Connection’ must also be set-up to use auto-IP in order to communicate on this network. Most PC’s are set-up to do this by default. If needed, instructions on how to do this using Windows 10 are detailed overleaf (other Windows operating systems will be similar). NOTE: Administrator privileges are required to carry out these modifications.

<!-- figure 1 on pdf page 9 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Web Browser Configuration | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 9 at 33,309-559,585 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 14/15 words >= 60, mean confidence 89) -->
Actisense
PRO-NDC-1E2K
Information
Status
Actisense-i
Settings
2024 Active Research Limited. All rights reserved. www.actisense.com
<!-- end of figure 2 -->

<!-- pdf page 10 | printed page 10 -->

- Once the PC and PRO-NDC-1E2K are using the same IP address range, launch any popular web browser.
- Replacing ‘xxxxxx’ below with the serial number of your PRO-NDC-1E2K, type in the following command into the address bar: http://prondc-xxxxxx
- The web-page shown above will now be displayed allowing configuration of the PRO-NDC- 1E2K.

## Configuring ‘Local Area Connection’

Search for ‘Network Status’ on your PC and open the ‘Network Status’ menu

In the ‘Network Status’ menu, under ‘Advanced Network Settings’, select ‘Change Adapter Options’

‘Right-click’ on your ‘Local Connection’ and select ‘Properties’;
- Select ‘Internet Protocol Version 4(TCP/IPv4)’ and leave the box on the RHS checked.
- Click on ‘Properties’

<!-- figure 1 on pdf page 10 at 0,17-593,60 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 10 at 36,218-249,273 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
Best match
Network status
System settings
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 10 at 38,317-320,386 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/15 words >= 60, mean confidence 88) -->
Advanced network settings
Change adapter options
View network adapters and change connection settings.
<!-- end of figure 3 -->

<!-- figure 4 on pdf page 10 at 38,475-213,624 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/21 words >= 60, mean confidence 77) -->
Local Area Connection
Realtek PC
Disable
Status
Diagnose
9
Bridge Connections
Create Shortcut
Delete
Rename
Properties
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 10 at 318,475-536,758 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 65/81 words >= 60, mean confidence 81) -->
Local Area Connection Properties
Networking
Connect using
Realtek PCle GBE Family Controller
This connection uses the following items
Client for Microsoft Networks
fe
and Printer Sharing for Microsoft Networks
Packet Scheduler
O Microsoft Network Adapter Protocol
Microsoft LLDP Protocol Driver
Intemet Protocol Version 6
Properties
Uninstall
Description
Transmission Control Protocol/Intemet Protocol. The default
wide area network protocol that provides communication
across diverse interconnected networks.
OK
<!-- end of figure 5 -->

<!-- pdf page 11 | printed page 11 -->

## Configuring ‘Local Area Connection’ (cont’d)

Under the ‘General’ tab in ‘Properties’ ensure:
- ‘Obtain an IP address automatically’ is selected.
- ‘Obtain DNS server address automatically’ is selected. Under the ‘Alternate Configuration’ tab make sure that:
- ‘Automatic private IP address’ is selected
- Click ‘OK’ to accept these changes, and close the ‘local connections window’

## Setting a Static IP

A static IP address can be assigned to the PRO-NDC-1E2K, meaning that the IP address will not change. Unlike DHCP where the IP address will be assigned by the host and can change, once a static IP address is set, this will always be the address of the device until it is manually changed or switched back to dynamic.

Please be aware that setting a static IP address may require you to login and change settings on your router, particularly if it utilises DHCP as default. Only change settings in your network/router if you feel confident in doing so, as misconfiguration can cause a number of issues.

Ensure you make note of the IP address you assign, as you cannot recover the device if the IP address is forgotten and you are unable to perform an arp -a network scan or log into the router to locate the device again.

## Password and Device Recovery

The device will be shipped with a unique password which can be found on the label, located on the side of the product. To log into the device and make changes to the configuration, this password is required, along with the username of ‘admin’. This password can be changed, should you wish.

If the password is lost or forgotten, then the device can be reset and it will default back to the original password.

<!-- figure 1 on pdf page 11 at 0,17-593,60 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 11 at 33,223-261,497 pt | caption: none | text-layer labels: none | nearby labels: Setting a Static IP | OCR text follows (tesseract, unverified; 67/77 words >= 60, mean confidence 87) -->
Internet Protocol Version 4 (TCP/IPv4) Properties
General
Alternative Configuration
You can get IP settings assigned automatically if your network supports
this capability, Otherwise, you need to ask your network administrator
for the appropriate IP settings.
Obtain an IP address automatically
the following IP address:
Subnet mask:
Default
Obtain DNS server address automatically
the following DNS server addresses:
Preferred DNS
er
Alternative DNS server:
Validate settings upon exit
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 11 at 294,223-521,497 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 51/54 words >= 60, mean confidence 90) -->
Internet Protocol Version 4 (TCP/IPv4) Properties
General Alternative Configuration
If this computer is used on more than one network, enter the alternative
IP settings below.
Automatic private IP address
configured
IP address:
Subnet mask:
Default gatey
Preferred DNS server:
Preferred WINS server
Alternative WIP
er:
Validate settings, if changed, upon exit
<!-- end of figure 3 -->

<!-- pdf page 12 | printed page 12 -->

## Troubleshooting Guide

First level PRO-NDC-1E2K diagnostics / fault finding can be performed by observing the LEDs. The normal behaviour of the PRO-NDC-1E2K LEDs is described on the table below. If the LEDs are not behaving as expected, this will indicate a fault in either the device connected to the PRO-NDC-1E2K, the wiring/connections, or the PRO-NDC-1E2K itself. Some common checks to perform on all terminals of the PRO-NDC-1E2K if the correct LED behaviour is not displayed:

| • | Connectors are fully inserted |
| --- | --- |
| • | All pins of the connector are in the correct location (not overlapping into another port position) |
| • | Wires are terminated firmly and correctly (check polarity) |

| LED | Colour | State | Description | User action |
| --- | --- | --- | --- | --- |
| PWR | Blue Green | Pulsing Flashing | Indicates presence of power Data available on input indicated by LED. | None required No action required |
| IN (INCLUDING |  |  |  |  |
| ‘SERIAL IN') | - | Off | No data available on this input or autobaud detection in progress (up to 20 seconds) Flashes at a rate determined by baud rate | Check if connected Talker is sending data. If it is, review configuration. |
| OUT (INCLUDING | Orange | Flashing/ solid | and data length. If available bandwidth is | None required |
| ‘SERIAL OUT’) | Red Yellow | Flashing / solid Flashing / solid | nearly full, LED may appear solid instead of flashing Buffer Full – Overload condition, sentences are being dropped. Warning, buffer is filling. Duplicate deletion is     Review configuration to understand the managing to maintain output capacity by | Use a web browser to review configuration and correct overload condition. required rates of sentences which is |
| STATUS | Green - Green | Flashing / solid Off Flashing On | deleting older copies of sentences Normal operation. No data issues. No data passing through outputs. Either no input data, or if IN LED is active it means all data is blocked. Data activity on the Ethernet port Indicates line speed at 100Mbps | acceptable to any connected device No action required Check if the connected Talker is sending data. If it is, review configuration. No action required |
| Ethernet | Yellow - | Off Off | Indicates line speed at 10Mbps No data available Indicates data is being received from the         Confirm there is another device transmitting | No action required Check that the Ethernet network is operational. |
| NMEA2000 - RX | Green | Flashing | NMEA2000 bus Indicates data is being transmitted on the         Confirm there are at least two NMEA2000 | on the NMEA2000 bus |
| NMEA2000 - TX | Amber | Flashing | NMEA2000 bus | devices present on the bus |
| PWR and |  |  |  |  |
| Power = blue   Power = on (solid) |  |  | Critical HW Error Both Power & Status LEDs          Return to manufacturer if this persists after a |  |
| STATUS |  |  |  |  |
| Status = red   Status = on (solid)                     are solid |  |  |  | power reset |
| (Combined) |  |  |  |  |

<!-- figure 1 on pdf page 12 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Troubleshooting Guide | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 13 | printed page 13 -->

<!-- sub/superscripts on this page (from font sizes): IsoDrive^TM -->

## Technical Specification

Power Supply

| Input supply voltage | 9 to 35 V DC |
| --- | --- |
| Input supply current | 150mA max @ 12V DC (all outputs @ full drive into 100 ohm loads) |
| Input protection | Continuous reverse polarity, transient overvoltage and ESD protection |
| Power indicator | LED, Blue - indicates unit is functioning correctly |
| Input Supply connector | Pluggable 2-way screw terminal, 5.08mm pitch (12 to 30 AWG) |
| NMEA 0183 Port - Listener & Talker |  |
| Number of Listener / Input Ports 5 isolated NMEA 0183 Listeners |  |
| Number of Talker / Output Ports 2 isolated NMEA 0183 Talkers | Fully NMEA 0183, RS422 & RS232 compatible. RS485 Listener |
| Compatibility | compatible |
| Speed / baud rate | 4800 to 38400 bps |
| Talker Output Voltage Drive | >= 2.2V (differential) into 100 ohm |
| Talker Output Current Drive | 20 mA maximum per output |
| Talker Output Protection | Short circuit and ESD |
| Talker Data Indicator | LED, Orange (Flashes with data rate) |
| Listener Input Voltage | -15 V to +15 V continuous, -35 V to +35 V short term (< 1 second) |
| Tolerance |  |
| Listener Input Protection | Current limited, overdrive protection to 40 VDC and ESD protection |
| Listener Data Indicator | LED, Green (Flashes with data rate) |
| Connectors | Pluggable 2/3 way screw terminals, 5.08mm pitch (12 to 30 AWG) |
| Serial Port |  |
| Compatibility | RS422 & RS232 compatible. RS485 Listener compatible |
| Speed / baud rate | 115200 bps |
| Output voltage drive | >= 2.1V (differential) into 100 ohm |
| Output current drive | 20 mA max. |
| Output protection | Short circuit and ESD |
| Input voltage tolerance | -15 V to +15 V continuous, -35 V to +35 V short term (< 1 second) |
| Input protection | Current limited, overdrive protection to 40 VDC and ESD protection |
| Data Indicators | LED's: Green = Receive, Orange = Transmit |
| Connectors | Pluggable 3-way screw terminals, 5.08mm pitch (12 to 30 AWG) |
| Ethernet Port |  |
| Host interface | 10/100BaseT, automatic polarity detection TCP/IP for configuration and firmware updating |
| Supported protocols | TCP/IP and UDP for NMEA 0183 comms |
| Connector | RJ45 |
| Indicators | Green - Link, Yellow - 100 Mbps |
| NMEA 2000 Port |  |
| Compatibility | NMEA 2000 Certification Pending |
| Speed / baud rate | 250 kbps |
| Connectivity | M12 male (A-coded) connector |
| Isolation |  |
| NMEA 0183 Listener | Uses IsoDrive^TM, Hi-Pot tested to 1000V |
| NMEA 0183 Talker | Uses IsoDrive^TM, Hi-Pot tested to 1000V |
| Serial Port | Uses IsoDrive^TM, Hi-Pot tested to 1000V |
| Ethernet Port | 2kv for 60s |
| NMEA 2000 Port | OPTO-Isolated, Hi-Pot tested to 1000V |

Mechanical

<!-- figure 1 on pdf page 13 at 0,17-593,60 pt | caption: none | text-layer labels: none | nearby labels: Technical Specification | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- pdf page 14 | printed page 14 -->

| Housing Material | 316 Stainless Steel |
| --- | --- |
| Dimensions | 139mm (W) x 98mm (H) x 26mm (D) |
| Weight | 360g |
| Mounting | Bulkhead mount or DIN rail mount (DIN kit 1) |
| Approvals and Certifications |  |
| EMC | IEC 60945:2002-08, DNVGL-CG-0339:2019 & IACS UR E10 Rev7 |
| Compass Safe Distance | 300mm |
| Type Approval Certificate | RINA |
| Operating Temperature | -25 to +70°C |
| Storage Temperature | -40 to +85°C |
| Relative Humidity (RH) | 95% @ 55°C |
| Environmental Protection | IP40 |
| Guarantee | 3 years (5 Years if registered) |

## PRO-NDC-1E2K Dimensions

<!-- figure 1 on pdf page 14 at 0,17-593,60 pt | caption: none; nearest centred text below: "316 Stainless Steel 139mm (W) x 98mm (H) x 26mm (D) 360g" | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 14 at 332,70-516,261 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 14 at 33,345-526,712 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 17/29 words >= 60, mean confidence 63) -->
139.3mm
124.3mm
27.1mm
109.3mm
15mm
25m,
Ethernet Port
M4 Earthing Stud
M12 NMEA 2000 connector
139.36mm
PRO-NDC-1E
<!-- end of figure 3 -->

<!-- pdf page 15 | printed page 15 -->

## Technical support and the returns procedure

The first point of contact for all technical enquiries should be the vendor / supplier where the device was originally purchased.

All warnings in this manual must be adhered to and installation instructions followed prior to any support requests.

If the troubleshooting guide or the supplier are not able to help resolve the problem and an error persists, please visit the Actisense help centre at www.actisense.com/support where you will find useful articles to aid further troubleshooting in our FAQ’s and Knowledge Base.

You will also find a link to the support centre where you can register and raise a support ticket.

<!-- figure 1 on pdf page 15 at 0,17-593,60 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
Actisense
<!-- end of figure 1 -->
