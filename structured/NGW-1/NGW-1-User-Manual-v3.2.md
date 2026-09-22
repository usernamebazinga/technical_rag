# NMEA Conversion Gateway

<!-- source: sources/NGW-1/NGW-1-User-Manual-v3.2.pdf | extraction: extracted/NGW-1/NGW-1-User-Manual-v3.2.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: no ToUnicode map in ArialMT, AvenirLT-Light; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1-14 checked against the rendered page) -->

<!-- pdf page 1 -->

NMEA Conversion Gateway Install/User Manual   Issue 3.2

For all variants: NGW-1-ISO NGW-1-ISO-AIS NGW-1-STNG NGW-1-USB

## Please also download our Actisense Toolkit software.

This powerful software allows you to configure and update your NGW-1 while it is connected to your PC. (NGW-1 firmware version 2.5 and above). Provided free of charge, Actisense Toolkit interfaces with not only the NGW-1, but also allows configuring and updating of the Actisense EMU-1, PRO-BUF-1 & PRO- MUX-1. With the addition on an Actisense NGT-1 connected between your NMEA2000 network and your PC you will not only have the facility to remotely configure an NGW-1, but also gain full visibility of any NMEA2000 certified devices connected to your network, making the NGT-1 an invaluable diagnostic tool.

### Download ToolKit Here

<!-- figure 1 on pdf page 1 at 33,523-559,652 pt | caption: none | text-layer labels: none | OCR: no legible text (0/9 words >= 60, mean confidence 35) -->

<!-- figure 2 on pdf page 1 at 222,724-557,806 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 78) -->
Actisense
Award Winning NMEA
<!-- end of figure 2 -->

<!-- pdf page 2 | printed page 2 | header: NMEA Conversion Gateway - NGW-1 -->

## NMEA Conversion Gateway - NGW-1

Contents

<!-- pdf page 3 | printed page 3 | header: NMEA Conversion Gateway - NGW-1 -->

### Important Notices

