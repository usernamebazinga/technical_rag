<!-- font check: Wingdings is not a standard text face; glyphs "Æ" on pages 30. Verify against the rendered page before trusting or mapping. -->

<!-- font check: no ToUnicode map in Arial-BoldMT, Arial-ItalicMT, ArialMT, TimesNewRomanPS-BoldItalicMT, TimesNewRomanPS-BoldMT, TimesNewRomanPS-ItalicMT, TimesNewRomanPSMT, Wingdings-Regular; ligatures (fi, fl) or special glyphs may be missing from the text (pages 2-13, 15-17, 19-67, 69-74 checked against the rendered page) -->

<!-- pdf page 1 -->

ADAM-4571/4570
1/2-port RS-232/422/485
Serial Device Servers

ADAM-4571L/4570L
1/2-port RS-232
Serial Device Servers

User Manual

<!-- figure 1 on pdf page 1 at 167,108-354,314 pt | caption: none | text-layer labels: ADAM-4571/4570 | ADAM-4571L/4570L | 1/2-port RS-232 Serial Device Servers | User Manual | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 2 | printed page ii | footer: ADAM-4570 Series User Manual -->

    Copyright
    The documentation and the software included with this product are copy-
    righted 2010 by Advantech Co., Ltd. All rights are reserved. Advantech
    Co., Ltd. reserves the right to make improvements in the products
    described in this manual at any time without notice. No part of this man-
    ual may be reproduced, copied, translated or transmitted in any form or
    by any means without the prior written permission of Advantech Co., Ltd.
    Information provided in this manual is intended to be accurate and reli-
    able. However, Advantech Co., Ltd. assumes no responsibility for its use,
    nor for any infringements of the rights of third parties, which may result
    from its use.

    Acknowledgements
    Intel and Pentium are trademarks of Intel Corporation.
    Microsoft Windows and MS-DOS are registered trademarks of
    Microsoft Corp.
    All other product names or trademarks are properties of their respective
    owners.

    Part No. 2003457102               3rd Edition
    Printed in Taiwan                 April 2010

ADAM-4570 Series User Manual          ii

<!-- pdf page 3 | printed page iii -->

Product Warranty (2 years)
Advantech warrants to you, the original purchaser, that each of its prod-
ucts will be free from defects in materials and workmanship for two years
from the date of purchase.
This warranty does not apply to any products which have been repaired or
altered by persons other than repair personnel authorized by Advantech,
or which have been subject to misuse, abuse, accident or improper instal-
lation. Advantech assumes no liability under the terms of this warranty as
a consequence of such events.
Because of Advantech’s high quality-control standards and rigorous test-
ing, most of our customers never need to use our repair service. If an
Advantech product is defective, it will be repaired or replaced at no
charge during the warranty period. For out-of-warranty repairs, you will
be billed according to the cost of replacement materials, service time and
freight. Please consult your dealer for more details.

If you think you have a defective product, follow these steps:
1.    Collect all the information about the problem encountered. (For
      example, CPU speed, Advantech products used, other hardware
      and software used, etc.) Note anything abnormal and list any
      onscreen messages you get when the problem occurs.
2.    Call your dealer and describe the problem. Please have your man-
      ual, product, and any helpful information readily available.
3.    If your product is diagnosed as defective, obtain an RMA (return
      merchandize authorization) number from your dealer. This allows
      us to process your return more quickly.
4.    Carefully pack the defective product, a fully-completed Repair and
      Replacement Order Card and a photocopy proof of purchase date
      (such as your sales receipt) in a shippable container. A product
      returned without proof of the purchase date is not eligible for war-
      ranty service.
5.    Write the RMA number visibly on the outside of the package and
      ship it prepaid to your dealer.

                                  iii

<!-- pdf page 4 | printed page iv | footer: ADAM-4570 Series User Manual -->

    Declaration of Conformity
    CE
    This product has passed the CE test for environmental specifications
    when shielded cables are used for external wiring. We recommend the use
    of shielded cables. This kind of cable is available from Advantech. Please
    contact your local supplier for ordering information.

    FCC Class A
    Note: This equipment has been tested and found to comply with the limits
    for a Class A digital device, pursuant to part 15 of the FCC Rules. These
    limits are designed to provide reasonable protection against harmful
    interference when the equipment is operated in a commercial environ-
    ment. This equipment generates, uses, and can radiate radio frequency
    energy and, if not installed and used in accordance with the instruction
    manual, may cause harmful interference to radio communications. Opera-
    tion of this equipment in a residential area is likely to cause harmful inter-
    ference in which case the user will be required to correct the interference
    at his own expense.

    Technical Support and Assistance
    Step 1. Visit the Advantech web site at www.advantech.com/support
            where you can find the latest information about the product.
    Step 2. Contact your distributor, sales representative, or Advantech's cus-
            tomer service center for technical support if you need additional
            assistance. Please have the following information ready before
            you call:
            - Product name and serial number
            - Description of your peripheral attachments
            - Description of your software (operating system, version, appli-
            cation software, etc.)
            - A complete description of the problem
            - The exact wording of any error messages

ADAM-4570 Series User Manual           iv

<!-- pdf page 5 | printed page v -->

Safety Instructions
1.    Read these safety instructions carefully.
2.    Keep this User's Manual for later reference.
3.    Disconnect this equipment from any AC outlet before cleaning.
      Use a damp cloth. Do not use liquid or spray detergents for clean-
      ing.
4.    For plug-in equipment, the power outlet socket must be located
      near the equipment and must be easily accessible.
5.    Keep this equipment away from humidity.
6.    Put this equipment on a reliable surface during installation. Drop-
      ping it or letting it fall may cause damage.
7.    The openings on the enclosure are for air convection. Protect the
      equipment from overheating. DO NOT COVER THE OPENINGS.
8.    Make sure the voltage of the power source is correct before con-
      necting the equipment to the power outlet.
9.    Position the power cord so that people cannot step on it. Do not
      place anything over the power cord.
10.   All cautions and warnings on the equipment should be noted.
11.   If the equipment is not used for a long time, disconnect it from the
      power source to avoid damage by transient overvoltage.
12.   Never pour any liquid into an opening. This may cause fire or elec-
      trical shock.
13.   Never open the equipment. For safety reasons, the equipment
      should be opened only by qualified service personnel.
14.   If one of the following situations arises, get the equipment checked
      by service personnel:
a. The power cord or plug is damaged.
b. Liquid has penetrated into the equipment.
c. The equipment has been exposed to moisture.
d. The equipment does not work well, or you cannot get it to work
      according to the user's manual.
e. The equipment has been dropped and damaged.
f. The equipment has obvious signs of breakage.
15.   DO NOT LEAVE THIS EQUIPMENT IN AN ENVIRONMENT
      WHERE THE STORAGE TEMPERATURE MAY GO BELOW -
                                  v

<!-- pdf page 6 | printed page vi | footer: ADAM-4570 Series User Manual -->

          20° C (-4° F) OR ABOVE 60° C (140° F). THIS COULD DAM-
          AGE THE EQUIPMENT. THE EQUIPMENT SHOULD BE IN A
          CONTROLLED ENVIRONMENT.
    16.   CAUTION: DANGER OF EXPLOSION IF BATTERY IS
          INCORRECTLY REPLACED. REPLACE ONLY WITH THE
          SAME OR EQUIVALENT TYPE RECOMMENDED BY THE
          MANUFACTURER, DISCARD USED BATTERIES ACCORD-
          ING TO THE MANUFACTURER'S INSTRUCTIONS.
    The sound pressure level at the operator's position according to IEC 704-
    1:1982 is no more than 70 dB (A).
    DISCLAIMER: This set of instructions is given according to IEC 704-1.
    Advantech disclaims all responsibility for the accuracy of any statements
    contained herein.

    Safety Precaution - Static Electricity
    Follow these simple precautions to protect yourself from harm and the
    products from damage.
    1.    To avoid electrical shock, always disconnect the power from your
          PC chassis before you work on it. Don't touch any components on
          the CPU card or other cards while the PC is on.
    2.    Disconnect power before making any configuration changes. The
          sudden rush of power as you connect a jumper or install a card may
          damage sensitive electronic components.

ADAM-4570 Series User Manual         vi

<!-- pdf page 7 | printed page vii -->

                                 Contents
Chapter    1 Overview .......................................................... 2
          1.1   Introduction ....................................................................... 2
          1.2   Features ............................................................................. 2
          1.3   Specifications .................................................................... 3
          1.4   Package Checklist ............................................................. 5
                1.4.1      ADAM-4571/4571L ...................................................... 5
                1.4.2      ADAM-4570/4570L ...................................................... 5
Chapter    2 Getting Started ................................................ 8
          2.1   Understanding the Advantech ADAM-4570 Series.......... 8
                2.1.1     Network Architecture .................................................... 8
                2.1.2     LED Indicators ............................................................... 9
                          Table 2.1:ADAM-4570 Series LED Definition ............. 9
                2.1.3     Dimensions (Unit: mm) ............................................... 10
                          Figure 2.1:Top Panel .................................................... 10
                          Figure 2.2:Front Panel ................................................. 10
                          Figure 2.3:Back Panel .................................................. 10
                2.1.4     Stickers ......................................................................... 11
          2.2   Connecting the Hardware................................................ 11
                2.2.1     Choosing a Location .................................................... 11
                          Figure 2.4:Panel Mounting .......................................... 12
                          Figure 2.5:DIN-rail Mounting ..................................... 13
                          Figure 2.6:Piggyback Stack ......................................... 14
                2.2.2     Network Connection .................................................... 15
                          Figure 2.7:Connecting ADAM-4570 Series to a Hub . 15
                2.2.3     Power Connection ........................................................ 16
                          Figure 2.8:Power Connection ...................................... 16
                2.2.4     Serial Connection ......................................................... 16
                          Figure 2.9:Serial Connection ....................................... 16
          2.3   Configuration Utility Installation .................................... 18
Chapter    3 Configuration................................................. 22
          3.1   Serial Device Server Configuration Utility Overview .... 22
          3.2   Discovering Your Serial Device Server .......................... 24
                3.2.1     Auto Searching ............................................................ 24
                3.2.2     Clearing the Device List and Searching Again ............ 27
                3.2.3     Manual Appending ...................................................... 28
          3.3   Setting Ethernet Parameters ............................................ 29
          3.4   Setting Serial Parameters ................................................ 31
                3.4.1     Basic Configuration ..................................................... 32
                3.4.2     Operation Mode Configuration .................................... 34
                3.4.3     Data Mode (USDG Mode) ........................................... 36
                3.4.4     Control Mode (USDG Mode) ...................................... 40
                3.4.5     AT Command List ....................................................... 42

                                            vii                                     Table of Contents

