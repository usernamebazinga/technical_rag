# NBE100 User's Manual

<!-- source: sources/NBE100/NBE100UM_1.2.pdf | extraction: extracted/NBE100/NBE100UM_1.2.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: SymbolMT is not a standard text face; glyphs "•" on pages 3, 11-12. Verify against the rendered page before trusting or mapping. -->
<!-- font check: no ToUnicode map in Arial-BoldItalicMT, Arial-BoldMT, Arial-ItalicMT, ArialMT, ArialNarrow, ArialNarrow-Bold, Calibri, CourierNewPSMT; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1-16 checked against the rendered page) -->

<!-- pdf page 1 | header: _______________________________________________________ -->

## _______________________________________________________

## NBE100

## Network Bus Extender

## User’s Manual

Revision 1.2

Copyright ©2021 Carling Technologies, Inc.

60 Johnson Ave. Plainville, CT 06062 USA All Rights Reserved

http://www.maretron.com

<!-- figure 1 on pdf page 1 at 180,228-434,466 pt | caption: none | text-layer labels: none | OCR: no legible text (0/10 words >= 60, mean confidence 18) -->

<!-- pdf page 2 | header: _______________________________________________________ -->

## Revision History

Revision                                Description 1.0    Original Document 1.1    Changed Company Information to Carling 1.2    Added PGN Filtering Notes

Table of Contents

## Table of Figures

<!-- figure 1 on pdf page 2 at 377,103-559,166 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 3 | printed page 1 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

## 1 Introduction

Congratulations on your purchase of the Maretron Network Bus Extender. Maretron has designed and built your NBE100 to the highest standards for years of dependable and accurate service.

Maretron's NBE100 (Network Bus Extender) allows you to extend the maximum node count, network trunk length and cumulative drop length of any NMEA 2000® network. The NBE100 solves bus errors and other electrical issues caused by exceeding any of these limitations and makes design of large networks easier. NMEA 2000® networks have a maximum of 50 nodes allowed on a single network, a maximum network trunk length of 200m and a maximum cumulative drop length of 78m. If you have a network that exceeds any of these specifications, you can simply disconnect the network trunk in the middle and connect the ends to the NBE100, along with additional termination resistors. This will split the network into two electrical segments, each of which can have up to 50 nodes, for a total of 100 nodes on the logical network. The NBE100 will transparently route NMEA 2000® messages between the two network segments, making them work as a single logical NMEA 2000® network. Advanced priority-based message routing ensures that higher-priority messages are always prioritized over lower-priority messages, enabling predictable and reliable network operation. For exceptionally large networks, multiple NBE100’s may be used. Enable NBE100’s PGN Filtering Mode to pass only the PGNs you desire.

### 1.1 Firmware Revision

This manual corresponds to NBE100 firmware revision 2.3.1.2

### 1.2 NBE100 Features

The Maretron NBE100 has the following features.

| • | Segments a single large NMEA 2000® network into two smaller electrical segments. |
| --- | --- |
| • | Allows you to exceed the 50 node limitation on a NMEA 2000® network. |
| • | Allows you to exceed the 200m trunk length limitation on a NMEA 2000® network. |
| • | Allows you to exceed the 78m cumulative drop length limitation on a NMEA 2000 ® networks. |
| • | Allows all NMEA 2000® devices to operate as if they were still on a single NMEA 2000® network. |
| • | Priority-based message routing ensures higher-priority messages get through the bus extender first. |
| • | Optically isolates network segments, increasing signal integrity and network reliability. |
| • | Features one user configurable PGN (Parameter Group Number) “Pass filter” per NMEA200® Interface where 32 PGNs per interface can be forwarded from one NMEA2000® Interface to the other. |

<!-- pdf page 4 | printed page 2 | header: _______________________________________________________ -->

## _______________________________________________________

### 1.3 NBE100 Application

The NBE100 can be applied, not only anytime a NMEA 2000® bus needs extending, but also can be used to make only specific communication messaging to be passed between NMEA2000® busses possible. Apply the PGN (Parameter Group Number) Pass Filter and the NBE100 will allow only the desired PGN messages to be passed between the connected NMEA2000® buses. Because NBE100 features a pass filter for each of the two NMEA2000® Interfaces it has, Pass Filters will obtain and forward the specific information messages you desire from one bus onto the other or vice versa. This feature is great for reducing unnecessary traffic but still share data without physically combining busses. The NBE100 allows up to 32 “Pass” PGNs per filter.

