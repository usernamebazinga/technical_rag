# RNS-8

<!-- source: sources/RNS-8 Network/RNS-8 Installation instructions 87455 (Rev 2) (EN).pdf | extraction: extracted/RNS-8 Network/RNS-8 Installation instructions 87455 (Rev 2) (EN).md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- pdf page 1 -->

## Installation Instructions

Document number: 87455 (Rev 2) | English (en-US) | Date: 10-2025

<!-- figure 1 on pdf page 1 at 98,34-550,302 pt | caption: none; nearest centred text below: "RNS-8 Installation Instructions" | text-layer labels: none | nearby labels: RNS-8 Installation Instructions | OCR: no legible text (0/1 words >= 60, mean confidence 22) -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

###### Legal notices

<!-- omitted: "Trademark and patents notice" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair Use Statement" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Content notice" (pdf pages 3-5; 4 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 4 -->
<!-- pdf page 5 | printed page 5 -->
###### CHAPTER 3 PRODUCT AND SYSTEM

###### CHAPTER 8 CABLES AND CONNECTIONS —

<!-- pdf page 6 | printed page 6 -->

###### Power over Ethernet (PoE) power

10.6 Power cable extension (12 / 24 V

13.1 Raymarine technical support and

15.2 RayNet to RayNet cables and 15.3 RayNet to RJ45, and RJ45 (SeaTalk HS)

###### APPENDIX A ETHERNET (IPV4) NETWORKING OF RAYMARINE DEVICES WITH THIRD-PARTY

<!-- pdf page 7 | printed page 7 -->

## CHAPTER 1: IMPORTANT INFORMATION

### Safety warnings

###### Warning: Product installation and operation

- This product must be installed and operated in accordance with the instructions provided. Failure to do so could result in personal injury, damage to your vessel and/or poor product performance.
- Certified installation by an approved installer is recommended. A certified installation qualifies for enhanced product warranty benefits. Contact your dealer for further details.

###### Warning: Switch off power supply

Ensure that the vessel’s power supply is switched OFF before starting to install this product. Do NOT connect or disconnect equipment with the power switched on, unless instructed to do so in this document.

### Product warnings

###### Warning: Product grounding

Before applying power to this product, it MUST be correctly grounded, in accordance with the instructions provided.

###### Warning: Positive ground systems

Do NOT connect this unit to a system which has positive grounding.

###### Warning: Power supply voltage

Connecting this product to a voltage supply greater than the specified maximum rating may cause permanent damage to the unit. For the correct voltage, refer to the information label affixed to the product.

###### Warning: Powering PoE devices

PoE devices can often be powered via an Ethernet connection (PoE) OR via a dedicated power cable.

NEVER connect a PoE device’s dedicated power cable when it is being supplied PoE, unless the device is specifically designed to be connected to multiple power sources, as confirmed by the device’s instruction documents.

When the PoE device’s dedicated power cable is not connected, any bare-end wire connections must be separately covered with insulation.

###### Warning: Do NOT exceed maximum power output

When connected to a Power Sourcing Equipment (PSE) such as a PoE network switch or PoE Injector, different classes of PoE-consuming devices (“Powered Device”, PD) require different amounts of electrical current.

Do NOT connect a PoE-consuming device which exceeds the maximum power (in Watts ) that can be provided by the device supplying PoE (“Power Sourcing Equipment”, PSE).

For the maximum power output (in Watts ) provided by the PSE, refer to the device’s Technical Specification.

7

<!-- figure 1 on pdf page 7 at 41,94-86,218 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 7 at 41,223-86,298 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 7 at 334,266-379,434 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 7 at 175,324-314,389 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 7 at 41,329-86,389 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 75) -->
a
<!-- end of figure 5 -->

<!-- figure 6 on pdf page 7 at 41,394-86,446 pt | caption: none | text-layer labels: none | nearby labels: Important information | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 8 | printed page 8 -->

###### Warning: Ensure sufficient nominal voltage

- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) is itself sufficiently powered, with a stable supply of at least 10.8 V dc.
- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) provides a nominal supply voltage to the PD device in the range of 44 V to 57 V dc.

###### Caution: Power supply protection

When installing this product, ensure that the power source is adequately protected by means of a suitably-rated fuse or thermal circuit breaker.

###### Caution: Service and maintenance

This product contains no user serviceable components. Please refer all maintenance and repair to authorized Raymarine dealers. Unauthorized repair may affect your warranty.

### Regulatory notices