<!-- pdf page 8 | printed page viii | footer: ADAM-4570 Series User Manual -->

                  3.4.6    Advanced Settings ....................................................... 43
            3.5   Security Configuration .................................................... 44
                  3.5.1    Accessible Function ..................................................... 44
                  3.5.2    Port Monitor ................................................................. 45
            3.6   Fulfilling Administrator Functions.................................. 46
                  3.6.1    Import/Export Serial Port Setting ................................ 46
                  3.6.2    Locate Serial Device .................................................... 47
                  3.6.3    Lock Device ................................................................. 47
                  3.6.4    Restore to Factory Default Settings ............................. 48
                  3.6.5    Upgrading the Firmware .............................................. 49
Chapter       4 Setting the COM Redirector ........................ 52
            4.1   Setting COM Redirector (Virtual COM port) ................. 52
                  4.1.1    Auto Mapping .............................................................. 52
                  4.1.2    Manual Mapping .......................................................... 54
                  4.1.3    Manual Direct Mapping Virtual COM Port ................. 55
                  4.1.4    Remove the Virtual COM Port .................................... 56
            4.2   Running Diagnostic Test................................................. 57
Appendix A Pin Assignments ............................................ 62
           A.1    RS-232 Pin Assignments................................................. 62
           A.2    RJ-48 Cable PIN Assignment ......................................... 62
                  A.2.1    1. RS-422 ..................................................................... 62
                  A.2.2    2. RS-485 ..................................................................... 62
Appendix B Creating VCOM ............................................ 64
            B.1   Configuration Wizard...................................................... 64

ADAM-4570 Series User Manual                viii

<!-- pdf page 9 | header: CHAPTER -->

Overview

<!-- figure 1 on pdf page 9 at 294,38-335,96 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 10 | printed page 2 | footer: ADAM-4570 Series User Manual -->

Chapter 1 Overview
1.1 Introduction

   Advantech's ADAM-4570 series of Industrial Serial Device Servers are a
   robust, feature-rich, and cost effective way to network-enable equipment
   in an industrial automation environment. ADAM-4570 series provide one
   or two RS-232/422/485 serial ports, and ADAM-4571L/4570L provide
   one or two RS-232 serial ports.
   By encapsulating serial data and transporting it over Ethernet, the
   ADAM-4570 series allows virtual serial links over Ethernet and IP (TCP/
   IP, UDP/IP) networks. After Advantech Serial Device Sever Configura-
   tion Utility installation, standard serial operation calls are transparently
   redirected to the serial device servers, guaranteeing compatibility with
   legacy serial devices and enabling backward compatibility with existing
   software.

1.2 Features

   • Up to 255 serial ports for one 2000/XP/Vista host
   • Supports 10/100 Mbps auto-sensing Ethernet port
   • Supports high transmission speeds up to 921.6 Kbps
   • Supports LED indicators: Easy to diagnostic
   • Supports integrated configuration utility and port-mapping utility:
     easy to configure and manage 255 COM ports and self-diagnostic
   • Easy to locate specific ADAM-4570 Device Servers
   • Supports multi-access features: allows max. of 5 hosts to access one
     serial port simultaneously
   • Surge protection for power line
   • Mounts on DIN-rail, panel or piggyback easily

<!-- pdf page 11 | printed page 3 | footer: Chapter 1 -->

1.3 Specifications

   LAN
   • Compatibility:    IEEE 802.3, IEEE 802.3u
   • Speed:            10/100 Mbps, auto-sensing
   • No. of Ports:     1
   • Port Connector: 8-pin RJ45
   • Protection:       Built-in 1.5 KV magnetic isolation
   Serial Communications
   • Port Type:        ADAM-4570 series: RS-232/422/485
                       ADAM-4571L/4570L: RS-232
   • No. of Ports:     ADAM-4571/4571L: 1
                       ADAM-4570/4570L: 2
   • Port Connector: ADAM-4571/4571L: DB9 male
                       ADAM-4570/4570L: 10-pin RJ48
   • Data Bits:        5, 6, 7, 8
   • Stop Bits:        1, 1.5, 2
   • Parity Bits:      None, Odd, Even, Space, Mark
   • Flow Control:     XON/XOFF, RTS/CTS, DTR/DSR
   • Baud Rate:        50 bps to 921.6 Kbps
   • Serial Signals:   RS-232: TxD, RxD, CTS, RTS, DTR, DSR, DCD,
                       RI, GND
                       RS-422: TxD+, TxD-, RxD+, RxD-, GND
                       RS-485: Data+, Data-, GND
   • Protection:       15 KV ESD protection for all signals

<!-- pdf page 12 | printed page 4 | footer: ADAM-4570 Series User Manual -->

Software
• Driver Support:   Windows 2000/XP/Vista
• Utility Software: Serial Device Server Configuration Utility
• Operation Modes:COM port redirection mode (Virtual COM)
                    TCP/UDP server mode
                    TCP/UDP client mode
                    Pair connection (peer to peer) mode
• Configuration Methods: Windows utility, Web Browser, and Telnet
Mechanics
• Dimensions (H x W x D):130 x 70 x 30 mm
• Enclosure:        ABS + PC with solid mounting hardware
• Mounting:         DIN-rail, panel mount, piggyback stack
• Weight:           ADAM-4571/4571L: 135g
                    ADAM-4570/4570L: 160g
General
• LED Indicators: Power, System Status
• LAN:              Speed, Link/Active
• Serial:           Tx, Rx
Power Requirement
• Power Input:      10 to 30 VDC
• Power Consumption:         ADAM-4571/4571L: 1.5W
                             ADAM-4570/4570L: 2W
• Power Line Protection: 1 KV burst (EN61000-4-4),
                         0.5 KV surge (EN61000-4-5)
Environment
• Operating Temperature: 0 to 60° C (32 to 140° F )
• Storage Temperature:       20 to 80° C (-4 to 176° F )
• Operating Humidity:        5 to 95 % RH
Regulatory Approvals
• EMC:                       CE, FCC Part 15 Subpart B (Class A)

<!-- pdf page 13 | printed page 5 | footer: Chapter 1 -->

1.4 Package Checklist

  1.4.1 ADAM-4571/4571L
  • 1 x ADAM-4571/4571L Serial Device Server
  • CD-ROM for utility and manual
  • 1 x RS-232 loopback DB9 tester
  • Five stickers
  • DIN-rail mounting Adapter
  • Panel mounting bracket
  • Stand

  1.4.2 ADAM-4570/4570L
  • 1 x ADAM-4570/4570L Serial Device Server
  • CD-ROM for utility and manual
  • 1 x RS-232 loopback DB9 tester
  • 2 x RJ48 to DB9 serial cable
  • Five stickers
  • DIN-rail mounting Adapter
  • Panel mounting bracket
  • Stand

<!-- pdf page 14 | printed page 6 | footer: ADAM-4570 Series User Manual -->

(no text layer on this page)

<!-- pdf page 15 | header: CHAPTER -->

Getting Started

<!-- figure 1 on pdf page 15 at 294,38-344,96 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 16 | printed page 8 | footer: ADAM-4570 Series User Manual -->

Chapter 2 Getting Started
  In this chapter, you will be given an overview of the ADAM-4570 series
  hardware installation procedures.

2.1 Understanding the Advantech ADAM-4570 Series

  The ADAM-4570 series are advanced device servers. They extend tradi-
  tional COM ports of a PC with access over a TCP/IP network. Through
  networking, you can control and monitor remote serial devices either over
  a LAN or over the WAN.Since the ADAM-4570 series is connected
  through a TCP/IP network, you will need to know some basic facts about
  networking in order to get the server hooked up correctly.

  2.1.1 Network Architecture
  Traditional serial port communication uses a COM port board that slides
  into one of the slots at the back of your PC. In this case, only the com-
  puter containing the board can access the serial port. With the ADAM-
  4570 series, you are now able to access the COM port from a distance
  through local area network. The ADAM-4570 series can be integrated
  within the network architecture of any protocol. Note, all serial devices
  which are connected to the port must have the same protocol running and
  the same transmission speed. Connect devices running different protocols
  to different ports of the ADAM-4570 series.

<!-- pdf page 17 | printed page 9 | footer: Chapter 2 -->

2.1.2 LED Indicators
There are three or four LEDs located on the top panel of ADAM-4570
series, each with its own specific function.
 Table 2.1: ADAM-4570 Series LED Definition

LED                Color

                   Red

Status/Power

                   Green

                   Red

Speed/Link (Act)

                   Green

                   Red

Tx/Rx              (Serial)

                   Green

Status   Description
ON       Heartbeat (1 time/sec)

OFF      Not working

ON       Power ON

OFF      Power OFF
ON       100 Mbps speed

OFF      10 Mbps speed

ON       Valid network link

OFF      Invalid network link
ON       Data being transmitted

OFF      No data being transmitted

ON       Data being received

OFF      No Data being received

<!-- pdf page 18 | printed page 10 | footer: ADAM-4570 Series User Manual -->

2.1.3 Dimensions (Unit: mm)

                 Figure 2.1: Top Panel

                Figure 2.2: Front Panel

                Figure 2.3: Back Panel

<!-- figure 1 on pdf page 18 at 136,67-249,137 pt | caption: "Figure 2.1: Top Panel" | text-layer labels: none | nearby labels: Figure 2.1: Top Panel | OCR text follows (tesseract, unverified; 1/3 words >= 60, mean confidence 43) -->
70.00
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 18 at 115,166-263,331 pt | caption: "Figure 2.2: Front Panel" | text-layer labels: none | nearby labels: Figure 2.1: Top Panel | Figure 2.2: Front Panel | OCR text follows (tesseract, unverified; 8/21 words >= 60, mean confidence 53) -->
60.00
(Ethernet)
N
5
6.00
ADAM-4571
(Ethernet)
R35.00
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 18 at 136,360-256,513 pt | caption: "Figure 2.3: Back Panel" | text-layer labels: none | nearby labels: Figure 2.2: Front Panel | Figure 2.3: Back Panel | OCR text follows (tesseract, unverified; 4/7 words >= 60, mean confidence 65) -->
§.20
56.00
28.00
4—5.00
<!-- end of figure 3 -->

<!-- pdf page 19 | printed page 11 | footer: Chapter 2 -->

  2.1.4 Stickers
  If you forgot the IP addresses of specific ADAM-4570 series or where the
  host PC is mapped to the ADAM-4570 series port, we have provided five
  stickers for you to note the IP addresses and place in a secure location.
  For example,
  172.20.20.5: The IP address of specific ADAM-4570 series
  160.59.20.89: The IP address of the specific host PC mapped to this port.

2.2 Connecting the Hardware

  Next, we will explain how to find a proper location for your serial device
  server, and then explain how to connect to the network, hook up the
  power cable, and connect to the ADAM-4570 series’s serial port.
  Note: Before you install ADAM-4570 series, you can install other com-
  munication cards first.
  2.2.1 Choosing a Location

  Due to its versatile and innovative design, the ADAM-4570 series can be:
  • Fixed to a panel mount
  • Fxed to a DIN-rail.
  • Piggyback Stack

<!-- pdf page 20 | printed page 12 | footer: ADAM-4570 Series User Manual -->

