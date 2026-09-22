<!-- font check: no ToUnicode map in ProximaNova-Bold, ProximaNova-Light, ProximaNova-Semibold, QTypeSquarePro-Light; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1, 88 checked against the rendered page) -->

<!-- pdf page 1 -->

AR200
Augmented Reality Sensor
        Software version: v1.33

    INSTALLATION
   INSTRUCTIONS
                       English (en-US)
                      Date: 09-2024
        Document number: 87372 (Rev 3)
          © 2024 Raymarine UK Limited

<!-- figure 1 on pdf page 1 at 0,175-664,292 pt | caption: none | text-layer labels: none | OCR: no legible text (0/5 words >= 60, mean confidence 27) -->
<!-- figure 2 on pdf page 1 at 705,201-839,241 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

Legal notices

Trademark and patents notice
Raymarine, Tacktick, Pathfinder, ClearPulse, Truzoom, SeaTalk , SeaTalk hs, SeaTalkng , and Micronet, are registered or claimed trademarks of Raymarine
Belgium.
FLIR, Fishidy, Fishing Hot Spots, YachtSense , DockSense, LightHouse, RangeFusion, DownVision, SideVision, RealVision, HyperVision, Dragonfly,
Element, Quantum, Axiom, Instalert, Infrared Everywhere, The World’s Sixth Sense and ClearCruise are registered or claimed trademarks of FLIR
Systems, Inc.
All other trademarks, trade names, or company names referenced herein are used for identification only and are the property of their respective owners.
This product is protected by patents, design patents, patents pending, or design patents pending.

Fair Use Statement
You may print no more than three copies of this manual for your own use. You may not make any further copies or distribute or use the manual in any other
way including without limitation exploiting the manual commercially or giving or selling copies to third parties.

Content notice
Please ensure that you have obtained this document only from Raymarine®, and that it is the latest available version.
There are numerous third-party Internet websites (such as www.manualslib.com ) hosting Raymarine product manuals. These websites are not authorized by
Raymarine® to do so, and are often hosting illegitimate or older versions of Raymarine product manuals, which may contain inaccurate or misleading information.
To obtain the latest official documentation for a Raymarine® product, please visit the official Raymarine® website: https://bit.ly/rym-docs

Artificial Intelligence (AI) content notice
There are numerous third-party Artificial Intelligence (AI) services available to the public, which are capable of providing a summary or transcription of the
information provided by official Raymarine® publications or websites, either in written or audio/video formats. These services may alter, supplement, or convey
the original information provided by Raymarine® in inaccurate or misleading ways.
Please ensure that you have obtained this document only from Raymarine®, and that it is the latest available version.

English (en-US)
Document number: 87372 (Rev 3)
AC;62513;2024-09-30T13:58:37

<!-- pdf page 4 -->

(no text layer on this page)

<!-- pdf page 5 | printed page 5 -->

CONTENTS
CHAPTER 1 IMPORTANT INFORMATION.................... 8
  Safety warnings ................................................................. 8
  Product warnings ............................................................... 8
  Regulatory notices............................................................. 9
           Declaration of conformity .......................................... 9
           Disclaimer..................................................................... 9
           Water ingress .............................................................. 9
           Suppression ferrites ................................................... 9
           Connections to other equipment ........................... 10
           Warranty registration ............................................... 10
           Product disposal ....................................................... 10
           IMO and SOLAS ....................................................... 10
           Technical accuracy ................................................... 10
           Publication copyright ............................................... 10
CHAPTER 2 DOCUMENT INFORMATION.................. 11
  2.1 Applicable products ................................................... 12
  2.2 Document information .............................................. 12
  2.3 Document illustrations .............................................. 12
  2.4 Product documentation ............................................ 12

CHAPTER 3 SOFTWARE DETAILS ............................ 13
  3.1 Applicable software version .................................... 14
  3.2 New software features and improvements .......... 14
  3.3 Software updates ....................................................... 14

CHAPTER 4 PRODUCT AND SYSTEM
OVERVIEW .................................................................. 15

      4.1 AR200 product overview.......................................... 16
          SeaTalk NG ................................................................ 16
      4.2 System examples ...................................................... 17
      4.3 Required additional components ........................... 17

CHAPTER 5 PARTS SUPPLIED.................................. 19
  5.1 Parts supplied ............................................................. 20

CHAPTER 6 PRODUCT DIMENSIONS....................... 21
  6.1 Product dimensions .................................................. 22
  6.2 Product dimensions with Mounting tray ............... 22
  6.3 Product dimensions with Mounting tray and
  Riser.................................................................................... 22
  6.4 Product dimensions with Mounting tray and
  Bulkhead bracket ............................................................. 23
CHAPTER 7 LOCATION REQUIREMENTS ................ 24
  7.1 Warnings and cautions ............................................. 25
  7.2 Location requirements .............................................. 25
  7.3 RF interference .......................................................... 26
  7.4 Compass safe distance ............................................ 26
  7.5 EMC installation guidelines ..................................... 26
            Suppression ferrites ................................................. 27
            Connections to other equipment ........................... 27
CHAPTER 8 INSTALLATION ....................................... 28
  8.1 Installation checklist .................................................. 29
           Schematic diagram .................................................. 29
      8.2 Tools required for installation .................................. 29

<!-- pdf page 6 | printed page 6 -->

     8.3 Mounting options ....................................................... 30
     8.4 Bulkhead mounting ................................................... 30
     8.5 Surface mounting ...................................................... 32
     8.6 Surface mounting using the Riser ......................... 33
     8.7 Releasing the product from the mounting
     tray ...................................................................................... 35
     8.8 Pole or rail mounting ................................................. 35
           Adjusting pole mount alignment............................ 36
CHAPTER 9 CABLES AND CONNECTIONS —
GENERAL INFORMATION .......................................... 37
  9.1 General cabling guidance ........................................ 38
         Cable types and length ........................................... 38
         Cable routing ............................................................. 38
         Strain relief ................................................................. 38
         Cable shielding ......................................................... 38
     9.2 Connections overview .............................................. 38
         Connecting SeaTalk NG cables ............................ 39
         SeaTalk NG product loading .................................. 39
     9.3 System examples ...................................................... 39

CHAPTER 10 POWER CONNECTIONS ..................... 41
  10.1 SeaTalk NG power supply ..................................... 42
         Inline fuse and thermal breaker ratings............... 42
     10.2 SeaTalk NG power cables ..................................... 42
     10.3 SeaTalk NG product loading ................................. 43
     10.4 SeaTalk NG power connection point................... 43
     10.5 SeaTalk NG system loading .................................. 44
     10.6 Power distribution — SeaTalk NG ....................... 44

     10.7 Power connection via Autopilot Control Unit
     (ACU-Series) .................................................................... 46
CHAPTER 11 NMEA 2000 CONNECTION .................. 48
  11.1 NMEA 2000 network connection .......................... 49

CHAPTER 12 SETUP AND CALIBRATION ................. 50
  12.1 Camera setup ........................................................... 51
         Fixed camera calibration ........................................ 51
         Pan and Tilt camera calibration ............................ 52
     12.2 AR200 Calibration (Linearization)........................ 54
           Magnetic deviation ................................................... 54
           AR200 calibration settings ..................................... 54
           Continual monitoring and adaptation .................. 55
           Compass lock ............................................................ 55
CHAPTER 13 SYSTEM CHECKS AND
TROUBLESHOOTING ................................................. 57
  13.1 Augmented Reality (AR) initial test ..................... 58
  13.2 GNSS (GPS) check ................................................ 58
  13.3 Troubleshooting ....................................................... 59
           LED Diagnostics ....................................................... 59
           Switching off sensor LEDs ..................................... 60
           Find me ....................................................................... 60
           GNSS (GPS) troubleshooting................................ 61
           Augmented Reality (AR) Troubleshooting .......... 62
CHAPTER 14 OPERATION ......................................... 63
  14.1 Operation instructions ............................................ 64

<!-- pdf page 7 | printed page 7 -->

CHAPTER 15 MAINTENANCE .................................... 65
  15.1 Service and maintenance ...................................... 66
  15.2 Routine equipment checks .................................... 66
  15.3 Product cleaning ...................................................... 66

CHAPTER 16 TECHNICAL SUPPORT........................ 67
  16.1 Raymarine technical support and
  servicing ............................................................................. 68
          Viewing product information .................................. 69
      16.2 Learning resources ................................................. 69
      16.3 Operation instructions ............................................ 69

CHAPTER 17 TECHNICAL SPECIFICATION.............. 70
  17.1 Power specification ................................................. 71
  17.2 Environmental specification .................................. 71
  17.3 GNSS (GPS) receiver specification .................... 71
  17.4 AHRS specification ................................................. 71
  17.5 Conformance specification .................................... 72

CHAPTER 18 SPARES AND ACCESSORIES ............ 73
  18.1 Accessories ............................................................... 74
  18.2 SeaTalk NG cables and accessories .................. 74

APPENDIX A NMEA 2000 PGN SUPPORT ................ 79

APPENDIX B AR200 SOFTWARE RELEASE
HISTORY...................................................................... 80

APPENDIX C DOCUMENT CHANGE HISTORY......... 81

<!-- pdf page 8 | printed page 8 -->

CHAPTER 1: IMPORTANT
INFORMATION

Safety warnings
       Warning: Ensure safe navigation
       This product is intended only as an aid to navigation and
       must never be used in preference to sound navigational
       judgment. Only official government charts and notices to
       mariners contain all the current information needed for safe
       navigation, and the captain is responsible for their prudent
       use. It is the user’s responsibility to use official government
       charts, notices to mariners, caution and proper navigational
       skill when operating this or any other Raymarine product.

       Warning: Product installation and operation
       • This product must be installed and operated in accordance
         with the instructions provided. Failure to do so could result
         in personal injury, damage to your vessel and/or poor
         product performance.
       • Raymarine highly recommends certified installation by
         a Raymarine approved installer. A certified installation
         qualifies for enhanced product warranty benefits.
         Register your warranty on the Raymarine website:
         www.raymarine.com/warranty

       Warning: Switch off power supply
       Ensure the vessel’s power supply is switched OFF before
       starting to install this product. Do NOT connect or disconnect
       equipment with the power switched on, unless instructed in
       this document.

       Warning: Potential ignition source
       This product is NOT approved for use in hazardous/flammable
       atmospheres. Do NOT install in a hazardous/flammable
       atmosphere (such as in an engine room or near fuel tanks).

Product warnings
       Warning: Positive ground systems
       Do not connect this unit to a system which has positive
       grounding.

       Warning: Power supply voltage
       Connecting this product to a voltage supply greater than the
       specified maximum rating may cause permanent damage
       to the unit. Refer to the product’s information label for the
       correct voltage.

       Warning: Product grounding
       Before applying power to this product, it MUST be correctly
       grounded, in accordance with the instructions provided.

       Caution: Power supply protection
       When installing this product ensure the power source is
       adequately protected by means of a suitably-rated fuse or
       thermal circuit breaker.

<!-- figure 1 on pdf page 8 at 427,41-492,105 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 8 at 321,131-413,256 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 8 at 41,134-103,256 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 8 at 580,155-801,210 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 8 at 427,158-492,210 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 6 on pdf page 8 at 427,215-801,294 pt | caption: none; nearest centred text below: "Warning: Product grounding" | text-layer labels: Warning: Power supply voltage | nearby labels: Warning: Product grounding | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 8 at 427,301-801,354 pt | caption: none; nearest centred text below: "Caution: Power supply protection" | text-layer labels: Warning: Product grounding | nearby labels: Caution: Power supply protection | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 66) -->
A\
<!-- end of figure 7 -->
<!-- figure 8 on pdf page 8 at 427,361-801,428 pt | caption: none | text-layer labels: Caution: Power supply protection | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 9 on pdf page 8 at 41,414-413,492 pt | caption: none | text-layer labels: Warning: Switch off power supply | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 9 | printed page 9 -->

                    Caution: Product cleaning
                    When cleaning products:
                    • Switch off power supply.
                    • Use a clean damp cloth to wipe clean.
                    • Do NOT use: abrasive, acidic, ammonia, solvent or other
                      chemical based cleaning products.
                    • Do NOT use a jet wash.

                    Caution: Service and maintenance
                    This product contains no user serviceable components. Please
                    refer all maintenance and repair to authorized Raymarine
                    dealers. Unauthorized repair may affect your warranty.

Regulatory notices
Declaration of conformity
Raymarine UK Ltd declares that the following products are in compliance
with the EMC Directive 2014/53/EU:
• AR200 Augmented Reality Sensor, part number E70537.
The original Declaration of Conformity certificate may be viewed on the
relevant product page at www.raymarine.com.

Disclaimer
Raymarine does not warrant that this product is error-free or that it is
compatible with products manufactured by any person or entity other than
Raymarine.
Raymarine is not responsible for damages or injuries caused by your use or
inability to use the product, by the interaction of the product with products
manufactured by others, or by errors in information utilized by the product
supplied by third parties.

Important information

Third-party hardware, such as converters, adapters, routers, switches, Access
Points etc., provided by third parties, may be made available directly to you
by other companies or individuals under separate terms and conditions,
including separate fees and charges. Raymarine UK Ltd or its affiliates have
not tested or screened the third-party hardware.
Raymarine has no control over, and is not responsible for:
• (a) the content and operation of such third-party hardware; or:
• (b) the privacy or other practices of such third-party hardware.
The fact that Raymarine’s documentation may make reference to such
third-party hardware does not indicate any approval or endorsement of
any such third-party hardware. Raymarine may reference such third-party
hardware only as a convenience.
THIS INFORMATION IS MADE AVAILABLE BY Raymarine ON THE BASIS
THAT YOU EXCLUDE TO THE FULLEST EXTENT LAWFULLY PERMITTED
ALL LIABILITY WHATSOEVER FOR ANY LOSS OR DAMAGE HOWSOEVER
ARISING OUT OF THE USE OF THIS INFORMATION OR RELIANCE UPON
THIS INFORMATION.
Raymarine does not exclude Raymarine’s liability (if any) to you for personal
injury or death resulting from Raymarine UK Ltd negligence, for fraud or for
any matter which it would be illegal to exclude or to attempt to exclude.

Water ingress
Water ingress disclaimer
Although the waterproof rating capacity of this product meets the stated
water ingress protection standard (refer to the product’s Technical
Specification), water intrusion and subsequent equipment failure may occur
if the product is subjected to high-pressure washing. Raymarine will not
warrant products subjected to high-pressure washing.

Suppression ferrites
• Raymarine cables may be pre-fitted or supplied with suppression ferrites.
  These are important for correct EMC performance. If ferrites are supplied
  separately to the cables (i.e. not pre-fitted), you must fit the supplied
  ferrites, using the supplied instructions.
• If a ferrite has to be removed for any purpose (e.g. installation or
  maintenance), it must be replaced in the original position before the
  product is used.
                                                                                9

<!-- figure 1 on pdf page 9 at 41,179-103,244 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 10 | printed page 10 -->

• Use only ferrites of the correct type, supplied by Raymarine or its authorized
  dealers.
• Where an installation requires multiple ferrites to be added to a cable,
  additional cable clips should be used to prevent stress on the connectors
  due to the extra weight of the cable.

Connections to other equipment
Requirement for ferrites on non-Raymarine cables:
If your Raymarine equipment is to be connected to other equipment using
a cable not supplied by Raymarine, a suppression ferrite MUST always be
attached to the cable near the Raymarine unit.
For more information, refer to your third-party cable manufacturer.

Warranty registration
To register your Raymarine product ownership, please visit
https://bit.ly/rym-warranty and register online.
It is important that you register your product to receive full warranty benefits.
Your unit package includes a bar code label indicating the serial number of
the unit. You will need this serial number when registering your product
online. You should retain the label for future reference.

Product disposal
Dispose of this product in accordance with the WEEE Directive.
The Waste Electrical and Electronic Equipment (WEEE) Directive requires
the recycling of waste electrical and electronic equipment which contains
materials, components and substances that may be hazardous and present
a risk to human health and the environment when WEEE is not handled
correctly.

                Equipment marked with the crossed-out wheeled bin
                symbol indicates that the equipment should not be
                disposed of in unsorted household waste.
                Local authorities in many regions have established
                collection schemes under which residents can dispose of
                waste electrical and electronic equipment at a recycling
                center or other collection point.
                For more information about suitable collection points for
                waste electrical and electronic equipment in your region,
                refer to the Raymarine website: https://bit.ly/rym-recycling