<!-- omitted: "Disclaimer" (pdf page 8; 2 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
###### THIS INFORMATION IS MADE AVAILABLE BY Raymarine ON

THE BASIS THAT YOU EXCLUDE TO THE FULLEST EXTENT LAWFULLY PERMITTED ALL LIABILITY WHATSOEVER FOR ANY LOSS OR DAMAGE HOWSOEVER ARISING OUT OF THE USE OF THIS INFORMATION OR RELIANCE UPON THIS INFORMATION. Raymarine does not exclude Raymarine’s liability (if any) to you for personal injury or death resulting from Raymarine UK Ltd negligence, for fraud or for any matter which it would be illegal to exclude or to attempt to exclude.

###### EMC installation guidelines

Raymarine equipment and accessories conform to the appropriate Electromagnetic Compatibility (EMC) regulations, to minimize electromagnetic interference between equipment and minimize the effect such interference could have on the performance of your system. Correct installation is required to ensure that EMC performance is not compromised.

Note: In areas of extreme EMC interference, some slight interference may be noticed on the product. Where this occurs the product and the source of the interference should be separated by a greater distance.

- For optimum EMC performance we recommend that wherever
- possible:

<!-- figure 1 on pdf page 8 at 41,29-86,166 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 9 | printed page 9 -->

- Raymarine equipment and cables connected to it are:
- At least 1 m (3.28 ft) from any equipment transmitting or cables carrying radio signals e.g. VHF radios, cables and antennas. In the case of SSB radios, the distance should be increased to 2 m (6.6 ft).
- More than 2 m (6.56 ft) from the path of a radar beam. A radar beam can normally be assumed to spread 20 degrees above and below the radiating element.
- The product is supplied from a separate battery from that used for engine start. This is important to prevent erratic behavior and data loss which can occur if the engine start does not have a separate battery.
- Raymarine specified cables are used.
- Cables are not cut or extended, unless doing so is detailed in the installation manual.

Note: Where constraints on the installation prevent any of the above recommendations, always ensure the maximum possible separation between different items of electrical equipment, to provide the best conditions for EMC performance throughout the installation.

###### Suppression ferrites

- Raymarine cables may be pre-fitted or supplied with suppression ferrites. These are important for correct EMC performance. If ferrites are supplied separately to the cables (i.e. not pre-fitted), you must fit the supplied ferrites, using the supplied instructions.
- If a ferrite has to be removed for any purpose (e.g. installation or maintenance), it must be replaced in the original position before the product is used.
- Use only ferrites of the correct type, supplied by Raymarine or its authorized dealers.
- Where an installation requires multiple ferrites to be added to a cable, additional cable clips should be used to prevent stress on the connectors due to the extra weight of the cable.

Important information

###### Connections to other equipment

Requirement for ferrites on non-Raymarine cables: If your Raymarine equipment is to be connected to other equipment using a cable not supplied by Raymarine, a suppression ferrite MUST always be attached to the cable near the Raymarine unit. For more information, refer to your third-party cable manufacturer.

<!-- omitted: "Declaration of Conformity" (pdf page 9; 6 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "PSTI Compliance" (pdf page 9; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Warranty policy and registration" (pdf pages 9-10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 10 | printed page 10 -->
###### Product disposal

Dispose of this product in accordance with the WEEE Directive. The Waste Electrical and Electronic Equipment (WEEE) Directive requires the recycling of waste electrical and electronic equipment which contains materials, components and substances that may be hazardous and present a risk to human health and the environment when WEEE is not handled correctly.

Equipment marked with the crossed-out wheeled bin symbol indicates that the equipment should not be disposed of in unsorted household waste. Local authorities in many regions have established collection schemes under which residents can dispose of waste electrical and electronic equipment at a recycling center or other collection point. For more information about suitable collection points for waste electrical and electronic equipment in your region, refer to the Raymarine website: https://bit.ly/rym-recycling

###### IMO and SOLAS

The equipment described within this document is intended for use on leisure marine boats and workboats NOT covered by International Maritime Organization (IMO) and Safety of Life at Sea (SOLAS) Carriage Regulations.

<!-- omitted: "Technical accuracy" (pdf page 9; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Publication copyright" (pdf pages 9-11; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 11 | printed page 11 -->
## CHAPTER 2: DOCUMENT INFORMATION

##### CHAPTER CONTENTS

###### 2.1 Applicable products (page 12)

###### 2.2 Product documentation (page 12)

###### 2.3 Document illustrations (page 12)

Document information                           11

<!-- pdf page 12 | printed page 12 -->

### 2.1 Applicable products

This document is applicable to the following products:

| Product | Part number | Description |
| --- | --- | --- |
| RNS-8 | A80732 | 8-port Gigabit PoE network switch |

### 2.2 Product documentation

The following documentation is applicable to your product: Document          Description                  Link

| 87455 | RNS-8 Installation Instructions (this document). | www.bit.ly/rns8-docs |
| --- | --- | --- |
| 87434 | RNS-8 Mounting template. | www.bit.ly/rns8-docs |

### 2.3 Document illustrations

Your product and if applicable, its user interface may differ slightly from that shown in the illustrations in this document, depending on product variant and date of manufacture. All images are provided for illustration purposes only.

<!-- pdf page 13 | printed page 13 -->

## CHAPTER 3: PRODUCT AND SYSTEM OVERVIEW

##### CHAPTER CONTENTS

###### 3.1 Product overview (page 14)

###### 3.2 Required additional components (page 15)

###### 3.3 System overview (page 15)

###### 3.4 Compatible network devices (page 16)

Product and system overview                            13

<!-- pdf page 14 | printed page 14 -->

### 3.1 Product overview

The Raymarine RNS-8 Ethernet network switch enables you to connect and share data between multiple devices featuring a RayNet connector (or RJ45 / SeaTalk HS connector, connected via adapter cables), at up to speeds of one Gigabit per second. The switch also provides 4 Power over Ethernet (PoE) ports, each allowing both power and data to be shared across a single cable to a PoE-compatible device.

The network switch has the following key features:
- 8x Ethernet ports (4x PoE ports, each supporting up to 30 W PoE, Classes 0 to 4), using waterproof RayNet connectors.
- Ability to mix a combination of PoE and non-PoE devices simultaneously, for a total of 8 devices (maximum PoE devices = 4; maximum non-PoE devices = 8).
- Each port can transfer data at the following speeds: 10 / 100 / 1000 Mbits/s.
- Multiple switches can be connected together in a “daisy chain” for expanded systems.
- Rugged enclosure — waterproof to IPx6, IPx7 standard.
- Ignition protection to EN ISO 8846:2017 standard.
- Status and speed LED indicators for each port.
- Compatible with devices featuring any of the following connectors:
- RayNet.
- RJ45 (SeaTalk HS), via adapter cables (available separately).
- RJ45, via adapter cables (available separately).

- Examples of Ethernet devices that can be networked together include:
- Radar scanner.
- Sonar module.
- Thermal camera.
- Multifunction display (MFD) / chartplotter.

Note: Connections to equipment with RJ45 or SeaTalk HS connectors must be made via adapter cables (available separately). For suitable adapter cables, refer to the following section: p.61 — RayNet to RJ45 adapter cables

###### Power over Ethernet (PoE)

Power over Ethernet (PoE) is a system which allows both power and data to be passed along a single CAT 6 Ethernet cable. There are 2 main types of PoE device: • Power Sourcing Equipment (PSE) — this PoE system component provides electrical power over a CAT 6 Ethernet cable. • Powered Device (PD) — this PoE system component is powered by the electrical power provided by the Power Sourcing Equipment (PSE). The RNS-8 Network Switch is a PSE (Power Sourcing Equipment) device, which can supply both data and power to a maximum of 4x connected Powered Devices (PD). Each Powered Device (PD) can be PoE Class 0 to 4, and each may draw a maximum of 30 W power (i.e. a maximum total power consumption of 120 W for all 4 devices combined). When a Powered Device (PD) is connected to one of the Network Switch’s PoE RayNet network ports, it is first checked to establish whether it is PoE-compatible, and if so, what class of device it is. If a connected Powered Device (PD) requires more power than the individual port’s maximum power output (30 W), then it will not be powered. Before connecting a Powered Device (PD) to the network switch, ensure that the maximum power output of the port to which it is connected PoE (i.e. 30 W) will not be surpassed.

<!-- figure 1 on pdf page 14 at 38,127-314,252 pt | caption: none; nearest centred text below: "The network switch has the following key features:" | text-layer labels: none | OCR text follows (tesseract, unverified; 7/12 words >= 60, mean confidence 65) -->
4
3e
Se
Te
1e
4
6
<!-- end of figure 1 -->

<!-- pdf page 15 | printed page 15 -->

- The following table lists the different classes of device, and their
- typical power draw:

| PoE Class                   Maximum power provided | Typical power |
| --- | --- |
| by Power Sourcing | required by |
| Equipment (PSE) | Powered Device (PD)(1) |

| Class 1 (Very low | 4W | ~3.84 W |
| --- | --- | --- |
| power draw) |  |  |
| Class 2 (Low | 7W | ~6.49 W |
| power draw) |  |  |
| Class 3 (Medium | 15.4 W | ~12.95 W |
| power draw) |  |  |
| Class 4 (High | 30 W | ~25.5 W |
| power draw) |  |  |
| Class 0 | 15.4 W | ~12.95 W |

(Classification unimplemented)

Note:
- (1) The power consumption figures provided in the third column in the table above are approximate figures only. The actual power consumption figures may differ, depending on the device.
- For more information on PoE requirements, refer to: p.55 — Power specification

### 3.2 Required additional components

Network switches must be used in conjunction with the following items, available separately from Raymarine.

###### Network cables

For information on suitable cables for your product, refer to: p.32 — Network connections

Product and system overview

###### Cable extensions

- Some installations may also require extensions to network or power cables. For further information on cable extensions, refer to the
- following sections:
- p.32 — Network connections
- p.35 — Power connections
- p.57 — Spares and accessories

### 3.3 System overview

The following example provides an overview of a typical system, including the available connections and the types of devices that can be connected to your network switch.

Note: The following system is shown as an example only, and may differ from your planned installation.

###### Example: typical system

| 1 | IP camera, powered via PoE. |
| --- | --- |
| 2 | RNS-8 network switch. |

15

<!-- figure 1 on pdf page 15 at 334,259-607,442 pt | caption: none | text-layer labels: Description | nearby labels: Example: typical system | 1 | IP camera, powered via PoE . | 2 | RNS-8 network switch. | OCR text follows (tesseract, unverified; 2/4 words >= 60, mean confidence 58) -->
Raymarine
Raymarine
<!-- end of figure 1 -->

<!-- pdf page 16 | printed page 16 | header: Description -->

## Description

| 3 | Marine router (YachtSense Link shown). |
| --- | --- |
| 4 | Sonar module (RVM1600 shown). |
| 5 | Radar scanner (Quantum 2 shown). |
| 6 | Multifunction display / chartplotter (Axiom 2 Pro shown). |
| 7 | Remote keypad, powered via PoE (RMK-10 shown). |
| 8 | RayNet (female) to RayNet (female) network cable (not supplied). |
| 9 | RayNet (female) to RJ45 (male) network cable (not supplied). |
| 10 | RJ45 to RJ45 waterproof coupler. (part number 4115028, not supplied). |

- Note: For information on how to connect your products, refer to the
- following sections:
- p.26 — Cables and connections — General information
- p.32 — Network connections
- p.35 — Power connections For information on the available cables and accessories, refer to
- the following section: p.57 — Spares and accessories

### 3.4 Compatible network devices

The network switch is compatible with the following network devices:
- Any Raymarine products featuring RayNet connectors can be connected to the network switch via the use of a RayNet to RayNet network cable.
- Any Raymarine products featuring RJ45 (SeaTalk HS) connectors can be connected to the network switch via the use of a RayNet to RJ45 (SeaTalk HS) network adapter cable.
- Any Raymarine / non-Raymarine product featuring an RJ45 connector can be connected to the network switch via the use of a RayNet to RJ45 network adapter cable.

<!-- pdf page 17 | printed page 17 -->

## CHAPTER 4: PARTS SUPPLIED

##### CHAPTER CONTENTS

###### 4.1 Parts supplied (page 18)

###### 4.2 Inline fuse requirement (page 18)

Parts supplied                                  17

<!-- pdf page 18 | printed page 18 -->

### 4.1 Parts supplied

###### Description

| 1 | Network switch. |
| --- | --- |
| 2 | Documentation pack. |
| 3 | Fixing screws (M4, 8.94 x 25 mm). |
| 4 | Power cable, 1.5 m (4.9 ft.). |

### 4.2 Inline fuse requirement

If your product is NOT supplied with an inline fuse (whether separately or fitted to the power cable), you MUST fit a suitably-rated inline fuse to your product’s red power wire, housed in a waterproof fuse holder. The illustration below shows the two main types of inline fuse with waterproof holder, for use in marine electronics installations. Fuses in a variety of ratings are widely available at chandleries and marine electrical retailers. Select one of the following fuse types to protect your product:

1. Waterproof fuse holder containing a “glass”-type inline fuse.
2. Waterproof fuse holder containing a “blade”-type inline fuse. Fuse ratings:
- Voltage rating — must be equal to or greater than the voltage of your vessel’s power supply.
- Current rating — refer to the Inline fuse and thermal breaker rating section in this document.

<!-- figure 1 on pdf page 18 at 38,62-314,194 pt | caption: none | text-layer labels: none | nearby labels: 4.1 Parts supplied | List of parts supplied in the box. | Description | 1 | Network switch. | OCR below floor, text not used (5/11 words >= 60, mean confidence 44) -->

<!-- figure 2 on pdf page 18 at 334,151-607,290 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR: no legible text (0/1 words >= 60, mean confidence 0) -->

<!-- pdf page 19 | printed page 19 -->

## CHAPTER 5: PRODUCT DIMENSIONS

##### CHAPTER CONTENTS

###### 5.1 Product dimensions (page 20)

Product dimensions                         19

<!-- pdf page 20 | printed page 20 -->

### 5.1 Product dimensions

###### Description

| A | 287.63 mm (11.32 in). |
| --- | --- |
| B | 125.50 mm (4.94 in). |
| C | 78.00 mm (3.07 in). |
| D | 270.63 mm (10.65 in). |
| E | 8.50 mm (0.33 in). |
| F | 34.31 mm (1.35 in). |

<!-- figure 1 on pdf page 20 at 38,43-314,197 pt | caption: none | text-layer labels: Description | nearby labels: 5.1 Product dimensions | A | 287.63 mm (11.32 in). | B | 125.50 mm (4.94 in). | OCR below floor, text not used (1/5 words >= 60, mean confidence 53) -->

<!-- pdf page 21 | printed page 21 -->

## CHAPTER 6: LOCATION REQUIREMENTS

##### CHAPTER CONTENTS

###### 6.1 Warnings and cautions (page 22)

###### 6.2 General location requirements (page 22)

###### 6.3 Ignition Protection (page 22)

###### 6.4 EMC installation guidelines (page 22)

###### 6.5 Connections to other equipment (page 23)

###### 6.6 Compass safe distance (page 23)

Location requirements                                  21

<!-- pdf page 22 | printed page 22 -->

### 6.1 Warnings and cautions

- Important: Before proceeding, ensure that you have read and understood the warnings and cautions provided in the following section of
- this document:
- p.7 — Important information

### 6.2 General location requirements

When selecting a location for your product it is important to consider a number of factors. Factors for consideration: • Ventilation — To ensure adequate airflow: – Ensure that product is mounted in a compartment of suitable size. – Ensure that ventilation holes are not obstructed. Allow adequate separation of all equipment. Any specific requirements for each system component are provided later in this chapter. • Mounting surface — Ensure product is adequately supported on a secure surface. Do not mount units or cut holes in places which may damage the structure of the vessel. • Cabling — Ensure the product is mounted in a location which allows proper routing, support and connection of cables: – Minimum bend radius of 100 mm (3.94 in) unless otherwise stated. – Use cable clips to prevent stress on connectors. – If your installation requires multiple ferrites to be added to a cable then additional cable clips should be used to ensure the extra weight of the cable is supported. • Water ingress — The product is suitable for mounting both above and below decks. Although the unit is waterproof, it is good practice to locate it in a protected area away from prolonged and direct exposure to rain and salt spray. • Electrical interference — Select a location that is far enough away from devices that may cause interference, such as motors, generators and radio transmitters / receivers.

- Power supply — Select a location that is as close as possible to the vessel’s DC power source. This will help to keep cable runs to a minimum.

### 6.3 Ignition Protection

This product is certified to the EN ISO 8846:2017 Ignition Protection standard.

### 6.4 EMC installation guidelines

Raymarine equipment and accessories conform to the appropriate Electromagnetic Compatibility (EMC) regulations, to minimize electromagnetic interference between equipment and minimize the effect such interference could have on the performance of your system. Correct installation is required to ensure that EMC performance is not compromised.

Note: In areas of extreme EMC interference, some slight interference may be noticed on the product. Where this occurs the product and the source of the interference should be separated by a greater distance.

For optimum EMC performance we recommend that wherever possible: • Raymarine equipment and cables connected to it are: – At least 1 m (3.28 ft) from any equipment transmitting or cables carrying radio signals e.g. VHF radios, cables and antennas. In the case of SSB radios, the distance should be increased to 2 m (6.6 ft). – More than 2 m (6.56 ft) from the path of a radar beam. A radar beam can normally be assumed to spread 20 degrees above and below the radiating element. • The product is supplied from a separate battery from that used for engine start. This is important to prevent erratic behavior and data loss which can occur if the engine start does not have a separate battery. • Raymarine specified cables are used.

<!-- pdf page 23 | printed page 23 -->

- Cables are not cut or extended, unless doing so is detailed in the installation manual.

Note: Where constraints on the installation prevent any of the above recommendations, always ensure the maximum possible separation between different items of electrical equipment, to provide the best conditions for EMC performance throughout the installation.

### 6.5 Connections to other equipment

Requirement for ferrites on non-Raymarine cables: If your Raymarine equipment is to be connected to other equipment using a cable not supplied by Raymarine, a suppression ferrite MUST always be attached to the cable near the Raymarine unit. For more information, refer to your third-party cable manufacturer.

### 6.6 Compass safe distance

To prevent potential interference with the vessel's magnetic compasses, ensure an adequate distance is maintained from the product. When choosing a suitable location for the product, you must aim to maintain a distance of at least 1 m (3.3 ft.) in all directions from any compasses. For some smaller vessels it may not be possible to locate the product this far away from a compass. In this situation, when choosing the installation location for your product, ensure that the compass is not affected by the product when it is in a powered on state.

Location requirements                                                      23

<!-- pdf page 24 | printed page 24 -->

## CHAPTER 7: MOUNTING

##### CHAPTER CONTENTS

###### 7.1 Tools required for installation (page 25)

###### 7.2 Mounting the unit (page 25)

<!-- pdf page 25 | printed page 25 -->

### 7.1 Tools required for installation

Product installation requires the following tools:

1. Power drill.
2. Pozi drive screwdriver.
3. Drill bit.

Note: The appropriate drill bit size is dependent on the thickness and material of the mounting surface.

### 7.2 Mounting the unit

- Instructions for mounting the unit.
- Before mounting the product, ensure that you have:
- Selected a suitable location, based on the location requirements found in this document.
- Identified the relevant cable connections and the route that the cables will take.

Mounting

1. Prepare the mounting surface:
i. Fix the supplied mounting template to the chosen location, using masking or self-adhesive tape.
ii. Drill mounting holes as indicated on the template to accept the fixings.
iii. Remove the mounting template.
iv. Screw the fixings approximately half way into the holes in the mounting surface.
2. Place the unit over the fixing screws and push the unit downwards to engage the keyhole slots.
3. Fully tighten the screws.

25

<!-- figure 1 on pdf page 25 at 334,29-607,211 pt | caption: none | text-layer labels: none | OCR below floor, text not used (1/5 words >= 60, mean confidence 37) -->

<!-- figure 2 on pdf page 25 at 38,62-314,202 pt | caption: none | text-layer labels: none | nearby labels: 7.1 Tools required for installation | 1. | Power drill. | 2. Pozi drive screwdriver. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 26 | printed page 26 -->

## CHAPTER 8: CABLES AND CONNECTIONS — GENERAL INFORMATION

##### CHAPTER CONTENTS

###### 8.1 General cabling guidance (page 27)

###### 8.2 System overview (page 28)

###### 8.3 Multiple switches (page 29)

###### 8.4 Network cable connector types (page 30)

###### 8.5 SeaTalk HS (page 30)

###### 8.6 Connections overview (page 30)

<!-- pdf page 27 | printed page 27 -->

### 8.1 General cabling guidance

###### Cable types and length

It is important to use cables of the appropriate type and length.
- Unless otherwise stated only use cables supplied by Raymarine.
- Where it is necessary to use non-Raymarine cables, ensure that they are of correct quality and gauge for their intended purpose. (e.g.: longer power cable runs may require larger wire gauges to minimize voltage drop along the run).

###### Cable routing and bend radius

To maximize cable performance and lifespan, it’s important to ensure that all cables are routed correctly and adequate space is provided to allow for each cable’s minimum bend radius.

###### Minimum cable bend radius

Do NOT bend cables excessively. Wherever possible, ensure that your chosen product installation location allows enough clearance for the minimum cable bend diameter specified in the following table: Description                                Value

| Ø | Cable minimum bend diameter. | 200 mm (7.87 in.) |
| --- | --- | --- |
| R | Cable minimum bend radius. | 100 mm (3.94 in.) |

Note: For products where multiple different cable types are connected, each with a different minimum cable bend radius, the higher figure is provided in the table above (i.e. the cable with the greatest minimum bend radius is specified).

###### Cable routing — best practices

- Protect all cables from physical damage and exposure to heat. Use trunking or conduit where possible. Do NOT run cables through bilges or doorways, or close to moving or hot objects.
- Secure cables in place using cable clips or cable ties. Coil any excess cable and tie it out of the way.
- Where a cable passes through an exposed bulkhead or deckhead, use a suitable watertight feed-through (conduit).
- Do NOT run cables near to engines or fluorescent lights.
- Always route data cables as far away as possible from:
- Other equipment and cables.
- High current-carrying AC and DC power lines.
- Antennas.

###### Strain relief

Use adequate strain relief for cabling to ensure that connectors are protected from strain and will not pull out under extreme sea conditions.

###### Circuit isolation

Appropriate circuit isolation is required for installations using both AC and DC current: • Always use isolating transformers or a separate power-inverter to run PCs, processors, displays and other sensitive electronic instruments or devices. • If using Weather FAX audio cables, always use an isolating transformer. • If using a third-party audio amplifier, always use an isolated power supply. • If using an RS232/NMEA converter, always ensure optical isolation on the signal lines.

<!-- figure 1 on pdf page 27 at 38,221-314,355 pt | caption: none | text-layer labels: none | nearby labels: Minimum cable bend radius | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 28 | printed page 28 -->

- Always ensure that PCs or other sensitive electronic devices have a dedicated power circuit.

###### Cable shielding

Ensure that cable shielding is not damaged during installation and that all cables are properly shielded.

Important: Be aware that some third-party cables and adaptors (for example, certain Ethernet cables using RJ45 connectors) are not always shielded. To prevent breaks in cable shielding continuity and potential grounding issues, special attention is required to ensure that any cables, extension cables, adaptors, or other signal-coupling devices (such as multi-way connectors, junction boxes, terminal blocks etc.) used in cable runs maintain all shield connections throughout the cable run.

###### Suppression ferrites

- Raymarine cables may be pre-fitted or supplied with suppression ferrites. These are important for correct EMC performance. If ferrites are supplied separately to the cables (i.e. not pre-fitted), you must fit the supplied ferrites, using the supplied instructions.
- If a ferrite has to be removed for any purpose (e.g. installation or maintenance), it must be replaced in the original position before the product is used.
- Use only ferrites of the correct type, supplied by Raymarine or its authorized dealers.
- Where an installation requires multiple ferrites to be added to a cable, additional cable clips should be used to prevent stress on the connectors due to the extra weight of the cable.

###### Warning: Positive ground systems

Do NOT connect this unit to a system which has positive grounding.

###### Connecting cables

Follow the steps below to connect the cable(s) to your product.
1. Ensure that the vessel's power supply is switched off.

2. Ensure that the device being connected has been installed in accordance with the installation instructions supplied with that device.
3. Ensuring correct orientation, push cable connectors fully onto the corresponding connectors.
4. Engage any locking mechanism to ensure a secure connection (e.g.: turn locking collars clockwise until tight, or in the locked position).
5. Ensure any bare ended wire connections are suitably insulated to prevent shorting and corrosion due to water ingress.

### 8.2 System overview

The following example provides an overview of a typical system, including the available connections and the types of devices that can be connected to your network switch.

Note: The following system is shown as an example only, and may differ from your planned installation.

###### Example: typical system

<!-- figure 1 on pdf page 28 at 334,278-607,442 pt | caption: none | text-layer labels: none | nearby labels: Example: typical system | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 97) -->
Raymarine
Raymarine
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 28 at 41,374-86,425 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 29 | printed page 29 | header: Description -->

| 1 | IP camera, powered via PoE. |
| --- | --- |
| 2 | RNS-8 network switch. |
| 3 | Marine router (YachtSense Link shown). |
| 4 | Sonar module (RVM1600 shown). |
| 5 | Radar scanner (Quantum 2 shown). |
| 6 | Multifunction display / chartplotter (Axiom 2 Pro shown). |
| 7 | Remote keypad, powered via PoE (RMK-10 shown). |
| 8 | RayNet (female) to RayNet (female) network cable (not supplied). |
| 9 | RayNet (female) to RJ45 (male) network cable (not supplied). |
| 10    RJ45 to RJ45 waterproof coupler. (part number 4115028, | not supplied). |

- Note: For information on how to connect your products, refer to the
- following sections:
- p.26 — Cables and connections — General information
- p.32 — Network connections
- p.35 — Power connections For information on the available cables and accessories, refer to
- the following section: p.57 — Spares and accessories

### 8.3 Multiple switches

Systems with more than 8 devices will require more than one network switch. Network switches can be connected together (daisy-chained) for this purpose. The network switch can be connected (daisy-chained) to another network switch via any of the connection ports.

###### Example: daisy-chain connection scenario

Note: If daisy-chaining 4 or more network switches together within a system, it is recommended that one network switch is used as a central connection point. This will ensure that any effects resulting from connection issues (such as faulty cabling or slow connection speeds) are minimized within your system.

Note: It is recommended that a maximum of 8 network switches are daisy-chained together at one time.

###### Description

| 1 | RNS-8 network switch. |
| --- | --- |
| 2 | Mobile router (YachtSense Link shown). |
| 3 | RayNet (male) to RayNet (male) adapter cable (A80162) (100 mm (3.94 in)). Suitable for joining (female) RayNet cables together for longer cable runs. |

For further information on additional cabling options, refer to: p.57 — Spares and accessories

<!-- figure 1 on pdf page 29 at 334,29-607,228 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 52) -->
Raymarine
DPR
DPR
<!-- end of figure 1 -->

<!-- pdf page 30 | printed page 30 -->

### 8.4 Network cable connector types

In Raymarine systems, Ethernet network cable connectors may be one of three different types — RayNet, RJ45, or RJ45 (SeaTalk HS). Connector         Description

RayNet. This connector type is waterproof.

RJ45. This connector type is NOT waterproof.

Waterproof RJ45 (SeaTalk HS) for connection to (legacy) Raymarine equipment featuring a lockable RJ45 (SeaTalk HS) connector. Alternatively, these cables may be coupled with suitable adapter cables for waterproof connections to equipment featuring a RayNet connector.

### 8.5 SeaTalk HS

SeaTalk HS is a high speed Ethernet-based marine network which allows compatible equipment (such as devices with an RJ45, RayNet, or RJ45 SeaTalk HS connector) to communicate rapidly and share large amounts of data. Information shared via the SeaTalk HS network includes, but is not limited to: • Shared cartography (between compatible displays). • Digital radar data. • Sonar data.

###### RayNet

Electrically, RayNet is identical to SeaTalk HS, and the two share the same underlying Ethernet protocol.

###### Connector types

- SeaTalk HS connections can be made using one of three different
- connector types:

- RJ45
- Waterproof RJ45 SeaTalk HS
- Waterproof RayNet All SeaTalk HS connector types are interchangeable, in terms of compatibility with devices featuring an RJ45 SeaTalk HS, RayNet, or RJ45 connector. However, the main difference between them is that RJ45 SeaTalk HS connectors are generally not waterproof, unless you select Raymarine cables which use the specific waterproof variant RJ45 connectors. However, all connections featuring RayNet connectors are waterproof. The different SeaTalk HS connector types are shown below: Connector        Description

RayNet. This connector type is waterproof.

Waterproof RJ45 SeaTalk HS for connection to (legacy) Raymarine equipment featuring a lockable RJ45 SeaTalk HS connector. Alternatively, these cables may be coupled with suitable adapter cables for waterproof connections to equipment featuring a RayNet connector. RJ45. This connector type is NOT waterproof.

Where required, adapter cables are available to connect RayNet devices to devices featuring an RJ45 or RJ45 SeaTalk HS connector.

### 8.6 Connections overview

The RNS-8 network switch includes the following connections:

Note: The network switch is supplied with protective caps fitted to the network connection ports. The protective caps should remain in place until connections are made. If a connection is not required then the protective cap should not be removed.

<!-- pdf page 31 | printed page 31 -->

1. 3-pin power connection port.
2. 4x PoE (Classes 0 to 4), (30 W maximum per port) RayNet network connection ports (10 / 100 / 1000 Mbits/s). PoE ports 1, 3, 5 and 7 (from left to right) can be easily identified via their red locking nuts.
3. Non-PoE RayNet network connection port (10 / 100 / 1000 Mbits/s). Non-PoE ports 2, 4, 6 and 8 (from left to right) can be easily identified via their black locking nuts.
4. Protective cap.

- Note: You can mix a combination of PoE and non-PoE devices simultaneously, for a total of 8 devices (maximum PoE devices = 4; maximum non-PoE devices = 8). For further network or power connection information, refer to the
- following sections:
- p.32 — Network connections
- p.35 — Power connections

Note: When attempting to view your network switch’s port diagnostic information, it is vital to know the associated port number for each port. For further port identification information, refer to the following section: p.47 — RNS-8 Port identification

<!-- figure 1 on pdf page 31 at 38,29-314,163 pt | caption: none | text-layer labels: none | nearby labels: 1. | 3-pin power connection port. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 32 | printed page 32 -->

## CHAPTER 9: NETWORK CONNECTIONS

##### CHAPTER CONTENTS

###### 9.1 Equipment connections (page 33)

###### 9.2 PoE network connections (page 33)

###### 9.3 Non-PoE network connections (page 33)

###### 9.4 Network cable extensions (page 34)

<!-- pdf page 33 | printed page 33 | header: Description -->

### 9.1 Equipment connections

Equipment is connected to the network switch using either a RayNet cable, a RayNet to RJ45 adapter cable, or a RayNet to RJ45 (SeaTalk HS) adapter cable. The following section provides 2 different scenarios that may be applicable when connecting your equipment to the RNS-8 Network Switch:

| 1. | p.33 — PoE network connections |
| --- | --- |
| 2. | p.33 — Non-PoE network connections |

### 9.2 PoE network connections

- Connecting the RNS-8 network switch to Raymarine equipment via a PoE RayNet connector.
- Required cabling / connectors:
- RayNet (female) to RayNet (female) cable (not supplied).
- OR:
- RayNet (female) to RJ45 (male) network cable (not supplied).
- RJ45 to RJ45 waterproof coupler. (not supplied). For further information on the cabling required, refer to the following
- section: p.57 — Spares and accessories
- Example: PoE network connection scenario

###### Description

| 1 | RNS-8 network switch. |
| --- | --- |
| 2 | Remote keypad (supplied power via PoE). |
| 3 | IP camera (supplied power via PoE). |

Network connections

| 4 | RayNet (female) to RayNet (female) network cable (not supplied). |
| --- | --- |
| 5 | RayNet (female) to RJ45 (male) network cable (not supplied). |
| 6 | RJ45 to RJ45 waterproof coupler. (not supplied). |
| 7 | IP camera RJ45 (male) cable. |
| 8 | IP camera power cable (if powering the camera via PoE, do NOT connect this to a 12 V / 24 V dc feed). |

### 9.3 Non-PoE network connections

- Connecting the RNS-8 network switch to Raymarine equipment (e.g. legacy MFDs / chartplotters) via a non-PoE RayNet connector.
- Required cabling / connectors:
- RayNet (female) to RayNet (female) network cable (not supplied).
- OR:
- RayNet (female) to RJ45 (SeaTalk HS) (male) adapter cable (not supplied). For further information on the cabling required, refer to the following
- section: p.61 — RayNet to RJ45 adapter cables
- Example: RJ45 (SeaTalk HS) cable connection scenario

33

<!-- figure 1 on pdf page 33 at 38,312-314,425 pt | caption: none | text-layer labels: Description | nearby labels: Example: PoE network connection scenario | 1 | RNS-8 network switch. | 2 | Remote keypad (supplied power via PoE ). | OCR: no legible text (0/2 words >= 60, mean confidence 38) -->

<!-- figure 2 on pdf page 33 at 334,317-607,458 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 91) -->
Raymarine
J
<!-- end of figure 2 -->

<!-- pdf page 34 | printed page 34 | header: Description -->

| 1 | RNS-8 network switch. |
| --- | --- |
| 2 | RayNet equipment featuring a RayNet connector, such as Axiom series multifunction displays. |
| 3 | Legacy SeaTalk HS multifunction display featuring an RJ45 (SeaTalk HS) connector. |
| 4 | RayNet (female) to RayNet (female) network cable (not supplied). |
| 5 | RayNet (female) to RJ45 (SeaTalk HS) waterproof plug (male) adapter cable (not supplied). |

### 9.4 Network cable extensions

If you wish to extend the length of a network cable connected to your product, refer to the following section for further information: p.57 — Spares and accessories

<!-- pdf page 35 | printed page 35 -->

## CHAPTER 10: POWER CONNECTIONS

##### CHAPTER CONTENTS

###### 10.1 Power over Ethernet (PoE) (page 36)

###### 10.2 Power connection (page 37)

- 10.3 Ensure sufﬁcient nominal voltage (page 38)

###### 10.4 Inline fuse and thermal breaker ratings (page 38)

###### 10.5 Power distribution (page 38)

###### 10.6 Power cable extension (12 / 24 V systems) (page 40)

###### 10.7 Power cable drain wire connection (page 41)

<!-- pdf page 36 | printed page 36 -->

### 10.1 Power over Ethernet (PoE)

Power over Ethernet (PoE) is a system which allows both power and data to be passed along a single CAT 6 Ethernet cable. There are 2 main types of PoE device: • Power Sourcing Equipment (PSE) — this PoE system component provides electrical power over a CAT 6 Ethernet cable. • Powered Device (PD) — this PoE system component is powered by the electrical power provided by the Power Sourcing Equipment (PSE). The RNS-8 Network Switch is a PSE (Power Sourcing Equipment) device, which can supply both data and power to a maximum of 4x connected Powered Devices (PD). Each Powered Device (PD) can be PoE Class 0 to 4, and each may draw a maximum of 30 W power (i.e. a maximum total power consumption of 120 W for all 4 devices combined). When a Powered Device (PD) is connected to one of the Network Switch’s PoE RayNet network ports, it is first checked to establish whether it is PoE-compatible, and if so, what class of device it is. If a connected Powered Device (PD) requires more power than the individual port’s maximum power output (30 W), then it will not be powered. Before connecting a Powered Device (PD) to the network switch, ensure that the maximum power output of the port to which it is connected PoE (i.e. 30 W) will not be surpassed. The following table lists the different classes of device, and their typical power draw:

| PoE Class             Maximum power provided | Typical power |
| --- | --- |
| by Power Sourcing | required by |
| Equipment (PSE) | Powered Device (PD)(1) |

| Class 1 (Very low | 4W | ~3.84 W |
| --- | --- | --- |
| power draw) |  |  |
| Class 2 (Low | 7W | ~6.49 W |
| power draw) |  |  |
| Class 3 (Medium | 15.4 W | ~12.95 W |
| power draw) |  |  |
| PoE Class | Maximum power provided by Power Sourcing Equipment (PSE) | Typical power required by Powered Device (PD)(1) |

| Class 4 (High | 30 W | ~25.5 W |
| --- | --- | --- |
| power draw) |  |  |
| Class 0 | 15.4 W | ~12.95 W |

(Classification unimplemented)

Note:
- (1) The power consumption figures provided in the third column in the table above are approximate figures only. The actual power consumption figures may differ, depending on the device.
- For more information on PoE requirements, refer to: p.55 — Power specification

###### Warning: Powering PoE devices

PoE devices can often be powered via an Ethernet connection (PoE) OR via a dedicated power cable.

NEVER connect a PoE device’s dedicated power cable when it is being supplied PoE, unless the device is specifically designed to be connected to multiple power sources, as confirmed by the device’s instruction documents.

When the PoE device’s dedicated power cable is not connected, any bare-end wire connections must be separately covered with insulation.

<!-- pdf page 37 | printed page 37 -->

###### Warning: Do NOT exceed maximum power output

When connected to a Power Sourcing Equipment (PSE) such as a PoE network switch or PoE Injector, different classes of PoE-consuming devices (“Powered Device”, PD) require different amounts of electrical current.

Do NOT connect a PoE-consuming device which exceeds the maximum power (in Watts ) that can be provided by the device supplying PoE (“Power Sourcing Equipment”, PSE).

For the maximum power output (in Watts ) provided by the PSE, refer to the device’s Technical Specification.

###### Warning: Ensure sufficient nominal voltage

- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) is itself sufficiently powered, with a stable supply of at least 10.8 V dc.
- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) provides a nominal supply voltage to the PD device in the range of 44 V to 57 V dc.