<!-- omitted: "Trademarks and registered trademarks" (pdf page 3; 2 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair use statement" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Technical accuracy" (pdf page 3; 3 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
#### Product registration

Please register your product via the online form on www.actisense.com.

Your product package includes a unit serial number. Your registration will assist Actisense Support to link your product to your details, simplifying any future assistance you may require.

#### Product Guarantee

This product comes with a three year ‘return to base’ guarantee. If you suspect that the unit is faulty please refer to the Troubleshooting Guide section of this document.

It is a requirement of the guarantee that all installations of electronic equipment follow the NMEA 0400 specification. Any connection to a battery or power supply must meet the mandatory essential safety requirements that may be imposed by local regulatory agencies.

Actisense products are intended for use in a marine environment, primarily for below deck use. If a product is to be used in a more severe environment, such use may be considered misuse under the Active Research Limited guarantee.

#### Product installation and operation

This product must be installed and operated in accordance with the instructions provided. Failure to do so could result in personal injury, damage to your boat and/or poor product performance.

#### Product disposal

Please dispose of this product in accordance with the WEEE Directive. The product should be taken to a registered establishment for the disposal of electronic equipment.

<!-- pdf page 4 | printed page 4 | header: NMEA Conversion Gateway - NGW-1 -->

### About

The Actisense NGW-1 NMEA 2000 Gateway is the easiest way to link between a boats old and new data networks. The NGW-1 can convert NMEA 0183 data into NMEA 2000 data and vice-versa.

The NGW-1 is available to purchase in a variety of options: NGW-1-ISO is the standard option. With an opto-isolated input and ISO-Drive output for direct NMEA 0183 device bi-directional connection.

NGW-1-ISO-AIS is the NMEA 0183 AIS option that enables the conversion of NMEA 0183 AIS data to its equivalent in NMEA 2000. This provides an ‘out of the box’ solution for quick installation with no configuration required.

NGW-1-USB is the NMEA 0183 USB (1.1 and 2.0) interface for bi-directional connection to a PC for use with NMEA 0183 software.

Every option of the NGW-1 is available with the SeaTalkNG to NMEA 2000 adaptor Cable - STNG-A06045. The SeaTalkNG to NMEA 2000® adaptor cable (STNG-A06045) is not available as a standalone product and must be bought as part of a bundle.

Please go to the ‘Downloads’ page of the Actisense website to see the up to date list of conversions the various configurations can handle.

The Actisense NMEA Reader software utility allows the NGW-1 user to view and understand (in detail) the translated NMEA 0183 sentences output by an NGW-1 directly.

### Firmware Updates

The NGW-1 units have built-in firmware which is held in ‘flash’ memory, allowing quick and easy upgrades using the latest NGW-1 ActiPatch.

Actisense recommends that the NGW-1 firmware is kept up to date. The firmware version currently installed on the NGW-1 can be checked on any NMEA 2000 MFD capable of displaying all devices that are active on the NMEA 2000 network. Simply check this number against the latest version number on in the downloads section of the Actisense website.

### Powering the NGW-1

ISO Variants: All ISO variants of the NGW-1 receive their power supply when connected to a correctly powered NMEA 2000 backbone. The backbone must also be correctly terminated to allow connected devices to communicate. Refer to the “Connecting to an NMEA 2000 Network” section for more information.

USB Variants: All USB variants will be powered by the PC/laptop USB connection once the USB drivers have been successfully installed. Depending on the settings of the PC/laptop that the NGW-1 is connected to, the latest Actisense USB drivers will install automatically from Windows update. If this does not happen, the same USB driver files are available from the NGW-1 downloads web page.

<!-- pdf page 5 | printed page 5 | header: NMEA Conversion Gateway - NGW-1 -->

### Connecting to an NMEA 2000 Network

The illustration below provides an example of the minimum requirements for an NMEA 2000 network. If an NMEA 2000 network is not currently installed, Actisense has a variety of Starter Kits available.

The horizontal cable illustrating the backbone is not always needed in reality as a backbone can be formed by simply connecting T-pieces directly to each other. The cable connecting a device to a T-piece must not exceed 6 metres as defined in the NMEA 2000 specification:

## Instrument Drop

## NMEA

## Terminator

## Power T

## NMEA

## Device

#### NMEA 2000 Pin Out

The diagram below illustrates the standard wiring colours used by all NMEA 2000 devices (like the NGW-1):

NET LO

| NMEA 2000 | NET HI Shield |
| --- | --- |
| Network | NET COM NET SUP |

### Connecting to a SeaTalkNG Network

| NMEA 2000 | Wire Colour | PCB Label |
| --- | --- | --- |
| Shield | Shield/Screen | SHIELD |
| Net Low | Blue | NET LO |
| Net High | White | NET HI |
| Net Common | Black | NET COM |
| Net Supply | Red | NET SUP |

Raymarine’s SeaTalkNG network uses exactly the same data as a standard NMEA 2000 network. The only difference is the physical network connections. To connect any standard NMEA 2000 device (like the NGW-1) to an STNG network, simply use an NMEA 2000 to STNG adapter cable (product code: STNG-A06045) between the device and the STNG network.

<!-- figure 1 on pdf page 5 at 38,206-543,360 pt | caption: none | text-layer labels: Power T | Instrument Drop | NMEA 2000 Device | NMEA 0183 Network | nearby labels: T-Piece | Backbone | Terminator | OCR text follows (tesseract, unverified; 5/7 words >= 60, mean confidence 61) -->
e
e
e
e
1.
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 5 at 349,434-392,564 pt | caption: none | text-layer labels: none | nearby labels: NMEA 2000 | Shield | Net Low | Blue | Net High | White | Net Common | Black | Net Supply | Red | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 5 at 418,434-483,564 pt | caption: none | text-layer labels: none | nearby labels: Wire Colour | Shield/Screen | SHIELD | Blue | NET LO | White | NET HI | Black | Red | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 5 at 33,444-292,564 pt | caption: none | text-layer labels: NMEA 2000 Network | NMEA 2000 Drop Cable | NET LO NET HI Shield NET COM NET SUP | nearby labels: NGW-1 | OCR below floor, text not used (5/16 words >= 60, mean confidence 45) -->

<!-- pdf page 6 | printed page 6 | header: NMEA Conversion Gateway - NGW-1 -->

### Connecting to NMEA 0183 Devices

The diagram and table below illustrate how to connect the individual wires from any ISO variant NGW-1 to the Talker/Listener terminals of an NMEA 0183 device.

NGW-1                                               NMEA 0183 DEVICE Arrows indicate direction of data flow

B/- / GND NMEA A/+ / TX Talker/Out B/- / GND NMEA A/+ / RX Listener/In Do not connect

### Connecting to a PC/laptop

| Label | Wire Colour | NMEA 0183 device |
| --- | --- | --- |
| IN B / - | Black | Talker OUT B / - / GND |
| IN A / + | Red | Talker OUT A / + / Data |

Listener OUT B / - / OUT B / -   Blue GND

Listener OUT A / + / OUT A / +   White Data

ISO GND     Shield / Screen   Not Connected

The diagram and table below illustrate how to connect the individual wires from any ISO variant NGW-1 to an RS232 serial cable (such as the Actisense DB9F). If the PC/laptop does not have a serial port, a USB- to-Serial converter will also be needed (such as the Actisense USBKIT).

| Label | Wire Colour | Computer / RS232 |
| --- | --- | --- |
| IN B / - | Black | GND (Pin 5) |
| IN A / + | Red | TX (Pin 3) |
| OUT B / - | Blue | GND (Pin 5) |
| OUT A / + | White | RX (Pin 2) |
| ISO GND | Shield / Screen | Not Connected |

NGW-1 Arrows indicate          COMPUTER direction of data flow TX Pin 3

GND Pin 5 Do not connect

Alternatively, for total piece-of-mind the flexible Actisense USG-2 can connect an NGW-1-ISO to a computer using USB. It can also be used as an NMEA 0183 diagnostic tool with NMEA Reader.

<!-- figure 1 on pdf page 6 at 294,429-545,537 pt | caption: none | text-layer labels: Arrows indicate direction of data flow | COMPUTER | TX Pin 3 | RX PC 9 PIN Pin 2 RS232 Port | Do not connect | GND Pin 5 | nearby labels: NGW-1 | OCR below floor, text not used (4/20 words >= 60, mean confidence 46) -->

<!-- pdf page 7 | printed page 7 | header: NMEA Conversion Gateway - NGW-1 -->

### LED Behaviour and Troubleshooting

There are 2 LEDs inside the NGW-1, one on the NMEA 0183 side, one on the NMEA 2000 side. On start up, these LEDs will flash alternately and very quickly for 2 seconds.

The primary function of the NGW-1 NMEA 0183 LED is to indicate reception of a valid NMEA 0183 sentence. The NMEA 2000 LEDs main function is to indicate reception of a PGN on the NGW-1 conversion list. It is normal for the NMEA 0183 LED to flash faster than the NMEA 2000 LED due to the smaller bandwidth available to NMEA 0183.

If the NGW-1 is not receiving any data on either side, both LEDs will flash together every 10 seconds. This could be a result of incorrect wiring, mismatched baud rates or a lack of data available to the NGW-1.

- Consult the video in the Actisense Support Centre for regular LED behaviour and the table below for
- irregular LED behaviour:

| Behaviour | Solution |
| --- | --- |
| USB only: The LEDs do not light | The USB driver has not been installed correctly. |

Check that the NGW-1 is connected to the NMEA 2000 network and that the NMEA 2000 network is operational. The NMEA 2000 LED does not flash when the NMEA 2000 network is Confirm that the PGN messages are available on the network (using an Actisense active NGT-1 or similar device) and that the required PGNs are supported on the latest NGW-1 Conversion List.

The NMEA 0183 LED does not flash Check that the NGW-1 is connected correctly to the NMEA 0183 device and that the when connected to an NMEA 0183 same Baud rate has been set on both devices. Talker

Indicates that the NGW-1 is powered but no data is received from either connection. If Both LEDs flash together, once valid data should be present and converted by the NGW-1 on one or both inputs, refer every 10 seconds to the two rows above.

The LEDs flash alternately very fast Indicates that the NGW-1 has lost its Firmware, please connect the unit to the latest (4 times per second). This sequence NGW-1 Actipatch and re-install the Firmware. repeats continuously

### Technical Support and the Returns Procedure

All installation instructions and any warnings contained in this manual must be followed before contacting Actisense technical support. If the troubleshooting guide did not help resolve the problem and an error persists, please contact Actisense technical support to help trace the issue before considering the return of the product. If Actisense support concludes that the NGW-1 unit should be returned to Actisense a Returns Number will be issued by the support engineer.

The Returns Number must be clearly visible on both the external packaging and any documentation returned with the product. Any returns sent without a Returns Number will incur a delay in being processed and a possible charge.

<!-- pdf page 8 | printed page 8 | header: NMEA Conversion Gateway - NGW-1 -->

### Changing Firmware

#### NGW-1 firmware v2.500 and newer

Switching between AIS and Standard configurations does not require the firmware to be updated, as Actisense Toolkit can help create the exact configuration by enabling or disabling conversions as required. Please refer to Page 9 for details of how to configure an NGW-1 using Actisense Toolkit.

If a new NGW-1 firmware has been released, download the ActiPatch that matches the hardware variant (ISO, USB, STNG) of your NGW-1 from the NGW-1 Download page. For example, if you have an NGW- 1-ISO, both the “NGW-1-ISO (STD) vX.XXX ActiPatch Setup” (defaults to ‘Standard conversions’) and the “NGW-1-ISO-AIS vX.XXX ActiPatch Setup” (defaults to ‘AIS/Full conversions’) can be used to update.

Once the update is complete, if the NGW-1 had previously been configured using Actisense Toolkit it will continue to use that configuration, if not, Actisense Toolkit can be used to create a configuration that exactly matches the conversion requirements.

#### NGW-1 firmware v2.420 and older

Both the ‘Standard conversions’ firmware and ‘AIS conversions’ firmware can be installed into any hardware variant (ISO, USB, STNG) using the corresponding ActiPatch. The firmware has all possible conversions enabled by default, ready to go and NMEA Reader can be used to disable any of those conversions that are not required. For full instructions on how to use NMEA Reader, please refer to the NMEA Reader & EBL Reader User Manual.

If a new NGW-1 firmware has been released or there is a requirement to change between the ‘Standard conversions’ and ‘AIS conversions’ firmware, download the required ActiPatch that matches the NGW-1 hardware variant (ISO, USB, STNG) from the NGW-1 Download page.

For example, if you have an NGW-1-ISO running the ‘Standard conversions’ firmware and wish to change to the ‘AIS conversions’ firmware, download the “NGW-1-ISO-AIS vX.XXX ActiPatch Setup” and use it to update the firmware. To return to the ‘Standard conversions’ firmware, download and use the “NGW-1-ISO (STD) vX.XXX ActiPatch Setup”.

#### Connecting an NGW-1-ISO or NGW-1-STNG to a PC

In order to update firmware or configure the conversions, these are the connection options:

1. The Actisense USBKIT is a quick and low-cost way to connect the NGW-1 to a PC. It can be connected to the NGW-1’s ISO / NMEA cable, or directly to the NGW-1 terminal block inside the case (as long as standard antistatic precautions are observed).

2. If a standard “USB to Serial” adapter cable is already available, this can be plugged in to a ‘D-type’ 9-pin connector (such as the Actisense DB9-F) which is wired to the NGW-1’s ISO / NMEA 0183 cable or directly to the NGW-1 terminal block inside the case instead if that is more convenient (as long as antistatic precautions are observed). Please refer to section “Connecting to a PC/laptop” on page 6 for more details.

3. The most flexible option is the Actisense USG-2 that includes a 4-pin terminal block that the NGW-1’s ISO / NMEA 0183 cable can connect directly to.

The USG-2 offers 1500 volts of isolation on both its input and output, which allows it to be used on any NMEA 0183 device whilst keeping the PC safe from ground loops and ground potential differences. This makes it a true NMEA 0183 diagnostic tool for installers when used with the freely available Actisense NMEA Reader software.

Please note that NGW-1-ISO variants are powered using the NMEA 2000/SeaTalkNG cable, therefore backbone power must be available on the “CAN C” and “CAN S” pins on the NMEA 2000/SeaTalkNG connector before the NGW-1 can operate. NGW-1-USB variants are powered once the latest USB drivers have been successfully downloaded and installed on the connected PC.

<!-- pdf page 9 | printed page 9 | header: NMEA Conversion Gateway - NGW-1 -->

#### Using ActiPatch to update firmware

With the NGW-1 connected to your PC, select the corresponding COM port for your NGW-1 in the “Comms” drop down menu in ActiPatch. Please note that you do not need to select a baud rate as ActiPatch will automatically try many different baud rates. Once bi-directional communication between ActiPatch and the NGW-1 has been achieved, the ‘Program’ button will go green.

Click on the ‘Program’ button to start the update process – the progress bar will indicate the firmware update progress, starting with a red bar and then a green bar. When the installation has completed successfully, the ‘Patch ID’ box and ‘Device ID’ box will contain identical numbers.

### Configuring Using Actisense Toolkit

NGW-1-USB variants can be connected directly to a PC using its USB cable and NGW-1-ISO variants can be connected using one of the options detailed in “Connecting an NGW-1-ISO or NGW-1-STNG to a PC” on page 8. Alternatively, if an Actisense NGT-1-USB or NGT-1-ISO is available, the NGW-1 can be connected to remotely via the NGT-1, greatly increasing the simplicity of the configuration operation.

Run the Actisense Toolkit program, either select the COM Port of the NGW-1 device and its matching baud rate (typically 4800 or 38400 baud) or select the COM port of the NGT-1 device and its matching baud rate (typically 115200 or 230400 baud). Select the NGW-1 device in the “Serial / CAN Device List” and choose the “Load from Device” option under “Device Configuration” section or on the right-click context sensitive menu to load the current NGW-1 configuration and open a new configuration document in Toolkit.

<!-- figure 1 on pdf page 9 at 33,365-557,628 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 90/106 words >= 60, mean confidence 84) -->
uration
COM port Actisense NGT (COM1)
ATC
Baud rate
Status
fresh
Enable Set save
Load from
Nev
Upgrade Downgrade
IP Network Ethernet 2
Logging location
Firmware Firmware
Device
Device
Cont
twork
Comms
Device Firmware
Logging
Device Configuration
Device Function
Serial...
Device Instance
Software ID
Hardware ID
PC Gateway
177174
"1.100, 2.690
[5]"
0x00)
NMEA 0183 Gateway
177047
0 (0x00)
"1.100, 2.660"
Engine Gateway
181260
0 (0x00)
"1.060, 1.015"
“EMU-1 [0]"
NMEA 0183 Gateway
177493
0 (0x00)
"1,100,
hv1.
Upgrade Firmware
Load from Device
Send to Device
Connect to Data server
<!-- end of figure 1 -->

