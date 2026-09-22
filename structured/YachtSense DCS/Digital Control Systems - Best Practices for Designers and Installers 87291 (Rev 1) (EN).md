# Digital Switching Systems

<!-- source: sources/YachtSense DCS/Digital Control Systems - Best Practices for Designers and Installers 87291 (Rev 1) (EN).pdf | extraction: extracted/YachtSense DCS/Digital Control Systems - Best Practices for Designers and Installers 87291 (Rev 1) (EN).md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: no ToUnicode map in Industry-Bold, Industry-Light, UniversLTStd-LightCn; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1, 32 checked against the rendered page) -->

<!-- pdf page 1 -->

Digital Switching Systems

## Best Practice

## for designers and installers

- English (EN)
- Date: 11-2016
- Document number: 87291-1 © 2016 Raymarine UK Limited

<!-- figure 1 on pdf page 1 at 332,722-538,775 pt | caption: none | text-layer labels: none | OCR below floor, text not used (1/3 words >= 60, mean confidence 55) -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

<!-- sub/superscripts on this page (from font sizes): SeaTalk^hs, SeaTalk^ng -->

<!-- omitted: "Trademark and patents notice" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair Use Statement" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
#### Software updates

Important: Check the Raymarine website for the latest software releases for your product.

www.raymarine.com/software

#### Product handbooks

The latest versions of all English and translated handbooks are available to download in PDF format from the website www.raymarine.com. Please check the website to ensure you have the latest handbooks.

Copyright ©2016 Raymarine UK Ltd. All rights reserved.

- English (en-US)
- Document number: 87291-1
- Release label: AA
- Commit revision: 1510
- Date: 11-2016

<!-- figure 1 on pdf page 3 at 153,312-564,360 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 4 -->

(no text layer on this page)

<!-- pdf page 5 | printed page 5 -->

Contents

| Chapter 1 Important information........... 7 | Best practice: dealing with inductive |
| --- | --- |
| Product disposal......................................            8 | Best practice: when to use GSM SMS |
| IMO and SOLAS......................................               8 | Best practice: consider control panel |
| Chapter 2 Document overview .............. 9 | Best practice: consider security of |
| 2.2 Audience ........................................... 10 | Best practice: configure strong Wi-Fi |
| for digital switching systems ................ 13 | Best practice: take extra |
| 3.1 Digital switching overview ................. 14 | precautions when switching moving |
| 3.3 Using this document.......................... 15 | Best practice: configure software fuses |
| recommendations................................... 17 | 4.5 System redundancy and fail-safe |
| 4.1 Human factors in system |  |
| design...................................................... 18 | Best practice: use redundant switching |
| multifunction displays (MFDs) ................. 18 | Best practice: implement fail-safe |
| Best practice: consider MFD | Best practice: consider |
| context..................................................... 19        SeaTalkng/NMEA 2000 (CAN bus) |  |
| capabilities for MFDs............................... 19 | Best practice: limit configuration file |
| switches .................................................. 19 | 4.7 System testing and |
| Best practice: use switch-guards for |  |
| critical circuits.......................................... 19 | Best practice: take appropriate |

| unlatched switches.................................. 20 | Best practice: perform comprehensive |
| --- | --- |
| installation ............................................... 21 | Best practice: perform regression |
| CAN-cabling ............................................ 22 | 4.8 System documentation and |
| Best practice: use a CAN |  |
| network bridge to isolate critical | Best practice: provide comprehensive |

Best practice: do not exceed CAN bus                                   Best practice: keep system

<!-- pdf page 6 | printed page 6 -->

- Best practice: provide contextual labelling and emergency
- Best practice: create system backups,

<!-- pdf page 7 | printed page 7 -->

## Chapter 1: Important information

### Warning: Product installation and operation

- This product must be installed and operated in accordance with the instructions provided. Failure to do so could result in personal injury, damage to your vessel and/or poor product performance.
- Raymarine recommends certified installation by a Raymarine approved installer. A certified installation qualifies for enhanced product warranty benefits. Contact your Raymarine dealer for further details, and refer to the separate warranty document packed with your product.

### Warning: Product grounding

Before applying power to this product, ensure it has been correctly grounded, in accordance with the instructions provided.

### Warning: Positive ground systems

Do not connect this unit to a system which has positive grounding.

### Warning: Power supply voltage

Connecting a product to a voltage supply greater than the specified maximum rating may cause permanent damage. For voltage ratings, refer to the Technical specification section of the product's documentation.

### Warning: Switch off power supply

Ensure the vessel’s power supply is switched OFF before starting to install this product. Do NOT connect or disconnect equipment with the power switched on, unless instructed in this document.

### Caution: Do not open the unit

The unit is factory sealed to protect against atmospheric humidity, suspended particulates and other contaminates. It is important that you do not open the unit or remove the casing for any reason. Opening the unit will: • compromise the seal with possible damage to the unit, and • void the manufacturer’s warranty.

Important information

### Caution: Power supply protection

When installing this product ensure the power source is adequately protected by means of a suitably-rated fuse or automatic circuit breaker.

### Caution: Service and maintenance

This product contains no user serviceable components. Please refer all maintenance and repair to authorized Raymarine dealers. Unauthorized repair may affect your warranty.

## EMC installation guidelines

