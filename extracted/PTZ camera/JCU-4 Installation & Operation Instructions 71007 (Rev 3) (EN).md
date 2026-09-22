<!-- pdf page 1 -->

                                                 JCU-4 Installation and Operation Instructions

                                        FLIR JCU-4

                                           JCU-4
              Installation & Operation Instructions
Document number: 71007 (Rev 3) | English (en-US) | Date: 03-2026 | Applicable software version: v2.0.12

<!-- figure 1 on pdf page 1 at 214,34-432,302 pt | caption: none; nearest centred text below: "JCU-4 Installation and Operation Instructions" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/8 words >= 60, mean confidence 64) -->
p
BOW CAMERA
v
fy
<!-- end of figure 1 -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

Legal notices (FLIR)

Trademark and patents notice
FLIR, Instalert, Infrared Everywhere, The World’s Sixth Sense and ClearCruise are registered or claimed trademarks of Teledyne
FLIR LLC.
All other trademarks, trade names, or company names referenced herein are used for identification only and are the property of their
respective owners.
This product is protected by patents, design patents, patents pending, or design patents pending.

Fair Use Statement
You may print no more than three copies of this manual for your own use. You may not make any further copies or distribute or use the
manual in any other way including without limitation exploiting the manual commercially or giving or selling copies to third parties.

Content notice
Please ensure that you have obtained this document only from FLIR, and that it is the latest available version.
There are numerous third-party Internet websites (such as www.manualslib.com) hosting FLIR product manuals. These websites are not
authorized by FLIR to do so, and are often hosting illegitimate or older versions of FLIR product manuals, which may contain inaccurate or
misleading information.
To obtain the latest official documentation for a FLIR product, please visit the official FLIR website: www.marine.flir.com

Artificial Intelligence (AI) content notice
There are numerous third-party Artificial Intelligence (AI) services available to the public, which are capable of providing a summary or
transcription of the information provided by official FLIR publications or websites, either in written or audio/video formats. These services
may alter, supplement, or convey the original information provided by FLIR in inaccurate or misleading ways.
Please ensure that you have obtained this document only from FLIR, and that it is the latest available version.

English (en-US)
Document number: 71007 (Rev 3)
AC;80041;2026-03-02T16:02:48

<!-- pdf page 4 -->

(no text layer on this page)

<!-- pdf page 5 | printed page 5 -->

CONTENTS
CHAPTER 1 IMPORTANT INFORMATION ................. 10
   Safety warnings .................................................. 10
   Product warnings ................................................ 10
   Regulatory notices .............................................. 11
          Water ingress ................................................ 11
          Disclaimer ..................................................... 11
          EMC installation guidelines...........................12
          Suppression ferrites ......................................12
          Connections to other equipment...................12
          Declaration of Conformity .............................12
          PSTI Compliance ...........................................13
          Product disposal ...........................................13
          Warranty policy and registration ...................13
          IMO and SOLAS ............................................13
          Technical accuracy ........................................13
          Publication copyright ....................................13

CHAPTER 2 DOCUMENT INFORMATION ................. 14
   2.1 Applicable products .......................................15
   2.2 Product documentation..................................15
          Printed (hardcopy) product manuals .............15
     2.3 Document illustrations ...................................15
     2.4 Applicable software version ...........................16

CHAPTER 3 SOFTWARE RELEASE
SUMMARY............................................................... 17
   3.1 Introduction ...................................................18
   3.2 JCU-4 v2.0.12 Release Notes (December
   2025) ...................................................................18

CHAPTER 4 PRODUCT AND SYSTEM
OVERVIEW ............................................................... 20
   4.1 Product overview ...........................................21
   4.2 Required additional components ...................21
   4.3 Compatible FLIR maritime cameras ...............22
   4.4 System overview (example only) ...................22

CHAPTER 5 PARTS SUPPLIED .................................. 24
   5.1 Parts supplied ................................................25
   5.2 Parts supplied (Joystick only) .........................25
   5.3 Inline fuse requirement ..................................25

CHAPTER 6 PRODUCT DIMENSIONS....................... 27
   6.1 Product dimensions .......................................28

CHAPTER 7 LOCATION REQUIREMENTS ................. 29
   7.1 Warnings and cautions ...................................30
   7.2 General location requirements .......................30
   7.3 Location requirements....................................30
   7.4 EMC installation guidelines ............................30
   7.5 Suppression ferrites .......................................31
   7.6 Connections to other equipment ....................31
   7.7 Compass safe distance ...................................31

CHAPTER 8 MOUNTING .......................................... 32
   8.1 Tools required ................................................33
   8.2 Mounting options ..........................................33
   8.3 Removing the front cover ..............................33
   8.4 Retrofit mounting the unit ..............................34
   8.5 Surface mounting the unit .............................34
   8.6 Fitting the front cover.....................................35

<!-- pdf page 6 | printed page 6 -->

CHAPTER 9 CABLES AND CONNECTIONS —
GENERAL INFORMATION ........................................ 36
   9.1 General cabling guidance ..............................37
         Cable types and length .................................37
         Cable routing and bend radius ......................37
         Strain relief ...................................................37
         Circuit isolation .............................................37
         Cable shielding .............................................38
         Bare-ended wire connections........................38
         Connecting cables .........................................38

CHAPTER 10 NETWORK CONNECTIONS ................. 39
   10.1 Power options ..............................................40
         Multiple power sources ................................40
    10.2 Connections overview ..................................40
    10.3 System overview (example only) .................41
         Network cable extensions .............................41

CHAPTER 11 POE POWER CONNECTIONS............... 42
   11.1 Power options ...............................................43
         Multiple power sources ................................43
    11.2 Power over Ethernet (PoE) ............................43
    11.3 PSE (Power Sourcing Equipment) power
    connection ..........................................................43
         PoE network switch power
         connection ....................................................43
         PoE injector power connection .....................44
    11.4 Network cable extensions .............................44

CHAPTER 12 NON-POE POWER
CONNECTIONS ........................................................ 45
   12.1 Power options ..............................................46

          Multiple power sources ................................46
     12.2 Direct power connection ..............................46
     12.3 Inline fuse requirement ................................46
     12.4 Inline fuse and thermal breaker
     ratings.................................................................47
     12.5 Power distribution ........................................47
     12.6 Power cable extension (12 / 24 V
     systems) .............................................................49
     12.7 Power cable drain wire connection...............50

CHAPTER 13 OPERATION (M460-SERIES /
M560-SERIES) .......................................................... 51
   13.1 Controls overview ........................................52
   13.2 Powering on the unit ....................................53
   13.3 Startup wizard ..............................................53
         System selection ...........................................53
         Assigning a static IP address ........................54
         Assigning a netmask .....................................54
     13.4 Camera detection .........................................55
     13.5 Controlled camera ........................................55
          Status icons ..................................................55
     13.6 Main menu ...................................................56
         Select camera ...............................................56
         Power down ..................................................56
         Brightness .....................................................57
         Camera focus ................................................57
     13.7 JCU settings .................................................58
          Shortcut keys ................................................58
          Joystick mode ...............................................61
          Controllable cameras ....................................61
          Installation ....................................................62

<!-- pdf page 7 | printed page 7 -->

          About this device ..........................................62
          Settings reset ................................................62
          Factory reset .................................................63

CHAPTER 14 OPERATION (M400-SERIES /
M500-SERIES).......................................................... 64
   14.1 Controls overview ........................................65
   14.2 Powering on the unit ....................................66
   14.3 Startup wizard ..............................................66
         System selection ...........................................66
         Assigning a static IP address ........................67
         Assigning a netmask .....................................67
     14.4 Camera detection .........................................68
     14.5 Controlled camera ........................................68
          Status icons ..................................................68
     14.6 Main menu ...................................................69
         Select camera ...............................................69
         Power down ..................................................70
         Brightness .....................................................70
         Camera focus ................................................71
     14.7 JCU settings .................................................71
         Shortcut keys ................................................72
         Joystick mode ...............................................72
         Controllable cameras ....................................72
         Installation ....................................................72
         About this device ..........................................73
         Settings reset ................................................73
         Factory reset ................................................. 74
     14.8 Ready to track ............................................... 74
     14.9 Spotlight on ................................................. 74
     14.10 User programmable buttons (UPBs) ...........75

         Programming UPBs via the Web
         interface ........................................................75
         Programming UPBs via the On-Screen
         Display (OSD) menu .....................................75

CHAPTER 15 OPERATION (M300-SERIES)................ 77
   15.1 Controls overview ........................................78
   15.2 Powering on the unit ....................................79
   15.3 Startup wizard ..............................................79
        System selection ...........................................79
        Assigning a static IP address ........................80
        Assigning a netmask .....................................80
    15.4 Camera detection .........................................81
    15.5 Controlled camera ........................................81
         Status icons ..................................................81
    15.6 Main menu ...................................................82
        Select camera ...............................................82
        Power down ..................................................82
        Brightness .....................................................83
        Camera focus ................................................83
    15.7 JCU settings .................................................83
        Shortcut keys ................................................84
        Joystick mode ...............................................84
        Controllable cameras ....................................85
        Installation ....................................................85
        About this device ..........................................85
        Settings reset ................................................86
        Factory reset .................................................86
    15.8 User programmable buttons (UPBs) ............87

<!-- pdf page 8 | printed page 8 -->

          Programming UPBs via the Web
          interface ........................................................87
          Programming UPBs via the On-Screen
          Display (OSD) menu .....................................87

CHAPTER 16 OPERATION (M100-SERIES /
M200-SERIES).......................................................... 88
   16.1 Controls overview ........................................89
   16.2 Powering on the unit ....................................90
   16.3 Startup wizard ..............................................91
         System selection ...........................................91
         Assigning a static IP address ........................91
         Assigning a netmask .....................................92
     16.4 Camera detection .........................................92
     16.5 Controlled camera ........................................92
     16.6 Main menu ...................................................92
         Select camera ...............................................93
         Power down ..................................................93
         Brightness .....................................................94
         Camera focus ................................................94
     16.7 JCU settings .................................................94
         Shortcut keys ................................................95
         Joystick mode ...............................................95
         Controllable cameras ....................................95
         Installation ....................................................96
         About this device ..........................................96
         Settings reset ................................................96
         Factory reset .................................................97
     16.8 User programmable buttons (UPBs) ............97

          Programming UPBs via the Web
          interface ........................................................97

CHAPTER 17 OPERATION (MD-SERIES) ................... 99
   17.1 Controls overview ....................................... 100
   17.2 Powering on the unit................................... 101
   17.3 Startup wizard............................................. 101
          System selection ......................................... 101
          Assigning a static IP address ...................... 102
          Assigning a netmask ................................... 102
     17.4 Camera detection ........................................ 103
     17.5 Controlled camera ...................................... 103
     17.6 Main menu ................................................. 103
          Select camera ............................................. 104
          Power down ................................................ 104
          Brightness ................................................... 104
          Camera focus .............................................. 105
     17.7 JCU settings................................................ 105
          Shortcut keys .............................................. 106
          Joystick mode ............................................. 106
          Controllable cameras .................................. 106
          Installation .................................................. 107
          About this device ........................................ 107
          Settings reset .............................................. 107
          Factory reset ............................................... 108
     17.8 User programmable buttons (UPBs) ........... 108
          Programming UPBs via the On-Screen
          Display (OSD) menu ................................... 108

CHAPTER 18 CONFIGURATION VIA WEB
INTERFACE ............................................................. 110

<!-- pdf page 9 | printed page 9 -->

     18.1 Web browser user interface
     overview ............................................................ 111
     18.2 Logging in to the Web browser user
     interface ............................................................. 111
         IP address discovery ................................... 112
     18.3 Web browser user interface........................ 112
          Product information page ........................... 112
          Setup page.................................................. 113
          Diagnostics page ........................................ 116

CHAPTER 19 MAINTENANCE .................................. 117
   19.1 Service and maintenance ........................... 118
   19.2 Routine equipment checks .......................... 118
   19.3 Cleaning the unit ........................................ 118

CHAPTER 20 SYSTEM CHECKS AND
TROUBLESHOOTING .............................................. 119
   20.1 Troubleshooting ......................................... 120
   20.2 PoE power connection
   troubleshooting ................................................ 120
   20.3 Non-PoE power connection
   troubleshooting ................................................ 121
   20.4 System data troubleshooting ..................... 122
   20.5 Miscellaneous troubleshooting .................. 122

CHAPTER 21 SUPPORT AND SERVICING............... 123
   21.1 FLIR Maritime technical support and
   servicing ........................................................... 124

CHAPTER 22 TECHNICAL SPECIFICATION ............. 125
   22.1 Physical specification ................................. 126
   22.2 Power specification .................................... 126
   22.3 Network specification ................................. 126
   22.4 Display specification .................................. 126

     22.5 Environmental specification ....................... 126
     22.6 Conformance specification ......................... 126

CHAPTER 23 SPARES AND ACCESSORIES ............ 127
   23.1 Spares and accessories .............................. 128
   23.2 FLIR networking accessories ...................... 129
   23.3 RayNet to RayNet cables and
   connectors ........................................................ 131
   23.4 RayNet to RJ45, and RJ45 (SeaTalk HS)
   adapter cables................................................... 133

APPENDIX A SOFTWARE RELEASE
HISTORY ................................................................ 135

<!-- pdf page 10 | printed page 10 -->

CHAPTER 1: IMPORTANT
INFORMATION

Safety warnings
      Warning: Product installation and
      operation
      • This product must be installed and operated in
      accordance with the instructions provided. Failure to
      do so could result in personal injury, damage to your
      vessel and/or poor product performance.
      • Certified installation by an approved installer is
      recommended. A certified installation qualifies for
      enhanced product warranty benefits. Contact your
      dealer for further details.

      Warning: Potential ignition source
      This product is NOT approved for use in
      hazardous/flammable atmospheres. Do NOT install
      in a hazardous/flammable atmosphere (such as in an
      engine room or near fuel tanks).

      Warning: Switch off power supply
      Ensure that the vessel’s power supply is switched OFF
      before starting to install this product. Do NOT connect
      or disconnect equipment with the power switched on,
      unless instructed to do so in this document.

      Warning: High voltage
      This product contains high voltage. Do NOT remove
      covers or attempt to access internal components,
      unless specifically instructed in the documentation
      provided.

      Warning: Ensure safe navigation
      This product is intended only as an aid to navigation
      and must never be used in preference to sound
      navigational judgment. Only official government
      charts and notices to mariners contain all the current
      information needed for safe navigation, and the
      captain is responsible for their prudent use. It is the
      user’s responsibility to use official government charts,
      notices to mariners, caution and proper navigational
      skill when operating this or any other product.

      Warning: Maintain a permanent watch
      Always maintain a permanent watch, this will allow
      you to respond to situations as they develop. Failure
      to maintain a permanent watch puts yourself, your
      vessel and others at serious risk of harm.

Product warnings
      Warning: Product grounding
      Before applying power to this product, it MUST
      be correctly grounded, in accordance with the
      instructions provided.

      Warning: Positive ground systems
      Do NOT connect this unit to a system which has
      positive grounding.

      Warning: Power supply voltage
      Connecting this product to a voltage supply greater
      than the specified maximum rating may cause
      permanent damage to the unit. For the correct
      voltage, refer to the information label affixed to the
      product.

<!-- figure 1 on pdf page 10 at 334,29-379,146 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 10 at 166,101-314,230 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 10 at 41,103-86,230 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 10 at 334,154-379,226 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 10 at 41,238-86,310 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 6 on pdf page 10 at 547,266-607,329 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 10 at 334,269-379,329 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 66) -->
a
<!-- end of figure 7 -->
<!-- figure 8 on pdf page 10 at 41,314-314,389 pt | caption: none; nearest centred text below: "Warning: High voltage" | text-layer labels: Warning: Switch off power supply | nearby labels: Warning: High voltage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 9 on pdf page 10 at 334,334-607,389 pt | caption: none; nearest centred text below: "Warning: Power supply voltage" | text-layer labels: Warning: Positive ground systems | nearby labels: Warning: Power supply voltage | OCR: no legible text (0/1 words >= 60, mean confidence 16) -->
<!-- figure 10 on pdf page 10 at 41,394-314,466 pt | caption: none | text-layer labels: Warning: High voltage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 11 on pdf page 10 at 334,394-379,475 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 12 on pdf page 10 at 562,394-607,475 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 11 | printed page 11 -->

                        Warning: Ensure all equipment has
                        isolated power supply
                        This product has an isolated power supply. To prevent
                        potential damage to equipment, it is recommended
                        that any external equipment connected to this product
                        also has an isolated power supply.

                        Caution: Power supply protection
                        When installing this product, ensure that the power
                        source is adequately protected by means of a
                        suitably-rated fuse or thermal circuit breaker.

                        Caution: Sun covers
                        • Sun covers are used to protect the display screen
                        against the damaging effects of ultraviolet (UV) light.
                        If your product is supplied with a sun cover always
                        ensure it is fitted when the product is not in use.
                        • To avoid potential loss of the sun cover, ensure that
                        the sun cover is removed when travelling at high
                        speed, whether in the water or when the vessel is
                        being towed.
                        • To avoid potential screen damage, ensure that the
                        rear surface of the sun cover and the display screen
                        are clean and free from debris before placing the sun
                        cover on the screen.

                        Caution: Do not open the unit
                        The unit is factory sealed to protect against
                        atmospheric humidity, suspended particulates and
                        other contaminates. It is important that you do not
                        open the unit or remove the casing for any reason.
                        Opening the unit will:
                        • compromise the seal with possible damage to the
                        unit, and
                        • void the manufacturer’s warranty.

Important information

            Caution: Service and maintenance
            This product contains no user serviceable
            components. Please refer all maintenance and repair
            to authorized FLIR dealers. Unauthorized repair may
            affect your warranty.

Regulatory notices
Water ingress
Water ingress disclaimer
Although the waterproof rating capacity of this product meets the
stated standard (refer to the product’s Technical Specification),
water intrusion and subsequent equipment failure may occur if
the product is not installed correctly or subjected to commercial
high-pressure washing. FLIR will not warrant products subjected to
high-pressure washing.

Disclaimer
FLIR does not warrant that this product is error-free or that it is
compatible with products manufactured by any person or entity
other than FLIR.
FLIR is not responsible for damages or injuries caused by your use
or inability to use the product, by the interaction of the product
with products manufactured by others, or by errors in information
utilized by the product supplied by third parties.
Third-party hardware, such as converters, adapters, routers,
switches, Access Points etc., provided by third parties, may be
made available directly to you by other companies or individuals
under separate terms and conditions, including separate fees and
charges. Teledyne FLIR LLC or its affiliates have not tested or
screened the third-party hardware.
FLIR has no control over, and is not responsible for:
• (a) the content and operation of such third-party hardware; or:
• (b) the privacy or other practices of such third-party hardware.
The fact that FLIR’s documentation may make reference to
such third-party hardware does not indicate any approval or
endorsement of any such third-party hardware. FLIR may reference
such third-party hardware only as a convenience.
                                                                      11

<!-- figure 1 on pdf page 11 at 41,29-86,110 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 11 at 334,29-379,96 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 11 at 41,118-86,180 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 11 at 41,353-86,470 pt | caption: none; nearest centred text below: "Important information" | text-layer labels: none | nearby labels: Important information | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 11 at 240,353-314,470 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 12 | printed page 12 | header: Note: -->

THIS INFORMATION IS MADE AVAILABLE BY FLIR ON THE
BASIS THAT YOU EXCLUDE TO THE FULLEST EXTENT
LAWFULLY PERMITTED ALL LIABILITY WHATSOEVER FOR
ANY LOSS OR DAMAGE HOWSOEVER ARISING OUT OF
THE USE OF THIS INFORMATION OR RELIANCE UPON THIS
INFORMATION.
FLIR does not exclude FLIR’s liability (if any) to you for personal
injury or death resulting from Teledyne FLIR LLC negligence, for
fraud or for any matter which it would be illegal to exclude or to
attempt to exclude.

EMC installation guidelines
FLIR equipment and accessories conform to the appropriate
Electromagnetic Compatibility (EMC) regulations, to minimize
electromagnetic interference between equipment and minimize the
effect such interference could have on the performance of your
system.
Correct installation is required to ensure that EMC performance is
not compromised.

 Note:
 In areas of extreme EMC interference, some slight interference may
 be noticed on the product. Where this occurs the product and the
 source of the interference should be separated by a greater distance.

For optimum EMC performance we recommend that wherever
possible:
• FLIR equipment and cables connected to it are:
  – At least 1 m (3.3 ft) from any equipment transmitting or cables
    carrying radio signals e.g. VHF radios, cables and antennas. In
    the case of SSB radios, the distance should be increased to 2
    m (6.6 ft).
  – More than 2 m (6.6 ft) from the path of a radar beam. A radar
    beam can normally be assumed to spread 20 degrees above
    and below the radiating element.
• The product is supplied from a separate battery from that used
  for engine start. This is important to prevent erratic behavior
  and data loss which can occur if the engine start does not have
  a separate battery.
• FLIR specified cables are used.
• Cables are not cut or extended, unless doing so is detailed in
  the installation manual.

 Note:
 Where constraints on the installation prevent any of the
 above recommendations, always ensure the maximum possible
 separation between different items of electrical equipment, to
 provide the best conditions for EMC performance throughout the
 installation.

Suppression ferrites
• Cables may be pre-fitted or supplied with suppression ferrites.
  These are important for correct EMC performance. If ferrites are
  supplied separately to the cables (i.e. not pre-fitted), you must fit
  the supplied ferrites, using the supplied instructions.
• If a ferrite has to be removed for any purpose (e.g. installation or
  maintenance), it must be replaced in the original position before
  the product is used.
• Use only ferrites of the correct type, supplied by the manufacturer
  or its authorized dealers.
• Where an installation requires multiple ferrites to be added to a
  cable, additional cable clips should be used to prevent stress on
  the connectors due to the extra weight of the cable.
• If your installation requires long cable runs, you may need to fit
  additional ferrites to maintain acceptable EMC performance.

Connections to other equipment
Requirement for ferrites on non-FLIR cables:
If your FLIR equipment is to be connected to other equipment using
a cable not supplied by FLIR, a suppression ferrite MUST always
be attached to the cable near the FLIR unit.
For more information, refer to your third-party cable manufacturer.

Declaration of Conformity
Raymarine UK Ltd (FLIR) declares that the products listed below are
in conformity with the relevant sections of the listed designated
standards and / or other normative documents:
• JCU-4 Joystick Control Unit (with cables), part number: E70695
• JCU-4 Joystick Control Unit (Joystick only), part number: E70697

<!-- pdf page 13 | printed page 13 -->

  Region            Standard                                          Mark

  UK                EMC Regulations 2016

  EU                EMC Directive 2014/30/EU

The original Declaration of Conformity certificate may be viewed
on the relevant product page at www.bit.ly/JCU-4-docs

PSTI Compliance
For products sold into the United Kingdom (UK), use the following
link to obtain the product’s Statement of Compliance with the
Product Security and Telecommunications Infrastructure (PSTI)
Regulations:
Visit the following web address and enter the product’s model
name or number (SKU) into the provided search field:
• www.bit.ly/rym-sec-com

Product disposal
Dispose of this product in accordance with the WEEE Directive.
The Waste Electrical and Electronic Equipment (WEEE) Directive
requires the recycling of waste electrical and electronic equipment
which contains materials, components and substances that may be
hazardous and present a risk to human health and the environment
when WEEE is not handled correctly.
                        Equipment marked with the crossed-out wheeled bin
                        symbol indicates that the equipment should not be
                        disposed of in unsorted household waste.
                        Local authorities in many regions have established
                        collection schemes under which residents can dispose
                        of waste electrical and electronic equipment at a
                        recycling center or other collection point.
                        For more information about suitable collection
                        points for waste electrical and electronic equipment
                        in your region, refer to the Raymarine website:
                        https://bit.ly/rym-recycling

Warranty policy and registration
Visit the Raymarine / FLIR Maritime website to read the latest
warranty policy, and register your product’s warranty online:
www.bit.ly/rym-warranty
Important information

It is important that you register your product to receive full warranty
benefits. Your product package includes a barcode label indicating
the serial number of the unit. This serial number is also provided
on a label affixed to the product itself. You will need this serial
number when registering your product online.

IMO and SOLAS
The equipment described within this document is intended for
use on leisure marine boats and workboats NOT covered by
International Maritime Organization (IMO) and Safety of Life at Sea
(SOLAS) Carriage Regulations.

Technical accuracy
To the best of our knowledge, the information in this document
was correct at the time it was produced. However, FLIR cannot
accept liability for any inaccuracies or omissions it may contain.
In addition, our policy of continuous product improvement may
change specifications without notice. As a result, FLIR cannot accept
liability for any differences between the product and this document.
Please check the FLIR website (www.flir.com/marine/support) to ensure
you have the most up-to-date version(s) of the documentation for
your product.

Publication copyright
Copyright © 2026 Teledyne FLIR LLC. All rights reserved.
No parts of this material may be copied, translated, or
transmitted (in any medium) without the prior written
permission of Teledyne FLIR LLC.

                                                                     13

<!-- figure 1 on pdf page 13 at 46,343-91,391 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 14 | printed page 14 -->

CHAPTER 2: DOCUMENT INFORMATION

CHAPTER CONTENTS

•   2.1 Applicable products — page 15
•   2.2 Product documentation — page 15
•   2.3 Document illustrations — page 15
•   2.4 Applicable software version — page 16

<!-- pdf page 15 | printed page 15 -->

2.1 Applicable products
This document is applicable to the following products:
• JCU-4, part number: E70695
• JCU-4 (Joystick only), part number: E70697

2.2 Product documentation
The following documentation is applicable to your product:

Applicable documents:
  Part number          Description

  71007                JCU-4 Installation and Operation Instructions (this
                       document)
  77011                JCU-4 Mounting Template

Related documents:
  Part number                 Description

  432–0010–00–10              MD-Series Camera Operation Instructions
  71001                       M100-Series / M200-Series Installation
                              and Operation Instructions
  71004                       M300-Series Thermal Camera Installation
                              and Operation Instructions
  432–0012–02–10              M400-Series Camera Operation
                              Instructions
  432–0012–01–10              M500-Series Camera Operation
                              Instructions
  71006                       M460-Series / M560-Series Installation
                              and Operation Instructions

Printed (hardcopy) product manuals
All applicable user documentation for your product is available
on our website to view or download free-of-charge. If you
would prefer a printed (hardcopy) product manual, a Print Shop

Document information

service is available, enabling you to purchase a high-quality,
professionally-printed manual for your product, delivered directly
to your door.
Printed manuals are ideal for keeping onboard your vessel, as
a useful source of reference whenever you need assistance with
your product.
Printed manuals are provided by a third-party (Lulu Press).
To order a printed manual, use the Lulu Press website link provided
below. The manual will then be printed and delivered to the
address you specify. Once an order is placed, it typically takes
Lulu Press approximately 5 to 10 working days to print and deliver
a printed manual.

 Supplier         How to purchase

                  1.   Click the following link.
                  2. In the displayed search field, enter the
                     required document number, e.g. 81406
                  www.bit.ly/rym-printshop

 Note:
 • Accepted methods of payment for printed manuals are credit
 cards and PayPal.
 • Printed manuals can be shipped worldwide.

2.3 Document illustrations
While every effort is made to ensure that the illustrations provided
in this publication accurately reflect the final released product,
due to editorial and production lead times, your product — and
if applicable — its user interface, may differ slightly from the
illustrations provided in this document, depending on product
variant and date of manufacture.
All images are provided for illustration purposes only.

                                                                     15

<!-- pdf page 16 | printed page 16 -->

2.4 Applicable software version
Product software is updated regularly to add new features and
improve existing functionality.
This document has been updated to reflect the following software
version:

 Product                           Software version

 JCU-4                             v2.0.12

Check the website for the latest software:

 JCU-4 software download link

 www.bit.ly/jcu4-download

<!-- pdf page 17 | printed page 17 -->

CHAPTER 3: SOFTWARE RELEASE SUMMARY

CHAPTER CONTENTS

•      3.1 Introduction — page 18
•      3.2 JCU-4 v2.0.12 Release Notes (December 2025) — page 18

Software Release Summary                                           17

<!-- pdf page 18 | printed page 18 -->

3.1 Introduction
Details of new features and improvements that have been included
in the latest JCU-4 software release are detailed here.
These details also appear inline in the relevant chapters of the
JCU-4 Installation & Operation Instructions (Document number:
71007). You may need to refer to these chapters to understand
the full context of the feature.
For more information on the new features and improvements
which have been introduced, refer to the following section that is
applicable to your FLIR maritime camera variant:
• p.51 — Operation (M460-Series / M560-Series)
• p.64 — Operation (M400-Series / M500-Series)
• p.77 — Operation (M300-Series)
• p.88 — Operation (M100-Series / M200-Series)
• p.99 — Operation (MD-Series)