<!-- pdf page 10 | printed page 10 | header: NMEA Conversion Gateway - NGW-1 -->

The NGW-1 configuration document shows every aspect of the configuration such as the NMEA 0183 baud rate, whether the ARL P-Codes are enable/disable and two tabs that detail every possible NMEA 0183 Sentence and NMEA 2000 PGN that can be configured for receive (Rx) and transmit (Tx), plus their “Tx Period” in milliseconds.

Once the various configuration options have been configured as required, the “Estimated NMEA 0183 Transmit Load” bar will indicate whether the configuration will work as expected (when the load is 100% or below) or whether the transmit rates in reality may be lower than requested (when the load is above 100%) due to output overload.

To send the configuration to an NGW-1, select the “Send to Device” option in “Device Configuration” or right-click menu option and choose the NGW-1 device to send it to.

Full details of this configuration process can be found in the “NGW-1 Help” document available from the Actisense Toolkit “User Manual” Help menu.

<!-- figure 1 on pdf page 10 at 79,223-512,604 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 152/158 words >= 60, mean confidence 92) -->
0183 Rx and Tx Sentences NMEA 2000 Rx and Tx PGNs
Rx Tx
Formatter
Name
Tx Period(ms)
AAM
Waypoint Arrival Alarm
1000
M
ABM
Non-Periodic
AIS Addressed binary and safety related message
M
APB
Heading/Track Controller (Autopilot) Sentence
1000
M
BBM
Non-Periodic
AIS Broadcast Binary Message
BWC
Bearing Distance to Waypoint (Great Circle)
1000
BWR
Bearing Distance to Waypoint (Rhumb Line)
1000
DBT
Depth Below Transducer
1000
DPT
Depth
1000
DSC
Digital Selective Calling Information
Non-Periodic
DSE
Expanded Digital Selective Calling
Non-Periodic
DTM
Datum Reference
1000
GGA
Global Positioning System Fix Data
1000
GLL
Geographic Position Latitude/Longitude
1000
GNS
GNSS Fix Data
1000
GRS
GNSS Range Residuals
1000
GSA
GNSS DOP and Active Satellites
4000
GST
GNSS Pseudorange Error Statistics
Non-Periodic
GSV
GNSS Satellites in View
4000
HDG
Heading, Deviation Variation
1000
HDM
1000
Heading, Magnetic
HDT
Heading, True
1000
HSC
Heading Steering Command
1000
MDA
Meteorological Composite
1000
Water Temperature
1000
<!-- end of figure 1 -->