###### Power over Ethernet (PoE) power output

PoE devices can be powered via one of the RNS-8’s PoE ports, located on the bottom connector row on the rear of the unit. PoE ports can be easily identified via their red locking nuts. In the example below, the power requirements of each of the 3 PoE devices do not exceed the 30 W maximum power provided by each PoE port. All 3 devices can therefore be powered by the network switch, via PoE.

###### Example PoE connections

Note:
- The PoE devices should be connected using RayNet to RayNet cables or RayNet to RJ45 cables. For more information on the cabling required, refer to the documentation supplied with your PoE device.
- Any suppression ferrites supplied with the powered device must be used on the network cable connecting the powered device to the network switch.
- In order to sufficiently power PoE devices, the network switch’s power supply must exceed 10.8 V dc.

### 10.2 Power connection

The power for the network switch is provided directly by a 12 V or 24 V dc power source. The network switch is supplied with a power cable with bare stripped wires, suitable for direct connection to a 12 V or 24 V dc power supply:

<!-- figure 1 on pdf page 37 at 41,29-86,197 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 37 at 334,46-607,247 pt | caption: none | text-layer labels: none | nearby labels: Example PoE connections | Note: | OCR text follows (tesseract, unverified; 23/28 words >= 60, mean confidence 77) -->
4x 30 W
PoE class 1
(4 W)
PoE class 2
(7 W)
PoE class 1
PoE class 1
(4 W)
(4 W)
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 37 at 41,202-86,338 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 38 | printed page 38 -->