IMO and SOLAS
The equipment described within this document is intended for use on
leisure marine boats and workboats NOT covered by International Maritime
Organization (IMO) and Safety of Life at Sea (SOLAS) Carriage Regulations.

Technical accuracy
To the best of our knowledge, the information in this document was correct
at the time it was produced. However, Raymarine cannot accept liability
for any inaccuracies or omissions it may contain. In addition, our policy of
continuous product improvement may change specifications without notice.
As a result, Raymarine cannot accept liability for any differences between
the product and this document. Please check the Raymarine website
(https://bit.ly/raymarine-home) to ensure you have the most up-to-date
version(s) of the documentation for your product.

Publication copyright
Copyright ©2024 Raymarine UK Ltd. All rights reserved. No parts of this
material may be copied, translated, or transmitted (in any medium) without
the prior written permission of Raymarine UK Ltd.

<!-- figure 1 on pdf page 10 at 432,55-501,127 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 11 | printed page 11 -->

CHAPTER 2: DOCUMENT INFORMATION
CHAPTER CONTENTS

•       2.1 Applicable products — page 12
•       2.2 Document information — page 12
•       2.3 Document illustrations — page 12
•       2.4 Product documentation — page 12

Document information                           11

<!-- pdf page 12 | printed page 12 -->

2.1 Applicable products
This document is applicable to the AR200 Augmented reality sensor , part
number E70537.

2.2 Document information
This document contains important information related to the installation of
your Raymarine® product.
The document includes information to help you:
• Plan your installation and ensure you have all the necessary equipment.
• Install and connect your product as part of a wider system of connected
  marine electronics.
• Troubleshoot problems and obtain technical support if required.
This and other Raymarine® product documents are available to download
in PDF format from www.raymarine.com/manuals

2.3 Document illustrations
Your product and if applicable, its user interface may differ slightly from that
shown in the illustrations in this document, depending on product variant and
date of manufacture.
All images are provided for illustration purposes only.

2.4 Product documentation
The following documentation is applicable to your product:

Applicable documents
 Document          Description                    Link
 87372             AR200 Installation             www.bit.ly/ar200-docs
                   instructions (This document)
 87170             Deck and bracket mounting      www.bit.ly/ar200-docs
                   template

Related documents
 Document          Description                    Link
 81406             LightHouse 4 Advanced          www.bit.ly/LH4-docs
                   Operation Instructions
 81370             LightHouse 3 Advanced          www.bit.ly/LH3-docs
                   Operation Instructions
 81300             SeaTalk NG Reference           www.bit.ly/STNG-docs
                   Guide

<!-- figure 1 on pdf page 12 at 38,93-413,230 pt | caption: none | text-layer labels: none | OCR: no legible text (0/12 words >= 60, mean confidence 27) -->

<!-- pdf page 13 | printed page 13 -->

CHAPTER 3: SOFTWARE DETAILS
CHAPTER CONTENTS

•        3.1 Applicable software version — page 14
•        3.2 New software features and improvements — page 14
•        3.3 Software updates — page 14

Software details                                                13

<!-- pdf page 14 | printed page 14 -->

3.1 Applicable software version
Product software is updated regularly to add new features and improve
existing functionality.
This document has been updated to reflect the following software version:
 Software name                         Applicable software version
 AR200                                 v1.33

Check the website for the latest software:
 AR200 software download link
 https://bit.ly/ar200-download

3.2 New software features and improvements
The following new features have been added to version v1.33 of the AR200.
AR200 v1.33 new features:
• Added support for a new LED indicator ‘Switch off’ setting which can
  be toggled via a networked LightHouse 4 multifunction display (running
  software version v4.6.74 or later). For more information, refer to:
  p.60 — Switching off sensor LEDs
• Added support for a new LED indicator ‘Find me’ setting which can be
  toggled via a networked LightHouse 4 multifunction display (running
  software version v4.6.74 or later). For more information, refer to:
  p.60 — Find me

3.3 Software updates
Raymarine regularly issues software updates for its products, which provide
new and enhanced features and improved performance and usability. It’s
important to ensure that you have the latest software for your products by
regularly checking the Raymarine website for new software releases.
To check for the latest software updates and the software update procedure
for your specific product(s) refer to: https://bit.ly/rym-software
Unless otherwise stated, software updates for Raymarine products are
performed using a Raymarine MFD/chartplotter.

• Where applicable, you should always backup your user data and settings
  before performing a software update.
• To update SeaTalk NG products you must use the datamaster
  MFD/Chartplotter which is physically connected to the SeaTalk NG
  backbone.
• Ethernet (RayNet) products can be updated from any MFD/Chartplotter on
  the same network as the product to be updated.
• In order to perform a software update, any connected Autopilot or Radar
  must be switched to Standby.
• The MFD’s/Chartplotter’s “Check online” feature is only available when
  connected to the Internet.

 Note:
 If in doubt as to the correct procedure for updating your product software,
 refer to your dealer or Raymarine technical support.

             Caution: Installing software updates
             • The software update process is carried out at your own
               risk. Before initiating the update process ensure you have
               backed up any important files.
             • Ensure that the product(s) has a reliable power supply and
               that the update process is not interrupted.
             • Damage caused by an incomplete update is not covered
               by Raymarine warranty.
             • By downloading the software update package, you agree to
               these terms.

<!-- pdf page 15 | printed page 15 -->

CHAPTER 4: PRODUCT AND SYSTEM OVERVIEW
CHAPTER CONTENTS

•       4.1 AR200 product overview — page 16
•       4.2 System examples — page 17
•       4.3 Required additional components — page 17

Product and system overview                            15

<!-- pdf page 16 | printed page 16 -->

4.1 AR200 product overview
The AR200 is an Augmented Reality Sensor consisting of a GNSS (GPS)
receiver and an Attitude and Heading Reference System (AHRS) sensor.
When combined with a compatible IP or Thermal camera and an Axiom-Series
display running LightHouse 3 v3.7.70, or later or a Axiom 2-Series display
running LightHouse 4 v4.0.70, or later; the AR200 enables the ClearCruise®
Augmented Reality feature.
ClearCruise® Augmented Reality overlays data objects (such as waypoints,
AIS targets and charted objects) onto a live camera feed being shown on your
display. This enhances your situational awareness by allowing you to quickly
see the position of these objects relative to your camera’s field of view..

The AR200 provides position, heading, pitch and roll data to compatible
displays that are on the same SeaTalk NG/NMEA 2000 network.
Product features:
• Enables the ClearCruise® Augmented Reality feature on compatible
  displays.
• Includes a 9-axis AHRS (Attitude and Heading Reference System) sensor.
• Compatible with GPS, and GLONASS GNSS satellite constellations.

• Automatic calibration.
• Pole, Rail, Surface or Bulkhead mountable (mounting kits available).
• Can be used as a source of GNSS (GPS) position and Heading data for
  other devices in your network. For more information, please refer to the
  Multiple Data Sources (MDS) information in your display’s Advanced
  operation instructions document.
• 10 Hz refresh rate.
• NMEA 2000 compliant.
• Low power consumption.
• 12 V DC operation (protected up to 32 V DC), via the SeaTalk NG/NMEA
  2000 network.
• Waterproof to IPx6, IPx7.

SeaTalk NG
SeaTalk NG (Next Generation) is an enhanced protocol for connection of
compatible marine instruments and equipment. It replaces the older SeaTalk
1 and SeaTalk 2 protocols.
SeaTalk NG utilizes a single backbone which compatible equipment connects
to using a spur. Data and power are carried within the backbone. Devices
that have a low power draw can be powered from the network, although high
current equipment will need to have a separate power connection.
SeaTalk NG is a proprietary extension to NMEA 2000 and the proven CAN bus
technology. Compatible NMEA 2000, SeaTalk 1 and SeaTalk 2 devices can also
be connected using the appropriate interfaces or adaptor cables as required.

<!-- figure 1 on pdf page 16 at 38,206-413,435 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/27 words >= 60, mean confidence 25) -->
RedJet
PASSENGER VESSEL
200m
<!-- end of figure 1 -->

<!-- pdf page 17 | printed page 17 -->

4.2 System examples
Below is a typical system example showing the components and connections
required to enable ClearCruise® Augmented Reality on your system.

CAM300 and Axiom 2 XL system example

1.   Axiom 2 XL display (Power sourcing equipment providing PoE (Power
     over ethernet) to the CAM300 camera.
2. AR200 sensor.
3.   SeaTalk NG network.
4.   RayNet (female) to RJ45 (male) adapter cable (part number: A62360).
5. RJ45 to RJ45 waterproof coupler (part number: 4115028).
Product and system overview

6. CAM300.
7. 12 V dc power supply connection (powering the SeaTalk NG network).

 Note:
 • In the above example the camera is being powered by the display using
   PoE. If the display does not support PoE an alternative power connection
   for the camera is required, using either a PoE injector (part number:
   4113746) or the camera’s power cable connection.
 • The display also requires its own power source, this is not shown in
   the system example.

4.3 Required additional components
The AR200 forms part of the ClearCruise® Augmented Reality System and
requires the following additional components to enable the Augmented
Reality features on your system.
Required components for Augmented Reality (IP cameras)
• Axiom-Series display running LightHouse 3 v3.7.70 or later, or
• Axiom 2-Series display running LightHouse 4 v4.1.140 or later.
• IP camera (CAM300, CAM210IP or CAM220IP).
Required components for Augmented Reality (M-Series cameras)
• Axiom-Series or Axiom 2-Series display.
• M-Series camera (M100-Series, M200-Series or M300-Series).
• M100-Series and M200-Series cameras require Axiom-Series displays to be
  running LightHouse 3 v3.9.46 or later.
• M300-Series cameras require Axiom-Series displays to be running
  LightHouse 3 v3.10.42 or later.
• All M-Series cameras require Axiom 2-Series displays to be running
  LightHouse 4 v4.1.140 or later.

 Important:
 Cameras utilizing ClearCruise® Augmented Reality are subject to an
 unstable image on rough waters.

Recommended components
                                                                          17

<!-- figure 1 on pdf page 17 at 38,124-413,445 pt | caption: none; nearest centred text below: "Axiom 2 XL display (Power sourcing equipment providing PoE (Power" | text-layer labels: none | nearby labels: CAM300 and Axiom 2 XL system example | 1. | over ethernet) to the CAM300 camera. | OCR text follows (tesseract, unverified; 5/10 words >= 60, mean confidence 55) -->
1?
*4
5A
@<6
‘7
<!-- end of figure 1 -->

<!-- pdf page 18 | printed page 18 -->

• An AIS receiver / transceiver is required to overlay AIS targets on the live
  camera feed.
• Compatible detailed electronic cartography is required to overlay charted
  objects on the live camera feed.

<!-- pdf page 19 | printed page 19 -->

CHAPTER 5: PARTS SUPPLIED
CHAPTER CONTENTS

•        5.1 Parts supplied — page 20

Parts supplied                          19

<!-- pdf page 20 | printed page 20 -->

5.1 Parts supplied
The following parts are supplied with your product.

1.   Mounting tray top.
2. Small sealing ring.
3.   AR200.
4.   6 m (19.69 ft) SeaTalk NG (White) cable.
5. 3 x large bulkhead bracket fixings (Pan head pozi DIN7981 ST 3.9x22 C Z
   A4 Stainless steel).
6. 4 x small surface mount fixings (Pan head pozi DIN7981–ST 2.9x13 C Z
   A4 Stainless steel).
7.   Mounting tray bottom.
8. Bulkhead bracket.
9.   Documentation.
10. Large sealing ring.
Unpack your product carefully to prevent damage or loss of parts, check the
box contents against the list above. Retain the packaging and documentation
for future reference.

<!-- figure 1 on pdf page 20 at 38,81-413,306 pt | caption: none | text-layer labels: none | nearby labels: 5.1 Parts supplied | 1. | Mounting tray top. | 2. Small sealing ring. | OCR text follows (tesseract, unverified; 9/30 words >= 60, mean confidence 47) -->
1?
2?
3?
4?
7?
8?
Hf
9?
10”
<!-- end of figure 1 -->

<!-- pdf page 21 | printed page 21 -->

CHAPTER 6: PRODUCT DIMENSIONS
CHAPTER CONTENTS

•       6.1 Product dimensions — page 22
•       6.2 Product dimensions with Mounting tray — page 22
•       6.3 Product dimensions with Mounting tray and Riser — page 22
•       6.4 Product dimensions with Mounting tray and Bulkhead bracket — page 23

Product dimensions                                                                 21

<!-- pdf page 22 | printed page 22 -->

6.1 Product dimensions

        Dimension
 A      108.48 mm (4.27 in)
 B      26.61 mm (1.05 in)
 C      14.96 mm (0.59 in)

6.2 Product dimensions with Mounting tray
The following dimensions apply when surface mounting using the Mounting
tray.

        Dimension
 A      41.57 mm (1.64 in)
 B      90.00 mm (3.54 in)

      Dimension
C     140.40 mm (5.53 in)
D     128.00 mm (5.0 in)

6.3 Product dimensions with Mounting tray
and Riser
The following dimensions apply when surface mounting using the Mounting
tray and Riser supplied in the Deck mounting kit.

      Dimension
A     66.07 mm (2.60 in)
B     65.50 mm (2.58 in)
C     140.40 mm (5.53 in)
D     128.00 mm (5.0 in)