<!-- pdf page 11 | printed page 11 | header: NMEA Conversion Gateway - NGW-1 -->

### Tech Tips from the Actisense Support Team

#### Using the NGW-1 with waypoints

If you want to use the NGW-1 with NMEA 0183 waypoint names, they have to be purely numeric – e.g. a valid waypoint name is “73”, an invalid name is “waypoint 73” in order for the NGW-1 to correctly convert it to NMEA 2000. This is because NMEA 2000 waypoint names can only be numeric (at their lowest level). Converting NMEA 2000 waypoint names to NMEA 0183 is simple as they will automatically use the numeric value defined in NMEA 2000.

#### Multiple sources of NMEA 0183 data

Unfortunately it is not possible in any NMEA 0183 networking situation to connect the output of more than one Talker device to the input of one or more Listeners. To convert data from more than one NMEA 0183 Talker to NMEA 2000 you have two choices:

1. Use a dedicated NGW-1 for each NMEA 0183 Talker device. This solution allows bi-directional sharing of NMEA 0183 data between the NMEA 0183 device and the NMEA 2000 network.

2. Use an NMEA 0183 multiplexer, such as the Actisense NDC-5 to combine the output of the two Talkers. Then use an NGW-1 to convert the output from the NDC-5 to NMEA 2000. Only if the multiplexer has already been purchased is this a good solution as it is very difficult to share data bi-directionally.