Panel Mounting
The ADAM-4570 series can be attached to a wall using the included
metal brackets. Each bracket comes with four screws; first attach the
brackets to the bottom of the ADAM-4570 series. Next, screw each
bracket to a wall.

                   Figure 2.4: Panel Mounting

<!-- figure 1 on pdf page 20 at 67,137-323,425 pt | caption: "Figure 2.4: Panel Mounting" | text-layer labels: none | nearby labels: Figure 2.4: Panel Mounting | OCR: no legible text (0/2 words >= 60, mean confidence 12) -->

<!-- pdf page 21 | printed page 13 | footer: Chapter 2 -->

DIN-rail Mounting
You can mount the ADAM-4570 series on a standard DIN-rail. First,
using two screws, attach the metal plate to the DIN-rail bracket. Because
the screw heads are beveled, the tops of the screws will be flush with the
metal plate. DIN-rail Mounting Brackets—Orientation of Metal Plates
You can now screw the metal plate with the DIN-rail bracket assembly to
the bottom of the server is a more convenient way. Next, use the remain-
ing screws to put the metal plate on the bottom of the ADAM-4570 series.

                  Figure 2.5: DIN-rail Mounting

<!-- figure 1 on pdf page 21 at 96,170-292,470 pt | caption: "Figure 2.5: DIN-rail Mounting" | text-layer labels: none | nearby labels: Figure 2.5: DIN-rail Mounting | OCR: no legible text (0/5 words >= 60, mean confidence 24) -->

<!-- pdf page 22 | printed page 14 | footer: ADAM-4570 Series User Manual -->

Piggyback Stack
ADAM-4570 series can be stacked as seen in the figure below.

                   Figure 2.6: Piggyback Stack

<!-- figure 1 on pdf page 22 at 251,86-316,185 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 66) -->
J
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 22 at 77,194-297,379 pt | caption: "Figure 2.6: Piggyback Stack" | text-layer labels: none | nearby labels: Figure 2.6: Piggyback Stack | OCR: no legible text (0/8 words >= 60, mean confidence 22) -->

<!-- pdf page 23 | printed page 15 | footer: Chapter 2 -->

2.2.2 Network Connection
There are two ways to use the 10/100Base-T Ethernet connector located
on the ADAM-4570 series:
1. For Local Area Network (LAN) applications using the
ADAM-4570 series, you will simply plug one end of your Ethernet cable
into the 10/100Base-T connector, and the other end into the hub con-
nected to your network.
2. When installing and configuring, you will find it convenient to hook
the ADAM-4570 Series directly to your computer’s Ethernet card. To do
this you will need to use a “crossed-cable”, such as the one supplied with
your server.

Cabling requirements for the Ethernet side
Use an RJ-45 to connect the Ethernet port of the ADAM-4570 series to
the network hub. The cable for connection should be Category 3 (for
10Mbps data rate) or Category 5 (for 100 Mbps data rate) UTP/STP
cable, which is compliant with EIA/TIA 586 specifications. Maximum
length between the hub and any ADAM-4570 Series is up to 100 meters
(ca.300 ft).

       Figure 2.7: Connecting ADAM-4570 Series to a Hub

<!-- figure 1 on pdf page 23 at 50,326-344,389 pt | caption: "Figure 2.7: Connecting ADAM-4570 Series to a Hub" | text-layer labels: none | OCR text follows (tesseract, unverified; 13/20 words >= 60, mean confidence 67) -->
Dual Speed Hub
Category 5
EIA/TIA 568
ADAM-5510
UTP Cable
ADAM-4570
0
100m
<!-- end of figure 1 -->

<!-- pdf page 24 | printed page 16 | footer: ADAM-4570 Series User Manual -->

2.2.3 Power Connection
You should take the following steps to connect ADAM-4570 series
power.
1. Connect the power cable to 2-pin connector
2. Connect power cable to power adapter

                   Figure 2.8: Power Connection

If the ADAM-4570 Series is working properly, the green power LED will
light up, indicating that the ADAM-4570 Series is receiving power.

2.2.4 Serial Connection
The model of the ADAM-4570 Series that you purchased has RJ-48
serial ports or DB-9 male connector on the bottom of module. Depending
on your serial device and serial interfaces, there are two options:
1. For an RS-232/422/485 port you may use a RJ-48 to DB-9 cable
  which we supply to connect your serial device to the ADAM-4570/
  4570L. Simply plug one end of the cable into the jack, and plug the
  other end into the serial port jack on your serial device.
2. Refer to the following table for details on serial cable RJ-48 to DB-9
  pinouts.

                   Figure 2.9: Serial Connection

<!-- figure 1 on pdf page 24 at 141,113-242,199 pt | caption: "Figure 2.8: Power Connection" | text-layer labels: none | nearby labels: Figure 2.8: Power Connection | OCR text follows (tesseract, unverified; 3/9 words >= 60, mean confidence 52) -->
RS-232/422/485
+Vs GND
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 24 at 48,432-349,480 pt | caption: "Figure 2.9: Serial Connection" | text-layer labels: none | nearby labels: Figure 2.9: Serial Connection | OCR text follows (tesseract, unverified; 7/19 words >= 60, mean confidence 48) -->
to DB-9 (male)
DB-9 (female)
PLC
RJ-45
<!-- end of figure 2 -->

<!-- pdf page 25 | printed page 17 | footer: Chapter 2 -->

RJ-48

PIN Name   DCD   RX   TX   DTR   GND   DSR   RTS   CTS   RI
RJ-48      1     2    3    4     5     6     7     8     9

DB-9

<!-- figure 1 on pdf page 25 at 165,118-234,209 pt | caption: none | text-layer labels: none | nearby labels: 2 | 3 | 4 | 5 | 6 | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 76) -->
DSR
RX
RTS
T™
DTR
RI
GND
RS
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 25 at 160,226-213,309 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 82) -->
1
DATA-
DATA+
GND
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 25 at 165,326-227,408 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 86) -->
TX-
TX+
RX-
GND
422
<!-- end of figure 3 -->

<!-- pdf page 26 | printed page 18 | footer: ADAM-4570 Series User Manual -->

2.3 Configuration Utility Installation

   In order to use a PC and an Ethernet network to control serial devices
   connected to the ADAM-4570 Series, you must first have a host running
   Windows 2000/XP/Vista. This type of application also requires the host
   to have an Ethernet card and TCP/IP protocol installed. The following are
   the required steps for ADAM-4570 Series:

             Be sure that you have at least version 2.0 of the
   Note:
             Microsoft .NET Framework installed on your PC.

   1. Insert the Advantech IEDG series driver utility CD-ROM into the drive
     (e.g. D:\) on the host PC. Change the host computer's default drive from
     C: to D:
   2. Use your Windows Explorer or the Windows Run command to execute
     the Setup program (the path for the Setup program on the CD-ROM
     should be on the CD-ROM should be:
   D:\Utility&Driver\Serial Device Server Configuration Utility\Serial_
    Device_Server_Configuration_Utility_[Version]_Release_[Date].exe
   3. Upon executing the setup program, the Welcome Dialog Box will pop-
     up. Press the "Next" button to continue.

<!-- figure 1 on pdf page 26 at 38,333-340,559 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 68/70 words >= 60, mean confidence 93) -->
Advantech Serial Device Server Configuration Utility Setup
Welcome to the Advantech Serial Device Server
Configuration Utility Setup Wizard
This wizard will quide you through the installation of Advantech Serial Device Server
Configuration Utility.
Itis recommended that you close all other applications before starting Setup. This will
make it to update relevant system files without having to reboot your
Click Next to continue.
lem v2.40
Nullsoft Install S
hA
<!-- end of figure 1 -->

<!-- pdf page 27 | printed page 19 | footer: Chapter 2 -->

4. Carefully read the Software License Agreement, and press "Yes" to
   continue.

5. The Setup program will specify a default installation path:
  Advantech eAutomation\Serial Device Server Configuration Utility\

<!-- figure 1 on pdf page 27 at 69,82-330,276 pt | caption: none; nearest centred text below: "5. The Setup program will specify a default installation path:" | text-layer labels: none | OCR text follows (tesseract, unverified; 156/165 words >= 60, mean confidence 91) -->
(x)
Advantech Serial Device Server Configuration Utility Setup
License Agreement
Please review the license terms before installing Advantech Serial Device Server Configuration Utility.
the rest of the
Press Page
|ADVANTECH CORPORATION
LICENSE AGREEMENT
SHOULD CAREFULLY READ THE FOLLOWING TERMS AND CONDITIONS!
(Opening and using the enclosed software for any purpose indicates your
acceptance of the terms and conditions of this License Agreement. If you
do not agree with the terms and conditions of this license agreement you
should return alll software, documentation and copy protection keys for a
refund. Restocking fees may apply. Advantech Automation Corporation provides
program and licenses, for its use in the United States, Puerto Rico,
‘or internationally. You assume the responsibility for the selection of the
program to achieve your intended results, and for the installation, use and
results obtained from this program.
click to conti
If you accept the terms of the
Device Server C
y
Nullsoft Install System v2.40
<Back
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 27 at 65,324-330,523 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/24 words >= 60, mean confidence 82) -->
er Ci
Configuration Utility Setup
ial
Devi
v
Installing
Server C
Pk
wait
Extract:
stall
Nt
ft Ir
Back
Cancel
<!-- end of figure 2 -->

<!-- pdf page 28 | printed page 20 | footer: ADAM-4570 Series User Manual -->

7. After setup has copied all program files to your computer, click the
   <Finish> button to finish the installation.

<!-- figure 1 on pdf page 28 at 60,82-330,283 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 28/33 words >= 60, mean confidence 86) -->
Ix
on Uti
Advantech Serial Device Ser
ity Setup
the Ad
Serial Device Server
Configuration Utility Setup Wizard
computer.
Click Finish to close this wizard.
Einish
stall S
<!-- end of figure 1 -->

<!-- pdf page 29 | header: CHAPTER -->

Configuration

<!-- figure 1 on pdf page 29 at 294,38-344,96 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 30 | printed page 22 | footer: ADAM-4570 Series User Manual -->

Chapter 3 Configuration
3.1 Serial Device Server Configuration Utility Overview

   The ADAM-4570 series provides an easy-to-use configuration utility to
   configure your serial device server through an Ethernet connection. For
   secure administration, it can also restrict the access rights for configura-
   tion to only one host PC to enhance network security. With this secure
   function enabled, other PCs will not have permission for configuration.
   After the installation program on the Advantech IEDG Series Driver
   Utility CD-ROM is finished, the serial device servers will be ready for
   use and configure.
   Advantech Serial Device Server Configuration Utility is an excellent
   device server management tool. You can connect and configure the local
   and remote Advantech serial device servers easily. Moreover, Virtual
   COM port will be enabled in the same utility. Using this utility, you can:
   • Configure the network settings (you can set the IP address, Gateway
     address, and Subnet mask)
   • View and set the serial port parameters ( configure operating mode,
     baud rate, serial port settings and operating mode settings)
   • Perform diagnostic tests (virtual COM port testing, port status list)
   • Perform administrative functions (export and import the serial device
     server setting, manage access IP, a descriptive name, upgrade
     firmware)
   • Configure COM port redirector(virtual COM port)

   You may open the Serial Device Server Configuration Utility from the
   Windows Start Menu by clicking Start Æ All Programs Æ Advantech
   eAutomation Æ Serial Device Server Configuration Utility. The Serial
   Device Server Configuration Utility will appear as below figure.