<!-- figure 1 on pdf page 22 at 38,65-413,194 pt | caption: none | text-layer labels: none | nearby labels: 6.1 Product dimensions | C | D | Dimension | A | OCR text follows (tesseract, unverified; 3/6 words >= 60, mean confidence 63) -->
A
B
Cc
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 22 at 427,182-801,330 pt | caption: none | text-layer labels: none | nearby labels: Dimension | OCR text follows (tesseract, unverified; 2/6 words >= 60, mean confidence 52) -->
{ff
Raymarine
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 22 at 38,337-413,509 pt | caption: none | text-layer labels: Dimension | nearby labels: tray . | A | 41.57 mm (1.64 in) | B | 90.00 mm (3.54 in) | A | B | C | D | OCR text follows (tesseract, unverified; 3/11 words >= 60, mean confidence 42) -->
Raymarine
fy
Za
<!-- end of figure 3 -->

<!-- pdf page 23 | printed page 23 -->

6.4 Product dimensions with Mounting tray
and Bulkhead bracket
The following dimensions apply when bulkhead mounting using the Mounting
tray and the Bulkhead bracket.

          Dimension
 A        41.57 mm (1.64 in)
 B        90.00 mm (3.54 in)
 C        128.00 mm (5.0 in)
 D        101.57 mm (4.00 in
 E        140.40 mm (5.53 in)

Product dimensions                                                         23

<!-- figure 1 on pdf page 23 at 38,115-413,275 pt | caption: none | text-layer labels: none | nearby labels: tray and the Bulkhead bracket . | Dimension | OCR: no legible text (0/5 words >= 60, mean confidence 28) -->

<!-- pdf page 24 | printed page 24 -->

CHAPTER 7: LOCATION REQUIREMENTS
CHAPTER CONTENTS

•   7.1 Warnings and cautions — page 25
•   7.2 Location requirements — page 25
•   7.3 RF interference — page 26
•   7.4 Compass safe distance — page 26
•   7.5 EMC installation guidelines — page 26

<!-- pdf page 25 | printed page 25 -->

7.1 Warnings and cautions
 Important:
 Before proceeding, ensure that you have read and understood the
 warnings and cautions provided in the following section of this document:
 p.8 — Important information

                   Warning: Potential ignition source
                   This product is NOT approved for use in hazardous/flammable
                   atmospheres. Do NOT install in a hazardous/flammable
                   atmosphere (such as in an engine room or near fuel tanks).

7.2 Location requirements
The installation location must take into account the following requirements:

• The unit should be installed above decks.
• Choose a location that provides the most unobstructed view of the sky
  in all directions:

• The unit must be mounted on a horizontal and level surface. The installed
  unit must be level within 5º of pitch and 5º of roll (compared with the
  vessel’s neutral position when at rest and normally laden).
Location requirements

  1.   Roll (Rotation side to side)
  2. Pitch (Rotation front to back)
• The unit can be mounted on a vertical surface such as a bulkhead or mast
  etc, using the supplied bulkhead bracket.
• Do NOT mount on top of a mast.
• The unit location must be at least 1 m (3 ft.) away from sources that
  can cause interference, such as compasses, electrical cables, motors,
  generators, VHF radio units and other transmitters / receivers.
• Ensure the unit is NOT mounted in the path of the beam emitted from
  Radar scanners.
• Choose a location where the unit will be safe from physical damage and
  excessive vibration.
• Choose a location where the unit will not be subjected to a load or force.
• Mount away from any source of heat or potential flammable hazards, such
  as fuel vapor.
• The unit should be mounted in a location where the diagnostics LED is
  viewable.
• The unit must be mounted with the LED ‘arrow’ on the top of the unit
  pointing forwards, in parallel alignment with the centerline (longitudinal
  axis) of the vessel.

                                                                               25

<!-- figure 1 on pdf page 25 at 439,38-801,201 pt | caption: none | text-layer labels: none | nearby labels: 1. | Roll (Rotation side to side) | 2. Pitch (Rotation front to back) | OCR text follows (tesseract, unverified; 1/7 words >= 60, mean confidence 29) -->
1?
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 25 at 41,146-413,213 pt | caption: none | text-layer labels: Warning: Potential ignition source | nearby labels: 1. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 25 at 50,347-413,500 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 31) -->

<!-- pdf page 26 | printed page 26 -->

1.   Vessel centerline (longitudinal axis)

7.3 RF interference
Certain third-party external electrical equipment can cause Radio Frequency
(RF) interference with GNSS (GPS), AIS or VHF devices, if the external
equipment is not adequately insulated and emits excessive levels of
electromagnetic interference (EMI).
Some common examples of such external equipment include LED lighting
(e.g.: navigation lights, searchlights and floodlights, interior and exterior
lights) and terrestrial TV tuners.
To minimize interference from such equipment:
• Keep it as far away from GNSS (GPS), AIS or VHF products and their
  antennas as possible.

• Ensure that any power cables for external equipment are not entangled
  with the power or data cables for these devices.
• Consider fitting one or more high frequency suppression ferrites to the
  EMI-emitting device. The ferrite(s) should be rated to be effective in the
  range 100 MHz to 2.5 GHz, and should be fitted to the power cable and
  any other cables exiting the EMI-emitting device, as close as possible to
  the position where the cable exits the device.

7.4 Compass safe distance
To prevent potential interference with the vessel's magnetic compasses,
ensure an adequate distance is maintained from the product.
When choosing a suitable location for the product you must aim to maintain a
distance of at least 1 m (3.3 ft) in all directions from any compasses.
For some smaller vessels it may not be possible to locate the product this
far away from a compass. In this situation, when choosing the installation
location for your product, ensure that the compass is not affected by the
product when it is in a powered on state.

7.5 EMC installation guidelines
Raymarine equipment and accessories conform to the appropriate
Electromagnetic Compatibility (EMC) regulations, to minimize electromagnetic
interference between equipment and minimize the effect such interference
could have on the performance of your system.
Correct installation is required to ensure that EMC performance is not
compromised.

 Note:
 In areas of extreme EMC interference, some slight interference may be
 noticed on the product. Where this occurs the product and the source of
 the interference should be separated by a greater distance.

For optimum EMC performance we recommend that wherever possible:

<!-- figure 1 on pdf page 26 at 38,38-413,323 pt | caption: none | text-layer labels: none | nearby labels: 1. | Vessel centerline (longitudinal axis) | OCR: no legible text (0/7 words >= 60, mean confidence 25) -->

<!-- pdf page 27 | printed page 27 -->

• Raymarine equipment and cables connected to it are:
   – At least 1 m (3.28 ft) from any equipment transmitting or cables carrying
     radio signals e.g. VHF radios, cables and antennas. In the case of SSB
     radios, the distance should be increased to 2 m (6.6 ft).
   – More than 2 m (6.56 ft) from the path of a Radar beam. A Radar beam
     can normally be assumed to spread 20 degrees above and below the
     radiating element.
• The product is supplied from a separate battery from that used for engine
  start. This is important to prevent erratic behavior and data loss which can
  occur if the engine start does not have a separate battery.
• Raymarine specified cables are used.
• Cables are not cut or extended, unless doing so is detailed in the
  installation manual.

 Note:
 Where constraints on the installation prevent any of the above
 recommendations, always ensure the maximum possible separation
 between different items of electrical equipment, to provide the best
 conditions for EMC performance throughout the installation.

Suppression ferrites
• Raymarine cables may be pre-fitted or supplied with suppression ferrites.
  These are important for correct EMC performance. If ferrites are supplied
  separately to the cables (i.e. not pre-fitted), you must fit the supplied
  ferrites, using the supplied instructions.
• If a ferrite has to be removed for any purpose (e.g. installation or
  maintenance), it must be replaced in the original position before the
  product is used.
• Use only ferrites of the correct type, supplied by Raymarine or its authorized
  dealers.
• Where an installation requires multiple ferrites to be added to a cable,
  additional cable clips should be used to prevent stress on the connectors
  due to the extra weight of the cable.

Location requirements

Connections to other equipment
Requirement for ferrites on non-Raymarine cables:
If your Raymarine equipment is to be connected to other equipment using
a cable not supplied by Raymarine, a suppression ferrite MUST always be
attached to the cable near the Raymarine unit.
For more information, refer to your third-party cable manufacturer.

                                                                          27

<!-- pdf page 28 | printed page 28 -->

CHAPTER 8: INSTALLATION
CHAPTER CONTENTS

•   8.1 Installation checklist — page 29
•   8.2 Tools required for installation — page 29
•   8.3 Mounting options — page 30
•   8.4 Bulkhead mounting — page 30
•   8.5 Surface mounting — page 32
•   8.6 Surface mounting using the Riser — page 33
•   8.7 Releasing the product from the mounting tray — page 35
•   8.8 Pole or rail mounting — page 35

<!-- pdf page 29 | printed page 29 | footer: Installation -->

8.1 Installation checklist
Installation includes the following activities:
Installation Task
1.   Plan your system.
2. Obtain all required equipment and tools.
3.   Site all equipment.
4.   Route all cables.
5. Drill cable and mounting holes.
6. Make all connections into equipment.
7.   Secure all equipment in place.
8. Power on and test the system.

Schematic diagram
A schematic diagram is an essential part of planning any installation. It is also
useful for any future additions or maintenance of the system. The diagram
should include:
• Location of all components.
• Connectors, cable types, routes and lengths.

8.2 Tools required for installation
The following tools are required for installation:

       Description
 1     Power drill.
 2     Pozi-drive screwdriver.
 3     Suitable size drill bit (for Mounting tray and Bulkhead bracket
       mounting).

        Note:
        Drill bit size is dependent on the type of material the unit is
        to be mounted on.

 4     12 mm (15/32”) drill bit (if required, for cable hole).
 5     Size 4 (2.5 mm) Hex Key (only required for Pole mount installations).

<!-- figure 1 on pdf page 29 at 427,84-801,294 pt | caption: none | text-layer labels: Description | nearby labels: 1 | Power drill. | 2 | Pozi-drive screwdriver. | OCR: no legible text (0/1 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 29 at 463,368-777,421 pt | caption: none | text-layer labels: Note: | nearby labels: 3 | 4 | 5 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 30 | printed page 30 -->

8.3 Mounting options
Several mounting options are available.

1.   Bulkhead mounting using the supplied Mounting tray and Bulkhead
     bracket. Refer to: p.30 — Bulkhead mounting
2. Surface mounting using the supplied Mounting tray. Refer to:
   p.32 — Surface mounting
3.   Surface mounting on riser using the Deck mounting
     (Clamshell/Riser) kit. (part number: A80437). Refer to:
     p.33 — Surface mounting using the Riser
4.   Pole/rail mounting using the Pole/rail mounting adaptor kit (part number:
     A80370). Refer to: p.35 — Pole or rail mounting

8.4 Bulkhead mounting
The supplied Mounting tray and Bulkhead bracket can be used to mount
your product horizontally on a vertical bulkhead.
Ensure that the chosen location meets the product’s location requirements,
for details refer to: 7.2 Location requirements

<!-- figure 1 on pdf page 30 at 38,84-413,328 pt | caption: none | text-layer labels: none | nearby labels: Several mounting options are available. | 1. | OCR text follows (tesseract, unverified; 5/21 words >= 60, mean confidence 44) -->
2?
1?
4?
3?
D
<!-- end of figure 1 -->

<!-- pdf page 31 | printed page 31 | footer: Installation -->

1. Use the supplied Bracket mounting template (Document number: 87170)
   to drill 3 pilot holes in the vertical mounting surface. Secure the mounting
   bracket to the surface using the supplied screws.
2. Place the small sealing ring in the groove located on the bottom of the
   Mounting tray.
3. Secure the tray to the bracket using 3 of the 4 supplied small screws, in
   the positions indicated in the illustration above.
4. Place the large sealing ring into the groove on the upper side of the
   Mounting tray.
5. Pull the SeaTalk NG cable up through the center of the bracket and tray.
   Plug in the cable connector on the underside of the unit and secure by
   rotating the locking collar clockwise 2 clicks.
6. Insert the unit into the mounting tray, ensuring the tabs in the Mounting
   tray are slotted into the grooves around the edge of the unit.

 Important:
 The unit must be mounted with the LED ‘arrow’ on the top of the unit
 pointing forwards, in parallel alignment with the centerline (longitudinal
 axis) of your vessel.

<!-- figure 1 on pdf page 31 at 38,38-413,519 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/53 words >= 60, mean confidence 33) -->
wy
s
JS
NN
if
4
y
<!-- end of figure 1 -->

<!-- pdf page 32 | printed page 32 -->

7. Orientate the Mounting tray top so that the release hole is pointing
   forwards so that it will be accessible once mounted.

8. Place the Mounting trim over the unit slightly offset, and then twist the
   Mounting trim clockwise until it locks into position.

8.5 Surface mounting
The supplied Mounting tray can be used to mount your product on a flat,
horizontal surface.
The Bulkhead bracket is not required for this type of installation.

Ensure that the chosen location meets the product’s location requirements,
for details refer to: 7.2 Location requirements

1. Using the supplied Mounting tray template (87170), drill 4 holes in the
   mounting surface, plus a 12 mm (15/32”) hole for the SeaTalk NG cable.
2. Place the small sealing ring in the groove located on the bottom of the
   mounting tray.
3. Secure the tray to the mounting surface using the 4 x fixings, supplied.
4. Place the large sealing ring into the groove on the upper side of the
   Mounting tray.

<!-- figure 1 on pdf page 32 at 55,65-413,304 pt | caption: none | text-layer labels: none | OCR: no legible text (0/3 words >= 60, mean confidence 15) -->
<!-- figure 2 on pdf page 32 at 427,69-801,426 pt | caption: none | text-layer labels: none | OCR: no legible text (0/20 words >= 60, mean confidence 27) -->
<!-- figure 3 on pdf page 32 at 55,332-413,449 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/7 words >= 60, mean confidence 58) -->
Raymarine
Raymarine
e
<!-- end of figure 3 -->

<!-- pdf page 33 | printed page 33 | footer: Installation -->

5. Pull the SeaTalk NG cable up through the hole in the mounting surface
   and the Mounting tray. Plug in the cable connector on the underside of
   the unit and secure by rotating the locking collar clockwise 2 clicks.
6. Insert the unit into the Mounting tray, ensuring the tabs in the tray are
   slotted into the grooves around the edge of the unit.

 Important:
 The unit must be mounted with the LED ‘arrow’ on the top of the unit
 pointing towards the vessel’s bow and be in parallel alignment with the
 centerline (longitudinal axis) of your vessel.

7. Place the Mounting tray top over the unit slightly offset, and then twist the
   Mounting tray top clockwise until it locks into position.

8.6 Surface mounting using the Riser
The Riser that is supplied in the Deck mounting kit (part number: A80437)
can be used to raise the product from the mounting surface.
The bulkhead bracket cannot be used with the using the Riser.
Ensure that the chosen location meets the product’s location requirements,
for details refer to: 7.2 Location requirements

<!-- figure 1 on pdf page 33 at 55,232-413,342 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/6 words >= 60, mean confidence 62) -->
il
Raymarine
Raymarine
<!-- end of figure 1 -->

<!-- pdf page 34 | printed page 34 -->

1. Use the mounting template supplied with the Deck mounting kit to drill
   4 holes in the mounting surface.
2. Secure the Riser to the mounting surface using 4 x supplied fixings.
3. Place the small sealing ring in the groove located on the bottom of the
   mounting tray.
4. Position the Mounting tray on top of the Riser.
5. Secure the Mounting tray to the Riser using 4 x supplied fixings.
6. Place the large sealing ring into the groove on the upper side of the
   Mounting tray.
7. Pull the SeaTalk NG cable up through the Riser and Mounting tray. Plug
   in the cable connector on the underside of the unit and secure by rotating
   the locking collar clockwise 2 clicks.
8. Insert the unit into the Mounting tray, ensuring the tabs in the Mounting
   tray are slotted into the grooves around the edge of the unit.

 Important:
 The unit must be mounted with the LED ‘arrow’ on the top of the unit
 pointing towards the vessel’s bow and be in parallel alignment with the
 centerline (longitudinal axis) of your vessel.

9. Place the Mounting tray top over the unit slightly offset, and then twist the
   Mounting tray top clockwise until it locks into position.

<!-- figure 1 on pdf page 34 at 38,38-413,538 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/34 words >= 60, mean confidence 35) -->
i
Vi
id
IN
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 34 at 444,359-801,469 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/7 words >= 60, mean confidence 63) -->
A
Raymarine
Raymarine
Raymarine
<!-- end of figure 2 -->

<!-- pdf page 35 | printed page 35 | footer: Installation -->

8.7 Releasing the product from the mounting
tray
Follow the steps below to release the product from the mounting tray.

 Important:
 To help prevent scratching the product, cover the tip of your screwdriver
 with a small piece of insulation tape.

1. Insert the end of a small flat blade screwdriver (or similar tool) into the
   release hole located on the flat edge of the mounting tray.
2. Twist the screwdriver 90°, so that there is a small gap between the top
   and bottom pieces of the mounting tray.
3. With the screwdriver in place, twist the mounting trim counter-clockwise
   approximately 10°.
4. You should now be able to lift the top away from the product.

8.8 Pole or rail mounting
The Pole mount kit (part number: A80370) can be used to mount your
product on a pole or rail.

 Note:
 A pole or rail mount with a 1 inch 14 TPI thread is required.

Ensure that the chosen location meets the product’s location requirements,
for details refer to: p.24 — Location requirements

1. Screw the Pole mount adaptor on to the pole.
2. Feed the SeaTalk NG cable through either:
   • a) the center of the pole and Pole mount adaptor, or:
   • b) the cable exit hole in the Pole mount adaptor.
3. Connect the cable to the connector on the underside of the product, and
   secure using the locking collar. Connect the other end of the cable to an
   available SeaTalk NG spur connection.

<!-- figure 1 on pdf page 35 at 38,177-413,394 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/15 words >= 60, mean confidence 50) -->
2?
ll
4?
3?
Raymarine
Raymarine
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 35 at 427,194-801,445 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/18 words >= 60, mean confidence 35) -->
Uy
3?
5
G
2a’.
<!-- end of figure 2 -->

<!-- pdf page 36 | printed page 36 -->

4. Ensuring correct orientation, secure the product to the Pole mount
   adaptor using the supplied fixings.
5. Fix the products’s orientation by tightening the grub screws.

   The grub screws and their captive nuts are supplied fitted to the adaptor.

Adjusting pole mount alignment
If the product you are mounting includes a heading sensor, you must ensure
that the unit is orientated correctly. If the alignment is not correct it can be
adjusted.
1. Loosen the grub screws slightly.
2. Twist the unit until the desired alignment is achieved.

   The Product’s LED should be facing the bow and be parallel with the
   centerline of the vessel.

3. Re-tighten the grub screws to secure the product in position.

<!-- pdf page 37 | printed page 37 -->

CHAPTER 9: CABLES AND CONNECTIONS — GENERAL INFORMATION
CHAPTER CONTENTS

•       9.1 General cabling guidance — page 38
•       9.2 Connections overview — page 38
•       9.3 System examples — page 39

Cables and connections — General information              37

<!-- pdf page 38 | printed page 38 -->

9.1 General cabling guidance
Cable types and length
It is important to use cables of the appropriate type and length.
• Unless otherwise stated only use cables supplied by Raymarine.
• Where it is necessary to use non-Raymarine cables, ensure that they are of
    correct quality and gauge for their intended purpose. (e.g.: longer power
    cable runs may require larger wire gauges to minimize voltage drop along
    the run).

