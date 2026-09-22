# PATHFINDER™

<!-- source: sources/SV-ECS/Pathfinder ECDIS & ECS System Commissioning & Acceptance Testing Instructions 81427 (Rev 1).pdf | extraction: extracted/SV-ECS/Pathfinder ECDIS & ECS System Commissioning & Acceptance Testing Instructions 81427 (Rev 1).md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: Wingdings is not a standard text face; glyphs "�" on pages 52-54, 56. Verify against the rendered page before trusting or mapping. -->
<!-- font check: U+FFFD (glyph with no Unicode mapping) on pages 52-54, 56; the character carries no meaning as text, read the rendered page -->
<!-- font check: no ToUnicode map in ProximaNova-Bold, ProximaNova-Light, QTypeSquarePro-Extlight, QTypeSquarePro-Light; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1 checked against the rendered page) -->

<!-- pdf page 1 -->

PATHFINDER™

##### COMMERCIAL ECDIS / ECS SYSTEM

### COMMISSIONING &

### ACCEPTANCE INSTRUCTIONS

- English (en-US)
- Date: 09-2025
- Document number: 81427 (Rev 1) © 2025 Raymarine UK Limited

<!-- figure 1 on pdf page 1 at 0,136-839,593 pt | caption: none | text-layer labels: PATHFINDER ™ | COMMERCIAL ECDIS / ECS SYSTEM | COMMISSIONING & ACCEPTANCE INSTRUCTIONS | OCR below floor, text not used (7/188 words >= 60, mean confidence 27) -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

###### Legal notices

<!-- omitted: "Trademark and patents notice" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair Use Statement" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Content notice" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Artificial Intelligence (AI) content notice" (pdf pages 3-5; 3 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 4 -->
<!-- pdf page 5 | printed page 5 -->
##### FCC Interference Statement (Part 15.105

##### Innovation, Science and Economic

##### Innovation, Sciences et Développement

##### CHAPTER 3 ECDIS PRODUCT AND SYSTEM

<!-- pdf page 6 | printed page 6 -->

##### Pathfinder Control Panel keyboard

##### CHAPTER 4 ECS PRODUCT AND SYSTEM

##### Pathfinder Control Panel keyboard

<!-- pdf page 7 | printed page 7 -->

<!-- pdf page 8 | printed page 8 -->

## CHAPTER 1: HEALTH & SAFETY

### Warnings and cautions

Note: The warnings and cautions detailed in this document apply to the installation and commissioning of the equipment. For warnings and cautions related to equipment operation please refer to the relevant operator’s instructions. For a list of applicable documents refer to: p.17 — Product documentation

### Risk assessment

In accordance with employer’s, vessel owner's and/or shipyard’s requirements, risk assessments of the work areas must be carried out prior to commencing installation of equipment. Risk assessments should be reviewed regularly.

### Aid to navigation

Unless specifically stated as “non-type approved”, the equipment detailed in this document comply with relevant SOLAS regulations and are provided as an aid to navigation. The equipment should be used in accordance with the SOLAS regulations.

### Safety warnings

##### Warning: Product installation and commissioning

- This product must be installed and operated in accordance with the instructions provided. Failure to do so could result in personal injury, damage to the vessel and/or poor product performance.
- The installation and commissioning of the equipment must be performed by an authorized engineer.
- Register product warranty and gain enhanced product warranty benefits on the Raymarine website: www.bit.ly/rym-warranty
- Incorrect or unauthorized installations can be dangerous and may void product warranty.

##### Warning: Fire Risk

Equipment may contain materials which produce toxic fumes if burnt.

##### Warning: Potential ignition source

This product is NOT approved for use in hazardous/flammable atmospheres. Do NOT install in a hazardous/flammable atmosphere (such as in an engine room or near fuel tanks).

##### Warning: High voltage

This product contains high voltage. Adjustments require specialized service procedures and tools only available to qualified service technicians. There are no user serviceable parts or adjustments. The operator should never remove the cover or attempt to service the product.

<!-- figure 1 on pdf page 8 at 427,65-492,258 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 8 at 427,265-492,318 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 20) -->

<!-- figure 3 on pdf page 8 at 427,325-801,392 pt | caption: none; nearest centred text below: "Warning: High voltage" | text-layer labels: Warning: Potential ignition source | nearby labels: Warning: High voltage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 8 at 427,397-801,488 pt | caption: none | text-layer labels: Warning: High voltage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 9 | printed page 9 -->

##### Warning: Switch off power supply

Ensure that the vessel’s power supply is switched OFF before starting to install this product. Do NOT connect or disconnect equipment with the power switched on, unless instructed to do so in this document.

##### Warning: Day mode brightness warning

Switching from Night mode to Day mode instantly increases the display brightness to maximum. This will impact the operator’s night vision, due to the relative brightness of Day mode in night time conditions.

### Product warnings

##### Warning: Positive ground systems

Do NOT connect this unit to a system which has positive grounding.

##### Warning: Power supply voltage

Connecting this product to a voltage supply greater than the specified maximum rating may cause permanent damage to the unit. For the correct voltage, refer to the information label affixed to the product.

##### Warning: Marine-grade sealant

Only use marine-grade neutral cure polyurethane sealants. Do NOT use sealants containing acetate or silicone, which can cause damage to plastic parts.

##### Warning: Product grounding

Before applying power to this product, it MUST be correctly grounded, in accordance with the instructions provided.

##### Warning: Anti-virus protection

This product does not include protection against computer viruses. Before inserting any memory device, ensure it is free from computer viruses by scanning the device with a suitable anti-virus application with up to date virus definitions.

##### Caution: Product weight

- Refer to the technical specification for your product to ensure the intended mounting surface is suitable to bear its weight.
- 2 people may be required for installation of larger / heavier products.

##### Caution: Power supply protection

When installing this product, ensure that the power source is adequately protected by means of a suitably-rated fuse or thermal circuit breaker.

##### Warning: Sun cover contains magnets

The display’s sun cover contains magnets which may interfere with magnetic sensitive devices (such as compasses, attitude sensors and gyroscopes). To prevent potential interference: • The display must be installed a safe distance away from magnetic sensitive devices. • When the display is in use the sun cover must be stored away from such devices.

9

<!-- figure 1 on pdf page 9 at 41,41-103,117 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 9 at 329,41-413,117 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 9 at 427,41-492,117 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 9 at 693,41-801,117 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 9 at 41,124-413,203 pt | caption: none | text-layer labels: Warning: Day mode brightness warning | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 6 on pdf page 9 at 427,124-492,220 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 7 on pdf page 9 at 657,124-801,220 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 8 on pdf page 9 at 427,227-492,292 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 9 on pdf page 9 at 715,227-801,292 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 10 on pdf page 9 at 331,253-413,306 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 11 on pdf page 9 at 41,256-103,306 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 12 on pdf page 9 at 41,313-413,390 pt | caption: none; nearest centred text below: "Warning: Marine-grade sealant" | text-layer labels: Warning: Power supply voltage | nearby labels: Warning: Marine-grade sealant | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 13 on pdf page 9 at 41,397-413,464 pt | caption: none; nearest centred text below: "Warning: Product grounding" | text-layer labels: Warning: Marine-grade sealant | nearby labels: Warning: Product grounding | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 14 on pdf page 9 at 41,469-413,524 pt | caption: none | text-layer labels: Warning: Product grounding | nearby labels: Health & Safety | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 78) -->
A
<!-- end of figure 14 -->

<!-- pdf page 10 | printed page 10 -->

##### Caution: Sun covers

- Sun covers are used to protect the display screen against the damaging effects of ultraviolet (UV) light. If your product is supplied with a sun cover always ensure it is fitted when the product is not in use.
- To avoid potential loss of the sun cover, ensure that the sun cover is removed when travelling at high speed, whether in the water or when the vessel is being towed.
- To avoid potential screen damage, ensure that the rear surface of the sun cover and the display screen are clean and free from debris before placing the sun cover on the screen.

##### Caution: Servicing, maintenance and repair

Servicing, maintenance and repair of this equipment can only be carried out by Raymarine authorized engineers. Unauthorized servicing, maintenance and repair of the equipment will invalidate product warranty and require re-commissioning of the equipment.

### Regulatory notices

##### IHO standards

The latest standards can be viewed by visiting the IHO (International Hydrographic Organization) website at the following address: www.iho.int/

- Note: Raymarine UK Ltd is not responsible for the content of external websites.