We recommend using a dedicated NGW-1 for each device because multiplexing can become complicated when considering bi-directional data and multiple data sources. In addition, the cost of an NDC-5 and an NGW-1 is approximately the same as the cost of four NGW-1’s.

#### NGW-1 Prioritisation of NMEA 2000 Talkers

When there is more than one device of the same type (like a GPS) on the NMEA 2000 network, the NGW-1 will use the data from the highest priority (lowest source address) device on the bus. If the device required to be the primary data source for the NGW-1 claims a lower source address than other devices of the same type, the NGW-1 will convert the data from the preferred device. If however, a secondary device claims a lower source address than the primary data source, there is no direct way to change this.

One possible resolution however is to try changing the “Device Instance” of the secondary device to instance 1, leaving the primary data source as instance 0.

Not all NMEA 2000 device manufacturers support the standard method for changing the Device Instance, however for those that do, NMEA Reader software and an Actisense NGT-1 (we recommend the USB variant for simple PC connections) can be used to quickly change the Device Instance.

The NGT-1 is compatible with a wide range of software. To view a list of software that can be used with the NGT-1, please visit our NGT-1 compatibility page. If using the ISO variant of the NGT-1, please contact the software developer to ensure that they support this option.

<!-- pdf page 12 | printed page 12 | header: NMEA Conversion Gateway - NGW-1 -->