<!-- pdf page 31 | printed page 23 | footer: Chapter 3 -->

There are four major areas in the serial device server configuration utility.
1.      Serial Device Server List Area: All devices will be searched and
        listed in this area. You can arrange different favorite group and vir-
        tual COM ports.
2.      Serial Device Server Information Area: Click on the serial device
        server or move cursor to the serial device server, the related infor-
        mation will be shown on this area.
3.      Configuration Area: Click on the item on the Device Server List
        Area, the configuration page will display on the area.
4.      Quick Tool Bar: Useful management functions shortcut.

Note:      Please reserve TCP/UDP port 5048 and 5058 in your
           Ethernet network, configuration utility will use these
           ports to communicate with Advantech EKI-1000,
           EDG-4500, and ADAM-4570 serial device servers.

<!-- figure 1 on pdf page 31 at 45,204-349,434 pt | caption: none | text-layer labels: none | nearby labels: 4. | OCR text follows (tesseract, unverified; 77/105 words >= 60, mean confidence 74) -->
Advantech Serial Device Server Configuration
File Yiew Management Tools Help
Servers System Accessible Monitor
ADAM-4571L
Basic
Type J
ADAM-4571L
1.22
Version
Name |ADAM-4571L-4641DB
EKI-1524-220109
Favorites
Ethernet
Ports
[IP Address
Port Type
System Serial Ports
Subnet Mask
Default Gateway
Eth1
Static IP
10.0.0.1
0.0.0.0
COM2
Virtual Com Ports
1
Serial Port Information
Status
Port
Mode
Host IP
Port 1
Virtual Com Mode
Idle
None
2
DAM-4571L
Ethemet Port
Serial Port
aly Undo
Monday, August 25, 2008 6:57:36 PM
<!-- end of figure 1 -->

<!-- pdf page 32 | printed page 24 | footer: ADAM-4570 Series User Manual -->

3.2 Discovering Your Serial Device Server

   3.2.1 Auto Searching
   Advantech Serial Device Server Configuration Utility will automatically
   search all the EKI-1000, EDG-4500, and ADAM-4570 series device
   servers on the network and show them on the Serial Device Server List
   Area of the utility. The utility provides an auto-search function to show
   your device(s) by simply executing the configuration utility program
   from the Start Menu.
   From here all device on the same network domain will be searched and
   display on Device Server List Area. You can click on the device name to
   show the features of the specific device. Click on the "+" before the
   model name (e.g. ADAM-4570), and the utility will expand the tree struc-
   ture to show the individual device name. Click on the "-" before the
   model name (e.g.ADAM-4570), and the utility will collapse the tree
   structure.

   For Example, the ADAM-4570 in this figure is shown "ADAM-4570-
   457001" after expanding the tree structure.

<!-- figure 1 on pdf page 32 at 98,314-352,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 28/43 words >= 60, mean confidence 69) -->
Advantech Serial Device Server Configur:
nU
File View Management Tools Help
Eth
Port 1
Robin
EKI-1528-152601
Serial Ports
System Serial Ports
Virtual Com Ports
1 Ethernet Port
Part
<!-- end of figure 1 -->

<!-- pdf page 33 | printed page 25 | footer: Chapter 3 -->

Note      When you run the Configuration Utility for the first
          time, the default device name is "MAC ID". In this
          case, the device name "ADAM-4570-457001" means
          the device "MAC ID" is "00 D0 C9 45 70 01". You can
          change the default device name in System Tab of
          Device Properties.

Select the device in this sub-tree. The first tab on the “Configuration
Area” shows the summary of “Basic Information” included device type,
version, and name, “Ethernet Information”, and “Serial Port Informa-
tion”. In the serial port information frame, it displays the operation mode,
status and connected host IP.

Click on the “+” before the device name, and the utility will expand the
interfaces on this device server.

<!-- figure 1 on pdf page 33 at 62,250-328,451 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 63/88 words >= 60, mean confidence 70) -->
Advantech Serial Device Server Configuration Utility
File View Management Tools Help
Serial Device Servers
system Event PortEvent Mail Alert SNMP Trap
EKE-1522
Robin
type
Version J
1.65
EKI-1526
EKI-1526-152601
Name
Favorites
Serial Ports
‘System Serial Ports
Ethernet Information
Virtual Com Ports
‘Static
10.0.0.1
0.0.0.0
Serial P
Host IP
Mode
Port
Status
Virtual Com Mode Idle
Port1
VirtualCom Mode
None
Apply Undo
FF 01:20:14
<!-- end of figure 1 -->

<!-- pdf page 34 | printed page 26 | footer: ADAM-4570 Series User Manual -->

Click on each item, you will entry the configuration page to change the
setting. The configuration will be introduced on following sections.

<!-- figure 1 on pdf page 34 at 124,53-256,216 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 22/32 words >= 60, mean confidence 72) -->
Serial Device Servers
ADAM-4570
Eth 1 (10.0.0.1)
Port 2
Robin
EKI-1526
EKI-1526-152601
_B Favorites
Serial Ports
System Serial Ports
Virtual Com Ports
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 34 at 65,283-332,487 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 58/83 words >= 60, mean confidence 68) -->
Advantech Serial Device Server Configuration Utility
View Management Tools Help
File
Serial Device Servers
ADAM-4570
Launch Browser
Eth
MAC Address
Port 2
{Static IP
Robin
IP Address
10.0.0.1
EKI-1526-152601
Subnet Mask
B Favorites
Serial Ports
‘System Serial Ports
Virtual Com Ports
DNS Setting
[Automatic
Primary DNS Server
‘Secondary DNS Server
DHCP Advanced
Timeout(s)
DHCP
pply Un
FF 01:23:00
<!-- end of figure 2 -->

<!-- pdf page 35 | printed page 27 | footer: Chapter 3 -->

3.2.2 Clearing the Device List and Searching Again
You can click the      button on the “Quick Tool Bar”; utility will clear
all list device servers in the Serial Device Server List Area and re-search
again. Don’t use this function frequently. The warning message will be
pop-up when you double click this button.

You can click the      button on the “Quick Tool Bar”; utility will search
serial device server on local LAN.

<!-- figure 1 on pdf page 35 at 69,53-325,247 pt | caption: none; nearest centred text below: "3.2.2 Clearing the Device List and Searching Again" | text-layer labels: none | OCR text follows (tesseract, unverified; 53/84 words >= 60, mean confidence 68) -->
D
File View Management Tools Help
Serial
Basic Operation Advanced
ADAM-4570
Description
Eth 1(10.0.0.1)
Type
Port2
Baud Rate
Robin
None
Parity
B Favorites
Serial Ports
Data Bits
‘System Serial Ports
Virtual Com Ports
Stop Bits
1
Flow Control
‘Serial Port 1
‘9600 bps, N81
flow control
Apply Alll Ports
Ap do
FF 01:24:27
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 35 at 136,348-249,408 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 94) -->
Please do not refresh so frequently.
<!-- end of figure 2 -->

<!-- pdf page 36 | printed page 28 | footer: ADAM-4570 Series User Manual -->

3.2.3 Manual Appending
Using “Add IP address to Favorite” or “Search a Range of IP addresses”
function, you are able to add one device or group of devices to
“Favorites”. These devices can locate on local network domain or other
network domain.

<!-- figure 1 on pdf page 36 at 62,122-330,317 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 35/55 words >= 60, mean confidence 65) -->
Advantech Ser:
Device Serve:
File
Hele
ool:
Management
2 Serial Device Serv
WB
EKI-1526
EKI-1526-000001
Favorites
Serial Ports
a
System Serial Ports
Virtual Com Ports
Input IP address
92.168.0.1]
Friday, June 27, 2008 1:08:15 PM
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 36 at 62,331-330,525 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 44/65 words >= 60, mean confidence 68) -->
Advantech Ser:
Device Serve:
File
Help
Viev
Mar
ement
Device Servers
WB
EKI-1526
EKI-1526-000001
Favorites
8 Serial Ports
System Serial Ports
Virtual Com Ports
Please input a vaild IP range
Start IP Address.
End IP Address
192.168.0.1
Cancel
Friday, June 27, 2008 1:09:08 PM
<!-- end of figure 2 -->

<!-- pdf page 37 | printed page 29 | footer: Chapter 3 -->

3.3 Setting Ethernet Parameters

   This section explains how to configure the ADAM-4570 series network
   using this utility so that it can communicate over a network with serial
   devices.
   Click on the "+" before the model name (e.g. ADAM-4570), and the util-
   ity will expand the tree structure to show the individual device name. And
   click on the “+” before the device name, and the utility will expand the
   interfaces on this device server. Select the Ethernet interface (Eth1).

   MAC Address:
   The MAC address is for the local system to identify and locate each serial
   device servers. This MAC address is already set before delivery from fac-
   tory, hence no need for further configuration.

   IP Address, Subnet Mask, Default Gateway:
   The IP address identifies your Advantech serial device server on the glo-
   bal network. Each ADAM-4570 series has the same default IP address
   10.0.0.1. Obtain these specific IP addresses from your network adminis-
   trator and then configure each Advantech serial device server with indi-
   vidual IP addresses, related Subnet Mask and Gateway Setting.
   You can choose from four possible IP configure modes: Static, DHCP,
   BOOTP, and DHCP/BOOTP.

<!-- figure 1 on pdf page 37 at 84,170-316,345 pt | caption: none | text-layer labels: none | nearby labels: MAC Address: | OCR text follows (tesseract, unverified; 54/83 words >= 60, mean confidence 67) -->
Advantech Serial Device Server Configuration Utility
File View Management Tools Help
Serial Device
B
Launch Browser
ADAM-4570-457001
MAC Address
Port2
IP Address
5
EKI-1526-152601
‘Subnet Mask
Serial Ports
‘System Serial Ports
Default Gateway
Virtual Com Ports
‘Secondary DNS Server
Ethernet Port 1
|MAC:
DHCP Advanced Setting
‘Static IP Address: 10.0.0.1
180
DHCP
FF 01:33:07
<!-- end of figure 1 -->

<!-- pdf page 38 | printed page 30 | footer: ADAM-4570 Series User Manual -->

Static IP
User defines IP address, Subnet Mask, Default Gateway, and DNS.

DHCP + Auto-IP
DHCP server assigns IP address.

BOOTP + Auto-IP
BOOTP server assigns IP address.

DHCP + BOOTP + Auto-IP
DHCP server assigns IP address, Subnet Mask, Default Gateway, and
DNS or BOOTP server assigns IP address (If DHCP server does not
respond).