3.2 JCU-4 v2.0.12 Release Notes
(December 2025)
The following changes have been implemented in release v2.0.12
of the JCU-4’s software: The changes may include New features,
Improvements and Bug fixes.
To download the latest software release visit:
 JCU-4 software download link

 www.bit.ly/jcu4-download

New features:
 New features

 A startup wizard has been added which enables you to configure the
 type of system the JCU-4 is connected to, as well as the JCU-4’s IP
 address type, IP address and netmask.

 Support for M460-Series / M560-Series cameras has been added.
 Camera status icons have been added to the [Controlled camera]
 screen (viewable when controlling an M300-Series / M400-Series /
 M460-Series / M500-Series / M560-Series camera).

New features

A [Main menu] navigation page has been added which enables you
to access the existing [Select camera], [Power down], [Brightness]
and [Camera focus] screens, as well as a new [JCU settings] screen.
A [Night] mode color palette option has been added to the
[Brightness] screen.
A [JCU settings] navigation page has been added which enables
you to access the new [Shortcut keys], [Joystick mode], [Cameras],
[Installation], [About], [Settings reset] and [Factory reset] screens.

The ability to assign shortcut actions to the JCU-4’s softkey buttons
(when an M460-Series / M560-Series camera is being controlled)
has been added. These actions can be assigned via either the new
[Shortcut keys] screen, or, the new Web browser user interface
[Softkey] menu.
The ability to configure which direction your camera tilts when the
JCU-4’s joystick is moved up and down has been added. This can
be configured via either the new [Joystick mode] screen, or, the new
Web browser user interface [Joystick] menu.

The ability to configure which compatible FLIR maritime cameras on
your network can be controlled by the JCU-4 has been added. This
can be configured via the new [Cameras] screen.

An alternate method of reconfiguring the JCU-4’s IP network
parameters has been added. These parameters can now also be
changed via the new [Installation] screen.

The ability to view additional information related to the JCU-4 has
been added. This information can be viewed via the new [About]
screen.

An alternate method of resetting the JCU-4’s settings (excluding any
configured IP network parameters) has been added. These settings
can now also be reset via the new [Settings reset] screen.

An alternate method of resetting the JCU-4’s settings (including any
configured IP network parameters) has been added. These settings
can now also be reset via the new [Factory reset] screen.
A [Spotlight on] notification screen has been added which appears
when the spotlight of a controlled M400-Series / M460-Series /
M500-Series / M560-Series camera is enabled.

<!-- pdf page 19 | printed page 19 -->

 New features

 The ability to initiate a controlled M460-Series / M560-Series
 camera’s object tracking system has been added. This can be
 initiated via either the [Video tracking] joystick button, or, the new
 [Ready to track] screen.

 The ability to trigger a controlled M460-LRF (30 Hz) / M560-LRF (30
 Hz) camera’s laser range finder (LRF) has been added. This can be
 triggered via the new [Ready to range] screen.
 The ability has been added to view event log information that can be
 used by FLIR technical support to help diagnose and troubleshoot
 issues experienced with your unit. This information can be viewed
 via the new Web browser user interface [Diagnostics] page.

General improvements:
 Improvements

 Responsiveness improved of the manual focus options available
 via the [Camera focus] screen.
 Control improved of the brightness options available via the
 [Brightness] screen.

Software Release Summary                                                  19

<!-- pdf page 20 | printed page 20 -->

CHAPTER 4: PRODUCT AND SYSTEM OVERVIEW

CHAPTER CONTENTS

•   4.1 Product overview — page 21
•   4.2 Required additional components — page 21
•   4.3 Compatible FLIR maritime cameras — page 22
•   4.4 System overview (example only) — page 22

<!-- pdf page 21 | printed page 21 -->

4.1 Product overview
The JCU-4 joystick control unit is an ultra-compact wired remote
keypad designed to control single or multiple FLIR maritime
cameras without the use of an additional control interface, such
as a multifunction display / chartplotter. With two power options
(Direct power and Power over Ethernet (PoE)) and the ability to be
retrofitted to an existing FLIR JCU-1 or JCU-2 cut-out, the JCU-4 is
ideal for providing control of your camera(s) from the required
location(s) onboard your vessel.

1.    LCD screen.
2. Keypad buttons.
3. Joystick.
The JCU-4 has the following key functions and features:
• IP connectivity to simplify installation and system integration.
• 2.9” backlit LCD screen for displaying camera information and
  menu options.
• 12 interactive buttons — includes 3 user-programmable buttons,
  which can be re-assigned via either:
     – The camera’s Web interface (applies when controlling an
       MD-Series / M100-Series / M200-Series / M300-Series /
       M400-Series / M500-Series camera).
Product and system overview

  – The JCU-4’s [Shortcut keys] screen (applies when controlling
    an M460-Series / M560-Series camera).
• An 8-way navigational pad which is used to navigate the JCU-4’s
  menus, the camera’s [On-screen Display] menus, and can
  optionally be used to pan and tilt the selected camera.
• Dedicated 3-axis joystick control which can be used to pan, tilt,
  and zoom (PTZ) the selected camera, and enter an M400XR /
  M460-Series / M500-Series / M560-Series into [Ready to track]
  mode.
• Can be retrofitted to the mounting cutout of an existing FLIR
  JCU-1 or JCU-2.
• Supports direct power connection @ 12 / 24 V dc nominal supply
  voltage, or Class 2 Power over Ethernet (PoE) @ 48 V nominal
  supply voltage.
• Low power consumption — 5 W maximum at full illumination.
• Dedicated secondary RayNet (Ethernet) connector for
  configuration and diagnostic purposes.
• Waterproof to IPx6 (suitable for above or below decks
  installation).

4.2 Required additional components
This product forms part of a system of electronics and requires
some or all of the following additional system components in order
to fully function.

 Component               Examples                    Refer to:

 Power Sourcing          • PoE Injector              p.127 —
 Equipment (PSE)                                     Spares and
 (Only if powering       • PoE network switch        accessories
 JCU-4 via PoE).
 Compatible FLIR         • M100-Series               For a full list of
 maritime camera                                     all compatible
                         • M200-Series               cameras, refer
                                                     to:
                         • M300-Series               p.22 —
                                                     Compatible
                                                     FLIR maritime
                                                     cameras

                                                                          21

<!-- figure 1 on pdf page 21 at 38,134-314,314 pt | caption: none | text-layer labels: none | nearby labels: 1. | LCD screen. | 2. Keypad buttons. | OCR: no legible text (0/2 words >= 60, mean confidence 49) -->

<!-- pdf page 22 | printed page 22 -->

 Component              Examples                   Refer to:

 Ethernet network       • 10/100/1000 Mbits/s      p.127 —
 switch                   network switches         Spares and
 (Required in larger      featuring RayNet         accessories
 systems featuring        connectors.
 multiple IP devices)
                        • 10/100/1000 Mbits/s
                          network switches
                          featuring RJ45
                          connectors.
 Cable extensions       Network extension cables   p.41 —
                        featuring RayNet or        Network cable
                        RJ45 connectors, as        extensions
                        appropriate.

4.3 Compatible FLIR maritime
cameras
Your product can be used in conjunction with the following FLIR
maritime cameras:
 Camera series                     Camera models

 M560-Series:                      M560 (30 Hz), M560-LRF (30 Hz)
 M500-Series:                      M500
 M460-Series:                      M460 (30 Hz), M460-LRF (30 Hz)
 M400-Series:                      M400, M400XR
 M300-Series:                      M300, M332, M364, M364 C,
                                   M364 LR
 M200-Series:                      M232
 M100-Series:                      M132
 MD-Series:                        MD324, MD625

4.4 System overview (example only)
The JCU-4 has a flexible array of connection options which enable
you to integrate it with your electronics system.
With the right combination of devices and connections, you can
use the JCU-4 to control a connected FLIR maritime camera’s image
from the most convenient locations on your vessel.

The following illustration shows a typical installation scenario.
For more system configuration examples, ranging from small to
large systems, refer to your FLIR maritime camera Installation and
Operation Instructions manual: www.bit.ly/FLIR-maritime-docs

 Note:
 Power connections are not shown in this illustration. For power
 connection information, refer to the instructions which accompany
 each device.

         Description

 1       Digital video (SDI) monitor, available separately from
         third-party retailers.
 2       M300-Series camera, available separately.
 3       SDI video cable (BNC connectors), available separately.
 4       RayNet (Ethernet) to RJ45 adapter cable, available
         separately.
 5       Right-angled RayNet (Ethernet) to RayNet (Ethernet) cable,
         available separately.
 6       Laptop — primarily intended for configuration and diagnostic
         purposes, available separately from third-party retailers.

<!-- figure 1 on pdf page 22 at 334,77-607,257 pt | caption: none | text-layer labels: none | nearby labels: Note: | OCR text follows (tesseract, unverified; 2/4 words >= 60, mean confidence 45) -->
a
SF
<!-- end of figure 1 -->

<!-- pdf page 23 | printed page 23 | header: Description -->

  7          JCU-4.
  8          Non-PoE network switch, available separately from third-party
             retailers.
  9          3 m (9.84 ft) Right-angled RayNet (Ethernet) to RJ45 adapter
             cable (1x supplied with E70695).

Product and system overview                                                  23

<!-- pdf page 24 | printed page 24 -->

CHAPTER 5: PARTS SUPPLIED

CHAPTER CONTENTS

•   5.1 Parts supplied — page 25
•   5.2 Parts supplied (Joystick only) — page 25
•   5.3 Inline fuse requirement — page 25

<!-- pdf page 25 | printed page 25 -->

5.1 Parts supplied
The following parts are supplied when ordering the JCU-4, part
number: E70695

                 Description

  1              1x JCU-4 (includes 4x screws and 4x mounting plates
                 pre-fitted).
  2              1x Front cover.
  3              1x Weather cover.
  4              1x Documentation pack.
  5              1x Right-angled RayNet (Ethernet) to RJ45 adapter cable,
                 3 m (9.84 ft).
  6              1x Right-angled 3-pin power cable, 3 m (9.84 ft).

Parts supplied

5.2 Parts supplied (Joystick only)
The following parts are supplied when ordering the JCU-4 (Joystick
only), part number: E70697

        Description

 1      1x JCU-4 (includes 4x screws and 4x mounting plates
        pre-fitted).
 2      1x Front cover.
 3      1x Documentation pack.

5.3 Inline fuse requirement
If your product is NOT supplied with an inline fuse (whether
separately or fitted to the power cable), you MUST fit a
suitably-rated inline fuse to your product’s red power wire, housed
in a waterproof fuse holder.
The illustration below shows the two main types of inline fuse
with waterproof holder, for use in marine electronics installations.
Fuses in a variety of ratings are widely available at chandleries
and marine electrical retailers.
Select one of the following fuse types to protect your product:

                                                                   25

<!-- figure 1 on pdf page 25 at 38,72-314,242 pt | caption: none | text-layer labels: none | nearby labels: Description | 1 | 1 | 2 | 3 | OCR: no legible text (0/1 words >= 60, mean confidence 12) -->
<!-- figure 2 on pdf page 25 at 334,79-607,216 pt | caption: none | text-layer labels: Description | nearby labels: 1 | 2 | 1x Front cover. | OCR text follows (tesseract, unverified; 3/3 words >= 60, mean confidence 84) -->
N
SS
S
<!-- end of figure 2 -->

<!-- pdf page 26 | printed page 26 -->

1.   Waterproof fuse holder containing a “glass”-type inline fuse.
2. Waterproof fuse holder containing a “blade”-type inline fuse.
Fuse ratings:
• Voltage rating — must be equal to or greater than the voltage
  of your vessel’s power supply.
• Current rating — refer to the Inline fuse and thermal breaker
  rating section in this document.

<!-- figure 1 on pdf page 26 at 38,29-314,170 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 27 | printed page 27 -->

CHAPTER 6: PRODUCT DIMENSIONS

CHAPTER CONTENTS

•       6.1 Product dimensions — page 28

Product dimensions                         27

<!-- pdf page 28 | printed page 28 -->

6.1 Product dimensions

    Description

A   146.66 mm (5.77 in)
B   93.66 mm (3.69 in)
C   44.99 mm (1.77 in)
D   35.00 mm (1.38 in)
E   49.94 mm (1.97 in)
F   63.36 mm (2.49 in)
G   52.71 mm (2.08 in)
H   77.50 mm (3.05 in)
I   130.00 mm (5.12 in)

<!-- figure 1 on pdf page 28 at 38,43-314,240 pt | caption: none | text-layer labels: Description | nearby labels: 6.1 Product dimensions | A | 146.66 mm (5.77 in) | B | 93.66 mm (3.69 in) | OCR: no legible text (0/2 words >= 60, mean confidence 19) -->

<!-- pdf page 29 | printed page 29 -->

CHAPTER 7: LOCATION REQUIREMENTS

CHAPTER CONTENTS

•       7.1 Warnings and cautions — page 30
•       7.2 General location requirements — page 30
•       7.3 Location requirements — page 30
•       7.4 EMC installation guidelines — page 30
•       7.5 Suppression ferrites — page 31
•       7.6 Connections to other equipment — page 31
•       7.7 Compass safe distance — page 31

Location requirements                                  29

<!-- pdf page 30 | printed page 30 -->

7.1 Warnings and cautions
 Important:
 Before proceeding, ensure that you have read and understood the
 warnings and cautions provided in the following section of this
 document:
 • p.10 — Important information

              Warning: Potential ignition source
              This product is NOT approved for use in
              hazardous/flammable atmospheres. Do NOT install
              in a hazardous/flammable atmosphere (such as in an
              engine room or near fuel tanks).

7.2 General location requirements
When selecting a location for your product it is important to
consider a number of factors.
Factors for consideration:
• Ventilation — To ensure adequate airflow:
  – Ensure that product is mounted in a compartment of suitable
    size.
  – Ensure that ventilation holes are not obstructed. Allow
    adequate separation of all equipment.
  Any specific requirements for each system component are
  provided later in this chapter.
• Mounting surface — Ensure product is adequately supported
  on a secure surface. Do not mount units or cut holes in places
  which may damage the structure of the vessel.
• Cabling — Ensure the product is mounted in a location which
  allows proper routing, support and connection of cables:
  – Minimum bend radius of 100 mm (3.94 in) unless otherwise
    stated.
  – Use cable clips to prevent stress on connectors.
  – If your installation requires multiple ferrites to be added to a
    cable then additional cable clips should be used to ensure the
    extra weight of the cable is supported.

• Water ingress — The product is suitable for mounting both
  above and below decks. Although the unit is waterproof, it
  is good practice to locate it in a protected area away from
  prolonged and direct exposure to rain and salt spray.
• Electrical interference — Select a location that is far enough
  away from devices that may cause interference, such as motors,
  generators and radio transmitters / receivers.
• Power supply — Select a location that is as close as possible
  to the vessel’s DC power source. This will help to keep cable
  runs to a minimum.

7.3 Location requirements
When planning the installation location, consider the following
points:
• Select a position on your vessel that is close to a display showing
  the camera video output.
• Before mounting the unit, consider the required minimum cable
  lengths and cable routing options available.
• Ensure the unit is mounted at least 200 mm (7.9 in.) away from
  any equipment fitted with a magnetic compass.
• The unit must be mounted in the vertical (portrait) orientation.
• The unit must NOT be mounted higher than 2 m (6.56 ft.) above
  the floor level at your selected mounting location.

7.4 EMC installation guidelines
FLIR equipment and accessories conform to the appropriate
Electromagnetic Compatibility (EMC) regulations, to minimize
electromagnetic interference between equipment and minimize the
effect such interference could have on the performance of your
system.
Correct installation is required to ensure that EMC performance is
not compromised.

 Note:
 In areas of extreme EMC interference, some slight interference may
 be noticed on the product. Where this occurs the product and the
 source of the interference should be separated by a greater distance.

<!-- figure 1 on pdf page 30 at 41,118-86,190 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 31 | printed page 31 -->

For optimum EMC performance we recommend that wherever
possible:
• FLIR equipment and cables connected to it are:
   – At least 1 m (3.3 ft) from any equipment transmitting or cables
     carrying radio signals e.g. VHF radios, cables and antennas. In
     the case of SSB radios, the distance should be increased to 2
     m (6.6 ft).
   – More than 2 m (6.6 ft) from the path of a radar beam. A radar
     beam can normally be assumed to spread 20 degrees above
     and below the radiating element.
• The product is supplied from a separate battery from that used
  for engine start. This is important to prevent erratic behavior
  and data loss which can occur if the engine start does not have
  a separate battery.
• FLIR specified cables are used.
• Cables are not cut or extended, unless doing so is detailed in
  the installation manual.

  Note:
  Where constraints on the installation prevent any of the
  above recommendations, always ensure the maximum possible
  separation between different items of electrical equipment, to
  provide the best conditions for EMC performance throughout the
  installation.

7.5 Suppression ferrites
• Cables may be pre-fitted or supplied with suppression ferrites.
  These are important for correct EMC performance. If ferrites are
  supplied separately to the cables (i.e. not pre-fitted), you must fit
  the supplied ferrites, using the supplied instructions.
• If a ferrite has to be removed for any purpose (e.g. installation or
  maintenance), it must be replaced in the original position before
  the product is used.
• Use only ferrites of the correct type, supplied by the manufacturer
  or its authorized dealers.
• Where an installation requires multiple ferrites to be added to a
  cable, additional cable clips should be used to prevent stress on
  the connectors due to the extra weight of the cable.
• If your installation requires long cable runs, you may need to fit
  additional ferrites to maintain acceptable EMC performance.
Location requirements

7.6 Connections to other equipment
Requirement for ferrites on non-FLIR cables:
If your FLIR equipment is to be connected to other equipment using
a cable not supplied by FLIR, a suppression ferrite MUST always
be attached to the cable near the FLIR unit.
For more information, refer to your third-party cable manufacturer.

7.7 Compass safe distance
To prevent potential interference with the vessel's magnetic
compasses, ensure an adequate distance is maintained from the
product.
When choosing a suitable location for the product, you must aim
to maintain a distance of at least 200 mm (7.9 in.) in all directions
from any compasses.
For some smaller vessels it may not be possible to locate the
product this far away from a compass. In this situation, when
choosing the installation location for your product, ensure that the
compass is not affected by the product when it is in a powered
on state.

                                                                    31

<!-- pdf page 32 | printed page 32 -->

CHAPTER 8: MOUNTING

CHAPTER CONTENTS

•   8.1 Tools required — page 33
•   8.2 Mounting options — page 33
•   8.3 Removing the front cover — page 33
•   8.4 Retrofit mounting the unit — page 34
•   8.5 Surface mounting the unit — page 34
•   8.6 Fitting the front cover — page 35

<!-- pdf page 33 | printed page 33 -->

8.1 Tools required
The following tools are required for installation.

1.   (1) Power drill.

2.   (1) Drill bit (currently illustrated) or hole cutter of an appropriate
     size for the 6.0 mm (0.24 in) surface mount corner diameter
     cutout line (appropriate size dependent on thickness and
     material of mounting surface).
3.   (1) Jigsaw.

4.   (1) Half round file (or sandpaper).

5. Pozidrive screwdriver.
6. Flathead screwdriver.
7.   Marine grade sealant.
8. Masking / self adhesive tape.

 Note:
 (1) Items are only required when surface mounting the display.

8.2 Mounting options
The unit can be mounted in 2 different ways, depending on your
preferred installation method:
1.   Retrofit mounting — this method should be used when the
     unit is being retrofitted to the mounting cutout of an existing
     FLIR JCU-1 or JCU-2.
Mounting

2. Surface mounting — this method should be used when the
   unit is NOT being fitted to a pre-existing mounting cutout.

 Note:
 Both mounting methods provide an installation where the product
 protrudes by the thickness of the bezel from the mounting surface.

8.3 Removing the front cover
To gain access to the mounting hole locations, the front cover
must first be removed.

 Note:
 To help prevent scratching the product, cover the tip of your
 screwdriver blade with a small piece of insulation tape.

1. Using a thin flat-bladed screwdriver, insert the tip of the
   screwdriver into an available notch (as indicated above) between
   the edge of the front cover and the keypad mat.
2. Gently push the front cover away from the unit to release the
   cover.
   Take care not to bend the front cover during removal.

                                                                      33

<!-- figure 1 on pdf page 33 at 38,60-314,211 pt | caption: none; nearest centred text below: "(1) Drill bit (currently illustrated) or hole cutter of an appropriate" | text-layer labels: none | nearby labels: 8.1 Tools required | 1. | (1) Power drill. | 2. | OCR: no legible text (0/2 words >= 60, mean confidence 18) -->
<!-- figure 2 on pdf page 33 at 334,156-607,341 pt | caption: none | text-layer labels: none | nearby labels: 8.3 Removing the front cover | Note: | OCR: no legible text (0/6 words >= 60, mean confidence 23) -->

<!-- pdf page 34 | printed page 34 -->

8.4 Retrofit mounting the unit
The unit can be retrofitted to the mounting cutout of an existing
FLIR JCU-1 or JCU-2. Follow the steps listed below to retrofit the
unit.

 Note:
 It may be necessary to use a marine-grade sealant if the mounting
 surface is not entirely flat and stiff, or if the surface has a rough finish.

1. Check the selected location for the unit. A clear, flat area with
   suitable clearance behind the mounting surface is required.
   If this is not possible, consider creating a new cutout for the
   unit by following the steps found in the following section:
   p.34 — Surface mounting the unit
2. Remove the pre-existing JCU-1 / JCU-2 unit and fixings from
   the mounting surface cutout.
3. Depending on your cable routing plan, either:
   • Remove the existing JCU-1 / JCU-2’s RJ45-to-RJ45 Ethernet
     cable, then route the appropriate supplied cables behind the
     mounting surface cutout; OR:
   • Connect the existing JCU-1 / JCU-2’s RJ45-to-RJ45 Ethernet
     cable to a RayNet (female) to RJ45 (female) adapter cable
     (available separately).

   This may be difficult or not possible once the unit has been
   mounted.
4. With the front cover removed, connect the cables to your unit
   through the mounting surface cutout, then insert the unit into
   the cutout.
5. Using a suitable pozihead screwdriver, tighten the pre-fitted
   screws until the mounting plates attached to the screws are
   secure against the mounting surface.
6. Fit the front cover to the unit by following the instructions in the
   following section: p.35 — Fitting the front cover

              Warning: Marine-grade sealant
              Only use marine-grade neutral cure polyurethane
              sealants. Do NOT use sealants containing acetate or
              silicone, which can cause damage to plastic parts.

8.5 Surface mounting the unit
Follow the steps listed below to surface mount the unit.

 Note:
 It may be necessary to use a marine-grade sealant if the mounting
 surface is not entirely flat and stiff, or if the surface has a rough finish.

<!-- figure 1 on pdf page 34 at 38,139-314,324 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 52) -->
4
6?
Ww
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 34 at 334,144-379,206 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 34 at 559,144-607,206 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 35 | printed page 35 -->

1. Check the selected location for the unit. A clear, flat area with
   suitable clearance behind the panel is required.
2. Before modifying the mounting surface, refer to the dimensions
   supplied in this document to ensure there is enough space for
   the unit and all cables.
3. Fix the supplied mounting template to the selected location,
   using masking or self adhesive tape.
4. Use a drill and an appropriate size drill bit or hole cutter to cut
   out the corners of the cutout line. The corner diameter for the
   unit is 6 mm (0.24 in).
5. Use a jigsaw or similar cutting tool to cut out the remainder
   of the cutout area.
6. Ensure that the unit fits into the removed area and then remove
   rough edges.
7. Route the appropriate supplied cables behind the mounting
   surface cutout.
    This may be difficult or not possible once the unit has been
    mounted.
8. With the front cover removed, connect the cables to your unit
   through the mounting surface cutout, then insert the unit into
   the cutout.
9. Using a suitable pozihead screwdriver, tighten the pre-fitted
   screws until the mounting plates attached to the screws are
   secure against the mounting surface.
Mounting

10. Fit the front cover to the unit by following the instructions found
    in the following section: p.35 — Fitting the front cover

             Warning: Marine-grade sealant
             Only use marine-grade neutral cure polyurethane
             sealants. Do NOT use sealants containing acetate or
             silicone, which can cause damage to plastic parts.

8.6 Fitting the front cover
The keypad mat should be fitted once the unit has been secured
to the mounting surface.

1. Ensure the front cover is correctly orientated.
2. Starting with one of the longer edges, place the front cover over
   the keypad mat and gently push down so that the long edge
   is in position.
3. Gently push the opposite long edge of the front cover down
   until it is in position.
4. Once the front cover is in position, firmly push along all edges
   of the front cover until it is secure.

                                                                     35

<!-- figure 1 on pdf page 35 at 38,29-314,211 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 59) -->
3-5?
4
3?
10”
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 35 at 334,60-379,122 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 35 at 559,60-607,122 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 35 at 334,187-607,370 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 37) -->
p
2)
<!-- end of figure 4 -->

<!-- pdf page 36 | printed page 36 -->

CHAPTER 9: CABLES AND CONNECTIONS — GENERAL INFORMATION

CHAPTER CONTENTS

•   9.1 General cabling guidance — page 37

<!-- pdf page 37 | printed page 37 | header: Note: -->

9.1 General cabling guidance
Cable types and length
It is important to use cables of the appropriate type and length.
• Unless otherwise stated use only standard cables of the correct
  type, supplied by FLIR.
• Ensure that any non-FLIR cables are of the correct quality and
  gauge. For example, longer power cable runs may require larger
  wire gauges to minimize voltage drop along the run.

Cable routing and bend radius
To maximize cable performance and lifespan, it’s important to
ensure that all cables are routed correctly and adequate space is
provided to allow for each cable’s minimum bend radius.

Minimum cable bend radius

Do NOT bend cables excessively. Wherever possible, ensure that
your chosen product installation location allows enough clearance
for the minimum cable bend diameter specified in the following
table:

               Description                         Value

  Ø            Cable minimum bend diameter.        200 mm
                                                   (7.87 in.)
  R            Cable minimum bend radius.          100 mm
                                                   (3.94 in.)

Cables and connections — General information

 Note:
 For products where multiple different cable types are connected,
 each with a different minimum cable bend radius, the higher figure is
 provided in the table above (i.e. the cable with the greatest minimum
 bend radius is specified).

Cable routing — best practices
• Protect all cables from physical damage and exposure to heat.
  Use trunking or conduit where possible. Do NOT run cables
  through bilges or doorways, or close to moving or hot objects.
• Secure cables in place using cable clips or cable ties. Coil any
  excess cable and tie it out of the way.
• Where a cable passes through an exposed bulkhead or deckhead,
  use a suitable watertight feed-through (conduit).
• Do NOT run cables near to engines or fluorescent lights.
• Always route data cables as far away as possible from:
  – Other equipment and cables.
  – High current-carrying AC and DC power lines.
  – Antennas.

Strain relief
Use adequate strain relief for cabling to ensure that connectors
are protected from strain and will not pull out under extreme sea
conditions.

Circuit isolation
Appropriate circuit isolation is required for installations using both
AC and DC current:
• Always use isolating transformers or a separate power-inverter
  to run PCs, processors, displays and other sensitive electronic
  instruments or devices.
• If using Weather FAX audio cables, always use an isolating
  transformer.
• If using a third-party audio amplifier, always use an isolated
  power supply.
• If using an RS232/NMEA converter, always ensure optical
  isolation on the signal lines.
• Always ensure that PCs or other sensitive electronic devices have
  a dedicated power circuit.
                                                                     37

<!-- figure 1 on pdf page 37 at 38,211-314,346 pt | caption: none | text-layer labels: none | nearby labels: Minimum cable bend radius | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 38 | printed page 38 -->

Cable shielding
Ensure that cable shielding is not damaged during installation and
that all cables are properly shielded.

 Important:
 Be aware that some third-party cables and adapters (for example,
 certain Ethernet cables using RJ45 connectors) are not always
 shielded. To prevent breaks in cable shielding continuity and
 potential grounding issues, special attention is required to ensure
 that any cables, extension cables, adapters, or other signal-coupling
 devices used in cable runs maintain all shield connections
 throughout the cable run.

Bare-ended wire connections
You must ensure that any bare-ended wires are adequately
protected from short circuit and water ingress.

Bare-ended wire connections
It is recommended that bare-ended wire connections are made
by soldering or using crimp connectors, and then protected by
wrapping the connection in electrical insulation tape.