#### Difference between NGW-1 and NGT-1

1. NGT-1: NMEA 2000 PC Interface – allows NMEA 2000 / SeaTalkNG messages to be read by an application and also allows that application to send NMEA 2000 messages back to the network. The NGT-1 does not understand NMEA 0183.

The most common variant is the NGT-1-USB as that is the easiest method of getting NMEA 2000 data to a PC. The NGT-1-ISO is available for customers who do not want USB and the drivers it requires.

An NGT-1 working with NMEA Reader is a very powerful NMEA 2000 network diagnostic tool.

2. NGW-1: NMEA 2000 to NMEA 0183 Gateway – converts between the old and the new NMEA protocols bi-directionally. It cannot be used to transfer NMEA 2000 messages to the PC; the serial port only understands NMEA 0183.

The most common variant is the NGW-1-ISO for direct connection to an NMEA 0183 Talker / Listener device. The NGW-1-USB is available for customers who want an easy method of getting NMEA 0183 data to a PC and an application running on it.

An NGW-1 makes it possible for new and old NMEA devices to share data, bi-directionally.

It is not possible to change an NGW-1 to an NGT-1 or vice versa. Fundamentally, the product name shown on the case determines the expected device behaviour and if these two conflict with each other, the resultant confusion can lead to the device being incorrectly considered faulty.

<!-- pdf page 13 -->

Power Supply (ISO, ISO-AIS & STNG Variants)