DNS Setting
In order to use DNS feature, you need to set the IP address of DNS server
to be able to access the host with the domain name. The ADAM-4570
serial device server provides Primary DNS server and Secondary DNS
server configuration items to set the IP address of the DNS server. Sec-
ondary DNS server is included for use when Primary DNS sever is
unavailable.

<!-- figure 1 on pdf page 38 at 136,58-256,137 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 17/20 words >= 60, mean confidence 80) -->
Launch Browser
MAC Address
IP
Static IP
DHCP Auto-IP
Bootp Auto-IP
Boo tp Auto-IP
DHCP
Default Gateway
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 38 at 139,142-249,190 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 80) -->
DNS Setting
Primary DNS Server
foooo
Secondary DNS Server
<!-- end of figure 2 -->

<!-- pdf page 39 | printed page 31 | footer: Chapter 3 -->

   DHCP Timeout(s)
   If you select DHCP as IP configuration mode, the ADAM-4570 will retry
   DHCP timeout(s) (default: 180s) until network settings are assigned by
   the DHCP server. If the DHCP/BOOTP server is unavailable, the
   ADAM-4570 will use Address auto configuration (based on RFC 3330
   and RFC 3927) for IP setting.

   Note   When you have finished the configuration of these set-
          tings for each category, please press the “Apply” button in
          order to make these settings effective on the Serial
          Device Server. (Will reboot your Serial Device Server)

3.4 Setting Serial Parameters

   This section explains how to configure the ADAM-4570 series serial
   communication parameters using this utility. There are various operation
   modes that are suitable for different application.
   Click on the "+" before the model name (e.g. ADAM-4571L), and the
   utility will expand the tree structure to show the individual device name.
   And click on the “+” before the device name, and the utility will expand
   the interfaces on this device server. Select the serial interface (Port1).

<!-- figure 1 on pdf page 39 at 69,343-328,540 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 53/71 words >= 60, mean confidence 72) -->
D
d
File View Management Tools Help
Serial Device Servers
Operation Advanced
Description
J
B ADAM-4571L-A641DB
(10.0.0.1)
RS-232
Port 1
ype
vorites
tial Ports
Baud Rate
9600
7
System Serial Ports
Virtual Com Ports
Parity
None
Data Bits
8
Stop Bits
1
Flow Control
None
Apply Undo
thursday, August 28, 2008 6:15:29 PM
<!-- end of figure 1 -->

<!-- pdf page 40 | printed page 32 | footer: ADAM-4570 Series User Manual -->

3.4.1 Basic Configuration
Description:
You can give a more detailed description on the function of the port for
easier management and maintenance. Descriptions have a limit of 128
characters.

Baud Rate:
The ADAM-4570 series supports baud rate from 50 to 921.6Kbps. While
setting the baud rate, please note that the value should conform to the cur-
rent transmission speeds of connected devices.

Parity:
ADAM-4570 series provides 5 options: None, Odd, Even, Space, and
Mark.

<!-- figure 1 on pdf page 40 at 172,254-265,329 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 89) -->
14400
19200
38400
57600
115200
460800
921600
None
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 40 at 170,413-265,461 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 97) -->
None
Odd
Even
Mark
Space
<!-- end of figure 2 -->

<!-- pdf page 41 | printed page 33 | footer: Chapter 3 -->

Data Bits:
The ADAM-4570 series provides four options: 5, 6, 7 and 8.

Stop Bits:
The ADAM-4570 series provides three options: 1, 1.5 and 2.

Flow Control:
The ADAM-4570 series provides four options: None, XOn/XOff, RTS/
CTS, and DTR/DSR.

<!-- figure 1 on pdf page 41 at 172,77-268,125 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 96) -->
5
None
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 41 at 167,317-263,357 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 68) -->
None
RTS/CTS
DTR/DSR
<!-- end of figure 2 -->

<!-- pdf page 42 | printed page 34 | footer: ADAM-4570 Series User Manual -->

3.4.2 Operation Mode Configuration
COM Redirector Setting:
The Advantech serial device servers extend traditional COM ports of a
PC to Ethernet access. Through Ethernet networking, users can control
and monitor remote serial devices and equipments over LAN or WAN.
Advantech serial device servers come with a COM port redirector
(Virtual COM driver) that transmits all serial signals intact. This means
that your existing COM-based software can be preserved, without modi-
fying to fulfill the needs. The Virtual COM mode allows user to continue
using RS-232 serial communications software that was written for pure
serial communication applications.
The ADAM-4570 series comes with COM port redirector (virtual COM
driver) that work with series comes with COM port redirector Window
2000/XP/Vista systems. The driver establishes a transparent connection
between host and serial device by mapping the IP of Advantech serial
device server serial port to a local COM port on the host computer.
The ADAM-4570 series provides Multi-access function through Ethernet
connection path. Allow the maximum of 5 connections to open one serial
port simultaneously. In this mode, all connection has to use the same
serial setting. If one serial setting of these connections is different from
others, the data communication may operate incorrectly.

<!-- figure 1 on pdf page 42 at 62,326-330,528 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 79/101 words >= 60, mean confidence 75) -->
Advantech Serial Device Server Configuration
Yiew Management Tools Help
Serial Device Servers
Basic Operation Advanced
Virtual Com Mode
Operation Mode
Eth1 (10.0.0.1)
Virtual Com Mode Configuration
Port 1
Basic Settings
Enable Host Idle Timeout
JQ Favorites
Host Idle Timeout
60
Serial Ports
7
System Serial Ports
Enable Response Timeout
Virtual Com Ports
Response Timeout
ne Breal
r
vab
Frame Break {ms}
Por 1
Static IP Addr
0.
Subnet Mask:
Default Gateway: 0.0.0.0
pply
Friday, August 29, 2008 10:39:40 AM
<!-- end of figure 1 -->

<!-- pdf page 43 | printed page 35 | footer: Chapter 3 -->

Host Idle Timeout (10 to 255 seconds):
The "Host Idle Timeout" setting monitors the connection between the
host and the device. If the "Host Idle Timeout" setting time is reached, the
device server will release the resources allocated to the port mapping.
This prevents a stalled host from affecting the connective device.

Note    The default value of "Host Idle Timeout" is 60 seconds.

The ADAM-4570 series provides Multi-access function through Ethernet
connection path. Allow the maximum of 5 connections to open one serial
port simultaneously. In the mode, all connection has to use the same
serial setting. If one serial setting of these connections is different from
others, the data communication may operate incorrectly.
There are two operating mode of Multi-access function. One is Normal
mode; another is Round-Robin mode.

Normal mode:
Disabling “Response Timeout” parameter, the ADAM-4570 series will
operate in “normal mode”. When multiple hosts open the serial port
simultaneously, the ADAM-4570 series only offers control ability for the
first connected host and provides data communication function for others.
Each serial port supports up to five simultaneous connections, so multiple
hosts can transmit/receive data to/from the same serial port simulta-
neously. Every host can transmit data to the same serial port, and the
ADAM-4570 series will also transmit data to every hosts. When the mul-
tiple hosts transmit data to the same serial port at the same time, the
received data from Ethernet and the outputs of serial port are mixed.
When the ADAM-4570 series receives data from serial port, the data will
also be transmitted to the connected hosts simultaneously.

Note          This operating mode is suitable for the one major
              host send the command and others hosts just lis-
              ten the data from serial port. If two of connected
              hosts send the command at the same time, it is
              possible that ADAM-4570 series serial device
              server will not handle the command and will
              response the incorrect data.

<!-- pdf page 44 | printed page 36 | footer: ADAM-4570 Series User Manual -->

Round-Robin mode:
Enabling “Response Timeout” parameter, the ADAM-4570 series will
operate in “Round-Robin mode”. Each serial port supports up to five
simultaneous connections, so multiple hosts can transmit/receive data to/
from the same serial port simultaneously. Every host can transmit data to
the same serial port simultaneously, but the ADAM-4570 series will pro-
cess the data communication in order. ADAM-4570 series will process
the first host’s request and reply the response to the first host. ADAM-
4570 serial device server can determine the end of the serial acknowl-
edgement via response timeout. When ADAM-4570 serial device server
receives nothing from serial port after the setting of response timeout, the
device will reply the acknowledgement to the host and then process the
next host’s request. While the connected hosts are more and “Response
Timeout” is long, the process time is much longer.

Frame Break is a very import parameter for Round Robin mode. This
parameter is the smart way to reduce inefficient waiting time and the
ADAM-4570 series can transmit data more efficiently. Disabling the
Frame Break function, the ADAM-4570 series will wait “Response Tim-
eout” period, whether the device have transmitted the data. During this
period, the commands from hosts will be queued and the ADAM-4570
series just processes this command. Enabling “Frame Break”, if the serial
port idle is longer than the “Frame Break” period, ADAM-4570 series
will assume the communication is completed and continue the next host’s
query. This is an efficient way to reduce the waiting time and improve the
performance.

3.4.3 Data Mode (USDG Mode)
The ADAM-4570 series can be Data Server or Data Client either. Both
operations support TCP and UDP protocol. The ADAM-4570 series
makes your serial devices behave just like networking devices. You can
issue commands or transmit data from serial devices, which connected to
the ADAM-4570 series, to any devices that are connected to the Internet.
The ADAM-4570 series allows most 5 host PCs accessing data simulta-
neously via polling networking architecture. You can use it according to
your application. If you want to access the ADAM-4570 series, you must
ascertain your application software supports standard networking appli-
cation programming interface (API) such as: WinSock Socket.
You might select “USDG Mode” as the following figure to change the
mode of the port to TCP server/client or UDP mode.

<!-- pdf page 45 | printed page 37 | footer: Chapter 3 -->

Protocol
The ADAM-4570 series provides TCP/IP and UDP two protocols. In
settings, you can choose either TCP mode or UDP mode according to
your application.

Data Listen Port
The TCP/UDP port number represents the source port number, and the
number is used to identify the channel for remote initiating connections.
Range: 1024-65533. If an unknown caller wants to connect to the system
and asks for some services, they need to define the TCP/UDP port to
carry a long-term conversation.

Each node on a TCP/IP network has an IP address, and each IP address
can allow connections on one or more TCP port. The well known TCP
ports are those that have been defined; for example, port 23 is used for
Telnet connections. There are also custom sockets that users and develop-
ers define for their specific needs. The default TCP/UDP port of the
ADAM-4570 series is 5300. The example initial 5300 is System Port, and
5301 is Data Port. But users can adjust them by one's preference or appli-
cation.
Each port has its own data listen port to accept connected request of other
network device. So, the data listen port can’t be set the same value. You
can transmit/receive data to/from device via the data listen port.

<!-- figure 1 on pdf page 45 at 103,53-273,154 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 44/61 words >= 60, mean confidence 75) -->
Basic Operation advanced
Mode
Operation Mode
Mode |DataMode
\re Peers to Receiving Data (0/16)
Enable Auto Connect
Timeout
Data Listen Port
Local Address
Peer Port
Response Timeout (ms)
‘Command Listen Port
Enable Frame Break
Frame Break (ms)
Basic Settings
Enable
Data Idle Timeout (s)
<!-- end of figure 1 -->