<!-- omitted: "Open source license agreements" (pdf page 10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Disclaimer" (pdf page 10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
###### THIS INFORMATION IS MADE AVAILABLE BY Raymarine ON THE BASIS

THAT YOU EXCLUDE TO THE FULLEST EXTENT LAWFULLY PERMITTED ALL LIABILITY WHATSOEVER FOR ANY LOSS OR DAMAGE HOWSOEVER ARISING OUT OF THE USE OF THIS INFORMATION OR RELIANCE UPON THIS INFORMATION. Raymarine does not exclude Raymarine’s liability (if any) to you for personal injury or death resulting from Raymarine UK Ltd negligence, for fraud or for any matter which it would be illegal to exclude or to attempt to exclude.

##### Water ingress

Water ingress disclaimer Although the waterproof rating capacity of this product meets the stated water ingress protection standard (refer to the product’s Technical Specification), water intrusion and subsequent equipment failure may occur if the product is not installed correctly or subjected to high-pressure washing. Raymarine will not warrant products subjected to high-pressure washing.

<!-- figure 1 on pdf page 10 at 41,41-103,213 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 10 at 41,218-413,308 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 11 | printed page 11 -->

<!-- omitted: "Declaration of Conformity" (pdf page 11; 6 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
##### RF exposure

This equipment complies with FCC / ISED RF exposure limits for general population / uncontrolled exposure. The wireless LAN / Bluetooth antenna is mounted behind the front facia of the display. This equipment should be installed and operated with a minimum distance of 1 cm (0.39 in) between the device and the body. This transmitter must not be co-located or operating in conjunction with any other antenna or transmitter, except in accordance with FCC multi-transmitter product procedures.

<!-- omitted: "Compliance Statement (Part 15.19)" (pdf page 11; 5 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "FCC Interference Statement (Part 15.105 (b))" (pdf page 11; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
##### Innovation, Science and Economic Development Canada (ISED)

This device complies with License-exempt RSS standard(s). Operation is subject to the following two conditions: 1.   This device may not cause interference; and 2. This device must accept any interference, including interference that may cause undesired operation of the device. This Class B digital apparatus complies with Canadian ICES-003(B) / NMB-003(B).

##### Innovation, Sciences et Développement économique Canada (Français)

Cet appareil est conforme aux normes d'exemption de licence RSS. Son fonctionnement est soumis aux deux conditions suivantes: 1.   cet appareil ne doit pas causer d'interférence, et 11

<!-- pdf page 12 | printed page 12 -->

2. cet appareil doit accepter toute interférence, notamment les interférences qui peuvent affecter son fonctionnement. Cet appareil numérique de la classe B est conforme à la norme NMB-003 du Canada.

##### Approval certificates

Copies of the type approval certificates for the system can be obtained through the Raymarine Commercial website:: https://www.bit.ly/ray-commdocs

<!-- omitted: "Warranty policy and registration" (pdf page 12; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
##### Product disposal

Dispose of this product in accordance with the WEEE Directive. The Waste Electrical and Electronic Equipment (WEEE) Directive requires the recycling of waste electrical and electronic equipment which contains materials, components and substances that may be hazardous and present a risk to human health and the environment when WEEE is not handled correctly.

Equipment marked with the crossed-out wheeled bin symbol indicates that the equipment should not be disposed of in unsorted household waste. Local authorities in many regions have established collection schemes under which residents can dispose of waste electrical and electronic equipment at a recycling center or other collection point. For more information about suitable collection points for waste electrical and electronic equipment in your region, refer to the Raymarine website: https://bit.ly/rym-recycling

<!-- omitted: "Technical accuracy" (pdf page 12; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Publication copyright" (pdf pages 12-13; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 13 | printed page 13 -->
## CHAPTER 2: DOCUMENT INFORMATION

#### CHAPTER CONTENTS

<!-- pdf page 14 | printed page 14 -->

### 2.1 Handbooks

It is recommended that you read this document thoroughly before attempting installation, commissioning, or operation of this equipment. Ensure that you have read and understood all the specified warnings, cautions, location requirements, and limitations for the equipment. Ensure that you have read and understood cable routing requirements, connection requirements, connection methods, and configuration steps for the equipment and any connected devices.

### 2.2 Introduction

- This document details the commissioning and acceptance testing
- procedures for the following systems:
- Pathfinder ECDIS
- Pathfinder ECS

### 2.3 ECDIS — Applicable products

##### Applicable systems

This document is applicable to the following Pathfinder ECDIS systems:
- Pathfinder 24" ECDIS Single System, part number: T70615
- Pathfinder 24" ECDIS Dual System, part number: T70616

Note: The Dual system part number (T70616) includes hardware to create 2 complete, independent ECDIS stations, sharing a single eSyncBox.

##### ECDIS displays

- Pathfinder 24" ECDIS, part number: E70664-ECDIS. Including peripherals such as: the external alarm buzzer and external card reader.

<!-- figure 1 on pdf page 14 at 427,77-801,287 pt | caption: none | text-layer labels: none | nearby labels: ECDIS displays | The following displays are applicable: | OCR: no legible text (0/1 words >= 60, mean confidence 48) -->

<!-- pdf page 15 | printed page 15 -->

- eSyncBox, part number CW-50620

| • Pathfinder Trackball, part number A80788 | 2.4 ECS — Applicable products |
| --- | --- |
| Data Collection Unit (DCU) | Applicable systems |
| The following DCU-Series product is applicable: | This document is applicable to the following Pathfinder ECS systems: |

###### Single systems

- Pathfinder ECS 16" Single System, part number: T70609.
- Pathfinder ECS 19" Single System, part number: T70610.
- Pathfinder ECS 22" Single System, part number: T70611.

###### Dual systems

- Pathfinder ECS 16" Dual System, part number: T70612.
- Pathfinder ECS 19" Dual System, part number: T70613.
- Pathfinder ECS 22" Dual System, part number: T70614.
- Pathfinder DCU, part number A80792. Note: Dual systems include hardware to create 2 fully independent ECS stations, sharing a single eSyncBox.

<!-- figure 1 on pdf page 15 at 427,74-801,215 pt | caption: none | text-layer labels: none | nearby labels: eSyncBox gateway | The following gateway is applicable: | • eSyncBox , part number CW-50620 | OCR below floor, text not used (10/34 words >= 60, mean confidence 44) -->

<!-- figure 2 on pdf page 15 at 38,77-413,261 pt | caption: none | text-layer labels: none | nearby labels: Trackball | The following Trackball is applicable: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 15 at 38,330-413,481 pt | caption: none | text-layer labels: none | nearby labels: Data Collection Unit (DCU) | • Pathfinder DCU , part number A80792. | OCR: no legible text (0/19 words >= 60, mean confidence 24) -->

<!-- pdf page 16 | printed page 16 -->

| ECS displays | Data Collection Unit (DCU) |
| --- | --- |
| The following displays are applicable: | The following DCU-Series product is applicable: |

- Pathfinder ECS 16", part number: E70661–ECS.
- Pathfinder ECS 19", part number: E70662–ECS.
- Pathfinder ECS 22", part number: E70663–ECS.                                  • Pathfinder DCU-2, part number A80839.

Including supplied peripherals such as the external alarm buzzer and external card reader.                                                                    eSyncBox gateway The following gateway is applicable:

- eSyncBox, part number CW-50620

<!-- figure 1 on pdf page 16 at 427,69-801,328 pt | caption: none | text-layer labels: none | nearby labels: Data Collection Unit (DCU) | • Pathfinder DCU-2 , part number A80839. | OCR below floor, text not used (3/21 words >= 60, mean confidence 42) -->

<!-- figure 2 on pdf page 16 at 38,77-413,294 pt | caption: none | text-layer labels: none | nearby labels: ECS displays | The following displays are applicable: | OCR text follows (tesseract, unverified; 2/4 words >= 60, mean confidence 54) -->
BPR
BPR
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 16 at 427,390-801,531 pt | caption: none | text-layer labels: none | nearby labels: eSyncBox gateway | The following gateway is applicable: | • eSyncBox , part number CW-50620 | OCR below floor, text not used (11/40 words >= 60, mean confidence 42) -->

<!-- pdf page 17 | printed page 17 -->

### 2.5 Product documentation

The following documentation is applicable to the Pathfinder ECDIS System.

###### Applicable documents

| Document | Description |
| --- | --- |
| number |  |
| 81427 | Pathfinder ECDIS/ECS Commissioning & Acceptance Testing Instructions (This document). Commissioning and configuration details for ECDIS and ECS including acceptance testing and sign off. |
| 81422 | Pathfinder ECDIS Operator’s Instructions. Instructions for operators on how to use the system features and functions. |
| 87487 | Pathfinder ECDIS Installation Instructions. Installation details for ECDIS including system components. |
| 87497 | Pathfinder ECS Installation Instructions. Installation details for the ECS display including system components. |

### 2.6 Document conventions

The following conventions are used throughout this document.

###### Formatting of user interface menus and settings references

- References to menus, settings options and physical buttons are formatted using square brackets [].
- Examples:
- “Select [Guard Zone] from the [Additional features] menu.
- “Enable the [AIS] toggle switch to display AIS targets onscreen.”
- Swipe your finger from left to right across the [Power swipe] touch control. Procedures for performing specific tasks using the product’s user interface
- The term “Select” is used to refer to the action of:

- Trackball — moving the cursor over an item and clicking the left or right button.
- Touchscreen — using your finger to select a menu option or item on the screen. Examples:
- “Select [Ok] to confirm your selection.”
- “Select the target onscreen.” The term “Drag” is used to refer to the action of:
- Trackball — click and hold left or right button and use the ball to move the cursor.
- Touchscreen — using your finger to select an item and then moving your finger in the required direction. Procedures for navigating menu hierarchies Menu hierarchies are used in this document to provide a quick summary on how to access a particular function or menu option. References to menu hierarchies are formatted using square brackets [] with an arrow > separating each menu setting. Examples:
- “The CCRP location can be configured from the [Ownship] settings menu: [Standby screen > Settings > Ownship].”

### 2.7 Document illustrations and screenshots

Note:
- Whilst care is taken to ensure that the illustrations and screenshots provided in this document portray the latest hardware and software versions available, where differences are purely aesthetic, some illustrations and screenshots may depict an older version of hardware or software.
- The navigation and/or sensor data shown in screenshots may be simulated data and therefore may not reflect real world conditions.

<!-- pdf page 18 | printed page 18 -->

## CHAPTER 3: ECDIS PRODUCT AND SYSTEM OVERVIEW

#### CHAPTER CONTENTS

<!-- pdf page 19 | printed page 19 | header: Description -->

### 3.1 Pathfinder ECDIS overview

The Raymarine Commercial Pathfinder ECDIS comprises of a display with an integrated processor, a Data Collection Unit (DCU), an Internet gateway and display peripherals. The Raymarine Commercial Pathfinder ECDIS complies with IMO (International Maritime Organization) standards and is Type Approved to the ECDIS standard IEC 61174 edition 4. Pathfinder ECDIS is built on the Nautilus ECDIS Kernel, ensuring future S-100 support, reliable hardware and a software roadmap to S-100 compliance.

##### Standalone/Single ECDIS

A Single Pathfinder ECDIS should be set up as follows:

###### Description

| 1 | Pathfinder ECDIS — A display that is used for navigation and can show data from externally connected devices, to provide situational and navigational awareness. |
| --- | --- |
| 2 | RJ45 cable — Connects the eSyncBox to the ship’s WAN connection (NOT supplied). |

| 3 | Alarm buzzer — The alarm buzzer is used to provide an audible alert of a situation requiring the user’s attention. The alarm buzzer is mandatory for the Pathfinder ECDIS, as the display does not include a built-in buzzer or speaker. |
| --- | --- |
| 4 | External card reader — The external card reader is used to backup and restore user data and settings. |
| 5 | RayNet to RJ45 cable — Connects the display to the eSyncBox. |
| 6 | External sensors — External sensors are connected to the DCU’s NMEA 0183 inputs. |
| 7 | eSyncBox — Cyber security data gateway. |
| 8 | Pathfinder DCU (Data Collection Unit) — Collects data transmitted by externally connected devices and transmits the data over Ethernet, so that it can be shown on the display. |
| 9 | DCU power cable — A cable is required to power the DCU (NOT supplied). |
| 10 | RayNet to RJ45 cable — Transfers data from the DCU to the display. |
| 11 | Trackball — Used to control the display and interact with its user interface. |
| 12 | Display power cable — The cable is used to power the display. |

Note: The external sensors, eSyncBox’s WAN connection cable and the DCU’s power cable are not supplied with the system. All other components and cables are supplied when ordering a Single Pathfinder ECDIS, part number: T70615.

<!-- figure 1 on pdf page 19 at 38,227-413,452 pt | caption: none; nearest centred text below: "Pathfinder ECDIS — A display that is used for navigation and can" | text-layer labels: Description | nearby labels: Standalone/Single ECDIS | 7 | 8 | 9 | 10 | 11 | 12 | 1 | OCR below floor, text not used (2/7 words >= 60, mean confidence 44) -->

<!-- pdf page 20 | printed page 20 | header: Description -->

##### Dual ECDIS

A Dual Pathfinder ECDIS should be set up as follows:

###### Description

1      RayNet to RayNet 10 m (32.8 ft) cable — Used to create a direct Ethernet connection between the primary and secondary stations.

Note: Useful for installations where the distance between primary and secondary stations precludes both stations being connected directly to the eSyncBox.

2      Pathfinder ECDIS — A display that is used for navigation and can show data from externally connected devices, to provide situational and navigational awareness.

| 3 | Alarm buzzer — The alarm buzzer is used to provide an audible alert of a situation requiring the user’s attention. The alarm buzzer is mandatory for the Pathfinder ECDIS system, as the display does not include a built-in buzzer or speaker. |
| --- | --- |
| 4 | External card reader — The external card reader is used to backup and restore user data and settings. |
| 5 | RJ45 cable — Connects the eSyncBox to the ship’s WAN connection (NOT supplied). |
| 6 | eSyncBox — Cyber security data gateway. |
| 7 | Display power cables — The cables are used to power the displays. |
| 8 | Trackball — Used to control the display and interact with its user interface. |
| 9 | RayNet to RJ45 adaptor cables. |
| 10 | Pathfinder DCU (Data Collection Unit) — Collects data transmitted by externally connected devices and transmits the data over Ethernet, so that it can be shown on the display. |
| 11 | DCU power cable — A cable is required to power the DCU (NOT supplied). |
| 12 | External sensors — External sensors are connected to the DCU’s NMEA 0183 inputs. |

Note: The external sensors, eSyncBox’s WAN connection cable and the power cables for the DCUs are not supplied with the system. All other components and cables are supplied when ordering a Dual Pathfinder ECDIS, part number: T70616.

###### Secondary (backup) station

Full redundancy is achievable using a complete second station. The secondary station is connected to the primary station via the Ethernet network so that routes, updates and other information can be shared between the 2 stations.

<!-- figure 1 on pdf page 20 at 38,77-413,390 pt | caption: none; nearest centred text below: "RayNet to RayNet 10 m (32.8 ft) cable — Used to create a direct" | text-layer labels: Description | nearby labels: Dual ECDIS | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 1 | OCR text follows (tesseract, unverified; 7/15 words >= 60, mean confidence 60) -->
PSU
PSU 1
12
24V de
de
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 20 at 82,428-391,495 pt | caption: none; nearest centred text below: "Pathfinder ECDIS — A display that is used for navigation and can" | text-layer labels: Note: | nearby labels: 1 | 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 21 | printed page 21 | header: Description -->

The 2 stations will operate as 2 standalone stations. In the event of a system fault the user can switch to the secondary station so that the faulty station can be diagnosed and repaired without impacting operations.

###### Sensor redundancy

Further sensor redundancy can be achieved by having both sets of sensors connected to the DCU in both the primary and secondary stations.

##### Radar & ECDIS system

The Pathfinder Radar Display and the Pathfinder ECDIS can be in a combined system. In a combined system the sensor data received via the DCU is shared.

###### Description

1      Cyclone Pro radar scanner with 6 ft antenna — Detects targets by transmitting microwaves and generating a picture on the Radar Display using the microwaves reflected from the objects. 2      Alarm buzzer — The alarm buzzer is used to provide an audible alert of a situation requiring the user’s attention. The alarm buzzer is mandatory part of the system as there is no built-in buzzer or speaker.

| 3 | External card reader — The external card reader is used to backup and restore user data and settings. |
| --- | --- |
| 4 | VCM100 — The radar scanner’s Voltage Control Module (VCM) provides power to the radar scanner. |
| 5 | Pathfinder Radar Display — A display that shows the radar image and data from externally connected devices, to provide situational and navigational awareness. |
| 6 | Pathfinder ECDIS — A display that is used for navigation and can show data from externally connected devices, to provide situational and navigational awareness. |
| 7 | Radar power cable — Connects the radar scanner to the VCM100. |
| 8 | RayNet to RayNet cable (white) — Transfers data from the radar scanner to the Radar Display. |
| 9 | Display power cables — The cables provides power to the displays. |
| 10 | RJ45 cable — Connects the eSyncBox to the ship’s WAN connection. (NOT supplied). |
| 11 | VCM power cable — A cable is required to provide power to the VCM100 (NOT supplied). |
| 12 | RayNet to RJ45 cables. |
| 13 | Pathfinder Trackball — Used to control the display it is connected to and interact with its user interface. |
| 14 | Pathfinder DCU (Data Collection Unit) — Collects data transmitted by externally connected devices and transmits the data over Ethernet, so that it can be shown on the display. |
| 15 | External sensors — External sensors are connected to the DCU’s NMEA 0183 inputs. |
| 16 | eSyncBox — Cyber security data gateway (The eSyncBox is supplied with the ECDIS. |
| 17 | RJ45 cable (NOT supplied). |
| 18 | DCU power cable — A cable is required to power the DCU (NOT supplied). |

<!-- figure 1 on pdf page 21 at 38,203-413,449 pt | caption: none | text-layer labels: Description | nearby labels: 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 1 | 15 | 16 | 17 | OCR text follows (tesseract, unverified; 22/34 words >= 60, mean confidence 67) -->
2?
2?
<5 6?
10
9?
9
12?
12?
13?
14
sensors
AIS
15°
*16
GNSS (GPS)
Speed
$17
Depth
18
Wind
<!-- end of figure 1 -->

<!-- pdf page 22 | printed page 22 -->

3.2 Display overview                                                           • Waterproof to IPx6, IPx7 (suitable for above or below decks installation).

The displays are type approved, glass bridge style touchscreen displays with an integrated navigation processor.

### 3.3 DCU overview

The DCU is a Data Collection Unit which converts data received from external devices and transfers the data over Ethernet so that it can be displayed onscreen.

| • 24 inch screen. | • 8 Configurable Opto-isolated inputs (Listeners). |
| --- | --- |
| • 1920 x 1200 resolution. | • 6 Configurable ISO-Drive isolated outputs (Talkers). |
| • Hexacore (6-core) processor. | • 1 Bidirectional, configurable, isolated serial port. |
| • 64 GByte internal solid state storage, for user data. | • Automatic baud rate matching on inputs. |
| • Edge-to-edge glass construction. | • Advanced data filtering/routing. |
| • Multi-point touchscreen. | • 1 Alarm output relay (N/O and N/C contacts). |
| • Full HD IPS display. | • Mode input pins to set operating mode without PC. |
| • Hydrotough nano-coated, impact-resistant glass screen, which repels | • Diagnostics LEDs on all inputs and outputs. |
| water, oil, and smudges for better viewing and accurate touch controls. | • Alarm status LED / Mode LED / Bi-color status LED. |
| • Wide viewing angles. | • Durable stainless steel housing. |
| • Integrated 3 port network switch. |  |
| • USB input for control. | • Panel mountable. |
| • External memory card reader connection, via RCR-SDUSB card reader |  |
| (Part number: A80440). |  |

<!-- figure 1 on pdf page 22 at 38,98-413,304 pt | caption: none | text-layer labels: none | nearby labels: Display features include: | • 24 inch screen. | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 63) -->
DR
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 22 at 427,153-801,299 pt | caption: none | text-layer labels: none | nearby labels: DCU features: | OCR below floor, text not used (7/20 words >= 60, mean confidence 44) -->

<!-- pdf page 23 | printed page 23 -->

### 3.4 Pathfinder Trackball overview

- The Pathfinder Trackball (part number: A80788) is a USB trackball that can be used to control the system.

###### Trackball features:

- USB communication and power.
- Infrared optical navigation technology.
- Sealed 38 mm (1.5 in) ball providing precise cursor movement.
- Integrated left, middle and right buttons.
- Integrated scroll wheel.
- IP68 Ingress protection rating (fully waterproof).
- Removable ball for easy cleaning.
- Installation options: panel mounting.
- 2 m (6.56 ft) fitted cable with USB A connector.

### 3.5 eSyncBox overview

- The eSyncBox (part number: CW-50620) is a cyber security data gateway that can be used to connect to the ChartWorld eSync service.

The eSyncBox is IEC 61162–460 compliant and uses a secure VPN tunnel so that data can be exchanged safely between the eSyncBox and the NavCloud ChartWorld server. eSync eliminates the need for AVCS (Admiralty Vectors Chart Service) data stored on physical media onboard vessels. eSync protects and secures the network using a multi-layer inspection firewall, network and transport layer access control (based on addresses, ports, and protocols) and enables download, installation and storage of weekly AVCS Base Media, exchange of MyRA routes and CIO+ data files between the system and the NavCloud ChartWorld servers. The eSyncBox offers a wired Ethernet WAN port, Cellular (4G) and Wi-Fi connections which can be used to connect directly or in-directly to the Internet.

### 3.6 Additional components

The following additional devices are required to provide data to the system:
- A gyro-compass or transmitting heading device (THD)
- Speed and Distance Measuring Equipment (SDME)
- An Electronic Position Fixing System (EPFS)
- An Automatic Identification System (AIS); or:

<!-- figure 1 on pdf page 23 at 427,98-801,234 pt | caption: none | text-layer labels: none | OCR below floor, text not used (11/38 words >= 60, mean confidence 44) -->

<!-- figure 2 on pdf page 23 at 38,100-413,280 pt | caption: none | text-layer labels: none | nearby labels: Trackball features: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 24 | printed page 24 -->

- Other sensors or networks providing equivalent information acceptable to the IMO (e.g.: an INS).

### 3.7 Optional accessories

- A number of optional accessories are available that can be used to control the system. Optional accessories must be ordered separately.
- The following accessories are available:
- Pathfinder Control Panel keyboard.
- Pathfinder Keyboard.

##### Pathfinder Control Panel keyboard overview

- The Pathfinder Control Panel (part number: A80790) is a USB keyboard with an integrated trackball that can be used to control the system.

###### Keyboard features:

- USB communication and power.
- Full QWERTY keyboard.
- ECDIS function buttons.
- 2 x large rotary encoders for VRM and EBL.
- 3 x small rotary encoders for Gain, Rain and Sea clutter.
- Backlit silicone keyboard.

- Integrated sealed trackball with buttons and scroll wheel.
- IP65 Ingress protection rating.
- Installation options: Desktop.
- 1.60 m (5.25 ft) fitted cable with USB A connector.

Pathfinder Control Panel keyboard controls

1. Full QWERTY keyboard.
2. EBL rotary controls.
3. Gain, Rain and Sea clutter controls.
4. VRM rotary controls.
5. Range, Radar and AIS controls.
6. 3 button trackball.

<!-- figure 1 on pdf page 24 at 427,134-801,313 pt | caption: none | text-layer labels: none | nearby labels: 1. | Full QWERTY keyboard. | 2. EBL rotary controls. | OCR text follows (tesseract, unverified; 45/63 words >= 60, mean confidence 71) -->
1
2
3
4
5
6
EBL
Gain
Rain
Sea
Ese
a
Dal
1
2
3
6
8
Q
w
E
R
Y
U
Teb
D
F
H
J
K
TR
Ener
Shift
x
v
B
N
M
shift
a
Fa
A
Alt
ACK
ve
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 24 at 38,258-413,416 pt | caption: none | text-layer labels: none | nearby labels: 1. | 3. | 4. | Keyboard features: | OCR text follows (tesseract, unverified; 40/62 words >= 60, mean confidence 69) -->
EBL
Gain
Rain
Sea
Eso
Fi
Fé
el
1
2
3
4
8
w
E
R
Y
Tab
Caps Lock
A
D
F
G
H
J
K
TR
shift
x
c
v
B
N
M
Shift
AIS
At
A
ACK
<!-- end of figure 2 -->

<!-- pdf page 25 | printed page 25 -->

##### Pathfinder Keyboard overview

The Pathfinder Keyboard (part number A80789) is a USB keyboard that can be used in conjunction with a Trackball to control the system.

###### Keyboard features

- USB communication and power.
- Full QWERTY keyboard.
- Separate Numerical/control keypads.
- Dimmable backlit keyboard.
- A Pathfinder Trackball can be connected via the keyboard.
- IP67 Ingress protection rating.
- Installation options: Panel mounting.
- 1.60 m (5.25 ft) fitted cable with USB A connector.

<!-- figure 1 on pdf page 25 at 38,93-413,275 pt | caption: none | text-layer labels: none | nearby labels: Keyboard features | OCR text follows (tesseract, unverified; 6/9 words >= 60, mean confidence 71) -->
Num
Caps
Lock
Lock
Goes
Enter
<!-- end of figure 1 -->

<!-- pdf page 26 | printed page 26 -->

## CHAPTER 4: ECS PRODUCT AND SYSTEM OVERVIEW

#### CHAPTER CONTENTS

<!-- pdf page 27 | printed page 27 | header: Description -->

### 4.1 Pathfinder ECS overview

The Raymarine Commercial Pathfinder ECS comprises of a display with an integrated processor, a Data Collection Unit (DCU), an Internet gateway and display peripherals. The Raymarine Commercial Pathfinder ECS complies with the UK Maritime and Coastguard Agency’s (MCA) Small Vessel Electronic Chart System (SV-ECS) standard. Pathfinder ECS utilizes the Pathfinder ECDIS operating system which is built on the Nautilus ECDIS Kernel, ensuring future S-100 support, reliable hardware and a software roadmap to S-100 compliance.

##### Standalone/Single ECS

A Single Pathfinder ECS should be set up as follows:

###### Description

| 1 | Pathfinder ECS — A display that is used for navigation and can show data from externally connected devices, to provide situational and navigational awareness. |
| --- | --- |
| 2 | RJ45 cable — Connects the eSyncBox to the ship’s WAN connection. |

| 3 | Alarm buzzer — The alarm buzzer is used to provide an audible alert of a situation requiring the user’s attention. The alarm buzzer is mandatory for the Pathfinder ECS system, as the display does not include a built-in buzzer or speaker. |
| --- | --- |
| 4 | External card reader — The external card reader is used to backup and restore user data and settings. |
| 5 | RayNet to RJ45 cable — Connects the eSyncBox to the display. |
| 6 | External sensors — External sensors are connected to the DCU-2’s NMEA 0183 inputs or to an NMEA 2000 network that the DCU-2 is also connected. |
| 7 | eSyncBox — Cyber security data gateway. |
| 8 | DCU-2 (Data Collection Unit 2) — Collects data transmitted by externally connected devices and transmits the data over Ethernet, so that it can be shown on the display. |
| 9 | DCU-2 power cable — A cable is required to power the DCU-2 (NOT supplied). |
| 10 | RayNet to RJ45 cable — Transfers data from the DCU-2 to the display. |
| 11 | Display power cable — The cable is used to power the display. |

Note: The external sensors, eSyncBox’s WAN connection cable and the DCU-2’s power cable are not supplied with the system. All other components and cables are supplied when ordering a Single Pathfinder ECS.

<!-- figure 1 on pdf page 27 at 38,239-413,442 pt | caption: none; nearest centred text below: "Pathfinder ECS — A display that is used for navigation and can" | text-layer labels: Description | nearby labels: Standalone/Single ECS | 7 | 8 | 9 | 10 | 11 | 1 | OCR text follows (tesseract, unverified; 4/8 words >= 60, mean confidence 57) -->
PSU
12
24V de
<!-- end of figure 1 -->

<!-- pdf page 28 | printed page 28 | header: Description -->

##### Dual ECS

- The Dual Pathfinder ECS provides complete system redundancy and should
- be set up as follows:

###### Description

1       RayNet to RayNet 10 m (32.8 ft) cable — Used to create a direct Ethernet connection between the primary and secondary stations.

Note: Useful for installations where the distance between primary and secondary stations precludes both stations being connected directly to the eSyncBox.

2       Pathfinder ECS — A display that is used for navigation and can show data from externally connected devices, to provide situational and navigational awareness.

| 3 | Alarm buzzer — The alarm buzzer is used to provide an audible alert of a situation requiring the user’s attention. The alarm buzzer is mandatory for the Pathfinder ECS system, as the display does not include a built-in buzzer or speaker. |
| --- | --- |
| 4 | External card reader — The external card reader is used to backup and restore user data and settings. |
| 5 | Display power cable — The cable is used to power the display. |
| 6 | eSyncBox — Cyber security data gateway. |
| 7 | RJ45 cable — Connects the eSyncBox to the ship’s WAN connection. |
| 8 | RayNet to RJ45 adaptor cables. |
| 9 | DCU-2 (Data Collection Unit 2) — Collects data transmitted by externally connected devices and transmits the data over Ethernet, so that it can be shown on the display. |
| 10 | DCU-2 power cable — A cable is required to power the DCU-2 (NOT supplied). |
| 11 | External sensors — External sensors are connected to the DCU-2’s NMEA 0183 inputs or to an NMEA 2000 network that the DCU-2 is also connected. |

Note: The external sensors, eSyncBox’s WAN connection cable and the power cables for the DCU-2s are not supplied with the system. All other components and cables are supplied when ordering a Dual Pathfinder ECS.

Secondary (backup) station Full redundancy is achievable using a complete second station. The secondary station is connected to the primary station via the Ethernet network so that routes, updates and other information can be shared between the 2 stations. The 2 stations will operate as 2 standalone stations. In the event of a system fault the user can switch to the secondary station so that the faulty station can be diagnosed and repaired without impacting operations.

<!-- figure 1 on pdf page 28 at 38,88-413,387 pt | caption: none; nearest centred text below: "RayNet to RayNet 10 m (32.8 ft) cable — Used to create a direct" | text-layer labels: Description | nearby labels: 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 1 | OCR text follows (tesseract, unverified; 10/15 words >= 60, mean confidence 68) -->
PSU O
PSU 1
12
12 V
dc
24V dc
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 28 at 82,428-391,492 pt | caption: none; nearest centred text below: "Pathfinder ECS — A display that is used for navigation and can" | text-layer labels: Note: | nearby labels: 1 | 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 29 | printed page 29 -->

Sensor redundancy Further sensor redundancy can be achieved by having both sets of sensors connected to the DCU in both the primary and secondary stations.

### 4.2 Display overview

The displays are, glass bridge style touchscreen displays that include an integrated navigation processor.

Display features include:
- Available in 16”, 19” and 22” screens.
- 1920 x 1080 FHD resolution.
- Hexacore (6-core) processor.
- 64 GByte internal solid state storage, for user data.
- Edge-to-edge glass construction.
- Multi-point touchscreen.
- Full HD IPS display.
- Hydrotough nano-coated, impact-resistant glass screen, which repels water, oil, and smudges for better viewing and accurate touch controls.
- Wide viewing angles.

- Integrated 3 port network switch.
- USB-A connection for optional input devices.
- External memory card reader connection, via RCR-SDUSB card reader (Part number: A80440).
- Waterproof to IPx6, IPx7 (suitable for above or below decks installation).

### 4.3 DCU-2 overview

The DCU-2 is a Data Collection Unit which converts data received from external sensors and transmits the data over the Ethernet connection so that it can be displayed onscreen.

DCU-2 features:
- 5 Configurable Opto-isolated inputs (Listeners).
- 2 Configurable ISO-Drive outputs (Talkers).
- 1 Bidirectional, configurable, isolated serial port.
- NMEA 2000 DeviceNet port.

<!-- figure 1 on pdf page 29 at 38,158-413,375 pt | caption: none | text-layer labels: none | OCR below floor, text not used (1/5 words >= 60, mean confidence 45) -->

<!-- figure 2 on pdf page 29 at 427,208-801,464 pt | caption: none | text-layer labels: none | nearby labels: DCU-2 features: | OCR below floor, text not used (7/25 words >= 60, mean confidence 34) -->

<!-- pdf page 30 | printed page 30 -->

- Automatic baud rate matching on inputs.
- Advanced data filtering/routing.
- Mode input pins to set operating mode without PC.
- Diagnostics LEDs on all inputs and outputs.
- Bi-color status LED.
- Durable stainless steel housing.
- Panel mountable.

### 4.4 eSyncBox overview

- The eSyncBox (part number: CW-50620) is a cyber security data gateway that can be used to connect to the ChartWorld eSync service.

The eSyncBox is IEC 61162–460 compliant and uses a secure VPN tunnel so that data can be exchanged safely between the eSyncBox and the NavCloud ChartWorld server. eSync eliminates the need for AVCS (Admiralty Vectors Chart Service) data stored on physical media onboard vessels. eSync protects and secures the network using a multi-layer inspection firewall, network and transport layer access control (based on addresses, ports, and protocols) and enables download, installation and storage of weekly AVCS Base Media, exchange of MyRA routes and CIO+ data files between the system and the NavCloud ChartWorld servers. The eSyncBox offers a wired Ethernet WAN port, Cellular (4G) and Wi-Fi connections which can be used to connect directly or in-directly to the Internet.

### 4.5 Additional components

The following additional devices are required to provide data to the system:
- A gyro-compass or transmitting heading device (THD)
- Speed and Distance Measuring Equipment (SDME)
- An Electronic Position Fixing System (EPFS)
- An Automatic Identification System (AIS); or:
- Other sensors or networks providing equivalent information acceptable to the IMO (e.g.: an INS).

### 4.6 Optional accessories

- A number of optional accessories are available that can be used to control the system. Optional accessories must be ordered separately.
- The following accessories are available:
- Pathfinder Trackball.
- Pathfinder Control Panel keyboard.
- Pathfinder Keyboard.

<!-- figure 1 on pdf page 30 at 38,241-413,375 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 12/26 words >= 60, mean confidence 54) -->
i
al
LAN2
CONSOLE
USB2
2>
USB1
WAN
LAN1
LAN3
HDMI
OTG
<!-- end of figure 1 -->

<!-- pdf page 31 | printed page 31 -->

##### Pathfinder Trackball overview

- The Pathfinder Trackball (part number: A80788) is a USB trackball that can be used to control the system.

###### Trackball features:

- USB communication and power.
- Infrared optical navigation technology.
- Sealed 38 mm (1.5 in) ball providing precise cursor movement.
- Integrated left, middle and right buttons.
- Integrated scroll wheel.
- IP68 Ingress protection rating (fully waterproof).
- Removable ball for easy cleaning.
- Installation options: panel mounting.
- 2 m (6.56 ft) fitted cable with USB A connector.

##### Pathfinder Control Panel keyboard overview

- The Pathfinder Control Panel (part number: A80790) is a USB keyboard with an integrated trackball that can be used to control the system.

###### Keyboard features:

- USB communication and power.
- Full QWERTY keyboard.
- ECDIS function buttons.
- 2 x large rotary encoders for VRM and EBL.
- 3 x small rotary encoders for Gain, Rain and Sea clutter.
- Backlit silicone keyboard.
- Integrated sealed trackball with buttons and scroll wheel.
- IP65 Ingress protection rating.
- Installation options: Desktop.
- 1.60 m (5.25 ft) fitted cable with USB A connector.

<!-- figure 1 on pdf page 31 at 427,88-801,246 pt | caption: none | text-layer labels: none | nearby labels: Keyboard features: | OCR text follows (tesseract, unverified; 39/64 words >= 60, mean confidence 66) -->
EBL
Gain
Sea
Rain
Esc
Fa
Dal
1
2
3
5
6
Q
w
E
R
Y
Tab
1X
On/Off
s
G
D
H
J
K
TR
Shift
Shift
x
v
B
N
M
OniOff
At
Alt
ACK
ve
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 31 at 38,93-413,273 pt | caption: none | text-layer labels: none | nearby labels: Trackball features: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 32 | printed page 32 -->

Pathfinder Control Panel keyboard controls

1. Full QWERTY keyboard.
2. EBL rotary controls.
3. Gain, Rain and Sea clutter controls.
4. VRM rotary controls.
5. Range, Radar and AIS controls.
6. 3 button trackball.

##### Pathfinder Keyboard overview

The Pathfinder Keyboard (part number A80789) is a USB keyboard that can be used in conjunction with a Trackball to control the system.

###### Keyboard features

- USB communication and power.
- Full QWERTY keyboard.
- Separate Numerical/control keypads.
- Dimmable backlit keyboard.
- A Pathfinder Trackball can be connected via the keyboard.
- IP67 Ingress protection rating.
- Installation options: Panel mounting.
- 1.60 m (5.25 ft) fitted cable with USB A connector.

<!-- figure 1 on pdf page 32 at 38,57-413,237 pt | caption: none | text-layer labels: none | nearby labels: 1. | Full QWERTY keyboard. | 2. EBL rotary controls. | OCR text follows (tesseract, unverified; 48/66 words >= 60, mean confidence 73) -->
1
2
3
4
5
6
EBL
Gain
Rain
Sea
Esc
Fé
Fé
el
3
4
5
8
Y
Q
w
E
R
U
Tab
Cape Lock
D
F
G
H
J
K
TR
Shift
Shift
x
c
v
B
N
M
AIS On/Off
At
Alt
ACK
ve
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 32 at 427,93-801,275 pt | caption: none | text-layer labels: none | nearby labels: Keyboard features | OCR text follows (tesseract, unverified; 5/9 words >= 60, mean confidence 61) -->
Num
Caps
Lock
OO)
Enter
<!-- end of figure 2 -->

<!-- pdf page 33 | printed page 33 -->

## CHAPTER 5: SOFTWARE DETAILS

#### CHAPTER CONTENTS

Software details                                      33

<!-- pdf page 34 | printed page 34 -->

### 5.1 Software

This document is applicable to the following software:

| Software name | Software version |
| --- | --- |
| Pathfinder ECDIS | v1.0 |

Important: Running any software other than that supplied with the display will invalidate the product warranty.

- Note: This software is used on Pathfinder ECDIS and Pathfinder ECS.

### 5.2 Performing a software update

From time to time software updates will be available which will improve available features and functionality. Software update files will be provided by Raymarine or an authorized dealer The current software version can be found in the [Maintenance] setting menu: [Taskbar > Additional Features > Settings > Maintenance].

- Note: Access to the [Settings] menu is password protected.

1. Copy the software update ISO file to a folder named “PathfinderUpgrades” which must be located in the root directory of a compatible memory card.
2. Insert the card into the external card reader.
3. Select the [Update Display] button from the [Maintenance] setting menu.
4. Select [Yes] to confirm you want to install the software update. The software update will be performed and the system will reboot. Once the update process is complete, the software version on the [Maintenance] setting will be updated to reflect the new software version.

<!-- figure 1 on pdf page 34 at 38,84-413,294 pt | caption: none; nearest centred text below: "Software version" | text-layer labels: none | nearby labels: Software name | Software version | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 79) -->
PATHFINDER
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 34 at 427,201-801,411 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 40/46 words >= 60, mean confidence 83) -->
General Settings
Network
This Display
Ownship
External Devices
Alert Settings
integrity
Backup Restore
Backup Everything
Diagnostics
Capture Screen
Backup Everything
External SD 1
‘Save all products logs
18
Updates
Text
eh
Update Radar
Certificate
App version
Platform version
Bundle version
<!-- end of figure 2 -->

<!-- pdf page 35 | printed page 35 -->

## CHAPTER 6: COMMISSIONING

#### CHAPTER CONTENTS

<!-- pdf page 36 | printed page 36 -->

### 6.1 Before you begin

##### Warnings and cautions

Important: Before proceeding, ensure that you have read and understood the warnings and cautions provided in the following section of this document: p.8 — Health & Safety

##### Handbooks

It is recommended that you read this document thoroughly before attempting installation, commissioning, or operation of this equipment. Ensure that you have read and understood all the specified warnings, cautions, location requirements, and limitations for the equipment. Ensure that you have read and understood cable routing requirements, connection requirements, connection methods, and configuration steps for the equipment and any connected devices.

##### Laptop computer

The configuration of the DCU-Series product requires connection to a laptop computer. A suitable Ethernet LAN cable will be required to connected the laptop to the converter.

##### Warning: Anti-virus protection

This product does not include protection against computer viruses. Before inserting any memory device, ensure it is free from computer viruses by scanning the device with a suitable anti-virus application with up to date virus definitions.

##### Password protection

The settings menus required for setup and commissioning of the equipment are password protected. The password must be obtained prior to commencing commissioning.

The password is not provided in this document. The password cannot be changed.

Important:
- Unauthorized access to the settings menus is prohibited.
- Commissioning by unauthorized or untrained persons will invalidate the equipment’s warranty.
- NEVER COMMUNICATE THE PASSWORD TO ANYONE WITHOUT EXPRESS PERMISSION FROM Raymarine UK Ltd.

##### System checks

The system must only contain the equipment listed as compatible in the System overview section. No other equipment should be connected to the system.

##### Software checks

The commissioning engineer must ensure that all equipment has the latest available software installed.

Note:
- Failure to upgrade software to the latest versions may cause equipment to not communicate properly and may prevent successful commissioning of the system.
- Equipment must never be downgraded without the express permission of Raymarine UK Ltd.

<!-- figure 1 on pdf page 36 at 307,392-413,471 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 36 at 41,394-103,471 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 37 | printed page 37 -->

| Commissioning process | 6.2 System set up |
| --- | --- |
| The commissioning steps are shown below: | To set up the system, first work through the [General Settings] menu |
| Sequence      Step | completing the relevant fields. |
| 1             Install and connect all hardware in accordance with the |  |
| relevant Installation Instructions: |  |
| • Pathfinder DCU-Series Installation Instructions |  |
| (document number: 87487), or |  |
| • Pathfinder ECS Installation Instructions (document |  |
| number: 87497). |  |
| 2             Read this document thoroughly. |  |
| 3             Familiarize yourself with the operational features by reading | The [General Settings] menu is accessed by selecting the “3 dots” [Additional |
| the Pathfinder ECDIS Operator’s Instructions (document | Features] icon located on the [Taskbar] and selecting [Settings]. |
| number: 81422). | The [General Settings] menu is password protected. |
| 4             Perform systems checks to ensure only compatible |  |
| products are connected to the system. |  |

##### General Settings menu

| 5 | Perform any required software upgrades. | The [General Settings] menu provides settings required during initial set up |
| --- | --- | --- |
| 6 | Configure the settings on the [This display] settings menus     and commissioning of the system. |  |
| 7 | Configure the settings from the [Ownship] settings menu. | The [General Settings] menu is divided into different menus, which are accessed by selecting the tabs at the top of the screen. The following menus |
| 8 | Check configured external devices. Add and configure any additional required external devices from the [External Devices] settings menu. | are available: • [This display] |
| 9 | Configure alerts and alert audio from the [Alert Settings] menu. | • [Ownship] • [External Devices] |
| 10 | Perform functional tests. | • [Integrity] |
| 11 | Complete acceptance testing and complete the test records. | • [Network] • [Alert Settings] |
| 12 | Backup the settings and user data to both internal and external memory. | • [Maintenance] |
| 13 | Complete warranty registration for the equipment. | This Display settings menu The [This Display] settings menu includes information and options related to the system. The [This Display] settings menu is the default settings menu displayed when selecting the [Settings] from the [Additional Features] menu. The following information and options are available: |

<!-- figure 1 on pdf page 37 at 427,91-801,203 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 57) -->
or Watch
<!-- end of figure 1 -->

<!-- pdf page 38 | printed page 38 | header: Description -->

| Item | Description |
| --- | --- |
| 1 | Menu tabs — Select a tab to open the relevant settings menu. |
| 2 | [Close] — Select to return to the chart application screen. |
| 3 | [Display Name] — Enter a name for the station (e.g.: ECDIS, or ECS). |
| 4 | [SFI] — Enter a unique SFI (System Function Identifier). For details, refer to: Configuring an SFI |
| 5 | [Display Number] — Enter a unique identifying number for the station. |
| 6 | [Display Group] — Assign the system to a group. |
| 7 | [Enable Touchscreen] — Enable / Disable (default) the display’s touchscreen. |
| 8 | [Enable Onscreen Keyboard] — Enable (default) / Disable the onscreen keyboard. |
| 9 | [Language] —Select a language for the user interface. |
| 10 | [Connect to Wi-Fi] — Connect the system to a Wi-Fi Access Point (AP). |
| 11 | [Presentation Library] — Identifies the current IHO ECDIS Presentation Library version. |
| 12 | [S63 User Permit] — Identifies the license key for S63 user permits. |
| Item         Description |  |
| 13 | [Manual gateway] — If applicable enable and enter the IP address for the [eSyncBox] . |
| 14 | [Reset Settings] — Reset the system settings to factory default values. |
| 15 | [Factory Reset] — Reset the system settings to factory default values and delete all user data. |

###### Configuring an SFI

- Each SFI must be unique and should consist of 2 letters followed by 4 numbers.
- The SFI should be configured as follows:
1. Select the SFI field.
2. Enter 2 letters.

To remain -450 compliant, it is recommended that you use RA for Radar, EI for ECDIS, and IN for Integrated Navigation.

3. Enter a unique 4 digit number. Example: RA0001, EI0002, IN0003.

###### Connecting the display to a Wi-Fi access point

The system can be connected to the Internet using the built-in Wi-Fi connection.

Note: This step may be required if the system does not have a wired network connection to a gateway that is providing Internet access.

From the [This Display] settings menu:

<!-- figure 1 on pdf page 38 at 38,38-413,194 pt | caption: none | text-layer labels: none | nearby labels: 13 | 14 | 15 | Item | Description | OCR text follows (tesseract, unverified; 51/67 words >= 60, mean confidence 73) -->
1 this
General Settings
Close
External Devices
Integrity
Network
Alert Settings
Maintenance
3°?
4?
ECDIS
6”:
5?
Group 1
8
e
e
ou
een
10?
English
WiFi Settings
er
11”
It
ry 4.0
esentatio
Lib
mi
3
12
alled,
rmit
For Customer Support please contact support@chartworld.com
Reset Settings
Factory Reset
*15
<!-- end of figure 1 -->

<!-- pdf page 39 | printed page 39 -->

1. Select the [Wi-Fi Settings] button.
2. Select the relevant Wi-Fi access point.
3. Enter the password for the access point.
4. Select [CONNECT].
5. Select the [Back] icon. S63 user permits When the system is connected to the Internet the [S63 User Permit] should be downloaded and installed automatically. If the user permit does not install automatically or there is no Internet connection it can be entered manually by selecting the [Enter User Permit] text or you can contact customer support for assistance.

###### Connecting to the eSyncBox

- When the eSyncBox is included in the system the Manual gateway settings should be configured.
- From the [This Display] settings menu:
1. Enable the [Manual Gateway] toggle switch.
2. Ensure that the [Gateway Address] field is set to the IP address of the eSyncBox.

- By default the [Gateway Address] field is set to the eSyncBox’s default IP
- Address: 198.18.1.1 .

3. If the eSyncBox’s IP address has been changed or the [Gateway Address] has been modified select the field and enter the correct IP address. for of the eSyncBox.

<!-- figure 1 on pdf page 39 at 38,38-413,387 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 23/52 words >= 60, mean confidence 54) -->
Close
be
Ne
ish
tinge
wit
ae
Wi-Fi
Use WiFi
Link
Show password
Wi-Fi
Use
4
‘Add network
preferences
connect
Saved networks
a
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 39 at 427,38-801,251 pt | caption: none | text-layer labels: none | nearby labels: Connecting to the eSyncBox | OCR text follows (tesseract, unverified; 23/31 words >= 60, mean confidence 73) -->
neral
ing:
Ownship
Maintenance
sett
Dev
splay
e
y
9
Xx
Group 1
Settings
port please
F
stomer Su
Reset Settings
Factory Reset
<!-- end of figure 2 -->