###### Description

| 1 | RNS-8 Network Switch. |
| --- | --- |
| 2 | Power cable (supplied), 1.5 m (4.9 ft.). |
| 3 | Red wire (positive) — connects to the power supply’s positive terminal. |
| 4 | Waterproof fuse holder containing a suitably-rated inline fuse (not supplied), which must be fitted to the red positive wire — for fuse ratings, refer to: p.38 — Inline fuse and thermal breaker ratings |
| 5 | Gray wire (drain) — connects to the vessel’s RF ground (if available), or the negative battery terminal. |
| 6 | Black wire (negative) — connects to the power supply’s negative terminal. |

10.3 Ensure sufﬁcient nominal voltage
- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) is itself sufficiently powered, with a stable supply of at least 10.8 V dc.
- Ensure that any device supplying PoE (i.e. Power Sourcing Equipment (PSE)) to a consuming device (“Powered Device”, PD) provides a nominal supply voltage to the PD device in the range of 44 V to 57 V dc.

### 10.4 Inline fuse and thermal breaker ratings

The following inline fuse and thermal breaker ratings apply to your product: Inline fuse rating                   Thermal breaker rating

| • 12 V: 15A | • 12 V: 20A |
| --- | --- |
| • 24 V: 8A | • 24 V: 10A |

Note: The suitable fuse rating for the thermal breaker is dependent on the number of devices you are connecting. If in doubt, consult an authorized Raymarine dealer.

### 10.5 Power distribution

Recommendations and best practice for the power connection of products supplied with a drain wire as part of the supplied power cable. • The product is supplied with a power cable, either as a separate item or a captive cable permanently attached to the product. Only use the power cable supplied with the product. Do NOT use a power cable designed for, or supplied with, a different product. • Refer to the Power connection section for more information on how to identify the wires in your product’s power cable, and where to connect them. • See below for more information on implementation for some common power distribution scenarios:

<!-- figure 1 on pdf page 38 at 38,29-314,230 pt | caption: none | text-layer labels: Description | nearby labels: 1 | RNS-8 Network Switch. | 2 | OCR text follows (tesseract, unverified; 5/12 words >= 60, mean confidence 60) -->
4
6
23
2?
*6
<!-- end of figure 1 -->

<!-- pdf page 39 | printed page 39 -->

Important:
- When planning and wiring, take into consideration other products in your system, some of which (e.g. sonar modules) may place large power demand peaks on the vessel’s electrical system, which may impact the voltage available to other products during the peaks.
- The information provided below is for guidance only, to help protect your product. It covers common vessel power arrangements, but does NOT cover every scenario. If you are unsure how to provide the correct level of protection, please consult an authorized dealer or a suitably qualified professional marine electrician.

###### Implementation — connection to distribution panel (Recommended)

###### Description

| 1 | Waterproof fuse holder containing a suitably-rated inline fuse must be fitted. For suitable fuse rating, refer to: Inline fuse and thermal breaker ratings. |
| --- | --- |
| 2 | Product power cable. |
| 3 | Drain wire connection point. |

- It is recommended that the supplied power cable is connected to a suitable breaker or switch on the vessel's distribution panel or factory-fitted power distribution point.
- The distribution point should be fed from the vessel’s primary power source by 8 AWG (8.36 mm2) cable.
- Ideally, all equipment should be wired to individual suitably-rated thermal breakers or fuses, with appropriate circuit protection.

Where this is not possible and more than 1 item of equipment shares a breaker, use individual inline fuses for each power circuit to provide the necessary protection. • The power cable supplied with your product includes a drain wire, which must be connected to the vessel’s common RF ground.

| 1 | Positive (+) bar |
| --- | --- |
| 2 | Negative (-) bar |
| 3 | Circuit breaker |
| 4 | Waterproof fuse holder containing a suitably-rated inline fuse must be fitted. For suitable fuse rating, refer to: Inline fuse and thermal breaker ratings. |

Important: Observe the recommended fuse / breaker ratings provided in the product’s documentation, however be aware that the suitable fuse / breaker rating is dependent on the number of devices being connected.

<!-- figure 1 on pdf page 39 at 334,94-607,283 pt | caption: none | text-layer labels: Description | nearby labels: 1 | Positive (+) bar | 2 | Negative (-) bar | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 66) -->
2?
4?
4
AN
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 39 at 38,206-314,314 pt | caption: none | text-layer labels: Description | nearby labels: 1 | 1 | 2 | 3 | 4 | OCR below floor, text not used (2/12 words >= 60, mean confidence 33) -->

<!-- pdf page 40 | printed page 40 -->

###### Implementation — direct connection to battery

- Where connection to a power distribution panel is not possible, the power cable supplied with your product may be connected directly to the vessel's battery, via a suitably rated fuse or breaker.
- If the power cable is NOT supplied with a fitted inline fuse, you MUST fit a suitably rated fuse or breaker between the red wire and the battery’s positive terminal.
- Refer to the inline fuse ratings provided in the product’s documentation.
- If you need to extend the length of the power cable supplied with your product, ensure you observe the dedicated Power cable extensions advice provided in the product’s documentation.

###### Description

| 1 | Waterproof fuse holder containing a suitably-rated inline fuse must be fitted. For suitable fuse rating, refer to: Inline fuse and thermal breaker ratings. |
| --- | --- |
| 2 | Product power cable. |
| 3 | Drain wire connection point. |

Battery connection scenario A: Suitable for a vessel with a common RF ground point. In this scenario, the power cable’s drain wire should be connected to the vessel’s common ground point. Battery connection scenario B:

Suitable for a vessel without a common grounding point. In this case, the power cable’s drain wire should be connected directly to the battery’s negative terminal.

###### Grounding

Ensure that you observe any additional grounding advice provided in the product’s documentation.

###### More information

- It is recommended that best practice is observed in all vessel electrical installations, as detailed in the following standards:
- BMEA Code of Practice for Electrical and Electronic Installations in Boats
- NMEA 0400 Installation Standard
- ISO 13297: Small craft — Electrical systems — Alternating and direct current installations
- ISO 10133: Small craft — Electrical systems — Extra-low-voltage d.c. installations
- ABYC E-11 AC & DC Electrical Systems on Boats
- ABYC A-31 Battery chargers and Inverters
- ABYC TE-4 Lightning Protection

### 10.6 Power cable extension (12 / 24 V systems)

If you need to extend the length of the power cable supplied with your product, ensure you observe the following advice: • The power cable for each unit in your system should be run as a separate, single length of 2-wire cable from the unit to the vessel's battery or distribution panel. • Ensure that the extension cable is of a sufficient gauge for the supply voltage, the total current load of the device, and the length of the cable run — as the cable run length increases, the greater the voltage drop will be from one end of the power cable to the other. • Refer to the following table for typical minimum power cable wire gauges:

<!-- figure 1 on pdf page 40 at 38,43-314,204 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 55) -->

<!-- pdf page 41 | printed page 41 -->

| Cable length in | Wire gauge in AWG | Wire gauge in AWG |
| --- | --- | --- |
| meters (feet) | (mm2) for 12 V supply | (mm2) for 24 V supply |
| <8 (<25) | 16 (1.31 mm2) | 18 (0.82 mm2) |
| 16 (50) | 14 (2.08 mm2) | 16 (1.31 mm2) |
| 24 (75) | 12 (3.31 mm2) | 14 (2.08 mm2) |
| >32 (>100) | 10 (5.26 mm2) | 12 (3.31 mm2) |

Important: Be aware that some products in your system (such as sonar modules) can create voltage peaks at certain times, which may impact the voltage available to other products during the peaks.

Important: To ensure power cables (including any extension) are of a sufficient gauge, ensure that there is a continuous minimum voltage of 10.8 V dc at the end of the cable where it enters the product’s power connector, even with a fully flat battery at 11 V dc. (Do not assume that a flat battery is at 0 V dc. Due to the discharge profile and internal chemistry of batteries, the current drops much faster than the voltage. A “fully flat” battery still shows a positive voltage, even if it doesn’t have enough current to power your device.)

### 10.7 Power cable drain wire connection

The power cable supplied with this product includes a dedicated drain wire for connection to a vessel's Radio Frequency (RF) ground point (if available), or the negative battery terminal. The purpose of the drain wire is to drain excess voltage from the cable shield, giving it a path to safety. The drain wire protects the cable's inner signal conductors from electrical noise emitted by other cables and devices. Although the drain wire is not intended to ground the product's internal circuits, it's important that the drain wire is connected to the vessel’s common RF ground point, which should be used for

all equipment in your system. If several items require grounding, the drain wires and dedicated ground connections (if available) of all equipment should first be connected to a single local point (e.g. within a distribution panel), and then this point connected via an appropriately-rated conductor to the vessel's RF common ground point. An RF ground point is typically a circuit with a very low-impedance signal at Radio Frequency, connected to the sea via an electrode immersed in the sea, or bonded to the inner side of the hull in an area that is underwater. On vessels without an RF ground system, the drain wires and dedicated ground connections (if available) of all equipment should be connected directly to the vessel’s negative battery terminal. The dc power system should be either: • Negative grounded (“bonded”), with the negative battery terminal connected to the vessel's RF ground. • Floating, with neither battery terminal connected to the vessel's ground. The preferred minimum requirement for the path to ground (bonded or non-bonded) is via a flat tinned copper braid, with a 30 A rating or greater. If this is not possible, an equivalent stranded wire conductor may be used, rated as follows: • for runs of <1 m (3.3 ft), use 6 mm2 (10 AWG) or greater. • for runs of >1 m (3.3 ft), use 8 mm2 (8 AWG) or greater. In any grounding system, always keep the length of connecting braid or wires as short as possible.

<!-- pdf page 42 | printed page 42 -->

## CHAPTER 11: TROUBLESHOOTING

##### CHAPTER CONTENTS

###### 11.1 Troubleshooting (page 43)

###### 11.2 Power up troubleshooting (page 43)

###### 11.3 LED diagnostic guidance (page 43)

###### 11.4 LED diagnostics (page 44)

###### 11.5 Diagnostic product information (page 46)

<!-- pdf page 43 | printed page 43 -->

### 11.1 Troubleshooting

The troubleshooting section provides possible causes and the corrective action required for common problems that are associated with the installation and operation of your product. Before packing and shipping, all products are subjected to comprehensive testing and quality assurance programs. If you do experience problems with your product, this section will help you to diagnose and correct problems to restore normal operation. If after referring to this section you are still having problems with your product, please refer to the Technical support and servicing section of this manual for useful links and contact details.

### 11.2 Power up troubleshooting

Before troubleshooting problems with your power connection, ensure that you have followed the power connection guidance provided in the product’s installation instructions and performed a power cycle/reboot of the device. The troubleshooting information below can be used if you are experiencing problems with powering up your product.

###### Blown fuse / tripped breaker

1. Check the fuse, located inline with the power cable. Ensure that it has the correct rating (refer to Connections chapter), as an under-rated fuse can affect the power supplied to the product. If the fuse has blown, replace with a new fuse.
2. Check the condition of relevant / additional fuses and breakers and connections; replace if necessary.
3. If fuse keeps blowing, check for cable damage, broken connector pins or incorrect wiring.

###### Poor / damaged / insecure power supply cable / connections

1. Check that the power cable connector is fully inserted into the unit and locked in position.
2. Check the power supply cable and connectors for signs of damage or corrosion, replace if necessary.
3. With the unit turned on, try flexing the power cable near to the connector to see if this causes the unit to re-boot/lose power; replace if necessary.

4. Check the vessel’s battery voltage, the condition of the battery terminals and power supply cables, ensuring connections are secure, clean and free from corrosion; replace if necessary.

###### Incorrect power connection

The power supply may be wired incorrectly, ensure the installation instructions have been followed.

Power source insufﬁcient Check that your power supply (battery or distribution panel) is providing a minimum of 10.8 V to each component in the system.

### 11.3 LED diagnostic guidance

Your product has diagnostic LEDs which can be used to identify the unit’s status and to help troubleshoot any potential issues that may occur. The following section provides two basic examples of how to interpret the LED diagnostic patterns included in this publication. Example solid LED diagnostic pattern:

1. LED ON — Indicates the color assigned to the unit’s diagnostic LED, and confirms that the diagnostic LED is active (switched on).
2. LED OFF — Indicates that the unit’s diagnostic LED is inactive (switched off).
3. Diagnostic pattern — Indicates a diagnostic pattern based on the number and duration of peaks (indicating LED is switched on) and troughs (indicating LED is switched off) generated within the duration of the diagnostic pattern. In the example shown above, a continuous peak occurs, indicating that the LED is permanently on.

<!-- figure 1 on pdf page 43 at 334,254-607,362 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR below floor, text not used (1/2 words >= 60, mean confidence 40) -->

<!-- pdf page 44 | printed page 44 -->

1. LED ON — Indicates the color assigned to the unit’s diagnostic LED, and confirms that the diagnostic LED is active (switched on).
2. LED OFF — Indicates that the unit’s diagnostic LED is inactive (switched off).
3. Diagnostic pattern — Indicates a diagnostic pattern based on the number and duration of peaks (indicating LED is switched on) and troughs (indicating LED is switched off) generated within the duration of the diagnostic pattern. In the example shown above, a peak followed by a trough occurs and then repeats again, indicating that the LED flashes twice within a period of one second.
4. Diagnostic pattern duration — Indicates the total duration of the diagnostic pattern.
5. Diagnostic pattern flash total — Indicates the total number of flashes that occur within the diagnostic pattern.