<!-- pdf page 46 | printed page 38 | footer: ADAM-4570 Series User Manual -->

Command Listen Port
Each port has its own command listen port to accept connected request of
other network device. So, the command listen port can’t be set the same
value. You can use ‘AT command’ to change the port setting via the com-
mand listen port. The Command Listen Port should be different from the
Data Listen port.

Data Idle Timeout
The default is 60 seconds. If you want to keep connection continually,
you can disable the Data Idle Timeout. Data idle Time is the time period
in which the device waits for data. If the ADAM-4570 series does not
receive data over an established idle time, the ADAM-4570 series will
disconnect temporarily. When the data comes to the ADAM-4570 series,
it will reconnect automatically. Users do not need to reconnect.

Enable Time Sharing
The ADAM-4570 series provides Multi-access function through Ethernet
connection path. Allow the maximum of 5 connections to open one serial
port simultaneously. In the mode, all connection has to use the same
serial setting. If one serial setting of these connections is different from
others, the data communication may operate incorrectly.

There are two operating mode of Multi-access function. One is Normal
mode; another is Round-Robin mode.

• Normal Mode
Disabling “Response Timeout” parameter, the ADAM-4570 series will
operate in “normal mode”. When multiple hosts open the serial port
simultaneously, the ADAM-4570 series only offers control ability for the
first connected host and provides data communication function for others.
Each serial port supports up to five simultaneous connections, so multiple
hosts can transmit/receive data to/from the same serial port simulta-
neously. Every host can transmit data to the same serial port, and the
ADAM-4570 series will also transmit data to every hosts. When the mul-
tiple hosts transmit data to the same serial port at the same time, the
received data from Ethernet and the outputs of serial port are mixed.
When the ADAM-4570 series receives data from serial port, the data will
also be transmitted to the connected hosts simultaneously.

<!-- pdf page 47 | printed page 39 | footer: Chapter 3 -->

• Round-Robin Mode
Enabling “Response Timeout” parameter, the ADAM-4570 series will
operate in “Round-Robin mode”. Each serial port supports up to five
simultaneous connections, so multiple hosts can transmit/receive data to/
from the same serial port simultaneously. Every host can transmit data to
the same serial port simultaneously, but the ADAM-4570 series will pro-
cess the data communication in order. The ADAM-4570 series will pro-
cess the first host’s request and reply the response to the first host. The
ADAM-4570 series serial device server can determine the end of the
serial acknowledgement via response timeout. When ADAM-4570 series
serial device server receives nothing from serial port after the setting of
response timeout, the device will reply the acknowledgement to the host
and then process the next host’s request. While the connected hosts are
more and “Response Timeout” is long, the process time is much longer.

Frame Break is a very import parameter for Round Robin mode. This
parameter is the smart way to reduce inefficient waiting time and the
ADAM-4570 series can transmit data more efficiently. Disabling the
Frame Break function, the ADAM-4570 series will wait “Response Tim-
eout” period, whether the device have transmitted the data. During this
period, the commands from hosts will be queued and the ADAM-4570
series just processes this command. Enabling “Frame Break”, if the serial
port idle is longer than the “Frame Break” period, the ADAM-4570 series
will assume the communication is completed and continue the next host’s
query. This is an efficient way to reduce the waiting time and improve the
performance.

Peer Number
Set the number of network device which you want to connect. You can
set maximum sixteen network devices which you want to connect. You
need to fill out the IP Address and Port of network devices which you
want to connect.

<!-- pdf page 48 | printed page 40 | footer: ADAM-4570 Series User Manual -->

3.4.4 Control Mode (USDG Mode)
In controlling mode, the ADAM-4570 series presents a modem interface
to the attached serial device: it accepts AT-style modem commands to
connect / disconnect to other networking device. If you want serial device
running application program to connect/disconnect to different devices
dynamically, you can use controlling mode.
The “Control mode” provides three kinds of modem AT-style commands.
The serial devices can use these commands to control the ADAM-4570
series to connect/disconnect to remote networking device. Thus, intelli-
gent serial devices such as standalone PLC will send /receive data to/from
devices one by one via Ethernet.

<!-- figure 1 on pdf page 48 at 120,53-275,218 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/13 words >= 60, mean confidence 89) -->
to Receiving Data (0/16)
Local Port
PeerIP Address
Peer Port
Add
Delete
<!-- end of figure 1 -->

<!-- pdf page 49 | printed page 41 | footer: Chapter 3 -->

   Please refer to the Data Mode (USDG Mode) to setup the Data Listen
   Port, Command Listen Port, and Data Idle Timeout.

   Hangup Character
   The default character is “+”. After you have connected to another serial
   device via ADAM-4570 series, you may need to disconnect. Then you
   can use the command "+++" to disconnect. To do this leaves your key-
   board idle (don't press any keys) for at least several seconds, then press
   "+" three times. You can set "Guard Time" to define the idle time. Be sure
   that you have to press "+" over the idle time.

   Guard Time
   The default value is 1000 ms.

Example: <Guard Time> + <Guard Time> + <Guard Time> +

   The following commands are available for the ADAM-4570 series.

<!-- figure 1 on pdf page 49 at 45,55-187,211 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 32/39 words >= 60, mean confidence 80) -->
USDG Mode
Operation Mode
Mode Mode Control Mode Configuration
Protocol
‘Common Settings
Hangup Character
Data Listen Port
Guard Time (ms)
Command Listen Port
1000
Basic Settings
Enable
Data Idle Timeout (s)
60
<!-- end of figure 1 -->

<!-- pdf page 50 | printed page 42 | footer: ADAM-4570 Series User Manual -->

3.4.5 AT Command List

Command       Function
ATDT<IP       “Forms a TCP connection to the specified host.
address>      Ex: ATDT 192.0.55.22:5201
<TCP port>    In above example, the ADAM-4570 series serial
<CR>          device server forms a raw TCP connection to the
              networking device (192.0.55.22). The TCP port is
              5301.”
ATA <CR>      Answering an incoming call
+++<CR>       Returns the user to the command prompt when
              entered from the serial port during a remote host
              connection.
<LF><CR> OK   Commands are executed correctly
<LF><CR>
<LF><CR>      Connect to other device
CONNECT
<LF><CR>
<LF><CR>      Detect the connection request from other device,
RING          which IP address is ddd.ddd.ddd.ddd.
ddd.ddd.ddd
<LF><
CR>
<LF><CR>      Disconnect from other device
DISCONNECT
<LF><CR>
<LF><CR>      Incorrect commands
ERROR
<LF><CR>
<LF><CR>      If you issue an ATDT command and cannot con-
FAIL          nect to the device, it will response “FAIL”.
<LF><CR>

<!-- pdf page 51 | printed page 43 | footer: Chapter 3 -->

  3.4.6 Advanced Settings
  The serial device server provides the advanced settings for some special
  applications which need critical time requirements. In normal applica-
  tions, these settings are recommended not to be set to avoid the unusual
  action happened.

  Delay Time (ms)
  When enabled, the serial port will postpone the received data for the time
  interval you set, and then send the received data to the TCP/IP network.
  Ignore Purge
  Some application program will purge the serial port the first time opens
  this serial port. You can ignore the purge command by enable this option.
  Disable Character Timeout Detection
  Enable this option will disable the serial port character timeout detection.
  Disable Multiple Connection
  Enabling this option will disable the multi-access function, thus the only
  one TCP connection is allowed on this serial port.

Note   These settings are just for special applications. We recom-
       mend not enabling advanced settings in normal usage.

<!-- figure 1 on pdf page 51 at 77,113-320,293 pt | caption: none | text-layer labels: none | nearby labels: Delay Time (ms) | OCR text follows (tesseract, unverified; 35/80 words >= 60, mean confidence 50) -->
Advant
Serial Device Serve:
Utility
FR Toots Help
Banc Ad
Settings
Tine
2
Delay Time
Page
Pot
Pot
Pot?
Pot 8
Pot 9
Poul
Pot 12
are
Potts
Wechesday, October OL, 2008 3:41 05 PM
<!-- end of figure 1 -->

<!-- pdf page 52 | printed page 44 | footer: ADAM-4570 Series User Manual -->

3.5 Security Configuration

   3.5.1 Accessible Function

   Allow any IP to access:
   The default option, any host PC can communicate with this serial device
   server.

   Specified IP which can access:
   Type the IP address in the column and click “Add” or “Delete” button to
   make the accessible IP address list. The limit of this list is 32 IP
   addresses.

<!-- figure 1 on pdf page 52 at 72,89-318,276 pt | caption: none | text-layer labels: none | nearby labels: 3.5.1 Accessible Function | Allow any IP to access: | OCR text follows (tesseract, unverified; 60/97 words >= 60, mean confidence 65) -->
Advantech Serial Device Server Configuration Utility
File Management Tools Help
System Accessible Monitor
Serial Device Sewer
Setting
Eth1
Allow any IP to access
1
Specified IP which can access
Accessible IP Address (0/32)
EKI-1524-A64227
dd
Favorites
Serial Ports
4
‘System Serial Ports
‘Virtual Com Ports:
‘Static IP Address: 172.18.6.115
MAC:
‘Static IP Address: 172.18.6.116
Friday, August 29, 2008 11:41:18 AM
<!-- end of figure 1 -->

<!-- pdf page 53 | printed page 45 | footer: Chapter 3 -->

3.5.2 Port Monitor

Configuration utility provides an excellent function that allows monitor-
ing the serial ports’ status. It will present each serial port’s operation
mode and status. The IP address of Host PC which is communicating with
serial port will be list on the right window. Click “Refresh” button, the
status will be refresh once. It will be auto refresh after click “Auto
Refresh” and the time duration is depending on the setting (the default
value is 1000ms).