| Supply Voltage (NMEA 2000 Port) | 9.5 to 35V DC |
| --- | --- |
| Supply Current (NMEA 2000 Port) | 35mA @ 12V DC, Max 50mA |
| Load Equivalent Number (LEN) | 1 |
| Power Supply (USB Variants) |  |
| Supply Voltage (NMEA 2000 Port) | 9 to 29V DC |
| Supply Current (USB Host Port) | 85mA @ 5V DC |
| Supply Current (NMEA 2000 Port) | 15mA @ 12V DC, Max 50mA |
| Load Equivalent Number (LEN) | 1 |
| NMEA 2000 Port (All Variants) |  |
| Compatibility | Fully NMEA 2000 certified |
| Galvanic Isolation | Refer to ‘ISO port’ or ‘USB port’ |
| Speed / Baud Rate | 250kbps |
| Connectivity | M12 Male (A polarised) connector moulded on cable |
| Cable Length NMEA 2000 | 1.5m |
| Cable Length STNG Adapter | 0.4m (1.9m with NMEA 2000 cable connected) |
| ISO Port (NMEA 0183 port - ISO, ISO-AIS & STNG Variants) |  |
| Compatibility | Full NMEA 0183, RS232 & RS422 compatible. RS485 Listener compatible |
| Galvanic Isolation | 2500V input to ground, 1500V output to ground using ISO-Drive |
| Speed/Baud Rate | 4800 to 115200 Baud |
| Output Voltage Drive | >= 2.1V (differential) into 100Ω |
| Output Current Drive | 20mA max. |
| Output Protection | Short circuit and ESD |
| Input Voltage Tolerance | -15V to +15V continuous -35V to +35V short term (< 1 second) |
| Input Protection | Current limited and overdrive protection to 40VDC |
| Connectivity | 5mm stripped and tinned wire |
| Cable Length | 1.5m |
| USB Port (USB Variant) |  |
| Compatibility | USB 1.1, 2.0 and 3.0 |
| Galvanic Isolation | 2500V input to ground |
| Speed / Baud Rate | 4800 to 230400 Baud |
| Connectivity | Male type A plug moulded onto cable |
| Cable Length | 1.5m |
| Drivers (Latest OS) | MAC OS X, Windows XP, 7, 8 & 10 supplied via the Product Downloads web page |
| Drivers (Legacy OS) | Contact Actisense for full details of the legacy OS versions supported: support@actisense.com |
| Mechanical |  |
| Housing Material Lid | Polycarbonate |
| Housing Material Base | Flame retardent ABS |
| Weight NGW-1-ISO & ISO-AIS | 220g |
| Weight NGW-1-USB | 210g |
| Weight NGW-1-STNG | 260g |
| Approvals and Certifications |  |
| Fully NMEA 2000 Certified |  |
| Meets all IEC 61162-1 & 61162-2 requirements |  |
| Meets all IEC 61162-3 requirements |  |
| EMC | IEC 60945 (sections 9, 10 & 11.2) |
| Environmental Protection | IP42 |
| Operating Temperature | -20°C to +55°C |
| Storage Temperature | -30°C to +70°C |
| Recommended Humidity | 0 - 93% RH |
| Guarantee | 3 years |

<!-- pdf page 14 | printed page 14 | header: NMEA Conversion Gateway - NGW-1 -->

### NGW-1 Product Order Codes

| Product Code | Product Description |
| --- | --- |
| NGW-1-ISO | NMEA 0183 to NMEA 2000 Gateway, standard configuration |
| NGW-1-ISO-AIS | NMEA 0183 to NMEA 2000 Gateway, pre-configured with AIS conversions |
| NGW-1-STNG | NMEA 0183 to SeaTalk NG Gateway |
| NGW-1-USB | NMEA 0183 to NMEA 2000 Gateway with USB, standard configuration |
| STNG-A06045 | SeaTalkNG to NMEA 2000 adaptor cable (drop). Only for purchase with Actisense NMEA 2000 devices |

Active Research Ltd. 21 Harwell Road Poole BH17 0GE Dorset, UK tel: (+44) 01202 746682 email: support@actisense.com ® web: actisense.com

<!-- figure 1 on pdf page 14 at 244,94-559,199 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 14 at 356,607-559,657 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 70) -->
Actisense
NMEA Specialists
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 14 at 258,722-325,772 pt | caption: none | text-layer labels: ® | OCR: no legible text (0/1 words >= 60, mean confidence 48) -->