For an example of when NBE100 pass filtering is necessary, suppose there is a vessel with two separate NMEA2000® buses. One Bus is for used for “Navigation Devices” and the other bus is used for the vessel’s Distributed Power System. The Distributed Power System has a Time display feature, the Time feature is set manually however, has the ability to update it’s Time via NMEA2000® message. Because the Distributed Power System’s NMEA2000® network does not have any devices with updated Time messaging the Time display does not update automatically when the vessel crosses time zones. Separately, the Distributed Power System only sends alerts within its own NMEA2000® network and would be beneficial if these messages could be shared to the “Navigation Devices” NMEA2000® network giving the ability to acknowledge Distributed Power System alerts using the vessel’s navigation display that is attached to the “Navigation Devices” NMEA2000® network. An NBE100 is applied to this vessel to connect the Distributed Power System’s NMEA2000® network and the “Navigation Devices” NMEA2000® network. Using the NBE100 Pass Filter, the Distributed Power System can get updated Time information from the “Navigation Devices” NMEA2000® network and the “Navigation Devices” NMEA2000® network can receive Distributed Power System alerts. The vessel’s captain can now acknowledge the Distributed Power Systems alerts while underway using the vessel’s navigation display. The NBE100 provides such a solution with only necessary bus traffic messaging being passed.

Please note that the NBE100 will not filter and always pass ISO Address Claim, Request, and Acknowledgement messages, as well as Product Information allowing for “visibility” of all devices connected to the two NMEA2000® networks as if they were one.

## 2 Installation

### 2.1 Unpacking the Box

When unpacking the box containing the Maretron NBE100, you should find the following items:

1 – NBE100 – Network Bus Extender 1 – Parts Bag containing 4 Stainless Steel Mounting Screws 1 – NBE100 User’s Manual 1 – Warranty Registration Card

If any of these items are missing or damaged, please contact Maretron.

<!-- pdf page 5 | printed page 3 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

### 2.2 Choosing a Mounting Location

Please consider the following when choosing a mounting location.

1. The NBE100 is waterproof, so it can be mounted in a damp or dry location.
2. The orientation is not important, so the NBE100 can be mounted on a horizontal deck, vertical bulkhead, or upside down if desired.
3. The NBE100 is temperature-rated to 55°C (130°F), so it should be mounted away from engines or engine rooms where the operating temperature exceeds the specified limit.

### 2.3 Mounting the NBE100

Attach the NBE100 securely to the vessel using the included stainless steel mounting screws or other fasteners as shown in Figure 1 below. Do not use thread locking compounds containing methacrylate ester, such as Loctite Red (271), as they will cause stress cracking of the plastic enclosure.

### 2.4 Connecting the NBE100

The NBE100 requires one type of electrical connection: the NMEA 2000® connections (refer to Section 2.4.1).

#### 2.4.1 NMEA 2000® Connection

The NBE100 has two NMEA 2000® connectors. The NMEA 2000® connectors can be found on either end of the enclosure.

The NMEA 2000® connectors are round five pin male connector (see Figure 2). You connect the NBE100 to an NMEA 2000® network using a Maretron NMEA 2000® cable (or compatible cable) by connecting the female end of the cable to the NBE100 (note the key on the male connector

<!-- figure 1 on pdf page 5 at 226,307-384,550 pt | caption: "Figure 1 – Mounting the NBE100" | text-layer labels: none | nearby labels: Figure 1 – Mounting the NBE100 | OCR text follows (tesseract, unverified; 5/11 words >= 60, mean confidence 60) -->
i
IN
Ur
<i
A
<!-- end of figure 1 -->

<!-- pdf page 6 | printed page 4 | header: _______________________________________________________ -->

## _______________________________________________________

and keyway on the female connector). Be sure the cable is connected securely and that the collar on the cable connector is tightened firmly. Connect the other end of the cable (male) to the NMEA 2000® network in the same manner. The NBE100 is designed such that you can plug or unplug it from an NMEA 2000® network while the power to the network is connected or disconnected. Please follow recommended practices for installing NMEA 2000 ® network products.

Figure 2 – NMEA 2000® Connector Face Views The NBE100 is installed on an NMEA 2000® network between the two sections that you wish to physically isolate. Because the port on the NBE100 are optically isolated, there is no electrical connection through the NBE100, so you must ensure that each of the two NMEA 2000® networks connected to the NBE100 have separate power sources and two termination resistors. This means that if you use an NBE100 to split an existing network into two separate networks, you must provide one additional power connection and two additional termination resistors (one for each side of the NBE100).