Raymarine equipment and accessories conform to the appropriate Electromagnetic Compatibility (EMC) regulations, to minimize electromagnetic interference between equipment and minimize the effect such interference could have on the performance of your system Correct installation is required to ensure that EMC performance is not compromised. Note: In areas of extreme EMC interference, some slight interference may be noticed on the product.Where this occurs the product and the source of the interference should be separated by a greater distance.

For optimum EMC performance we recommend that wherever possible: • Raymarine equipment and cables connected to it are: – At least 1m (3ft) from any equipment transmitting or cables carrying radio signals e.g. VHF radios, cables and antennas. In the case of SSB radios, the distance should be increased to 7 ft (2 m). – More than 2m (7ft) from the path of a radar beam. A radar beam can normally be assumed to spread 20 degrees above and below the radiating element. • The product is supplied from a separate battery from that used for engine start. This is important to prevent erratic behavior and data loss which can occur if the engine start does not have a separate battery. • Raymarine specified cables are used. • Cables are not cut or extended, unless doing so is detailed in the installation manual. Note: Where constraints on the installation prevent any of the above recommendations, always ensure the maximum possible separation between different items of electrical equipment, to provide the best conditions for EMC performance throughout the installation 7

<!-- figure 1 on pdf page 7 at 306,17-564,110 pt | caption: none; nearest centred text below: "Caution: Service and maintenance" | text-layer labels: Caution: Power supply protection | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 7 at 41,41-84,261 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 7 at 306,118-564,223 pt | caption: none | text-layer labels: Caution: Service and maintenance | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 7 at 41,266-299,333 pt | caption: none; nearest centred text below: "Warning: Positive ground systems" | text-layer labels: Warning: Product grounding | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 7 at 41,341-299,410 pt | caption: none; nearest centred text below: "Warning: Power supply voltage" | text-layer labels: Warning: Positive ground systems | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 6 on pdf page 7 at 41,415-299,535 pt | caption: none; nearest centred text below: "Warning: Switch off power supply" | text-layer labels: Warning: Power supply voltage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 7 on pdf page 7 at 41,540-299,648 pt | caption: none; nearest centred text below: "Caution: Do not open the unit" | text-layer labels: Warning: Switch off power supply | nearby labels: Caution: Do not open the unit | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 8 | printed page 8 -->

## Suppression ferrites

- Raymarine cables may be pre-fitted or supplied with suppression ferrites. These are important for correct EMC performance. If ferrites are supplied separately to the cables (i.e. not pre-fitted), you must fit the supplied ferrites, using the supplied instructions.
- If a ferrite has to be removed for any purpose (e.g. installation or maintenance), it must be replaced in the original position before the product is used.
- Use only ferrites of the correct type, supplied by Raymarine or its authorized dealers.
- Where an installation requires multiple ferrites to be added to a cable, additional cable clips should be used to prevent stress on the connectors due to the extra weight of the cable.
- If your camera installation requires long cable runs, you may need to fit additional ferrites to maintain acceptable EMC performance.

## Product disposal

Dispose of this product in accordance with the WEEE Directive.

The Waste Electrical and Electronic Equipment (WEEE) Directive requires the recycling of waste electrical and electronic equipment.