### 11.4 LED diagnostics

Your network switch has diagnostic LEDs on the front of the unit. These LEDs are used to identify the unit’s status.

###### Power Port LED:

LED Indication             LED status and action required

(Green) Powered up / Ok Normal operation — no user action is required. (Amber) Low power and operational (Voltage supplied: 9 V – 10.8 V) PoE functionality is disabled when the Voltage supplied is between 9 V – 10.8 V. 1.   Check the cable connection for the port. 2. For PoE operation, ensure that the RNS-8’s power supply is providing a minimum of 10.8 V. (Red) Low power and non-operational (Voltage supplied: < 9 V) 1.   Check the cable connection for the port. 2. Ensure that more than 10.8 V is supplied to your product. (Red) High power and non-operational (Voltage supplied: > 32 V) Ensure that less than 32 V is supplied to the RNS-8.

<!-- figure 1 on pdf page 44 at 38,43-314,170 pt | caption: none | text-layer labels: none | nearby labels: Example flashing LED diagnostic pattern: | 1. | OCR: no legible text (0/5 words >= 60, mean confidence 29) -->

<!-- figure 2 on pdf page 44 at 338,276-439,317 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 72) -->
1s
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 44 at 338,353-439,394 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 96) -->
1s
x4
<!-- end of figure 3 -->

<!-- pdf page 45 | printed page 45 -->

LED Indication         LED status and action required

(Red) Internal fault Consider contacting your local dealer or Raymarine Product Support. For Raymarine contact details, refer to the following section: p.52 — Raymarine product support and servicing (No color) No power Refer to the advice found within the following section: p.43 — Power up troubleshooting

###### RayNet (SeaTalk HS) Port LEDs (2 / 4 / 6 / 8):

LED Indication         LED status and action required

(Green) 1,000 Mbits/s Ethernet Active (no transfer) Normal operation — no user action is required. (Green) 1,000 Mbits/s Ethernet Active (transferring) Normal operation — no user action is required.

(Amber) 10 / 100 Mbits/s Ethernet Active (no transfer) Normal operation — no user action is required.

LED Indication         LED status and action required

(Amber) 10 / 100 Mbits/s Ethernet Active (transferring) Normal operation — no user action is required.

(No color) No network activity detected
1. Check the cable connection for the port.
2. Check any additional connections.
3. Check that the unit connected to the switch is powered on.
4. Check that the unit connected to the switch is currently transferring data. This can be confirmed by performing an action on the multifunction display / chartplotter that initiates data transfer for the relevant unit — for example, if you suspect a problem with the port corresponding to a connected radar scanner, range in or out in the radar application to initiate data activity.

RayNet (SeaTalk HS) PoE Port LEDs (1 / 3 / 5 / 7) — with a

###### non-PoE device connected:

LED Indication         LED status and action required

(No color) 10 / 100 / 1000 Mbits/s Ethernet Active (transferring) Normal operation — no user action is required.

<!-- figure 1 on pdf page 45 at 46,55-146,96 pt | caption: none | text-layer labels: none | nearby labels: LED Indication | OCR text follows (tesseract, unverified; 3/3 words >= 60, mean confidence 85) -->
3s
O
x1
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 45 at 341,55-439,96 pt | caption: none | text-layer labels: none | nearby labels: LED Indication | 1. | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 80) -->
1s
C)
x4
<!-- end of figure 2 -->

<!-- pdf page 46 | printed page 46 -->

###### RayNet SeaTalk HS) PoE Port (1 / 3 / 5 / 7) LEDs — with a PoE device connected:

LED Indication        LED status and action required

(No color) Not providing power
1. Ensure that the Ethernet cable is connected correctly and that connections are secure.
2. Ensure you are not using a crossover coupler or cable as they are not appropriate for PoE applications.
3. Ensure that the network switch has sufficient remaining power allocation to power the connected device. For further information on the network switch’s total power allocation, refer to the following section: p.55 — Power specification (Green) Supplying power Normal operation — no user action is required.

LED Indication              LED status and action required

(Amber) Connected device requires more than 30 W If a connected PoE device requires more power than the PoE port’s maximum power output, then it will not be powered. 1.   Attempt to reduce the connected PoE device’s total power consumption. 2. Re-configure the network so that your PoE device is powered via a dedicated power supply and plugged into a non-PoE Ethernet connection. (Red) Internal fault Consider contacting your local dealer or Raymarine Product Support. For Raymarine contact details, refer to the following section: p.52 — Raymarine product support and servicing

### 11.5 Diagnostic product information

Diagnostic product information can be viewed and exported from a Raymarine LightHouse multifunction display, for supported products networked using RayNet (Ethernet), RJ45, RJ45 (SeaTalk HS) or SeaTalk NG / NMEA 2000 cables. Diagnostic product information includes technical data related to the connected product, such as serial numbers, network addresses, firmware version numbers, and so on. It is useful for 2 main purposes: 1.   Sending detailed product information to the Raymarine product support team, in the event of a problem or fault with your product. The information can be exported to a MicroSD card, and you can then copy the file for the purposes of emailing it to the product support team. For contact details, refer to: p.51 — Technical support 2. Maintaining detailed off-boat records. This is particularly useful for vessels that have multiple Raymarine products installed.

<!-- figure 1 on pdf page 46 at 341,55-439,96 pt | caption: none | text-layer labels: none | nearby labels: LED Indication | 1. | OCR text follows (tesseract, unverified; 2/3 words >= 60, mean confidence 71) -->
1s
x4
<!-- end of figure 1 -->

<!-- pdf page 47 | printed page 47 -->

To view or export diagnostic product information, access the [Diagnostics] menu. For instructions on how to access this menu, refer to the relevant Operation Instructions for your multifunction display.

RNS-8 port identiﬁcation Before attempting to view your network switch’s port diagnostic information, it is vital to know the associated port number for each port.

1. Port 1 — PoE (Classes 0 to 4), (30 W maximum) RayNet Ethernet network connection port (10 / 100 / 1000 Mbits/s).
2. Port 2 — Non-PoE RayNet network connection port (10/100/1000 Mbits/s)
3. Port 3 — PoE (Classes 0 to 4), (30 W maximum) RayNet Ethernet network connection port (10 / 100 / 1000 Mbits/s).
4. Port 4 — Non-PoE RayNet network connection port (10/100/1000 Mbits/s)
5. Port 5 — PoE (Classes 0 to 4), (30 W maximum) RayNet Ethernet network connection port (10 / 100 / 1000 Mbits/s).
6. Port 6 — Non-PoE RayNet network connection port (10/100/1000 Mbits/s)
7. Port 7 — PoE (Classes 0 to 4), (30 W maximum) RayNet Ethernet network connection port (10 / 100 / 1000 Mbits/s).
8. Port 8 — Non-PoE RayNet network connection port (10/100/1000 Mbits/s)

Note: For product and port diagnostic information, refer to: p.47 — RNS-8 Diagnostic information

###### RNS-8 Diagnostic information

The following range of diagnostic information is available for the Network switch, which can be displayed on LightHouse 4 multifunction displays running software v4.5.84, or later. To view RNS-8 diagnostic product information on a LightHouse 4 multifunction display, select [RNS-8] from the [Diagnostics] pop over menu on the multifunction display: [Homescreen > Settings > Network > Diagnostics > RNS-8]. The following diagnostic information is displayed:

| Diagnostic | Description |
| --- | --- |
| Name: | Provides the product name. |
| Address: | Provides the product’s IP address. |
| Serial: | Provides the product’s serial number. |
| Version: | Provides the product’s software version number. |

Additional port diagnostic information can be displayed by tapping the row for the relevant unit and then selecting [Port traffic]. Once selected, the following port diagnostic information is displayed:

<!-- figure 1 on pdf page 47 at 38,130-314,278 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 7/12 words >= 60, mean confidence 63) -->
4
3e
4
Se
Te
6
12345678
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 47 at 334,185-607,276 pt | caption: none | text-layer labels: Diagnostic | Description | nearby labels: Name: | Provides the product name. | Address: | Provides the product’s IP address. | OCR text follows (tesseract, unverified; 11/13 words >= 60, mean confidence 77) -->
RNS-8 network switches
RNS-8
198.18.6.7
AG8KB9F
V0.42
RNS-8
198.18.5.185
A80732 AGCSH25
<!-- end of figure 2 -->

<!-- pdf page 48 | printed page 48 | header: Description -->

| Diagnostic | Description |
| --- | --- |
| Throughput (Bytes) — | Provides the current amount of |
| (port 1–8): | data (Bytes) that is currently being transferred via your network switch from a specific port. |
| Total Throughput | Provides the total amount of data |
| (Bytes) — (port 1–8): | (Bytes) that has been transferred via your network switch from a specific port. |
| Speed (Bps) — (port | Provides the current data transfer |
| 1–8): | speed (in Bits per second) for a specific port. |
| Negotiated Speed | Provides the port’s maximum data |
| (Mbits/sec) — (port 1–8):   transfer speed (10 / 100 / 1000 | Mbits/sec), which is negotiated during connection. |
| Diagnostic                Description |  |

| PoE Class (Watts) — | Provides the PoE classification of |
| --- | --- |
| (PoE ports 1, 3, 5, 7): | a connected PoE Powered Device (PD), and, the maximum power consumption (Watts) required by the PoE classification. For more PoE classification information, refer to the following section: p.36 — Power over Ethernet (PoE) |
| Power (Watts) — (PoE | Provides the current power |
| ports 1, 3, 5, 7): | consumption (Watts) of your connected Powered Device (PD). |

Note: The network switch can output a maximum of 120 Watts, for consumption by up to 4 PoE Powered Devices (i.e. 30 W maximum per Powered Device ).

<!-- figure 1 on pdf page 48 at 38,29-314,206 pt | caption: none | text-layer labels: Diagnostic | Description | nearby labels: Throughput (Bytes) — (port 1–8): | OCR text follows (tesseract, unverified; 26/28 words >= 60, mean confidence 88) -->
RNS-8 (A80732 AG8KB9F)
32680
2416729593
261440
1000
2.53
66008
1631084735
528064
1000
Unknown
0.00
Unknown,
0.00
2(7.0W)
257544
32193
2517796595
100
3.52
68552
1859172982
548416
1000
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 48 at 334,173-607,250 pt | caption: none | text-layer labels: none | nearby labels: Power (Watts) — ( PoE ports 1, 3, 5, 7): | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 49 | printed page 49 -->

## CHAPTER 12: MAINTENANCE

##### CHAPTER CONTENTS

###### 12.1 Service and maintenance (page 50)

###### 12.2 Routine equipment checks (page 50)

Maintenance                                      49

<!-- pdf page 50 | printed page 50 -->

### 12.1 Service and maintenance

This product contains no user serviceable components. Please refer all maintenance and repair to authorized Raymarine dealers. Unauthorized repair may affect your warranty.

### 12.2 Routine equipment checks

- It is recommended that you perform the following routine checks, on a regular basis, to ensure the correct and reliable operation of your
- equipment:
- Examine all cables for signs of damage or wear and tear.
- Check that all cables are securely connected.

###### Caution: Product cleaning