<!-- pdf page 40 | printed page 40 | header: Description -->

##### Ownship settings menu

The [Ownship] settings menu provides settings for items which require their position to be configured, and also Device delta values.

| Setting | Description |
| --- | --- |
| 1 | [Ship name] — Enter the ship’s name. |
| 2 | [Ship type] — Select the ship type from the drop down list. |
| 3 | [Call Sign] — Enter the ship’s call sign |
| 4 | [MMSI] — Enter the ship’s MMSI number. |
| 5 | [IMO Number] — Enter the ship’s IMO number. |
| 6 | [Length] — Enter the length of the ship. |
| 7 | [Width] — Enter the width of the ship. |
| 8 | A visual representation of the ship identifying the location of the CCRP and sensor device locations relative to the CCRP. |
| 9 | [CCRP] — Enter the [CCRP X] and [CCRP Y] position as measured from the stern of the ship. |
| Setting | Description |
| 10 | [Anchors] — Enable an anchor using the toggle switch. Enter the [Anchor X] and [Anchor Y] position as measured from the CCRP for the enabled anchor. |

Note: Only 1 anchor can be enabled. Enabling a different anchor will disable the currently enable anchor.

11           [External Devices] Enter [Device X] and [Device Y] positions for detected sensors as measured from the CCRP.