<!-- figure 1 on pdf page 53 at 69,53-328,250 pt | caption: none | text-layer labels: none | nearby labels: 3.5.2 Port Monitor | OCR text follows (tesseract, unverified; 58/84 words >= 60, mean confidence 70) -->
D
d
File View Management Tools Help
Serial Device Servers
Summary System| Accessible Moritor
Refresh [1000 ms
Sort host IP addresses
[Mode
[Status
Port 1
Port
Port 1
Virtual Com Mode
Idle
Favorites
Setial Ports
‘System Serial Ports
Virtual Com Ports
El
2 Port
Latest Update Time |11:43:42
Serial Port
Undo
Apply
Friday, August 29, 2008 11:43:51 AM
<!-- end of figure 1 -->

<!-- pdf page 54 | printed page 46 | footer: ADAM-4570 Series User Manual -->

3.6 Fulfilling Administrator Functions

   The configuration utility provides several administrator settings for easy
   management and configuration. Right click the mouse on the device
   name in the sub-tree of Serial Device Sever List Area, and select these
   administrator settings.

   3.6.1 Import/Export Serial Port Setting
   The utility allows importing or exporting the serial port setting including
   “Basic Setting” and “Operation Setting” via “.sps” file format.

<!-- figure 1 on pdf page 54 at 74,355-320,533 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 63/94 words >= 60, mean confidence 67) -->
Fil
Ip
Tools
view
Management
Q
Select the Serial Port Set
file
Device Ser
a ADAM-4571
EKI-1524-utilty.sps
Port
My Recent
Documents
EKI-1526
Desktop
_B Favorites
Ports
System Seria
Virtual Com PF
My Documents
My Computer
m
DB
MAC: 0
My Network
Save
File name:
‘Static IP Address: 10.0.
Save as type:
[SPS files
Cancel
Appl Und
Friday, August 29, 2008 11:
15 AM
<!-- end of figure 1 -->

<!-- pdf page 55 | printed page 47 | footer: Chapter 3 -->

3.6.2 Locate Serial Device
If there are many serial device servers need your management, you may
need to identify which unit is correct to configuration on utility. Click
“Locate” to make that unit’s “Status” LED be steady on until you click
“Stop Locate”.

3.6.3 Lock Device
The configuration utility provides the “Lock Device” function to make it
more confidential. You need to set up a password while the first time
clicking “Lock Device”. Be sure to click “Reset Device” to restart the
serial device server and store your setting password into the memory.

Click “Unlock Device” to unlock the serial device server, and you need to
fill in the password you have set up before. If you forgot the password,
the only way to solve this problem is to restore the setting of the serial
device server to the factory default which will be introduced next section.

<!-- figure 1 on pdf page 55 at 65,218-330,417 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 32/48 words >= 60, mean confidence 67) -->
Advantech Serial Device Server Configuration
tility
File View Management Tools Help
vers
EKI-1524-22010:
Favorites
Setial Ports
7
System Serial Ports
Virtual Com Ports
Be locked
r
Friday, August 29, 2008 11:54:35 AM
<!-- end of figure 1 -->

<!-- pdf page 56 | printed page 48 | footer: ADAM-4570 Series User Manual -->

If you want to disable this function or change the password, click
“Change Password” to change the password to default “None” (leave the
new password and confirm new password columns blank) to disable this
function or other password you want to change. Be sure to click “Reset
Device” to restart the serial device server and store the new password into
the memory.

3.6.4 Restore to Factory Default Settings
The configuration utility provides this function to let you can restore the
serial device server to factory default settings. The confirm message will
be pop-up while clicking “Restore to Factory Default Settings”. If you
really want to restore the serial device server to factory default settings,
please click “Yes” button to continue.

<!-- figure 1 on pdf page 56 at 62,53-330,257 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 74/105 words >= 60, mean confidence 70) -->
Device Server Configuration
Advantech
Yiew Management Tools Help
Summary System Accessible Monitor
Device Servers
Basic Information
Version J
ADAM-4571L
1.22
Type
524-220"
Name
EKI-1526
Ethernet Information
Favorites
[Type
LIP Address
I Gateway
Serial Ports
Port
Subnet Mask
System Serial Ports
Eth1
Static IP
10.0.0.1
255.0.0.0
Virtual Com Ports
Be unlocked
Port Information
[Host IP
Port
Status
Port 1
Virtual Com Mode
Idle
None
:DB
Static IP Address: 10.0.0.1
Friday, August 29, 2008 11:57:09 AM
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 56 at 103,449-287,509 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/17 words >= 60, mean confidence 86) -->
e confirm
4re you sure to reset the device setting to the Factory default?
Yes
No
<!-- end of figure 2 -->

<!-- pdf page 57 | printed page 49 | footer: Chapter 3 -->

Then, please power off the serial device server within ten seconds, after
reconnecting the power back, the all setting will be reset to the factory
default. If the power remains more than ten seconds, the serial device
server will not have any changes.

3.6.5 Upgrading the Firmware
Advantech continually upgrades its firmware to keep up with the ever-
expanding world of computing. You can use the update firmware
function in the utility to carry out the upgrade procedure. Please access
Advantech’s Website at http://www.advantech.com to download the
latest version of the firmware.
Right click on the device name and select “Update Firmware” function.

<!-- figure 1 on pdf page 57 at 100,103-292,218 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 56/57 words >= 60, mean confidence 94) -->
Power off device count down
If you want to restore the device setting to default, please power off
the device within 10 seconds.
After reconnecting the power back, the setting will be reset to the
factory default.
If the power remains more than 10 seconds, the device will not have
any change.
3 seconds remain
Jk
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 57 at 72,357-352,561 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 85/118 words >= 60, mean confidence 73) -->
Advantech Serial
Server Cont
nU
Management Tools Help
B
te Serial Device Servers
ADAM-4571L
5
Version J
1.22
(10.
Port 1
Import Serial Port Setting
Export Serial Port Setting
Refresh Data
EKI-1526
Locate
IP Address
‘Subnet Mask
Default
10.0.0.1
255.0.0.0
0.0.0.0
Lock Device
Ports
Restore to Factory Default Settings
System Serial
Virtual Com Ports:
Reset Device
Add to Favorite
[Host iP
[Status
Auto Mapping
Idle
None
Update Firmware
Ethernet Port
MAC:
‘Static IP Address: 10.0.0.
Apply Undo
Friday, August 29, 2008 12:03:20 PM
49
Chapter;
<!-- end of figure 2 -->

<!-- pdf page 58 | printed page 50 | footer: ADAM-4570 Series User Manual -->

Select the firmware you want to update.

After downloading the firmware completely, click on the “OK” button.
The serial device server will restart automatically.

Note:   Be sure that the host PC Ethernet network domain is
        as same as the ADAM-4570 series device server
        while doing the updating firmware process.

<!-- figure 1 on pdf page 58 at 72,67-325,245 pt | caption: none | text-layer labels: none | nearby labels: Select the firmware you want to update. | OCR text follows (tesseract, unverified; 9/30 words >= 60, mean confidence 44) -->
Select the binary image file
Bad
11522¥122_8
files bin)
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 58 at 84,302-309,437 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/18 words >= 60, mean confidence 80) -->
Firmware Update
Device Type: EKI-1522
Device Name: EKI-1522-A6E62B
IP 10.0.0.2
Device Version:1.21
Update Complete
OK
<!-- end of figure 2 -->

<!-- pdf page 59 | header: CHAPTER -->

Setting the COM
Redirector

<!-- figure 1 on pdf page 59 at 294,38-347,96 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 60 | printed page 52 | footer: ADAM-4570 Series User Manual -->

Chapter 4 Setting the COM Redirector
   Advantech Serial Device Sever Configuration Utility also creates virtual
   COM ports that Windows applications will use to communicate with
   remote serial devices. Advantech virtual COM ports follow the same
   naming/numbering convention as Windows COM ports.

4.1 Setting COM Redirector (Virtual COM port)

   Advantech COM port mapping software is a serial COM port redirector
   that creates virtual COM ports and provides access to serial devices con-
   nected to Advantech serial device servers. Your serial device applications
   can communicate with serial devices connected to Advantech serial
   device servers without software changes. Since the virtual COM ports
   work like standard Windows COM ports, your application software sees
   no difference between a local serial device and one connected to a Advan-
   tech serial device server.
   COM redirector utility and Virtual COM port Management utility are
   integrated into one utility with same GUI. Advantech Serial Device
   Server Configuration Utility can create all Virtual COM ports using
   “Auto Mapping” function. You can map the Virtual COM port by
   yourself.

   4.1.1 Auto Mapping
   Right click the serial device name on the sub-tree of Device Server List
   area and select the “Auto Mapping” function.

<!-- figure 1 on pdf page 60 at 38,374-318,559 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 73/108 words >= 60, mean confidence 67) -->
d
File View Management Tools
Help
System| Accessible Monitor
Device Servers
a ADAM-4571L
Basic Information
1.22
Por
Import Serial Port Setting
a
Export Serial Port Setting
EKI-1524,
Refresh Data
Locate
[IP
Serial Posts
7
System Serial
255.0.0.0
0.00.0
Lock Device
Virtual Com Pe
Restore to Factory Default Settings
Reset Device
Add to Favorite
[Host iP
Status
fode
Idle
None
Update Firmware
‘Static IP Address: 10.0.0.
Undo
Friday, August 23, 2008 1:15:54 PM
ADAM
<!-- end of figure 1 -->

<!-- pdf page 61 | printed page 53 | footer: Chapter 4 -->

The serial ports that can be assigned to virtual COM will be shown in this
window. Select the serial ports you wish to map or click the <Select All>
button and press <Map Selected Ports> button. The selected serial ports
will be mapped to virtual COM ports in sequential order.

The COM ports in the “Virtual Com Ports” listing are now available for
use by Windows applications.

<!-- figure 1 on pdf page 61 at 79,106-316,254 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/26 words >= 60, mean confidence 76) -->
From System Port |COM 3
Device Type
Device Port System Port
Port 1
Select All Clear All
Close
Map Selected Ports
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 61 at 74,314-313,451 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 42/76 words >= 60, mean confidence 64) -->
Advantech
Device Server Configuration
File View Management Tools Help
B
Setial Device Servers
system Accessible
Vetsion
ADAM-4571L
th
Type
Pott
Name
EKI-1524-220108
[type
[IP Address
Mask
Static IP
Favorites
255.0.0.0
0.0.00
Ports
Com Potts
[Status
Port
Pott 1
Com Mode
Idle
None
<!-- end of figure 2 -->

<!-- pdf page 62 | printed page 54 | footer: ADAM-4570 Series User Manual -->

4.1.2 Manual Mapping
Right click the serial device name on the sub-tree of Device Server List
area and select the “Manual Mapping” function.

ADAM-4570 series have only one IP address. You select the serial port
on the device server and the host COM that you want to set. Press <Map
it> to establish the virtual COM port on the host.

<!-- figure 1 on pdf page 62 at 67,98-325,290 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 90/121 words >= 60, mean confidence 71) -->
Advantech Serial Device Server Configuration Utility
File View Management Tools Help
B
Setial Device Servers
Summary System Accessible Moritor
Basic Information
Version J
1.22
(10.0,
Port 1
Import Serial Port Setting
I
EKI-1524-22010
Export Serial Port Setting
Refresh Data
Locate
IP Address
Subnet Mask
Default Gates
Favorites
10.0.0.1
00.0.0
Lock Device
Serial Ports
7
System Serial Ports
Restore to Factory Default Settings
Virtual Com Ports
Reset Device
COM:
Add to Favorite
[Host IP
[Status
Idle
None
Port 1
MAC:
Static IP Address: 10.0.0.1
Indo
Friday, August 29, 2008 1:18:56 PM
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 62 at 108,360-275,545 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 26/33 words >= 60, mean confidence 78) -->
Manual Mapping Virtual Com Port
Device Type
Device
IP Address 1 10.0.0.1
IP Address 2
Serial Port 1
Com Port 4
Auto Reconnect
Map it
Close
<!-- end of figure 2 -->

<!-- pdf page 63 | printed page 55 | footer: Chapter 4 -->

Auto Reconnect Property:
Sometimes, the connection between Advantech serial device server and
HOST is interrupted by network traffic or powered-off by accident. In
such a situation, the host has to reconnect to Advantech serial device
server. The function "Auto Reconnect" is for this purpose, if the
Advantech serial device server loses the connection to its host, the COM
redirector will try to re-establish the connection while the host’s AP
access the virtual COM port. The COM redirector DOES NOT re-estab-
lish the connection automatically. When the connection is working again,
the host's commands will be automatically received by the Advantech
serial device server again. Reconfiguration is not necessary, so this func-
tion enhances the reliability of the system.

If the function is disabled, the connection can not be re-established again
unless the COM redirector or host is restarted.

Note    If you set the wrong IP address, COM redirector will
        still try to connect the device. It might cause the system
        performance low or other issue

4.1.3 Manual Direct Mapping Virtual COM Port

Click the     button on the Quick Took bar, you can add a target by
selecting the Device Type and inputting the IP address without physically
connecting the serial device server to the network.

<!-- figure 1 on pdf page 63 at 127,408-268,542 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 22/27 words >= 60, mean confidence 80) -->
Device Type
Device
IP Address 1
IP Address 2
Serial Port 1
Host
Com Port |Com 4
Auto Reconnect
Map it
Close
<!-- end of figure 1 -->

<!-- pdf page 64 | printed page 56 | footer: ADAM-4570 Series User Manual -->

4.1.4 Remove the Virtual COM Port
If you want to remove the virtual COM port, you can remove them one by
one or group remove ports.

Individually Remove
Right click on COM port you have mapped before and select “Remove
This Port”.

Group Remove Port
Right click on Virtual Com Ports on Device Server List Area and select
“Group Remove Port”, you can choose which ports you want to remove.

<!-- figure 1 on pdf page 64 at 60,158-335,362 pt | caption: none | text-layer labels: none | nearby labels: Group Remove Port | OCR text follows (tesseract, unverified; 60/98 words >= 60, mean confidence 65) -->
in Ui
Advantech Serial Device Server
File View Management Tools Help
B
Serial Device Servers
Basic Com Port Information
8
Name
JEDG VCOM Port 3 (COM3)
Friendly Name
a} Port 1
Ltd
EKI-1524-220109
Hardware ID
EKI-1526
Service
Favorites
Serial Ports
‘System Serial Ports
Com Port Information:
ADAM-45;
0.0.0.1
1
Remote Com Port
Enable
Auto Reconnect
Update
Friday, August 29, PM
<!-- end of figure 1 -->

<!-- pdf page 65 | printed page 57 | footer: Chapter 4 -->

4.2 Running Diagnostic Test

  The purpose of this test is to make sure the communication from host PC
  to ADAM-4570 series is OK. If there is still an error, you can check the
  communication from the ADAM-4570 series to the devices.
  If the test is selected, an external test will be done to check that the
  connection signals for each port are working properly. For the test, you
  will need to connect each port to a loopback tester (provided in the
  package). The loopback test only applies to RS-232 mode. The test is
  divided into two parts: Signal test and Communication Parameters test.

  Note     Before you do this diagnostic test, you must complete
           the process of virtual COM port mapping (which is
           described in the next chapter 4.1).

<!-- figure 1 on pdf page 65 at 74,53-316,175 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 27/34 words >= 60, mean confidence 77) -->
(x)
Group Remove Ports
Index
Device Type
IP2
Port Auto
10.0.0.1
10.0.0.2
Port 1
COM5
EKI-1522
10.0.0.1
10.0.0.2
Port2
Remove Selected Ports
Close
Select All Clear All
<!-- end of figure 1 -->

<!-- pdf page 66 | printed page 58 | footer: ADAM-4570 Series User Manual -->

Click “Simple Serial Test” on the Tools menu.

Select which COM port you want to run diagnostic test, and then press
“Test” button to process the testing.

<!-- figure 1 on pdf page 66 at 67,53-320,242 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 66/95 words >= 60, mean confidence 70) -->
Advantech Serial Device Server Configuration Utility
File View Manageme
Tor
Simple Serial T
Serial Device Servers
Basic Com Pott Information
Name
Eth1
JEDG VCOM Port 3 (COM3)
Friendly
[Advantech Ltd
I
003
Hardware ID
EKI-1526-438650
Service
Serial Ports
System Serial Ports
Com Port Information
Virtual Com Ports
Model Name
0.0.0.1
IP Address 1
Remote Com Port
Enable
Auto Reconnect
Update
Friday, August 29, 2008 1:51:41 PM
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 66 at 72,302-320,475 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/13 words >= 60, mean confidence 70) -->
Simple Serial Test Tool
Auto Scroll Messages
<!-- end of figure 2 -->