The two NMEA 2000® connectors are labeled “N2K PORT A(PWR)” and “N2K PORT B”. Logically, these connectors are identical; that is, you can connect the NBE100 between two networks in either way and it will function identically. However, the NBE100 sources power only from the connector marked “N2K PORT A(PWR)”. It uses no power from the connector labeled “N2K PORT B”.

Figure 3 below shows the installation of an NBE100 into a simple NMEA 2000 ® network.

For exceptionally large networks, multiple NBE100’s may be used to segment the network into more than two segments. Each segment must have its power connection and two termination resistors.

<!-- figure 1 on pdf page 6 at 50,161-559,338 pt | caption: "Figure 2 – NMEA 2000 ® Connector Face Views" | text-layer labels: none | OCR text follows (tesseract, unverified; 34/38 words >= 60, mean confidence 88) -->
Sockets
Pins
Connector Threads
Connector Threads
Male Connector
Female Connector
NET-
Shield
Pin
Pin
NET-S, (power supply positive,
NET-L
Pin
NET-C, (power supply common, -V)
Pin
NET-H, (CAN-H)
Shield
Pin
NET-L, (CAN-L)
NET-C
NET-S
<!-- end of figure 1 -->

<!-- pdf page 7 | printed page 5 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

#### 2.4.2 Checking Connections

Once the NMEA 2000® connections to the NBE100 have been completed, check to see that information is being properly transmitted by using an appropriate NMEA 2000® display to observe a sensor on the opposite side of the NBE100. If you don’t see data from that sensor, refer to Section 4, “Troubleshooting”.

### 2.5 Configuring the NBE100

The NBE100 will function on the NMEA 2000 network as it is shipped from the factory; no user configuration is required. The NBE100 features PGN filtering if enabled. Configure the NBE100 using Maretron’s N2KAnaylzer®. See details below for information on how to configure your NBE100.

#### 2.5.1 General Tab

The “General Tab” for the NBE100 features a blank field for entering a Label. Enter any Label desired in the field such as the NBE100’s location on the vessel or an NBE100 reference number such as “Box 2”. See example below of the “General Tab”.

<!-- figure 1 on pdf page 7 at 53,70-559,307 pt | caption: "Figure 3 – NBE100 Connection Diagram" | text-layer labels: none | nearby labels: Figure 3 – NBE100 Connection Diagram | OCR text follows (tesseract, unverified; 14/23 words >= 60, mean confidence 69) -->
0
NBE10
Termination
Termination
Resistor
Resistor
Powertap
PowerTap
Tee
Tee
Termination
Termination
Resistor
Resistor
<!-- end of figure 1 -->

<!-- pdf page 8 | printed page 6 | header: _______________________________________________________ -->

## _______________________________________________________

#### 2.5.2 Advanced Tab

In the “Advanced Tab” there is a field for Device Instance. NMEA 2000® provides a unique device instance for each device on a vessel. This value should be programmed in each NBE100 so that each NBE100 is associated with a unique device instance number. The default instance number is 0, which is used to indicate the first NBE100 that is hooked to the network. Subsequent NBE100’s connected to the network would be numbered 1, 2, and so on. See preceding figure of the NBE100 Advanced Tab containing this field.

<!-- figure 1 on pdf page 8 at 106,72-504,377 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/3 words >= 60, mean confidence 96) -->
(Max. 32 Characters)
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 8 at 103,382-506,439 pt | caption: "Figure 4 - NBE100 General Tab" | text-layer labels: none | nearby labels: Figure 4 - NBE100 General Tab | OCR text follows (tesseract, unverified; 31/31 words >= 60, mean confidence 96) -->
Save Config To File... Restore Factory Defaults
Get Config From Device
Put Config To Device
Close
RED text indicates a changed parameter that has not yet been put to the device
<!-- end of figure 2 -->

<!-- pdf page 9 | printed page 7 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

#### 2.5.3 PGN Filter Tab

The NBE100 has a feature with which only certain messages will be passed from one port to the other, as opposed to the default state, in which all messages are passed between both ports. Messages to be passed are selected on the basis of the Parameter Group Numbers (PGN’s) of the messages. This is useful for passing only certain information from the NMEA 2000 network on one port of the NBE100 to the NMEA 2000 network on the other port.

If the PGN Filter is enabled the NBE100 will filter all PGNs except for the PGNs entered into the “Exception Field”. Where “CAN1” refers to the NBE100’s “N2K Port A” and “CAN2” refers to the NBE100’s “N2K Port B”, the PGN Filter can filter PGNs traveling from CAN1 to CAN2, CAN2 to CAN1 or PGNs traveling both directions. To enable PGN Filtering, select “Enable” in the dropdown box located under the desired PGN traveling direction to be filtered. To enable PGN filtering exceptions, enter the PGN number into the “PGN” field located under the “Filter Enabled” dialog. See example of the NBE100 PGN Filter Tab in the preceding figure for example of this feature.