###### CCRP location

The CCRP (Consistent Common Reference Point) location must be configured

###### CCRP and related settings

1. Ship details — The [Length] and [Width] of the ship must be entered in order to configure the location of the CCRP.

<!-- figure 1 on pdf page 40 at 38,88-413,316 pt | caption: none | text-layer labels: none | nearby labels: 10 | 11 | Setting | Description | OCR text follows (tesseract, unverified; 100/118 words >= 60, mean confidence 80) -->
General Settings
This Display
Ownship
Devices
Integrity
Network
Alert Settings.
Maintenance
work
Ship Details
Ship Outline
8
Ship name
v
Port
A
Cargo ship
3
Call Sign
712345689
3 5
IMO Nui
aber
Starboard
147.00 m
Width
g CCRP (from Stem of ship)
Starboard Anchor (from CCRP)
Port Anchor (from CCRP)
RP X
25.00m
Stbd Anchor X
Anchor X
CRP Y
hor Y
10”
Bow Anchor (from CCRP)
Stern Anchor (from CCRP)
Bow
x
Ste
Stern A
External Devices (from CCRP) 1 1
Ds1
NAVD
Ds3
Device X
evice X
0.00m
0.00m
Device
30.00 m
Device Y
0.00m
Device
15.00m
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 40 at 427,277-801,507 pt | caption: none | text-layer labels: none | nearby labels: CCRP and related settings | 1. | OCR text follows (tesseract, unverified; 102/121 words >= 60, mean confidence 80) -->
St
General Settings
This Display
Ownship
External Devices
Network
Alert Settings
Integrity
Maintenance
work
$4
Ship Details
Ship Outline
Ship name
Nostromos
Port (4)
Cargo ship
Ship
ype
Call S
gn
712345689
MMSI
MO Numbe
Starboard
147.00 m
Width
CCRP (from Stern of ship)
Starboard Anchor (from CCRP)
Port Anchor (from CCRP)
RP X
Anchor X
25.00m
Stbd Anc
or X
Anchor Y
Y
nchor Y
Bow Anchor (from CCRP)
Stern Anchor (from CCRP)
Anch
Anch
he
Stern
External Devices (from CCRP)
NAVD
Ds1
Device X
ce X
0.00m
0.00m
De
De
Device Y
20.00 m
Device Y
0.00m
15.00 m
eY
<!-- end of figure 2 -->

<!-- pdf page 41 | printed page 41 -->

2. A visual representation of the ship identifying the location of the CCRP and sensor device locations relative to the CCRP.
3. [CCRP]:
- [CCRP X:] determines the position of the CCRP along the length of your vessel. Zero is located at the stern.
- [CCRP Y:] determines the position of the CCRP along the width or beam of your vessel. Zero is located at the vessel’s centerline. Positive values are to port of the vessel’s centerline and negative values are to starboard of the vessel’s centerline.

###### Anchor position

The position of the ship’s anchor can be plotted relative to the CCRP. The Anchor’s position is configured from the [Ownship] settings menu. Anchor position is required for the [Anchor Watch] feature. 1 of 4 anchors can be configured: • Port • Starboard • Bow • Stern Anchor position is configured by providing an ‘X’ and ‘Y’ distance for the anchor where: • X = the distance along the length of the ship. Zero is located at the CCRP. Positive values are forwards of the CCRP and negative values are aft. • Y = the distance along the width or beam of the ship. Zero is located at the CCRP. Positive values are port of the CCRP and negative values are starboard.

Configuring an anchor Follow the steps below to configure the anchor’s position. The CCRP location must be configured before the anchor’s position is configured. The configured anchor will be used for [Anchor Watch] .

From the [Ownship] settings menu:
1. Enable the relevant anchor using the toggle switch.
2. Select the [X] value and adjust it to represent the distance from the CCRP (positive values are forwards of the CCRP and negative values are aft.

<!-- figure 1 on pdf page 41 at 427,38-801,198 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 8/9 words >= 60, mean confidence 82) -->
A
Port
CCRP
X
Stern
STBD
Vv
Y
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 41 at 427,263-801,490 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 99/127 words >= 60, mean confidence 78) -->
General Settings
This Display
Ownship
External Devices
Network
Alert Settings
Integrity
Maintenance
work
Ship Details
Ship Outline
Ship name
Nostromos
Port (4)
8
Cargo ship
Ship Type
Call Sign
712348689
7654321
MO Number
Starboard
ength
Width
CCRP (from Stern of ship)
Starboard Anchor (from CCRP)
Port Anchor (from CCRP)
2
CCRP X
Anchor X
Stbd Anchor X
P
Anchor Y
St
or
0
Bow Anchor (from Ct
CRP)
Stern Anchor (from CCRP)
Bow Anchor X
Stern
ry
n Anch
External Devices (from CCRP)
NAVD
Ds1
Device X
0.00m
0.00m
Device
Dev
Device Y
Device Y
15.00 m
Device Y
<!-- end of figure 2 -->

<!-- pdf page 42 | printed page 42 -->

3. Select the [Y] value and adjust it to represent the distance from the CCRP (positive values are to port and negative values to starboard). Configuring external device positions External devices that provide position data to the system require their installation location to be configured relative to the CCRP location. The CCRP location must be configured before the Anchor positions are configured.

1. Select the [ Device X] value and adjust it to represent the distance from the CCRP (positive values are forwards of the CCRP and negative values are aft.
2. Select the [Device Y] value and adjust it to represent the distance from the CCRP (positive values are to port and negative values to starboard).
3. Repeat steps 1 and 2 for all devices.

##### External devices settings

The display can receive and transmit data from external devices. In accordance with MSC.192/8.1, Pathfinder ECDIS is capable of receiving the required input information from the following equipment: • a gyro-compass or transmitting heading device (THD)

- a speed and distance measuring equipment (SDME)
- an electronic position fixing system (EPFS)
- an automatic identification system (AIS); or
- other sensors or networks providing equivalent information acceptable to the IMO (e.g.: an INS). For the DCU the most common external devices are pre-configured for you. Additional devices can be added manually as required. For the DCU-2 once the device has been connected and powered on, you will need to select the [Auto Detect] toggle switch for [DS1] and [DS2].

1. [Data I/O] — The [External devices] menu includes a data in/out area which lists all incoming and outgoing data messages.
- Incoming messages received from a device which is currently enabled in the [External devices] menu will be colored white.
- Incoming messages received from a device which is currently disabled in the [External devices] menu will be colored black.
- Outgoing messages are colored green.
- Messages which are invalid will be colored red.
2. [Add Device] — Select to add a new external device.
3. Scroll bar — Use to scroll the list of configured devices.

<!-- figure 1 on pdf page 42 at 38,146-413,373 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 107/131 words >= 60, mean confidence 77) -->
Statu
General Settings
This Display
Ownship
External Devices
Network
Alert Settings
Integrity
Maintenance
work
Ship Details
Ship Outline
Ship name
Nostromos
Port (4)
Cargo ship
Type
Call Sign
MMSI
72:
5689
MO Number
7654321
Starboard
147.00 m
Width
e
CCRP (from Stern of ship)
‘Starboard Anchor (from CCRP)
Port Anchor (from CCRP)
st
PX
25.00m
bd Anchor X
rt Anchor X
St
CCRP Y
15,00 m
Anchor Y
st
d Anc
Bow Anchor (from CCRP)
Stern Anchor (from CCRP)
Anch
Stern Anche
x
ry
External Devices (from CCRP)
NAVD
Ds1
Device X
Device X
Device X
1
5.00m
0.00m
Device Y
D
0.00m
Device Y
Dev
eY
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 42 at 427,177-801,390 pt | caption: none; nearest centred text below: "[Data I/O] — The [External devices] menu includes a data in/out area" | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 174/213 words >= 60, mean confidence 80) -->
ms
a
General Settings
‘Save
Close
This Display
‘Ownship
External Devices
Alert Settings
Integrity
Network
Maintenance
Network changes saved
1
Data
Add Device
Network Devices
13:55 45 RX:
Enable Device
DS1 13:55:45 RX:
e
e
z
Show Telegrams
IEC 61162-450
Auto Detect
DS1 13:55:45 RX: SGPGNS,135544,4932.0423,N,
00006.5400,W,DN,8,1.4,0.0,0.0,5.0,0*6A
60002
Loose
Receive Address
Receive Port
Strict
Loose
DS2 13:55:45 RX:
VDR Screen Output 13:55:45 TX: VDR Output: Query datagram
‘Manage
Transmit Address
Transmit Port
60002
5:45 RX: UdPbC\s:RAQ001*5B\SECOSD,198.0,A,
VDRD 13:
213.0,P5.8P,,
Enable Device
SATD
Device Name
VDRD 13:55:45 RX:
Enable Device
Device Name
NAVD
11
5:45 RX: UdPbC\s:RA0001*5B\!RATTD,
TGTD 13:
Enable Device
VORD
Device Name
s>4;D5003VnFOtbFbE;CPO03WnKOQRDR>;Bi00,0
1
Enable Device
Screen Output
Device
TGTD 13:55:45 RX:
jan
e
Enable Device
VDRD 13:55:45 RX: UdPbC\s:RA0001*5B\!RATTD,
Device Nan
BAM
01,01, CUwwowtCVwwowtCWwwowt,0*30
DS1 13:55:45 RX:
Enable Device
Device Nan
ps1
DS2 13:55:46 RX:
Enable Device
DS1 13:55:46 RX:
Devic
Na
2,
DS1 13:55:46 RX: $GPGLL,4932.0423,N,00006.5400,W,
Enable Device
ps3
Device Name
135544,A,D*5C
VDRD 13:55:46 TX: UdPbC\s:
*78 8
Enable Device
Device N:
e
2D
DS2 13:55:46 RX:
Pause
file
Manual Devices
<!-- end of figure 2 -->

<!-- pdf page 43 | printed page 43 | header: 4. -->

## 4.

4. Example of expanded device details and settings.
5. [˅] Down / [˄]Up arrow — Use to expand and contract device details and settings
6. [Save to file] — Select to save the I/O history to a file. The file will be exported when Display logs are exported.
7. [Pause] — Select to pause the I/O history. This is useful when searching for a specific item.
8. [Clear] — Select to clear the current history. Manual devices can be enabled and disabled from the bottom of the devices list. External devices which transmit positional data will appear in the [Ownship] settings menu so that their ‘X’ and ‘Y’ position can be plotted. Default external devices The typical required external devices are configured by default.

###### IEC 61162–450 compliant devices

- [TGTD]
- [SATD]
- [NAVD]
- [VDRD]
- [VDR Screen Output]
- [BAM] These devices are [Disabled] by default and will require enabling. For the default settings for these devices refer to: Default IEC 61162–450 devices

###### Data servers

- [DS1]
- [DS2]
- [DS3]
- [DS4] These devices are [Enabled] by default. For the default settings for these devices refer to: Default DCU/DCU-2 external devices

- Adding an Ethernet network device Ethernet network devices must be added and configured correctly.
- From the [External Devices] settings menu:
1. Select [Add Device] under the [Network Devices] section.
2. Enter a name for the device and select [OK].
3. Enable the [IEC 61162-450] and [Show Telegrams] toggle switches.
4. Enter the device’s receive IP address in the [Receive Address] field.
5. Enter the device’s receive port number in the [Receive Port] field.
6. If you want to transmit to the device, you can use the values in the [Transmit Address] and [Transmit port] field to configure the device you want to transmit to.
7. Select the [Strict/Loose] field to switch between Strict or Loose adherence to the telegram messages format.
8. Enable the [Auto-Detect] toggle switch to automatically detect Telegrams;
- or:
9. Select the [Telegrams] button and enable and disable your required Telegrams. The maximum Telegram input rate for all external devices is 50 Hz. To ensure compliance with IEC 61162-450, all Telegram will be configured in accordance with the IEC 61162-450 standards. Raymarine proprietary data will not conflict with the -450 ports.

If you have successfully connected to the device and it is transmitting data, the [Data I/O] section will show received data messages. Setting up an alarm system external device A connected alarm system must be set up as an external device.

Note:
- The alarm system connection applies to Pathfinder ECDIS and Pathfinder Radar Displays.
- The alarm system connection is not applicable to Pathfinder ECS.

From the [External devices] setting menu:
1. Scroll to the [DS4] device.
2. Select the [Manage Telegrams] button.
3. Select the [Output telegrams] tab.

<!-- pdf page 44 | printed page 44 -->

4. Enable the following Telegrams:
- [ALR Alarm State] (If Alarm Message event is enabled).
- [EVE General Event Message] (If Event Message event is enabled).
- [HBT Heartbeat] (If Heartbeat Message event is enabled).

The remaining [DS4] device settings can be left as is with their default values.

5. Select the [X] to close the menu.

BNWAS connection The output to the BNWAS (Bridge Navigational Watch Alarm System) should be connected via the Alarm output on the DCU.

Note: Only applicable to the DCU. The DCU-2 does not have an alarm output connection.

Only the ECDIS installed in the primary bridge location (i.e.: used for navigation) should be connected to the BNWAS for resets. When the EVE telegram is enabled the system will generate the Telegram for every Touch or Trackball event, resetting the BNWAS.

###### Deleting an external device

1. Select and hold on the Device name.
2. Select [Yes] from the confirmation box.

Input and Output tests All data inputs and outputs for external devices should be tested to ensure that the relevant, accurate data is being received, and where possible, matches the source devices’ data.

###### Manual Heading, Position and Speed

Manual [Heading], [Position] and [Speed] devices can be enabled and disabled from the [External devices] settings menu. The Manual devices are enabled by default.

Enabling and disabling external devices using SFIs Data from external IEC 61162–450 compliant devices can be enabled and disabled by SFI.

From the [External devices] settings menu:
1. Select the icon located to the right of the [IEC 61162–450] toggle switch.
2. Enable and disable the SFI(s) as required. The device will now be treated as disabled.