<!-- omitted: "Warranty registration" (pdf page 8; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
## IMO and SOLAS

The equipment described within this document is intended for use on leisure marine boats and workboats NOT covered by International Maritime Organization (IMO) and Safety of Life at Sea (SOLAS) Carriage Regulations.

<!-- omitted: "Technical accuracy" (pdf pages 8-9; 2 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 9 | printed page 9 -->
## Chapter 2: Document overview

### Chapter contents

| • | 2.1 Document information on page 10 |
| --- | --- |
| • | 2.2 Audience on page 10 |
| • | 2.3 Limitations on page 11 |

Document overview                           9

<!-- pdf page 10 | printed page 10 -->

## 2.1 Document information

The best-practice recommendations in this document apply to generic marine digital switching systems. This information is not specific to any single manufacturer of digital switching system components. In addition to reading this document, and before starting work on a digital switching system, you should also refer to the documentation provided by the original manufacturer of individual system components.

## 2.2 Audience

This document is intended to provide guidance to those responsible for designing, installing, testing, commissioning, maintaining, or modifying a marine digital switching system that uses components supplied by Raymarine. The guidance provided is relevant to boat builders, dealers, and support technicians. Owners of vessels equipped with a digital switching system, that wish to modify the system, may also find this guidance useful. Important: Personnel responsible for designing, installing, testing, commissioning, maintaining, or modifying digital switching systems must be appropriately trained and qualified to perform the tasks required.

<!-- pdf page 11 | printed page 11 -->

## 2.3 Limitations

Important: Marine digital switching systems are extremely flexible, and highly configurable. As such, this document does not, and cannot, provide guidelines for every circumstance and eventuality that you may encounter when designing and installing a digital switching system.

Document overview                                    11 (no text layer on this page)

<!-- pdf page 12 | printed page 12 -->

<!-- pdf page 13 | printed page 13 -->

## Chapter 3: Introducing best practice for digital switching systems

### Chapter contents

| • | 3.1 Digital switching overview on page 14 |
| --- | --- |
| • | 3.2 About “best practice” on page 15 |
| • | 3.3 Using this document on page 15 |

Introducing best practice for digital switching systems              13

<!-- pdf page 14 | printed page 14 -->

## 3.1 Digital switching overview

Digital switching systems enable the creation of highly customizable power distribution, control, monitoring, and alarm management systems for boats and yachts.

| Data from different systems on a vessel can be | Additionally, the simplification of power-distribution |
| --- | --- |
| integrated and centralized, increasing the availability | cabling achievable by implementing a digital |
| of important information. When integrated with | switching system can significantly reduce costs. |

Raymarine multifunction displays (MFDs), dedicated user interfaces can greatly simplify the control and monitoring of vessel systems.

| Symbol                 Description | Symbol                 Description |
| --- | --- |
| DC power cable | Wipers |
| SeaTalkng/NMEA 2000 (CAN bus) |  |
| network cable | Anchor winch |
| Digitally switched input / output |  |
| cable |  |
| DC power supply | This document applies to generic digital switching systems built on a SeaTalkng / NMEA 2000 (CAN bus) network, and making use of Raymarine |
| Digital switching unit | MFDs. Details of individual digital switching system components are not covered. |

Navigation light

Searchlight

Digital-switch panel

Interior light

Contact switch

Bilge pump

Raymarine multifunction display (MFD)

<!-- figure 1 on pdf page 14 at 29,158-552,367 pt | caption: none; nearest centred text below: "Symbol" | text-layer labels: none | nearby labels: Symbol | Symbol | Description | Description | OCR below floor, text not used (3/26 words >= 60, mean confidence 17) -->

<!-- figure 2 on pdf page 14 at 294,374-552,473 pt | caption: none | text-layer labels: Symbol | Description | Wipers | Anchor winch | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 15 | printed page 15 -->

## 3.2 About “best practice”

Digital switching systems offer almost unlimited possibilities for monitoring and controlling the electrical systems on a vessel. While this flexibility gives system designers vast scope for implementing bespoke and novel monitoring and control solutions, it is critical that these solutions are designed with consideration for the overall safety and security of the crew and the vessel. To help designers and installers create safe and secure digital switching systems, this document presents a number of “best practice” recommendations. Best practice is guided by the experience of skilled designers and installers with a range of digital switching systems, varying in scope and complexity. By following best-practice recommendations during the design and installation of a new digital switching system, or while modifying an existing system, you can benefit from the checks and processes already proved in the field. Following best practice will result in a safer, more secure, robust, and maintainable digital switching system. Note: In addition to this document, always refer to the detailed technical documentation provided by the original manufacturer of individual digital switching system components.

Note: As the designer or installer of a digital switching system, you should be appropriately trained and have experience of working with both the digital switching system components, and the vessel electrical systems and equipment that will be controlled or monitored by the digital switching system.

Note: Refer to the international standard IEC 61508 (”Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems”) for comprehensive guidelines on developing systems that comprise electrical, electronic, or programmable electronic components that perform safety functions.

Introducing best practice for digital switching systems

## 3.3 Using this document

This document groups best-practice recommendations into eight categories. Each category covers a particular aspect of digital switching system design and implementation: Category                  Summary 4.1 Human factors in      Human factors is a discipline system design             concerned with understanding how people interact with systems, and designing user interfaces that facilitate safe and efficient control and monitoring of those systems. 4.2 Physical network    Your digital switching system design and installation makes use of a wired SeaTalkng / NMEA 2000-compatible Controller Area Network bus (CAN bus) to transmit switching signals around the vessel. The linear nature of the CAN bus requires consideration during design. 4.3 System security       The best practice recommendations in this section will help you to design appropriate security features into your digital switching system. This is particularly important where moving equipment could cause injury if operated improperly. 4.4 System safety         Designers of digital switching systems must always consider the safety of the vessel and of those on board. The best practice recommendations in this section cover safety regarding moving equipment, and electrical fuses. 4.5 System                Digital switching systems redundancy and            are not immune to failures, fail-safe design          particularly when subject to extreme environmental conditions, such as a nearby lightning strike. Careful and considered design with regard to system redundancy and implementing fail-safe mechanisms, will ensure that your digital switching system is robust, and that rare events are less likely to disable critical vessel systems. 4.6 System                To ensure that your digital switching performance               system operates consistently and reliably, certain limitations of the SeaTalkng/NMEA 2000 (CAN bus) network, and Raymarine MFDs should be considered.

15

<!-- figure 1 on pdf page 15 at 469,101-564,197 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 16 | printed page 16 -->

Category                 Summary 4.7 System testing and Having followed best practice commissioning          for system design, it is important that all components of the digital switching system as implemented, are comprehensively tested. 4.8 System               Although a digital switching system documentation and        can greatly reduce the complexity backups                  and amount of cabling required compared to an equivalent traditionally switched system, it is still important to document the design of each installed system.

<!-- figure 1 on pdf page 16 at 29,17-287,197 pt | caption: none | text-layer labels: Category | Summary | 4.8 System documentation and backups | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 17 | printed page 17 -->

## Chapter 4: Best practice recommendations

### Chapter contents

| • | 4.1 Human factors in system design on page 18 |
| --- | --- |
| • | 4.2 Physical network design and installation on page 21 |
| • | 4.3 System security on page 23 |
| • | 4.4 System safety on page 24 |
| • | 4.5 System redundancy and fail-safe design on page 25 |
| • | 4.6 System performance on page 26 |
| • | 4.7 System testing and commissioning on page 27 |
| • | 4.8 System documentation and backups on page 28 |

<!-- pdf page 18 | printed page 18 -->

## 4.1 Human factors in system design

The best practice recommendations in this section cover design considerations based on human factors. Human factors is a discipline concerned with understanding how people interact with systems, and designing user interfaces that facilitate safe and efficient control and monitoring of those systems. When designing the user interfaces for a digital switching system, you are able to choose from a number of different switching mechanisms. Any one, or a combination of, the following switching mechanisms may be available: Soft-switches on a touch-screen multifunction display (MFD) (including toggle buttons, option buttons, and sliders)

Short-range wireless switches

Buttons on a SeaTalkng / NMEA 2000 keypad

Traditional push-button switches (including momentary, latching, and rotary switches)

Remote switching using a web application (running on a smart phone or tablet), or by sending a GSM SMS text message

- The most appropriate choice of switching mechanism
- depends on:
- the type of equipment or system being switched
- the physical environment and location of both the switched equipment and the switch
- the capabilities of the user operating the switch
- a requirement to display status information for the switched equipment or system
- the relationship, if any, between the switched item and other items or systems

### Introduction to touchscreen multifunction displays (MFDs)

Raymarine touchscreen multifunction displays (MFDs) provide a powerful and flexible method for utilizing soft-switches and bespoke graphical user interfaces to control and monitor vessel systems with digital switching. Touchscreen displays enable intuitive and efficient interactions with vessel systems, and allow for highly contextual presentation of controls and status information. However, touchscreen displays may not always be appropriate as the primary means to control certain vessel systems or equipment. The detailed design of individual touchscreen displays can also cause problems for users unless individual screen-designs and the components they comprise (for example, soft-buttons, gauges, and background images) are carefully built and tested. When designing a digital switching system that uses an MFD to control and monitor vessel systems, consider the following best practice recommendations.

### Best practice: consider MFD environmental conditions

Environmental conditions where the MFD is located may affect usability. For example: • Rain, sea spray, condensation, or sweat may make the MFD slippery or difficult to read, and could result in unintentional commands. • Excessive vibration or sudden motion (caused by other equipment, or a high sea state) may prevent users from interacting with the MFD using precise actions. • Direct sunlight may make it difficult to read and interact with the display. • In low temperatures, users may need to wear gloves, impacting the usability of the display To facilitate the safe and effective use of a touchscreen display in a variety of conditions: • Where possible, provide MFDs with physical protection from the environment. • Ensure that soft-buttons and associated icons and text are sufficiently large, and have adequate contrast. • Consider further distinguishing between important soft-buttons by using different button shapes, and contrasts. • Allow sufficient space between active parts of the touchscreen display (for example, between individual soft-buttons), to reduce the likelihood that users will touch a button inadvertently. • Remember that certain types of control may be difficult to use in some conditions. For example, don’t use a slider control that requires a precise swiping action as the only means to control a critical system. • Implement a “long press” feature to protect all buttons controlling important systems or equipment. For example, enforce a three-second press before a soft-button signals that AC shore-power is to be connected or disconnected from the vessel’s electrical system. Note: Where rapid operation or power-down of equipment may be required in an emergency, don’t enforce a “long press”. Also consider providing a physical switch in addition to soft buttons on an MFD (see Best practice: when to provide physical switches).

<!-- pdf page 19 | printed page 19 -->

### Best practice: consider MFD context

Contextual placement of touchscreen displays may affect usability. For example: • Locating a display where it is likely to be knocked or bumped could result in unintentional switching actions. • A display that is grouped with other controls (for example, an array of physical switches) will form an automatic association between the grouped controls for users. When locating touchscreen displays: • Consider the context of the display with respect to other user controls, and with the user’s position while operating the display. • Where space is limited and accidental touchscreen presses may be hard to avoid, consider safeguarding the touchscreen with appropriately positioned physical barriers. • Consider the context of the display with respect to the systems or equipment under control. In some cases (for example, moving equipment), maintaining line-of-sight between the user operating the MFD and the controlled equipment is important.

### Best practice: consider user capabilities for MFDs

User capabilities should be considered when designing touchscreen displays. For example: • Sight problems, such as reduced visual acuity, or color-blindness, may make it difficult for some users to operate touchscreen displays effectively. • Lack of experience with touchscreen displays may cause additional problems for some users. To assist users: • Ensure that soft-buttons and associated icons and text are sufficiently large, and have adequate contrast. • Consider further distinguishing between important soft-buttons by using different button shapes, and contrasts. • Do not rely solely on color to distinguish between important system conditions (for example, the operating status of a bilge pump). Colorblind users

may find it difficult to use systems that rely on visual cues based solely on color.

### Best practice: when to provide physical switches

Although well designed touchscreen displays offer intuitive, flexible, and compact switching solutions for multiple vessel systems and equipment, some cases are better implemented with (or supplemented with) physical switches, including NMEA keypads. Consider that touchscreen displays: • lack tactile feedback • are sensitive to accidental touches • can be hard to use in adverse environmental conditions (rain, rough sea state) • can be hard to use when wearing gloves • may require additional touches (for example, using menus and page jumps) to reveal the required control button • may be hard to navigate quickly, especially in emergency situations, or by users unfamiliar with the installation If the user needs to switch systems or equipment in response to urgent conditions, or repeatedly operate a switch while looking away from the touchscreen display, consider providing a physical switch in place of (or in addition to) a soft-button on a touchscreen. Physical switches are also recommended when it is important that the switch location maintains the operator’s line-of-sight with the switched-equipment. Some examples where provision of a physical switch is recommended: • operating the vessel’s horn • operating internal lighting positioned to illuminate bridge controls • operating an emergency stop feature (for example, to immediately stop a moving piece of equipment that is within the switch operator’s line of sight)

### Best practice: use switch-guards for critical circuits

For cases where inadvertent use of a switch could impact the safety of the vessel or its occupants, ensure that the switch is guarded. For example, a switch controlling power to a primary DC bus on the vessel should be guarded to prevent accidental powering down of multiple systems. Similarly, a soft-switch on a touchscreen display that operates a moving item of equipment (such as a powered hatch cover), should be designed with a software guard. For physical switches, install a purpose-built guard (such as an integral flip-cover). For soft-switches on a touchscreen display, consider implementing: • a “long press” feature. For example, enforce a three-second press before a soft-switch signals that AC shore-power is to be connected or disconnected from the vessel’s electrical system. • a confirmation message that the user must acknowledge to complete the action (for example, “Power-off the primary DC bus? <Yes>/<No>). • an access code (PIN code) that the user must enter before gaining access to a soft switch.

<!-- pdf page 20 | printed page 20 -->

### Best practice: use of latched and unlatched switches

The choice of a latched or unlatched (momentary) switch to control a particular system or piece of equipment may have a direct impact on user safety. Always consider the nature of the equipment under control when deciding which type of switch to use: • A latched switch may be appropriate when a continuously closed (or open) switch-state is unlikely to impact user or vessel safety. Note: Remember that a physically latched switch cannot be overridden by other switches within the digital switching system.

- Use an unlatched (momentary) switch for moving equipment that may present an entrapment hazard.

<!-- pdf page 21 | printed page 21 -->

## 4.2 Physical network design and installation

Your digital switching system makes use of a wired SeaTalkng / NMEA 2000-compatible Controller Area Network bus (CAN bus) to transmit switching signals around the vessel. The linear bus topology comprises a central cable (the backbone), with tee-connections and multi-way connectors to CAN-compatible devices (including digital switching components, and multifunction displays). Each end of the backbone is terminated with an appropriate resistor.

Note: *A multifunction display (MFD) cannot be powered from the SeaTalkng backbone and requires a dedicated power supply. Some Raymarine MFDs are 12V and 24V compatible. Refer to the documentation supplied with the MFD.

1. SeaTalkng Instrument (e.g. i60 Wind).
2. DSU (Digital Switching unit / module).
3. Raymarine Wind transducer.
4. Raymarine Depth transducer.
5. Raymarine iTC-5 converter.
6. SeaTalkng backbone.
7. SeaTalkng T-piece.
8. 12V power supply for SeaTalkng backbone.
9. SeaTalkng Instrument (e.g. i50 Depth).
10. Raymarine LightHouse™ Multifunction display (MFD).
11. SeaTalkng spur. The linear nature of the CAN bus means that a break or bad connection in the backbone could degrade or disable a digital switching system. A CAN bus

also has an upper limit to the bandwidth available to distribute messages; if the maximum supported data rate is exceeded, this may result in delayed messages, and unreliable operation. It is therefore important to consider the following best practice recommendations when designing and installing the CAN-bus wiring to support a digital switching system. Best practice in physical network design is not restricted to the CAN bus. Power-circuit design also needs careful consideration, particularly when switching devices that may place an additional strain on components, such as inductive loads.

<!-- figure 1 on pdf page 21 at 41,194-299,485 pt | caption: none | text-layer labels: none | OCR below floor, text not used (9/28 words >= 60, mean confidence 47) -->

<!-- pdf page 22 | printed page 22 -->

### Best practice: install robust CAN-cabling

Ensure that:
- all CAN-bus cables (including the backbone, device drops, and power insertion cables) are securely fixed to the vessel. Excessive play in cable runs can lead to intermittent or broken connections. Similarly, very tight cable runs in situations where some play is required, can also cause connection problems.
- the linear topology of the CAN bus is maintained.

### Best practice: use a CAN network bridge to isolate critical components

For complex digital switching systems comprising a number of digital switching control units, connected via a long central cable (backbone), consider using a CAN network bridge to split the CAN network into multiple independent subnets. CAN subnets must also have separate power connections. When designing a CAN network comprising bridged subnets, consider how best to distribute CAN-compatible devices between the subnets. For example: • multiple digital switching control units could be placed on different subnets • critical systems controlled by digital switching should be placed on a separate subnet from non-critical systems (for example, switching associated with engine monitoring and control on a separate sub-net from all other digital switching components and other components using the CAN bus)

### Best practice: do not exceed CAN bus specifications

Ensure that the following limits are not exceeded for an individual CAN network (or subnet): • maximum of 50 connected CAN devices • maximum 5 m drop (spur) to each CAN device; maximum 30 m total drop (spur) length • maximum 100 m total backbone length Also ensure that: • correct termination is applied to each end of the CAN bus • where possible, power is applied near to the center of the backbone • the CAN bus is not overloaded with data; overloading may result in delayed or unreliable responses from devices See the Raymarine “SeaTalkng Reference Manual” (document no. 81300) for more information about designing a SeaTalkng network.

### Best practice: dealing with inductive loads

Inductive loads may require special handling when incorporated into a digital switching system. Important: Failure to correctly install adequately rated flyback diodes could result in overheating of circuit components, and subsequent fire.

Important: Failure to correctly install adequately rated flyback diodes could result in damage to digital switching modules. Examples of loads which may result in high inductance during switching include: • dc motors (for example, a motor that comprises part of a fan or compressor) • transformers, relays, and coils When removing power from an inductive load, a large reverse-voltage may develop, which has the capacity to cause damage to digital switching modules. In extreme cases, excess reverse voltage may cause overheating of circuit components, and subsequent fire. To enable this reverse-voltage to be dissipated safely, you must install a “flyback” diode in the power circuit for the inductive load. Consider the following points when installing a flyback diode: • position the diode as close as possible to the inductive load • ensure that the diode is suitably specified for the expected reverse-voltage and current, and for the standard power-supply voltage of the circuit in which it will be installed. • if protecting a bi-directional load, use an appropriate diode (the following circuit diagram includes an example for bi-directional loads) • ensure that the diode circuitry is appropriately housed and secured. For example, install the diode securely within a waterproof junction box, to provide adequate environmental protection. The following illustration shows examples of flyback-diode circuits suitable for most uni-directional and bi-directional inductive loads:

<!-- pdf page 23 | printed page 23 -->

| Item | Description |
| --- | --- |
| A | Protection circuit for uni-directional loads |
| B | Protection circuit for bi-directional loads |
| 1 | Inductive load |
| 2 | TVS diode (for 12 V systems, use Littelfuse part number 5KP18A; for 24 V systems, use Littelfuse part number 5KP36A) |
| 3 | Dual TVS diodes (for 12 V systems, use two Littelfuse part number 5KP18A; for 24 V systems, use two Littelfuse part number 5KP36A) |
| 4 | Named digitally switched channel (‘X’ or ‘Y’) |
| 5 | ‘Minus’ connection on digital switching unit |

Note: The diodes specified above will safely dissipate reverse voltages up to 400 V. However, to ensure that the diodes are sufficiently specified for your installation, consult the original equipment manufacturer’s documentation for both the equipment that presents an inductive load, and for the digital switching units.

4.3 System security The best practice recommendations in this section will help you to design appropriate security features into your digital switching system. Digital switching systems facilitate both the concentration of vessel-systems data and control mechanisms (for example, multiple systems on a vessel can be managed using a single MFD screen), and a wider distribution (for example, by using peer-to-peer WiFi between an MFD and a tablet computer, or by providing a GSM SMS text interface to certain vessel systems). Although this concentration and distribution of vessel-systems data and control enables more efficient management and monitoring, you should ensure that your digital switching system is designed such that only authorized personnel can access and use vessel data and control mechanisms. This is particularly important where moving equipment could cause injury if operated improperly.

### Best practice: when to use GSM SMS (text message) control interfaces

Do not implement GSM SMS (text message) control interfaces for equipment whose improper use may compromise the security or safety of the vessel, or of personnel on board. Although GSM SMS text messaging is not inherently insecure, opening up control of critical equipment to a GSM interface without good cause is not recommended. For example, providing a GSM SMS interface to control the opening and closing of a motorized hatch cover, is not advisable. However, using SMS to control selected interior lighting on a vessel would be unlikely to create a safety hazard or security concern; remote control of interior lighting may actually enhance security, by giving the impression that a vessel is occupied.

### Best practice: consider control panel locks

If system control panels (MFDs) are located where non-authorized personnel may be able to access them, ensure that features controlling systems critical to the safety of those on board, and of the vessel, cannot be accessed without providing appropriate authorization. For example, the controls for a safety critical system such as the vessel’s navigation lights, should be locked by a PIN code or password. Note: It is important to balance the security of system controls, with ease-of-use by authorized personnel. For example, where an important system or item of equipment is protected by a control-panel lock because unauthorized users may have physical access to the panel, authorized users should be given unhindered access to control the same system or item of equipment from at least one other, more secure, location.

<!-- pdf page 24 | printed page 24 -->

### Best practice: consider security of switching components

Some of the hardware components of your digital switching system may incorporate physical manual-override switches that can be used to directly control individual circuits. Ensure that these components are positioned in a secure location on the vessel, while maintaining easy access for authorized personnel.

### Best practice: configure strong Wi-Fi passphrases for MFDs

If the RayControl or RayRemote applications will be used to view and remotely control MFD screens, ensure that all MFDs are set up with a strong Wi-Fi passphrase, and WPA2 Wi-Fi security. For advice on choosing a strong passphrase, see the “Wi-Fi sharing settings” topic in the “Lighthouse[TM] Operation Instructions” manual, document no. 81360.

## 4.4 System safety

Digital switching systems enable distributed control and monitoring of vessel electrical systems and equipment. Combined with bespoke touchscreen user interfaces, and additional means of triggering switching operations (for example, using GSM SMS text messages, or via Wi-Fi using smart phone or tablet applications), a digital switching system offers greater ease-of-use and efficiency when compared to a traditional wiring system. However, the flexibility available to designers of digital switching systems must be considered alongside the safety of the vessel and those on board. The following best practice recommendations cover a number of safety features that you should consider when designing a digital switching system.

### Best practice: take extra precautions when switching moving equipment

Electrically controlled moving equipment installed on a vessel presents special safety concerns. In particular, moving equipment has the potential to cause pinching or crushing injury, entrapment of clothing or body parts, and may cause trips or falls. Examples of electrically controlled moving equipment include: • bathing platforms • hatch covers • winches • anchor chains • passerelles (gangways) To mitigate against personal injury caused by moving equipment: • position switches such that users can maintain line-of-sight with the controlled equipment. • install a kill switch or dead-man’s switch in close proximity to the switched equipment, the closing of which is necessary to operate the equipment, irrespective of any other switching signals received. • install audible and visual warning devices (for example, a buzzer and strobe light) that are automatically activated before a piece of equipment starts to move, and during use. • install a safety limit switch (for example, an appropriately positioned micro-switch) to automatically stop equipment that is moved beyond fixed limits. • implement current detection and limiting, to automatically cut power to a moving piece of equipment that has stalled due to a physical obstruction. • never allow electrically powered moving equipment to be activated or controlled at a distance from the vessel, such as via GSM SMS text messages.

<!-- pdf page 25 | printed page 25 -->

### Best practice: configure software fuses for every switched circuit

The switching and control modules that comprise your digital switching system may include software fuses for each switched circuit. Always ensure that the software fuse is correctly configured for each circuit in use; do not leave software fuses set to their default rating, unless the default rating is appropriate for a specific circuit. Failure to configure software fuses correctly may result in damage to the vessel caused by excessive resistive heating, or in extreme cases, fire.

## 4.5 System redundancy and fail-safe design

Digital switching systems are generally very reliable. The reduction in cabling when compared to a traditionally switched system reduces the likelihood that cable connection faults will degrade or disable the control of vessel systems and equipment. However, digital switching systems are not immune to failures, particularly when subject to extreme environmental conditions, such as a nearby lightning strike. Careful and considered design with regard to system redundancy and implementing fail-safe mechanisms, will ensure that your digital switching system is robust, and that rare events are less likely to disable critical vessel systems.

### Best practice: use redundant switching mechanisms for critical systems

Do not rely on a single switching mechanism to control critical vessel systems and equipment. For example, if bridge wipers can be controlled and monitored via soft-switches on a touchscreen display, also provide an appropriate physical switch, wired to a digital switching channel, that offers a degree of bridge-wiper control. If the touchscreen display fails (and no alternative touchscreens are available), or becomes difficult to use due to harsh environmental conditions, a physical switch provides an important backup control.

### Best practice: implement fail-safe mechanisms

The components used to build a digital switching system (for example, switching modules and control modules) may include built-in functionality to provide sensible default switching states, given the failure of the CAN bus (in whole or in part), partial failure of power supply, or failure of other digital switching modules. Ensure that you specify and program appropriate settings for default switching states (often referred to as “limp home” settings), for all critical circuits under the control of the digital switching system.

<!-- pdf page 26 | printed page 26 -->

## 4.6 System performance

To ensure that your digital switching system operates consistently and reliably, certain limitations of the SeaTalkng/NMEA 2000 (CAN bus) network, and Raymarine MFDs should be considered. These limitations concern the bandwidth of the SeaTalkng/NMEA 2000 backbone (that is, the amount of data that can be transferred across the network within a given time), and the maximum memory available to the digital switching application running on Raymarine MFDs.

### Best practice: consider SeaTalkng/NMEA 2000 (CAN bus) bandwidth limitations

The SeaTalkng/NMEA 2000 (CAN bus) backbone is capable of reliably transmitting digital switching data between elements of a complex system at a high rate. However, the rate at which data can be reliably transmitted is not unlimited. In particular, graphical animations on an MFD’s digital switching pages may require a large amount of data to be transmitted across the SeaTalkng/NMEA 2000 network. For example, you may wish to animate the position of a bathing platform, as the platform position changes. To avoid overloading the SeaTalkng/NMEA 2000 network, minimize the number of animated elements in your MFD page designs.

### Best practice: limit configuration file size to 15 MB

Raymarine multifunction displays (MFDs), as used with digital switching systems, are sufficiently powerful to manage complex control systems with many pages and graphic elements. However, to avoid possible performance issues, ensure that configuration files (unzipped) are kept below 15 MB in size. To achieve this, consider: • using compressed image formats for graphic elements (such as PNG or JPG) • resizing large images before importing them into your digital switching project • using 8–bit color rather than 24–bit color for graphic elements Additionally, be sure to check the configuration file size when saving, to confirm that it is less than 15 MB in size.

<!-- pdf page 27 | printed page 27 -->

## 4.7 System testing and commissioning

Having followed best practice for system design, it is important that all components of the digital switching system as implemented, are comprehensively tested. Testing should take place during system build, and also when the vessel is commissioned, to ensure that the digital switching system operates as designed alongside and in conjunction with all other vessel systems. Note: Refer to the international standard IEC 61508 (”Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems”) for comprehensive guidelines on developing systems that comprise electrical, electronic, or programmable electronic components that perform safety functions.

### Best practice: take appropriate precautions when testing

When testing a system, take precautions to prevent unintended injuries to personnel or damage to the vessel. In particular, moving equipment or system components could cause entrapment injuries if they were to move unexpectedly. This could happen if, for example, a connector is incorrectly wired, or an output channel is incorrectly allocated. Precautions to take when testing, include: • ensuring personnel keep clear of moving equipment • checking that the correct output channels are activated as expected before connecting equipment power plugs

### Best practice: perform comprehensive system testing

A comprehensive description of how to test your digital switching system is beyond the scope of this document. However, as a minimum, the following points should be considered: • carefully document all tests and test results, including information about: – when each test was performed – who performed each test – the exact version of the software and firmware installed on system components during testing – the configuration files used during testing • before starting tests or commissioning, ensure that the latest firmware and software is installed on all devices (such as MFDs, and digital switching units); manufacturers may release frequent firmware or software updates to fix issues with components. • test every circuit that is under the control of the digital switching system; ensure that each

switching mechanism operates the equipment or vessel system that it is designed to operate, and only that equipment or vessel system. • comprehensively test all bespoke touchscreen user interfaces. • run tests to simulate the failure of digital switching system components, and of partial power and CAN-bus network failures; ensure that any fail-safe logic designed into the system operates correctly, and maintains adequate control of the vessel’s systems. When commissioning the vessel, you should make suitable user documentation available to the personnel that will be using the digital switching system while operating the vessel. For more complex systems, bespoke user training may also be appropriate.

### Best practice: perform regression tests

Whenever you make any changes to an existing system, always re-test the entire system to ensure that all features and components continue to operate as expected.

<!-- pdf page 28 | printed page 28 -->

## 4.8 System documentation and backups

Although a digital switching system can greatly reduce the complexity and amount of cabling required compared to an equivalent traditionally switched system, it is still important to document the design of each installed system. System documentation, copies of which should be stored on the vessel, can be invaluable when troubleshooting switching problems, or when modifying and upgrading a system.

Best practice: provide comprehensive system documentation Digital switching systems comprise numerous components, in addition to the items of equipment or vessel systems that are being switched. To aid troubleshooting and upgrades, document the following: • CAN-bus cabling, including the connectivity and locations of the main backbone, terminators, tee-pieces and adapters, drops (spurs), power connections, and CAN-compatible units. Create circuit diagrams as appropriate. • Connections (both power cables, and CAN-bus cables) between all digital switching system components (such as switching modules, and control modules), switched equipment and vessel systems. Create circuit diagrams as appropriate. • Switching-channel data (listing, for example, switching-module channel numbers, along with channel functions, associated touchscreen display switches and indicators, software-fuse settings, and fail-safe fallback settings). Much of this documentation can be based on the initial design documents for a digital switching system. Consider making documentation available electronically, as well as providing physical printed copies. For example, help materials could be built into the digital switching MFD pages, providing contextual help.

### Best practice: keep system documentation up to date

Whenever you make changes to a digital switching system, always update the system documentation to keep it in-line with the changes.

### Best practice: provide contextual labelling and emergency instructions

In a troubleshooting scenario, clear and comprehensive labeling of physical components can be of great assistance. Contextual labeling (physical labels applied directly to, or adjacent to, system components) supplements separate system documentation, and will make troubleshooting less prone to error, and more efficient.

Where space is limited, or individual labeling of switching-channel connections is inconvenient, provide a comprehensive list of switching-channel data on a separate sheet, and affix this adjacent to the relevant digital switching modules. Direct tagging and labeling of individual cables will also assist when troubleshooting or upgrading a system. In the unlikely case that a digital switching system suffers a major failure while the vessel is at sea, provision of emergency operation instructions and checklists will be of great benefit. This material should always be available on the vessel, and focused on operating the most critical vessel systems in the event that digital switching components are not working correctly (for example, navigation lights, communication systems, and engine control and monitoring).

### Best practice: create system backups, and manage software changes

In addition to the physical hardware and cabling, your digital switching system may include configuration files and software (for example, specific versions of firmware) that are essential for the correct operation of the system. It is important that any required configuration files and additional software are backed-up to a safe location, and that any changes are carefully managed. Maintaining backups and managing changes to configuration files and software will be helpful when recovering or troubleshooting a digital switching system, or if re-installation is required.

<!-- pdf page 29 | printed page 29 -->

## Chapter 5: References

### Chapter contents

- 5.1 References on page 30

References                        29

<!-- pdf page 30 | printed page 30 -->

## 5.1 References

- “Digital Switching: Raymarine Terms of Use” (Raymarine document no. 80018)
- “Functional Safety of Electrical / Electronic / Programmable Electronic Safety-related Systems” (IEC 61508)
- “SeaTalkng Reference Manual” (Raymarine document no. 81300)
- “Lighthouse 17 MFD Operation instructions” (document no. 81360)
- “NMEA 2000 Standard” (Edition 3.101, March 2016)

<!-- pdf page 31 -->

(no text layer on this page)

<!-- pdf page 32 -->

## www.raymarine.com

- Raymarine UK Limited, Marine House, Cartwright Drive, Fareham, PO15 5RJ. United Kingdom.
- Tel: +44 (0)1329 246 700

<!-- figure 1 on pdf page 32 at 141,348-447,425 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 2/3 words >= 60, mean confidence 56) -->
Raymarine
OFLIR
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 32 at 258,626-335,703 pt | caption: none; nearest centred text below: "www.raymarine.com" | text-layer labels: none | OCR: no legible text (0/3 words >= 60, mean confidence 16) -->