<!-- figure 1 on pdf page 9 at 106,74-504,377 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 96) -->
Device Instance
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 9 at 103,382-506,439 pt | caption: "Figure 5 - NBE100 Advanced Tab" | text-layer labels: none | nearby labels: Figure 5 - NBE100 Advanced Tab | OCR text follows (tesseract, unverified; 31/31 words >= 60, mean confidence 96) -->
Save Config To File... Restore Factory Defaults
Get Config From Device
Put Config To Device
Close
RED text indicates a changed parameter that has not yet been put to the device
<!-- end of figure 2 -->

<!-- pdf page 10 | printed page 8 | header: _______________________________________________________ -->

## _______________________________________________________

#### 2.5.4 Installation Description Tab

In the “Installation Description Tab” you can store data to the NBE100 for information about the installation or any notes required. See preceding figure of the NBE100 Installation Description Tab to see it’s content.

<!-- figure 1 on pdf page 10 at 113,70-497,425 pt | caption: "Figure 6 - NBE100 PGN Filter Tab" | text-layer labels: none | nearby labels: Figure 6 - NBE100 PGN Filter Tab | OCR text follows (tesseract, unverified; 38/42 words >= 60, mean confidence 89) -->
CAN2->CAN1
Filter |Disabled
A
PGN
Description
PGN
Description
Engine Parameters,
Save Config To File... Restore Factory Defaults
Put Device
Get Config From Device
Close
text indicates a changed parameter that has not yet been put to the device
<!-- end of figure 1 -->

<!-- pdf page 11 | printed page 9 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

Figure 7 - NBE100 Installation Description Tab

## 3 Maintenance

- Regular maintenance is important to ensure continued proper operation of the Maretron
- NBE100. Perform the following tasks periodically:

| • | Clean the unit with a soft cloth. Do not use chemical cleaners as they may remove paint or markings or may corrode the NBE100 enclosure or seals. Do not use any cleaners containing acetone, as they will deteriorate the plastic enclosure. |
| --- | --- |
| • | Ensure that the unit is mounted securely and cannot be moved relative to the mounting surface. If the unit is loose, tighten the mounting screws. |
| • | Check the security of the cables connected to the NMEA 2000® connector and tighten if necessary. |

<!-- figure 1 on pdf page 11 at 106,74-504,377 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 28/30 words >= 60, mean confidence 89) -->
Description #1:
ASCII (English language only, Max. 70 characters)
Unicode (Max. 35 characters)
ASCII (English language only, Max. 70 characters)
Unicode (Max. 35 characters)
Information
Maretron 1-866-550-9100 www.maretron.com
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 11 at 103,382-506,442 pt | caption: "Figure 7 - NBE100 Installation Description Tab" | text-layer labels: none | OCR text follows (tesseract, unverified; 30/30 words >= 60, mean confidence 94) -->
Save Config To File... Restore Factory Defaults
Get Config From Device
Put Config To Device
Close
RED text indicates changed parameter that has not yet been put to the device
<!-- end of figure 2 -->

<!-- pdf page 12 | printed page 10 | header: _______________________________________________________ -->

## _______________________________________________________

## 4 Troubleshooting

If you notice unexpected operation of the Maretron NBE100, follow the troubleshooting procedures in this section to remedy simple problems. If these steps do not solve your problem, please contact Maretron Technical Support (refer to Section 6 for contact information).

| Symptom | Troubleshooting Procedure |
| --- | --- |
| No devices on one side | • Ensure that the NBE100 is properly connected to the |
| of the NBE100 are | NMEA 2000® network segments. |
| visible from a display | • Ensure that both NMEA 2000 network segments have |
| connected to the other | power. |
| side. | • Ensure that both NMEA 2000 network segments have two termination resistors fitted. |
| PGNs do not pass the | • Ensure desired configuration of the PGN Filter feature |

NBE100

<!-- figure 1 on pdf page 12 at 182,149-559,283 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 13 | printed page 11 | header: NBE100 User's Manual_____________________________________ -->

<!-- sub/superscripts on this page (from font sizes): 7m/s^2 -->

## NBE100 User's Manual_____________________________________

## 5 Technical Specifications

As Maretron is constantly improving its products, all specifications are subject to change without notice. Maretron products are designed to be accurate and reliable; however, they should be used only as aids to navigation and not as a replacement for traditional navigation aids and techniques.