<!-- figure 1 on pdf page 44 at 427,220-801,433 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 105/148 words >= 60, mean confidence 72) -->
General Settings
‘save
Th
Ownship
External Devic
Network
Alert Set
Maintenance
Debug
Data
‘Add Device
Network Devices
Enable Device
DS1 14:32:06 RX: $GPVTG,000.0,7,000. 0.0,N,000.0,K,0*26
DS2 14:32:06 RX: SHEROT,000.0,A*2B
e
IEC 61162-450
Auto Detect
‘Show Telegrams
DS1 14:32:06 RX:
DS2 14:32:06 RX:
Loose
39.19;
DS1 14:32:07 RX: $GPGLL,4932,0423,N,00006.5400,W,
Manage Devices
‘Manage Telegrams
6000:
*2F
14:32:07 RX.
F
4
DS1 14:32:07 RX: $GPVTG,000.0,T,000.0,M,0.0,N,000.0,K,0*26
DS2 14:32:07 RX:
DF
F
at
4
DS1 14:32:07 RX: $GPGGA,143206,4932.0423,N,00006.5400,W,
‘Save and
14:32:07 RX:
DS1 14:32:08 RX:
Enable Device
143206,A,D*5C
14:32:08 RX: SHEHDT,000.0,1*2F
Enable Device
Enable Device
x
DRE
DS1 14:32:08 RX: $GPVTG,000.0,7,000.0,M,0.0,N,000.0,K,0*26
Enable Device
DS2 14:32:08 RX: SHEROT,000.0,A*2B
Pause Clear
Manual Devices
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 44 at 38,397-413,504 pt | caption: none | text-layer labels: none | nearby labels: Deleting an external device | External devices can be deleted. | OCR text follows (tesseract, unverified; 53/68 words >= 60, mean confidence 74) -->
able Device
DS2 14:33:12 RX: SHEHDT,000.0,1*2F
C2]
Enable Device
DS1 14:33:12 RX: $GPGLL,4932.0423,N,00006.5400,W,
Enable Device
DS1 14:33:12 RX: $GPVTG,000.0,7,000.0,M,0.0,N,000.0,K,0*26
x
Manual Devices
4
e
14:33:13 RX: SGPGGA,143311,4932.0423,N,00006. 5400,W,
Manual Position
Manual Heading
Manual Speed
2,8,1.4,0.0,M,0.0.M,5.0,0100*7F
DS2 14:33:13 RX:
‘Ave you sure you wart to delete this {ne}
DS2 14:33:13 RX: SHETHS,000.0,A*2D
Clear
fie
<!-- end of figure 2 -->

<!-- pdf page 45 | printed page 45 | header: 3. -->

## 3.

##### Integrity settings menu

The [Integrity] settings menu provides a traffic light system to show which external devices are providing data and which is the best data.

##### Network settings menu

The [Network] settings menu shows detailed hardware and software information about the system.

1. Product list.
2. Product Info — Selecting the Product name from the right side of the menu will show the Product info on the left side.

| 3. | [DHCP] — Switch the internal DHCP server On, Off, or set to Smart (default) mode. Smart mode allows the DHCP server to be automatically enable or disable, if another DHCP server is detected on the network. |
| --- | --- |
| 4. | [Refresh] — Select to refresh the product list. |

##### Alert Settings

The [Alert Settings] menu enables configuration of alerts and provides a list of historical alerts raised by the system.

Note: Hardware-dependent alerts are only triggered when relevant hardware (e.g.: sensors) is connected and reporting the data required for the alert.

The [Alarm History] can be cleared by selecting [Clear history] or it can be saved to the system logs, ready for export by selecting [Save].

The audible tone that accompanies Alerts and Warnings can be enabled and disabled using the [Audio alarm] toggle switch. The [Alert Settings] menu provides a list of all alerts that can be raised by the system.

<!-- figure 1 on pdf page 45 at 38,88-413,210 pt | caption: none | text-layer labels: none | nearby labels: 4. | Network settings menu | OCR text follows (tesseract, unverified; 25/28 words >= 60, mean confidence 86) -->
General Settings
Th
Network
Alert Sett
Ownship
External Device:
Maint
Display
9
External Devic
Position
Heading
Speed over Ground
Speed Through Water
Wind
Time
Depth
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 45 at 38,275-413,485 pt | caption: none | text-layer labels: none | nearby labels: 1. | Product list. | OCR text follows (tesseract, unverified; 100/119 words >= 60, mean confidence 78) -->
General Settings
Network chan
This Display
Ownship
Extemal Devices
Integrity
Network
Alert Settings
Maintenance
(Product Info
Product
Name
Device Number
Version
AXIOM
Product info
1
PU revision:
(4GB/64GB)
Hardware revision:
Carrier:3 Main:
Product family:
AXIOM 2 XL
Product ID:
£70661-IMO
AXIOM 2
Product name.
Product serial number:
TATGB63
Nautilus info
Nautilus version:
014
Software info
Application version:
0.1.6.11
Platform version:
Power micro hardware:
0.0.217
Power micro version:
Product bundle version:
‘Swipe micro version:
‘Temperature Status
‘Supply voltage:
Temperature CPU die:
30.6°C
Temperature GPU die
Temperature PSU:
31.4°C
IP address:
198,18.2.107
Link status:
Up
MAC address:
‘Subnet mask
Refresh
DHCP
‘Smart
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 45 at 427,277-801,488 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 348/368 words >= 60, mean confidence 90) -->
General Settings
External Devices
Network
Maintenance
This Display
Ownship
Integrity
Alert Settings.
Alarm History
Settings
fic
Alarm name
Event
Alert Handling
Position System Failure
Caution raised at Tue Apr 29 09:36:18 2025 GMT
1D
Type
Description
Escalate
BAM Controls
Position System Failure
Caution raised at Tue Apr 29 09:36:18 2025 GMT
3032
Warning
Anchor Watch
Position System Failure
Warning raised at Tue Apr 29 09:36:18 2025 GMT
3031
Alarm
Anchor Watch
Position System Failure
Caution raised at Tue Apr 29 09:36:18 2025 GMT
3016
Position System Failure
Lost Heading Input
Caution raised at Tue Apr 29 09:36:18 2025 GMT
Position System Failure
015
Lost Heading Input
Warning raised at Tue Apr 29 09:36:18 2025 GMT
Lost Heading input
Caution raised at Tue Apr 29 09:36:18 2025 GMT
3014
Alarm
Position System Failure
Lost Speed Over Ground Input
Caution raised at Tue Apr 29 09:36:18 2025 GMT
3016
Caution
Lost Heading input
Through Water
Warning raised at Tue Apr 29 09:36:18 2025 GMT
3015
Waring
Lost Heading input
Lost AIS Input
Caution raised at Tue Apr 29 09:36:18 2025 GMT
Alarm
3014
Lost Heading Input
cleared at Tue Apr 29 09:37:19 2025 GMT
Position System Failure
3016
Caution
Lost Speed Over Ground Input
Position System Failure
Alarm raised at Tue Apr 29 09:37:19 2025 GMT
3015
Warning
Lost Speed Over Ground Input
Position System Failure
Warning escalated at Tue Apr 29 09:37:19 2025 GMT
3014
Alarm
Lost Speed Over Ground Input
Lost Heading Input
Warning cleared at Tue Apr 29 09:37:19 2025 GMT
3016
Caution
Lost Speed Through Water input
Lost Heading Input
Alarm raised at Tue Apr 29 09:37:19 2025 GMT
3015
Warning
Lost Speed Through Water input
Lost Heading Input
Warning escalated at Tue Apr 29 09:37:19 2025 GMT
3014
Alarm
Lost Speed Through Water Input
Lost AIS Input
Warning cleared at Tue Apr 29 09:37:19 2025 GMT
Lost Speed Through Water
Alarm raised at Tue Apr 29 09:37:19 2025 GMT
3016
Caution
Lost Wind input
Speed Through Water
Warning escalated at Tue Apr 29 09:37:19 2025 GMT
3015
Lost Wind Input
Input
at Tie 20 OMT
<!-- end of figure 3 -->

<!-- pdf page 46 | printed page 46 | header: Alert / Type / Alert Identifier / Category -->

## Alert / Type / Alert Identifier / Category

| Escalate | Alert | Type | Category   Alert |  |
| --- | --- | --- | --- | --- |
| All warnings, with the exception of the [Anchor Watch] warning, are escalated |  |  |  | Identifier |
| automatically to an Alarm after 60 seconds of not being acknowledged. The | Lost Heading Input | Alarm | B | 3014 |
| [Anchor Watch] warning is escalated after 120 seconds. | Lost Speed Over Ground | Caution | B | 3016 |
| Warning escalation is enabled by default, if required, escalation can be | Input |  |  |  |
| disabled for each individual Warning using the associated [Escalate] toggle |  |  |  |  |
| switch. | Lost Speed Over Ground Input | Warning | B | 3015 |
| BAM Controls | Lost Speed Over Ground | Alarm | B | 3014 |
| The [BAM controls] toggle switch enables responsibility of an alert to be | Input |  |  |  |
| transferred to the BAM system. Control of Category A and Category B alerts | Lost Speed Through Water | Caution | B | 3016 |
| can be transferred to the BAM (Bridge Alert Management) system. | Input |  |  |  |
| By default BAM control for category A alerts will be disabled and will be | Lost Speed Through Water | Warning | B | 3015 |
| enabled for category B alerts. If required, you can change the control status | Input |  |  |  |
| using the relevant toggle switch | Lost Speed Through Water | Alarm | B | 3014 |
| Note: | Input |  |  |  |
| [Escalate] and [BAM Controls] are not available for Cautions. | Lost Wind Input Lost Wind Input | Caution Warning | B B | 3016 3015 |
| When connecting to a BAM, the External device’s HBT input telegram must | Lost Wind Input | Alarm | B | 3014 |
| be enabled. If the device loses the HBT then Responsibility transfer of the | Lost Depth Input | Caution | B | 3016 |
| alerts will be rejected, therefore a system failure of the BAM shall not lead to |  |  |  |  |
| the loss of the alert announcement functionality. | Lost Depth Input Lost Depth Input | Warning Alarm | B B | 3015 3014 |

###### Alerts list

|  | Lost AIS Input | Caution | B | 3016 |
| --- | --- | --- | --- | --- |
| A list of available alerts and their category and identifier is shown below | Lost AIS Input | Warning | B | 3015 |
| Alert                           Type            Category        Alert |  |  |  |  |
| Identifier | Lost AIS Input | Alarm | B | 3014 |
| Anchor Watch                    Warning         A               3032 | Different Geodetic Datum | Warning | B | 3005 |
| Anchor Watch                    Alarm           A               3031 | Different Geodetic Datum | Alarm | B | 3004 |
| Position System Failure         Caution         B               3016 | XTD Limit | Alarm | A | 3024 |
| Position System Failure         Warning         B               3015 | Safety Contour Crossing | Alarm | A | 3031 |
| Position System Failure         Alarm           B               3014 | Crossing Navigation Hazard | Caution | A | 3036 |
| Lost Heading Input              Caution         B               3016 | Crossing Navigation Hazard | Warning | A | 3035 |
| Lost Heading Input              Warning         B               3015 | Approach to area | Caution | A | 3036 |

<!-- pdf page 47 | printed page 47 | header: Alert / Type / Alert Identifier / Category -->

| Approach to area               Warning | A | 3035 |  |  |
| --- | --- | --- | --- | --- |
| Approach to the critical point Warning | A | 3038 |  |  |
| Approach to the critical point Alarm | A | 3037 |  |  |
| AIS Capacity about to be       Caution | A | 3043 |  |  |
| exceeded |  |  |  |  |
| AIS Capacity exceeded          Warning | A | 3042 |  |  |
| AIS Capacity exceeded          Alarm | A | 3041 |  |  |
| ARPA Capacity about to be      Caution | A | 3043 |  |  |
| exceeded |  |  |  |  |
| ARPA Capacity exceeded         Warning | A | 3042 |  |  |
| ARPA Capacity exceeded         Alarm | A | 3041 |  |  |
| Lost Target                    Warning | B | 3052 | Item   Description |  |
| Lost Target                    Alarm | B | 3051 | 1 | [Backup] — Backup user data and settings. |
| Dangerous Target               Alarm | A | 3044 | 2 | [Restore] — Restore user data and settings from a backup. |
| S63 User Permit Error          Caution | A | 10003 | 3 | [Save Display’s logs] — Save logs from this display to a memory card. |
| Maintenance settings menu |  |  | 4 | [Erase Display’s logs] — Erase the logs saved on this display. |
| The [Maintenance] settings menu includes options related to the maintenance |  |  | 5 | [Save all products logs] — Save logs from all products on the |
| and troubleshooting of the system. |  |  |  | network. |
| The following options are available: |  |  | 6 7 8 9 10 11 | [Update Display] — Update the display’s software. [Delete IHO Certificate] — Delete the current IHO certificate. Software details. [Anydesk Access ] — Open the Anydesk app to set up remote desktop access to the display. The AnyDesk app is only accessible when the Enable AnyDesk toggle switch is on. [Enable Anydesk] — Enable / Disable the use of Anydesk. [Select SD Card] — Select the card reader slot that data, logs, screen capture etc are saved to. |

<!-- figure 1 on pdf page 47 at 427,38-801,275 pt | caption: none | text-layer labels: Item | Description | nearby labels: 1 | 2 | OCR text follows (tesseract, unverified; 50/60 words >= 60, mean confidence 82) -->
General Settings
Close
This Display
Ownship
External Devices
Integrity
Network
Alert Settings
Maintenance
Access
Backup Restore
2?
4?
Restore
Enable
De:
Backup Everything
Diagnostics
Capture Screen
External SD 1
Save Displays Logs
4
5 D> Save all products
*13
5s
Updates
Update Display
Certificate
App version
Platform version
Bundle version
<!-- end of figure 1 -->

<!-- pdf page 48 | printed page 48 | header: Description -->

## Description

| Item | Description |
| --- | --- |
| 12 | [Capture Screen] — Enable / Disable automatic screenshots at the specified time interval |
| 13 | [Capture Interval] — Time interval for the [Capture Screen] feature. |

### 6.3 Installing ENCs

ENCs are installed from external memory cards. Ensure that the necessary ENC files and related permit/license files are saved to the memory card and is inserted into the external card reader.

- Note: The “IHO.crt” file MUST be saved to the root directory of the memory card
- i.e.: at the top level and not inside a folder.

1. Select the [Chart Loader] icon from the [Taskbar] .
2. Select the [Install / Update Charts] button. The display will now scan the memory card and install any available ENCs.

##### Chart boundaries

The areas covered by installed charts can be viewed using the [Chart Boundaries (index)] setting. The [Chart Boundaries (index)] setting is useful for quickly confirming successful installation and which regions are covered by your installed ENCs.

The [Chart boundaries (index)] setting is accessed from the [Chart Display] menu: [Chart Display > Advanced > Additional Options > Chart boundaries (index)].

### 6.4 Backup and restore

##### Backup

- Settings and data can be backed up to internal and external memory. The backup procedure backs up the following data and settings:
- Ship Data (External devices and ownship settings).
- User Charts.
- User Profiles.
- Routes.
- Past Track Data.

<!-- figure 1 on pdf page 48 at 427,117-801,320 pt | caption: none | text-layer labels: none | OCR below floor, text not used (25/92 words >= 60, mean confidence 41) -->

<!-- figure 2 on pdf page 48 at 38,277-413,466 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 31/49 words >= 60, mean confidence 65) -->
Mode
41?
Chart 1
Install
Inventory
Review Updates
Route
MFD Network
Install
Update
arts
oot
263.1
200
2.25
install
Inventory
Review Updates
MFD Network
die
Cancel
(Update Log Update)
‘Summary
2)
<!-- end of figure 2 -->

<!-- pdf page 49 | printed page 49 -->

- Voyage recordings.
- Alerts Configuration. The backup file can be used at a later date to [Restore] your data and settings. For details on restoring user data and settings refer to the Commissioning & Acceptance Testing Instructions (Document number: 81427).

Performing a backup A backup should be performed as part of commissioning, but can also be performed by the operator.

Note: A backup should be been created and saved to both internal and external memory as part of the commissioning process.

1. Select the [Backup] from the [Additional Features] menu.
2. Select the memory device from the drop down list.
3. Select [Backup].
4. Select [OK] on the backup confirmation notification. The backup file will be created in the ‘:\PathfinderBackUp’ folder of the internal or external memory.

The name for the backup file will be in the following format: PFNDBackup_YYYMMDDHHMMSS_ShipName_DisplaySN A [Backup] can also be performed by selecting [Backup Everything] from the password protected [Maintenance] settings menu.

##### Restore

User data and settings can be restored from a backup file stored on internal or external memory. The restore function is provided in the password protected settings menu. A restore should only be performed by an authorized engineer. Performing a restore Follow the steps below to perform a restore from a backup file.

1. Select [Restore] from the [Maintenance] settings menu.
2. Select the memory device from the drop down list.
3. Select the backup file.
4. Select [Restore].
5. Either select the items that you want restored and select [Restore Selected], or select [Restore All]. The following items can be restored from a backup file:
- Ship Data (External devices and ownship settings).