Unused bare-ended wires
Any unused bare-ended wires should be folded back and wrapped
in electrical insulation tape.

Connecting cables
Follow the steps below to connect the cable(s) to your product.
1. Ensure that the vessel's power supply is switched off.
2. Ensure that the device being connected has been installed in
   accordance with the installation instructions supplied with that
   device.
3. Ensuring correct orientation, push cable connectors fully onto
   the corresponding connectors.
4. Engage any locking mechanism to ensure a secure connection
   (e.g.: turn locking collars clockwise until tight, or in the locked
   position).
5. Ensure any bare ended wire connections are suitably insulated
   to prevent shorting and corrosion due to water ingress.

<!-- pdf page 39 | printed page 39 -->

CHAPTER 10: NETWORK CONNECTIONS

CHAPTER CONTENTS

•       10.1 Power options — page 40
•       10.2 Connections overview — page 40
•       10.3 System overview (example only) — page 41

Network connections                                     39

<!-- pdf page 40 | printed page 40 | header: 10.1 Power options -->

This product must be powered using only one of the following
methods:
1.   PoE (Power over Ethernet)
     • Direct connection to a PSE (Power Sourcing Equipment)
       device, e.g. a PoE Injector or a PoE network switch. Only
       one Ethernet cable is required to carry both data and power
       signals.
2. Self-powered (“direct / dedicated / alternate power
   connection”)
     • Direct connection to a vessel's power supply using the
       supplied power cable.

Multiple power sources
Product behavior when connected to more than one power supply.

 Important:
 If a direct power connection is made to both the vessel’s power
 supply (via the JCU-4’s 3-pin power connection) and a PSE device
 (via the JCU-4’s PoE connection) at the same time, the JCU-4
 will automatically default to the vessel’s power supply as its sole
 power source.

10.2 Connections overview
The JCU-4 includes the following connections:

Connector                             Suitable cables

1) Power                              • Right-angled power supply
(Only required if PoE is not used).     cable, 1x supplied.
Connects to:
• 12 / 24 V dc power supply
2) 10/100/1000 Mbits/s RayNet         • Right-angled RayNet
(Ethernet)                              (Ethernet) to RJ45 adapter
This connection is intended             cable, 1x supplied with
for configuration and                   E70695, or available
diagnostic purposes only.               separately.
Connects to:
                                      • Right-angled RayNet
• RayNet (Ethernet) network             (Ethernet) to RayNet
  device.                               (Ethernet) cable, available
• RJ45 network device.                  separately.

3) 10/100/1000 Mbits/s PoE            • Right-angled RayNet
RayNet (Ethernet)                       (Ethernet) to RJ45 adapter
                                        cable, 1x supplied with
• RayNet (Ethernet) network             E70695, or available
  device.                               separately.
• RJ45 network device.                • Right-angled RayNet
                                        (Ethernet) to RayNet
                                        (Ethernet) cable, available
                                        separately.

<!-- figure 1 on pdf page 40 at 334,29-607,233 pt | caption: none | text-layer labels: Connector | Suitable cables | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 41 | printed page 41 | header: Description -->

10.3 System overview (example only)
The JCU-4 has a flexible array of connection options which enable
you to integrate it with your electronics system.
With the right combination of devices and connections, you can
use the JCU-4 to control a connected FLIR maritime camera’s image
from the most convenient locations on your vessel.
The following illustration shows a typical installation scenario.
For more system configuration examples, ranging from small to
large systems, refer to your FLIR maritime camera Installation and
Operation Instructions manual: www.bit.ly/FLIR-maritime-docs

  Note:
  Power connections are not shown in this illustration. For power
  connection information, refer to the instructions which accompany
  each device.

             Description

  1          Digital video (SDI) monitor, available separately from
             third-party retailers.
  2          M300-Series camera, available separately.
  3          SDI video cable (BNC connectors), available separately.
Network connections

        Description

 4      RayNet (Ethernet) to RJ45 adapter cable, available
        separately.
 5      Right-angled RayNet (Ethernet) to RayNet (Ethernet) cable,
        available separately.
 6      Laptop — primarily intended for configuration and diagnostic
        purposes, available separately from third-party retailers.
 7      JCU-4.
 8      Non-PoE network switch, available separately from third-party
        retailers.
 9      3 m (9.84 ft) Right-angled RayNet (Ethernet) to RJ45 adapter
        cable (1x supplied with E70695).

Network cable extensions
If you wish to extend the length of a network cable connected to
your product, refer to the following section for further information:
p.127 — Spares and accessories

                                                                       41

<!-- figure 1 on pdf page 41 at 38,149-314,329 pt | caption: none | text-layer labels: none | nearby labels: 7 | 8 | 9 | Note: | OCR: no legible text (0/2 words >= 60, mean confidence 44) -->

<!-- pdf page 42 | printed page 42 -->

CHAPTER 11: POE POWER CONNECTIONS

CHAPTER CONTENTS

•   11.1 Power options — page 43
•   11.2 Power over Ethernet (PoE) — page 43
•   11.3 PSE (Power Sourcing Equipment) power connection — page 43
•   11.4 Network cable extensions — page 44

<!-- pdf page 43 | printed page 43 | header: 11.1 Power options -->

11.1 Power options
This product must be powered using only one of the following
methods:
1.    PoE (Power over Ethernet)
      • Direct connection to a PSE (Power Sourcing Equipment)
        device, e.g. a PoE Injector or a PoE network switch. Only
        one Ethernet cable is required to carry both data and power
        signals.
2. Self-powered (“direct / dedicated / alternate power
   connection”)
      • Direct connection to a vessel's power supply using the
        supplied power cable.

Multiple power sources
Product behavior when connected to more than one power supply.

 Important:
 If a direct power connection is made to both the vessel’s power
 supply (via the JCU-4’s 3-pin power connection) and a PSE device
 (via the JCU-4’s PoE connection) at the same time, the JCU-4
 will automatically default to the vessel’s power supply as its sole
 power source.

11.2 Power over Ethernet (PoE)
Power over Ethernet (PoE) is a system which allows both power
and data to be passed along a single CAT 6 Ethernet cable.
There are 2 main types of PoE device:
• Power Sourcing Equipment (PSE) — this PoE system
  component provides electrical power over a CAT 6 Ethernet
  cable.
• Powered Device (PD) — this PoE system component is
  powered by the electrical power provided by the Power Sourcing
  Equipment (PSE).
The JCU-4 is a Class 2 Powered Device (PD) with a 48 V
nominal supply voltage, which consumes 5 W maximum (at full
illumination). Before connecting the JCU-4, ensure that your Power
Sourcing Equipment (PSE)’s maximum power output will not be
surpassed. For further information on your PSE’s maximum power
output, refer to the instructions that accompany the device.
PoE power connections

11.3 PSE (Power Sourcing Equipment)
power connection
The JCU-4 can be powered via a PSE’s (Power Sourcing Equipment)
Ethernet connection.
The following section will provide 2 different PSE (Power Sourcing
Equipment) connection examples:
• p.43 — PoE network switch power connection
• p.44 — PoE injector power connection

PoE network switch power connection
In the following example, the PSE (Power Sourcing Equipment)
providing power to the JCU-4 is the FLIR 8-port Gigabit Network
Switch (part number: 4230175).

 Important:
 Any device supplying PoE (Power over Ethernet) to the JCU-4 must
 output a nominal supply voltage in the range of 44 to 57 V dc.

       Description

 1     JCU-4.
 2     PSE (Power Sourcing Equipment) providing PoE (Power over
       Ethernet) to the JCU-4 (e.g. PoE network switch is shown in
       the example above, available separately).
 3     3 m (9.84 ft) Right-angled RayNet (Ethernet) to RJ45 adapter
       cable, 1x supplied with E70695, or available separately.

                                                                      43

<!-- figure 1 on pdf page 43 at 334,187-607,324 pt | caption: none | text-layer labels: none | nearby labels: Important: | OCR text follows (tesseract, unverified; 1/5 words >= 60, mean confidence 34) -->
2?
<!-- end of figure 1 -->

<!-- pdf page 44 | printed page 44 | header: Description -->

PoE injector power connection
In the following example, the PSE (Power Sourcing Equipment)
providing power to the JCU-4 is the FLIR PoE Injector (2nd
Generation; 5 Gbit) (part number: A80811).

 Important:
 If powering the JCU-4 via the separately-available PoE Injector (2nd
 Generation; 5 Gbit) (A80811), do NOT connect the power input
 labelled “VIN1+” on the PoE Injector.

 Important:
 Any device supplying PoE (Power over Ethernet) to the JCU-4 must
 output a nominal supply voltage in the range of 44 to 57 V dc.

        Description

 1      JCU-4.
 2      3 m (9.84 ft) Right-angled RayNet (Ethernet) to RJ45 adapter
        cable, 1x supplied with E70695, or available separately.
 3      Non-PoE network switch, available separately from third-party
        retailers.
 4      12 / 24 V dc power supply — providing power to the PoE
        Injector.

        Description

 5      RJ45 to RJ45 cable, available separately.
 6      PSE (Power Sourcing Equipment) providing PoE (Power over
        Ethernet) to the JCU-4 (e.g. PoE Injector (A80811) is shown
        in the example above, available separately).

11.4 Network cable extensions
If you wish to extend the length of a network cable connected to
your product, refer to the following section for further information:
p.127 — Spares and accessories

<!-- figure 1 on pdf page 44 at 38,77-314,223 pt | caption: none | text-layer labels: none | nearby labels: 5 | 6 | Important: | OCR text follows (tesseract, unverified; 9/17 words >= 60, mean confidence 59) -->
10
1?
Do NOT use
a
5?
24V de
<!-- end of figure 1 -->

<!-- pdf page 45 | printed page 45 | footer: Non-PoE power connections -->

CHAPTER 12: NON-POE POWER CONNECTIONS

CHAPTER CONTENTS

•   12.1 Power options — page 46
•   12.2 Direct power connection — page 46
•   12.3 Inline fuse requirement — page 46
•   12.4 Inline fuse and thermal breaker ratings — page 47
•   12.5 Power distribution — page 47
•   12.6 Power cable extension (12 / 24 V systems) — page 49
•   12.7 Power cable drain wire connection — page 50

<!-- pdf page 46 | printed page 46 | header: 12.1 Power options -->

This product must be powered using only one of the following
methods:
1.   PoE (Power over Ethernet)
     • Direct connection to a PSE (Power Sourcing Equipment)
       device, e.g. a PoE Injector or a PoE network switch. Only
       one Ethernet cable is required to carry both data and power
       signals.
2. Self-powered (“direct / dedicated / alternate power
   connection”)
     • Direct connection to a vessel's power supply using the
       supplied power cable.

Multiple power sources
Product behavior when connected to more than one power supply.

 Important:
 If a direct power connection is made to both the vessel’s power
 supply (via the JCU-4’s 3-pin power connection) and a PSE device
 (via the JCU-4’s PoE connection) at the same time, the JCU-4
 will automatically default to the vessel’s power supply as its sole
 power source.

12.2 Direct power connection
The JCU-4 can be powered directly from a 12 V or 24 V power
source, using the 3 m (9.8 ft) right-angled 3-pin power cable
(supplied with E70695, or available separately). The direct power
connection is only required if PoE is not used to power the
JCU-4).
The right-angled 3-pin power cable includes bare stripped wires,
which are suitable for direct connection to a 12 V or 24 V power
supply:

        Description

 1      JCU-4.
 2      3 m (9.8 ft) Right-angled 3-pin power cable, 1x supplied with
        E70695, or available separately.
 3      Red wire (positive) — connects to the power supply’s positive
        terminal.
 4      Waterproof fuse holder containing a suitably-rated
        inline fuse (not supplied), which must be fitted to the
        red positive wire — refer to the following fuse ratings:
        p.47 — Inline fuse and thermal breaker ratings

 5      Gray wire (drain) — connects to the vessel RF ground (if
        available), or the negative battery terminal.
 6      Black wire (negative) — connects to the power supply’s
        negative terminal.

12.3 Inline fuse requirement
If your product is NOT supplied with an inline fuse (whether
separately or fitted to the power cable), you MUST fit a
suitably-rated inline fuse to your product’s red power wire, housed
in a waterproof fuse holder.
The illustration below shows the two main types of inline fuse
with waterproof holder, for use in marine electronics installations.
Fuses in a variety of ratings are widely available at chandleries
and marine electrical retailers.
Select one of the following fuse types to protect your product:

<!-- figure 1 on pdf page 46 at 334,29-607,151 pt | caption: none | text-layer labels: none | nearby labels: Description | 1 | JCU-4 . | OCR text follows (tesseract, unverified; 1/3 words >= 60, mean confidence 49) -->
*5
<!-- end of figure 1 -->

<!-- pdf page 47 | printed page 47 | footer: Non-PoE power connections -->

1.   Waterproof fuse holder containing a “glass”-type inline fuse.
2. Waterproof fuse holder containing a “blade”-type inline fuse.
Fuse ratings:
• Voltage rating — must be equal to or greater than the voltage
  of your vessel’s power supply.
• Current rating — refer to the Inline fuse and thermal breaker
  rating section in this document.

12.4 Inline fuse and thermal breaker
ratings
The following inline fuse and thermal breaker ratings apply to
your product:

 Inline fuse rating                 Thermal breaker rating

 • 12 V: 1A                         • 12 V: 1A
 • 24 V: 500mA                      • 24 V: 500mA

 Note:
 The suitable fuse rating for the thermal breaker is dependent on
 the number of devices you are connecting. If in doubt, consult an
 authorized FLIR dealer.

12.5 Power distribution
Recommendations and best practice for the power connection of
products supplied with a drain wire as part of the supplied power
cable.
• The product is supplied with a power cable, either as a separate
  item or a captive cable permanently attached to the product.
  Only use the power cable supplied with the product. Do NOT use
  a power cable designed for, or supplied with, a different product.
• Refer to the Power connection section for more information on
  how to identify the wires in your product’s power cable, and
  where to connect them.
• See below for more information on implementation for some
  common power distribution scenarios:

 Important:
 • When planning and wiring, take into consideration other
 products in your system, some of which (e.g. sonar modules)
 may place large power demand peaks on the vessel’s electrical
 system, which may impact the voltage available to other
 products during the peaks.
 • The information provided below is for guidance only, to
 help protect your product. It covers common vessel power
 arrangements, but does NOT cover every scenario. If you are
 unsure how to provide the correct level of protection, please
 consult an authorized dealer or a suitably qualified professional
 marine electrician.

Implementation — connection to distribution panel
(Recommended)

<!-- figure 1 on pdf page 47 at 38,29-314,170 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 47 at 334,362-607,449 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/9 words >= 60, mean confidence 26) -->
3°=
<!-- end of figure 2 -->

<!-- pdf page 48 | printed page 48 | header: Description / Description -->

 1    Waterproof fuse holder containing a suitably-rated inline fuse
      must be fitted. For suitable fuse rating, refer to: Inline fuse
      and thermal breaker ratings.
 2    Product power cable.
 3    Drain wire connection point.

• It is recommended that the supplied power cable is connected
  to a suitable breaker or switch on the vessel's distribution panel
  or factory-fitted power distribution point.
• The distribution point should be fed from the vessel’s primary
  power source by 8 AWG (8.36 mm2) cable.
• Ideally, all equipment should be wired to individual suitably-rated
  thermal breakers or fuses, with appropriate circuit protection.
  Where this is not possible and more than 1 item of equipment
  shares a breaker, use individual inline fuses for each power
  circuit to provide the necessary protection.
• The power cable supplied with your product includes a drain wire,
  which must be connected to the vessel’s common RF ground.

        Description

 1      Positive (+) bar
 2      Negative (-) bar

 3      Circuit breaker
 4      Waterproof fuse holder containing a suitably-rated inline fuse
        must be fitted. For suitable fuse rating, refer to: Inline fuse
        and thermal breaker ratings.

 Important:
 Observe the recommended fuse / breaker ratings provided in the
 product’s documentation, however be aware that the suitable fuse
 / breaker rating is dependent on the number of devices being
 connected.

Implementation — direct connection to battery

• Where connection to a power distribution panel is not possible,
  the power cable supplied with your product may be connected
  directly to the vessel's battery, via a suitably rated fuse or breaker.
• If the power cable is NOT supplied with a fitted inline fuse, you
  MUST fit a suitably rated fuse or breaker between the red wire
  and the battery’s positive terminal.
• Refer to the inline fuse ratings provided in the product’s
  documentation.
• If you need to extend the length of the power cable supplied with
  your product, ensure you observe the dedicated Power cable
  extensions advice provided in the product’s documentation.

<!-- figure 1 on pdf page 48 at 334,190-607,350 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 36) -->
3°=
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 48 at 38,254-314,442 pt | caption: none | text-layer labels: Description | nearby labels: 1 | Positive (+) bar | 2 | Negative (-) bar | OCR text follows (tesseract, unverified; 3/6 words >= 60, mean confidence 55) -->
2?
4
4?
<!-- end of figure 2 -->

<!-- pdf page 49 | printed page 49 | header: Description | footer: Non-PoE power connections -->

        Description

 1      Waterproof fuse holder containing a suitably-rated inline fuse
        must be fitted. For suitable fuse rating, refer to: Inline fuse
        and thermal breaker ratings.
 2      Product power cable.
 3      Drain wire connection point.

Battery connection scenario A:
Suitable for a vessel with a common RF ground point. In this
scenario, the power cable’s drain wire should be connected to the
vessel’s common ground point.
Battery connection scenario B:
Suitable for a vessel without a common grounding point. In this
case, the power cable’s drain wire should be connected directly to
the battery’s negative terminal.

Grounding
Ensure that you observe any additional grounding advice provided
in the product’s documentation.

More information
It is recommended that best practice is observed in all vessel
electrical installations, as detailed in the following standards:
• BMEA Code of Practice for Electrical and Electronic Installations
  in Boats
• NMEA 0400 Installation Standard
• ISO 13297: Small craft — Electrical systems — Alternating and
  direct current installations
• ISO 10133: Small craft — Electrical systems — Extra-low-voltage
  d.c. installations
• ABYC E-11 AC & DC Electrical Systems on Boats
• ABYC A-31 Battery chargers and Inverters
• ABYC TE-4 Lightning Protection

12.6 Power cable extension (12 / 24 V
systems)
If you need to extend the length of the power cable supplied with
your product, ensure you observe the following advice:
• The power cable for each unit in your system should be run as
  a separate, single length of 2-wire cable from the unit to the
  vessel's battery or distribution panel.
• Ensure that the extension cable is of a sufficient gauge for the
  supply voltage, the total current load of the device, and the
  length of the cable run — as the cable run length increases, the
  greater the voltage drop will be from one end of the power cable
  to the other.
• Refer to the following table for typical minimum power cable
  wire gauges:

 Cable length in       Wire gauge in AWG         Wire gauge in AWG
 meters (feet)         (mm2) for 12 V supply     (mm2) for 24 V supply

 <8 (<25)              16 (1.31 mm2)             18 (0.82 mm2)
 16 (50)               14 (2.08 mm2)             16 (1.31 mm2)
 24 (75)               12 (3.31 mm2)             14 (2.08 mm2)

 >32 (>100)            10 (5.26 mm2)             12 (3.31 mm2)

 Important:
 Be aware that some products in your system (such as sonar modules)
 can create voltage peaks at certain times, which may impact the
 voltage available to other products during the peaks.

 Important:
 To ensure power cables (including any extension) are of a sufficient
 gauge, ensure that there is a continuous minimum voltage of
 10.8 V dc at the end of the cable where it enters the product’s power
 connector, even with a fully flat battery at 11 V dc. (Do not assume
 that a flat battery is at 0 V dc. Due to the discharge profile and
 internal chemistry of batteries, the current drops much faster than
 the voltage. A “fully flat” battery still shows a positive voltage, even
 if it doesn’t have enough current to power your device.)

<!-- pdf page 50 | printed page 50 -->

12.7 Power cable drain wire
connection
The power cable supplied with this product includes a dedicated
drain wire for connection to a vessel's Radio Frequency (RF) ground
point (if available), or the negative battery terminal.
The purpose of the drain wire is to drain excess voltage from the
cable shield, giving it a path to safety. The drain wire protects the
cable's inner signal conductors from electrical noise emitted by
other cables and devices.
Although the drain wire is not intended to ground the product's
internal circuits, it's important that the drain wire is connected to
the vessel’s common RF ground point, which should be used for
all equipment in your system. If several items require grounding,
the drain wires and dedicated ground connections (if available)
of all equipment should first be connected to a single local point
(e.g. within a distribution panel), and then this point connected
via an appropriately-rated conductor to the vessel's RF common
ground point. An RF ground point is typically a circuit with a very
low-impedance signal at Radio Frequency, connected to the sea via
an electrode immersed in the sea, or bonded to the inner side of
the hull in an area that is underwater.
On vessels without an RF ground system, the drain wires and
dedicated ground connections (if available) of all equipment should
be connected directly to the vessel’s negative battery terminal.
The dc power system should be either:
• Negative grounded (“bonded”), with the negative battery
  terminal connected to the vessel's RF ground.
• Floating, with neither battery terminal connected to the vessel's
  ground.
The preferred minimum requirement for the path to ground
(bonded or non-bonded) is via a flat tinned copper braid, with a
30 A rating or greater. If this is not possible, an equivalent stranded
wire conductor may be used, rated as follows:
• for runs of <1 m (3.3 ft), use 6 mm2 (10 AWG) or greater.
• for runs of >1 m (3.3 ft), use 8 mm2 (8 AWG) or greater.
In any grounding system, always keep the length of connecting
braid or wires as short as possible.

<!-- pdf page 51 | printed page 51 | header: CHAPTER 13: OPERATION (M460-SERIES / M560-SERIES) | footer: Operation (M460-Series / M560-Series) -->

CHAPTER CONTENTS

•   13.1 Controls overview — page 52
•   13.2 Powering on the unit — page 53
•   13.3 Startup wizard — page 53
•   13.4 Camera detection — page 55
•   13.5 Controlled camera — page 55
•   13.6 Main menu — page 56
•   13.7 JCU settings — page 58

<!-- pdf page 52 | printed page 52 | header: 13.1 Controls overview / Description -->

Applicability: M460-Series / M560-Series
The JCU-4 buttons and their associated functions (while controlling
an M460-Series / M560-Series camera) are described below.

       Description

 1     [Power]
       • With the JCU-4 powered off, press to power the unit on.
       • With the JCU-4 powered on, press to display the [Main
         menu] screen.
       • With the [Main menu] screen displayed, press to access
         the [Brightness] screen.
       • With the [Brightness] screen displayed, press to
         increase the JCU-4’s brightness by 20%.
       • With the JCU-4 powered on, press and hold to power
         the unit off.
 2     [On-screen Display]
       • (1) Press to show / hide the camera’s [On-screen Display]
         menu on a networked video display or the camera’s
         Web browser configuration interface.

3    [Park]
     • (1) Press to park the camera.
4    [Softkey 1, Softkey 2, Softkey 3]
     • Press to initiate the corresponding action displayed
       on-screen.
5    [Back]
     • With a (sub)menu displayed, press to return back to the
       previous screen.
6    [Select]
     • With a (sub)menu displayed, press to select the
       highlighted item.
7    [IR Color]
     • Press to cycle between infrared color palettes on the
       camera’s thermal video feed.
     • Press and hold to invert the infrared color palette
       displayed on the camera’s thermal video feed.
     • Press and hold, then hold the joystick upward to display
       the JCU-4 and camera’s IP addresses.
8    [Home]
     • (1) Press to return the camera to the configured home
       position.
     • (1) Press and hold to save the current azimuth and
       elevation as the camera’s home position.
9    [IR Contrast]
     • Press to cycle between infrared contrast palettes on the
       camera’s thermal video feed.
     • Press and hold to display the [Camera focus] screen.
10   [Active feed switch]
     • Press to change which camera payload is being
       controlled by the JCU-4.
     • Press and hold to display the [Select camera] screen.

<!-- figure 1 on pdf page 52 at 38,91-314,293 pt | caption: none | text-layer labels: Description | nearby labels: Applicability: M460-Series / M560-Series | 3 | 4 | 5 | 6 | 7 | 1 | [Power] | 8 | OCR: no legible text (0/4 words >= 60, mean confidence 44) -->

<!-- pdf page 53 | printed page 53 | header: Description | footer: Operation (M460-Series / M560-Series) -->

 11      [Navigation pad]
         • Press to pan and tilt the camera.
         • With a (sub)menu displayed, press to change the
           highlighted menu option.
 12      [Video tracking]
         • Press to display the [Ready to Track] screen.
 13      [Joystick]
         • Twist to (un)zoom the camera’s active payload.
         • Push up / down to tilt the camera.
         • Push left or right to rotate the camera.
 14      [Reboot (over Ethernet)]
         • Press to reboot the JCU-4 (over Ethernet).

 Note:
 (1) For more information, refer to the documentation that is supplied
 with your compatible FLIR maritime camera:
 • (71010) M460-Series Thermal Camera Operation Instructions.
 • (71011) M560-Series Thermal Camera Operation Instructions.
 Please ensure that you obtain the latest version of your
 documentation via the FLIR website: www.bit.ly/3Seupv7

13.2 Powering on the unit
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 can be turned on by pressing the [Power] button.
After the [Power] button has been pressed, the following screen
will be displayed as your unit begins to power on:

13.3 Startup wizard
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If your unit is being switched on for the first time or if a factory
reset has just occurred, you will be required to configure your unit
via the startup wizard.

 Note:
 While proceeding through the startup wizard, the [Back] button can
 be selected at any time to return to the previous screen.

System selection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Select system] startup wizard screen, you will be prompted
to select the type of system that your JCU-4 is networked to.
The JCU-4 will be automatically assigned an IP address type
according to the system type that you have selected.

<!-- figure 1 on pdf page 53 at 334,29-607,139 pt | caption: none | text-layer labels: none | nearby labels: 13.3 Startup wizard | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 95) -->
Powering up...
<!-- end of figure 1 -->

<!-- pdf page 54 | printed page 54 | header: Note: -->

The following system options are available:

 System                  IP address type

 • [Raymarine]           Dynamic IP (DHCP):
                         DHCP (Dynamic Host Control Protocol) is
 • [Garmin]              used to automatically assign IP addresses
                         and other important IP-network parameters
 • [Simrad or B&G]       to devices on a network.
 • [Lowrance]
 • [Furuno]              Static IP:
                         Networks that do NOT use DHCP or link
 • [Other]               local IP addressing require a static IP
                         address to be permanently assigned to each
                         connected device.

If the system option that you have selected is listed above as
being assigned a dynamic IP address type, the startup wizard
will complete and you will be automatically redirected onto the
[Controlled camera] screen.
If the system option that you have selected is listed above as being
assigned a static IP address type, you will instead be redirected
onto the [Enter IP address] screen.

Assigning a static IP address
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a static IP address via the [Enter IP address] screen.

 Some IP networks require IP addresses to be within a specific range.
 When setting your IP address, ensure that it is within an allowed
 range as specified by your network administrator

 Note:
 IP addresses are self-allocated by certain Raymarine equipment
 in the following range: 198.18.0.32 to 198.18.3.254 (inclusive). On
 networks featuring Raymarine-branded IP devices, you must avoid
 placing any devices in this range using manual (static) IP addresses.

From the [Enter IP address] screen:
1. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
2. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
3. After you have entered a valid address, press the [Next] softkey
   button to proceed onto the [Enter netmask] screen.

Assigning a netmask
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a netmask via the [Enter netmask] screen.
From the [Enter netmask] screen:
1. Optionally, press the [Default] softkey button to change the
   address shown on-screen to ‘255.255.255.0’.
2. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
3. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
4. After you have entered a valid address, press the [Save] softkey
   button.

<!-- figure 1 on pdf page 54 at 38,29-314,142 pt | caption: none; nearest centred text below: "IP address type" | text-layer labels: none | nearby labels: System | IP address type | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
SELECT
SYSTEM
Furuno
Garmin
Simrad or B&G
<!-- end of figure 1 -->

<!-- pdf page 55 | printed page 55 | header: 13.4 Camera detection / Description | footer: Operation (M460-Series / M560-Series) -->

Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 will automatically attempt to search for compatible FLIR
maritime cameras on the network once every 30 seconds.

 Note:
 If a compatible camera is connected to your network and cannot
 be automatically detected by your unit after a prolonged period,
 refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

13.5 Controlled camera
Applicability: M460-Series / M560-Series
Once the start-up process has been completed, the following
[Controlled camera] screen will be displayed.