When cleaning products:
- Switch off power supply.
- Use a clean damp cloth to wipe clean.
- Do NOT use: abrasive, acidic, ammonia, solvent or other chemical-based cleaning products.
- Do NOT use a jet wash.

<!-- figure 1 on pdf page 50 at 197,180-314,298 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 50 at 41,182-86,298 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 51 | printed page 51 -->

## CHAPTER 13: TECHNICAL SUPPORT

##### CHAPTER CONTENTS

###### 13.1 Raymarine technical support and servicing (page 52)

###### 13.2 Diagnostic product information (page 53)

###### 13.3 Learning resources (page 53)

Technical support                                                  51

<!-- pdf page 52 | printed page 52 -->

### 13.1 Raymarine technical support and servicing

Raymarine provides a comprehensive product support service, as well as warranty, service, and repairs. You can access these services through the Raymarine website, telephone, and e-mail.

###### Product information

- If you need to request service or support, please have the following
- information to hand:
- Product name.
- Product identity.
- Serial number.
- Software application version.
- System diagrams.

###### Servicing and warranty

- Raymarine offers dedicated service departments for warranty, service, and repairs. Visit the Raymarine website to read the latest warranty policy, and
- register your product’s warranty online:
- www.bit.ly/rym-warranty
- United Kingdom (UK), EMEA, and Asia Pacific:
- Web: www.bit.ly/rym-service
- Tel: +44 (0)1329 246 932
- United States (US):
- Web: www.bit.ly/rym-service
- Tel: +1 (603) 324 7900

###### Web support

Please visit the “Support” area of the Raymarine website for:
- Manuals and Documents — www.bit.ly/rym-docs
- Technical support forum — www.bit.ly/rym-support
- Software updates — www.bit.ly/rym-software

###### Telephone and online support

| Region | Contact details |
| --- | --- |
| All regions | Online support: www.bit.ly/rym-support |
| United Kingdom (UK) and | Telephone: +44 (0)1329 246 |
| EMEA | 777 Address: Marine House, Cartwright Drive, Fareham, PO15 5RJ, UK. |
| United States (US) | Telephone: Tel: +1 (603) 324 7900 (Toll -free: +800 539 5539) Address: 110 Lowell Road, Hudson, NH 03051, USA. |
| Australia and New Zealand   Telephone: +61 2 8977 0300 |  |
| (Raymarine subsidiary) | Address: Suite 1.01, 26 Rodborough Road, Frenchs Forest, NSW, 2086, Australia. |
| France | Telephone: +33 (0)1 46 49 72 |
| (Raymarine subsidiary) | 30 Address: 35 avenue Michel Crépeau, 17000 La Rochelle - France. |
| Germany | Telephone: +49 40 237 808 0 |
| (Raymarine subsidiary) | Address: Atlantic-Haus, Zirkusweg 1, 20359 Hamburg. |
| Italy | Telephone: +39 02 9945 1001 |
| (Raymarine subsidiary) | Address: Via L. Manara 2, 20812 Limbiate (MB), Italy. |
| Spain | Telephone: +34 96 2965 102 |
| (Authorized Raymarine | Email: sat@azimut.es |
| distributor) |  |
| Netherlands / Benelux | Telephone: +31 (0)26 3614 905 |
| (Authorized Raymarine | Address: Florijnweg 21G, 6883 |
| distributor) | JN VELP, Nederland. |

<!-- pdf page 53 | printed page 53 -->

| Region | Contact details |
| --- | --- |
| Sweden | Telephone: +46 (0)317 633 670 |
| (Raymarine subsidiary) | Address: Bolshedens Industriväg 18, 427 50 Billdal, Sweden. |
| Finland | Telephone: +358 (0)207 619 |
| (Raymarine subsidiary) | 937 Address: Suomalaistentie 1-3, 02270 Espoo, Finland. |
| Norway | Telephone: +47 692 64 600 |
| (Raymarine subsidiary) | Address: Årvollskogen 30, 1529 Moss, Norway. |
| Denmark | Telephone: +45 437 164 64 |
| (Raymarine subsidiary) | Address: Centervej 7, 4600 Køge, Denmark. |
| Russia | Telephone: Tel: +7 495 788 |
| (Distributor) | 0508 Email: info@mikstmarine.ru |

### 13.2 Diagnostic product information

Diagnostic product information can be viewed and exported from a Raymarine LightHouse multifunction display, for supported products networked using RayNet (Ethernet), RJ45, RJ45 (SeaTalk HS) or SeaTalk NG / NMEA 2000 cables. Diagnostic product information includes technical data related to the connected product, such as serial numbers, network addresses, firmware version numbers, and so on. It is useful for 2 main purposes: 1.     Sending detailed product information to the Raymarine product support team, in the event of a problem or fault with your product. The information can be exported to a MicroSD card, and you can then copy the file for the purposes of emailing it to the product support team. For contact details, refer to: p.51 — Technical support 2. Maintaining detailed off-boat records. This is particularly useful for vessels that have multiple Raymarine products installed.

Technical support

To view or export diagnostic product information, access the [Diagnostics] menu. For instructions on how to access this menu, refer to the relevant Operation Instructions for your multifunction display.

### 13.3 Learning resources

Raymarine has produced a range of learning resources to help you get the most out of your products.

###### Video tutorials

Raymarine official channel on YouTube
- http://www.youtube.com /user/RaymarineInc

###### Training courses

- Raymarine regularly runs a range of in-depth training courses to help you make the most of your products. Visit the Training section of the
- Raymarine website for more information:
- www.bit.ly/rym-training

###### Technical support forum

You can use the Technical support forum to ask a technical question about a Raymarine product or to find out how other customers are using their Raymarine equipment. The resource is regularly updated with contributions from Raymarine customers and staff: • www.bit.ly/rym-support

53

<!-- pdf page 54 | printed page 54 -->

## CHAPTER 14: TECHNICAL SPECIFICATION

##### CHAPTER CONTENTS

| • | 14.1 Physical speciﬁcation (page 55) |
| --- | --- |
| • | 14.2 Power speciﬁcation (page 55) |
| • | 14.3 Network speciﬁcation (page 55) |
| • | 14.4 Environmental speciﬁcation (page 55) |
| • | 14.5 Conformance speciﬁcation (page 56) |

<!-- pdf page 55 | printed page 55 -->

14.1 Physical speciﬁcation

###### Specification

| Length: | 287.63 mm (11.32 in). |
| --- | --- |
| Height: | 125.5 mm (4.94 in). |
| Depth: | 78 mm (3.07 in). |
| Port separation distance: | 17.38 mm (0.68 in) |
| Weight: | 960.5 g (2.12 lbs) |

14.2 Power speciﬁcation

| Nominal supply voltage: | 12 V or 24 V dc |
| --- | --- |
| Operating voltage range: | 9 V to 31.2 V dc |
| PoE nominal output voltage range: | 42.5 V to 57.0 V dc |
| Power consumption: | • 160 W (Maximum) @ 12 V dc • 150 W (Maximum) @ 24 V dc |
| Current draw: | • 13.3 A (Maximum) @ 12 V dc • 6.25 A (Maximum) @ 24 V dc |
| Inline fuse ratings: | • 12 V: 15A • 24 V: 8A |
| Thermal breaker ratings: | • 12 V: 20A • 24 V: 10A |

Technical speciﬁcation

14.3 Network speciﬁcation

Network connection       • 4x RayNet connection ports (10 / 100 ports:                     / 1000 Mbits/s) • 4x PoE RayNet connection ports (10 / 100 / 1000 Mbits/s). Each of the 4 ports supports PoE Classes 0 to 4, with 30 W maximum power available for each port.

Note:
- You can mix a combination of PoE and non-PoE devices simultaneously, for a total of 8 devices (maximum PoE devices = 4; maximum non-PoE devices = 8).
- In order to sufficiently power PoE devices, the network switch’s power supply must exceed 10.8 V dc.

IEEE Standard:           Conforms to IEEE 802.3at

14.4 Environmental speciﬁcation

| Operating temperature: | -25 °C (-13 °F) to +55 °C (131 °F) |
| --- | --- |
| Non-operating | -30 °C (-22 °F) to +70 °C (158 °F) |
| temperature: |  |
| Relative humidity: | up to 93% @ 40 °C (104 °F) |
| Waterproof rating: | IPx6, IPx7 |

55

<!-- pdf page 56 | printed page 56 -->

14.5 Conformance speciﬁcation

- Approvals:          • EN 60945:2002 (Europe, Australia New Zealand)
- EN ISO 8846:2017
- ICES-003 (Canada)
- CFR47 Part 15 (USA)
- IACS section E10 (Japan / China)
- EMC Directive 2014/30/EU
- Product markings:   • UKCA
- CE
- Australian Tick
- WEEE Directive

<!-- pdf page 57 | printed page 57 -->

## CHAPTER 15: SPARES AND ACCESSORIES

##### CHAPTER CONTENTS

###### 15.1 Spares and accessories (page 58)

###### 15.2 RayNet to RayNet cables and connectors (page 59)

###### 15.3 RayNet to RJ45, and RJ45 (SeaTalk HS) adapter cables (page 61)

<!-- pdf page 58 | printed page 58 -->

### 15.1 Spares and accessories

- The following spares and accessories are available for the
- RNS-Series:

|  | Part | Description |
| --- | --- | --- |
| 1 | 4115028 | RJ45 to RJ45 waterproof coupler. |
| 2 | A80346 | Power cable, 1.5 m (4.9 ft.). |

<!-- figure 1 on pdf page 58 at 38,72-314,170 pt | caption: none | text-layer labels: Part | Description | nearby labels: 1 | 4115028 | RJ45 to RJ45 waterproof coupler. | 2 | A80346 | Power cable, 1.5 m (4.9 ft.) . | OCR: no legible text (0/2 words >= 60, mean confidence 0) -->

<!-- pdf page 59 | printed page 59 -->

### 15.2 RayNet to RayNet cables and connectors

1. Standard RayNet connection cable with a RayNet (female) socket on both ends.
2. Right-angle RayNet connection cable with a straight RayNet (female) socket on one end, and a right-angle RayNet (female) socket on the other end. Suitable for connecting at 90° (right angle) to a device, for installations where space is limited.

| 3. | Right-angle RayNet connection cable with a straight RayNet (female) socket on one end, and a right-angle RayNet (female) socket on the other end. Available as an alternative to the (A80512) accessory cable, for installations which require an alternate cable routing direction. |
| --- | --- |
| 4. | RayNet cable puller (5 pack). |

<!-- figure 1 on pdf page 59 at 38,46-607,403 pt | caption: none | text-layer labels: none | nearby labels: 1. | 3. | OCR text follows (tesseract, unverified; 26/36 words >= 60, mean confidence 70) -->
1
00 mm (1.3 ft)
ft)
5 m (16.4 ft)
10 m (32.8 ft)
4
A80161 A62361
ft)
0.5 m (1.6 ft)
10 m (32.8 ft)
<!-- end of figure 1 -->

<!-- pdf page 60 | printed page 60 -->

5. RayNet to RayNet right-angle coupler / adapter. Suitable for connecting RayNet cables at 90° (right angle) to devices, for installations where space is limited.
6. Adapter cable with a RayNet (male) plug on both ends. Suitable for joining (female) RayNet cables together for longer cable runs.

<!-- pdf page 61 | printed page 61 -->

### 15.3 RayNet to RJ45, and RJ45 (SeaTalk HS) adapter cables

1. Adapter cable with a RayNet (female) socket on one end, and a waterproof (female) RJ45 (SeaTalk HS) socket on the other end, accepting the following cables with an RJ45 (SeaTalk HS) waterproof locking (male) plug:
- A62245 (1.5 m).
- A62246 (15 m).