<!-- figure 1 on pdf page 49 at 427,218-801,428 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 42/48 words >= 60, mean confidence 84) -->
General Settings
This Display
Ownship
External Devices
Network
Aler
Maintenance
ting
Access
Backup Restore
Backup Everything
Diagnostics
Capture Screen
‘Save Logs
External SD 1
‘Save all products logs
Updates
‘Update Display
Restore Selected Restore All
Certificate
App version
Platform version
Bundle version
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 49 at 38,246-413,459 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 79/130 words >= 60, mean confidence 67) -->
é
Range (NM)
System Backup
[7m ono
Internal Memory
Memory Location
File Size
Date Modified
Name
153.1
Mode
PFNDBackup_2025-04-11_15-23-43_.
Fri Apr 11 15:23:43 2025 GMT
156774B)
2.33MB
Planning Mode
PFNDBackup_2025-04-22_09-24-14_.
Tue Apr 22 09:24:14 2025 GMT
4g
Tue Apr 22 14:2
PFNDBackup_2025-04-22_14-22-23_.
2025 GMT
36
(2691554B)
Settings
54
Device Selection
Backup
33
Display Setup
Anchor Watch
181
Backup
BRG
1497
Up
ms
ONM
67
3g
44
completed successfully.
1g
14
VA
83
19
Og
ect
1445.02 20250422
(4.
14
<!-- end of figure 2 -->

<!-- pdf page 50 | printed page 50 -->

- User Charts.
- User Profiles.
- Routes.
- Past Track Data.
- Voyage recordings.
- Alerts Configuration.

6. Select [OK] on the restore complete notification.

<!-- pdf page 51 | printed page 51 -->

## CHAPTER 7: ACCEPTANCE TESTING

#### CHAPTER CONTENTS

<!-- pdf page 52 | printed page 52 -->

### 7.1 Acceptance testing

- Once all installation and commissioning activities are complete, the system requires acceptance testing to confirm correct operation.
- Pre-requisites:
- Before performing acceptance testing ensure that:
- All equipment is running the latest available software.
- All relevant devices are powered on.
- All relevant Health & Safety precautions as noted in this document and
- in the Operator’s Instructions (Document number: 81422) are adhered to throughout the testing.
- Testing procedure: Carry out the relevant checks as described in the following test record pages to verify that the system has been set up correctly, operates as expected and that the relevant data is displayed onscreen.
- Follow the Operator’s Instructions (Document number: 81422) to establish correct functional operation.

### 7.2 Chart application operational test record

| Test | Steps 1.   Ensure that the system is connected to | Pass |
| --- | --- | --- |
| User permit | the Internet. 2. Open the [This Display] settings menu. 3.   Check that there is a valid S63 User Permit installed. | ☐ Passed |
| Range | 1.   Check that the chart application screen can be ranged in and out. 1.   Check that ownship icon is present | ☐ Passed |
| Ownship |  |  |
| data | onscreen. | ☐ Passed |
| Cursor | 1.   Place the cursor within the chart area |  |
| position | and check that range, bearing, latitude and longitude are displayed in the cursor box located on the right side of the screen. | ☐ Passed |

| Test          Steps | Pass |
| --- | --- |
| 1.   Check that the following Orientation |  |
| Orientation |  |
| modes are available: [N-Up], [C-Up] and | ☐ Passed |
| [STAB H-Up]. |  |
| Clear display 1.   Select the [CLR DISP] button, located |  |
| on the [Toolbar] . All onscreen graphics | ☐ Passed |
| other than the Ownship symbol and the |  |
| cartography should be removed. |  |
| 2. Select the [CLR DISP] button again. All |  |
| the graphics should reappear. |  |
| Screen        1.   Open the Shortcuts menu. |  |
| brightness | ☐ Passed |
| 2. Check that the screen brightness can |  |
| be adjusted. |  |
| Check         1.   Open the [Device selection] menu and |  |
| sensor data        check data all expected sensors are | ☐ Passed |
| present and available. |  |
| 2. Check that the sensor data appears |  |
| accurate. |  |
| 3.   Ensure the preferred data sources are |  |
| selected. |  |
| Check         1.   Select [Navigation mode]. |  |
| cartography | ☐ Passed |
| 2. Pan to an area covered by your ENC |  |
| data. |  |
| 3.   Range in and select each of the |  |
| cartography details icons in turn |  |
| ensuring that the level of detail changes |  |
| as expected. |  |

<!-- pdf page 53 | printed page 53 -->

### 7.3 AIS target test record

If AIS testing is not applicable tick here:   ☐, otherwise complete the following tests: Test            Steps                                           Pass Enable AIS      1.   Ensure [STAB H-up] orientation is selected.                                  ☐ Passed 2. Enable the [AIS] toggle switch in the [TGT] Targets menu. 3.   Check that AIS target symbols appear onscreen. 1.   Select an AIS target. Activate AIS target ☐ Passed 2. Ensure that the target vectors are displayed. 3.   Open the AIS target context menu and ensure that data for the AIS target is available. 1.   Double click on an activated AIS target, Deactivate AIS target           or disable the [Activate AIS] toggle       ☐ Passed switch. 2. Check that vector lines are removed. 1.   Disable the [AIS] toggle switch in the Disable AIS [TGT] Targets menu.                        ☐ Passed 2. Check that AIS target symbols no longer appear onscreen.

### 7.4 ARPA target test record

If ARPA testing is not applicable tick here:   ☐, otherwise complete the following tests: Test            Steps                                          Pass Enable          1.   Using your connected radar system ARPA                 acquire several ARPA targets.             ☐ Passed 2. On the ECDIS, ensure [STAB H-up] orientation is selected. 3.   Enable the [ARPA] toggle switch in the [TGT] Targets menu. 4.   Check that the acquired ARPA target symbols appear onscreen. ARPA            1.   Select an ARPA target. targets                                                        ☐ Passed 2. Ensure that the target vectors are displayed. 3.   Open the ARPA target context menu and ensure that data for the ARPA target is available. 1.   Disable the [ARPA] toggle switch in the Disable ARPA                 [TGT] Targets menu.                       ☐ Passed 2. Check that ARPA target symbols no longer appear onscreen.

<!-- pdf page 54 | printed page 54 -->

### 7.5 Equipment Registration Certificate

This certificate must be completed in full, and returned to Raymarine UK Ltd. The system warranty will then be activated.

###### All sections must be completed:

Installation date:                     Installation company name:

Installation Engineer Name:

Vessel Name:                           Vessel Owner Name & Address:

IMO Number:

Vessel type:

Port:

| Display serial number: | Display software version: |
| --- | --- |
| DCU\DCU-2 serial number: | DCU\DCU-2 software version: |

###### Complete the following questions:

|  | Yes    No |
| --- | --- |
| 1. Did you unpack | If yes please answer question 2, |
| the equipment? | ☐ ☐           otherwise proceed to question 3. |
| 2. Was the | If yes please provide photographs |
| packaging | ☐ ☐           and comment in the available white |
| damaged? | space or on a separate sheet. Yes    No |
| 3. Were any items | If yes please provide details in |
| missing? | ☐ ☐              the available white space or on a separate sheet. |
| 4. Were all supplied | If no please provide details in |
| cables and fittings | ☐ ☐              the available white space or on a |
| correct? | separate sheet. |
| 5. Did the equipment | If no please provide details in |
| work first time? | ☐ ☐              the available white space or on a separate sheet and then answer question 6. |
| 6. Did you get the | If yes please provide corrective |
| equipment to work? | ☐ ☐              actions taken in the available white space or on a separate sheet, and then answer question 7. |
| 7. Were any spare | If yes please provide details in |
| parts required to get    ☐ ☐              the available white space or on a |  |
| the equipment to | separate sheet. |
| work? |  |
| All equipment | Wiring                        Cable runs |
| properly installed   ☐     electrically           ☐      secured and      ☐ |  |
| and earthed? | tested and                    tidy? labelled? |
| Latest software | System tested                 Crew / |
| loaded?              ☐     and adjusted?          ☐      Customer         ☐ | handover complete? |

<!-- figure 1 on pdf page 54 at 41,454-413,547 pt | caption: none | text-layer labels: Yes | 1. Did you unpack the equipment? | 2. Was the packaging damaged? | No | � � � � | nearby labels: Complete the following questions: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 55 | printed page 55 -->

| Signature of Installation Engineer | Signature of Master |
| --- | --- |
| Sign: | Sign: |
| Print name: | Print name: |
| Date: (DD/MM/YYYY): | Date: (DD/MM/YYYY): |

<!-- pdf page 56 | printed page 56 -->

### 7.6 Customer handover & sign off

Once the installation and commissioning has been successfully completed, the following must be handed to the most senior member of the crew, ship owner, or agent.

###### Customer handover:

System manuals / instructions. ☐ System drawings (if applicable). ☐ Fully completed copy of test records. ☐ Fully completed Equipment Registration Certificate. ☐ Completed warranty registration for each system component.                                                      ☐ System backup.

###### Return to Raymarine UK Ltd:

Fully completed service / installation report ☐ Where possible, photographs of installed system components and wiring.                                          ☐ System manuals / instructions. ☐ System drawings (Iif applicable). ☐ Fully completed copy of test records. ☐ Fully completed Equipment Registration Certificate. ☐ Completed warranty registration for each system component.                                                      ☐ System backup. ☐ Shipyard: Customer:

- Vessel, hull, or
- project reference:

| Signed (Raymarine | Sign: | Print Name: |
| --- | --- | --- |
| UK Ltd |  |  |
| representative) |  |  |
| Date: |  |  |
| Signed (Customer): | Sign: | Print Name: |

Date:

<!-- figure 1 on pdf page 56 at 41,120-360,275 pt | caption: none | text-layer labels: System manuals / instructions. | System drawings (if applicable). | Fully completed copy of test records. | System backup. | nearby labels: Customer handover: | Return to Raymarine UK Ltd: | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 57 | printed page 57 -->

## CHAPTER 8: TROUBLESHOOTING

#### CHAPTER CONTENTS

Troubleshooting                                   57

<!-- pdf page 58 | printed page 58 -->

### 8.1 Troubleshooting

The troubleshooting section provides possible causes and the corrective action required for common problems that are associated with the installation and operation of your product. Before packing and shipping, all products are subjected to comprehensive testing and quality assurance programs. If you do experience problems with your product, this section will help you to diagnose and correct problems to restore normal operation. If after referring to this section you are still having problems with your product, please refer to the Technical support and servicing section of this manual for useful links and contact details.

### 8.2 LED Diagnostics

The Display’s “Power swipe” key is illuminated using LEDs. The LED color and flash sequence identifies the status of the display, along with any error codes. LED indication                  Status and required action (White) Powered up / Ok Normal operation — no user action is required.

###### (Red) Standby

Swipe to power up display.

###### (Red flash: 1 per second) Low voltage

- Increase supply voltage to within operating temperature range.
- Check power cabling and connections for damage and corrosion; replace if required.

LED indication   Status and required action (Red flash: 2 per second) High voltage • Reduce supply voltage to within operating temperature range.

###### (Red / Blue alternating flash) High

temperature
- Check display installation for adequate ventilation and ‘free’ space around rear of display.
- Check ambient temperature; if high, consider powering down the display until ambient temperature reduces.

<!-- figure 1 on pdf page 58 at 432,65-573,120 pt | caption: none | text-layer labels: none | nearby labels: LED indication | OCR below floor, text not used (2/7 words >= 60, mean confidence 30) -->

<!-- figure 2 on pdf page 58 at 432,129-573,170 pt | caption: none | text-layer labels: none | OCR: no legible text (0/9 words >= 60, mean confidence 16) -->

<!-- figure 3 on pdf page 58 at 43,301-189,349 pt | caption: none | text-layer labels: none | nearby labels: LED indication | OCR: no legible text (0/2 words >= 60, mean confidence 45) -->

<!-- figure 4 on pdf page 58 at 46,354-187,399 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 58 at 48,406-187,459 pt | caption: none | text-layer labels: none | OCR: no legible text (0/3 words >= 60, mean confidence 22) -->

<!-- pdf page 59 | printed page 59 -->

### 8.3 Power up troubleshooting

###### Product does not turn on or keeps turning off

| Possible causes | Possible solutions |
| --- | --- |
| Blown fuse / tripped | 1.   Check condition of relevant fuses and breakers |
| breaker | and connections, and replace if necessary. (Refer to the Technical Specification section of your product’s installation instructions for fuse ratings.) 2. If fuse keeps blowing, check for cable damage, broken connector pins or incorrect wiring. |
| Poor / damaged | 1.   Check that the power cable connector is |
| / insecure power | correctly orientated and fully inserted into the |
| supply or cable / | display connector and locked in position. |
| connections | 2. Check the power supply cable and connectors for signs of damage or corrosion, and replace if necessary. 3.   With the display turned on, try flexing the power cable near to the display connector to see if this causes the unit to restart or lose power. Replace if necessary. 4.   Check the vessel’s battery voltage and the condition of the battery terminals and power supply cables, ensuring connections are secure, clean and free from corrosion. Replace if necessary. 5. With the product under load, using a multi-meter, check for high voltage drop across all connectors / fuses etc, and replace if necessary. |
| Incorrect power | The power supply may be wired incorrectly, ensure |
| connection | the installation instructions have been followed. |

Troubleshooting

###### Product will not start up (restart loop)

| Possible causes | Possible solutions |
| --- | --- |
| Power supply and | See possible solutions from the table above, entitled |
| connection | ‘Product does not turn on or keeps turning off’. |
| Software corruption | In the unlikely event that the product’s software has become corrupted, contact Raymarine to obtain and install the latest software. |

59

<!-- pdf page 60 | printed page 60 -->

## CHAPTER 9: TECHNICAL SUPPORT

#### CHAPTER CONTENTS

<!-- pdf page 61 | printed page 61 -->

### 9.1 Pathfinder technical support

- For technical support for you Pathfinder system please call: +1 978–850–3025. If you need to request technical support, please have the following
- information to hand:
- Product name.
- Product identity.
- Serial number.
- Software application version.
- System diagrams.

### 9.2 Approval certificates

Copies of the type approval certificates for the system can be obtained through the Raymarine Commercial website:: https://www.bit.ly/ray-commdocs

Technical support                                                               61

<!-- pdf page 62 | printed page 62 -->

## CHAPTER 10: IEC-61162 MESSAGES

#### CHAPTER CONTENTS

<!-- pdf page 63 | printed page 63 -->

### 10.1 IEC61162 Messages

The following table details the IEC61162 messages that can be accepted by the Pathfinder ECDIS operating system. This list is current for the Pathfinder ECDIS operating system v1.0, and is subject to change with later versions of software.

- Note: Items in bold are mandatory sentences.

###### Input

| Telegram            Parameter |  |
| --- | --- |
| ACN | Alert Command |
| ALR | Alarm State |
| DBT | Depth Below Transducer |
| DPT | Depth |
| DTM | Datum Reference |
| GGA | Geographic Position (GPS Fix Data) |
| GLL | Geographic Position (Latitude and Longitude) |
| GNS | Geographic Position (GNSS Fix Data) |
| HBT | Heartbeat |
| HDT | Heading True |
| MWV | Wind Speed and Angle |
| RMC | Recommended Minimum Specific GNSS Data |
| ROT | Rate of turn |
| RRT | Report Route Transfer |
| SRP | System function ID Resolution Protocol* |
| THS | True Heading and Status |
| TLB | Tracked Target Label |
| TTD | Tracked Target Data |
| TTM | Tracked Target Message |
| IEC-61162 messages |  |
| Telegram | Parameter |
| VBW | Dual Ground/Water Speed |
| VDM | AIS Target Data |
| VDO | AIS Ownship Information |
| VHW | Water Speed and Heading |
| VSD | AIS Voyage Static Data |
| VTG | Course Over Ground and Ground Speed |
| ZDA | Time and Date |

###### Output

| Telegram | Parameter | Transmission Time |
| --- | --- | --- |
| ALC | Cyclic Alert Output | 30 seconds |
| ALF | Alert Data Output | Event based (on alert state change or on request by ACN) |
| ARC | Alert Command Refused | Event based (on command refused) |
| EVE | General Event Message | Event based (1 second after user input) |
| HBT | Heartbeat | 30 seconds |
| RRT | Report Route Transfer | Event based or on request when IEC61162–450 is enabled). |
| VSD | AIS Voyage Static Data | When [Set Voyage Data] is pressed. |
| VR | Screen Output | Period defined during commissioning. |

63

<!-- pdf page 64 | printed page 64 -->

## CHAPTER 11: IEC-61162-450 SUPPORT

#### CHAPTER CONTENTS

<!-- pdf page 65 | printed page 65 -->

### 11.1 IEC-61162-450 Support

The system supports communication compliant to IEC 61162-450. When configuring for a -450 network the IP address must be 192.168.0.0/24 – 192.168.10.0/24 and 172.16.0.0/16. The underlying network for communication compliant to IEC 61162-450 is Ethernet based. All interface connections must meet the requirements of IEC 61162-450. System Function ID (SFI) is configured during the commissioning process, as detailed here: Configuring an SFI

###### Transmission Group

All supported transmission groups are shown in the table below. To remain IEC 61162-450 compliant, all multicast addresses must be configured within these transmission groups. Some of the transmission groups are set up by default, but will need to be enabled. Others can be added as a new device, as detailed here: p.42 — External devices

| Transmission | Multicast | Destination port   Setting |  |
| --- | --- | --- | --- |
| Group | Address |  |  |
| MISC | 239.192.0.1 | 60001 | To be added |
| TGTD | 239.192.0.2 | 60002 | Disabled |
| SATD | 239.192.0.3 | 60003 | Disabled |
| NAVD | 239.192.0.4 | 60004 | Disabled |
| VDRD | 239.192.0.5 | 60005 | Disabled |
| RCOM | 239.192.0.6 | 60006 | To be added |
| TIME | 239.192.0.7 | 60007 | To be added |
| PROP | 239.192.0.8 | 60008 | To be added |
| USR1 to USR8 | 239.192.0.9 to   60009 to 60016 239.192.0.16 |  | To be added |
| BAM1 | 239.192.0.17 | 60017 | To be added |
| BAM2 | 239.192.0.18 | 60018 | To be added |
| CAM1 | 239.192.0.19 | 60019 | To be added |

| Transmission | Multicast | Destination port | Setting |
| --- | --- | --- | --- |
| Group | Address |  |  |
| CAM2 | 239.192.0.20 | 60020 | To be added |
| NETA | 239.192.0.56 | 60056 | To be added |

65

<!-- pdf page 66 | printed page 66 -->

## CHAPTER 12: ABBREVIATIONS

#### CHAPTER CONTENTS

<!-- pdf page 67 | printed page 67 | header: Term / Abbreviation -->

## Term / Abbreviation