Cable routing
Cables must be routed correctly, to maximize performance and prolong
cable life.
• Do NOT bend cables excessively. Wherever possible, ensure a minimum
  bend diameter (Ø) of 200 mm (7.87 in) / minimum bend radius (R) of
  100 mm (3.94 in).

• Protect all cables from physical damage and exposure to heat. Use
  trunking or conduit where possible. Do NOT run cables through bilges or
  doorways, or close to moving or hot objects.
• Secure cables in place using cable clips or cable ties. Coil any excess
  cable and tie it out of the way.
• Where a cable passes through an exposed bulkhead or deckhead, use
  a suitable watertight feed-through.

• Do NOT run cables near to engines or fluorescent lights.
• Always route data cables as far away as possible from:
  – Other equipment and cables.
  – High current carrying AC and DC power lines.
  – Antennas.

Strain relief
Use adequate strain relief for cabling to ensure that connectors are protected
from strain and will not pull out under extreme sea conditions.

Cable shielding
Ensure that cable shielding is not damaged during installation and that all
cables are properly shielded.

 Important:
 Be aware that some third-party cables and adaptors (for example, certain
 Ethernet cables using RJ45 connectors) are not always shielded. To
 prevent breaks in cable shielding continuity and potential grounding issues,
 special attention is required to ensure that any cables, extension cables,
 adaptors, or other signal-coupling devices (such as multi-way connectors,
 junction boxes, terminal blocks etc.) used in cable runs maintain all shield
 connections throughout the cable run.

9.2 Connections overview
Your product is supplied power and data using the SeaTalk NG connector
located on the underside of the unit.
 Connector      Connection options
                • SeaTalk NG backbone using a SeaTalk NG spur cable.
                • NMEA 2000 backbone using SeaTalk NG to DeviceNet
                  adaptor cable (A06045)
                • SeaTalk 1 backbone using a SeaTalk 1 to SeaTalk NG
                  adaptor cable (A06073)

For a list of available cables, refer to: p.73 — Spares and accessories

<!-- figure 1 on pdf page 38 at 38,270-413,449 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 92) -->
200 mm (7.87 in)
R 100 mm (3.94 in) Min.
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 38 at 432,454-501,519 pt | caption: none | text-layer labels: none | nearby labels: Connector | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 39 | printed page 39 -->

Connecting SeaTalk NG cables

1. Rotate your product’s SeaTalk NG connector locking collar counter
   clockwise, so that the connector is in the unlocked position.
2. Ensure the cable’s connector is correctly oriented (groove pointing up).
3. Fully insert the cable connector.
4. Rotate the locking collar clockwise (2 clicks) until it is in the locked
   position.

SeaTalk NG product loading
The number of products that can be connected to a SeaTalk NG backbone
depends on the current draw of each product and the physical length of
the backbone cabling.
NMEA 2000 Load Equivalency Numbers (LEN) are used to express the amount
of current that is drawn from SeaTalk NG products (1 LEN = 50 mA). The LEN
for each product can be found in the product’s Technical Specification.
Products which have a dedicated power supply connection that are
connected to the SeaTalk NG backbone will still have an LEN rating. This is
because the product’s NMEA 2000/SeaTalk NG internal transceiver will still be
powered by the SeaTalk NG backbone.
LENs are used to determine the power connection point for the SeaTalk NG
backbone.

Cables and connections — General information

9.3 System examples
Below is a typical system example showing the components and connections
required to enable ClearCruise® Augmented Reality on your system.

CAM300 and Axiom 2 XL system example

1.   Axiom 2 XL display (Power sourcing equipment providing PoE (Power
     over ethernet) to the CAM300 camera.
2. AR200 sensor.
3.   SeaTalk NG network.
4.   RayNet (female) to RJ45 (male) adapter cable (part number: A62360).
5. RJ45 to RJ45 waterproof coupler (part number: 4115028).
6. CAM300.
                                                                           39

<!-- figure 1 on pdf page 39 at 38,60-413,225 pt | caption: none | text-layer labels: none | nearby labels: Connecting SeaTalk NG cables | OCR text follows (tesseract, unverified; 1/10 words >= 60, mean confidence 26) -->
ANN
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 39 at 427,115-801,435 pt | caption: none; nearest centred text below: "Axiom 2 XL display (Power sourcing equipment providing PoE (Power" | text-layer labels: none | nearby labels: CAM300 and Axiom 2 XL system example | 1. | over ethernet) to the CAM300 camera. | OCR text follows (tesseract, unverified; 3/13 words >= 60, mean confidence 43) -->
1?
Raymarine
5A
<!-- end of figure 2 -->

<!-- pdf page 40 | printed page 40 | header: 7. -->

7.   12 V dc power supply connection (powering the SeaTalk NG network).

 Note:
 • In the above example the camera is being powered by the display using
   PoE. If the display does not support PoE an alternative power connection
   for the camera is required, using either a PoE injector (part number:
   4113746) or the camera’s power cable connection.
 • The display also requires its own power source, this is not shown in
   the system example.

<!-- pdf page 41 | printed page 41 | footer: Power connections -->

CHAPTER 10: POWER CONNECTIONS
CHAPTER CONTENTS

•   10.1 SeaTalk NG power supply — page 42
•   10.2 SeaTalk NG power cables — page 42
•   10.3 SeaTalk NG product loading — page 43
•   10.4 SeaTalk NG power connection point — page 43
•   10.5 SeaTalk NG system loading — page 44
•   10.6 Power distribution — SeaTalk NG — page 44
•   10.7 Power connection via Autopilot Control Unit (ACU-Series) — page 46

<!-- pdf page 42 | printed page 42 | header: Note: -->

10.1 SeaTalk NG power supply
Your product is supplied power via the SeaTalk NG backbone (or the NMEA
2000 backbone if applicable).
A SeaTalk NG backbone requires a single 12 V dc power supply. Power can
be supplied to the SeaTalk NG backbone by one of the following methods:
• (1) Direct connection to a 12 V dc battery using an inline 5 amp fuse.
• Connection to a 12 V dc distribution panel using a 3 amp thermal breaker.
• (2) Connection to the SeaTalk NG connector of an ACU-Series Autopilot
  Control Unit (not ACU-100 or ACU-150), or an SPX-Series course computer
  (not SPX-5).
• For 24 V vessels, connection must be via a 5 amp, regulated, continuous
  24 V dc to 12 V dc converter.

 Note:
 • (1) The battery used for starting the vessel’s engine(s) should NOT be
   used to power the SeaTalk NG backbone, as this can cause sudden
   voltage drops when the engines are started.
 • (2) The ACU-100, ACU-150 or SPX-5 cannot be used to power the SeaTalk
   NG backbone.
 • The course computer SeaTalk NG connector includes a power switch that
   must be in the On position to provide power to the backbone.

              Warning: 12 Volt dc only
              This product must ONLY be connected to a 12 V dc power
              source.

Inline fuse and thermal breaker ratings
The SeaTalk NG network’s power supply requires a suitably-rated inline fuse
or thermal breaker to be fitted.
 Inline fuse rating                      Thermal breaker rating
 5A                                      3A (refer to note below)

 Note:
 The suitable fuse rating for the thermal breaker is dependent on:
 1.    How many devices you have connected to your SeaTalk NG network,
       and;
 2. How many devices are sharing the same thermal breaker that your
    SeaTalk NG network is connected to.

10.2 SeaTalk NG power cables
The following SeaTalk NG power cables can be used to connect the
backbone to your chosen 12 V dc power supply:

Direct connection cables

1.    Standard (straight) SeaTalk NG power cable, 2 m (6.6 ft) (part number:
      A06049).
2. Elbow (right-angled) SeaTalk NG power cable, 2 m (6.6 ft) (part number:
   A06070).
Wiring
• + Red (positive) wire — connects to the battery or distribution panel
  positive terminal. A waterproof fuse holder with 5 A inline fuse (not
  supplied) must be fitted to this red wire.
• – Black (negative) wire — connects to battery or distribution panel
  negative terminal.
• Drain wire — connects to the vessel’s RF common ground point (if
  available), or the battery’s negative (-) terminal.

<!-- figure 1 on pdf page 42 at 427,239-801,325 pt | caption: none | text-layer labels: none | nearby labels: Direct connection cables | 1. | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 47) -->
1?
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 42 at 41,383-413,435 pt | caption: none; nearest centred text below: "Inline fuse and thermal breaker ratings" | text-layer labels: Warning: 12 Volt dc only | nearby labels: Inline fuse and thermal breaker ratings | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 95) -->
A
<!-- end of figure 2 -->

<!-- pdf page 43 | printed page 43 | footer: Power connections -->

Autopilot Control Unit connection cable

1.   ACU-Series/SPX-Series autopilot to SeaTalk NG spur cable, 0.3 m (1.0 ft)
     (part number R12112). Connects the course computer to the SeaTalk NG
     backbone. This connection can also be used to provide 12 V dc power to
     the SeaTalk NG backbone.

10.3 SeaTalk NG product loading
The number of products that can be connected to a SeaTalk NG backbone
depends on the current draw of each product and the physical length of
the backbone cabling.
NMEA 2000 Load Equivalency Numbers (LEN) are used to express the amount
of current that is drawn from SeaTalk NG products (1 LEN = 50 mA). The LEN
for each product can be found in the product’s Technical Specification.
Products which have a dedicated power supply connection that are
connected to the SeaTalk NG backbone will still have an LEN rating. This is
because the product’s NMEA 2000/SeaTalk NG internal transceiver will still be
powered by the SeaTalk NG backbone.
LENs are used to determine the power connection point for the SeaTalk NG
backbone.

10.4 SeaTalk NG power connection point
The point along the backbone where the power connection should be made
is based on the length of the backbone.

 Note:
 • A 12 V dc power supply must be connected to a white spur SeaTalk NG
   connection on the backbone.
 • Do NOT connect the power connection to a blue SeaTalk NG backbone
   connector.
 • With the exception of the iTC-5 and the backbone itself, do NOT
   connect the power supply directly to a product’s white SeaTalk NG spur
   connector.

Small systems
If the backbone length is 60 m (197 ft) or less, the power connection may be
made at any point in the backbone.
Large systems
If the backbone length is greater than 60 m (197 ft), the power connection
should be made at a point that creates a balanced current draw from
each side of the backbone. Load Equivalency Numbers (LEN) are used to
determine the power connection point for the system.

<!-- figure 1 on pdf page 43 at 38,57-413,124 pt | caption: none | text-layer labels: none | nearby labels: Autopilot Control Unit connection cable | 1. | OCR: no legible text (0/1 words >= 60, mean confidence 59) -->

<!-- pdf page 44 | printed page 44 -->

In the example above, the system has an overall LEN of 16, so the optimum
connection point would be to have a loading of 8 LEN either side of the
connection point.

10.5 SeaTalk NG system loading
The maximum loading (LEN) for a SeaTalk NG system depends on the length
of the backbone.
Unbalanced system loading:
• Backbone Length: 0 m (0 ft) to 20 m (66 ft) — Maximum LEN: 40
• Backbone Length: > 20 m (66 ft) to 40 m (131 ft) — Maximum LEN: 20
• Backbone Length: > 40 m (131 ft) to 60 m (197 ft) — Maximum LEN: 14
Balanced system loading:
• Backbone Length: 0 m (0 ft) to 60 m (197 ft) — Maximum LEN: 100
• Backbone Length: > 60 m (197 ft) to 80 m (262 ft) — Maximum LEN: 84
• Backbone Length: > 80 m (262 ft) to 100 m (328 ft) — Maximum LEN: 60
• Backbone Length: > 100 m (328 ft) to 120 m (394 ft) — Maximum LEN: 50

• Backbone Length: > 120 m (394 ft) to 160 m (525 ft) — Maximum LEN: 40
• Backbone Length: > 160 m (525 ft) to 200 m (656 ft) — Maximum LEN: 32

10.6 Power distribution — SeaTalk NG
Recommendations and best practice.
• Only use approved SeaTalk NG power cables. Do NOT use a power cable
  designed for, or supplied with, a different product.
• See below for more information on implementation for some common
  power distribution scenarios.

Important:
• When planning and wiring, take into consideration other products in
  your system, some of which (e.g. sonar modules) may place large power
  demand peaks on the vessel’s electrical system, which may impact the
  voltage available to other products during the peaks.
• The information provided below is for guidance only, to help protect
  your product. It covers common vessel power arrangements, but does
  NOT cover every scenario. If you are unsure how to provide the correct
  level of protection, please consult an authorized Raymarine dealer or a
  suitably qualified professional marine electrician.

Implementation — connection to distribution panel
(recommended)

<!-- figure 1 on pdf page 44 at 38,38-413,287 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 16/28 words >= 60, mean confidence 61) -->
LEN =1
LEN
LEN =1
LEN =1
Raymarine
SA
LEN =3
LEN
LEN
LEN =1
LEN
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 44 at 427,385-801,547 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/15 words >= 60, mean confidence 58) -->
5A
©0008
3?
12 V de
SeaTalk NG
<!-- end of figure 2 -->

<!-- pdf page 45 | printed page 45 | header: 1. | footer: Power connections -->

1.        Waterproof fuse holder with 5 A inline fuse must be fitted (not supplied).
2. SeaTalk NG power cable.
3.        RF Ground connection point for drain wire.
• Ideally, the SeaTalk NG power cable should be connected to a suitable
  breaker or switch on the vessel's distribution panel or factory-fitted power
  distribution point. It is recommended that a 5 A inline fuse is fitted to the
  red (positive) wire of the SeaTalk NG power cable.
• The distribution point should be fed from the vessel’s primary power
  source by 8 AWG (8.36 mm2) cable.
• Ideally, all equipment should be wired to individual suitably-rated thermal
  breakers or fuses, with appropriate circuit protection. Where this is not
  possible and more than one item of equipment shares a breaker, use
  individual in-line fuses for each power circuit to provide the necessary
  protection.

     1.     Positive (+) bar
     2. Negative (-) bar
     3.     Circuit breaker
     4.     Waterproof fuse holder with 5 A inline fuse must be fitted (not supplied).

 Important:
 Observe the recommended fuse / breaker ratings provided in the product’s
 documentation, however be aware that the suitable fuse / breaker rating is
 dependent on the number of devices being connected.

Implementation — direct connection to battery
• Where connection to a power distribution panel is not possible, the power
  cable may be connected to the vessel's battery.
• You MUST fit a 5 A inline fuse between the red wire and the battery’s
  positive terminal.
• If you need to extend the length of the power cable, ensure you use
  suitably rated cable and that sufficient power (12 V dc) is available at the
  SeaTalk NG backbone’s power connection.

1.   Waterproof fuse holder with 5 A inline fuse must be fitted (not supplied).
2. SeaTalk NG power cable.

<!-- figure 1 on pdf page 45 at 427,234-801,512 pt | caption: none | text-layer labels: none | nearby labels: 1. | 2. SeaTalk NG power cable. | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 72) -->
3?
NG
SeaTalk NG
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 45 at 50,244-413,466 pt | caption: none | text-layer labels: none | nearby labels: 1. | Positive (+) bar | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 60) -->
2?
4?
<!-- end of figure 2 -->

<!-- pdf page 46 | printed page 46 | header: 3. -->

3.   Connection point for drain wire.
Battery connection scenario A:
Suitable for a vessel with a common RF ground point. In this scenario, the
power cable’s drain wire should be connected to the vessel’s common RF
ground point.
Battery connection scenario B:
Suitable for a vessel without a common RF ground point. In this scenario
the power cable’s drain wire should be connected directly to the battery’s
negative terminal.