From the [Controlled camera] screen, the following key information
can be viewed and / or interacted with:

         Description

 1       [Camera name]
         Indicates the camera which is currently being controlled.
 2       [Status icons]
         Indicates which camera functions are currently enabled.
 3       [Active feed]
         Indicates which camera payload is currently being controlled.

 4      [Shortcut key 1]
        Corresponds to the shortcut action assigned via the [Shortcut
        keys] screen. Select the associated softkey button to initiate
        the assigned shortcut.
 5      [Shortcut key 2]
        Corresponds to the shortcut action assigned via the [Shortcut
        keys] screen. Select the associated softkey button to initiate
        the assigned shortcut.
 6      [Shortcut key 3]
        Corresponds to the shortcut action assigned via the [Shortcut
        keys] screen. Select the associated softkey button to initiate
        the assigned shortcut.

Status icons
Applicability: M460-Series / M560-Series
The following status icons can be monitored via the status area
located on the right side of the [Controlled cameras] screen:

 Icon             Description

                  [Target classifier tracking system — Tracking object]
                  Indicates that the camera’s target classifier tracking
                  system is tracking a detected object.

                  [NMEA tracking — Radar target (TTM)]
                  Indicates that Radar target (TTM) tracking is
                  enabled and that the camera’s field of view can be
                  directed by a selected radar target’s position.

                  [Spotlight ON]
                  Indicates that the camera’s spotlight is enabled

<!-- figure 1 on pdf page 55 at 38,240-314,353 pt | caption: none | text-layer labels: none | nearby labels: Applicability: M460-Series / M560-Series | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 80) -->
E70679
JR
Active Feed:
6
4
Camera
surveil
Flash
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 55 at 338,257-401,310 pt | caption: none | text-layer labels: none | nearby labels: Icon | OCR: no legible text (0/2 words >= 60, mean confidence 47) -->
<!-- figure 3 on pdf page 55 at 338,319-401,382 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 55 at 334,391-607,434 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 56 | printed page 56 -->

13.6 Main menu
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
While viewing the [Controlled camera] screen, you can press the
[Power] button to access the JCU-4’s [Main menu] screen.

With the [Main menu] screen displayed, the following options
are available:
 Option             Description

 [Select camera]    Select to change which camera is currently
                    being controlled by the JCU-4.

 [Power down]       Select to access power options for both the
                    JCU-4 and the camera which is currently being
                    controlled.
 [Brightness]       Select to adjust the JCU-4’s LCD brightness
                    / button illumination and to also enable or
                    disable [Night] mode.
 [Camera focus]     Select to adjust the focus of the camera which
                    is currently being controlled.
 [JCU settings]     Select to access further configurable JCU-4
                    settings.

Select camera
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can change which compatible FLIR maritime camera the JCU-4
is currently controlling via the [Select camera] screen.
The [Select camera] screen can be accessed by:

• Navigating to: [Controlled camera > Main menu > Select camera],
  OR;
• By press and holding the [Active feed switch] button.

If a camera which you wish to control is not displayed, ensure
that it has been selected via the [Cameras] configuration screen:
[Controlled camera > Main menu > JCU settings > Cameras].

Power down
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 and other compatible FLIR maritime cameras on your
network can be remotely set to standby and / or restarted via the
[Power down] screen.
The [Power down] screen can be accessed by navigating to:
[Controlled camera > Main menu > Power down].

With the [Power down] screen displayed, the following options
are available:
• [JCU standby] — Select to enter the JCU-4 into a standby state
  until operation is resumed.

<!-- figure 1 on pdf page 56 at 420,67-607,180 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 83) -->
Bow Camera
Engine Room
Cabin
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 56 at 38,91-314,204 pt | caption: none; nearest centred text below: "With the [Main menu] screen displayed, the following options are available:" | text-layer labels: none | nearby labels: Option | Description | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 70) -->
MAIN
MENU
Power down
Brightness
7 Camera Focus
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 56 at 420,317-607,430 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 94) -->
Camera Standby
Camera Restart
Svstem Standbv
<!-- end of figure 3 -->

<!-- pdf page 57 | printed page 57 | header: Night mode enabled / Night mode disabled | footer: Operation (M460-Series / M560-Series) -->

• [Camera standby] — Select to enter the controlled camera into to
  a standby state until operation is resumed.
• [Camera restart] — Select to restart the controlled camera.
• [System standby] — Select to enter both the JCU-4 and the
  controlled camera into a standby state until operation is resumed.

Brightness
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can adjust the JCU-4’s LCD brightness / button illumination and
also enable or disable [Night] mode via the [Brightness] screen.
The [Brightness] screen can be accessed by navigating to:
[Controlled camera > Main menu > Brightness].

With the [Brightness] screen displayed, the following options are
available:
• [Down] — Select to increase the LCD brightness and button
  illumination by 5%.
• [Night] — Select to either enable or disable [Night] mode.
• [Up] — Select to decrease the LCD brightness and button
  illumination by 5%.

Night mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4’s user interface and physical buttons can be configured
to use a red color palette intended for night time use by selecting
the [Night] mode option via the [Brightness] screen.

 Night mode enabled                  Night mode disabled

 Important:
 If you are using the [Night] mode color palette at night, be aware
 that your vision may be compromised when either disabling the
 [Night] mode or switching to a display screen with a higher level
 of brightness.

Camera focus
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
The controlled camera’s focus can be manually or automatically
adjusted via the [Camera focus] screen.
The [Camera focus] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Camera focus]
• Press and holding the [IR Contrast] button.

With the [Camera focus] screen displayed, the following options
are available:
• [Nearer] — Select to adjust the camera’s focus manually.
• [Auto] — Select to automatically adjust the camera’s focus.

<!-- figure 1 on pdf page 57 at 334,53-607,113 pt | caption: none | text-layer labels: none | nearby labels: Important: | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 75) -->
MAIN
MENU
Power down
Brightness
Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 57 at 38,192-314,305 pt | caption: none; nearest centred text below: "With the [Brightness] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 74) -->
BRIGHTNESS
Night
Down
Up
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 57 at 334,302-607,415 pt | caption: none; nearest centred text below: "With the [Camera focus] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 86) -->
MANUAL FOCUS
Further
Nearer
Auto
<!-- end of figure 3 -->

<!-- pdf page 58 | printed page 58 -->

• [Further] — Select to adjust the camera’s focus manually.

13.7 JCU settings
Applicability: M460-Series / M560-Series
Additional advanced settings can be accessed via the [JCU settings]
menu.
The [JCU settings] menu can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings].

With the [JCU settings] menu displayed, the following options
are available:
 Option              Description

 [Shortcut keys]     Select to configure which actions are assigned
                     to the JCU-4’s softkey buttons when viewing
                     the [Controlled camera] screen.
 [Joystick mode]     Select to configure which direction the camera
                     tilts when the joystick is moved up and down.
 [Cameras]           Select to configure which compatible FLIR
                     maritime cameras detected on the network can
                     be controlled by your JCU-4.
 [Installation]      Select to reconfigure the JCU-4’s IP network
                     parameters which were set during the startup
                     wizard.

 [About]             Select to display additional information related
                     to the JCU-4.
 [Settings reset]    Select to perform a settings reset.

 [Factory reset]     Select to perform a factory reset.

Shortcut keys
Applicability: M460-Series / M560-Series
You can assign different shortcut actions to the JCU-4’s softkey
buttons while controlling an M460-Series / M560-Series camera
via the [Shortcut keys] screen.
The [Shortcut keys] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Shortcut keys].

With the [Shortcut keys] screen displayed, selecting an assigned
action will enable you to reconfigure it to one of the following
options:

 Option              Description

 [BWC]

                      Note:
                      This option is not supported by
                      M460-Series / M560-Series cameras.

 [Camera]            Changes the camera which is being controlled
                     by the JCU-4 to the next available camera
                     (cycling in alphabetical order).

 [CTV]               (1) Enables / disables the camera’s [CTV] (Color
                     Thermal Vision) blending mode.
 [Defog]             (1) Enables / disables the camera’s visible light
                     [Defog] video filter mode.
 [FFC]               Initiates the camera’s configured [FFC] (Flat
                     Field Correction) mode. For more information,
                     refer to: Flat Field Correction (FFC)

<!-- figure 1 on pdf page 58 at 334,113-607,226 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
Configure shortcut keys:
Track
Focus
Range
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 58 at 38,144-314,250 pt | caption: none; nearest centred text below: "With the [JCU settings] menu displayed, the following options are available:" | text-layer labels: none | nearby labels: Option | Description | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
JCU
SET-UP
Joystick Mode
Cameras
Installation
<!-- end of figure 2 -->

<!-- pdf page 59 | printed page 59 | header: Description / Description / Option / Option | footer: Operation (M460-Series / M560-Series) -->

[Fire]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

[Flash]       Enables / disables the camera’s spotlight.
              When enabled, a flashing spotlight beam will
              appear at the center of the camera’s field of
              view and the JCU-4’s [Spotlight on] screen will
              be displayed.

[Focus]       Displays the JCU-4’s [Camera focus] screen,
              which can be used to manually or automatically
              adjust the controlled camera’s focus.
[Ice]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

[InstAlert]   (1) Enables / disables the camera’s [InstAlert]
              thermal imaging mode.
[Light]       Enables / disables the camera’s spotlight. When
              enabled, a continuous spotlight beam will
              appear at the center of the camera’s field of
              view and the JCU-4’s [Spotlight on] screen will
              be displayed.
[MSX]         (1) Enables / disables the camera’s [MSX]
              (Multi-Spectral Dynamic Imaging) blending
              mode.
(2) [Range]   Displays the JCU-4’s [Ready to Range] screen,
              which can be used to trigger the camera’s laser
              range finder (LRF). For more information, refer
              to: Ready to range
[RSD]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

 [Stab]              (1) Enables / disables the camera’s [Stabilization]
                     mode.

 [Surveil]           (1) Enables / disables the camera’s [Surveillance
                     scan] mode.

 [Track]             Displays the JCU-4’s [Ready to Track] screen,
                     which can be used to track an object detected by
                     the camera’s target classifier tracking system.
                     For more information, refer to: Ready to track
 [TTM]               (1) Enables / disables NMEA Radar target (TTM)
                     tracking for the camera.
 [None]              Removes the assigned action.

Any changes made will be reflected on the [Controlled camera]
screen.

 Note:
 • (1) For more information, refer to the documentation that is
 supplied with your compatible FLIR maritime camera:
 – (71010) M460-Series Thermal Camera Operation Instructions.
 – (71011) M560-Series Thermal Camera Operation Instructions.
 Please ensure that you obtain the latest version of your
 documentation via the FLIR website: www.bit.ly/3Seupv7
 • (2) This option is only available for camera variants which
 support a laser range finder (LRF).

Flat Field Correction (FFC)
Applicability: M460-Series / M560-Series
During an FFC calibration procedure, the camera uses a target
surface with a consistent temperature to measure, detect and
subsequently correct any potential issues experienced with the
camera’s thermal image.
An FFC calibration procedure can be initiated at any time via the
camera’s Web browser configuration interface, or a networked
Joystick Control Unit (JCU) if you perceive that the quality of your
camera’s thermal image has degraded.
The type of FFC calibration procedure that is performed by your
camera will vary depending on which [FFC] mode has been selected
on your camera's Web browser configuration interface.

<!-- figure 1 on pdf page 59 at 125,204-290,245 pt | caption: none; nearest centred text below: "(1) Enables / disables the camera’s [InstAlert]" | text-layer labels: Note: | nearby labels: thermal imaging mode. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 60 | printed page 60 -->

FFC modes
Applicability: M460-Series / M560-Series
For more information on the FFC modes that are available via
your camera’s Web browser configuration interface, refer to the
documentation that is supplied with your compatible FLIR maritime
camera:
• (71010) M460-Series Thermal Camera Operation Instructions.
• (71011) M560-Series Thermal Camera Operation Instructions.
Please ensure that you obtain the latest version of your
documentation via the FLIR website: www.bit.ly/3Seupv7
Spotlight on
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
Once your camera’s spotlight has been enabled, the JCU-4 will
automatically switch to display the [Spotlight on] screen.

With the [Spotlight on] screen displayed, the following options
are available:
• [Dismiss] — Select to return to the [Controlled camera] screen.
• [Turn off] — Select to disable the camera’s spotlight and return to
  the [Controlled camera] screen.
Ready to range
Applicability: M460-LRF (30 Hz) / M560-LRF (30 Hz)
You can trigger the camera’s laser range finder (LRF) to measure the
distance between the camera and a position located at the center of
the camera’s field of view via the JCU-4’s [Ready to range] screen.
The [Ready to range] screen can be accessed by first assigning
the [Range] shortcut action to a softkey button, and then selecting
[Range] via the [Controlled camera] screen. For more information
how to assign a shortcut action, refer to:

• p.58 — Shortcut keys

Once the [Ready to range] screen is displayed, center the camera’s
field of view on the position you wish to measure the distance to,
then press the [Range] softkey button to trigger the camera’s LRF.
Alternatively, you can return to the [Controlled camera] screen by
pressing the [Cancel] button.
After the distance has been successfully measured, a pop-up
containing LRF information will appear on a networked video
display. For more details, refer to the documentation that is
supplied with your camera:
• (71010) M460-Series Thermal Camera Operation Instructions.
• (71011) M560-Series Thermal Camera Operation Instructions.
Please ensure that you obtain the latest version of your
documentation via the FLIR website: www.bit.ly/3Seupv7

Ready to track
Applicability: M460-Series / M560-Series
You can track an object detected by the camera’s target classifier
tracking system via the JCU-4’s [Ready to track] screen.
The [Ready to Track] screen can be accessed by:
• Pressing the JCU-4’s [Video tracking] button. OR;
• Pressing the associated [Track] softkey button on the JCU-4’s
  [Controlled camera] screen (this method requires the [Track]
  shortcut function to be assigned to a softkey button via the
  [Shortcut keys] screen).
Once either of the above buttons have been pressed, a crosshair
will appear on the camera’s live video feed and the following
[Ready to Track] screen will be displayed on the JCU-4.

<!-- figure 1 on pdf page 60 at 334,43-607,156 pt | caption: none | text-layer labels: none | nearby labels: • p.58 — Shortcut keys | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
READY TO RANGE
Place crosshairs over object
and press Joystick button
Cancel
Range
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 60 at 38,204-314,317 pt | caption: none; nearest centred text below: "With the [Spotlight on] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/10 words >= 60, mean confidence 60) -->
SPOTLIGHT ON
Dismiss
Turn Off
<!-- end of figure 2 -->

<!-- pdf page 61 | printed page 61 | footer: Operation (M460-Series / M560-Series) -->

The crosshair shown on the live video feed can be moved to
highlight a detected object using:
• The JCU-4’s joystick. OR;
• The [Prev target] and [Next target] softkey buttons to cycle the
  crosshair’s position between detected objects.
Once the detected object that you wish to track is highlighted, press
the JCU-4’s [Track] softkey button or the [Video track] button once
again to initiate target tracking.

Joystick mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can configure the JCU-4’s up and down joystick inputs to either
tilt the camera in the same direction as the joystick or the opposite
direction via the [Joystick mode] screen.
The [Joystick mode] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Joystick mode].

With the [Joystick mode] screen displayed, the following options
are available:

• [Gaming] — Causes the camera to tilt upward when the joystick
  is pushed up and downward when the joystick is pushed down.
• [Pilot] — Causes the camera to tilt upward when the joystick is
  pushed down and downward when the joystick is pushed up.
The JCU-4 is set to [Gaming] mode by default.

Controllable cameras
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Cameras] screen you can select which compatible FLIR
maritime camera(s) on the network can be controlled by your
JCU-4.
The [Cameras] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > Cameras].

Once you have chosen the camera(s) that you wish to control using
the JCU-4 and have selected [Save], the chosen camera(s) will then
appear on the [Select camera] screen.

 Note:
 The list of controllable cameras will dynamically update if a camera
 is either connected to or disconnected from the network. If a
 compatible FLIR maritime camera is connected to your network and
 cannot be automatically detected by the JCU-4 after a prolonged
 period, refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

<!-- figure 1 on pdf page 61 at 38,29-314,142 pt | caption: none; nearest centred text below: "The crosshair shown on the live video feed can be moved to highlight a detected object using:" | text-layer labels: none | nearby labels: • The JCU-4’s joystick. OR; | OCR text follows (tesseract, unverified; 16/16 words >= 60, mean confidence 96) -->
READY TO TRACK
Select Tracking box target
and press Joystick button
Prev target
TRACK
Next target
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 61 at 334,209-607,317 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 74) -->
M364C
CAMERAS
SAVE
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 61 at 142,348-314,454 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 0) -->

<!-- pdf page 62 | printed page 62 -->

Installation
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
It is possible to reconfigure the settings which were selected during
the startup wizard at any time via the [Installation] screen.
The [Installation] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Installation].

With the [Installation] screen displayed, the following options are
available:
• [Select system] — Select to reconfigure the type of system that
  your JCU-4 is networked to.
• [IP Address type] — Select to reconfigure the assigned IP address
  type.
• (1) [IP Address] — Select to reconfigure the assigned static IP
  address and netmask.

 Note:
 (1) This menu option is only available if the JCU-4’s assigned IP
 address type is set to [Static IP].

About this device
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The [About] screen contains additional information related to the
JCU-4.
The [About] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > About].

The following range of information can be found on the [About]
screen:
• [Serial] — Provides the JCU-4’s serial number.
• [Software V] — Provides the software version number that the
  JCU-4 is currently running.
• [IP Address] — Provides the JCU-4’s IP address.
• [Hours] — Provides the number of hours that the JCU-4 has been
  in operation for this session.
• [Total hours] — Provides the total number of hours that the JCU-4
  has been in operation for.

Settings reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can reset the JCU-4’s configured user settings (excluding the
assigned IP network parameters) via the [Settings reset] screen.
The [Settings reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Settings reset].

<!-- figure 1 on pdf page 62 at 334,29-607,142 pt | caption: none; nearest centred text below: "The following range of information can be found on the [About] screen:" | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 92) -->
About JCU-4
Serial: AMOO01B
Software V: 2.0.12
IP Address: 198.18.7.71
Total Hours: 59.4
Hours: 0.1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 62 at 38,120-314,233 pt | caption: none; nearest centred text below: "With the [Installation] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
INSTALL
IP Address Type
IP Address
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 62 at 334,362-607,475 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Reset JCU-4 settings?
No
Yes
<!-- end of figure 3 -->

<!-- pdf page 63 | printed page 63 | header: With the [Settings reset] screen displayed, the following options are available: | footer: Operation (M460-Series / M560-Series) -->

• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4 has
  been reset to settings default, the unit will return back to the
  [Controlled camera] screen.

Factory reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If you wish to reset the JCU-4’s configured user settings (including
the assigned IP network parameters), or, if you are experiencing
problems with your JCU-4 which cannot be resolved using the
troubleshooting advice provided, you may need to reset the JCU-4
to factory default via the [Factory reset] screen.

 Note:
 If you are experiencing problems with your JCU-4 and have not yet
 followed the troubleshooting advice provided, refer to:
 • p.119 — System checks and troubleshooting

The [Factory reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Factory reset].

With the [Factory reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4
  has been reset to factory default, the startup wizard will be
  automatically displayed on-screen.

<!-- figure 1 on pdf page 63 at 46,293-314,406 pt | caption: none; nearest centred text below: "With the [Factory reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Reset JCU-4 to factory defaults?
No
Yes
<!-- end of figure 1 -->

<!-- pdf page 64 | printed page 64 | header: CHAPTER 14: OPERATION (M400-SERIES / M500-SERIES) -->

CHAPTER CONTENTS

•   14.1 Controls overview — page 65
•   14.2 Powering on the unit — page 66
•   14.3 Startup wizard — page 66
•   14.4 Camera detection — page 68
•   14.5 Controlled camera — page 68
•   14.6 Main menu — page 69
•   14.7 JCU settings — page 71
•   14.8 Ready to track — page 74
•   14.9 Spotlight on — page 74
•   14.10 User programmable buttons (UPBs) — page 75

<!-- pdf page 65 | printed page 65 | header: 14.1 Controls overview / Description | footer: Operation (M400-Series / M500-Series) -->

Applicability: M400-Series / M500-Series
The JCU-4 buttons and their associated functions (while controlling
an M400-Series / M500-Series camera) are described below.

       Description

 1     [Power]
       • With the JCU-4 powered off, press to power the unit on.
       • With the JCU-4 powered on, press to display the [Main
         menu] screen.
       • With the [Main menu] screen displayed, press to access
         the [Brightness] screen.
       • With the [Brightness] screen displayed, press to
         increase the JCU-4’s brightness by 20%.
       • With the JCU-4 powered on, press and hold to power
         the unit off.
 2     [On-screen Display]
       • (1) Press to show / hide the camera’s [On-screen Display]
         menu on a networked video display.

3   [Park]
    • (1) Press to park the camera.
4   [Softkey 1, Softkey 2, Softkey 3]
    • Press to initiate the corresponding action displayed
      on-screen.
    • With the [Controlled camera] screen displayed, press to
      initiate the corresponding [UPB 1 / UPB 2 / UPB 3] action
      assigned via your FLIR maritime camera’s Web browser
      user interface or [On-Screen Display] menu.
    • With the [Controlled camera] screen displayed,
      press and hold to show the on-screen display
      [User-programmable buttons] submenu on a networked
      video display.
5   [Back]
    • With a (sub)menu displayed, press to return back to the
      previous screen.
6   [Select]
    • With a (sub)menu displayed, press to select the
      highlighted item.
7   [IR Color]
    • Press to cycle between infrared color palettes on the
      camera’s thermal video feed.
    • Press and hold to invert the infrared color palette
      displayed on the camera’s thermal video feed.
    • Press and hold, then hold the joystick upward to display
      the JCU-4 and camera’s IP addresses.
8   [Home]
    • (1) Press to return the camera to the configured home
      position.
    • (1) Press and hold to save the current azimuth and
      elevation as the camera’s home position.

<!-- figure 1 on pdf page 65 at 38,91-314,293 pt | caption: none | text-layer labels: Description | nearby labels: Applicability: M400-Series / M500-Series | 3 | 4 | 5 | 6 | 1 | [Power] | 7 | OCR: no legible text (0/4 words >= 60, mean confidence 44) -->

<!-- pdf page 66 | printed page 66 | header: Description -->

        Description

9       [IR Contrast]
        • Press to cycle between infrared contrast palettes on the
          camera’s thermal video feed.
        • Press and hold to display the [Camera focus] screen.
10      [Active feed switch]
        • Press to change which camera payload is being
          controlled by the JCU-4.
        • Press and hold to display the [Select camera] screen.
11      [Navigation pad]
        • Press to pan and tilt the camera.
        • With a (sub)menu displayed, press to change the
          highlighted menu option.
12      [Video tracking]
        • (M400XR / M500-Series only) Press to display the
          [Ready to Track] screen.
13      [Joystick]
        • Twist to (un)zoom the camera’s active payload.
        • Push up / down to tilt the camera.
        • Push left or right to rotate the camera.
14      [Reboot (over Ethernet)]
        • Press to reboot the JCU-4 (over Ethernet).

Note:
(1) For more information, refer to the documentation that is supplied
with your compatible FLIR maritime camera:
• (432-0012-02-10) M400-Series Thermal Camera Operation
Instructions.
• (432-0012-01-10) M500-Series Thermal Camera Operation
Instructions.
Please ensure that you obtain the latest version of your
documentation via the FLIR website: www.marine.flir.com

14.2 Powering on the unit
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 can be turned on by pressing the [Power] button.
After the [Power] button has been pressed, the following screen
will be displayed as your unit begins to power on:

14.3 Startup wizard
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If your unit is being switched on for the first time or if a factory
reset has just occurred, you will be required to configure your unit
via the startup wizard.

 Note:
 While proceeding through the startup wizard, the [Back] button can
 be selected at any time to return to the previous screen.

System selection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Select system] startup wizard screen, you will be prompted
to select the type of system that your JCU-4 is networked to.
The JCU-4 will be automatically assigned an IP address type
according to the system type that you have selected.

<!-- figure 1 on pdf page 66 at 334,115-607,226 pt | caption: none | text-layer labels: none | nearby labels: 14.3 Startup wizard | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 94) -->
Powering up...
<!-- end of figure 1 -->

<!-- pdf page 67 | printed page 67 | header: Note: | footer: Operation (M400-Series / M500-Series) -->

The following system options are available:

 System                  IP address type

 • [Raymarine]           Dynamic IP (DHCP):
                         DHCP (Dynamic Host Control Protocol) is
 • [Garmin]              used to automatically assign IP addresses
                         and other important IP-network parameters
 • [Simrad or B&G]       to devices on a network.
 • [Lowrance]
 • [Furuno]              Static IP:
                         Networks that do NOT use DHCP or link
 • [Other]               local IP addressing require a static IP
                         address to be permanently assigned to each
                         connected device.

If the system option that you have selected is listed above as
being assigned a dynamic IP address type, the startup wizard
will complete and you will be automatically redirected onto the
[Controlled camera] screen.
If the system option that you have selected is listed above as being
assigned a static IP address type, you will instead be redirected
onto the [Enter IP address] screen.

Assigning a static IP address
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a static IP address via the [Enter IP address] screen.

 Some IP networks require IP addresses to be within a specific range.
 When setting your IP address, ensure that it is within an allowed
 range as specified by your network administrator

 Note:
 IP addresses are self-allocated by certain Raymarine equipment
 in the following range: 198.18.0.32 to 198.18.3.254 (inclusive). On
 networks featuring Raymarine-branded IP devices, you must avoid
 placing any devices in this range using manual (static) IP addresses.

From the [Enter IP address] screen:
1. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
2. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
3. After you have entered a valid address, press the [Next] softkey
   button to proceed onto the [Enter netmask] screen.

Assigning a netmask
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a netmask via the [Enter netmask] screen.
From the [Enter netmask] screen:
1. Optionally, press the [Default] softkey button to change the
   address shown on-screen to ‘255.255.255.0’.
2. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
3. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
4. After you have entered a valid address, press the [Save] softkey
   button.

<!-- figure 1 on pdf page 67 at 38,29-314,142 pt | caption: none; nearest centred text below: "IP address type" | text-layer labels: none | nearby labels: System | IP address type | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
SELECT
SYSTEM
Furuno
Garmin
Simrad or B&G
<!-- end of figure 1 -->

<!-- pdf page 68 | printed page 68 | header: 14.4 Camera detection / Description -->

Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 will automatically attempt to search for compatible FLIR
maritime cameras on the network once every 30 seconds.

 Note:
 If a compatible camera is connected to your network and cannot
 be automatically detected by your unit after a prolonged period,
 refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

14.5 Controlled camera
Applicability: M300-Series / M400-Series / M500-Series
Once the start-up process has been completed, the following
[Controlled camera] screen will be displayed.

From the [Controlled camera] screen, the following key information
can be viewed and / or interacted with:

         Description

 1       [Camera name]
         Indicates the camera which is currently being controlled.
 2       [Active feed]
         Indicates which camera payload is currently being controlled.

 3      [Status icons]
        Indicates which camera functions are currently enabled.
 4      [User programmable button (UPB 1 / UPB 2 / UPB 3)]
        Corresponds to the [UPB 1 / UPB 2 / UPB 3] action assigned
        on your FLIR maritime camera’s Web browser user interface
        or [On-Screen Display] menu. While viewing the [Controlled
        camera] screen:
        • Pressing the associated softkey button will initiate the
          assigned action.
        • Press and holding the associated softkey button will
          show the on-screen display [User-programmable
          buttons] submenu on a networked video display.

Status icons
Applicability: M400-Series / M500-Series
The following status icons can be monitored via the status area
located on the right side of the [Controlled cameras] screen:

 Icon             Description

                  (1) [Video tracking]
                  Indicates that the camera is video tracking a
                  detected target.

                  [NMEA tracking — Radar cursor (RSD)]
                  Indicates that Radar cursor (RSD) tracking is
                  enabled and that the camera’s field of view can be
                  directed by the radar display’s cursor.

                  [NMEA tracking — Next waypoint (BWC)]
                  Indicates that Next waypoint (RSD) tracking is
                  enabled and that the camera’s field of view can be
                  directed by a selected waypoint’s position.