| 12.1 Abbreviations |  | Term | Abbreviation |
| --- | --- | --- | --- |
| Term | Abbreviation   Bearing Waypoint To Waypoint |  | BWW |
| Acknowledge | ACK | Bow Crossing Range | BCR |
| Acquire, Acquisition | ACQ | Bow Crossing Time | BCT |
| Aids to Navigation (applies to AIS) | AtoNs | Built in Test Equipment | BITE |
| Air Search & Rescue (applies to AIS) | ASARs | Calibrate | CAL |
| Acquisition Zone | AZ | Cancel | CNCL |
| Additional Military Layer | AML | Cancel All | CNCL ALL |
| Adjust, Adjustment | ADJ | Category | CAT |
| All-purpose STructured Eurocontrol suRveillance   ASTERIX |  | Center | CENT |
| Information eXchange |  | Change | CHG |
| Altitude | ALT | Chart Display Settings | CHT DISP SET |
| Anchor Watch | ANCH | Chart Management | CHT MGMT |
| Antenna | ANT | Chart Safety Settings | CHT SF SET |
| Automatic | AUTO | Circularly Polarized | CP |
| Automatic Frequency Control | AFC | Clear | CLR |
| Automatic Gain Control | AGC | Closest Point of Approach | CPA |
| Automatic Identification System | AIS | Compact Disc Read Only Memory | CD-ROM |
| Automatic Identification System – Search and      AIS-SART |  | Conning | CONN |
| Rescue Transmitter |  | Consistent Common Reference Point    CCRP |  |
| Automatic Radar Plotting Aid | ARPA | Consistent Common Reference System   CCRS |  |
| Autopilot | AP | Contrast | CONT |
| Auxiliary System / Function | AUX | Coordinated Universal Time | UTC |
| Available | AVAIL | Correction | CORR |
| Admiralty Vector Chart Service | AVCS | Course | CRS |
| Azimuth Indicator | AZI | Course Over the Ground | COG |
| Background | BKGND | Course Through the Water | CTW |
| Beacon mode | BCM | Course To Steer | CTS |
| Bearing | BRG |  |  |

<!-- pdf page 68 | printed page 68 | header: Term / Term / Abbreviation / Abbreviation -->

## Term / Term / Abbreviation / Abbreviation

| Course Up | C UP | Down | DN |
| --- | --- | --- | --- |
| Cross Track Distance | XTD | Drift | DRIFT |
| Cross Track Limit | XTL | Electromagnetic Compatibility | EMC |
| Cursor | CURS | Electronic Bearing Line | EBL |
| Curved Heading Line | CHL | Electronic Chart Display and Information System    ECDIS |  |
| Dangerous Goods | DG | Electronic Chart System | ECS |
| Data Collection Unit | DCU | Electronic Navigational Chart | ENC |
| Date | DATE | Electronic Position Fixing System | EPFS |
| Dated Objects | DO | Electronic Range and Bearing Line | ERBL |
| Day | DAY | Emergency Position Indicating Radio Beacon | EPIRB |
| Day/Night | DAY/NT | Emergency Position Indicating Radio Beacon – AIS   EPIRB-AIS |  |
| Dead Reckoning, Dead Reckoned Position   DR |  | ENC Management Report | ENC MGMT REP |
| Decrease | DECR | ENC Update Status Report | ENC UPD STATUS |
| Default Settings | DFLT SET   Enhance |  | ENH |
| Delay | DELAY | Enter | ENT |
| Delete | DEL | Equipment | EQUIP |
| Departure | DEP | Error | ERR |
| Depth | DPTH | Estimated Position | EP |
| Destination | DEST | Estimated Time of Arrival | ETA |
| Deviation | DEV | Estimated Time of Departure | ETD |
| Differential GNSS | DGNSS | European Geo-Stationary Navigational Overlay | EGNOS |
| Differential GPS | DGP | System Event | EVENT |
| Digital Selective Calling                DSC |  | Exclusion Zone | EZ |
| Display | DISP | Export Route | ROUTE EXP |
| Display Settings | DISP SET | External | EXT |
| Display Brilliance | BRILL | Federal Communications Commission | FCC |
| Distance | DIST | Frequently Asked Questions | FAQ |
| Distance To Go | DTG |  |  |

<!-- pdf page 69 | printed page 69 | header: Term / Term / Abbreviation / Abbreviation -->

| Forward | FWD | Initialization | INIT |
| --- | --- | --- | --- |
| Frequency | FREQ | Input | INP |
| Global Maritime Distress and Safety System    GMDSS |  | Input/Output | I/O |
| Global Navigation Satellite System | GNSS | Integrated Navigation System | INS |
| Global Orbiting Navigation Satellite System   GLONASS |  | Integrated Radio Communication System | IRCS |
| Global Positioning System | GPS | Interference Rejection | IR |
| Great Circle | GC | International Maritime Organization | IMO |
| Grid | GRID | Innovation, Science and Economic Development   ISED |  |
| Ground | GND | Canada — previously Industry Canada (IC) |  |
| Grounding Avoidance System | GAS | Interval | INT |
| Guard Zone | GZ | JavaScript Object Notation | JSON |
| Head Up | H UP | Label | LBL |
| Heading | HDG | Latitude | LAT |
| Heading Line | HL | Latitude / Longitude | L/L |
| Heading Line Off | HL OFF HDMI | Leeway Light Emitting Diode | LWY LED |
| High Definition Multimedia Interface |  | Limit | LIM |
| High Frequency | HF | Line Of Position | LOP |
| High Speed Craft | HSC | Liquid Crystal Display | LCD |
| Horizontal Dilution Of Precision | HDOP | Local Area Network | LAN |
| Identification | ID | Log | LOG |
| Import Chart | IMPORT CHT | Long Pulse | LP |
| Import Route | ROUTE IMP | Long Range | LR |
| Increase | INCR | Longitude | LON |
| Indication | IND | Loran | LORAN |
| Information | INFO | Lost Target | LOST TGT |
| Information Report | INFO REPORT | Low Frequency | LF |
| Infrared | INF RED | Magnetic | MAG |

<!-- pdf page 70 | printed page 70 | header: Term / Term / Abbreviation / Abbreviation -->

| Main Bang Suppression | MBS | Out / Output | OUT |
| --- | --- | --- | --- |
| Man Overboard | MOB | Own Ship | OS |
| Manoeuvre | MVR | Own Ship Look-Ahead | LOOK AHEAD |
| Manual | MAN | Panel Illumination | PANEL |
| Manual Update | MAN UPD | Parallel Index Line | PI |
| Map(s) | MAP | Past Positions | PAST POSN |
| Maritime Mobile Services Identity number   MMSI |  | Passenger Vessel (applies to AIS)   PASSV |  |
| Maritime Pollutant (applies to AIS)        MP |  | Performance Monitor | MON |
| Maritime Safety Information | MSI | Permanent | PERM |
| Marker | MKR | Person Overboard | POB |
| Master | MSTR | Personal Computer | PC |
| Maximum | MAX | Personal Identification Number | PIN |
| Medium Frequency | MF | Pilot Vessel | PILOT |
| Medium Pulse | MP | Position | POSN |
| Menu | MENU | Positional Dilution Of Precision    PDOP |  |
| Minimum | MIN | Power | PWR |
| Missing | MISSING | Predicted | PRED |
| Mute | MUTE | Predicted Area of Danger | PAD |
| Nautical Mile | NM | Predicted Point of Collision | PPC |
| Navigation | NAV | Pulse Length | PL |
| Night | NT | Pulse Repetition Frequency | PRF |
| Normal | NORM | Pulse Repetition Rate | PRR |
| North Up | N UP | Pulses Per Revolution | PPR |
| Off | OFF | Racon | RACON |
| Off-centered | OFF CENT   Radar |  | RADAR |
| Officer of the Watch | OOW | Radar Cross Section | RCS |
| Offset | OFFSET | Radar Overlay | RADAR OVR |
| On | ON | Radar Settings | RADAR SET |

<!-- pdf page 71 | printed page 71 | header: Term / Term / Abbreviation / Abbreviation -->

| Radar Plotting | RP | Short Pulse |  | SP |
| --- | --- | --- | --- | --- |
| Radar Transponder | TPR | Signal to Noise Ratio |  | SNR |
| Radio Frequency | RF | Silence |  | SLNC |
| Radius | RAD | Simulation |  | SIM |
| Range | RNG | Slave |  | SLAVE |
| Range Rings | RR | Sleeping Target (applies to AIS) |  | ST |
| Raster Chart Display System | RCDS | Speed |  | SPD |
| Raster Navigational Chart | RNC | Speed and Distance Measuring Equipment   SDME |  |  |
| Rate Of Turn | ROT | Speed Over the Ground |  | SOG |
| Receiver | RX | Speed Through the Water |  | STW |
| Receiver Autonomous Integrity Monitoring     RAIM |  | Stabilized |  | STAB |
| Reference | REF | Standard Display |  | STND DISP |
| Relative | R | Standby |  | STBY |
| Relative | REL | Starboard/Starboard Side |  | STBD |
| Relative Motion | RM | Station |  | STN |
| Revolutions Per Minute | RPM | Symbol(s) |  | SYM |
| Rhumb Line | RL | Synchronization |  | SYNC |
| Roll On / Roll Off Vessel (applies to AIS)   RoRo |  | System Electronic Navigational Chart     SENC |  |  |
| Root Mean Square | RMS | System Function Identifier |  | SFI |
| Save User Settings | SAVE USR   Target |  |  | TGT |
| S-Band (applies to radar) | S-BAND | Target Association |  | TA |
| Safety Of Life At Sea (Convention) | SOLAS | Target Tracking |  | TT |
| Scan to Scan | SC/SC | Time Difference |  | TD |
| Search And Rescue | SAR | Time Dilution Of Precision |  | TDOP |
| Search And Rescue Transponder | SART | Time Of Arrival |  | TOA |
| Search And Rescue Vessel | SARV | Time Of Departure |  | TOD |
| Select | SEL | Time to CPA |  | TCPA |
| Select User Settings | USR SEL |  |  |  |

<!-- pdf page 72 | printed page 72 | header: Term / Term / Abbreviation / Abbreviation -->

| Time To Go | TTG | Vector | VECT |
| --- | --- | --- | --- |
| Time to Wheel Over Line | TWOL | Very High Frequency | VHF |
| Track | TRK | Very Low Frequency | VLF |
| Track Control System | TCS | Vessel Aground (applies to AIS) | GRND |
| Tracking | TRKG | Vessel at Anchor (applies to AIS) | ANCH |
| Track Made Good | TMG | Vessel Constrained by Draught (applies to AIS) | VCD |
| Transceiver | TXRX | Vessel Engaged in Diving Operations | DIVE |
| Transferred Line Of Position   TPL |  | Vessel Engaged in Dredging or Underwater | DRG |
| Transmitter | TX | Operations (applies to AIS) |  |
| Transmitting Heading Device | THD | Vessel Engaged in Towing Operations (applies to     TOW AIS) |  |
| Trial | TRIAL | Vessel Not Under Command (applies to AIS) | NUC |
| Trial Manoeuvre | TM | Vessel Restricted in Manoeuverability (applies to   RIM |  |
| Trial Settings | TRIAL SET   AIS) |  |  |
| Trigger Pulse | TRIG | Vessel Traffic Service | VTS |
| True | T | Vessel Underway Using Engine (applies to AIS) | UWE |
| True Motion | TM | Video | VID |
| Tune | TUNE | Visual Display Unit | VDU |
| UltraHigh Frequency | UHF | Voltage Converter Module | VCM |
| Uninterruptible Power Supply   UPS |  | Voyage | VOY |
| Universal Serial Bus | USB | Voyage Data Recorder | VDR |
| Universal Time, Coordinated | UTC | Water | WAT |
| Unstabilized | UNSTAB | Waypoint | WPT |
| Update Log | UPD LOG | Waypoint Closure Velocity | WCV |
| Update Review | UPD REV | Wheel Over Line | WOL |
| User Chart | USR CHT | Wheel Over Point | WOP |
| User Maps | UM | Wheel Over Time | WOT |
| Variable Range Marker | VRM |  |  |
| Variation | VAR |  |  |

<!-- pdf page 73 | printed page 73 | header: Term / Abbreviation -->

## Term / Abbreviation

| World Geodetic System | WGS |
| --- | --- |
| X-Band (applies to radar) | X-BAND |

<!-- pdf page 74 | printed page 74 -->

(no text layer on this page)

<!-- pdf page 75 | printed page 75 | header: Alert / Type / Alert Identifier / Category -->

## Alert / Type / Alert Identifier / Category

| Appendix A Alerts list |  |  |  | Alert | Type | Category   Alert | Identifier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A list of available alerts and their category and identifier is shown below |  |  |  | Lost AIS Input | Warning | B | 3015 |
| Alert | Type | Category        Alert | Identifier   Lost AIS Input |  | Alarm | B | 3014 |
| Anchor Watch | Warning | A | 3032 | Different Geodetic Datum | Warning | B | 3005 |
| Anchor Watch | Alarm | A | 3031 | Different Geodetic Datum | Alarm | B | 3004 |
| Position System Failure | Caution | B | 3016 | XTD Limit | Alarm | A | 3024 |
| Position System Failure | Warning | B | 3015 | Safety Contour Crossing | Alarm | A | 3031 |
| Position System Failure | Alarm | B | 3014 | Crossing Navigation Hazard | Caution | A | 3036 |
| Lost Heading Input | Caution | B | 3016 | Crossing Navigation Hazard | Warning | A | 3035 |
| Lost Heading Input | Warning | B | 3015 | Approach to area | Caution | A | 3036 |
| Lost Heading Input | Alarm | B | 3014 | Approach to area | Warning | A | 3035 |
| Lost Speed Over Ground | Caution | B | 3016 | Approach to the critical point Warning   A |  |  | 3038 |
| Input |  |  |  | Approach to the critical point Alarm |  | A | 3037 |
| Lost Speed Over Ground | Warning | B | 3015 | AIS Capacity about to be | Caution | A | 3043 |
| Input |  |  |  | exceeded |  |  |  |
| Lost Speed Over Ground | Alarm | B | 3014 | AIS Capacity exceeded | Warning | A | 3042 |
| Input |  |  |  | AIS Capacity exceeded | Alarm | A | 3041 |
| Lost Speed Through Water | Caution | B | 3016 |  |  |  |  |
| Input |  |  |  | ARPA Capacity about to be exceeded | Caution | A | 3043 |
| Lost Speed Through Water | Warning | B | 3015 |  |  |  |  |
| Input |  |  |  | ARPA Capacity exceeded | Warning | A | 3042 |
| Lost Speed Through Water | Alarm | B | 3014 | ARPA Capacity exceeded | Alarm | A | 3041 |
| Input |  |  |  | Lost Target | Warning | B | 3052 |
| Lost Wind Input | Caution | B | 3016 | Lost Target | Alarm | B | 3051 |
| Lost Wind Input | Warning | B | 3015 | Dangerous Target | Alarm | A | 3044 |
| Lost Wind Input | Alarm | B | 3014 | S63 User Permit Error | Caution | A | 10003 |
| Lost Depth Input | Caution | B | 3016 |  |  |  |  |
| Lost Depth Input | Warning | B | 3015 |  |  |  |  |
| Lost Depth Input | Alarm | B | 3014 |  |  |  |  |
| Lost AIS Input | Caution | B | 3016 |  |  |  |  |
| Alerts list |  |  |  |  |  |  | 75 |

<!-- pdf page 76 | printed page 76 -->

#### Appendix B DCU settings overview

The Pathfinder DCU is supplied pre-configured, ready for use with the system. The configuration is shown below and is provided for troubleshooting purposes. Accessing the DCU web interface requires a laptop or personal computer to be connected directly to the DCU, or to the same network as the DCU using a free network connection and an appropriate network cable. Any popular web browser can be used to access the user interface. Enter the following web address into the web browser’s address bar: http://promux-xxxxxx Replacing the xxxxxx with the DCU’s serial number.

###### Homepage overview

1. [Information] icon.
2. [Status] icon.
3. [Settings] icon. [Information] icon Selecting the [Information] icon will display relevant technical information. This information is important for troubleshooting purposes, or require technical assistance at a future date. [Status] icon

- Selecting the [Status] icon displays the current status of the user-controlled
- settings:
- [Data Servers] – Displays the information about the data server, if enabled.
- [Serial] – Displays the current status of the serial ports, including their baud rate, alias name if applied, port direction, and the current data load on each port.
- [Detailed Stats] – Once the DCU is operational, this page shows the number of individual sentences being received or transmitted over a 10 second period.
- [Routing] – Matrix showing data flow between inputs and outputs.
- [Alarms] – Displays the status of any alarms which are currently set. [Settings] icon The [Settings] icon provides access to the device configuration settings. To access these settings you must log-in.
- By default the login details are:
- Username: admin
- Password: The password is provided on the product label. The settings page provides the following functionality:
- [Administration] – Change password or re-start the DCU.
- [Firmware Update] – Displays current firmware version and provides the facility to update the firmware.
- [Network] – Allows the network to be configured correctly depending on your particular setup.
- It is recommended that these settings are not altered.
- [Operating Mode] – Allows pre-configured modes to be selected.
- It is recommended that these settings are not altered.
- [Reset Password] – Reset the password to factory default.
- [Alarms] – Do NOT use. The Plugins menu is used to set up alarm IDs.
- [Data Server] – Provides facility to turn the data server on / off, as well as specifying data format output, direction, and output protocol.
- [Plugins] — Set up a relay connection to an external alarm system.
- [Routing] – Main configuration table, allowing precise routing of data between inputs and outputs. Provides access to ‘autoswitch’ operation and setup.

<!-- figure 1 on pdf page 76 at 53,239-398,414 pt | caption: none | text-layer labels: none | nearby labels: Homepage overview | 1. | OCR text follows (tesseract, unverified; 12/15 words >= 60, mean confidence 77) -->
-MUX-2
‘Combine 1°
Information
Status
Settings
Version 2 489, Web Version 1.620
<!-- end of figure 1 -->

<!-- pdf page 77 | printed page 77 -->

- [Serial] – Provides configuration for each port, including baud rate setting, data direction, an ‘alias’ naming facility, and also shows the current data load on each port.

Data server configuration The default data server configuration for the DCU is shown below..

###### Data servers

- 4 data servers are configured Server 1 to Server 4. The Data server settings
- are as follows:

| Server | Filter | Format | Direction | Protocol | Port |
| --- | --- | --- | --- | --- | --- |
| Server 1 | Enabled | NMEA 0183 | Both | UDP | 2001 |
| Server 2 | Enabled | NMEA 0183 | Both | UDP | 2002 |
| Server 3 | Enabled | NMEA 0183 | Both | UDP | 2003 |
| Server 4 | Enabled | NMEA 0183 | Both | UDP | 2004 |