SeaTalk NG Power cable extension
If you need to extend the length of the SeaTalk NG power cable, ensure you
use suitably-rated cable, and that sufficient power is available at the SeaTalk
NG backbone’s power connection point:
• For power cable extensions, a minimum wire gauge of 16 AWG (1.31 mm2)
  is recommended. For cable runs longer than 15 m (49.2 ft), you may need
  to consider a thicker wire gauge (e.g. 14 AWG (2.08 mm2), or 12 AWG
  (3.31 mm2).
• To ensure power cables (including any extension) are of a sufficient gauge,
  ensure that there is a continuous minimum voltage of 10.8 V dc at the
  end of the cable where it enters the product’s power connector, even
  with a fully flat battery at 11 V dc. (Do not assume that a flat battery is at
  0 V dc. Due to the discharge profile and internal chemistry of batteries,
  the current drops much faster than the voltage. A “fully flat” battery still
  shows a positive voltage, even if it doesn’t have enough current to power
  your device.)

 Important:
 Be aware that some products in your system (such as sonar modules)
 can create voltage peaks at certain times, which may impact the voltage
 available to other products during the peaks.

More information
It is recommended that best practice is observed in all vessel electrical
installations, as detailed in the following standards:
• BMEA Code of Practice for Electrical and Electronic Installations in Boats
• NMEA 0400 Installation Standard

• ISO 13297: Small craft — Electrical systems — Alternating and direct
  current installations
• ISO 10133: Small craft — Electrical systems — Extra-low-voltage d.c.
  installations
• ABYC E-11 AC & DC Electrical Systems on Boats
• ABYC A-31 Battery chargers and Inverters
• ABYC TE-4 Lightning Protection

              Warning: Product grounding
              Before applying power to this product, it MUST be correctly
              grounded, in accordance with the instructions provided.

              Warning: Positive ground systems
              Do not connect this unit to a system which has positive
              grounding.

10.7 Power connection via Autopilot Control
Unit (ACU-Series)
The SeaTalk NG backbone can be supplied 12 V dc power from a compatible
Raymarine Autopilot Control Unit (ACU-Series).

 Important:
 The SeaTalk NG backbone must have a single power supply connection.
 If your SeaTalk NG backbone is supplied power directly from a battery or
 distribution panel, then you must ensure that the SeaTalk NG power switch
 on your ACU-Series is switched Off.

 Note:
 ACU-100, ACU-150 and SPX-5 autopilot control units cannot supply power
 to the SeaTalk NG backbone.

<!-- figure 1 on pdf page 46 at 602,155-801,210 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 46 at 427,158-492,210 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 46 at 427,218-492,270 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 46 at 720,218-801,270 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 47 | printed page 47 | footer: Power connections -->

1.   Fuse for SeaTalk NG power supply.
2. Power switch for SeaTalk NG power supply:
     a.   Select the [OFF] position if your SeaTalk NG backbone is supplied
          power directly from a battery or distribution panel.
     b.   Select the [ON] position if your SeaTalk NG backbone is supplied
          power by the ACU-Series.
3.   ACU-Series/SPX-Series autopilot to SeaTalk NG spur cable (part number:
     R12112).

<!-- figure 1 on pdf page 47 at 38,38-413,282 pt | caption: none | text-layer labels: none | nearby labels: 1. | Fuse for SeaTalk NG power supply. | OCR text follows (tesseract, unverified; 15/22 words >= 60, mean confidence 66) -->
POWER
OFF
on
Raymarine UK Ltd
ce
12
SLEEP
GROUND
RUDDER
ER
MOT
POV/ER
OFF
<!-- end of figure 1 -->

<!-- pdf page 48 | printed page 48 -->

CHAPTER 11: NMEA 2000 CONNECTION
CHAPTER CONTENTS

•   11.1 NMEA 2000 network connection — page 49

<!-- pdf page 49 | printed page 49 -->

11.1 NMEA 2000 network connection
Your SeaTalk NG device can be connected to a DeviceNet / NMEA 2000
network.

1.   SeaTalk NG device.
2. SeaTalk NG to DeviceNet (male) adapter cable (A06078, A06074,
   A06076, or A06046).
3.   DeviceNet T-piece.
4.   NMEA 2000 backbone.

NMEA 2000 connection                                                 49

<!-- figure 1 on pdf page 49 at 38,93-413,332 pt | caption: none | text-layer labels: none | nearby labels: 1. | SeaTalk NG device. | OCR text follows (tesseract, unverified; 6/7 words >= 60, mean confidence 76) -->
$1
device
3?
NMEA
2000
*2
<!-- end of figure 1 -->

<!-- pdf page 50 | printed page 50 -->

CHAPTER 12: SETUP AND CALIBRATION
CHAPTER CONTENTS

•   12.1 Camera setup — page 51
•   12.2 AR200 Calibration (Linearization) — page 54

<!-- pdf page 51 | printed page 51 | footer: Setup and calibration -->

12.1 Camera setup
Before using the Augmented Reality features, it’s important to correctly install
and setup your compatible camera.
Refer to your camera’s installation manual to determine the correct physical
installation and connections for using the camera as part of an Augmented
Reality system.
A number of additional camera-related settings and calibrations must be
completed in the Video app before Augmented Reality features can be used:
• Camera height above the waterline.
• Camera direction.
• Camera horizontal field of view [not required for cameras which auto
  assign their field of view].
• Horizon calibration.

 Note:
 • The camera’s height above the waterline and camera’s view direction
   need to be physically measured for accurate camera installation.
 • The camera’s horizontal field of view can be found in your camera’s
   installation manual specification.

Fixed camera calibration
Fixed mount cameras require calibration for Augmented Reality to function
correctly.
1. For first time setup, either:
   i. Select [Enter details] from the notification when the Video app is
        opened.
   ii. Select [Enter details] from the [ClearCruise] settings menu: [Menu >
        Settings > ClearCruise].
   iii. Select [Configure] from the [Camera setup] settings menu: [Settings >
        Camera Setup > Camera Installation > Configure].
   The [Camera installation] details page is displayed.

2. The [Camera Installation] page contains camera installation options which
   all need to be completed correctly.
3. Adjust the values of [Camera height above waterline], [Camera direction]
   and [Field of view (horizontal)] by selecting the field for each settings and
   using the arrows to adjust the value..
 Setting                                 Options
 [Camera height above waterline]         • 0m to 50m
                                         • 0ft to 165ft
 [Camera direction]                      • 0° (Forward) (default)
                                         • 0° to 180°p (Port)
                                         • 0° to 180°s (Starboard)
 [Field of view]                         • 30° to 120°
                                         • [CAM210IP – 53°]
                                         • [CAM220IP – 93°]
                                         • [CAM300 – 90° recommended]

 Important:
 Incorrect physical camera installation and incorrect installation settings
 could result in an inaccurate Augmented Reality overlay.

4. Select [Horizon position].
   The [Calibrate horizon] page is displayed.

<!-- figure 1 on pdf page 51 at 444,38-801,179 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 19/30 words >= 60, mean confidence 71) -->
Camera installation dete”
Camera height above waterline:
9.8ft
Camera direction:
K
Horizon Position:
Set
53°
Field of view (horizontal):
<!-- end of figure 1 -->

<!-- pdf page 52 | printed page 52 -->

5. Use the [Up], [Down], [Rotate left] and [Rotate right] buttons to align the
   red line with the horizon.
6. Select [Done].

 Important:
 Calibrating the horizon correctly is essential for accurate Augmented
 Reality overlay. Calibrating on calm water and in clear sight of the horizon
 is recommended.

Pan and Tilt camera calibration
Pan and Tilt cameras require calibration for Augmented Reality to function
correctly.
1. For first time setup, either:
   i. Select [Enter details] from the notification when the Video app is
        opened.
   ii. Select [Enter details] from the [ClearCruise] settings menu: [Menu >
        Settings > ClearCruise].
   iii. Select [Configure] from the [Camera setup] settings menu: [Settings >
        Camera Setup > Camera Installation > Configure].
   The [Camera installation details] page is displayed.

2. Select the [Camera height above waterline] field and adjust the value
   using the arrows.
 Menu item                               Options
 [Camera height above waterline]         • 0m to 50m
                                         • 0ft to 165ft

 Important:
 Incorrect physical camera installation and incorrect installation settings
 could result in an inaccurate Augmented Reality overlay.

3. Select the [Set] button for [Forward position].
   The [Set forward position] page is displayed.

<!-- figure 1 on pdf page 52 at 55,38-413,196 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/12 words >= 60, mean confidence 35) -->
Calibrate horizon
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 52 at 444,38-801,153 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/18 words >= 60, mean confidence 82) -->
Camera installation det
Camera height above waterline:
9.8ft
Forward position:
Set
4
Horizon Position:
Set
<!-- end of figure 2 -->

<!-- pdf page 53 | printed page 53 | footer: Setup and calibration -->

4. Use the touchscreen to adjust the camera’s direction so that the vertical
   line is positioned directly forward, parallel to your vessel’s forward
   position.

                  Important:
                  • Calibrating the camera’s forward position is essential
                    for accurate Augmented Reality overlay when the
                    camera pans and tilts. Calibrating on calm water
                    and with a clear view of the front of your vessel is
                    recommended.
                  • Certain cameras display a camera direction indicator,
                    which can help identify when the camera is facing
                    directly forward.

5. Select [Save].
6. Select [Horizon position].
   The [Calibrate horizon (1 of 2)] page is displayed.

7. Using the buttons, tilt the red lines until they are parallel to the horizon.
8. Pan the camera by approximately 90° and correct the angle if necessary.
9. Repeat the previous step until you have panned at least 360° and the
    lines are parallel on each subsequent pan of the camera.
10. Select [Next] .
    The [Calibrate horizon (2 of 2)] page is displayed.

<!-- figure 1 on pdf page 53 at 55,38-413,241 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 17/17 words >= 60, mean confidence 96) -->
Set forward position
Point the camera in the forward direction and press the button to save
Save
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 53 at 444,38-801,241 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 59/66 words >= 60, mean confidence 88) -->
Calibrate horizon (1 of 2)
Reset
1, Using the buttons, tilt the red lines until they are parallel to the horizon.
2. Pan the camera by approximately 90° and correct the angle if necessary. It is best to repeat this at several camera angles.
3. When the lines are parallel to the horizon at all angles, press Next
Next
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 53 at 46,289-408,449 pt | caption: none | text-layer labels: Important: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 53 at 444,337-801,533 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 39/44 words >= 60, mean confidence 88) -->
Calibrate horizon (2 of 2)
Move the red line up/down with the buttons to place it exactly on the horizon. This will improve placement accuracy of Augmented
Reset
Reality items
When the line is in position, press Done
Done
<!-- end of figure 4 -->

<!-- pdf page 54 | printed page 54 -->

11. Use the buttons to move the red line up and down until it is placed exactly
    on the horizon.
12. Select [Done].

 Important:
 Calibrating the horizon correctly is essential for accurate Augmented
 Reality overlay. Calibrating on calm water and in clear sight of the horizon
 is recommended.

12.2 AR200 Calibration (Linearization)
To enable accurate placement of Augmented Reality (AR) flags on the
camera’s video feed, the AR200’s AHRS sensors need to compensate for
local magnetic fields, as well as the Earth’s magnetic fields.
Calibration is achieved using an automatic linearization process. The
linearization process starts automatically after your vessel has turned
approximately 100°, when travelling at a speed of between 3 to 15 knots.
The linearization process requires no user input, however at least a 270°
turn is required before linearization can be completed. The duration of the
linearization process can be decreased by completing a full 360° turn, when
travelling at a speed of between 3 to 15 knots. The linearization process can
also be restarted at anytime.

In the Video app the Linearization progress bar is displayed when
linearization is in progress. The bar is filled to indicate completeness, and will
turn Red if the process is paused or otherwise interrupted.
The time taken to complete the linearization process will vary according to
the characteristics of the vessel, the AR200’s installation location, and the
levels of magnetic interference present at the time linearization is performed.
Magnetic interference can be caused by objects onboard your vessel, such
as:
• Speakers

• Electronic equipment
• Electrical cabling
• Metal bulkhead or hull
Magnetic interference can also be caused by external objects in close
proximately to your vessel, such as:
• Metal hulled vessels
• Underwater electrical cables
• Marine pontoons

Magnetic deviation
Magnetic deviation is the error induced in a compass caused by interference
from local magnetic fields.
The automatic linearization process results in a deviation value being set for
your AR200. If Augmented Reality flags in the Video app are not aligned with
their onscreen objects, or the compass is out of alignment, you should check
the AR200’s current calibration settings. For instructions on how to do this,
refer to the following section: p.54 — AR200 calibration settings

AR200 calibration settings
The calibration settings page provides access to the AR200’s compass
calibration options.
The AR200 calibration settings can be accessed by selecting [Calibrate] from
the AR200’s pop-over menu on the Network settings page: [Homescreen >
Settings > Network > AR200 > Calibrate].

<!-- figure 1 on pdf page 54 at 38,349-413,418 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/7 words >= 60, mean confidence 70) -->
AR200 in progress
Range: 2.00nm
<!-- end of figure 1 -->

<!-- pdf page 55 | printed page 55 | footer: Setup and calibration -->

    Description
1   [Current reading:]
    The current heading reported by the AR200.
2   [Calibration in progress:]
    While linearization is in progress the progress percentage is
    displayed.
    [Maximum deviation at last calibration:]
    If calibration is complete then the maximum deviation reported
    during the last linearization process is shown.

     Important:
     If the [Maximum deviation at last calibration] is 45° or above, it
     is recommended that the AR200 unit is moved and re-installed
     in a location which is subject to less magnetic interference.

       Description
 3     [Compass offset]
       Once the linearization process has completed, it is possible that the
       heading value may be slightly out of alignment. This is common
       where installation space is limited and the AR200 is not properly
       aligned with your vessel’s longitudinal axis. In this case, it is possible
       to manually adjust the Compass offset.
 4     [Compass lock]
       When enabled, the Compass lock prevents the continual monitoring
       and adaptation of the compass linearization process. For more
       information, refer to: p.55 — Compass lock.
 5     [Reset calibration]
       You can reset your AR200’s current linearization settings by
       selecting [Reset calibration]

Continual monitoring and adaptation
To ensure optimum performance, after the initial linearization process is
complete the unit continues to monitor and adapt the compass linearization
to suit current conditions.
If the conditions for linearization are less than ideal, the automatic
linearization process temporarily pauses until conditions improve again. The
following conditions can cause the linearization process to temporarily pause:
• significant magnetic interference is present
• vessel speed too slow or too fast
• rate-of-turn too slow or too fast

Compass lock
Once you are satisfied with the compass accuracy, you can lock the setting
to prevent the system from completing a further automatic linearization in
the future.
This feature is particularly useful for vessels in environments that are exposed
to strong magnetic disturbances on a regular basis (such as offshore wind
farms or very busy rivers, for example). In these situations it may be desirable
to use the Compass lock feature to disable the continuous linearization
process, as the magnetic interference may build a heading error over time.

<!-- figure 1 on pdf page 55 at 38,38-413,270 pt | caption: none | text-layer labels: Description | nearby labels: 3 | 4 | 5 | 1 | [Current reading:] | OCR text follows (tesseract, unverified; 24/32 words >= 60, mean confidence 74) -->
Calibrate E70537 for heading
41?
Current reading
133°T
2?
Calibration in progress
0%
3?
Compass offset
-2°
Compass lock
4?
5?
Reset calibration
Reset
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 55 at 74,409-391,473 pt | caption: none | text-layer labels: Important: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 56 | printed page 56 | header: Note: -->

The compass lock may be released at any time, to allow the compass
continual monitoring and adaptation to re-commence. This is particularly
useful if planning a long voyage. The earth’s magnetic field will change
significantly from one geographical location to another, and the compass
can continually compensate for the changes, ensuring you maintain
accurate heading data throughout the voyage.

<!-- pdf page 57 | printed page 57 | footer: System checks and troubleshooting -->

CHAPTER 13: SYSTEM CHECKS AND TROUBLESHOOTING
CHAPTER CONTENTS

•   13.1 Augmented Reality (AR) initial test — page 58
•   13.2 GNSS (GPS) check — page 58
•   13.3 Troubleshooting — page 59

<!-- pdf page 58 | printed page 58 | header: Note: -->

13.1 Augmented Reality (AR) initial test
With the AR200 sensor and a compatible IP camera successfully installed,
you can perform an initial check of your Augmented Reality system.

 Note:
 Displays must be running:
 • LightHouse 3 v3.7.70 or later.
 • LightHouse 4 v4.0.70 or later

1. Select the [Video] app icon from the Homescreen.
2. Select the [Menu] icon.
3. Select your Augmented Reality compatible IP camera.
   When you select the relevant camera, in addition to the video feed being
   displayed v4.0.70ClearCruise® AR features are also displayed onscreen.

1.   Compass bar and heading indicator.
2. AR Object (AIS, Waypoint and Chart object) flag toggle options.
3.   AR Object detection range.

 Note:
 If the AR features are not displayed, ensure that the [AUGMENTED
 REALITY] toggle switch is enabled in the [ClearCruise] settings menu:
 [Menu > Settings > ClearCruise > AUGMENTED REALITY].