<!-- figure 1 on pdf page 68 at 38,240-314,353 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 75) -->
M364C
Feed:
1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 68 at 338,264-401,317 pt | caption: none | text-layer labels: none | nearby labels: Icon | OCR: no legible text (0/2 words >= 60, mean confidence 51) -->
<!-- figure 3 on pdf page 68 at 338,326-401,389 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 68 at 338,398-401,466 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 69 | printed page 69 | header: Description | footer: Operation (M400-Series / M500-Series) -->

 Icon            Description

                 [NMEA tracking — Radar target (TTM)]
                 Indicates that Radar target (TTM) tracking is
                 enabled and that the camera’s field of view can be
                 directed by a selected radar target’s position.

                 [Spotlight ON]
                 Indicates that the camera’s spotlight is enabled

                 [Spotlight ON — Flashing]
                 Indicates that the camera’s spotlight is flashing

                 [Spotlight ON — SOS]
                 Indicates that the camera’s spotlight is flashing
                 SOS.

 Note:
 (1) This function is only supported by M400XR / M500-Series
 cameras.

14.6 Main menu
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
While viewing the [Controlled camera] screen, you can press the
[Power] button to access the JCU-4’s [Main menu] screen.

With the [Main menu] screen displayed, the following options
are available:

 Option              Description

 [Select camera]     Select to change which camera is currently
                     being controlled by the JCU-4.
 [Power down]        Select to access power options for both the
                     JCU-4 and the camera which is currently being
                     controlled.
 [Brightness]        Select to adjust the JCU-4’s LCD brightness
                     / button illumination and to also enable or
                     disable [Night] mode.

 [Camera focus]      Select to adjust the focus of the camera which
                     is currently being controlled.
 [JCU settings]      Select to access further configurable JCU-4
                     settings.

Select camera
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can change which compatible FLIR maritime camera the JCU-4
is currently controlling via the [Select camera] screen.
The [Select camera] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Select camera],
  OR;
• By press and holding the [Active feed switch] button.

<!-- figure 1 on pdf page 69 at 334,29-607,142 pt | caption: none; nearest centred text below: "With the [Main menu] screen displayed, the following options are available:" | text-layer labels: none | nearby labels: Option | Description | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 74) -->
MAIN
MENU
Power down
Brightness
7 Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 69 at 46,53-106,113 pt | caption: none | text-layer labels: none | nearby labels: Icon | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 69 at 41,218-312,262 pt | caption: none | text-layer labels: none | nearby labels: Note: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 70 | printed page 70 -->

If a camera which you wish to control is not displayed, ensure
that it has been selected via the [Cameras] configuration screen:
[Controlled camera > Main menu > JCU settings > Cameras].

Power down
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 and other compatible FLIR maritime cameras on your
network can be remotely set to standby and / or restarted via the
[Power down] screen.
The [Power down] screen can be accessed by navigating to:
[Controlled camera > Main menu > Power down].

With the [Power down] screen displayed, the following options
are available:
• [JCU standby] — Select to enter the JCU-4 into a standby state
  until operation is resumed.
• [Camera standby] — Select to enter the controlled camera into to
  a standby state until operation is resumed.
• [Camera restart] — Select to restart the controlled camera.

• [System standby] — Select to enter both the JCU-4 and the
  controlled camera into a standby state until operation is resumed.

Brightness
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can adjust the JCU-4’s LCD brightness / button illumination and
also enable or disable [Night] mode via the [Brightness] screen.
The [Brightness] screen can be accessed by navigating to:
[Controlled camera > Main menu > Brightness].

With the [Brightness] screen displayed, the following options are
available:
• [Down] — Select to increase the LCD brightness and button
  illumination by 5%.
• [Night] — Select to either enable or disable [Night] mode.
• [Up] — Select to decrease the LCD brightness and button
  illumination by 5%.

Night mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4’s user interface and physical buttons can be configured
to use a red color palette intended for night time use by selecting
the [Night] mode option via the [Brightness] screen.

<!-- figure 1 on pdf page 70 at 38,29-314,142 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 83) -->
Bow Camera
SELECT
CAMERA
Engine Room
Cabin
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 70 at 334,154-607,266 pt | caption: none; nearest centred text below: "With the [Brightness] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 74) -->
BRIGHTNESS
Night
Down
Up
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 70 at 38,278-314,391 pt | caption: none; nearest centred text below: "With the [Power down] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 88) -->
POWER
DOWN
Camera Standby
Camera Restart
Svstem Standbv
<!-- end of figure 3 -->

<!-- pdf page 71 | printed page 71 | header: Night mode enabled / Night mode disabled | footer: Operation (M400-Series / M500-Series) -->

 Night mode enabled                  Night mode disabled

 Important:
 If you are using the [Night] mode color palette at night, be aware
 that your vision may be compromised when either disabling the
 [Night] mode or switching to a display screen with a higher level
 of brightness.

Camera focus
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
The controlled camera’s focus can be manually or automatically
adjusted via the [Camera focus] screen.
The [Camera focus] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Camera focus]
• Press and holding the [IR Contrast] button.

With the [Camera focus] screen displayed, the following options
are available:
• [Nearer] — Select to adjust the camera’s focus manually.
• [Auto] — Select to automatically adjust the camera’s focus.
• [Further] — Select to adjust the camera’s focus manually.

14.7 JCU settings
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
Additional advanced settings can be accessed via the [JCU settings]
menu.
The [JCU settings] menu can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings].

With the [JCU settings] menu displayed, the following options
are available:

 Option              Description

 [Shortcut keys]

                      Note:
                      This menu option is only available
                      when the JCU-4 is controlling an
                      M460-Series / M560-Series camera.

 [Joystick mode]     Select to configure which direction the camera
                     tilts when the joystick is moved up and down.
 [Cameras]           Select to configure which compatible FLIR
                     maritime cameras detected on the network can
                     be controlled by your JCU-4.
 [Installation]      Select to reconfigure the JCU-4’s IP network
                     parameters which were set during the startup
                     wizard.

 [About]             Select to display additional information related
                     to the JCU-4.

<!-- figure 1 on pdf page 71 at 41,53-312,113 pt | caption: none | text-layer labels: none | nearby labels: Important: | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 86) -->
MAIN
MENU
Power down
Brightness
Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 71 at 334,118-607,230 pt | caption: none; nearest centred text below: "With the [JCU settings] menu displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/8 words >= 60, mean confidence 79) -->
JCU
SET-UP
Joystick Mode
Cameras
Installation
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 71 at 420,290-586,338 pt | caption: none | text-layer labels: Note: | nearby labels: Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 71 at 38,295-314,408 pt | caption: none; nearest centred text below: "With the [Camera focus] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 86) -->
MANUAL FOCUS
Further
Nearer
Auto
<!-- end of figure 4 -->

<!-- pdf page 72 | printed page 72 | header: Description / Option -->

 Option               Description

 [Settings reset]     Select to perform a settings reset.

 [Factory reset]      Select to perform a factory reset.

Shortcut keys
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series

 Note:
 This menu option is only available when the JCU-4 is controlling an
 M460-Series / M560-Series camera.

Joystick mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can configure the JCU-4’s up and down joystick inputs to either
tilt the camera in the same direction as the joystick or the opposite
direction via the [Joystick mode] screen.
The [Joystick mode] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Joystick mode].

With the [Joystick mode] screen displayed, the following options
are available:
• [Gaming] — Causes the camera to tilt upward when the joystick
  is pushed up and downward when the joystick is pushed down.
• [Pilot] — Causes the camera to tilt upward when the joystick is
  pushed down and downward when the joystick is pushed up.
The JCU-4 is set to [Gaming] mode by default.

Controllable cameras
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Cameras] screen you can select which compatible FLIR
maritime camera(s) on the network can be controlled by your
JCU-4.
The [Cameras] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > Cameras].

Once you have chosen the camera(s) that you wish to control using
the JCU-4 and have selected [Save], the chosen camera(s) will then
appear on the [Select camera] screen.

 Note:
 The list of controllable cameras will dynamically update if a camera
 is either connected to or disconnected from the network. If a
 compatible FLIR maritime camera is connected to your network and
 cannot be automatically detected by the JCU-4 after a prolonged
 period, refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

Installation
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
It is possible to reconfigure the settings which were selected during
the startup wizard at any time via the [Installation] screen.
The [Installation] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Installation].

<!-- figure 1 on pdf page 72 at 334,137-607,245 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 74) -->
M364C
CAMERAS
SAVE
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 72 at 38,283-314,389 pt | caption: none; nearest centred text below: "With the [Joystick mode] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 72) -->
Gaming
JOYSTICK
MODE
<!-- end of figure 2 -->

<!-- pdf page 73 | printed page 73 | footer: Operation (M400-Series / M500-Series) -->

With the [Installation] screen displayed, the following options are
available:
• [Select system] — Select to reconfigure the type of system that
  your JCU-4 is networked to.
• [IP Address type] — Select to reconfigure the assigned IP address
  type.
• (1) [IP Address] — Select to reconfigure the assigned static IP
  address and netmask.

 Note:
 (1) This menu option is only available if the JCU-4’s assigned IP
 address type is set to [Static IP].

About this device
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The [About] screen contains additional information related to the
JCU-4.
The [About] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > About].

The following range of information can be found on the [About]
screen:
• [Serial] — Provides the JCU-4’s serial number.
• [Software V] — Provides the software version number that the
  JCU-4 is currently running.
• [IP Address] — Provides the JCU-4’s IP address.
• [Hours] — Provides the number of hours that the JCU-4 has been
  in operation for this session.
• [Total hours] — Provides the total number of hours that the JCU-4
  has been in operation for.

Settings reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can reset the JCU-4’s configured user settings (excluding the
assigned IP network parameters) via the [Settings reset] screen.
The [Settings reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Settings reset].

<!-- figure 1 on pdf page 73 at 38,29-314,142 pt | caption: none; nearest centred text below: "With the [Installation] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
INSTALL
IP Address Type
IP Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 73 at 334,29-607,142 pt | caption: none; nearest centred text below: "The following range of information can be found on the [About] screen:" | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 92) -->
About JCU-4
Serial: AMOO01B
Software V: 2.0.12
IP Address: 198.18.7.71
Total Hours: 59.4
Hours: 0.1
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 73 at 334,362-607,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Reset JCU-4 settings?
No
Yes
<!-- end of figure 3 -->

<!-- pdf page 74 | printed page 74 | header: With the [Settings reset] screen displayed, the following options are available: -->

With the [Settings reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4 has
  been reset to settings default, the unit will return back to the
  [Controlled camera] screen.

Factory reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If you wish to reset the JCU-4’s configured user settings (including
the assigned IP network parameters), or, if you are experiencing
problems with your JCU-4 which cannot be resolved using the
troubleshooting advice provided, you may need to reset the JCU-4
to factory default via the [Factory reset] screen.

 Note:
 If you are experiencing problems with your JCU-4 and have not yet
 followed the troubleshooting advice provided, refer to:
 • p.119 — System checks and troubleshooting

The [Factory reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Factory reset].

With the [Factory reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4
  has been reset to factory default, the startup wizard will be
  automatically displayed on-screen.

14.8 Ready to track
Applicability: M400XR / M500-Series
You can track a target located within the camera’s field of view via
the JCU-4’s [Ready to track] screen.
The [Ready to Track] screen can be accessed by pressing the
JCU-4’s [Video tracking] button.
Once the [Video tracking] button has been pressed, a tracking
box will appear on the camera’s live video feed and the following
[Ready to Track] screen will be displayed on the JCU-4.

Manually center the tracking box over a target using the JCU-4’s
joystick.
Once the target that you wish to track is centered within the tracking
box, press the JCU-4’s [Track] softkey button or the [Video track]
button once again to initiate target tracking.

14.9 Spotlight on
Applicability: M400-Series / M460-Series / M500-Series /
M560-Series
Once your camera’s spotlight has been enabled, the JCU-4 will
automatically switch to display the [Spotlight on] screen.

<!-- figure 1 on pdf page 74 at 334,142-607,254 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 96) -->
READY TO TRACK
Place Tracking box over target
and press Joystick button
TRACK
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 74 at 46,293-314,406 pt | caption: none; nearest centred text below: "With the [Factory reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Reset JCU-4 to factory defaults?
No
Yes
<!-- end of figure 2 -->

<!-- pdf page 75 | printed page 75 | footer: Operation (M400-Series / M500-Series) -->

With the [Spotlight on] screen displayed, the following options
are available:
• [Dismiss] — Select to return to the [Controlled camera] screen.
• [Turn off] — Select to disable the camera’s spotlight and return to
  the [Controlled camera] screen.

14.10 User programmable buttons
(UPBs)
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
The JCU’s User-programmable buttons (UPBs) can be configured
from a compatible FLIR maritime camera’s Web browser user
interface and / or [On-Screen Display] menu.
You can assign a different action to each UPB (for example, ”Park”
or “Surveillance mode”) on a per-camera basis.

 Note:
 UPB assignments apply to individual cameras rather than specific
 JCU units. This means that, if you are using a single JCU unit to
 control 2 FLIR maritime cameras, UPB number 1 could be configured
 to initiate a different action on each camera.

Programming UPBs via the Web interface
Applicability: M100-Series / M200-Series / M400-Series /
M500-Series
To configure the JCU’s user-programmable buttons (UPBs) using an
M100-Series, M200-Series, M400-Series or M500-Series camera’s
Web browser user interface:

1. From the camera’s Web browser user interface, select [Setup]
   on the top menu.
   The [Setup] menu is displayed.
2. From the left-hand panel, select [JCU].
   The [UPB Configuration] panel is displayed:

3. From the [UPB Button] list, select the button you wish to
   configure.
4. From the [UPB Action] list, choose the camera action you wish
   to associate with that UPB button.
5. Repeat steps 3 and 4 for each UPB you wish to configure.
6. Click [Set] to save the UPB Configuration.

Programming UPBs via the On-Screen Display
(OSD) menu
Applicability: M300-Series / M400-Series / M500-Series
User-programmable buttons (UPBs) can also be assigned from the
On Screen Display (OSD) menu when connected to a video display.
To configure the UPBs using the camera’s [OSD] menu:
1. Press the [Menu] button.
   The [OSD] menu is displayed:

<!-- figure 1 on pdf page 75 at 38,29-314,142 pt | caption: none; nearest centred text below: "With the [Spotlight on] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/10 words >= 60, mean confidence 60) -->
SPOTLIGHT ON
Dismiss
Turn Off
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 75 at 346,89-607,276 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 26/31 words >= 60, mean confidence 81) -->
SFLIR
Live Video
Help
Setup
Maintenance
GEO Settings
UPB Button
UPB 1
Temperature
UPB Action
IR
Surveillance Mode
Pan and Tilt
Set
‘Surveillance
Advanced
Control
Status
<!-- end of figure 2 -->

<!-- pdf page 76 | printed page 76 -->

2. Scroll through the menu using the joystick, and select [Settings].
   The [Settings] menu is displayed.
3. Select [User Interface].
   The [User Interface] menu is displayed.
4. From the [UPB Button] list, select the button you wish to
   configure.
5. From the [UPB Action] list, choose the camera action you wish
   to associate with that UPB button.
6. Repeat steps 4 and 5 for each UPB you wish to configure.

<!-- figure 1 on pdf page 76 at 53,29-314,170 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 78) -->
Menu
J
Scene: Night
MVA
Surveillance
NMEA
Image
<!-- end of figure 1 -->

<!-- pdf page 77 | printed page 77 | footer: Operation (M300-Series) -->

CHAPTER 15: OPERATION (M300-SERIES)

CHAPTER CONTENTS

•   15.1 Controls overview — page 78
•   15.2 Powering on the unit — page 79
•   15.3 Startup wizard — page 79
•   15.4 Camera detection — page 81
•   15.5 Controlled camera — page 81
•   15.6 Main menu — page 82
•   15.7 JCU settings — page 83
•   15.8 User programmable buttons (UPBs) — page 87

<!-- pdf page 78 | printed page 78 | header: 15.1 Controls overview / Description -->

Applicability: M300-Series
The JCU-4 buttons and their associated functions (while controlling
an M300-Series camera) are described below.

       Description

 1     [Power]
       • With the JCU-4 powered off, press to power the unit on.
       • With the JCU-4 powered on, press to display the [Main
         menu] screen.
       • With the [Main menu] screen displayed, press to access
         the [Brightness] screen.
       • With the [Brightness] screen displayed, press to
         increase the JCU-4’s brightness by 20%.
       • With the JCU-4 powered on, press and hold to power
         the unit off.
 2     [On-screen Display]
       • (1) Press to show / hide the camera’s [On-screen Display]
         menu on a networked video display.

3   [Park]
    • (1) Press to park the camera.
4   [Softkey 1, Softkey 2, Softkey 3]
    • Press to initiate the corresponding action displayed
      on-screen.
    • With the [Controlled camera] screen displayed, press to
      initiate the corresponding [UPB 1 / UPB 2 / UPB 3] action
      assigned via your FLIR maritime camera’s Web browser
      user interface or [On-Screen Display] menu.
    • With the [Controlled camera] screen displayed,
      press and hold to show the on-screen display
      [User-programmable buttons] submenu on a networked
      video display.
5   [Back]
    • With a (sub)menu displayed, press to return back to the
      previous screen.
6   [Select]
    • With a (sub)menu displayed, press to select the
      highlighted item.
7   [IR Color]
    • Press to cycle between infrared color palettes on the
      camera’s thermal video feed.
    • Press and hold to invert the infrared color palette
      displayed on the camera’s thermal video feed.
    • Press and hold, then hold the joystick upward to display
      the JCU-4 and camera’s IP addresses.
8   [Home]
    • (1) Press to return the camera to the configured home
      position.
    • (1) Press and hold to save the current azimuth and
      elevation as the camera’s home position.

<!-- figure 1 on pdf page 78 at 38,91-314,293 pt | caption: none | text-layer labels: Description | nearby labels: Applicability: M300-Series | 3 | 4 | 5 | 6 | 1 | [Power] | 7 | OCR: no legible text (0/4 words >= 60, mean confidence 44) -->

<!-- pdf page 79 | printed page 79 | header: Description | footer: Operation (M300-Series) -->

        Description

9       [IR Contrast]
        • Press to cycle between infrared contrast palettes on the
          camera’s thermal video feed.
10      [Active feed switch]
        • (Multi-payload cameras only) Press to change which
          camera payload is being controlled by the JCU-4.
        • Press and hold to display the [Select camera] screen.
11      [Navigation pad]
        • Press to pan and tilt the camera.
        • With a (sub)menu displayed, press to change the
          highlighted menu option.
12      [Video tracking]

         Note:
         The function(s) associated with this button are not
         supported by M300-Series cameras.

13      [Joystick]
        • Twist to (un)zoom the camera’s active payload.
        • Push up / down to tilt the camera.
        • Push left or right to rotate the camera.
14      [Reboot (over Ethernet)]
        • Press to reboot the JCU-4 (over Ethernet).

Note:
(1) For more information, refer to the documentation that is supplied
with your compatible FLIR maritime camera:
• (71004) M300-Series Thermal Camera Installation and
Operation Instructions.
Please ensure that you obtain the latest version of your
documentation via the FLIR website: www.bit.ly/m300-docs

15.2 Powering on the unit
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 can be turned on by pressing the [Power] button.
After the [Power] button has been pressed, the following screen
will be displayed as your unit begins to power on:

15.3 Startup wizard
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If your unit is being switched on for the first time or if a factory
reset has just occurred, you will be required to configure your unit
via the startup wizard.

 Note:
 While proceeding through the startup wizard, the [Back] button can
 be selected at any time to return to the previous screen.

System selection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Select system] startup wizard screen, you will be prompted
to select the type of system that your JCU-4 is networked to.
The JCU-4 will be automatically assigned an IP address type
according to the system type that you have selected.

<!-- figure 1 on pdf page 79 at 334,115-607,226 pt | caption: none | text-layer labels: none | nearby labels: 15.3 Startup wizard | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 94) -->
Powering up...
<!-- end of figure 1 -->

<!-- pdf page 80 | printed page 80 | header: Note: -->

The following system options are available:

 System                  IP address type

 • [Raymarine]           Dynamic IP (DHCP):
                         DHCP (Dynamic Host Control Protocol) is
 • [Garmin]              used to automatically assign IP addresses
                         and other important IP-network parameters
 • [Simrad or B&G]       to devices on a network.
 • [Lowrance]
 • [Furuno]              Static IP:
                         Networks that do NOT use DHCP or link
 • [Other]               local IP addressing require a static IP
                         address to be permanently assigned to each
                         connected device.

If the system option that you have selected is listed above as
being assigned a dynamic IP address type, the startup wizard
will complete and you will be automatically redirected onto the
[Controlled camera] screen.
If the system option that you have selected is listed above as being
assigned a static IP address type, you will instead be redirected
onto the [Enter IP address] screen.

Assigning a static IP address
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a static IP address via the [Enter IP address] screen.

 Some IP networks require IP addresses to be within a specific range.
 When setting your IP address, ensure that it is within an allowed
 range as specified by your network administrator

 Note:
 IP addresses are self-allocated by certain Raymarine equipment
 in the following range: 198.18.0.32 to 198.18.3.254 (inclusive). On
 networks featuring Raymarine-branded IP devices, you must avoid
 placing any devices in this range using manual (static) IP addresses.

From the [Enter IP address] screen:
1. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
2. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
3. After you have entered a valid address, press the [Next] softkey
   button to proceed onto the [Enter netmask] screen.

Assigning a netmask
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a netmask via the [Enter netmask] screen.
From the [Enter netmask] screen:
1. Optionally, press the [Default] softkey button to change the
   address shown on-screen to ‘255.255.255.0’.
2. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
3. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
4. After you have entered a valid address, press the [Save] softkey
   button.

<!-- figure 1 on pdf page 80 at 38,29-314,142 pt | caption: none; nearest centred text below: "IP address type" | text-layer labels: none | nearby labels: System | IP address type | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
SELECT
SYSTEM
Furuno
Garmin
Simrad or B&G
<!-- end of figure 1 -->

<!-- pdf page 81 | printed page 81 | header: 15.4 Camera detection / Description | footer: Operation (M300-Series) -->

Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 will automatically attempt to search for compatible FLIR
maritime cameras on the network once every 30 seconds.

 Note:
 If a compatible camera is connected to your network and cannot
 be automatically detected by your unit after a prolonged period,
 refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

15.5 Controlled camera
Applicability: M300-Series / M400-Series / M500-Series
Once the start-up process has been completed, the following
[Controlled camera] screen will be displayed.

From the [Controlled camera] screen, the following key information
can be viewed and / or interacted with:

         Description

 1       [Camera name]
         Indicates the camera which is currently being controlled.
 2       [Active feed]
         Indicates which camera payload is currently being controlled.

 3      [Status icons]
        Indicates which camera functions are currently enabled.
 4      [User programmable button (UPB 1 / UPB 2 / UPB 3)]
        Corresponds to the [UPB 1 / UPB 2 / UPB 3] action assigned
        on your FLIR maritime camera’s Web browser user interface
        or [On-Screen Display] menu. While viewing the [Controlled
        camera] screen:
        • Pressing the associated softkey button will initiate the
          assigned action.
        • Press and holding the associated softkey button will
          show the on-screen display [User-programmable
          buttons] submenu on a networked video display.

Status icons
Applicability: M300-Series
The following status icons can be monitored via the status area
located on the right side of the [Controlled cameras] screen:
 Icon             Description

                  [NMEA tracking — Radar cursor (RSD)]
                  Indicates that Radar cursor (RSD) tracking is
                  enabled and that the camera’s field of view can be
                  directed by the radar display’s cursor.

                  [NMEA tracking — Next waypoint (BWC)]
                  Indicates that Next waypoint (RSD) tracking is
                  enabled and that the camera’s field of view can be
                  directed by a selected waypoint’s position.

                  [NMEA tracking — Radar target (TTM)]
                  Indicates that Radar target (TTM) tracking is
                  enabled and that the camera’s field of view can be
                  directed by a selected radar target’s position.

<!-- figure 1 on pdf page 81 at 38,240-314,353 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 75) -->
M364C
Feed:
1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 81 at 338,257-401,319 pt | caption: none | text-layer labels: none | nearby labels: Icon | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 81 at 338,329-401,398 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 81 at 334,408-607,482 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 82 | printed page 82 -->

15.6 Main menu
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series
While viewing the [Controlled camera] screen, you can press the
[Power] button to access the JCU-4’s [Main menu] screen.

With the [Main menu] screen displayed, the following options
are available:

 Option             Description

 [Select camera]    Select to change the which camera is currently
                    being controlled by the JCU-4.
 [Power down]       Select to access power options for both the
                    JCU-4 and the camera which is currently being
                    controlled.

 [Brightness]       Select to adjust the JCU-4’s LCD brightness
                    / button illumination and to also enable or
                    disable [Night] mode.
 [Camera focus]

                      Note:
                      This function is only supported
                      by M400-Series / M460-Series /
                      M500-Series / M560-Series cameras.

 [JCU settings]     Select to access further configurable JCU-4
                    settings.

Select camera
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can change which compatible FLIR maritime camera the JCU-4
is currently controlling via the [Select camera] screen.
The [Select camera] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Select camera],
  OR;
• By press and holding the [Active feed switch] button.

If a camera which you wish to control is not displayed, ensure
that it has been selected via the [Cameras] configuration screen:
[Controlled camera > Main menu > JCU settings > Cameras].

Power down
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 and other compatible FLIR maritime cameras on your
network can be remotely set to standby and / or restarted via the
[Power down] screen.
The [Power down] screen can be accessed by navigating to:
[Controlled camera > Main menu > Power down].

<!-- figure 1 on pdf page 82 at 38,94-314,206 pt | caption: none; nearest centred text below: "With the [Main menu] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 70) -->
MAIN
MENU
Power down
Brightness
7 Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 82 at 334,154-607,266 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 83) -->
Bow Camera
SELECT
CAMERA
Engine Room
Cabin
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 82 at 125,358-290,408 pt | caption: none | text-layer labels: Note: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 83 | printed page 83 | footer: Operation (M300-Series) -->

With the [Power down] screen displayed, the following options
are available:
• [JCU standby] — Select to enter the JCU-4 into a standby state
  until operation is resumed.
• [Camera standby] — Select to enter the controlled camera into to
  a standby state until operation is resumed.
• [Camera restart] — Select to restart the controlled camera.
• [System standby] — Select to enter both the JCU-4 and the
  controlled camera into a standby state until operation is resumed.

Brightness
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can adjust the JCU-4’s LCD brightness / button illumination and
also enable or disable [Night] mode via the [Brightness] screen.
The [Brightness] screen can be accessed by navigating to:
[Controlled camera > Main menu > Brightness].

With the [Brightness] screen displayed, the following options are
available:

• [Down] — Select to increase the LCD brightness and button
  illumination by 5%.
• [Night] — Select to either enable or disable [Night] mode.
• [Up] — Select to decrease the LCD brightness and button
  illumination by 5%.
Night mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4’s user interface and physical buttons can be configured
to use a red color palette intended for night time use by selecting
the [Night] mode option via the [Brightness] screen.
 Night mode enabled                  Night mode disabled

 Important:
 If you are using the [Night] mode color palette at night, be aware
 that your vision may be compromised when either disabling the
 [Night] mode or switching to a display screen with a higher level
 of brightness.

Camera focus
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series

 Note:
 This function is only supported by M400-Series / M460-Series /
 M500-Series / M560-Series cameras.

15.7 JCU settings
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
Additional advanced settings can be accessed via the [JCU settings]
menu.

<!-- figure 1 on pdf page 83 at 38,29-314,142 pt | caption: none; nearest centred text below: "With the [Power down] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 88) -->
POWER
DOWN
Camera Standby
Camera Restart
Svstem Standbv
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 83 at 334,190-607,250 pt | caption: none | text-layer labels: none | nearby labels: Night mode enabled | Night mode disabled | Important: | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 75) -->
MAIN
MENU
Power down
Brightness
Camera Focus
<!-- end of figure 2 -->

<!-- pdf page 84 | printed page 84 -->

The [JCU settings] menu can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings].

With the [JCU settings] menu displayed, the following options
are available:

 Option             Description

 [Shortcut keys]

                      Note:
                      This menu option is only available
                      when the JCU-4 is controlling an
                      M460-Series / M560-Series camera.

 [Joystick mode]    Select to configure which direction the camera
                    tilts when the joystick is moved up and down.
 [Cameras]          Select to configure which compatible FLIR
                    maritime cameras detected on the network can
                    be controlled by your JCU-4.
 [Installation]     Select to reconfigure the JCU-4’s IP network
                    parameters which were set during the startup
                    wizard.
 [About]            Select to display additional information related
                    to the JCU-4.

 [Settings reset]   Select to perform a settings reset.

 [Factory reset]    Select to perform a factory reset.

Shortcut keys
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series

 Note:
 This menu option is only available when the JCU-4 is controlling an
 M460-Series / M560-Series camera.