<!-- pdf page 67 | printed page 59 | footer: Chapter 4 -->

Signal Test
• RTS -> CTS check the RTS and CTS signal between two ports
• DTR -> RI check the DTR and RI signal between two ports
• DTR -> DSR check the DTR and DSR signal between two ports
• DTR -> DCD check the DTR and DCD signal between two ports

Communication Parameters Test
• Baud rate: 50bps ~ 921.6kbps
• Data bits: 5, 6, 7, 8
• Stop bit    1, 1.5, 2
• Parity      Odd, Even, None, Space, Mark

When the test is finish, it will show the test result, the click “Exit” button
to return to the utility window.

<!-- figure 1 on pdf page 67 at 67,274-328,456 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 137/139 words >= 60, mean confidence 93) -->
Port {coms
Testing
baud
2400
Space
dataBits
stopBits
1.5
rate
parity:
Testing
baud
4800
Space
dataBits
stopBits
1.5
rate
parit
Testing
baud
7200
Space
dataBits
stopBits
1.5
rate
parit
Testing
baud
9600
Space
dataBits
stopBits
1.5
rate
parit
Testing
baud
14400
Space
dataBits
stopBits
1.5
rate
parit
baud
19200
dataBits
1.5
Testing
Space
stopBits
rate
parity
Testing
baud
38400
Space
dataBits
stopBits
1.5
rate
parity
baud
57600
dataBits
1.5
Testing
Space
stopBits
rate
parity
Testing
baud
115200
Space
dataBits
stopBits
1.5
rate
parity
baud
230400
dataBits
1.5
Testing
Space
stopBits
rate
parity
Testing
baud
460800
Space
dataBits
stopBits
1.5
rate
parity
baud
921600
dataBits
1.5
Testing
parity:
Space
stopBits
rate
All test cases have been done.
840 test cases have been tested
640 test cases were passed.
test cases were failed
Auto Scroll Messages Save Log
Exit
<!-- end of figure 1 -->

<!-- pdf page 68 | printed page 60 | footer: ADAM-4570 Series User Manual -->

(no text layer on this page)

<!-- pdf page 69 -->

                        A
                 APPENDIX
2

    Pin Assignments

<!-- pdf page 70 | printed page 62 | footer: ADAM-4570 Series User Manual -->

Appendix A Pin Assignments
A.1 RS-232 Pin Assignments

A.2 RJ-48 Cable PIN Assignment

  A.2.1 1. RS-422
   Pin No.     Description
   1           Tx-
   4           Tx+
   5           GND
   7           Rx+
   9           Rx-

  A.2.2 2. RS-485
   Pin No.     Description
   1           Data-
   4           Data+
   5           GND

<!-- figure 1 on pdf page 70 at 41,96-132,197 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 19/22 words >= 60, mean confidence 82) -->
Pin No
Description
Pin1
DCD
Pin2
Rx
Pin3
Tx
DTR
GND
Pins
Pin6
DSR
Pin7
RTS
CTS
Ping
Ri
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 70 at 41,230-187,321 pt | caption: none; nearest centred text below: "A.2.1 1. RS-422" | text-layer labels: none | nearby labels: A.2.1 1. RS-422 | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 61) -->
12345 67 8 910
0000,
1234567 8 g
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 70 at 153,345-280,444 pt | caption: none | text-layer labels: none | nearby labels: Description | Tx- | Tx+ | GND | Rx+ | Rx- | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 71 -->

                       B
                APPENDIX
2

    Creating VCOM

<!-- pdf page 72 | printed page 64 | footer: ADAM-4570 Series User Manual -->

Appendix B Creating VCOM
B.1 Configuration Wizard

  1.   First Step
       Click //image:      button on the "Quick Tool Bar" to start the Con-
       figuration Wizard; Select the serial device server you want to create
       the VCOM. (ex. ADAM-4570)

<!-- figure 1 on pdf page 72 at 72,163-318,350 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 68/108 words >= 60, mean confidence 67) -->
Advantech Serial Device Server Configuration Utility
File View Management Tools Help
Serial Device Servers
system Event Mail Alert SNMP Trap
Basic Information
Eth
Port1
1.65
Name
Favorites
Serial Ports
Static IP
0.0.0.0
System Serial Ports
Eth1
Virtual Com Ports
Serial Port Information
Host IP
Mode
status
[Ethernet Port 1
Port
Data Mode
MAC:
Data Mode
|Static IP Address: 172.19.1.183
Mask: 255.255.255.0
Default Gateway: 0.0.0.0
Apply Undo
FF 02:37:30
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 72 at 38,362-318,559 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/37 words >= 60, mean confidence 64) -->
Address 1
Address 2
Address 2
Model Name Device Name
MAC Address 1
EKI-1528-152
172.19.1.191
172.19.1.192
10.0.0.2
Cancel
Previous
ADAM
fA
<!-- end of figure 2 -->

<!-- pdf page 73 | printed page 65 -->

2.   Second Step
     Fill in options of serial device server including "Serial Type", "IP
     address", "Subnet Mask", and "Default Gateway".

3.   Third Step
     Choose Port number of start and select to device port you want to
     create VCOM, then click "Finish" button.

                                 65                             Appendix B

<!-- figure 1 on pdf page 73 at 72,86-323,276 pt | caption: none | text-layer labels: none | nearby labels: 3. | OCR text follows (tesseract, unverified; 15/24 words >= 60, mean confidence 63) -->
Ethernet 1
Setting
MAC Address
Name
IP Address
Port Setting
Type
‘Subnet Mask
Cancel
Previous
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 73 at 67,341-328,537 pt | caption: none | text-layer labels: none | nearby labels: Appendix B | OCR text follows (tesseract, unverified; 11/23 words >= 60, mean confidence 56) -->
From System
Clear All
Device Port
Pi
Port1
Previous
Finish
Cancel
<!-- end of figure 2 -->

<!-- pdf page 74 | printed page 66 | footer: ADAM-4570 Series User Manual -->

Now, you have two mapped VCOM in your host!

<!-- figure 1 on pdf page 74 at 60,70-335,276 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 51/81 words >= 60, mean confidence 66) -->
dvantech Serial Device Server Configuration Utility
View Management Tools Help
File
Fi
Serial Device Servers
Com
[coms
Name
Port 5
Friendly Name
Serial Ports
[Advantech Co,, Ltd
Manufacture
Serial Ports
Virtual Com Ports
Hardware ID
Virtual Com Port
Model Name
IP Address 1
Remote Com Port
[Enable
Auto Reconnect
Update
02:59:13
<!-- end of figure 1 -->