13.2 GNSS (GPS) check
If you intend to use the AR200 as your system’s main GNSS (GPS) receiver,
you may need to manually select it from the [Data sources] menu.
The Data sources menu can be accessed from your Data master display:
[Homescreen > Settings > Network > Data sources > GPS].

To choose the AR200 as your preferred source for GNSS (GPS) position data,
select [Raymarine AR200 GNSS] from the list of devices, and then select
[Always use this device] from the Pop-over options. This will make the AR200
the preferred source for GNSS (GPS) position data.
Once selected, a tick is placed in the [Preferred] column and the [Manual
selection] toggle switch will be enabled. If your AR200 has a position fix,
position accuracy is displayed in the [Value] column.

<!-- figure 1 on pdf page 58 at 427,208-801,356 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 57/72 words >= 60, mean confidence 79) -->
Data sources
Depth
Speed through water
Heading
GPS datum
Time and date
Wind
Preferred
Source device
Value
Serialnum Port
Manual selection
Raymarine YachtSense Link GNSS
Internal
AFOOOGW
preferred source
for this type of data, activate
4
Internal
Raymarine AR200 GNSS
0980006
‘manual selection" and tick
your preferred source
O
Internal GPS
TAGG80X Unknown
Internal GPS
0901205 Unknown
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 58 at 38,268-413,495 pt | caption: none | text-layer labels: none | nearby labels: 1. | Compass bar and heading indicator. | OCR text follows (tesseract, unverified; 14/23 words >= 60, mean confidence 69) -->
VIDEO
x
Home
hold
[P] Park camera
REAR VIE
BAT
RI
025
E703
3
<!-- end of figure 2 -->

<!-- pdf page 59 | printed page 59 | footer: System checks and troubleshooting -->

When a valid position fix is achieved, your vessel’s latitude and longitude
position is displayed on the Homescreen in the top left corner. Fix details
can be viewed by selecting the current position coordinates and selecting
[Satellites] from the Pop-over options.

13.3 Troubleshooting
The troubleshooting section provides possible causes and the corrective
action required for common problems that are associated with the installation
and operation of your product.
Before packing and shipping, all Raymarine products are subjected to
comprehensive testing and quality assurance programs. If you do experience
problems with your product, this section will help you to diagnose and correct
problems to restore normal operation.
If after referring to this section you are still having problems with your
product, please refer to the Technical support section of this manual for
useful links and Raymarine technical support contact details.

LED Diagnostics
 LED indication                 Status and required action
                                Green LED is off once every 15 seconds.
                                • All sensors connected and ready.
                                • Bus healthy, no communication faults
                                No action required.
                                Green LED flashes on and off once every
                                second.
                                All sensors are initializing.
                                No action required.
                                Green LED flashes on and off once every 2
                                seconds.
                                GNSS (GPS) initializing

                                 Note:
                                 Can take up to 5 minutes at first use or
                                 after factory reset or software update.

                                No action required.

<!-- figure 1 on pdf page 59 at 38,38-413,282 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 34/45 words >= 60, mean confidence 76) -->
Satellites
Accuracy: 5,5ft
Satellites
Raymarine AR200 via STng(150)
inuse
HDOP:
1.0
lost
Accuracy:
6.3ft
Fix Status:
Fix
Position:
50°49.479'N
001°10.245' W
Date:
03/07/2022
Time:
03:10:38pm
Mode:
Automatic differential
Show Signal (dB) Datum:
WGS 1984
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 59 at 434,232-799,299 pt | caption: none | text-layer labels: LED indication | Status and required action | Green LED is off once every 15 seconds. | • All sensors connected and ready. | nearby labels: LED Diagnostics | • Bus healthy, no communication faults | No action required. | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 91) -->
15s
14.5s
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 59 at 434,328-573,373 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 73) -->
1s
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 59 at 432,392-573,435 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 91) -->
2s
1s
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 59 at 580,445-777,497 pt | caption: none | text-layer labels: Note: | nearby labels: GNSS (GPS) initializing | No action required. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 60 | printed page 60 -->

LED indication   Status and required action
                 Green LED flashes on and off once every 4
                 seconds.
                 Compass linearizing.
                 Refer to:
                 p.54 — AR200 Calibration (Linearization)
                 Red LED flashes on once every 3 seconds.
                 No GNSS (GPS) signal.
                 User actions:
                 1.   Try power cycling the system.
                 2. Ensure there is a clear view of the sky.
                 3.   Check for interference from other
                      devices.
                 4.   Check installation location. Refer to
                      p.24 — Location requirements
                 Red LED flashes on twice every 4 seconds.
                 Cannot send data.
                 User actions:
                 1.   Check condition of Bus cabling.
                 2. Ensure bus is correctly terminated.
                 3.   Ensure bus has correct voltage.
                 4.   Replace device.
                 Red LED flashes on 7 times every 9 seconds.
                 Devices are not receiving data.
                 User actions:
                 1.   Check condition of Bus cabling.
                 2. Ensure bus is correctly terminated.
                 3.   Ensure bus has correct voltage.
                 4.   Replace device.

Switching off sensor LEDs
To assist users who wish their vessel to “go dark” (i.e. not emit any visible
light), the LED indicators present on SeaTalk NG position sensors can be
switched off. Supported devices: RS150, EV-1, EV-2 and AR200).

 Note:
 The [Always Off] feature may not be available for devices running older
 software versions. Ensure that you obtain the latest available software for
 your position sensors.

1. Open the [Network] settings menu: [Homescreen > Settings > Network].
2. Select the relevant sensor from the network list.
3. Select [LEDs:].
4. Select [Always Off].
The status LED on the selected device will now be switched off, and will
remain off until this setting is reverted to [Normal], or the [Find Me] feature is
enabled.

Find me
The [Find me] feature assists you in finding the physical installation location
of a specific Raymarine SeaTalk NG position sensor (i.e.: RS150, EV-1, EV-2, or
AR200).
The [Find me] feature works by making the selected device’s status LED flash
continuously for 5 minutes, giving you time to search the vessel to determine
the device’s physical location. The feature works even if the device’s LEDs
have been switched to [Always off].

<!-- figure 1 on pdf page 60 at 46,65-187,110 pt | caption: none | text-layer labels: none | nearby labels: LED indication | OCR text follows (tesseract, unverified; 2/3 words >= 60, mean confidence 71) -->
4s
x1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 60 at 46,139-187,182 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 83) -->
3s
2.75s
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 60 at 427,175-801,330 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 43/48 words >= 60, mean confidence 87) -->
Settings
Boat details
This displa
Autopilot
Getting started
Units
Rename
Product
rsion
Product info
Raymarine iTC5 Converter 0420065
Normal
Raymarine EV-2 Course Computer 0430008
LEDs: Always Off
Always Off
Raymarine p70s Control Head £70328 0360009
Cancel Find Me
Raymarine AR200 0980006
Factory reset
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 60 at 46,289-187,330 pt | caption: none | text-layer labels: none | nearby labels: 4. | 1. | OCR text follows (tesseract, unverified; 3/3 words >= 60, mean confidence 93) -->
4s
1.75s
1.75s
<!-- end of figure 4 -->
<!-- figure 5 on pdf page 60 at 46,411-187,457 pt | caption: none | text-layer labels: none | nearby labels: 3. | 4. | 1. | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 68) -->
9s
1s
0.29s
<!-- end of figure 5 -->

<!-- pdf page 61 | printed page 61 | footer: System checks and troubleshooting -->

The [Find Me] flash sequence will be visibly different than normal LED status
sequences in that both the red and green LEDs will flash on and off at the
same time, twice every second for 5 minutes.

 Note:
 The [Find me] feature may not be available on devices running older
 software versions. Ensure that you obtain the latest available software for
 your position sensors.

To initiate the [Find Me] feature for a specific SeaTalk NG device, locate the
device name in the [Network] settings menu, and then select [Find Me] from
the device’s pop-over menu.
Once [Find Me] has been activated, its menu option will change to [Cancel
Find Me] until 5 minutes has elapsed.
Selecting [Cancel Find Me] at any time within the 5 minute timeframe will stop
the LED flashing and return the device to its previous LED state.

GNSS (GPS) troubleshooting
Problems with the GNSS (GPS) and their possible causes and solutions are
described here. Your position fix coordinates are displayed in the status area
located in the top left corner of the Homescreen.
No position fix

Possible causes         Possible solutions
Display installation    Connect an external passive GNSS (GPS) antenna
location (e.g.:         such as the GA200 to the display GPS antenna
installed below         connection.
decks or in
close proximity
to equipment
which may cause
interference).
Internal GNSS (GPS)     When using your product’s internal GNSS (GPS)
receiver disabled.      receiver, ensure that it is enabled in the relevant
                        settings menu.
                        To access the relevant menu, select the status area
                        located in the top left corner of the Homescreen
                        and select [Satellites] and then select the [Settings]
                        tab, locate the Internal GPS option and ensure it is
                        enabled.
External GNSS (GPS)     When using an external GNSS (GPS) receiver,
receiver connection     ensure that connections are secure and that the
fault.                  cabling is free from damage.
External GNSS           Ensure the GNSS (GPS) receiver or antenna has a
(GPS) receiver or       clear unobstructed view of the sky.
antenna location
                        Refer to the documentation supplied with your
(e.g.: installed
                        external receiver / antenna and ensure location
below decks or
                        requirements have been adhered to.
in close proximity
to equipment
which may cause
interference).
Geographic              Check periodically to see if a fix is obtained in better
location or             conditions or another geographic location.
prevailing conditions
preventing satellite
fix.