Joystick mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can configure the JCU-4’s up and down joystick inputs to either
tilt the camera in the same direction as the joystick or the opposite
direction via the [Joystick mode] screen.
The [Joystick mode] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Joystick mode].

With the [Joystick mode] screen displayed, the following options
are available:
• [Gaming] — Causes the camera to tilt upward when the joystick
  is pushed up and downward when the joystick is pushed down.
• [Pilot] — Causes the camera to tilt upward when the joystick is
  pushed down and downward when the joystick is pushed up.
The JCU-4 is set to [Gaming] mode by default.

<!-- figure 1 on pdf page 84 at 38,53-314,166 pt | caption: none; nearest centred text below: "With the [JCU settings] menu displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/8 words >= 60, mean confidence 79) -->
JCU
SET-UP
Joystick Mode
Cameras
Installation
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 84 at 125,226-290,274 pt | caption: none | text-layer labels: Note: | nearby labels: Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 84 at 334,235-607,341 pt | caption: none; nearest centred text below: "With the [Joystick mode] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 72) -->
Gaming
JOYSTICK
MODE
<!-- end of figure 3 -->

<!-- pdf page 85 | printed page 85 | footer: Operation (M300-Series) -->

Controllable cameras
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Cameras] screen you can select which compatible FLIR
maritime camera(s) on the network can be controlled by your
JCU-4.
The [Cameras] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > Cameras].

Once you have chosen the camera(s) that you wish to control using
the JCU-4 and have selected [Save], the chosen camera(s) will then
appear on the [Select camera] screen.

 Note:
 The list of controllable cameras will dynamically update if a camera
 is either connected to or disconnected from the network. If a
 compatible FLIR maritime camera is connected to your network and
 cannot be automatically detected by the JCU-4 after a prolonged
 period, refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

Installation
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
It is possible to reconfigure the settings which were selected during
the startup wizard at any time via the [Installation] screen.
The [Installation] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Installation].

With the [Installation] screen displayed, the following options are
available:
• [Select system] — Select to reconfigure the type of system that
  your JCU-4 is networked to.
• [IP Address type] — Select to reconfigure the assigned IP address
  type.
• (1) [IP Address] — Select to reconfigure the assigned static IP
  address and netmask.

 Note:
 (1) This menu option is only available if the JCU-4’s assigned IP
 address type is set to [Static IP].

About this device
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The [About] screen contains additional information related to the
JCU-4.
The [About] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > About].

<!-- figure 1 on pdf page 85 at 334,29-607,142 pt | caption: none; nearest centred text below: "With the [Installation] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
INSTALL
IP Address Type
IP Address
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 85 at 38,137-314,245 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 74) -->
M364C
CAMERAS
SAVE
<!-- end of figure 2 -->

<!-- pdf page 86 | printed page 86 | header: With the [Settings reset] screen displayed, the following options are available: -->

The following range of information can be found on the [About]
screen:
• [Serial] — Provides the JCU-4’s serial number.
• [Software V] — Provides the software version number that the
  JCU-4 is currently running.
• [IP Address] — Provides the JCU-4’s IP address.
• [Hours] — Provides the number of hours that the JCU-4 has been
  in operation for this session.
• [Total hours] — Provides the total number of hours that the JCU-4
  has been in operation for.

Settings reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can reset the JCU-4’s configured user settings (excluding the
assigned IP network parameters) via the [Settings reset] screen.
The [Settings reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Settings reset].

• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4 has
  been reset to settings default, the unit will return back to the
  [Controlled camera] screen.

Factory reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If you wish to reset the JCU-4’s configured user settings (including
the assigned IP network parameters), or, if you are experiencing
problems with your JCU-4 which cannot be resolved using the
troubleshooting advice provided, you may need to reset the JCU-4
to factory default via the [Factory reset] screen.

 Note:
 If you are experiencing problems with your JCU-4 and have not yet
 followed the troubleshooting advice provided, refer to:
 • p.119 — System checks and troubleshooting

The [Factory reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Factory reset].

With the [Factory reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4
  has been reset to factory default, the startup wizard will be
  automatically displayed on-screen.

<!-- figure 1 on pdf page 86 at 38,29-314,142 pt | caption: none; nearest centred text below: "The following range of information can be found on the [About] screen:" | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 92) -->
About JCU-4
Serial: AMOO01B
Software V: 2.0.12
IP Address: 198.18.7.71
Total Hours: 59.4
Hours: 0.1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 86 at 341,293-607,406 pt | caption: none; nearest centred text below: "With the [Factory reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Reset JCU-4 to factory defaults?
No
Yes
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 86 at 38,362-314,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Reset JCU-4 settings?
No
Yes
<!-- end of figure 3 -->

<!-- pdf page 87 | printed page 87 | footer: Operation (M300-Series) -->

15.8 User programmable buttons
(UPBs)
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
The JCU’s User-programmable buttons (UPBs) can be configured
from a compatible FLIR maritime camera’s Web browser user
interface and / or [On-Screen Display] menu.
You can assign a different action to each UPB (for example, ”Park”
or “Surveillance mode”) on a per-camera basis.

 Note:
 UPB assignments apply to individual cameras rather than specific
 JCU units. This means that, if you are using a single JCU unit to
 control 2 FLIR maritime cameras, UPB number 1 could be configured
 to initiate a different action on each camera.

Programming UPBs via the Web interface
Applicability: M300-Series
To configure the JCU’s user-programmable buttons (UPBs) using
an M300-Series camera’s Web browser user interface:
1. From the camera’s Web browser user interface, select [System
   Settings] at the bottom left of the menu.
   The camera’s settings page is displayed.
2. From the options displayed at the top, select [JCU].
   The [JCU] setting page is displayed:

3. From the [UPB Button] list, select the button you wish to
   configure.

4. From the [UPB Action] list, choose the camera action you wish
   to associate with that UPB button.
5. Repeat steps 3 and 4 for each UPB you wish to configure.
6. Select [Save] to save the UPB Configuration.

Programming UPBs via the On-Screen Display
(OSD) menu
Applicability: M300-Series / M400-Series / M500-Series
User-programmable buttons (UPBs) can also be assigned from the
On Screen Display (OSD) menu when connected to a video display.
To configure the UPBs using the camera’s [OSD] menu:
1. Press the [Menu] button.
   The [OSD] menu is displayed:

2. Scroll through the menu using the joystick, and select [Settings].
   The [Settings] menu is displayed.
3. Select [User Interface].
   The [User Interface] menu is displayed.
4. From the [UPB Button] list, select the button you wish to
   configure.
5. From the [UPB Action] list, choose the camera action you wish
   to associate with that UPB button.
6. Repeat steps 4 and 5 for each UPB you wish to configure.

<!-- figure 1 on pdf page 87 at 353,187-607,329 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/11 words >= 60, mean confidence 74) -->
Menu
Scene: Night
MVA
Surveillance
NMEA
Image.
<!-- end of figure 1 -->

<!-- pdf page 88 | printed page 88 | header: CHAPTER 16: OPERATION (M100-SERIES / M200-SERIES) -->

CHAPTER CONTENTS

•   16.1 Controls overview — page 89
•   16.2 Powering on the unit — page 90
•   16.3 Startup wizard — page 91
•   16.4 Camera detection — page 92
•   16.5 Controlled camera — page 92
•   16.6 Main menu — page 92
•   16.7 JCU settings — page 94
•   16.8 User programmable buttons (UPBs) — page 97

<!-- pdf page 89 | printed page 89 | header: 16.1 Controls overview / Description | footer: Operation (M100-Series / M200-Series) -->

Applicability: M100-Series / M200-Series
The JCU-4 buttons and their associated functions (while controlling
an M100-Series / M200-Series camera) are described below.

1   [Power]
    • With the JCU-4 powered off, press to power the unit on.
    • With the JCU-4 powered on, press to display the [Main
      menu] screen.
    • With the [Main menu] screen displayed, press to access
      the [Brightness] screen.
    • With the [Brightness] screen displayed, press to
      increase the JCU-4’s brightness by 20%.
    • With the JCU-4 powered on, press and hold to power
      the unit off.
2   [On-screen Display]

     Note:
     The function(s) associated with this button are not
     supported by M100-Series / M200-Series cameras.

3   [Park]
    • (1) Press to park the camera.
4   [Softkey 1, Softkey 2, Softkey 3]
    • Press to initiate the corresponding action displayed
      on-screen.
    • With the [Controlled camera] screen displayed, press
      to initiate the corresponding [UPB 1 / UPB 2 / UPB 3]
      action assigned via your FLIR maritime camera’s Web
      browser user interface.
5   [Back]
    • With a (sub)menu displayed, press to return back to the
      previous screen.
6   [Select]
    • With a (sub)menu displayed, press to select the
      highlighted item.

<!-- figure 1 on pdf page 89 at 38,91-314,271 pt | caption: none | text-layer labels: none | nearby labels: Applicability: M100-Series / M200-Series | 2 | 3 | 4 | OCR: no legible text (0/5 words >= 60, mean confidence 42) -->
<!-- figure 2 on pdf page 89 at 365,197-586,238 pt | caption: none | text-layer labels: Note: | nearby labels: 2 | [On-screen Display] | 3 | [Park] | • (1) Press to park the camera. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 90 | printed page 90 | header: Description / Description -->

7    [IR Color]
     • Press to cycle between infrared color palettes on the
       controlled camera’s thermal video feed.
     • Press and hold to invert the infrared color palette
       displayed on the controlled camera’s thermal video
       feed.
     • Press and hold, then hold the joystick upward to display
       the JCU-4 and camera’s IP addresses.
8    [Home]
     • (1) Press to return the camera to the configured home
       position.
     • (1) Press and hold to save the current azimuth and
       elevation as the camera’s home position.
9    [IR Contrast]
     • Press to cycle between infrared contrast palettes on the
       camera’s thermal video feed.
10   [Active feed switch]
     • Press and hold to display the [Select camera] screen.
11   [Navigation pad]
     • Press to pan and tilt the camera.
     • With a (sub)menu displayed, press to change the
       highlighted menu option.
12   [Video tracking]

      Note:
      The function(s) associated with this button are not
      supported by M100-Series / M200-Series cameras.

 13      [Joystick]
         • Twist to (un)zoom the camera’s thermal payload.
         • Push up / down to tilt the camera.
         • Push left or right to rotate the camera.
 14      [Reboot (over Ethernet)]
         • Press to reboot the JCU-4 (over Ethernet).

 Note:
 (1) For more information, refer to the documentation that is supplied
 with your compatible FLIR maritime camera:
 • (71001) M100-Series / M200-Series Thermal Camera Installation
 and Operation Instructions.
 Please ensure that you obtain the latest version of your
 documentation via the FLIR website: www.bit.ly/m100-m200-manual

16.2 Powering on the unit
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 can be turned on by pressing the [Power] button.
After the [Power] button has been pressed, the following screen
will be displayed as your unit begins to power on:

<!-- figure 1 on pdf page 90 at 334,343-607,454 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 95) -->
Powering up...
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 90 at 72,360-290,401 pt | caption: none | text-layer labels: Note: | nearby labels: 12 | [Video tracking] | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 91 | printed page 91 | footer: Operation (M100-Series / M200-Series) -->

16.3 Startup wizard
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If your unit is being switched on for the first time or if a factory
reset has just occurred, you will be required to configure your unit
via the startup wizard.

 Note:
 While proceeding through the startup wizard, the [Back] button can
 be selected at any time to return to the previous screen.

System selection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Select system] startup wizard screen, you will be prompted
to select the type of system that your JCU-4 is networked to.
The JCU-4 will be automatically assigned an IP address type
according to the system type that you have selected.

The following system options are available:

 System                   IP address type

 • [Raymarine]            Dynamic IP (DHCP):
                          DHCP (Dynamic Host Control Protocol) is
 • [Garmin]               used to automatically assign IP addresses
                          and other important IP-network parameters
 • [Simrad or B&G]        to devices on a network.
 • [Lowrance]
 • [Furuno]               Static IP:
                          Networks that do NOT use DHCP or link
 • [Other]                local IP addressing require a static IP
                          address to be permanently assigned to each
                          connected device.

If the system option that you have selected is listed above as
being assigned a dynamic IP address type, the startup wizard
will complete and you will be automatically redirected onto the
[Controlled camera] screen.
If the system option that you have selected is listed above as being
assigned a static IP address type, you will instead be redirected
onto the [Enter IP address] screen.

Assigning a static IP address
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a static IP address via the [Enter IP address] screen.

 Note:
 Some IP networks require IP addresses to be within a specific range.
 When setting your IP address, ensure that it is within an allowed
 range as specified by your network administrator

 Note:
 IP addresses are self-allocated by certain Raymarine equipment
 in the following range: 198.18.0.32 to 198.18.3.254 (inclusive). On
 networks featuring Raymarine-branded IP devices, you must avoid
 placing any devices in this range using manual (static) IP addresses.

From the [Enter IP address] screen:
1. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.

<!-- figure 1 on pdf page 91 at 38,266-314,379 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
SELECT
SYSTEM
Furuno
Garmin
Simrad or B&G
<!-- end of figure 1 -->

<!-- pdf page 92 | printed page 92 -->

2. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
3. After you have entered a valid address, press the [Next] softkey
   button to proceed onto the [Enter netmask] screen.

Assigning a netmask
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a netmask via the [Enter netmask] screen.
From the [Enter netmask] screen:
1. Optionally, press the [Default] softkey button to change the
   address shown on-screen to ‘255.255.255.0’.
2. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
3. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
4. After you have entered a valid address, press the [Save] softkey
   button.

16.4 Camera detection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 will automatically attempt to search for compatible FLIR
maritime cameras on the network once every 30 seconds.

 Note:
 If a compatible camera is connected to your network and cannot
 be automatically detected by your unit after a prolonged period,
 refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

16.5 Controlled camera
Applicability: M100-Series / M200-Series
Once the start-up process has been completed, the following
[Controlled camera] screen will be displayed.

From the [Controlled camera] screen, the following key information
can be viewed and / or interacted with:

       Description

 1     [Camera name]
       Indicates the camera which is currently being controlled.
 2     [Active feed]
       Indicates which camera payload is currently being controlled.
 3     [User programmable button (UPB 1 / UPB 2 / UPB 3)]
       Corresponds to the [UPB 1 / UPB 2 / UPB 3] action assigned
       on your FLIR maritime camera’s Web browser user interface.
       While viewing the [Controlled camera] screen:
       • Pressing the associated softkey button will initiate the
         assigned action.
       • Press and holding the associated softkey button will
         show the on-screen display [User-programmable
         buttons] submenu on a networked video display.

16.6 Main menu
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series
While viewing the [Controlled camera] screen, you can press the
[Power] button to access the JCU-4’s [Main menu] screen.

<!-- figure 1 on pdf page 92 at 334,29-607,139 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 86) -->
Bow Camera::
Feed:
3
1
3
<!-- end of figure 1 -->

<!-- pdf page 93 | printed page 93 | footer: Operation (M100-Series / M200-Series) -->

With the [Main menu] screen displayed, the following options
are available:
 Option             Description

 [Select camera]    Select to change the which camera is currently
                    being controlled by the JCU-4.
 [Power down]       Select to access power options for both the
                    JCU-4 and the camera which is currently being
                    controlled.

 [Brightness]       Select to adjust the JCU-4’s LCD brightness
                    / button illumination and to also enable or
                    disable [Night] mode.
 [Camera focus]

                     Note:
                     This function is only supported
                     by M400-Series / M460-Series /
                     M500-Series / M560-Series cameras.

 [JCU settings]     Select to access further configurable JCU-4
                    settings.

Select camera
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can change which compatible FLIR maritime camera the JCU-4
is currently controlling via the [Select camera] screen.
The [Select camera] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Select camera],
  OR;

• By press and holding the [Active feed switch] button.

If a camera which you wish to control is not displayed, ensure
that it has been selected via the [Cameras] configuration screen:
[Controlled camera > Main menu > JCU settings > Cameras].

Power down
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 and other compatible FLIR maritime cameras on your
network can be remotely set to standby and / or restarted via the
[Power down] screen.
The [Power down] screen can be accessed by navigating to:
[Controlled camera > Main menu > Power down].

With the [Power down] screen displayed, the following options
are available:
• [JCU standby] — Select to enter the JCU-4 into a standby state
  until operation is resumed.
• [Camera standby] — Select to enter the controlled camera into to
  a standby state until operation is resumed.

<!-- figure 1 on pdf page 93 at 38,29-314,142 pt | caption: none; nearest centred text below: "With the [Main menu] screen displayed, the following options are available:" | text-layer labels: none | nearby labels: Option | Description | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 70) -->
MAIN
MENU
Power down
Brightness
7 Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 93 at 420,43-607,156 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/6 words >= 60, mean confidence 87) -->
Bow Camera
Engine Room
Cabin
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 93 at 125,288-290,338 pt | caption: none | text-layer labels: Note: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 93 at 334,293-607,406 pt | caption: none; nearest centred text below: "With the [Power down] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 87) -->
POWER
DOWN
Camera Standby
Camera Restart
Svstem Standbv
<!-- end of figure 4 -->

<!-- pdf page 94 | printed page 94 | header: Night mode enabled / Night mode disabled -->

• [Camera restart] — Select to restart the controlled camera.
• [System standby] — Select to enter both the JCU-4 and the
  controlled camera into a standby state until operation is resumed.

Brightness
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can adjust the JCU-4’s LCD brightness / button illumination and
also enable or disable [Night] mode via the [Brightness] screen.
The [Brightness] screen can be accessed by navigating to:
[Controlled camera > Main menu > Brightness].

With the [Brightness] screen displayed, the following options are
available:
• [Down] — Select to increase the LCD brightness and button
  illumination by 5%.
• [Night] — Select to either enable or disable [Night] mode.
• [Up] — Select to decrease the LCD brightness and button
  illumination by 5%.

Night mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4’s user interface and physical buttons can be configured
to use a red color palette intended for night time use by selecting
the [Night] mode option via the [Brightness] screen.

 Night mode enabled                  Night mode disabled

 Important:
 If you are using the [Night] mode color palette at night, be aware
 that your vision may be compromised when either disabling the
 [Night] mode or switching to a display screen with a higher level
 of brightness.

Camera focus
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series

 Note:
 This function is only supported by M400-Series / M460-Series /
 M500-Series / M560-Series cameras.

16.7 JCU settings
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
Additional advanced settings can be accessed via the [JCU settings]
menu.
The [JCU settings] menu can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings].

<!-- figure 1 on pdf page 94 at 334,53-607,113 pt | caption: none | text-layer labels: none | nearby labels: Important: | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 75) -->
MAIN
MENU
Power down
Brightness
Camera Focus
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 94 at 38,170-314,281 pt | caption: none; nearest centred text below: "With the [Brightness] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 74) -->
BRIGHTNESS
Night
Down
Up
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 94 at 334,370-607,475 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/7 words >= 60, mean confidence 85) -->
JCU
SET-UP
Joystick Mode
Cameras
Installation
<!-- end of figure 3 -->

<!-- pdf page 95 | printed page 95 | footer: Operation (M100-Series / M200-Series) -->

With the [JCU settings] menu displayed, the following options
are available:
 Option               Description

 [Shortcut keys]

                       Note:
                       This menu option is only available
                       when the JCU-4 is controlling an
                       M460-Series / M560-Series camera.

 [Joystick mode]      Select to configure which direction the camera
                      tilts when the joystick is moved up and down.
 [Cameras]            Select to configure which compatible FLIR
                      maritime cameras detected on the network can
                      be controlled by your JCU-4.
 [Installation]       Select to reconfigure the JCU-4’s IP network
                      parameters which were set during the startup
                      wizard.
 [About]              Select to display additional information related
                      to the JCU-4.
 [Settings reset]     Select to perform a settings reset.

 [Factory reset]      Select to perform a factory reset.

Shortcut keys
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series

 Note:
 This menu option is only available when the JCU-4 is controlling an
 M460-Series / M560-Series camera.

Joystick mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can configure the JCU-4’s up and down joystick inputs to either
tilt the camera in the same direction as the joystick or the opposite
direction via the [Joystick mode] screen.
The [Joystick mode] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Joystick mode].

With the [Joystick mode] screen displayed, the following options
are available:
• [Gaming] — Causes the camera to tilt upward when the joystick
  is pushed up and downward when the joystick is pushed down.
• [Pilot] — Causes the camera to tilt upward when the joystick is
  pushed down and downward when the joystick is pushed up.
The JCU-4 is set to [Gaming] mode by default.

Controllable cameras
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Cameras] screen you can select which compatible FLIR
maritime camera(s) on the network can be controlled by your
JCU-4.
The [Cameras] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > Cameras].

Once you have chosen the camera(s) that you wish to control using
the JCU-4 and have selected [Save], the chosen camera(s) will then
appear on the [Select camera] screen.

<!-- figure 1 on pdf page 95 at 334,29-607,142 pt | caption: none; nearest centred text below: "With the [Joystick mode] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 64) -->
Gaming
JOYSTICK
MODE
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 95 at 125,86-290,134 pt | caption: none | text-layer labels: Note: | nearby labels: Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 95 at 434,338-600,394 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 96) -->
SAVE
<!-- end of figure 3 -->

<!-- pdf page 96 | printed page 96 | header: Note: -->

 Note:
 The list of controllable cameras will dynamically update if a camera
 is either connected to or disconnected from the network. If a
 compatible FLIR maritime camera is connected to your network and
 cannot be automatically detected by the JCU-4 after a prolonged
 period, refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

Installation
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
It is possible to reconfigure the settings which were selected during
the startup wizard at any time via the [Installation] screen.
The [Installation] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Installation].

With the [Installation] screen displayed, the following options are
available:
• [Select system] — Select to reconfigure the type of system that
  your JCU-4 is networked to.
• [IP Address type] — Select to reconfigure the assigned IP address
  type.
• (1) [IP Address] — Select to reconfigure the assigned static IP
  address and netmask.

 Note:
 (1) This menu option is only available if the JCU-4’s assigned IP
 address type is set to [Static IP].

About this device
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The [About] screen contains additional information related to the
JCU-4.
The [About] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > About].

The following range of information can be found on the [About]
screen:
• [Serial] — Provides the JCU-4’s serial number.
• [Software V] — Provides the software version number that the
  JCU-4 is currently running.
• [IP Address] — Provides the JCU-4’s IP address.
• [Hours] — Provides the number of hours that the JCU-4 has been
  in operation for this session.
• [Total hours] — Provides the total number of hours that the JCU-4
  has been in operation for.

Settings reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can reset the JCU-4’s configured user settings (excluding the
assigned IP network parameters) via the [Settings reset] screen.
The [Settings reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Settings reset].

<!-- figure 1 on pdf page 96 at 334,122-607,235 pt | caption: none; nearest centred text below: "The following range of information can be found on the [About] screen:" | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 92) -->
About JCU-4
Serial: AMOO01B
Software V: 2.0.12
IP Address: 198.18.7.71
Total Hours: 59.4
Hours: 0.1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 96 at 38,206-314,319 pt | caption: none; nearest centred text below: "With the [Installation] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
INSTALL
IP Address Type
IP Address
<!-- end of figure 2 -->

<!-- pdf page 97 | printed page 97 | footer: Operation (M100-Series / M200-Series) -->

With the [Settings reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4 has
  been reset to settings default, the unit will return back to the
  [Controlled camera] screen.

Factory reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If you wish to reset the JCU-4’s configured user settings (including
the assigned IP network parameters), or, if you are experiencing
problems with your JCU-4 which cannot be resolved using the
troubleshooting advice provided, you may need to reset the JCU-4
to factory default via the [Factory reset] screen.

 Note:
 If you are experiencing problems with your JCU-4 and have not yet
 followed the troubleshooting advice provided, refer to:
 • p.119 — System checks and troubleshooting

The [Factory reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Factory reset].

With the [Factory reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4
  has been reset to factory default, the startup wizard will be
  automatically displayed on-screen.

16.8 User programmable buttons
(UPBs)
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
The JCU’s User-programmable buttons (UPBs) can be configured
from a compatible FLIR maritime camera’s Web browser user
interface and / or [On-Screen Display] menu.
You can assign a different action to each UPB (for example, ”Park”
or “Surveillance mode”) on a per-camera basis.

 Note:
 UPB assignments apply to individual cameras rather than specific
 JCU units. This means that, if you are using a single JCU unit to
 control 2 FLIR maritime cameras, UPB number 1 could be configured
 to initiate a different action on each camera.

Programming UPBs via the Web interface
Applicability: M100-Series / M200-Series / M400-Series /
M500-Series
To configure the JCU’s user-programmable buttons (UPBs) using an
M100-Series, M200-Series, M400-Series or M500-Series camera’s
Web browser user interface:

<!-- figure 1 on pdf page 97 at 38,29-314,142 pt | caption: none; nearest centred text below: "With the [Settings reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Reset JCU-4 settings?
No
Yes
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 97 at 334,29-607,142 pt | caption: none; nearest centred text below: "With the [Factory reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Reset JCU-4 to factory defaults?
No
Yes
<!-- end of figure 2 -->

<!-- pdf page 98 | printed page 98 -->

1. From the camera’s Web browser user interface, select [Setup]
   on the top menu.
   The [Setup] menu is displayed.
2. From the left-hand panel, select [JCU].
   The [UPB Configuration] panel is displayed:

3. From the [UPB Button] list, select the button you wish to
   configure.
4. From the [UPB Action] list, choose the camera action you wish
   to associate with that UPB button.
5. Repeat steps 3 and 4 for each UPB you wish to configure.
6. Click [Set] to save the UPB Configuration.

<!-- figure 1 on pdf page 98 at 53,89-314,276 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 26/31 words >= 60, mean confidence 81) -->
SFLIR
Live Video
Help
Setup
Maintenance
GEO Settings
UPB Button
UPB 1
Temperature
UPB Action
IR
Surveillance Mode
Pan and Tilt
Set
‘Surveillance
Advanced
Control
Status
<!-- end of figure 1 -->

<!-- pdf page 99 | printed page 99 | footer: Operation (MD-Series) -->

CHAPTER 17: OPERATION (MD-SERIES)

CHAPTER CONTENTS

•   17.1 Controls overview — page 100
•   17.2 Powering on the unit — page 101
•   17.3 Startup wizard — page 101
•   17.4 Camera detection — page 103
•   17.5 Controlled camera — page 103
•   17.6 Main menu — page 103
•   17.7 JCU settings — page 105
•   17.8 User programmable buttons (UPBs) — page 108

<!-- pdf page 100 | printed page 100 | header: 17.1 Controls overview / Description -->

Applicability: MD-Series
The JCU-4 buttons and their associated functions (while controlling
an MD-Series camera) are described below.

       Description

 1     [Power]
       • With the JCU-4 powered off, press to power the unit on.
       • With the JCU-4 powered on, press to display the [Main
         menu] screen.
       • With the [Main menu] screen displayed, press to access
         the [Brightness] screen.
       • With the [Brightness] screen displayed, press to
         increase the JCU-4’s brightness by 20%.
       • With the JCU-4 powered on, press and hold to power
         the unit off.
 2     [On-screen Display]
       • (1) Press to show / hide the camera’s [On-screen Display]
         menu on a networked video display.

3   [Park]

     Note:
     The function(s) associated with this button are not
     supported by MD-Series cameras.

4   [Softkey 1, Softkey 2, Softkey 3]
    • Press to initiate the corresponding action displayed
      on-screen.
    • With the [Controlled camera] screen displayed, press
      the [Softkey 1] button to initiate the corresponding
      [User Programmable Button] action assigned via your
      camera’s [On-Screen Display] menu.
    • With the [Controlled camera] screen displayed, press
      and hold the [Softkey 1] button to display the camera’s
      [On-screen Display] menu on a networked video display.
    • With the [Controlled camera] screen displayed, press
      the [Softkey 2] button to initiate [Rear-view mode],
      which horizontally flips the camera’s video feed image.
5   [Back]
    • With a (sub)menu displayed, press to return back to the
      previous screen.
6   [Select]
    • With a (sub)menu displayed, press to select the
      highlighted item.
7   [IR Color]
    • Press to cycle between infrared color palettes on the
      camera’s thermal video feed.
    • Press and hold, then hold the joystick upward to display
      the JCU-4 and controlled camera’s IP addresses.
8   [Home]

     Note:
     The function(s) associated with this button are not
     supported by MD-Series cameras.

<!-- figure 1 on pdf page 100 at 365,67-586,108 pt | caption: none | text-layer labels: Note: | nearby labels: 3 | [Park] | 4 | [Softkey 1, Softkey 2, Softkey 3] | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 100 at 38,91-314,293 pt | caption: none | text-layer labels: Description | nearby labels: Applicability: MD-Series | 3 | 4 | 5 | 1 | [Power] | 6 | OCR: no legible text (0/4 words >= 60, mean confidence 44) -->
<!-- figure 3 on pdf page 100 at 365,430-586,470 pt | caption: none | text-layer labels: Note: | nearby labels: 8 | [Home] | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 101 | printed page 101 | header: Description | footer: Operation (MD-Series) -->

         Description

 9       [IR Contrast]
         • Press to cycle between infrared contrast palettes on the
           camera’s thermal video feed.
         • Press and hold to display the [Camera focus] screen.
 10      [Active feed switch]
         • Press and hold to display the [Select camera] screen.
 11      [Navigation pad]
         • With a (sub)menu displayed, press to change the
           highlighted menu option.
 12      [Video tracking]

          Note:
          The function(s) associated with this button are not
          supported by MD-Series cameras.

 13      [Joystick]
         • Twist to (un)zoom the camera’s thermal payload.
 14      [Reboot (over Ethernet)]
         • Press to reboot the JCU-4 (over Ethernet).

 Note:
 (1) For more information, refer to the documentation that is supplied
 with your compatible FLIR maritime camera:
 • (432-0010-00-10) MD-Series Thermal Camera Operation
 Instructions.
 Please ensure that you obtain the latest version of your
 documentation via the FLIR website: www.marine.flir.com

17.2 Powering on the unit
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 can be turned on by pressing the [Power] button.

After the [Power] button has been pressed, the following screen
will be displayed as your unit begins to power on:

17.3 Startup wizard
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If your unit is being switched on for the first time or if a factory
reset has just occurred, you will be required to configure your unit
via the startup wizard.

 Note:
 While proceeding through the startup wizard, the [Back] button can
 be selected at any time to return to the previous screen.

System selection
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Select system] startup wizard screen, you will be prompted
to select the type of system that your JCU-4 is networked to.
The JCU-4 will be automatically assigned an IP address type
according to the system type that you have selected.