##### Certifications

| Parameter | Comment |  |
| --- | --- | --- |
| NMEA 2000® Standard | Level A+ |  |
| Maritime Navigation and Radiocommunication Equipment & Systems | IEC 61162-3 |  |
| Maritime Navigation and Radiocommunication Equipment & Systems | IEC 60945 |  |
| FCC and CE Mark | Electromagnetic Compatibility |  |
| NMEA 2000® Parameter Group Numbers (PGNs) |  |  |
| Description            PGN #                           PGN Name |  | Default Rate |
| Response to Requested        126464   PGN List (Transmit and Receive) |  | N/A |
| PGNs                         126996   Product Information |  | N/A |
| 126998   Configuration Information |  | N/A |
| Protocol PGNs                059392   ISO Acknowledge |  | N/A |
| 059904   ISO Request |  | N/A |
| 060928   ISO Address Claim |  | N/A |
| 065240   ISO Address Command |  | N/A |
| 126208   NMEA Request/Command/Acknowledge |  | N/A |
| Maretron Proprietary PGN’s   126720   Configuration |  | N/A |

##### Electrical

| Parameter | Value | Comment |
| --- | --- | --- |
| Operating Voltage | 9 to 16 Volts | DC Voltage |
| Power Consumption | <150mA | Average Current Drain |
| Load Equivalence Number (LEN) | 3 | NMEA 2000® Spec. (1LEN = 50 mA) |
| Reverse Battery Protection | Yes | Indefinitely |
| Load Dump Protection | Yes | Energy Rated per SAE J1113 |

##### Mechanical

Parameter                       Value                           Comment Size                                     3.11” x 3.46” x 1.38” Including Flanges for Mounting (79mm x 88mm x 35mm) Weight                                       8 oz. (227 g)

##### Environmental

| Parameter | Value |
| --- | --- |
| IEC 60945 Classification | Exposed |
| Degree of Protection | IP67 |
| Operating Temperature | -25°C to 55°C |
| Storage Temperature | -40°C to 70°C |
| Relative Humidity | 93%RH @40°C per IEC60945-8.2 |
| Vibration | 2-13.2Hz @ ±1mm, 13.2-100Hz @ 7m/s^2 per IEC 60945-8.7 |
| Rain and Spray | 12.5mm Nozzle @ 100liters/min from 3m for 30min per IEC 60945-8.8 |
| Solar Radiation | Ultraviolet B, A, Visible, and Infrared per IEC 60945-8.10 |
| Corrosion (Salt Mist)           4 times 7 days @ 40°C, 95%RH after 2 hour Salt Spray Per IEC 60945-8.12 |  |
| Electromagnetic Emission | Conducted and Radiated Emission per IEC 60945-9 |
| Electromagnetic Immunity | Conducted, Radiated, Supply, and ESD per IEC 60945-10 |
| Safety Precautions               Dangerous Voltage, Electromagnetic Radio Frequency per IEC 60945-12 |  |

<!-- figure 1 on pdf page 13 at 420,266-490,391 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 13 at 125,274-182,370 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 13 at 209,413-262,490 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 13 at 82,514-235,566 pt | caption: none | text-layer labels: Parameter | nearby labels: Mechanical | Size | Weight | Environmental | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 13 at 499,514-559,566 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 14 | printed page 12 | header: _______________________________________________________ -->

## _______________________________________________________

## 6 Technical Support

- If you require technical support for Maretron products, you can reach us in any of the following
- ways:

| Telephone: | 1-866-550-9100 |
| --- | --- |
| Fax: | 1-602-861-1777 |
| E-mail: | support@maretron.com |
| World Wide Web: | http://www.maretron.com |
| Mail: | Carling Technologies, Inc. Attn: Maretron Technical Support 120 Intracoastal Pointe Dr. Suite 100 Jupiter, FL 33477 USA |

<!-- pdf page 15 | printed page 13 | header: NBE100 User's Manual_____________________________________ -->

## NBE100 User's Manual_____________________________________

## 7 Installation Template

Please check the dimensions before using the following diagram as a template for drilling the mounting holes because the printing process may have distorted the dimensions.

Figure 8 – Mounting Surface Template

<!-- figure 1 on pdf page 15 at 125,178-485,583 pt | caption: none | text-layer labels: none | OCR below floor, text not used (3/13 words >= 60, mean confidence 40) -->

<!-- pdf page 16 | printed page 14 | header: _______________________________________________________ -->

## _______________________________________________________

<!-- omitted: "8 Maretron (2 Year) Limited Warranty" (pdf page 16; 8 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