DCU settings overview

Plugins configuration The default plugins configuration for the DCU is shown below.

###### Plugins

| Event | Relay On Time | Timeout | Unique Alarm Number | State |
| --- | --- | --- | --- | --- |
| Alarm | 1s |  | 0 | Disabled |
| Message |  |  |  |  |
| Event | 1s |  |  | Disabled |
| Message |  |  |  |  |
| Heartbeat |  | 40s |  | Enabled |

Message

77

<!-- figure 1 on pdf page 77 at 427,100-801,270 pt | caption: none; nearest centred text below: "0" | text-layer labels: Event | Relay On Time | Timeout | Unique Alarm Number | State | nearby labels: Plugins | Alarm Message | 1s | 0 | Disabled | OCR text follows (tesseract, unverified; 11/11 words >= 60, mean confidence 96) -->
Event Relay
Alarm Message
1s
Event Message
1s
Heartbeat Message
40s
<!-- end of figure 1 -->

<!-- pdf page 78 | printed page 78 -->

Serial configuration The default serial configuration for the DCU is shown below.

###### Serial

| Interface          Name |  |  | Mode | Speed |
| --- | --- | --- | --- | --- |
| IN1 | AIS |  | Auto | Set by Auto |
| IN2 | GPS 1 |  | Auto | Set by Auto |
| IN3 | Gyro |  | Auto | Set by Auto |
| IN4 | Speed Log |  | Auto | Set by Auto |
| Interface | Name         Mode | Speed |  |  |
| IN5 | Echo Sound | 4800 |  |  |
| IN6 | GPS 2 | 4800 |  |  |
| IN7 | Gyro 2 | 4800 |  |  |
| IN8 | Wind | 4800 |  |  |
| OUT1 | Track Out | 4800 |  |  |
| OUT2 | VDR | 4800 |  |  |
| DS1 | DS1 |  |  |  |
| DS2 | DS2 |  |  |  |
| DS3 | DS3 |  |  |  |
| DS4 | DS4 |  |  |  |

<!-- figure 1 on pdf page 78 at 38,96-413,476 pt | caption: none; nearest centred text below: "Auto" | text-layer labels: Interface | Name | Mode | Speed | nearby labels: Serial | IN7 | IN1 | AIS | Auto | Set by Auto | IN2 | GPS 1 | Auto | Set by Auto | OCR text follows (tesseract, unverified; 77/95 words >= 60, mean confidence 79) -->
Serial Settings
Direction
Load
0%
SERIAL
115200
0%
AIS
38400
Auto
0
IN2
GPS1
Auto
4800
0%
IN3
Gyro
Auto
4800
0%
IN4
Speed Log
Auto
4800
0%
INS
Echo Sound
4800
0%
GPS 2
4800
0%
IN7
4800
0%
Gyro 2
4800
Wind
0%
OUT1
Track Out
4800
0%
0%
OUT2
4800
38400
0
OUT4
38400
0%
OUTS
38400
0%
38400
0%
0%
500000
0%
0%
500000
0
0
03@
500000
0%
0
DS4
500000
0%
<!-- end of figure 1 -->

<!-- pdf page 79 | printed page 79 -->

Routing configuration The default routing configuration for the DCU is shown below.

###### Routing

| Source |  | Name | Destination |
| --- | --- | --- | --- |
| IN1 |  | AIS | DS1 |
| IN2 |  | GPS 1 | DS1 |
| IN3 |  | Gyro | DS2 |
| IN4 |  | Speed Log | DS3 |
| IN5 |  | Echo Sound | DS3 |
| DCU settings overview |  |  |  |
| Source | Name | Destination |  |
| IN6 | GPS 2 | DS3 |  |
| IN7 | Gyro 2 | DS3 |  |
| IN8 | Wind | DS3 |  |
| DS1 | DS1 |  |  |
| DS2 | DS2 |  |  |
| DS3 | DS3 |  |  |
| DS4 | DS4 | OUT1, OUT2, OUT3, OUT4, OUT5, OUT6 |  |

79

<!-- figure 1 on pdf page 79 at 38,93-413,459 pt | caption: none; nearest centred text below: "AIS" | text-layer labels: Source | Name | Destination | nearby labels: Routing | IN7 | IN1 | AIS | DS1 | IN2 | GPS 1 | DS1 | OCR text follows (tesseract, unverified; 11/23 words >= 60, mean confidence 54) -->
Routing Settings
B
on
a
4
+t
between both real and
<!-- end of figure 1 -->

<!-- pdf page 80 | printed page 80 -->

#### Appendix C DCU-2 settings overview

The Pathfinder DCU-2 is supplied pre-configured, ready for use with the system. The configuration is shown below and is provided for troubleshooting purposes. Accessing the DCU-2 web interface requires a laptop or personal computer to be connected directly to the DCU-2, or to the same network as the DCU-2 using a free network connection and an appropriate network cable. Any popular web browser can be used to access the user interface. Enter the following web address into the web browser’s address bar: http://prondc-xxxxxx Replacing the xxxxxx with the DCU-2’s serial number.

###### Homepage overview

| 1. | [Information] icon. |
| --- | --- |
| 2. | [Status] icon. |
| 3. | [Actisense-i] icon. |
| 4. | [Settings] icon. |

[Information] icon Selecting the [Information] icon will display relevant technical information. This information is important for troubleshooting purposes, or if technical assistance is required at a future date.

[Status] icon Selecting the [Status] icon displays the current status of the user-controlled settings: • [Data Servers] — Displays the information about the data server, if enabled. • [Serial] — Displays the current status of the serial ports, including their baud rate, alias name if applied, port direction, and the current data load on each port. • [Detailed Stats] — Once the DCU-2 is operational, this page shows the number of individual sentences being received or transmitted over a 10 second period. • [Routing] — Matrix showing data flow between inputs and outputs. • [Alarms] — Displays the status of any alarms which are currently set. [Settings] icon The [Settings] icon provides access to the device configuration settings. To access these settings you must log-in. By default the login details are: • Username: admin • Password: The password is provided on the product label. The settings page provides the following functionality:

###### System

- [Administration] — Change the login password.
- [Firmware Update] — Displays current firmware version and provides the facility to update the firmware.
- [Network] — Allows the network to be configured correctly depending on your particular setup.
- It is recommended that these settings are not altered.
- [Operating Mode] — Allows pre-configured modes to be selected.
- It is recommended that these settings are not altered.
- [Reset Device] — Restart the DCU-2, or restore default settings.
- [Reset Password] — Reset the password to factory default. Data
- [Actisense-i] — Configure [Actisense-i] settings.
- [Alarms] — Do NOT use.

<!-- figure 1 on pdf page 80 at 38,220-413,428 pt | caption: none | text-layer labels: none | nearby labels: Homepage overview | OCR text follows (tesseract, unverified; 21/26 words >= 60, mean confidence 80) -->
Actisense
PRO-NDC-1E2K
Information
Status
Actisense-i
Settings
3°
2024 Active Research Limited. All rights reserved. www.actisense.com
Firmware Version 2.546, Web Version 1.113
<!-- end of figure 1 -->

<!-- pdf page 81 | printed page 81 -->

| • [Data Server] — Provides facility to turn the data server on / off, as well as | Serial configuration |
| --- | --- |
| specifying data format output, direction, and output protocol. | The default serial configuration for the DCU-2 is shown below. |
| • [NMEA 2000] — Configure NMEA 2000 settings. |  |
| • [Routing] — Main configuration table, allowing precise routing of data | Serial |
| between inputs and outputs. Provides access to ‘autoswitch’ operation |  |
| and setup. |  |
| • [Serial] — Provides configuration for each port, including baud rate setting, |  |
| data direction, an ‘alias’ naming facility, and also shows the current data |  |
| load on each port. |  |

###### Data server configuration

The default data server configuration is shown below..

###### Data servers

- Two data servers are configured Server 1 and Server 2. The data server
- settings are as follows:

|  |  |  |  |  | Interface          Name IN1 IN2 | AIS GNSS 1 | Mode Auto Auto | Speed Set by Auto Set by Auto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Server | Filter | Direction | Protocol | Port | IN3 | Gyro | Auto | Set by Auto |
| Server 1 | Enabled | Both | UDP | 2001 | IN4 | Speed Log | Auto | Set by Auto |
| Server 2 | Enabled | Both | UDP | 2002 | IN5 OUT1 OUT2 DS1 DS2 | GNSS 2 Track Out VDR DS1 DS2 |  | 4800 4800 4800 |
| DCU-2 settings overview |  |  |  |  |  |  |  | 81 |

<!-- figure 1 on pdf page 81 at 427,98-801,311 pt | caption: none; nearest centred text below: "Mode" | text-layer labels: none | nearby labels: Serial | Interface | Name | Mode | Speed | IN1 | AIS | Auto | Set by Auto | OCR text follows (tesseract, unverified; 45/67 words >= 60, mean confidence 71) -->
Serial Settings
Name
Fitter Mode
interface
Format
Speed
Direction
Load
SERIAL
115200
0%
0%
0%
Gyro
0%
IN4
0%
Y
GNSS 2
0%
Out
NMEA 0183
OUT1
38400
0%
NMEA 0183
38400
0%
v
0%
osi@
NMEA 0183
115200
0%
0%
N2K ASCII
115200
0%
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 81 at 38,268-413,392 pt | caption: none; nearest centred text below: "Both" | text-layer labels: Server | Filter | Direction | Protocol | Port | nearby labels: IN1 | Server 1 | Enabled | Both | UDP | 2001 | Server 2 | Enabled | Both | UDP | 2002 | OCR text follows (tesseract, unverified; 19/21 words >= 60, mean confidence 89) -->
Data Server Settings
Server
Direction
Protocol
Port
2001
Both
UDP
Server 1
v
v
2002
Both
UDP
Server 2
<!-- end of figure 2 -->

<!-- pdf page 82 | printed page 82 -->

Routing configuration The default routing configuration for the DCU-2 is shown below.

###### Routing

| Source | Name | Destination |
| --- | --- | --- |
| IN1 | AIS | DS1 |
| IN2 | GNSS 1 | DS1 |
| IN3 | Gyro | DS1 |
| IN4 | Speed Log | DS1 |
| IN5 | GNSS 2 | DS1 |
| DS1 | DS1 |  |
| DS2 | DS2 |  |
| N2K | N2K | DS2 |

#### Appendix D Default external devices

###### Default IEC 61162–450 devices

The following IEC 61162–450 devices are configured by default. Usually there should be no need to change the default settings for these devices. These devices will need to be enabled.

###### TGTD

1. [Device Name]: TGTD
2. [Enable Device]: Disabled
3. [IEC 61162–450]: Enabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Disabled
6. [Receive address]: 239.192.0.2
7. [Receive Port]: 60002
8. [Strict / Loose]: Loose
9. [Transmit address]: 239.192.0.2
10. [Transmit Port]: 60002
11. [Input Telegrams] : TLB, TTD, VDM and VDO
12. [Output Telegrams] : None

###### SATD

1. [Device Name]: SATD
2. [Enable Device]: Disabled
3. [IEC 61162–450]: Enabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Disabled
6. [Receive address]: 239.192.0.3
7. [Receive Port]: 60003
8. [Strict / Loose]: Loose
9. [Transmit address]: 239.192.0.3
10. [Transmit Port]: 60003
11. [Input Telegrams] : HDT, ROT and THS
12. [Output Telegrams] : None

<!-- figure 1 on pdf page 82 at 38,100-413,380 pt | caption: none; nearest centred text below: "Name" | text-layer labels: none | nearby labels: Routing | Source | Name | Destination | OCR text follows (tesseract, unverified; 25/33 words >= 60, mean confidence 74) -->
Routing Settings
The matrix shows routes between both real and virtual interfaces.
A\ Basic routing can be overridden by Advanced Routing rules
t
t
a
<!-- end of figure 1 -->

<!-- pdf page 83 | printed page 83 | header: 4. -->

## 4.

###### NAVD

1. [Device Name]: NAVD
2. [Enable Device]: Disabled
3. [IEC 61162–450]: Enabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Disabled
6. [Receive address]: 239.192.0.4
7. [Receive Port]: 60004
8. [Strict / Loose]: Loose
9. [Transmit address]: 239.192.0.4
10. [Transmit Port]: 60004
11. [Input Telegrams] : DBT, DPT, GGA, GLL, RMC, VBW, VDM, VHW, VTG and ZDA
12. [Output Telegrams] : None

###### VDRD

1. [Device Name]: VDRD
2. [Enable Device]: Disabled
3. [IEC 61162–450]: Enabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Disabled
6. [Receive address]: 239.192.0.5
7. [Receive Port]: 60005
8. [Strict / Loose]: Loose
9. [Transmit address]: 239.192.0.5
10. [Transmit Port]: 60005
11. [Input Telegrams] : None
12. [Output Telegrams] : HBT

###### VDR Screen Output

1. [Device Name]: VDR Screen Output.
2. [Enable Device]: Disabled
3. [IEC 61162–450]: Enabled Default external devices

4. [Auto Detect]: Disabled
5. [Show Telegrams] : Disabled
6. [Receive address]: 239.192.0.26
7. [Receive Port]: 60026
8. [Strict / Loose]: Loose
9. [Transmit address]: 239.192.0.26
10. [Transmit Port]: 60026
11. [Input Telegrams] : None
12. [Output Telegrams] : VR The VDR Screen Output device also has the following default [VDR Advanced settings]:
- [Transmission delay]: 0 sec
- [Transmission period]: 8 sec
- [Destination SFI]: VR001
- [Binary File Transfer Type] : JPG
- [VDR Source]: MFD
- [Device Location]: -

Note: For the primary ECDIS station the transmission period should be set to 8 seconds, for a secondary station it is recommended that the transmission period is set to 12 seconds.

###### BAM

| 1. | [Device Name]: BAM. |
| --- | --- |
| 2. | [Enable Device]: Disabled |
| 3. | [IEC 61162–450]: Enabled |
| 4. | [Auto Detect]: Disabled |
| 5. | [Show Telegrams] : Disabled |
| 6. | [Receive address]: 239.192.0.17 . |
| 7. | [Receive Port]: 60017. |
| 8. | [Strict / Loose]: Loose 83 |

<!-- pdf page 84 | printed page 84 | header: 9. -->

## 9.

9. [Transmit address]: 239.192.0.17 .
10. [Transmit Port]: 60017.
11. [Input Telegrams] : ACN and HBT
12. [Output Telegrams] : ALC, ALF, ARC and HBT Default DCU/DCU-2 external devices The following data server devices are configured by default. Usually there should be no need to change the default settings for these devices.

###### DS1

1. [Device Name]: DS1
2. [Enable Device]: Enabled
3. [IEC 61162–450]: Disabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Enabled
6. [Receive address]: 198.18.7.255
7. [Receive Port]: 2001
8. [Strict / Loose]: Loose
9. [Transmit address]: 198.18.7.255
10. [Transmit Port]: 3001
11. [Input Telegrams] : GGA, GLL, RMC, VDM, VDO, VTG and ZDA
12. [Output Telegrams] : None

###### DS2

| 1. | [Device Name]: DS2 |
| --- | --- |
| 2. | [Enable Device]: Enabled |
| 3. | [IEC 61162–450]: Disabled |
| 4. | [Auto Detect]: Disabled |
| 5. | [Show Telegrams] : Enabled |
| 6. | [Receive address]: 198.18.7.255 |
| 7. | [Receive Port]: 2002 |
| 8. | [Strict / Loose]: Loose |
| 9. | [Transmit address]: 198.18.7.255 |

10. [Transmit Port]: 3002
11. [Input Telegrams] : HDT, ROT and THS
12. [Output Telegrams] : None

###### DS3

1. [Device Name]: DS3
2. [Enable Device]: Enabled
3. [IEC 61162–450]: Disabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Enabled
6. [Receive address]: 198.18.7.255
7. [Receive Port]: 2003
8. [Strict / Loose]: Loose
9. [Transmit address]: 198.18.7.255
10. [Transmit Port]: 3003
11. [Input Telegrams] : DBT, DPT, GGA, GLL, HDT, MWV, RMC, ROT, THS, VBW, VHW, VSD, VTG and ZDA
12. [Output Telegrams] : None

###### DS4

1. [Device Name]: DS4.
2. [Enable Device]: Enabled
3. [IEC 61162–450]: Disabled
4. [Auto Detect]: Disabled
5. [Show Telegrams] : Enabled
6. [Receive address]: 198.18.7.255 .
7. [Receive Port]: 3004.
8. [Strict / Loose]: Loose
9. [Transmit address]: 198.18.7.255 .
10. [Transmit Port]: 2004.
11. [Input Telegrams] : None
12. [Output Telegrams] : None

<!-- pdf page 85 | printed page 85 -->

- Note: The Transmit port on [DS4] is 2004 as this outputs to the DCU/DCU-2.

Default external devices                                                85 (no text layer on this page)

<!-- pdf page 86 -->

<!-- pdf page 87 -->

#### Index A

Alarms Alerts Alerts list............................................................................................ 46, 75 Alerts manager Anchor positions Displays ...........................................................................................14, 16 eSyncBox ........................................................................................ 15–16 Keyboard ....................................................................................... 25, 32

#### B

Backup .............................................................................................. 47–49

#### C

CCRP

#### D

Data servers configuration ................................................................. 77, 81 Configuration ................................................................................. 76, 80 DCU–2 DCU—2 Documentation

#### E

ECS

#### C

eSync................................................................................................. 23, 30 External Device positions

<!-- pdf page 88 -->

#### G

#### I

IEC 61162–450 Integrity

#### L

#### M

Menus

#### N

#### O

#### P

Pathfinder ........................................................................................... 19, 27 Product overview...............................................................................22, 29

#### R

Restore .............................................................................................. 47, 49

#### S

Secondary station..............................................................................20, 28 Software System example

#### T

Test record Trackball ............................................................................................. 23, 31

<!-- pdf page 89 -->

#### U

User data

#### W