<!-- figure 1 on pdf page 101 at 334,53-607,163 pt | caption: none | text-layer labels: none | nearby labels: 17.3 Startup wizard | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 95) -->
Powering up...
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 101 at 72,194-290,235 pt | caption: none | text-layer labels: Note: | nearby labels: 12 | [Video tracking] | 13 | [Joystick] | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 102 | printed page 102 | header: Note: -->

The following system options are available:

 System                  IP address type

 • [Raymarine]           Dynamic IP (DHCP):
                         DHCP (Dynamic Host Control Protocol) is
 • [Garmin]              used to automatically assign IP addresses
                         and other important IP-network parameters
 • [Simrad or B&G]       to devices on a network.
 • [Lowrance]
 • [Furuno]              Static IP:
                         Networks that do NOT use DHCP or link
 • [Other]               local IP addressing require a static IP
                         address to be permanently assigned to each
                         connected device.

If the system option that you have selected is listed above as
being assigned a dynamic IP address type, the startup wizard
will complete and you will be automatically redirected onto the
[Controlled camera] screen.
If the system option that you have selected is listed above as being
assigned a static IP address type, you will instead be redirected
onto the [Enter IP address] screen.

Assigning a static IP address
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a static IP address via the [Enter IP address] screen.

 Some IP networks require IP addresses to be within a specific range.
 When setting your IP address, ensure that it is within an allowed
 range as specified by your network administrator

 Note:
 IP addresses are self-allocated by certain Raymarine equipment
 in the following range: 198.18.0.32 to 198.18.3.254 (inclusive). On
 networks featuring Raymarine-branded IP devices, you must avoid
 placing any devices in this range using manual (static) IP addresses.

From the [Enter IP address] screen:
1. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
2. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
3. After you have entered a valid address, press the [Next] softkey
   button to proceed onto the [Enter netmask] screen.

Assigning a netmask
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The following steps provide instructions on how to assign the
JCU-4 a netmask via the [Enter netmask] screen.
From the [Enter netmask] screen:
1. Optionally, press the [Default] softkey button to change the
   address shown on-screen to ‘255.255.255.0’.
2. Use the [Navigation up] and [Navigation down] buttons to
   change the numerical value displayed in the highlighted field.
3. Once the value shown for the highlighted field is correct, use
   the [Navigation left] and [Navigation right] buttons to change
   which field is highlighted.
4. After you have entered a valid address, press the [Save] softkey
   button.

<!-- figure 1 on pdf page 102 at 38,29-314,142 pt | caption: none; nearest centred text below: "IP address type" | text-layer labels: none | nearby labels: System | IP address type | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 96) -->
SELECT
SYSTEM
Furuno
Garmin
Simrad or B&G
<!-- end of figure 1 -->

<!-- pdf page 103 | printed page 103 | header: 17.4 Camera detection / Description | footer: Operation (MD-Series) -->

Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 will automatically attempt to search for compatible FLIR
maritime cameras on the network once every 30 seconds.

 Note:
 If a compatible camera is connected to your network and cannot
 be automatically detected by your unit after a prolonged period,
 refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

17.5 Controlled camera
Applicability: MD-Series
Once the start-up process has been completed, the following
[Controlled camera] screen will be displayed.

From the [Controlled camera] screen, the following key information
can be viewed and / or interacted with:

         Description

 1       [Camera name]
         Indicates the camera which is currently being controlled.
 2       [Active feed]
         Indicates which camera payload is currently being controlled.

 3     [User programmable button (UPB)]
       Corresponds to the [User Programmable Button] action
       assigned via your MD-Series camera’s [On-Screen Display]
       menu. While viewing the [Controlled camera] screen:
       • Pressing the associated softkey button will initiate the
         assigned action.
       • Press and holding the associated softkey button will
         display the camera’s [On-Screen Display] menu on a
         networked video display.
 4     [Rear-view mode]
       Pressing the associated softkey button will horizontally flip
       the camera’s video feed image.
 5

        Note:
        This option is not supported by MD-Series cameras.

17.6 Main menu
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series
While viewing the [Controlled camera] screen, you can press the
[Power] button to access the JCU-4’s [Main menu] screen.

With the [Main menu] screen displayed, the following options
are available:

<!-- figure 1 on pdf page 103 at 38,240-314,353 pt | caption: none | text-layer labels: none | nearby labels: Applicability: MD-Series | OCR text follows (tesseract, unverified; 6/7 words >= 60, mean confidence 78) -->
Bow Camera::
Feed:
2
1
3
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 103 at 334,305-607,418 pt | caption: none; nearest centred text below: "With the [Main menu] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/11 words >= 60, mean confidence 74) -->
MAIN
MENU
Power down
Brightness
7 Camera Focus
<!-- end of figure 2 -->

<!-- pdf page 104 | printed page 104 | header: Description / Option -->

 Option              Description

 [Select camera]     Select to change the which camera is currently
                     being controlled by the JCU-4.
 [Power down]        Select to access power options for both the
                     JCU-4 and the camera which is currently being
                     controlled.
 [Brightness]        Select to adjust the JCU-4’s LCD brightness
                     / button illumination and to also enable or
                     disable [Night] mode.
 [Camera focus]

                      Note:
                      This function is only supported
                      by M400-Series / M460-Series /
                      M500-Series / M560-Series cameras.

 [JCU settings]      Select to access further configurable JCU-4
                     settings.

Select camera
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can change which compatible FLIR maritime camera the JCU-4
is currently controlling via the [Select camera] screen.
The [Select camera] screen can be accessed by:
• Navigating to: [Controlled camera > Main menu > Select camera],
  OR;
• By press and holding the [Active feed switch] button.

If a camera which you wish to control is not displayed, ensure
that it has been selected via the [Cameras] configuration screen:
[Controlled camera > Main menu > JCU settings > Cameras].

Power down
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4 and other compatible FLIR maritime cameras on your
network can be remotely set to standby and / or restarted via the
[Power down] screen.
The [Power down] screen can be accessed by navigating to:
[Controlled camera > Main menu > Power down].

With the [Power down] screen displayed, the following options
are available:
• [JCU standby] — Select to enter the JCU-4 into a standby state
  until operation is resumed.
• [Camera standby] — Select to enter the controlled camera into to
  a standby state until operation is resumed.
• [Camera restart] — Select to restart the controlled camera.
• [System standby] — Select to enter both the JCU-4 and the
  controlled camera into a standby state until operation is resumed.

Brightness
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can adjust the JCU-4’s LCD brightness / button illumination and
also enable or disable [Night] mode via the [Brightness] screen.

<!-- figure 1 on pdf page 104 at 125,154-290,202 pt | caption: none | text-layer labels: Note: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 104 at 334,173-607,286 pt | caption: none; nearest centred text below: "With the [Power down] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 88) -->
POWER
DOWN
Camera Standby
Camera Restart
Svstem Standbv
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 104 at 38,360-314,473 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 83) -->
Bow Camera
SELECT
CAMERA
Engine Room
Cabin
<!-- end of figure 3 -->

<!-- pdf page 105 | printed page 105 | footer: Operation (MD-Series) -->

The [Brightness] screen can be accessed by navigating to:
[Controlled camera > Main menu > Brightness].

With the [Brightness] screen displayed, the following options are
available:
• [Down] — Select to increase the LCD brightness and button
  illumination by 5%.
• [Night] — Select to either enable or disable [Night] mode.
• [Up] — Select to decrease the LCD brightness and button
  illumination by 5%.
Night mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The JCU-4’s user interface and physical buttons can be configured
to use a red color palette intended for night time use by selecting
the [Night] mode option via the [Brightness] screen.
 Night mode enabled                  Night mode disabled

 Important:
 If you are using the [Night] mode color palette at night, be aware
 that your vision may be compromised when either disabling the
 [Night] mode or switching to a display screen with a higher level
 of brightness.

Camera focus
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series

 Note:
 This function is only supported by M400-Series / M460-Series /
 M500-Series / M560-Series cameras.

17.7 JCU settings
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
Additional advanced settings can be accessed via the [JCU settings]
menu.
The [JCU settings] menu can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings].

With the [JCU settings] menu displayed, the following options
are available:

 Option              Description

 [Shortcut keys]

                      Note:
                      This menu option is only available
                      when the JCU-4 is controlling an
                      M460-Series / M560-Series camera.

 [Joystick mode]     Select to configure which direction the camera
                     tilts when the joystick is moved up and down.

<!-- figure 1 on pdf page 105 at 38,50-314,163 pt | caption: none; nearest centred text below: "With the [Brightness] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 74) -->
BRIGHTNESS
Night
Down
Up
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 105 at 334,218-607,331 pt | caption: none; nearest centred text below: "With the [JCU settings] menu displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/8 words >= 60, mean confidence 79) -->
JCU
SET-UP
Joystick Mode
Cameras
Installation
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 105 at 41,348-312,408 pt | caption: none | text-layer labels: none | nearby labels: Night mode enabled | Night mode disabled | Important: | OCR text follows (tesseract, unverified; 7/9 words >= 60, mean confidence 86) -->
MAIN
MENU
Power down
Brightness
Camera Focus
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 105 at 420,391-586,439 pt | caption: none | text-layer labels: Note: | nearby labels: Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 106 | printed page 106 | header: Description / Option -->

 Option               Description

 [Cameras]            Select to configure which compatible FLIR
                      maritime cameras detected on the network can
                      be controlled by your JCU-4.

 [Installation]       Select to reconfigure the JCU-4’s IP network
                      parameters which were set during the startup
                      wizard.
 [About]              Select to display additional information related
                      to the JCU-4.
 [Settings reset]     Select to perform a settings reset.

 [Factory reset]      Select to perform a factory reset.

Shortcut keys
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series

 Note:
 This menu option is only available when the JCU-4 is controlling an
 M460-Series / M560-Series camera.

Joystick mode
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can configure the JCU-4’s up and down joystick inputs to either
tilt the camera in the same direction as the joystick or the opposite
direction via the [Joystick mode] screen.
The [Joystick mode] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Joystick mode].

With the [Joystick mode] screen displayed, the following options
are available:
• [Gaming] — Causes the camera to tilt upward when the joystick
  is pushed up and downward when the joystick is pushed down.
• [Pilot] — Causes the camera to tilt upward when the joystick is
  pushed down and downward when the joystick is pushed up.
The JCU-4 is set to [Gaming] mode by default.

Controllable cameras
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
On the [Cameras] screen you can select which compatible FLIR
maritime camera(s) on the network can be controlled by your
JCU-4.
The [Cameras] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > Cameras].

Once you have chosen the camera(s) that you wish to control using
the JCU-4 and have selected [Save], the chosen camera(s) will then
appear on the [Select camera] screen.

 Note:
 The list of controllable cameras will dynamically update if a camera
 is either connected to or disconnected from the network. If a
 compatible FLIR maritime camera is connected to your network and
 cannot be automatically detected by the JCU-4 after a prolonged
 period, refer to the following section for troubleshooting information:
 p.119 — System checks and troubleshooting

<!-- figure 1 on pdf page 106 at 334,233-607,341 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 74) -->
M364C
CAMERAS
SAVE
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 106 at 38,370-314,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 64) -->
Gaming
JOYSTICK
MODE
<!-- end of figure 2 -->

<!-- pdf page 107 | printed page 107 | footer: Operation (MD-Series) -->

Installation
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
It is possible to reconfigure the settings which were selected during
the startup wizard at any time via the [Installation] screen.
The [Installation] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Installation].

With the [Installation] screen displayed, the following options are
available:
• [Select system] — Select to reconfigure the type of system that
  your JCU-4 is networked to.
• [IP Address type] — Select to reconfigure the assigned IP address
  type.
• (1) [IP Address] — Select to reconfigure the assigned static IP
  address and netmask.

 Note:
 (1) This menu option is only available if the JCU-4’s assigned IP
 address type is set to [Static IP].

About this device
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
The [About] screen contains additional information related to the
JCU-4.
The [About] screen can be accessed by navigating to: [Controlled
camera > Main menu > JCU settings > About].

The following range of information can be found on the [About]
screen:
• [Serial] — Provides the JCU-4’s serial number.
• [Software V] — Provides the software version number that the
  JCU-4 is currently running.
• [IP Address] — Provides the JCU-4’s IP address.
• [Hours] — Provides the number of hours that the JCU-4 has been
  in operation for this session.
• [Total hours] — Provides the total number of hours that the JCU-4
  has been in operation for.

Settings reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
You can reset the JCU-4’s configured user settings (excluding the
assigned IP network parameters) via the [Settings reset] screen.
The [Settings reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Settings reset].

<!-- figure 1 on pdf page 107 at 334,29-607,142 pt | caption: none; nearest centred text below: "The following range of information can be found on the [About] screen:" | text-layer labels: none | OCR text follows (tesseract, unverified; 15/15 words >= 60, mean confidence 92) -->
About JCU-4
Serial: AMOO01B
Software V: 2.0.12
IP Address: 198.18.7.71
Total Hours: 59.4
Hours: 0.1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 107 at 38,120-314,233 pt | caption: none; nearest centred text below: "With the [Installation] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 96) -->
INSTALL
IP Address Type
IP Address
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 107 at 334,362-607,482 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/5 words >= 60, mean confidence 95) -->
Reset JCU-4 settings?
No
Yes
<!-- end of figure 3 -->

<!-- pdf page 108 | printed page 108 | header: With the [Settings reset] screen displayed, the following options are available: -->

With the [Settings reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4 has
  been reset to settings default, the unit will return back to the
  [Controlled camera] screen.

Factory reset
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M460-Series / M500-Series /
M560-Series
If you wish to reset the JCU-4’s configured user settings (including
the assigned IP network parameters), or, if you are experiencing
problems with your JCU-4 which cannot be resolved using the
troubleshooting advice provided, you may need to reset the JCU-4
to factory default via the [Factory reset] screen.

 Note:
 If you are experiencing problems with your JCU-4 and have not yet
 followed the troubleshooting advice provided, refer to:
 • p.119 — System checks and troubleshooting

The [Factory reset] screen can be accessed by navigating to:
[Controlled camera > Main menu > JCU settings > Factory reset].

With the [Factory reset] screen displayed, the following options
are available:
• [No] — Select to cancel the reset process.
• [Yes] — Select to initiate the reset process. Once the JCU-4
  has been reset to factory default, the startup wizard will be
  automatically displayed on-screen.

17.8 User programmable buttons
(UPBs)
Applicability: MD-Series / M100-Series / M200-Series /
M300-Series / M400-Series / M500-Series
The JCU’s User-programmable buttons (UPBs) can be configured
from a compatible FLIR maritime camera’s Web browser user
interface and / or [On-Screen Display] menu.
You can assign a different action to each UPB (for example, ”Park”
or “Surveillance mode”) on a per-camera basis.

 Note:
 UPB assignments apply to individual cameras rather than specific
 JCU units. This means that, if you are using a single JCU unit to
 control 2 FLIR maritime cameras, UPB number 1 could be configured
 to initiate a different action on each camera.

Programming UPBs via the On-Screen Display
(OSD) menu
Applicability: MD-Series
A single user-programmable button (UPB) action can be assigned
to the JCU’s [Softkey 1] button using the MD-Series camera’s
[On-Screen Display] menu.
To assign a UPB action using the camera’s [On-Screen Display]
menu:
1. Press the JCU-4’s [On-screen Display] button.
    Once selected, the camera’s [On-Screen Display] menu will
    appear on your networked video display:

<!-- figure 1 on pdf page 108 at 46,293-314,406 pt | caption: none; nearest centred text below: "With the [Factory reset] screen displayed, the following options are available:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/7 words >= 60, mean confidence 95) -->
Reset JCU-4 to factory defaults?
No
Yes
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 108 at 346,324-607,475 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 11/19 words >= 60, mean confidence 66) -->
Set Symbology
User Programmable Button
System Setup
About/Help
Exit
Puck to
<!-- end of figure 2 -->

<!-- pdf page 109 | printed page 109 | footer: Operation (MD-Series) -->

2. Select the [User Programmable Button] option.
   Once selected, the [User Programmable Button] sub-menu is
   displayed.
3. From the [User Programmable Button] sub-menu, select the
   camera action that you wish to assign to the JCU-4’s [Softkey
   1] button.
   Once chosen, the assigned action will be highlighted in a black
   font.

<!-- pdf page 110 | printed page 110 -->

CHAPTER 18: CONFIGURATION VIA WEB INTERFACE

CHAPTER CONTENTS

•   18.1 Web browser user interface overview — page 111
•   18.2 Logging in to the Web browser user interface — page 111
•   18.3 Web browser user interface — page 112

<!-- pdf page 111 | printed page 111 | footer: Conﬁguration via Web interface -->

18.1 Web browser user interface
overview
This section describes how to use a Web browser to communicate
with and configure your JCU-4.
The JCU-4 is a network device that communicates over an Ethernet
network using Internet Protocol (IP). Using a Web browser, you
can perform software updates and configure your unit’s network
configuration settings.

 Note:
 • Changes to configuration settings should only be made by
 someone who has expertise with JCU-4 devices and a thorough
 understanding of how each setting will affect the JCU-4.
 Haphazard changes can lead to potential problems.
 • You can use various types of IP-networked devices to interact
 with the JCU-4 Web interface (such as a laptop, PC or tablet).
 The device must be connected to the same network as the JCU-4
 (or connected directly).

18.2 Logging in to the Web browser
user interface
You can log in to the JCU-4’s Web interface using the login details
provided on the serial number label located on the rear of your
unit and / or in the product box:

To log in:
1. Go to the JCU-4’s Web page by:
   • Entering the JCU-4’s IP address directly into the address bar
     of your Web browser, OR:
   • Double-clicking the JCU-4 device listed in “Network” in
     Windows Explorer.

 Note:
 For more information on how to discover the JCU-4’s IP address,
 refer to: p.112 — IP address discovery

   The login screen is displayed:

<!-- figure 1 on pdf page 111 at 334,103-607,281 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/5 words >= 60, mean confidence 47) -->
il
<!-- end of figure 1 -->

<!-- pdf page 112 | printed page 112 -->

2. Enter the password referenced above, then select [Login].

IP address discovery
Before you can access the JCU-4’s Web interface page(s), you may
first need to know the JCU-4’s IP address.
The JCU-4’s IP address can be obtained by:
• Navigating to the [About] screen: [Controlled camera > Main
  menu > JCU settings > About]. OR;
• Press and holding the [IR Color] button down, then holding the
  joystick upward to display the JCU-4 and controlled camera’s
  IP address.

18.3 Web browser user interface
The Web browser user interface is split into the following 3 pages,
which can be accessed at any time using the sidebar menu located
on the left side of your screen:
1.   p.112 — Product information page

2.   p.113 — Setup page

3.   p.116 — Diagnostics page

The available Web browser user interface menu options are
subject to change depending upon which software version your
device is running. Ensure that your device is running the latest
software by visiting the Raymarine / FLIR maritime website:
www.raymarine.com/software

Product information page
Once you have successfully logged into the Web interface the
[Product information] page will be displayed, where additional
information for your unit can be found.

The following information is displayed on the [Product information]
page.
Hardware:

 Item                Description

 [Friendly Name]     Provides a description of the network name
                     assigned to the JCU-4.
 [Serial Number]     Provides the JCU-4’s serial number.

Software:

 Item                Description

 [Version]           Provides the JCU-4’s current software version
                     number.

Network:

 Item                Description

 [Mode] / [ IP] /    Provides a description of the JCU-4’s
 [Mask]              configured IP-network parameters.

<!-- figure 1 on pdf page 112 at 53,29-314,161 pt | caption: none | text-layer labels: none | nearby labels: IP address discovery | OCR: no legible text (0/1 words >= 60, mean confidence 2) -->
<!-- figure 2 on pdf page 112 at 334,77-607,209 pt | caption: none | text-layer labels: none | nearby labels: Hardware: | OCR text follows (tesseract, unverified; 6/10 words >= 60, mean confidence 72) -->
JCU4 Admin Panel
Into
Software
Network
<!-- end of figure 2 -->

<!-- pdf page 113 | printed page 113 | header: Description / Option | footer: Conﬁguration via Web interface -->

Setup page
The [Setup] page provides access to a series of menus and
associated configuration settings which impact how your unit
operates and connects to other devices in your system.
From the [Setup] page, the following menus can be accessed:
1.   Network menu

2. Joystick menu
3. Softkey menu
4. System menu

Network menu
The [Network] menu contains configuration options related to your
unit’s IP-network parameters.

The following options can be found under the [Network] menu.

 Option             Description

 [DHCP]             Select to automatically assign the JCU-4’s
                    IP-network parameters via DHCP (Dynamic
                    Host Configuration Protocol).
                    By default, the JCU-4 is set to use DHCP.
 [Static]           Select to manually assign a static IP address
                    to the JCU-4.
 [IP Address]       Select to manually configure the JCU-4’s IP
                    address.
                    This setting is only available if the JCU-4’s IP
                    address type is set to [Static].

 Option              Description

 [Netmask]           Select to manually configure the JCU-4’s
                     Netmask address.
                     This setting is only available if the JCU-4’s IP
                     address type is set to [Static].
 [Gateway            Select to manually configure the JCU-4’s
 (optional)]         Gateway address.
                     This setting is only available if the JCU-4’s IP
                     address type is set to [Static].
 [Save]              Select to save the current setting configuration.
                     Once the [Save] button has been selected,
                     the JCU-4 must be rebooted via the [Reboot]
                     popup in order to initiate any changes created.

Joystick menu
The [Joystick] menu contains configuration options which enable
you to change the JCU-4’s up and down joystick inputs to either tilt
the camera in the same direction as the joystick or the opposite
direction.

The following options can be found under the [Joystick] menu.

 Option              Description

 [Gaming]            Causes the camera to tilt upward when the
                     joystick is pushed up and downward when the
                     joystick is pushed down.
 [Pilot]             Causes the camera to tilt upward when the
                     joystick is pushed down and downward when
                     the joystick is pushed up.

<!-- figure 1 on pdf page 113 at 38,199-314,324 pt | caption: none | text-layer labels: none | nearby labels: Network menu | Option | Description | OCR text follows (tesseract, unverified; 4/13 words >= 60, mean confidence 45) -->
Setup
fo
Setup
80
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 113 at 334,240-607,365 pt | caption: none; nearest centred text below: "Description" | text-layer labels: none | nearby labels: Option | Description | OCR text follows (tesseract, unverified; 4/13 words >= 60, mean confidence 40) -->
Setup
Diag
Joystick Mode
<!-- end of figure 2 -->

<!-- pdf page 114 | printed page 114 | header: Description / Option -->

Softkey menu
The [Softkey] menu contains configuration options which enable
you to assign different shortcut actions to the JCU-4’s softkey
buttons while controlling an M460-Series / M560-Series camera.

The following options can be found under the [Softkey] menu when
selecting an assigned shortcut action:

 Option             Description

 [BWC]

                      Note:
                      This option is not supported by
                      M460-Series / M560-Series cameras.

 [Camera]           Changes the camera which is being controlled
                    by the JCU-4 to the next available camera
                    (cycling in alphabetical order).
 [CTV]              (1) Enables / disables the camera’s [CTV] (Color
                    Thermal Vision) blending mode.
 [Defog]            (1) Enables / disables the camera’s visible light
                    [Defog] video filter mode.

 [FFC]              Initiates the camera’s configured [FFC] (Flat
                    Field Correction) mode. For more information,
                    refer to: Flat Field Correction (FFC)

Option        Description

[Fire]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

[Flash]       Enables / disables the camera’s spotlight.
              When enabled, a flashing spotlight beam will
              appear at the center of the camera’s field of
              view and the JCU-4’s [Spotlight on] screen will
              be displayed.

[Focus]       Displays the JCU-4’s [Camera focus] screen,
              which can be used to manually or automatically
              adjust the controlled camera’s focus.
[Ice]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

[InstAlert]   (1) Enables / disables the camera’s [InstAlert]
              thermal imaging mode.
[Light]       Enables / disables the camera’s spotlight. When
              enabled, a continuous spotlight beam will
              appear at the center of the camera’s field of
              view and the JCU-4’s [Spotlight on] screen will
              be displayed.
[MSX]         (1) Enables / disables the camera’s [MSX]
              (Multi-Spectral Dynamic Imaging) blending
              mode.
(2) [Range]   Displays the JCU-4’s [Ready to Range] screen,
              which can be used to trigger the camera’s laser
              range finder (LRF). For more information, refer
              to: Ready to range
[RSD]

               Note:
               This option is not supported by
               M460-Series / M560-Series cameras.

<!-- figure 1 on pdf page 114 at 38,77-314,214 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 7/15 words >= 60, mean confidence 49) -->
JCU4 Admin Panel
Product Inf
Setup
Setup
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 114 at 420,204-586,245 pt | caption: none; nearest centred text below: "(1) Enables / disables the camera’s [InstAlert]" | text-layer labels: Note: | nearby labels: thermal imaging mode. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 115 | printed page 115 | header: Description / Option | footer: Conﬁguration via Web interface -->

 Option              Description

 [Stab]              (1) Enables / disables the camera’s [Stabilization]
                     mode.
 [Surveil]           (1) Enables / disables the camera’s [Surveillance
                     scan] mode.

 [Track]             Displays the JCU-4’s [Ready to Track] screen,
                     which can be used to track an object detected by
                     the camera’s target classifier tracking system.
                     For more information, refer to: Ready to track
 [TTM]               (1) Enables / disables NMEA Radar target (TTM)
                     tracking for the camera.
 [None]              Removes the assigned action.

Any changes made will be reflected on the [Controlled camera]
screen.

 Note:
 • (1) For more information, refer to the documentation that is
 supplied with your compatible FLIR maritime camera:
 – (71010) M460-Series Thermal Camera Operation Instructions.
 – (71011) M560-Series Thermal Camera Operation Instructions.
 Please ensure that you obtain the latest version of your
 documentation via the FLIR website: www.bit.ly/3Seupv7
 • (2) This option is only available for camera variants which
 support a laser range finder (LRF).

System menu
The [System] menu contains configuration options which enable
you to perform an update, or reset your unit to factory default
settings.

The following options can be found in the [System] menu.
Firmware:

 Option             Description

 [Choose file]      Select to navigate your operating system’s
                    file explorer and choose a file containing the
                    updated JCU-4 firmware.
 [Upgrade]          Select to initiate an update once a
                    corresponding file has been chosen.

Factory Reset:

 Option             Description

 [Partial reset]    Select to reset all configuration settings
                    (excluding assigned IP network parameters) to
                    factory default.
 [Full reset]       Select to reset all configuration settings
                    (including assigned IP network parameters) to
                    factory default.

Reboot:

 Option             Description

 [Reboot]           Select to initiate a reboot (device restart).