<!-- figure 1 on pdf page 61 at 38,167-413,359 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 55/74 words >= 60, mean confidence 77) -->
Settings
Getting started
Boat details
Units
This display
Autopilot
Rename
Product
Nome
Version
Raymarine iTC5 Converter 0420065
Product Info
3.15 (RSCP V1
EV-2 Course Computer
LEDs
Nor
a
Rename
p70s 0360009
3.13
Find Me
Product info
Raymarine AR200 GNSS 0980006
1.33
Factory reset
LEDs:
Cancel Find Me
Raymarine AR200 GNSS £70537 0980006
1.33
Factory reset
<!-- end of figure 1 -->

<!-- pdf page 62 | printed page 62 -->

Augmented Reality (AR) Troubleshooting
AR options not available in Video app
Possible causes        Possible solutions
Wrong camera           Ensure that the correct AR-compatible camera has
selected.              been selected in the Video app menu.
Compatible camera      1.   Ensure your camera is AR compatible.
not detected.
                       2. Ensure your camera is correctly installed and
                          networked to your MFD.
AR200 not detected.    Ensure your AR200 is correctly installed and on the
                       same network as the MFD from which you are using
                       the AR features.
Incorrect LightHouse   Ensure that your MFD is running LightHouse 3
software version.      v3.7.70 or later, or LightHouse 4.
AR options turned      The Compass bar, AIS, Waypoint and Chart object
off.                   flags can be enabled and disabled from the
                       [ClearCruise] settings page ([Video app > Menu >
                       Settings > ClearCruise]). Ensure relevant options
                       are enabled.

                        Note:
                        For AIS flags to be displayed, compatible AIS
                        hardware must be operational and connected
                        to the same network as your MFD.

AR flags do not appear directly above on-screen targets
Possible causes        Possible solutions
AIS update rate        Depending on the classification of the target’s AIS
                       hardware, transmitted position updates may be sent
                       up to 3 minutes apart and therefore the flag may
                       appear up to 3 minutes behind the actual onscreen
                       target.
Camera Field of View Ensure that the FOV setting reflects your
(FOV) set incorrectly. camera’s horizontal FOV. Check your camera’s
                       documentation for FOV specifications.

Possible causes      Possible solutions
AR200 interference   If your AR200 is installed in a location which includes
                     a source of magnetic interference large enough to
                     affect AR flag placement, you may need to re-install
                     the AR200 in a different location.
Deviation too high   1.   Reset the AR200 calibration by selecting [Reset]
                          from the AR200 calibration page: [Homescreen
                          > Settings > Network > Data sources > Heading
                          > Raymarine AR200 Attitude > Calibrate].
                     2. If the problem persists, you may need to move
                        your AR200 to a location with less magnetic
                        interference.

<!-- figure 1 on pdf page 62 at 41,325-413,394 pt | caption: none; nearest centred text below: "AR flags do not appear directly above on-screen targets" | text-layer labels: Note: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 63 | printed page 63 -->

CHAPTER 14: OPERATION
CHAPTER CONTENTS

•       14.1 Operation instructions — page 64

Operation                                       63

<!-- pdf page 64 | printed page 64 -->

14.1 Operation instructions
For detailed operation instructions for your product, refer to the
documentation that accompanies your display.
 Document           Description                    Link
 81406              LightHouse 4 Advanced          www.bit.ly/LH4-docs
                    Operation Instructions
 81370              LightHouse 3 Advanced          www.bit.ly/LH3-docs
                    Operation Instructions

<!-- pdf page 65 | printed page 65 -->

CHAPTER 15: MAINTENANCE
CHAPTER CONTENTS

•       15.1 Service and maintenance — page 66
•       15.2 Routine equipment checks — page 66
•       15.3 Product cleaning — page 66

Maintenance                                       65

<!-- pdf page 66 | printed page 66 -->

15.1 Service and maintenance
This product contains no user serviceable components. Please refer all
maintenance and repair to authorized Raymarine dealers. Unauthorized
repair may affect your warranty.

15.2 Routine equipment checks
It is recommended that you perform the following routine checks, on a
regular basis, to ensure the correct and reliable operation of your equipment:
• Examine all cables for signs of damage or wear and tear.
• Check that all cables are securely connected.

15.3 Product cleaning
Best cleaning practices.
When cleaning products:
• Switch off power supply.
• Use a clean damp cloth to wipe clean.
• Do NOT use: abrasive, acidic, ammonia, solvent or other chemical based
  cleaning products.
• Do NOT use a jet wash.

<!-- pdf page 67 | printed page 67 -->

CHAPTER 16: TECHNICAL SUPPORT
CHAPTER CONTENTS

•        16.1 Raymarine technical support and servicing — page 68
•        16.2 Learning resources — page 69
•        16.3 Operation instructions — page 69

Technical support                                                   67

<!-- pdf page 68 | printed page 68 -->

16.1 Raymarine technical support and
servicing
Raymarine provides a comprehensive product support service, as well as
warranty, service, and repairs. You can access these services through the
Raymarine website, telephone, and e-mail.
Product information
If you need to request service or support, please have the following
information to hand:
• Product name.
• Product identity.
• Serial number.
• Software application version.
• System diagrams.
You can obtain this product information using diagnostic pages of the
connected display.
Servicing and warranty
Raymarine offers dedicated service departments for warranty, service, and
repairs.
Don’t forget to visit the Raymarine website to register your product
for extended warranty benefits: https://www.raymarine.com/en-
us/support/product-registration
United Kingdom (UK), EMEA, and Asia Pacific:
• E-Mail: emea.service@raymarine.com
• Tel: +44 (0)1329 246 932
United States (US):
• E-Mail: rm-usrepair@flir.com
• Tel: +1 (603) 324 7900
Web support
Please visit the “Support” area of the Raymarine website for:
• Manuals and Documents — http://www.raymarine.com/manuals
• Technical support forum — https://raymarine.custhelp.com/app/home
• Software updates — http://www.raymarine.com/software
Worldwide support

United Kingdom (UK), EMEA, and Asia Pacific:
• Help desk: https://raymarine.custhelp.com/app/home
• Tel: +44 (0)1329 246 777
United States (US):
• Help desk: https://raymarine.custhelp.com/app/home
• Tel: +1 (603) 324 7900 (Toll -free: +800 539 5539)
Australia and New Zealand (Raymarine subsidiary):
• E-Mail: aus.support@raymarine.com
• Tel: +61 2 8977 0300
France (Raymarine subsidiary):
• E-Mail: support.fr@raymarine.com
• Tel: +33 (0)1 46 49 72 30
Germany (Raymarine subsidiary):
• E-Mail: support.de@raymarine.com
• Tel: +49 40 237 808 0
Italy (Raymarine subsidiary):
• E-Mail: support.it@raymarine.com
• Tel: +39 02 9945 1001
Spain (Authorized Raymarine distributor):
• E-Mail: sat@azimut.es
• Tel: +34 96 2965 102
Netherlands (Raymarine subsidiary):
• E-Mail: support.nl@raymarine.com
• Tel: +31 (0)26 3614 905
Sweden (Raymarine subsidiary):
• E-Mail: support.se@raymarine.com
• Tel: +46 (0)317 633 670
Finland (Raymarine subsidiary):
• E-Mail: support.fi@raymarine.com
• Tel: +358 (0)207 619 937
Norway (Raymarine subsidiary):

<!-- pdf page 69 | printed page 69 -->

• E-Mail: support.no@raymarine.com
• Tel: +47 692 64 600
Denmark (Raymarine subsidiary):
• E-Mail: support.dk@raymarine.com
• Tel: +45 437 164 64
Russia (Authorized Raymarine distributor):
• E-Mail: info@mikstmarine.ru
• Tel: +7 495 788 0508

Viewing product information
Use the [Settings] menu to view hardware and software information about
your display, and connected products.

1. Select [Settings], from the Homescreen.
   The [Getting started] menu contains hardware and software information
   for your display.

Technical support

2. You can view further information about your display, or view information
   about products networked using SeaTalk HS and SeaTalk NG / NMEA
   2000, by selecting the [Network] tab, then:
   i. to display detailed software information and your display’s network
       IP address, select your display from the list.
   ii. to display detailed diagnostics information for all products, select
       [Product info] from the [Diagnostics] pop over menu.

16.2 Learning resources
Raymarine has produced a range of learning resources to help you get the
most out of your products.

Video tutorials
Raymarine official channel on YouTube
• http://www.youtube.com/user/RaymarineInc

Training courses
Raymarine regularly runs a range of in-depth training courses to help you
make the most of your products. Visit the Training section of the Raymarine
website for more information:
• http://www.raymarine.co.uk/view/?id=2372

Technical support forum
You can use the Technical support forum to ask a technical question about
a Raymarine product or to find out how other customers are using their
Raymarine equipment. The resource is regularly updated with contributions
from Raymarine customers and staff:
• https://raymarine.custhelp.com/app/home

16.3 Operation instructions
For detailed operation instructions for your product, refer to the
documentation that accompanies your display.
All product documentation is available to download from the Raymarine
website: https://bit.ly/rym-docs
                                                                              69

<!-- figure 1 on pdf page 69 at 38,241-413,490 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 92/147 words >= 60, mean confidence 64) -->
Settings
Network
AXIOM PRO (E70483 0870964)
‘Software version 4.3.7
Settings
Boat
‘View terms
Regulatory
2 TAGGBOX
(US)
0500025
Raymarine FICS Converter
EV-2 Course Computer £70097 0430008
Product information
‘SeaTalk-STNG-Converter £22158 0500025
2.03
version:
‘Data sources:
CAN address:
73
Database Version:
130
Model Version:
SeaTalk-STNG-Converter
Product Code:
1
Product ID:
£221
Product name:
‘SeaTalk-STNG-Converter
Converter 0420065.
Ri
info
Application
112
CAN address:
69
Database Version
1210
Model Version:
Raymarine (TCS Converter
Product Code:
12743
Product ID;
Product name:
Raymarine Converter
EV-2 Course Computer 0430008
3.02 (RSCP V1 L4)
version:
CAN adare
Database Version:
<!-- end of figure 1 -->

<!-- pdf page 70 | printed page 70 -->

CHAPTER 17: TECHNICAL SPECIFICATION
CHAPTER CONTENTS

•   17.1 Power specification — page 71
•   17.2 Environmental specification — page 71
•   17.3 GNSS (GPS) receiver specification — page 71
•   17.4 AHRS specification — page 71
•   17.5 Conformance specification — page 72

<!-- pdf page 71 | printed page 71 -->

17.1 Power specification
 Specification
 Nominal supply voltage:      12 V dc (Supplied by the SeaTalk NG
                              network.)
 Operating voltage range:     9 V dc to 16 V dc (protected up to 32 V dc)
 Power consumption:           30 mA Max.
 LEN (Load Equivalency        1
 Rating):

17.2 Environmental specification
 Specification
 Operating temperature        -25 ºC to +55 ºC (-13 ºF to 131 ºF)
 range:
 Storage temperature range: -25 ºC to +70 ºC (-13 ºF to 158 ºF)
 Relative humidity:           93%
 Water ingress protection:    IPx6, IPx7

17.3 GNSS (GPS) receiver specification
 Specification
 Signal acquisition:          Automatic
 Channels:                    Simultaneously track up to 28 satellites.
 Operating frequency:         1574 MHz to 1605 MHz
 Update rate:                 10 Hz
 Sensitivity:                 • Cold start = -147 dBm
                              • Re-acquisition = -160 dBm
                              • Tracking = -164 dBm
 GNSS (GPS) satellite system • GPS
 compatibility:
                             • GLONASS
                              • Galileo ready
                              • Beidou ready
Technical specification

Specification
Satellite Differential Type   • WAAS (United States)
(SBAS):
                              • EGNOS (Europe)
                              • MSAS (Japan)
                              • GAGAN (India)
                              • QZSS ready (Japan)
Differential acquisition:     Automatic
Position accuracy without     < 15 m
SBAS (95%):
Position accuracy with        <5m
SBAS (95%):
Speed accuracy (95%):         < 0.3 kt
Time to first fix from cold   < 2 minutes (< 60 seconds typical)
start:
Time to first fix from hot    < 45 seconds
start:
Geodetic Datum:               WGS–84
Antenna:                      Internal

17.4 AHRS specification
Specification
AHRS:                         • 3–Axis digital accelerometer
                              • 3–Axis digital compass
                              • 3–Axis MEMS Gyro digital angular rate
                                sensor
Magnetic compass              • Static = ≤1° RMS
accuracy:
                              • Dynamic = ≤3° RMS
Pitch, Roll and Yaw           ≤1°
accuracy:
Heading, Pitch, Roll and      10 Hz
Rate of Turn update rate:
                                                                        71

<!-- pdf page 72 | printed page 72 -->

17.5 Conformance specification
Specification
EMC Directive:              2014/30/EU
Australia and New Zealand   Level 2
C-Tick compliance:
RoHS Directive:             2011/65/EU
WEEE Directive:             2012/19/EU

<!-- pdf page 73 | printed page 73 | footer: Spares and accessories -->

CHAPTER 18: SPARES AND ACCESSORIES
CHAPTER CONTENTS

•   18.1 Accessories — page 74
•   18.2 SeaTalk NG cables and accessories — page 74

<!-- pdf page 74 | printed page 74 -->

18.1 Accessories
The following accessories are available:

 Part           Description
 A80437         Deck mounting (Clamshell / Riser) kit.
 A80370         Pole / rail mounting adaptor kit.
 A06072         6 m (19.69 ft) SeaTalk NG white spur cable.

18.2 SeaTalk NG cables and accessories
SeaTalk NG cables and accessories for use with compatible products.

SeaTalk NG kits
SeaTalk NG kits enable you to create a simple SeaTalk NG backbone.
Starter kit (part number: T70134) consists of:

1.   1 x Spur cable 3 m (9.8 ft) (part number: A06040). Used to connect
     device to the SeaTalk NG backbone.
2. 1 x Power cable 2 m (6.6 ft) (part number: A06049). Used to provide
   12 V dc power to the SeaTalk NG backbone.
3.   2 x Backbone terminators (part number: A06031). Terminators must be
     fitted to both ends of the SeaTalk NG backbone.
4.   1 x 5-Way connector (part number: A06064). Each connector block
     allows connection of up to 3 SeaTalk NG devices. Multiple connector
     blocks can be ‘daisy chained’ together.
Backbone kit (part number: A25062) consists of:

1.   2 x Backbone cables 5 m (16.4 ft) (part number: A06036). Used to create
     and extend the SeaTalk NG backbone.
2. 1 x Backbone cable 20 m (65.6 ft) (part number: A06037). Used to create
   and extend the SeaTalk NG backbone.

<!-- figure 1 on pdf page 74 at 427,38-801,148 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 2/8 words >= 60, mean confidence 47) -->
1?
2?
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 74 at 38,84-413,335 pt | caption: none | text-layer labels: Part | Description | nearby labels: The following accessories are available: | 1. | 3. | 4. | A80437 | Deck mounting (Clamshell / Riser) kit. | A80370 | Pole / rail mounting adaptor kit. | OCR text follows (tesseract, unverified; 8/29 words >= 60, mean confidence 43) -->
A80437
A80370
i>)
a
NS
fh
2)
A06072
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 74 at 427,301-801,466 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR: no legible text (0/2 words >= 60, mean confidence 37) -->

<!-- pdf page 75 | printed page 75 | header: 3. | footer: Spares and accessories -->

3.   4 x T-piece (part number: A06028). Each T-piece allows connection
     of one SeaTalk NG device. Multiple T-pieces can be ‘daisy chained’
     together.
4.   2 x Backbone terminators (part number: A06031). Terminators must be
     fitted to both ends of the SeaTalk NG backbone.
5. 1 x Power cable 2 m (6.6 ft) (part number: A06049). Used to provide
   12 V dc power to the SeaTalk NG backbone.
Evolution-Series autopilot cable kit (part number: R70160) consists of:

1.   1 x Backbone cable 5 m (16.4 ft) (part number: A06036). Used to create
     and extend the SeaTalk NG backbone.
2. 1 x Spur cable 1 m (3.3 ft) (part number: A06040). Used to connect device
   to the SeaTalk NG backbone.
3.   1 x Power cable 2 m (6.6 ft) (part number: A06049). Used to provide
     12 V dc power to the SeaTalk NG backbone.
4.   1 x 5-Way connector (part number: A06064). Each connector block
     allows connection of up to 3 SeaTalk NG devices. Multiple connector
     blocks can be ‘daisy chained’ together.
5. 2 x T-pieces (part number: A06028). Each T-piece allows connection
   of one SeaTalk NG device. Multiple T-pieces can be ‘daisy chained’
   together.
6. 2 x Backbone terminators (part number: A06031). Terminators must be
   fitted to both ends of the SeaTalk NG backbone.
SeaTalk 1 to SeaTalk NG converter kit (part number: E22158) consists of:

1.   1 x Power cable 2 m (6.6 ft) (part number: A06049). Used to provide
     12 V dc power to the SeaTalk NG backbone.
2. 1 x Spur cable 1 m (3.3 ft) (part number: A06039). Used to connect a
   device to the SeaTalk NG backbone.
3.   1 x SeaTalk 1 (3 pin) to SeaTalk NG adapter cable 0.4 m (1.3 ft) (part
     number: A22164). Used to connect SeaTalk 1 devices to the SeaTalk NG
     backbone via the SeaTalk 1 to SeaTalk NG converter.
4.   1 x SeaTalk 1 to SeaTalk NG converter (part number: E22158). Each
     converter allows connection of one SeaTalk 1 device and up to 2 SeaTalk
     NG devices.
5. 2 x Spur blanking plugs (part number: A06032). Used to cover unused
   spur connections in 5-way blocks, T-piece connectors and SeaTalk 1
   to SeaTalk NG converter.
6. 2 x Backbone terminators (part number: A06031). Terminators must be
   fitted to both ends of the SeaTalk NG backbone.
NMEA 0183 VHF 2-wire to SeaTalk NG converter kit (part number: E70196)
consists of:

<!-- figure 1 on pdf page 75 at 427,38-801,172 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 3/9 words >= 60, mean confidence 51) -->
1?
2?
3°
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 75 at 38,158-413,292 pt | caption: none | text-layer labels: none | nearby labels: 1. | 1. | 3. | 4. | OCR text follows (tesseract, unverified; 4/9 words >= 60, mean confidence 60) -->
1?
2?
3?
4?Q
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 75 at 427,414-801,547 pt | caption: none | text-layer labels: none | nearby labels: consists of: | OCR text follows (tesseract, unverified; 3/10 words >= 60, mean confidence 35) -->
2? (i
3°
<!-- end of figure 3 -->

<!-- pdf page 76 | printed page 76 | header: 1. -->

1.   1 x Power cable 2 m (6.6 ft) (part number: A06049). Used to provide
     12 V dc power to the SeaTalk NG backbone.
2. 1 x Spur cable 1 m (3.3 ft) (part number: A06039). Used to connect a
   device to the SeaTalk NG backbone.
3.   1 x NMEA 0183 VHF stripped-end (2-wire) to SeaTalk NG adapter cable 1 m
     (3.3 ft) (part number: A06071). Used to connect an NMEA 0183 VHF radio
     to the SeaTalk NG backbone via the NMEA 0183 to SeaTalk NG converter.
4.   1 x SeaTalk 1 to SeaTalk NG converter (part number: E22158). Each
     converter allows connection of one SeaTalk 1 device and up to 2 SeaTalk
     NG devices.
5. 2 x Spur blanking plugs (part number: A06032). Used to cover unused
   spur connections in 5-way blocks, T-piece connectors, and the SeaTalk 1
   to SeaTalk NG converter.
6. 2 x Backbone terminators (part number: A06031). Terminators must be
   fitted to both ends of the SeaTalk NG backbone.
SeaTalk NG spur cables
SeaTalk NG spur cables are required to connect devices to the SeaTalk NG
backbone.

1.   SeaTalk NG spur cables:
     • Spur cable 0.4 m (1.3 ft) (part number: A06038).
     • Spur cable 1 m (3.3 ft) (part number: A06039).
     • Spur cable 3 m (9.8 ft) (part number: A06040).
     • Spur cable 5 m (16.4 ft) (part number: A06041).

2. Elbow (right-angled) to elbow (right-angled) spur cable 0.4 m (1.3 ft) (part
   number: A06042). Used in confined spaces where a straight spur cable
   will not fit.
3.   Elbow (right-angled) to straight spur cable 1 m (3.3 ft) (part number:
     A06081). Used in confined spaces where a straight spur cable will not fit.
4.   SeaTalk NG to stripped-end spur cables (connects compatible products
     that do not have a SeaTalk NG connector, such as transducer pods):
     • SeaTalk NG to stripped-end spur cable 1 m (3.3 ft) (part number:
       A06043)
     • SeaTalk NG to stripped-end spur cable 3 m (9.8 ft) (part number:
       A06044)
5. ACU-Series / SPX-Series autopilot to SeaTalk NG spur cable 0.3 m (1.0 ft)
   (part number R12112). Connects the course computer to the SeaTalk NG
   backbone. This connection can also be used to provide 12 V dc power to
   the SeaTalk NG backbone.
SeaTalk NG backbone cables
SeaTalk NG backbone cables are used to create or extend a SeaTalk NG
backbone.

1.   Backbone cables:
     • Backbone cable 0.4 m (1.3 ft) (part number: A06033).
     • Backbone cable 1 m (3.3 ft) (part number: A06034).
     • Backbone cable 3 m (9.8 ft) (part number: A06035).
     • Backbone cable 5 m (16.4 ft) (part number: A06036).
     • Backbone cable 9 m (29.5 ft) (part number: A06068).
     • Backbone cable 20 m (65.6 ft) (part number: A06037).
2. SeaTalk NG to DeviceNet (female) Backbone cable 0.4 m (1.3 ft) (part
   number: A80675)

<!-- figure 1 on pdf page 76 at 38,294-413,459 pt | caption: none | text-layer labels: none | nearby labels: SeaTalk NG spur cables | backbone. | 1. | 1. | SeaTalk NG spur cables: | OCR text follows (tesseract, unverified; 1/8 words >= 60, mean confidence 48) -->
1?
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 76 at 427,299-801,392 pt | caption: none | text-layer labels: none | nearby labels: SeaTalk NG backbone cables | backbone. | 1. | Backbone cables: | OCR: no legible text (0/4 words >= 60, mean confidence 21) -->

<!-- pdf page 77 | printed page 77 | header: 3. | footer: Spares and accessories -->

3.   SeaTalk NG to DeviceNet (male) Backbone cable 0.4 m (1.3 ft) (part
     number: A80674)
SeaTalk NG power cables
SeaTalk NG power cables are used to provide the SeaTalk NG backbone
with a single 12 V dc power source. The power connection must include
a 5 amp inline fuse (not supplied).

1.   Power cable (straight) 2 m (6.6 ft) (part number: A06049).
2. Elbow (right-angled) power cable 2 m (6.6 ft) (part number: A06070).
SeaTalk NG connectors
SeaTalk NG connectors are used to connect SeaTalk NG devices to the
SeaTalk NG backbone and to create and extend the backbone.

1.   5-Way connector (part number: A06064). Each connector block allows
     connection of up to 3 SeaTalk NG devices. Multiple connector blocks
     can be ‘daisy chained’ together.
2. T-piece (part number: A06028). Each T-piece allows connection of one
   SeaTalk NG device. Multiple T-pieces can be ‘daisy chained’ together.
3.   Backbone extender (part number: A06030). Used to connect 2
     backbone cables together.
4.   Inline terminator (part number: A80001). Used to connect a spur cable
     and SeaTalk NG device at the end of a backbone instead of a backbone
     terminator.

5. Backbone terminator (part number: A06031). Terminators must be fitted
   to both ends of the SeaTalk NG backbone.
6. Spur blanking plug (part number: A06032). Used to cover unused spur
   connections in 5-Way blocks, T-piece connectors, or the SeaTalk 1 to
   SeaTalk NG converter.
7.   Elbow (right-angled) spur connector (part number: A06077). Used in
     confined spaces where a straight spur cable will not fit.
SeaTalk NG adaptors and adaptor cables
SeaTalk NG adaptor cables are used to connect devices designed for
different CAN Bus backbones (e.g.: SeaTalk 1 or DeviceNet) to the SeaTalk
NG backbone.

1.   SeaTalk 1 (3 pin) to SeaTalk NG converter cable 1 m (3.3 ft) (part number:
     A22164 / A06073). Can be used to connect a SeaTalk 1 device to a
     SeaTalk NG backbone via the SeaTalk 1 to SeaTalk NG converter, or to
     connect a SeaTalk NG product directly to a SeaTalk 1 network.
2. SeaTalk 1 (3 pin) to SeaTalk NG adaptor cable 0.4 m (1.3 ft) (part number:
   A06047). Can be used to connect a SeaTalk 1 device to a SeaTalk NG
   backbone via the SeaTalk 1 to SeaTalk NG converter, or to connect a
   SeaTalk NG product directly to a SeaTalk 1 network.
3.   SeaTalk 2 (5 pin) to SeaTalk NG adaptor cable 0.4 m (1.3 ft) (part number:
     A06048). Used to connect SeaTalk 2 devices or networks to a SeaTalk
     NG backbone.

<!-- figure 1 on pdf page 77 at 38,127-413,215 pt | caption: none | text-layer labels: none | nearby labels: 7. | 1. | OCR: no legible text (0/4 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 77 at 427,198-801,394 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 5/21 words >= 60, mean confidence 41) -->
1?
10”
11”
5>
6°?
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 77 at 38,296-413,404 pt | caption: none | text-layer labels: none | nearby labels: SeaTalk NG connectors | 1. | 1. | OCR: no legible text (0/4 words >= 60, mean confidence 27) -->

<!-- pdf page 78 | printed page 78 | header: 4. -->

4.   SeaTalk NG to DeviceNet (female) adaptor cables connect NMEA 2000
     devices that use a DeviceNet connector to the SeaTalk NG backbone, or
     connects SeaTalk NG devices to an NMEA 2000 network. The following
     cables are available:
     • SeaTalk NG to DeviceNet (female) adaptor cable 0.4 m (1.3 ft) (part
       number: A06045).
     • SeaTalk NG to DeviceNet (female) adaptor cable 1 m (3.3 ft) (part
       number: A06075).
5. SeaTalk NG to DeviceNet (male) adaptor cables. Connect NMEA 2000
   devices that use a DeviceNet connector to the SeaTalk NG backbone, or
   connect SeaTalk NG devices to an NMEA 2000 network. The following
   cables are available:
     • SeaTalk NG to DeviceNet (male) adaptor cable 0.1 m (0.33 ft) (part
       number: A06078).
     • SeaTalk NG to DeviceNet (male) adaptor cable 0.4 m (1.3 ft) (part
       number: A06074).
     • SeaTalk NG to DeviceNet (male) adaptor cable 1 m (3.3 ft) (part number:
       A06076).
     • SeaTalk NG to DeviceNet (male) adaptor cable 1.5 m (4.92 ft) (part
       number: A06046).
6. NMEA 0183 stripped-end (2-wire) to SeaTalk NG adapter cable 1 m (3.3 ft)
   (part number: A06071). Used to connect an NMEA 0183 VHF radio to the
   SeaTalk NG backbone via the NMEA 0183 to SeaTalk NG converter.
7.   SeaTalk NG (male) to DeviceNet (female) adaptor (A06082*).
8. SeaTalk NG (female) to DeviceNet (male) adaptor (A06083*).
9.   SeaTalk NG (male) to DeviceNet (female) elbow (right-angled) adaptor
     (A06084*).
10. DeviceNet (female) to stripped-end adaptor cable (0.4 m (1.3 ft)) (part
    number: E05026).
11. DeviceNet (male) to stripped-end adaptor cable (0.4 m (1.3 ft)) (part
    number: E05027).

 Important:
 * Do NOT connect the A06082, A06083, or A06084 adaptors directly to a
 backbone. Only connect as part of a spur connection between backbone
 and device.

<!-- pdf page 79 | printed page 79 -->

Appendix A NMEA 2000 PGN support
Supported standard NMEA 2000 PGNs are listed below. Raymarine and other
proprietary PGNs are not listed.

Administration PGNs
 PGN           Description                             Transmit   Receive
 59392         ISO Acknowledge                         ●
 59904         ISO Request                                        ●
 60160         ISO Transport Protocol, Data Transfer              ●
 60416         ISO Transport Protocol, Connection      ●          ●
               Management — BAM Group Function
 60928         ISO Address Claim                       ●          ●
 65240         ISO Commanded Address                              ●
 126208        NMEA — Request Group Function                      ●
 126208        NMEA — Command Group Function                      ●
 126208        NMEA — Acknowledge Group Function       ●
 126464        PGN Transmit and Receive List           ●          ●

Data PGNs
 PGN           Description                             Transmit   Receive
 126992        System Time                             ●
 126993        Heartbeat                               ●
 126996        Product Information                     ●
 126998        Configuration Information               ●
 127250        Vessel Heading                          ●
 127251        Rate Of Turn                            ●
 127257        Attitude                                ●
 129025        Position, Rapid Update                  ●
 129026        COG & SOG Rapid Update                  ●
 129029        GNSS Position Data                      ●
NMEA 2000 PGN support

PGN      Description                          Transmit   Receive
129033   Time and Date                        ●
129044   Datum                                ●          ●
129539   GNSS DOPs                            ●
129540   GNSS Satellites In View              ●
129542   GNSS Pseudo Range Noise Statistics   ●
129547   GNSS Pseudo Range Error Statistics   ●

                                                                   79

<!-- pdf page 80 | printed page 80 -->

Appendix B AR200 Software release history
The list below is a cumulative list of the new features introduced in
subsequent releases of the AR200 software, since the initial release (v1.28;
October 2019).
This list includes new features only. It does NOT include software
maintenance items, such as bug fixes or performance improvements.
To download the software, and view the complete list of all software updates,
including new features, bug fixes, and performance improvements, visit:
 AR200 software download link
 https://bit.ly/ar200-download

AR200 v1.33 new features:
(Software release date: February 2024)
• Added support for a new LED indicator ‘Switch off’ setting which can
  be toggled via a networked LightHouse 4 multifunction display (running
  software version v4.6.74 or later). For more information, refer to:
  p.60 — Switching off sensor LEDs
• Added support for a new LED indicator ‘Find me’ setting which can be
  toggled via a networked LightHouse 4 multifunction display (running
  software version v4.6.74 or later). For more information, refer to:
  p.60 — Find me

AR200 v1.32 new features:
(Software release date: December 2022)
• Software update to support internal component changes.

AR200 v1.31 new features:
(Software release date: August 2020)
• Increased resolution of the position data when the AR200 is being used
  at higher Latitudes.

AR200 v1.28 new features:
(Software release date: October 2019)
• Initial release.

<!-- pdf page 81 | printed page 81 -->

Appendix C Document change history
 Document revision and (Date)   Changes
 87372 Rev 3                    • Added software details chapter.
 (08–2024)                      • Updated to include details and
 Software version: v1.33          requirements for Axiom 2-Series
                                  displays.
                                • Updated system example.
                                • Added compatible cartography to
                                  recommended components list.
                                • Added additional product
                                  dimensions for Mounting tray,
                                  Bulkhead bracket and Riser.
                                • Added mounting options section.
                                • Added pole mounting details.
                                • Updated connections overview.
                                • Added NMEA 2000 connection
                                  chapter.
                                • Updated Setup and calibration
                                  and System checks and
                                  troubleshooting chapters to
                                  bring inline with the latest
                                  LightHouse 4 version.
                                • Updated LED diagnostics to
                                  include required user actions.
                                • Added details for switching the
                                  LED off and the Find me feature.
                                • Added images of accessories.
                                • Removed “Position delta high
                                  precision (PGN 129027)” from
                                  supported PGN list.
                                • Added software and document
                                  release history to appendix.

Document change history

Document revision and (Date)   Changes
                               • Updated to bring inline with latest
                                 styling standards.
87372 Rev 2                    • Expanded Product overview.
(12–2021)                      • Updated required additional
Software version: v1.31          component details.
                               • Updated document structure to
                                 latest standards.
                               • Added procedure for mounting
                                 using the Riser.
                               • Added new Setup and calibration
                                 details.
87372 Rev 1                    • Initial release.
(10–2018)
Software version: v1.28

                                                                   81

<!-- pdf page 82 -->

(no text layer on this page)

<!-- pdf page 83 -->

Index
A
Accessories ............................................................................................. 74
  SeaTalk NG adaptor cables ................................................................. 77
  SeaTalk NG backbone cables ............................................................. 76
  SeaTalk NG cables .............................................................................. 74
  SeaTalk NG connectors ....................................................................... 77
  SeaTalk NG kits ................................................................................... 74
  SeaTalk NG Power cables ................................................................... 77
  SeaTalk NG spur cables ...................................................................... 76
Applicable documents..............................................................................12
Applicable products .................................................................................12
AR200 ..................................................................................................... 54
  Calibration............................................................................................ 54
Augmented Reality
  Camera direction ..................................................................................51
  Camera height ......................................................................................51
  Camera installation and setup ..............................................................51
  Compass lock ...................................................................................... 55
  Compass offset .................................................................................... 55
  Current reading.................................................................................... 55
  Deviation.............................................................................................. 55
  Field of View .........................................................................................51
  Initial test.............................................................................................. 58
  Reset calibration .................................................................................. 55
  Troubleshooting .................................................................................. 62
Automatic linearization ............................................................................ 55

B
Backbone length,
  SeaTalk NG.......................................................................................... 43
Box contents, See Parts supplied

C
Cable
  Bend radius.......................................................................................... 38
  Protection ............................................................................................ 38
  Routing ................................................................................................ 38

  Security ................................................................................................ 38
  Strain relief........................................................................................... 38
Calibration ............................................................................................... 54
  Linearization ........................................................................................ 54
CAN bus ...................................................................................................16
Cleaning .............................................................................................. 9, 66
ClearCruise
  Augmented Reality .............................................................................. 52
Compass
  Linearization ................................................................................. 54–55
Compass lock .......................................................................................... 55
Compass safe distance ........................................................................... 26
Compliance specification ........................................................................ 72
Conformance specification...................................................................... 72
Connections
  Battery ................................................................................................. 45
  DeviceNet ............................................................................................ 38
  Distribution panel................................................................................. 45
  Overview.............................................................................................. 38
  Power.......................................................................................42–43, 46
  Power connections
     Power distribution ............................................................................ 44
  SeaTalk 1.............................................................................................. 38
  SeaTalk NG....................................................................................38–39
Contact details......................................................................................... 68

D
Diagnostics.............................................................................................. 69
Distribution panel connection ................................................................. 45
Documentation .........................................................................................12
  Operation instructions ......................................................................... 69

E
Electromagnetic Compatibility................................................................. 26
EMC, See Electromagnetic Compatibility
Environmental specification ..................................................................... 71

G
GNSS (GPS) ............................................................................................. 59

<!-- pdf page 84 -->

GNSS (GPS), Specification ........................................................................ 71
GPS.......................................................................................................... 59

I
Installation ............................................................................................... 35
   Bracket mounting ................................................................................ 30
   Bulkhead mounting.............................................................................. 30
   Checklist .............................................................................................. 29
   Mounting options................................................................................. 30
   Schematic diagram .............................................................................. 29
   Surface mounting................................................................................. 32
   Surface mounting (Riser)...................................................................... 33
Installation tools....................................................................................... 29
Interference ............................................................................................. 26
     See also Compass safe distance
   RF......................................................................................................... 26
IP address................................................................................................ 69

L
LED Diagnostics ...................................................................................... 59
LED indications........................................................................................ 59
LEN (Load Equivalency Rating) ................................................................. 71
Linearization ..................................................................................... 54–55
Load equivalency number ....................................................................... 43
Location requirements ............................................................................ 25

M
Magnetic deviation .................................................................................. 54
Magnetic interference ............................................................................. 54
Maintenance........................................................................................ 9, 66
Mounting, See Installation
Mounting location.................................................................................... 25
Mounting templates..................................................................................12
Mounting tray
 Release ................................................................................................ 35

N
Network length,

  SeaTalk NG.......................................................................................... 43
New features ......................................................................................14, 80
NMEA 2000
  LEN ................................................................................................ 39, 43

O
Operation instructions ............................................................................. 69

P
Pack contents, See Parts supplied
Parts supplied..........................................................................................20
Pole mount
  Alignment adjustment.......................................................................... 36
Pole mounting ......................................................................................... 35
Position.................................................................................................... 59
Position sensor
  Find me .................................................................................................61
  Find Me .................................................................................................61
Position sensor LED
  Find Me ................................................................................................60
  Go dark ................................................................................................60
  LEDs off ...............................................................................................60
Power
  Battery connection............................................................................... 45
  Distribution panel................................................................................. 45
  Sharing a breaker ................................................................................ 45
Power cable extension ............................................................................ 46
Power connection point .......................................................................... 43
Power specification .................................................................................. 71
Product dimensions, See Dimensions
Product documentation ............................................................................12
Product information ................................................................................. 69
Product loading ................................................................................. 39, 43
Product overview......................................................................................16
Product recycling (WEEE) .........................................................................10
Product support....................................................................................... 68
Protocols
  SeaTalk NG...........................................................................................16

<!-- pdf page 85 -->

R
Radio Frequency (RF) interference.......................................................... 26
Rail mounting........................................................................................... 35
Recommended components .................................................................... 18
Required components .............................................................................. 17
Routine checks ........................................................................................ 66

S
SeaTalk NG .................................................................................. 16, 39, 44
  Adaptor cables .................................................................................... 77
  Backbone cables ................................................................................. 76
  Connectors .......................................................................................... 77
  Kits ....................................................................................................... 74
  LEN ................................................................................................ 39, 43
  Load equivalency number ............................................................. 39, 43
  Power.......................................................................................42–43, 46
  Power cables ................................................................................. 42, 77
  Spur cables .......................................................................................... 76
  System loading .................................................................................... 44
SeaTalk NG cables .................................................................................. 74
Service Center......................................................................................... 68
Servicing.............................................................................................. 9, 66
Software updates ..................................................................................... 14
Software version....................................................................................... 14
Specification, GNSS (GPS) ........................................................................ 71
Support forum ......................................................................................... 69
Suppression ferrites ............................................................................ 9, 27
     See also EMC
System example (typical system)........................................................ 17, 39

T
Technical specification ............................................................................ 70
  AHRS .................................................................................................... 71
  Conformance ....................................................................................... 72
  Environmental ....................................................................................... 71
  GNSS receiver ...................................................................................... 71
  Power.................................................................................................... 71
Technical support............................................................................. 68–69
Tools required ......................................................................................... 29

Training courses ...................................................................................... 69
Troubleshooting ...................................................................................... 59
  Augmented Reality .............................................................................. 62
  GNSS ....................................................................................................61
  GNSS (GPS)...........................................................................................61
  GPS .......................................................................................................61
  LED indications .................................................................................... 59

U
Upgrading, software ................................................................................. 14

W
Warranty .............................................................................................10, 68
WEEE Directive.........................................................................................10

<!-- pdf page 86 -->

(no text layer on this page)

<!-- pdf page 87 -->

(no text layer on this page)

<!-- pdf page 88 -->

     Raymarine (UK / EU)
Marine House, Cartwright Drive,
     Fareham, Hampshire.
          PO15 5RJ.
       United Kingdom.

   Tel: (+44) (0)1329 246 700

    www.raymarine.co.uk

       Raymarine (US)
       110 Lowell Road,
     Hudson, NH 03051.
   United States of America.

    Tel: (+1) 603-324-7900

     www.raymarine.com

<!-- figure 1 on pdf page 88 at 329,45-511,110 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