2. Adapter cable with a RayNet (female) socket on one end, and a waterproof (female) RJ45 (SeaTalk HS) socket on the other end, along with a locking gland for a watertight fit.
3. Adapter cable with a RayNet (male) plug on one end, and an RJ45 (SeaTalk HS) waterproof (male) plug on the other end.

<!-- figure 1 on pdf page 61 at 38,46-607,401 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR text follows (tesseract, unverified; 57/73 words >= 60, mean confidence 77) -->
400 mm (1.3 tt)
100 mm (3.9 in)
3m (9.84 ft)
OF
(j=)
1m (3.28 ft)
10 m (32.8 ft)
3m (9.84 ft)
A80151
15 m (49.21 ft)
25 m (82.02 ft)
30 m (98.4 ft)
A80763 308-251-30-00
1m (3.28 ft)
3 m (9.84 ft)
30 m (98.4 ft)
10 m (32.81 ft)
A80756
A80837 308-252-30-00
308-0261-01-00
<!-- end of figure 1 -->

<!-- pdf page 62 | printed page 62 -->

4. Adapter cable with a RayNet (male) plug on one end, and an RJ45 (male) plug on the other end.
5. Adapter cable with a RayNet (female) socket on one end, and an RJ45 (SeaTalk HS) waterproof (male) plug on the other end.
6. Adapter cable with a RayNet (female) socket on one end, and an RJ45 (male) plug on the other end.
7. Adapter cable with a right-angled RayNet (female) socket on one end, and an RJ45 (male) plug on the other end.

<!-- pdf page 63 | printed page 63 -->

###### Appendix A Ethernet (IPv4) networking of Raymarine devices with third-party products

Raymarine uses a custom Ethernet (IPv4) networking configuration. Use the following information to help you understand how Raymarine’s Ethernet (IPv4) implementation interacts with third-party Ethernet (IPv4) devices on your vessel, such as routers, switches, Access Points (APs) etc.

Important:
- Third-party networking products such as routers, switches, and Access Points (APs) may work when connected to Raymarine networks, when configured correctly. However, correct operation is not guaranteed. It’s important to refer to the instructions provided by the relevant third-party device manufacturer, to ensure that your intended use of a third-party device is consistent with the device’s design intent.
- Raymarine does not warrant that Raymarine products are compatible with products manufactured by any person or entity other than Raymarine.
- When using third-party products in your Raymarine electronics network, you should be aware of, and understand, the concepts and limitations described in the following Disclaimer: p.8 — Disclaimer

###### Overview

- Ethernet (IPv4) networking is a method for interconnecting multiple electronic devices, allowing many devices to function in a network and share data using only a single RJ45 or RayNet connection for each device.
- In order to function correctly, every Ethernet (IPv4) device (whether Raymarine or third-party) must have a unique IP address allocated to it, and it must not conflict with that of any other device.
- IPv4 addresses can be centrally-allocated to devices either automatically, using a method known as DHCP (Dynamic Host Configuration Protocol), or manually (i.e. allocated a static IP address). The most common method for allocating IPv4 addresses on vessel electronics networks is DHCP. In this configuration, the server device is known as a DHCP server. Ethernet (IPv4) networking of Raymarine devices with third-party products

Client / Server device             Example(s)

| Raymarine IPv4 DHCP client | • Radar scanner (e.g. Quantum-Series) • Sonar module (e.g. CP470) • IP camera (e.g. CAM300) |
| --- | --- |
| Raymarine IPv4 DHCP server | • Chartplotter (MFD), running |
| and self-addressing device | LightHouse 3 or LightHouse 4 (e.g. Axiom-Series) • Marine Router (e.g. YachtSense Link) |
| Third-party IPv4 DHCP client | IP camera |
| Third-party IPv4 DHCP server | • Router • Switch • Access Point (AP) |

Note: The DHCP server maintains a pool of IP addresses and “leases” an address to any DHCP-enabled client, when the client device first powers up and announces its presence on the network. Because the IP addresses are dynamic (leased) rather than static (permanently assigned), addresses no longer in use are automatically returned to the DHCP server’s pool, for subsequent reallocation.

It’s also possible to have multiple DHCP servers issuing addresses on an IPv4 network, but to avoid addressing conflicts, all DHCP servers must be carefully configured to only allocate IP addresses in distinct address ranges. The subnet mask must also be carefully configured, to ensure that devices can correctly communicate with one another.

###### Implementation

- Raymarine Ethernet (IPv4) devices expect to use a private Raymarine IPv4 network, which is designed to be internal to the vessel only. Raymarine has carefully chosen a specific IP address range (198.18.0.0/21 ) to ensure that it does not interfere with 63

<!-- pdf page 64 | printed page 64 -->

any external IP address ranges, or other legacy and real-world addressing constraints (including but not limited to marina Wi-Fi networks).

Note: Raymarine’s IP address range is for local traffic within the vessel’s private Raymarine network only, and does NOT traverse across Raymarine products to external networks, or to the Internet.

- In a Raymarine Ethernet (IPv4) network, IP addresses are self-allocated by certain Raymarine equipment in the following range: 198.18.0.32 to 198.18.3.255 (inclusive). You must avoid placing any devices in this range using manual (static) IP addresses.
- Whether your network includes only Raymarine Ethernet (IP) devices, or a mixture of Raymarine and third-party Ethernet (IPv4) devices, you have 3 options for configuring the Ethernet (IPv4) network and managing the IP addresses for your devices:
1. Use a Raymarine device as the sole DHCP server to allocate IP addresses automatically to all Raymarine and third-party Ethernet (IPv4) devices on the network. For the purposes of simplicity and reliability, this is the recommended option for most vessels. The following Raymarine devices can act as DHCP servers:
a. Raymarine chartplotter (MFD), running LightHouse 3 or LightHouse 4; or:
b. Raymarine YachtSense Link router

Note: If both a Raymarine chartplotter (MFD) and YachtSense Link router are present in the same network, the YachtSense Link router MUST be configured as the DHCP server for that network. To facilitate this, the Raymarine chartplotter’s (MFD's) DHCP setting defaults to Automatic as standard. On power up, if the YachtSense Link router is detected on the Ethernet network, any chartplotters (MFDs) in the network will disable their own DHCP Server, to permit the YachtSense Link router to manage the network's IP addresses. Only Raymarine chartplotters (MFDs) running LightHouse 4 are compatible with the YachtSense Link router. Additionally, the most recent versions of the LightHouse 4 and YachtSense Link software must be used.

2. Use a third-party Ethernet (IPv4) device (such as a router or Access Point) to allocate IP addresses automatically, as a sole DHCP server. To do this, refer to the Configuring a third-party router as DHCP server section, below.

Note: Any Raymarine LightHouse 3 or LightHouse 4 chartplotters (MFDs) will still self-allocate their own IP address, even if a third-party DHCP server is being used to allocate IP addresses to other Raymarine or non-Raymarine DHCP client devices (Camera, Radar, Sonar etc.) on the network.

3. Manually configure static IP addresses for your devices. The address range 198.18.0.32 to 198.18.3.255 (inclusive) is used by Raymarine equipment, and any other third-party equipment on the network should not be set to a static IP address in this range. It should instead be set elsewhere in the 198.18.0.0/21 range.

###### Adding third-party devices to your Raymarine Ethernet (IP) network

- It is recommended that any third-party products connecting to a Raymarine Ethernet (IPv4) network (e.g., a third-party IP camera) are configured as DHCP clients, so that they automatically get allocated a correct IP address within the range used by the Raymarine IPv4 network. If this is not possible, (for example, in the scenario that your third-party IP Camera requires a static IP address), you should configure the product to have a static IP

<!-- pdf page 65 | printed page 65 -->

address within the following range: 198.18.0.1 to 198.18.0.31 (inclusive). • Any third-party router in your network should be performing IPv4 Network Address Translation (NAT) from the private address to another one on an upstream interface.

Conﬁguring a third-party router as DHCP server In the scenario that you wish to use a third-party DHCP server to allocate the IP addresses for your vessel’s IPv4 network, use the following information to help you configure the third-party DHCP server to work with Raymarine Ethernet (IPv4) client devices: 1.     Configure the third-party DHCP server / router to use Raymarine's subnet details, which are as follows: a.     Set the DHCP server's IP address to 198.18.0.1 b.     Set the netmask to /21, i.e. 255.255.248.0 c.     Set the DHCP range from 198.18.4.0 to 198.18.7.254 (inclusive). If this is not possible, ensure that the address range is smaller than this (but within the range of 198.18.4.0 to 198.18.7.254 (inclusive)). d. The address range 198.18.0.32 to 198.18.3.255 (inclusive) is used by Raymarine equipment, and therefore you must ensure that any other third-party equipment on the network is NOT set to a static IP address in this range. 2. It may be necessary to set the DHCP setting for all of the chartplotters (MFDs) on the vessel to [Off]. However, the default option ([Auto]) will likely work fine in many cases. If for any reason the third-party DHCP server starts up after the chartplotter (MFD) starts up, the user should manually set the chartplotter’s (MFD's) DHCP switch to [Off]. This is because, when the chartplotter (MFD) starts up, its DHCP [Auto] feature tries to detect if another DHCP server is already present on the network. 3.     In case of failure of the third-party device, the chartplotters (MFDs) can be easily configured to be the DHCP server again, by setting the chartplotter’s (MFD’s) DHCP setting back to [Auto].

###### Adding third-party Wi-Fi Access Points / Wi-Fi routers to your Raymarine Ethernet (IPv4) network

- There is a large volume of multicast IPv4 traffic on the Raymarine Ethernet (IPv4) network. Many consumer Wi-Fi Access Points / Ethernet (IPv4) networking of Raymarine devices with third-party products

Wi-Fi routers simply bridge all multicast traffic from the Ethernet interface to the Wi-Fi interface when there are connected Wi-Fi clients. This will result not only in poor Wi-Fi performance but also in a reduction of usable Wi-Fi spectrum to other Wi-Fi users and vessels in the vicinity. If using a third-party Wi-Fi Access Point or Wi-Fi router, Raymarine recommends that IGMP Snooping is enabled on the third-party device, and additional checks are performed, in order to ensure that your device is not bridging any unexpected multicast traffic to its Wi-Fi interface from the Raymarine Ethernet (IPv4) network. • Raymarine’s YachtSense Link router is pre-configured with IGMP Snooping enabled, and therefore does not bridge internal multicast traffic on the wired network to the Wi-Fi network. No additional configuration is required in this respect.

65 (no text layer on this page)

<!-- pdf page 66 -->

<!-- pdf page 67 -->

#### Index

#### A

#### C

Cable Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27–28 Cables Cabling Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15, 28

#### D

Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43, 46, 53 Exporting product information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46, 53 Viewing product information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46, 53

#### E

Electromagnetic Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8, 22 EMC, See Electromagnetic Compatibility

#### F

#### I

Installation See also Compass safe distance

#### L

Location requirements

#### M

Maintenance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8, 50

<!-- pdf page 68 -->

#### N

Network Network connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33–34 Networking (IP)

#### P

Power Protocols

#### R

RayNet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30, 63 cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59, 61 RJ45

#### S

SeaTalkhs Servicing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8, 50 Suppression ferrites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9, 28 See also EMC System diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15, 28

#### T

Technical specification Technical support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52–53 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43, 46, 53 PoE Status LED diagnostics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45–46 Typical system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15, 28

#### V

#### W

Warranty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9, 52