<!-- figure 1 on pdf page 115 at 334,74-607,209 pt | caption: none | text-layer labels: none | nearby labels: System menu | Firmware: | OCR text follows (tesseract, unverified; 7/14 words >= 60, mean confidence 58) -->
Admin Panel
Setup
Factory Reset
co
co
<!-- end of figure 1 -->

<!-- pdf page 116 | printed page 116 -->

Diagnostics page
The [Diagnostics] page contains event log information which can be
used by FLIR technical support to help diagnose and troubleshoot
issues experienced with your unit.

The following options can be found under the [Diagnostics] page.

       Description

 1     [Type to filter]
       Select to enter a term and manually filter the range of event
       log information displayed.
 2     [Download]
       Select to download the event log information to your device’s
       internal storage.
 3     [Refresh]
       Select to refresh the event log information displayed.

<!-- figure 1 on pdf page 116 at 38,84-98,214 pt | caption: none | text-layer labels: none | nearby labels: Description | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 63) -->
Diagnostics
Product
Setup
<!-- end of figure 1 -->

<!-- pdf page 117 | printed page 117 -->

CHAPTER 19: MAINTENANCE

CHAPTER CONTENTS

•      19.1 Service and maintenance — page 118
•      19.2 Routine equipment checks — page 118
•      19.3 Cleaning the unit — page 118

Maintenance                                       117

<!-- pdf page 118 | printed page 118 -->

19.1 Service and maintenance
This product contains no user serviceable components. Please
refer all maintenance and repair to authorized FLIR dealers.
Unauthorized repair may affect your warranty.

19.2 Routine equipment checks
It is recommended that you perform the following routine checks,
on a regular basis, to ensure the correct and reliable operation of
your equipment:
• Examine all cables for signs of damage or wear and tear.
• Check that all cables are securely connected.

19.3 Cleaning the unit
The remote should only be cleaned with the battery cover closed.
1. Power the unit off.
2. Wipe the unit’s enclosure with a clean, lint-free microfibre cloth.
3. If necessary, use a mild detergent to remove grease marks from
   the unit’s enclosure.
4. Rinse the screen with fresh water to remove all dirt particles
   and salt deposits.
5. Allow the screen to dry naturally.
6. If any smears remain, very gently wipe the screen with a clean,
   lint free microfibre cloth.

<!-- pdf page 119 | printed page 119 -->

CHAPTER 20: SYSTEM CHECKS AND TROUBLESHOOTING

CHAPTER CONTENTS

•       20.1 Troubleshooting — page 120
•       20.2 PoE power connection troubleshooting — page 120
•       20.3 Non-PoE power connection troubleshooting — page 121
•       20.4 System data troubleshooting — page 122
•       20.5 Miscellaneous troubleshooting — page 122

System checks and troubleshooting                                  119

<!-- pdf page 120 | printed page 120 -->

20.1 Troubleshooting
The troubleshooting section provides possible causes and the
corrective action required for common problems that are associated
with the installation and operation of your product.
Before packing and shipping, all FLIR products are subjected to
comprehensive testing and quality assurance programs. If you do
experience problems with your product, this section will help you
to diagnose and correct problems to restore normal operation.
If after referring to this section you are still having problems with
your product, please refer to the Technical support section of this
manual for useful links and FLIR technical support contact details.

20.2 PoE power connection
troubleshooting
Before troubleshooting problems with your PoE (Power over
Ethernet) power connection, ensure that you have read and
followed the power connection guidance provided and performed a

power cycle/reboot of the device. The troubleshooting information
below can be used if you are experiencing problems when
powering your product via PoE.

Product does not turn on or keeps turning off:
 Possible causes    Possible solutions

 Blown fuse /       1.   Check the condition of your relevant
 tripped breaker:        fuses, breakers and connections, and
                         replace if necessary.
                    2. If the fuse keeps blowing check for
                       cable damage, broken connector pins or
                       incorrect wiring between your unit, the
                       PSE (Power Sourcing Equipment) and
                       the power source providing power to the
                       PSE.
 Poor / damaged     1.   Check to ensure that all connections
 / insecure power        (e.g. between your unit, the PSE (Power
 supply cable /          Sourcing Equipment) and the power
 connections:            source providing power to the PSE) are
                         secure, clean and free from corrosion.
                         Replace if necessary.
                    2. Ensure that the power cable connector is
                       correctly orientated, fully inserted and in
                       the locked position.
                    3. With the unit turned on, try flexing the
                       power cable connector to see if this
                       causes the unit to restart or lose power.
                       Replace if necessary.
                    4. With the product under load, using a
                       multi-meter, check for high voltage drop
                       across all connectors / fuses etc, and
                       replace if necessary.

<!-- pdf page 121 | printed page 121 -->

  Possible causes                   Possible solutions

  Incorrect power                   1.   Check to ensure that connections
  connection:                            between your unit, the PSE (Power
                                         Sourcing Equipment) and the power
                                         source providing power to the PSE are
                                         correct.
  Power source                      1.   Any device supplying PoE (Power over
  insufficient:                          Ethernet) to the JCU-4 must output a
                                         nominal supply voltage of 44 V to 57 V
                                         dc.

20.3 Non-PoE power connection
troubleshooting
Before troubleshooting problems with your non-PoE (non-Power
over Ethernet) power connection, ensure that you have read and
followed the power connection guidance provided and performed a

System checks and troubleshooting

power cycle/reboot of the device. The troubleshooting information
below can be used if you are experiencing problems when
powering your product via non-PoE.

Product does not turn on or keeps turning off:
 Possible causes    Possible solutions

 Blown fuse /       1.   Check the condition of your relevant
 tripped breaker:        fuses, breakers and connections, and
                         replace if necessary.
                    2. If the fuse keeps blowing check for
                       cable damage, broken connector pins or
                       incorrect wiring.
 Poor / damaged     1.   Check the vessel’s battery voltage and
 / insecure power        the condition of the battery terminals
 supply cable /          and power supply cables, ensuring
 connections:            connections are secure, clean and free
                         from corrosion. Replace if necessary.
                    2. Check the power cable and your power
                       supply connection for signs of damage
                       or corrosion, and replace if necessary.
                    3. Ensure that the power cable connector is
                       correctly orientated, fully inserted and in
                       the locked position.
                    4. With the unit turned on, try flexing the
                       power cable connector to see if this
                       causes the unit to restart or lose power.
                       Replace if necessary.
                    5. With the product under load, using a
                       multi-meter, check for high voltage drop
                       across all connectors / fuses etc, and
                       replace if necessary.
 Incorrect power    1.   The power supply may be wired
 connection:             incorrectly, ensure the installation
                         instructions have been followed.
 Power source       1.   Check that your power supply (battery
 insufficient:           or distribution panel) is providing a
                         minimum of 8 V to the unit.

                                                                   121

<!-- pdf page 122 | printed page 122 -->

20.4 System data troubleshooting
Networked camera(s) not available on your joystick
controller(s):
Possible causes   Possible solutions

Connection        1.   Check that the FLIR maritime camera(s)
problem:               are correctly powered and operational.
                  2. Check that the controller(s) and FLIR
                     maritime camera(s) are correctly
                     connected to the same network.
                  3. Check the relevant product and or
                     network cabling and connections for
                     signs of damage or corrosion, and
                     replace if necessary.
                  4. If applicable, check the status of your
                     Ethernet network switch.
Software          1.   Ensure that all products have the latest
mismatch               software installed.
between
equipment
may prevent
communication:
IP network        1.   If the JCU-4 has been configured to
parameter              use a [Static] IP address, ensure that
configured             you have correctly configured your
incorrectly:           IP-network parameter settings (e.g. [IP
                       address] and [Netmask] and [Gateway]
                       settings) via the Web browser user
                       interface. For more information, refer to:
                       p.112 — Web browser user interface

20.5 Miscellaneous troubleshooting
Erratic or unresponsive controls:
Possible causes      Possible solutions

Connection           1.   Check that the FLIR maritime camera(s)
problem:                  are correctly powered and operational.
                     2. Check that the controller(s) and FLIR
                        maritime camera(s) are correctly
                        connected to the same network.
                     3. Check the relevant product and or
                        network cabling and connections for
                        signs of damage or corrosion, and
                        replace if necessary.
                     4. If applicable, check the status of your
                        Ethernet network switch.
Control conflict     1.   Ensure that no other controllers are in
(e.g. caused by           use at the same time.
multiple users
at different
stations):
Problem with         1.   Check cabling between the controller
the controller:           and the Power Sourcing Equipment (e.g.
                          PoE Injector / PoE network switch).
                     2. If available, check any other controllers
                        that have been connected to your
                        system. If the other controllers are
                        operating as intended, this will eliminate
                        the possibility of a more fundamental
                        camera fault.

LCD is too bright or dark:
Possible causes      Possible solutions

Brightness level     1.   Change the current LCD brightness and
is set too high or        button illumination via the [Brightness]
low:                      menu.

<!-- pdf page 123 | printed page 123 -->

CHAPTER 21: SUPPORT AND SERVICING

CHAPTER CONTENTS

•       21.1 FLIR Maritime technical support and servicing — page 124

Support and servicing                                                   123

<!-- pdf page 124 | printed page 124 -->

21.1 FLIR Maritime technical support
and servicing
FLIR provides a comprehensive product support service, as well as
warranty, service, and repairs. You can access these services using
the contact details provided below.

Product information
For the latest support information, go to: https://maritime-
support.flir.com
If you need to request service or support, please have the following
information to hand:
• Product name.
• Product identity.
• Serial number.
• Software application version.
• System diagrams.
You can obtain this product information using the menus available
when using your product.

Warranty policy and registration
Visit the Raymarine website to read the latest warranty policy,
and register your product’s warranty online: www.bit.ly/rym-warranty

Servicing and contact information
FLIR and Raymarine offer dedicated service departments for
servicing and repairs. Contact details:
 Region                             Contact details

 United Kingdom (UK), EMEA,         Telephone: +44 (0)1329 246 932
 and Asia Pacific:                  Address: Marine House,
                                    Cartwright Drive, Fareham, PO15
                                    5RJ, UK.
                                    www.bit.ly/rym-service

 United States (US):                Telephone: Tel: +1 (603) 324
                                    7900 (Toll-free: +800 539 5539)
                                    Address: 110 Lowell Road,
                                    Hudson, NH 03051, USA.
                                    www.bit.ly/rym-service

<!-- pdf page 125 | printed page 125 -->

CHAPTER 22: TECHNICAL SPECIFICATION

CHAPTER CONTENTS

•       22.1 Physical specification — page 126
•       22.2 Power specification — page 126
•       22.3 Network specification — page 126
•       22.4 Display specification — page 126
•       22.5 Environmental specification — page 126
•       22.6 Conformance specification — page 126

Technical speciﬁcation                                125

<!-- pdf page 126 | printed page 126 -->

22.1 Physical specification                                        Specification

Specification                                                      Viewing angles:              80 + / 80 +
Width:                    93.66 mm (3.69 in)                       Resolution:                  376 (H) x 960 (W) pixels (RBG)
Height:                   146.66 mm (5.77 in)                      Contrast ratio:              1:1500

Depth:                    63.36 mm (2.49 in)
Depth (including          113.30 mm (4.46 in)
                                                                   22.5 Environmental specification
joystick):                                                         Specification

                                                                   Operating tempera-        -25 ºC to +55 ºC (-13 ºF to 131 ºF)
22.2 Power specification                                           ture:
Specification                                                      Storage temperature:      -30 ºC to +70 ºC (-22 ºF to 158 ºF)
PoE class:                Class 2                                  Relative humidity:        Maximum 93% @ + 40 °C (104 °F)
Nominal supply            • PoE: 48 V dc                           Waterproof rating:        IPx6
voltage:
                          • Alternate power: 12 V / 24 V dc
Operating voltage         • PoE: 44 V to 57 V dc                   22.6 Conformance specification
range:
                          • Alternate power: 8 V to 32 V dc        Specification

Power consumption:        5 W Max with full keypad illumination.   Europe, UK, Australia &      • IEC/EN 60945:2002
                                                                   New Zealand:
IEEE Standard:            IEEE 802.3af                                                          • IEC/EN 62368-1:2020
                                                                   USA:                         FCC CFR 47, Part 15B
22.3 Network specification                                         Canada:                      ICES-003, RSS-GEN, Issue 5
Specification
                                                                   Ethernet / PoE:              • IEEE 802.3
Network             • 1x 10/100/1000 Mbits/s RayNet (Ethernet)
connection                                                                                      • IEEE 802.3af
ports:              • 1x 10/100/1000 Mbits/s PoE RayNet
                      (Ethernet)

22.4 Display specification
Specification

LCD Size:                    2.9”

LCD Type:                    IPS TFT LCD
Active area:                 26.51 mm x 67.68 mm
Brightness / Luminance:      600 nits / 600 cd/m2

<!-- pdf page 127 | printed page 127 | footer: Spares and accessories -->

CHAPTER 23: SPARES AND ACCESSORIES

CHAPTER CONTENTS

•   23.1 Spares and accessories — page 128
•   23.2 FLIR networking accessories — page 129
•   23.3 RayNet to RayNet cables and connectors — page 131
•   23.4 RayNet to RJ45, and RJ45 (SeaTalk HS) adapter cables — page 133

<!-- pdf page 128 | printed page 128 -->

23.1 Spares and accessories
The following spares and accessories are available for your product:

        Part         Description

 1      A80748       JCU-4 weatherproof cover.
 2      R70979       JCU-4 front fascia / cover.
 3      A80749       JCU-4 mounting kit.
 4      A80756       JCU-4 Right-angled RayNet (Ethernet) to RJ45
                     adapter cable, 3 m (9.8 ft).
 5      A80757       JCU-4 Right-angled 3-pin power cable, 3 m
                     (9.8 ft).

<!-- figure 1 on pdf page 128 at 38,70-314,252 pt | caption: none | text-layer labels: Part | Description | nearby labels: 23.1 Spares and accessories | 1 | A80748 | JCU-4 weatherproof cover. | 2 | R70979 | JCU-4 front fascia / cover. | OCR text follows (tesseract, unverified; 1/5 words >= 60, mean confidence 34) -->
ry
<!-- end of figure 1 -->

<!-- pdf page 129 | printed page 129 | footer: Spares and accessories -->

23.2 FLIR networking accessories

1.   RJ45 coupler, for joining 2 separate RJ45 network cables
     together to achieve longer cable runs.
2. PoE Injector (2nd Generation; 5 Gbit). Supplies power to a
   non-PoE network connection. Typical use is for powering a
   JCU-Series controller connected to a non-PoE network switch.
3. PoE 8-port Gigabit Network Switch.

4. 305 mm (1 ft.) RJ45-to-RJ45 Ethernet cable, double shielded
   with LSZH low interference jacket.
5. 7.6 m (25 ft.) RJ45-to-RJ45 Ethernet cable, double shielded with
   LSZH low interference jacket.
6. 15.2 m (50 ft.) RJ45-to-RJ45 Ethernet cable, double shielded
   with LSZH low interference jacket.

<!-- figure 1 on pdf page 129 at 38,43-607,403 pt | caption: none | text-layer labels: none | nearby labels: 23.2 FLIR networking accessories | 1. | OCR text follows (tesseract, unverified; 27/54 words >= 60, mean confidence 54) -->
2?
e e e
e e
3?
305 mm (1 ft.)
7.6 m (25 ft.)
15.2 m (50 ft.)
22.8 m (75 ft.)
30.4 m (100 ft.)
<!-- end of figure 1 -->

<!-- pdf page 130 | printed page 130 -->

7.   22.8 m (75 ft.) RJ45-to-RJ45 Ethernet cable, double shielded
     with LSZH low interference jacket.
8. 30.4 m (100 ft.) RJ45-to-RJ45 Ethernet cable, double shielded
   with LSZH low interference jacket.

<!-- pdf page 131 | printed page 131 | footer: Spares and accessories -->

23.3 RayNet to RayNet cables and connectors

1.   Standard RayNet connection cable with a RayNet (female)
     socket on both ends.
2. Right-angle RayNet connection cable with a straight RayNet
   (female) socket on one end, and a right-angle RayNet (female)
   socket on the other end. Suitable for connecting at 90° (right
   angle) to a device, for installations where space is limited.

3. Right-angle RayNet connection cable with a straight RayNet
   (female) socket on one end, and a right-angle RayNet (female)
   socket on the other end. Available as an alternative to the
   (A80512) accessory cable, for installations which require an
   alternate cable routing direction.
4. RayNet cable puller (5 pack).

<!-- figure 1 on pdf page 131 at 38,46-607,401 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 26/38 words >= 60, mean confidence 69) -->
1
ft)
10 m (32.8 ft)
5 m (16.4 ft)
4
00 mm (1.3 ft)
A80161 A62361
0.5 m (1.6 ft)
ft)
10 m (32.8 ft)
<!-- end of figure 1 -->

<!-- pdf page 132 | printed page 132 -->

5. RayNet to RayNet right-angle coupler / adapter. Suitable for
   connecting RayNet cables at 90° (right angle) to devices, for
   installations where space is limited.
6. Adapter cable with a RayNet (male) plug on both ends. Suitable
   for joining (female) RayNet cables together for longer cable
   runs.

<!-- pdf page 133 | printed page 133 | footer: Spares and accessories -->

23.4 RayNet to RJ45, and RJ45 (SeaTalk HS) adapter cables

1.   Adapter cable with a RayNet (female) socket on one end, and
     a waterproof (female) RJ45 (SeaTalk HS) socket on the other
     end, accepting the following cables with an RJ45 (SeaTalk HS)
     waterproof locking (male) plug:
     • A62245 (1.5 m).
     • A62246 (15 m).

2. Adapter cable with a RayNet (female) socket on one end, and a
   waterproof (female) RJ45 (SeaTalk HS) socket on the other end,
   along with a locking gland for a watertight fit.
3. Adapter cable with a RayNet (male) plug on one end, and an
   RJ45 (SeaTalk HS) waterproof (male) plug on the other end.

<!-- figure 1 on pdf page 133 at 38,46-607,401 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 57/79 words >= 60, mean confidence 74) -->
400 mm (1.3 ft)
400 mm (1.3 ft)
(j=)
100 mm (3.9 in)
3m (9.84 ft)
1m (3.28 ft)
10 m (32.8 ft)
ft)
A62360 ASO151 ASO159
15 m (49.21 ft)
25 m (82.02 ft)
30 m (98.4 ft)
A80763 A80764 308-251-30-00
1m (3.28 ft)
30 m (98.4 ft)
ft)
10 m (32.81 ft)
308-0261-01-00 A80837 308-252-30-00
<!-- end of figure 1 -->

<!-- pdf page 134 | printed page 134 -->

4. Adapter cable with a RayNet (male) plug on one end, and an
   RJ45 (male) plug on the other end.
5. Adapter cable with a RayNet (female) socket on one end, and
   an RJ45 (SeaTalk HS) waterproof (male) plug on the other end.
6. Adapter cable with a RayNet (female) socket on one end, and
   an RJ45 (male) plug on the other end.
7.   Adapter cable with a right-angled RayNet (female) socket on
     one end, and an RJ45 (male) plug on the other end.

<!-- pdf page 135 | printed page 135 -->

Appendix A Software release history
The list below is a cumulative list of the new features introduced in
subsequent releases of the JCU-4 software, since the initial release
(v1.0.12).
This list includes new features only. It does NOT include
software maintenance items, such as bug fixes or
performance improvements.
To download the software, and view the complete list of all software
updates, including new features, bug fixes, and performance
improvements, visit:

  JCU-4 software download link

  www.bit.ly/jcu4-download

JCU-4, v1.0.15 new features:
(Software release date: August 2025)
• Maintenance release.
JCU-4, v1.0.12 new features:
(Software release date: April 2025)
• Initial public release.

Software release history                                                135

<!-- pdf page 136 -->

(no text layer on this page)

<!-- pdf page 137 -->

                                    Index
A
About this device .......................................... 62, 73, 85, 96, 107
Accessories
  Network adapter cables .................................................. 133
  Network cables ............................................................. 131
  Networking .................................................................. 129
  RayNet cables............................................................... 131
Applicable products........................................................... 15
Assigning a netmask...................................... 54, 67, 80, 92, 102
Assigning a static IP address ........................... 54, 67, 80, 91, 102

B
Box contents .................................................................... 25
Brightness ................................................... 57, 70, 83, 94, 104

C
Cable
  Bend radius................................................................... 37
  Protection ................................................................. 37–38
  Routing ........................................................................ 37
  Security........................................................................ 37
  Strain relief ................................................................... 37
Cables
  Extension ................................................................. 41, 44
  Network ................................................................... 41, 44
Cabling
  Circuit isolation.............................................................. 37
Camera detection .......................................... 55, 68, 81, 92, 103
Circuit isolation................................................................. 37
Cleaning
  Screen ........................................................................ 118
Compass safe distance ....................................................... 31
Compatible maritime cameras ............................................. 22
Configuration
  Web browser user interface ............................................. 112
    Diagnostics ............................................................... 116
    Log in........................................................................ 111
    Overview ................................................................... 111
    Product information .................................................... 112
    Setup ....................................................................... 113

      Joystick ................................................................. 113
      Network................................................................. 113
      Softkey .................................................................. 114
      System .................................................................. 115
Connecting cables ............................................................. 38
Connections
  Bare-ended wires ........................................................... 38
  Battery ......................................................................... 48
  Distribution panel........................................................... 48
  Grounding .................................................................... 50
  Wire ............................................................................ 38
Connections overview ........................................................ 40
Contact details................................................................. 124
Controllable cameras ..................................... 61, 72, 85, 95, 106

D
Declaration of Conformity ................................................... 12
Dimensions...................................................................... 28

E
Electromagnetic Compatibility ......................................... 12, 30
EMC, See Electromagnetic Compatibility

F
Factory reset ................................................ 63, 74, 86, 97, 108
Front cover fitting.............................................................. 35
Front cover removal........................................................... 33
Fuse ratings ..................................................................... 47
Fuse requirement .......................................................... 25, 46

I
Inline fuse............................................................... 25, 46–47
Inline fuse rating ............................................................... 47
Installation
  Best practice.................................................................. 49
  Front cover fitting ........................................................... 35
  Front cover removal........................................................ 33
  Mounting options........................................................... 33

<!-- pdf page 138 -->

  Retrofit mount ............................................................... 33
  Retrofit mounting ........................................................... 34
  Surface mount ............................................................... 33
  Surface mounting........................................................... 34
Interference ..................................................................... 31
     See also Compass safe distance

J
Joystick mode .............................................. 61, 72, 84, 95, 106

L
Location requirements ....................................................... 30
  General ........................................................................ 30

M
Maintenance ............................................................... 11, 118
Mounting
 Front cover fitting ........................................................... 35
 Front cover removal........................................................ 33
 Mounting options........................................................... 33
 Retrofit mount ............................................................... 33
 Retrofit mounting ........................................................... 34
 Surface mount ............................................................... 33
 Surface mounting........................................................... 34

N
Network
  cables ......................................................................... 133
  Cables......................................................................... 129
  PoE............................................................................. 129
  Switch......................................................................... 129
Network cable extension ................................................ 41, 44
Network connections
  Connections overview ..................................................... 40
  System overview (example only) ................................... 22, 41
New features................................................................... 135
Night mode.................................................. 57, 70, 83, 94, 105

O
Operation
 About this device ....................................... 62, 73, 85, 96, 107
 Brightness ................................................ 57, 70, 83, 94, 104
   Night mode ............................................ 57, 70, 83, 94, 105
 Camera detection ....................................... 55, 68, 81, 92, 103
 Controllable cameras .................................. 61, 72, 85, 95, 106
 Factory reset ............................................. 63, 74, 86, 97, 108
 Installation ................................................ 62, 72, 85, 96, 107
 Joystick mode ........................................... 61, 72, 84, 95, 106
 Power down .............................................. 56, 70, 82, 93, 104
 Powering on the unit................................... 53, 66, 79, 90, 101
 Select camera ............................................ 56, 69, 82, 93, 104
 Settings reset ............................................ 62, 73, 86, 96, 107
 Startup wizard ........................................... 53, 66, 79, 91, 101
   Assigning a netmask ................................ 54, 67, 80, 92, 102
   Assigning a static IP address...................... 54, 67, 80, 91, 102
   System selection ..................................... 53, 66, 79, 91, 101
 User-programmable buttons (UPBs).................... 75, 87, 97, 108
Operation (M100-Series / M200-Series)
 Controlled camera .......................................................... 92
 Controls overview .......................................................... 89
Operation (M300-Series)
 Assigning user-programmable buttons (via Web
  interface)..................................................................... 87
 Controls overview .......................................................... 78
 Status icons .................................................................. 81
Operation (M400-Series / M500-Series)
 Controls overview .......................................................... 65
 Status icons .................................................................. 68
Operation (M400XR / M500-Series)
 Ready to track ................................................................. 74
Operation (M460-Series / M560-Series)
 Controlled camera .......................................................... 55
 Controls overview .......................................................... 52
 JCU settings.................................................................. 58
 Ready to track ................................................................ 60
 Shortcut keys ................................................................ 58
 Status icons .................................................................. 55
Operation (MD-Series)
 Assigning user-programmable buttons (via OSD menu)........ 108
 Controlled camera ......................................................... 103
 Controls overview ......................................................... 100

<!-- pdf page 139 -->

P
Parts supplied................................................................... 25
Power
  Battery connection.......................................................... 48
  Cable extension ............................................................. 49
  Connection to battery...................................................... 49
  Connection to distribution panel........................................ 48
  Distribution ................................................................... 47
  Distribution panel........................................................... 48
  Fuses .................................................................. 25, 46–47
  Grounding .................................................................... 49
  Sharing a breaker ........................................................... 48
Power cable extension ....................................................... 49
Power connections
  Connections overview ..................................................... 40
  Direct power connection .................................................. 46
  Multiple power sources .......................................... 40, 43, 46
  Power options ...................................................... 40, 43, 46
  Power over Ethernet (PoE)................................................ 43
  Power Sourcing Equipment (PSE) ...................................... 43
    PoE injector connection ................................................ 44
    PoE network switch connection ...................................... 43
Power down................................................. 56, 70, 82, 93, 104
Power over Ethernet (PoE) .................................................. 43
Powering on the unit...................................... 53, 66, 79, 90, 101
Printed manual ................................................................. 15
Product dimensions ........................................................... 28
Product documentation
  Applicable documents..................................................... 15
  Related documents ......................................................... 15
Product overview .............................................................. 21
Product recycling (WEEE).................................................... 13
Product support ............................................................... 124

R
RayNet
  cables ................................................................... 131, 133
Ready to track (M400XR / M500-Series) .................................. 74
Ready to track (M460-Series / M560-Series) ............................ 60
Required additional components .......................................... 21
Retrofit mount .................................................................. 33
Retrofit mounting .............................................................. 34
RJ45
  cables ......................................................................... 133

Routine checks................................................................. 118

S
SeaTalkhs
  cables ......................................................................... 133
Select camera............................................... 56, 69, 82, 93, 104
Service Center ................................................................. 124
Servicing .................................................................... 11, 118
Settings reset ............................................... 62, 73, 86, 96, 107
Software release history .................................................... 135
Software Release Summary ................................................ 18
Software version ............................................................... 16
Spares ........................................................................... 128
Startup wizard .............................................. 53, 66, 79, 91, 101
Suppression ferrites ...................................................... 12, 31
     See also EMC
Surface mount.................................................................. 33
Surface mounting ............................................................. 34
System overview (example only)...................................... 22, 41
System selection........................................... 53, 66, 79, 91, 101

T
Technical specification
  Conformance specification .............................................. 126
  Display specification ...................................................... 126
  Environmental specification ............................................ 126
  Network specification..................................................... 126
  Physical specification ..................................................... 126
  Power specification........................................................ 126
Technical support ............................................................. 124
Thermal breaker ............................................................... 47
Thermal breaker rating....................................................... 47
Tools required .................................................................. 33
Troubleshooting............................................................... 120

U
User-programmable buttons (UPBs) ...................... 75, 87, 97, 108

<!-- pdf page 140 -->

V
Ventilation ....................................................................... 30

W
Warranty ........................................................................ 124
Web browser user interface
 Diagnostics .................................................................. 116
 Log in .......................................................................... 111
 Overview ...................................................................... 111
 Product information ....................................................... 112
 Setup .......................................................................... 113
   Joystick .................................................................... 113
   Network ................................................................... 113
   Softkey ..................................................................... 114
   System ..................................................................... 115
WEEE Directive ................................................................. 13
What’s in the box .............................................................. 25
