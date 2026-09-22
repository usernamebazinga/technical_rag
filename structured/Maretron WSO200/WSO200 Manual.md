# WSO200 Ultrasonic Weather Station User's Manual

<!-- source: sources/Maretron WSO200/WSO200 Manual.pdf | extraction: extracted/Maretron WSO200/WSO200 Manual.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- font check: SymbolMT is not a standard text face; glyphs "•" on pages 5-6, 9, 11-12. Verify against the rendered page before trusting or mapping. -->
<!-- font check: no ToUnicode map in Arial-BoldItalicMT, Arial-BoldMT, Arial-ItalicMT, ArialMT, ArialNarrow, ArialNarrow-Bold, Calibri, CourierNewPSMT; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1-21 checked against the rendered page) -->

<!-- pdf page 1 | printed page i -->

## WSO200

## Ultrasonic Wind / Weather Station

## User’s Manual

#### Revision 1.0

Copyright © 2023 Carling Technologies, Inc. All Rights Reserved

Maretron, a Littelfuse Brand 120 Intracoastal Pointe Dr. Jupiter FL 33477 USA http://www.maretron.com

Revision 1.0                                                                Page i

<!-- pdf page 2 | printed page ii | header: WSO200 User’s Manual -->

## WSO200 User’s Manual

## Revision History

| Revision | Description |
| --- | --- |
| 1.0    Original document. |  |
| Page ii | Revision 1.0 |

<!-- pdf page 3 | printed page iii -->

Table of Contents

## Table of Figures

## Table of Appendices

Appendix A – NMEA 2000 Interfacing ..................................................................................... A1

Revision 1.0                                                                                                                     Page iii

<!-- pdf page 4 | printed page iv | header: WSO200 User’s Manual -->

This page intentionally left blank.

Page iv                                         Revision 1.0

<!-- pdf page 5 | printed page 1 -->

## 1 Introduction

Congratulations on your purchase of the Maretron WSO200 Ultrasonic Wind / Weather Station. Maretron has designed and built your WSO200 to the highest standards for years of reliable, dependable, and accurate service.

The Maretron WSO200 is designed to operate within the harsh demands of the marine environment. However, no piece of marine electronic equipment can function properly unless installed and maintained in the correct manner. Please read carefully and follow these instructions for installation and usage of the Maretron WSO200 in order to ensure optimal performance.

### 1.1 Firmware Revision

This manual corresponds to WSO200 firmware revision 1.0.x         .

### 1.2 WSO200 Features

The Maretron WSO200 has the following features.

| • | NMEA 2000® Interface |
| --- | --- |
| • | Ultrasonic Wind Sensor |
| • | Field Replaceable Relative Humidity Sensor |
| • | Barometric Pressure Sensor |
| • | Temperature Sensor |
| • | Waterproof Enclosure and Cable System |

## 2 Installation

### 2.1 Unpacking the Box

When unpacking the box containing the Maretron WSO200, you should find the following items:

1 - WSO200 Ultrasonic Wind/Weather Station 1 - Pole Mount Base 3 - Mounting Screws and Lock Washers 1 - WSO200 User’s Manual 1 - Warranty Registration Card

If any of these items are missing or damaged, please contact Maretron.

### 2.2 Choosing a Mounting Location

The selection of a suitable mounting location is important for the optimal performance of the Maretron WSO200. The mounting location and orientation of the WSO200 should be:

1. Level with the earth’s horizontal plane – This gives the WSO200 wind/weather sensor the best accuracy of wind speed and direction over the widest range of heel angles.

<!-- pdf page 6 | printed page 2 | header: WSO200 User’s Manual -->

2. High Enough to have a clear view of the sky to the horizon in all directions unblocked by sails or boat structures – The WSO200 provides the best readings when wind through it is unimpeded by sails or structures on the boat.

### 2.3 Mounting the WSO200

The Maretron WSO200 can be mounted on top of a 1” 14 threads per inch standard marine pole mount (Section 2.3.1).

#### 2.3.1 Mounting the WSO200 to a Standard Marine Pole Mount

Screw the included WSO200 mounting bracket to the standard marine pole mount. If you do not have a device capable of configuring installation offset in the WSO200, ensure that the pole mount is oriented as follows: the pole mount base has three small holes for mounting screws and one larger hole for the humidity sensor. Ensure that the small (mounting screw) hole which is nearest the larger (humidity sensor) hole is oriented such that it faces directly forward in the vessel. If you do have a device capable of configuring installation offset in the WSO200, you may mount the sensor in any orientation and adjust for it by configuring the installation offset appropriately (please refer to the display user’s manual for details).

Route the NMEA 2000® cable through the standard marine pole mount and the pole mount base and connect it to the WSO200 unit (see Section 2.4 below). Finally, attach the WSO200 to the pole mount base using the included brass mounting screws and lock washers as shown in Figure 1. Do not use threadlocking compounds containing methacrylate ester, such as Loctite Red (271), as they will cause stress cracking of the plastic enclosure.

WARNING
- When installing the WSO200 to a standard marine pole mount, be sure to first screw the WSO200 mounting bracket to the pole mount. Then, attach the WSO200 to the WSO200 mounting bracket with the three screws which connect these two components. DO NOT first attach the WSO200 mounting bracket to the WSO200 with the three screws and then screw the entire assembly onto the pole mount. Doing this will put excessive torque on the NMEA 2000 connector from the attached cable and cause damage to the connector which is not covered under the product warranty.
- Likewise, when uninstalling the WSO200 from a standard marine pole mount, be sure to first remove the three screws attaching the WSO200 to the WSO200 mounting bracket. DO NOT first unscrew the entire assembly from the pole mount before removing the three screws. Doing this will put excessive torque on the NMEA 2000 connector from the attached cable and cause damage to the connector, which is not covered under the product warranty.

<!-- figure 1 on pdf page 6 at 58,418-559,667 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 7 | printed page 3 -->

Humidity Sensor

® NMEA 2000 Cable

Sensor

Orient pole mount base so that this hole will face forward

Standard Marine Pole Mount

Figure 1 – Mounting the WSO200 to a Standard Marine Pole Mount

<!-- figure 1 on pdf page 7 at 178,86-485,631 pt | caption: "Figure 1 – Mounting the WSO200 to a Standard Marine Pole Mount" | text-layer labels: Standard Marine Pole Mount | nearby labels: ® | Lock Washer | Mounting Screw | OCR: no legible text (0/2 words >= 60, mean confidence 30) -->

<!-- pdf page 8 | printed page 4 | header: WSO200 User’s Manual -->

### 2.4 Connecting the WSO200

The Maretron WSO200 provides a connection to an NMEA 2000® interface through a connector that can be found on the bottom of the device (see Figure 2).

The NMEA 2000® connector is a five-pin male connector (see Figure 3). You connect the WSO200 to an NMEA 2000® network using a Maretron NMEA 2000® cable (or compatible cable) by connecting the female end of the cable to the WSO200 (note the key on the male connector and keyway on the female connector). Be sure the cable is connected securely and that the collar on the cable connector is tightened firmly. Connect the other end of the cable (male) to the NMEA 2000® network in the same manner. The WSO200 is designed such that you can plug or unplug it from an NMEA 2000® network while the power to the network is connected or disconnected. Please follow recommended practices for installing NMEA 2000 ® network products.

Figure 3 – NMEA 2000® Connector Face Views

<!-- figure 1 on pdf page 8 at 228,137-384,281 pt | caption: "Figure 2 – WSO200 Interface Connector" | text-layer labels: none | nearby labels: Figure 2 – WSO200 Interface Connector | OCR: no legible text (0/5 words >= 60, mean confidence 23) -->

<!-- figure 2 on pdf page 8 at 139,461-470,578 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 10/10 words >= 60, mean confidence 96) -->
Pins
Sockets
Connector Threads
Connector Threads
Male Connector
Female Connector
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 8 at 214,588-401,655 pt | caption: "Figure 3 – NMEA 2000 ® Connector Face Views" | text-layer labels: none | OCR text follows (tesseract, unverified; 20/20 words >= 60, mean confidence 94) -->
Shield
Pin
NET-S, (power supply positive, +V)
Pin
NET-C, (power supply common, -V)
Pin
NET-H, (CAN-H)
Pin
NET-L, (CAN-L)
Pin
<!-- end of figure 3 -->

<!-- pdf page 9 | printed page 5 -->

#### 2.4.1 Checking Connections

Once the NMEA 2000® connection to the Maretron WSO200 has been completed, check to see that wind speed information is being properly transmitted by observing an appropriate display. Refer to Section 5, “Troubleshooting”, if no heading information appears.

### 2.5 Configuring the WSO200

The WSO200 has several configurable parameters, which are shown in the following sections. If you are not using the default values, then you will need to refer to the corresponding section for configuring the WSO200 appropriately.

The WSO200 can be configured in any of the following ways:
- DSM410 Multifunction Display
- DSM570 Multifunction Display
- N2KAnalyzer Network Analysis / Configuration Software. This will require a Windows PC and one of the following: o USB100 NMEA 2000/USB Gateway, or o IPG100 Internet Protocol Gateway

#### 2.5.1 Device Label

Program this parameter with a text string which identifies this device. Maretron display products will display this label text when you are selecting data to display.

#### 2.5.2 Installation Offset Calibration

You may compensate the wind direction readings transmitted by the WSO200 in order to create a 0° apparent wind direction when the wind is blowing directly onto the bow of the boat. This compensates for installations where the WSO200 is not aligned exactly with the boat’s centerline.

#### 2.5.3 Wind Data Damping Period

You may adjust the damping that the WSO200 applies to transmitted wind speed and direction readings. The WSO200 comes from the factory preset with a damping period of 1.5 seconds, which should be appropriate for most applications. However, you may tune the damping period to anywhere between 0.1 seconds and 5.0 seconds if you desire.

#### 2.5.4 Barometric Pressure Offset Calibration

If you wish to apply an offset to the barometric pressure reported by the WSO200, you may change the barometric pressure to match the value you wish displayed, which will create and apply an offset to future barometric pressure readings.

#### 2.5.5 Outside Humidity Offset Calibration

If you wish to apply an offset to the humidity reported by the WSO200, you may change the humidity to match the value you wish displayed, which will create and apply an offset to future humidity readings.

<!-- pdf page 10 | printed page 6 | header: WSO200 User’s Manual -->

#### 2.5.6 Outside Temperature Offset Calibration

If you wish to apply an offset to the temperature reported by the WSO200, you may change the temperature to match the value you wish displayed, which will create and apply an offset to future temperature readings.

#### 2.5.7 Advanced Configuration…

Certain parameters do not normally need to be set for normal operation but are included in an advanced configuration section for use in special situations.

#### 2.5.7.1 Device Instance Configuration

This entry allows you to program the NMEA 2000 device instance for the unit. You usually will not need to modify the default value of “0” unless you have multiple units on the network. Device instance is always used in the Wind PGNs.

#### 2.5.7.2 Instance – Humidity Configuration

This entry allows you to program the NMEA 2000 device instance for the humidity transmitted in PGN 130313. You usually will not need to modify the default value of “0” unless you have multiple humidity sensors on the network.

#### 2.5.7.3 Instance – Pressure Configuration

This entry allows you to program the NMEA 2000 device instance for the air pressure transmitted in PGN 130314. You usually will not need to modify the default value of “0” unless you have multiple pressure sensors on the network.

#### 2.5.7.4 Instance – Temperature Configuration

This entry allows you to program the NMEA 2000 device instance for the temperature transmitted in PGN 130312. You usually will not need to modify the default value of “0” unless you have multiple temperature sensors on the network. Note that the TMP100 module also generates these PGNs.

#### 2.5.7.5 Installation Description Configuration

The WSO200, along with all other certified NMEA 2000 devices, has two user-programmable installation description fields. You may program these fields with information specific to the device, such as date installed, the initials/name of the installer, the physical location of the device, etc. This configuration option will allow you to program the values of these fields.

#### 2.5.7.6 NMEA 2000 PGN Enable/Disable Configuration

The WSO200 is capable of transmitting NMEA 2000® messages. You may individually enable or disable each of these messages. You may also change the rate of transmission of each of these messages if desired.

#### 2.5.7.7 Restore Factory Defaults

Selecting this configuration option causes all stored parameters in the WSO200 to be reset to the values they contained when the unit was manufactured.

<!-- pdf page 11 | printed page 7 -->

## 3 Operation

As shipped from the factory, the WSO200 automatically provides apparent wind direction, apparent wind speed, outside air temperature, relative humidity, and barometric pressure and requires no user configuration. However, some of the WSO200 parameters are user configurable as described below:

- Installation Offset – As shipped from the factory, the WSO200 will read 0° apparent wind direction when the wind blows into the sensor directly from the direction of the post nearest the black humidity sensor that protrudes from the bottom of the sensor. If the WSO200 is mounted with this post facing directly towards the bow of the boat, no adjustment is necessary; however, if the sensor is mounted in any other orientation, the installation offset can be used to compensate the apparent wind direction reading such that it will read 0° when the apparent wind is blowing directly into the bow of the vessel.
- Wind Speed Damping Period – As shipped from the factory, the WSO200 uses a damping period of 1.5 seconds to filter short-term variations in wind speed and direction and provide a more stable, usable output. This damping period can be changed by the user to increase or decrease the amount of filtering.
- Periodic Rate of Transmission – As shipped from the factory, the WSO200 transmits PGNs at a periodic rate. Alternatively, a PGN can be disabled by programming its periodic rate to zero.

Users with direct access to the NMEA 2000® interface may configure these parameters directly through the NMEA 2000® interface. Please refer to Appendix A for a description of the NMEA 2000® messages used to configure these parameters.

### 3.1 Ultrasonic Wind Speed Sensing

The wind speed measurement portion of the WSO200 consists of three sets of ultrasonic transducers spaced equally around a horizontally-aligned circle.

The wind speed is measured by measuring the time of flight of an ultrasonic sound pulse generated by one set of sensors and received by the other two sets of sensors. Each of the three sets of sensors takes a turn at being the transmitter, which the remaining two sensors receive the pulse. Wind blowing in the direction of flight of a pulse increases the speed of the pulse by the amount of the wind speed. Measuring the time of flight in both directions between a given pair of transducers allows the speed of sound to be cancelled out of the calculation, making the wind speed computation independent of air temperature and relative humidity.

The ultrasonic transducers are robust, yet sensitive instruments. The transducers themselves must be kept free of any coating, such as paint. The WSO200 unit itself, especially the area between the transducers, must be kept clean and free of debris for maximum wind speed and direction accuracy.

<!-- pdf page 12 | printed page 8 | header: WSO200 User’s Manual -->

## 4 Maintenance

- Regular maintenance is important to ensure continued proper operation of the Maretron
- WSO200. Perform the following tasks periodically:

| • | Clean the unit with a soft cloth. Do not use chemical cleaners as they may remove paint or markings or may corrode the WSO200 enclosure or seals. Do not use any cleaners containing acetone, as they will deteriorate the plastic enclosure. Any spider webs, etc. that accumulate inside the open portion of the WSO200 may be cleaned out with a water spray. |
| --- | --- |
| • | Ensure that the unit is mounted securely and cannot be moved relative to the mounting surface. If the unit is loose, tighten the mounting screws. |
| • | Check the security of the cable connected to the NMEA 2000® interface and tighten if necessary. |

### 4.1 Replacing the Humidity Sensor

After extended service in an ocean environment, the humidity sensor may need to be replaced.

<!-- pdf page 13 | printed page 9 -->

Humidity Sensor Cover / Humidity Sensor PCBA Screws                                          Assembly Humidity Sensor O-ring

Humidity Sensor Recess

Figure 4 - Replacing the Humidity Sensor Please follow these steps to replace the humidity sensor: 1. Remove the two screws holding the existing humidity sensor in place. 2. Remove the existing humidity sensor by grasping the tab on the humidity sensor holder and pulling straight up. 3. Remove the humidity sensor O-ring. 4. Snap the new humidity sensor PCBA into the humidity sensor holder. Please note that the PCBA and the humidity sensor holder are keyed, so that there is only one way to snap them together. 5. Place the new humidity sensor O-ring into the humidity sensor recess on the bottom of the WSO200, centering it on the raised rib. 6. Plug the assembled humidity sensor cover and humidity sensor PCBA into the humidity sensor recess on the bottom of the WSO200 until it is completely seated. Please ensure that the pins on the humidity sensor PCBA plug into the connector inside the WSO200. Also, please note that the humidity sensor cover is keyed so that there is only one way to plug it in. 7. Place the two screws into the screw holes in the humidity sensor and tighten until snug.

<!-- figure 1 on pdf page 13 at 149,86-485,451 pt | caption: "Figure 4 - Replacing the Humidity Sensor" | text-layer labels: none | nearby labels: Figure 4 - Replacing the Humidity Sensor | OCR: no legible text (0/5 words >= 60, mean confidence 35) -->

<!-- pdf page 14 | printed page 10 | header: WSO200 User’s Manual -->

## 5 Troubleshooting

If you notice unexpected operation of the Maretron WSO200, follow the troubleshooting procedures in this section to remedy simple problems.

| Symptom | Troubleshooting Procedure |
| --- | --- |
| No data output | Check the connections to the NMEA 2000® connector and tighten if necessary |

Ensure that power is supplied to the connected NMEA 2000® cable Incorrect wind direction or speed          Ensure that the flow of wind into the WSO200 is not blocked by surrounding structures.

Ensure that the flow of wind through the WSO200 is unimpeded and that the unit is free of debris. Incorrect humidity reading                 Check that a humidity offset value has not been configured

Replace the humidity sensor

If these steps do not solve your problem, please contact Maretron Technical Support (refer to Section 7 for contact information).

Warning: There are no user-serviceable components inside the Maretron WSO200. Opening the WSO200 will expose the sensitive electronic components to adverse environmental conditions that may render the unit inoperative. Please do not open the WSO200, as this will automatically void the warranty. If service is required, please return the unit to an authorized Maretron service location.

<!-- figure 1 on pdf page 14 at 468,137-530,391 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 96) -->
NMEA
<!-- end of figure 1 -->

<!-- pdf page 15 | printed page 11 -->

## 6 Technical Specifications

Specifications

| Parameter | Value                              Comment |
| --- | --- |
| Wind Speed Range | 0.5 to 99 knots (1 to 185 kph) |
| Wind Speed Resolution | 0.1 knot (0.19 kph) |
| Wind Speed Accuracy                ± 10% or 1 knot (1.9 Tilt 0° (operates to 30° tilt) | kph) |
| Wind Direction Accuracy | ± 5°       Tilt 0° (operates to 30° tilt) |
| Temperature Range | -25° to 55° C |
| Temperature Resolution | 0.18°F (0.1°C) |
| Temperature Accuracy | ±1.8°F (1° C) |
| Relative Humidity Range | 0-99% RH |
| Relative Humidity Resolution | 1% RH |
| Relative Humidity Accuracy | ± 4% RH |
| Barometric Pressure Range | 26 to 32” Hg (880 to 1080 mb) |
| Barometric Pressure Resolution        0.03” Hg (1 mb) |  |
| Barometric Pressure Accuracy | ±0.09” Hg (±3 mb) |

##### Certifications

| Parameter | Comment |
| --- | --- |
| NMEA 2000 | Certified |
| Maritime Navigation and Radiocommunication Equipment & Systems | IEC 61162-3 |
| Maritime Navigation and Radiocommunication Equipment & Systems | IEC 60945 |
| FCC and CE Mark | Electromagnetic Compatibility |

##### NMEA 2000® Parameter Group Numbers (PGNs) - See Appendix A for Details

| Description | PGN # | PGN Name | Default Rate |
| --- | --- | --- | --- |
| Periodic Data PGNs | 130306 130310 130311 130312 130313 130314 | Wind Data                                      10 Times/Second Environmental Parameters Environmental Parameters Temperature Humidity Actual Pressure | 2 Times/Second 2 Times/Second 2 Times/Second 2 Times/Second 2 Times/Second |
| Response to Requested PGNs | 126464 126996 126998 | PGN List (Transmit and Receive) Product Information Configuration Information | N/A N/A N/A |
| Protocol PGNs | 059392 059904 060416 060160 060928 065240 126208 | ISO Acknowledge ISO Request ISO Transport Protocol, Connection Management ISO Transport Protocol, Data Transfer                 N/A ISO Address Claim ISO Address Command NMEA Complex Request/Command/Ack. | N/A N/A N/A N/A N/A N/A |
| Maretron Proprietary PGNs | 126720 | Configuration | N/A |

<!-- figure 1 on pdf page 15 at 163,108-214,314 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 15 at 466,108-559,314 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 15 at 158,434-202,509 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 15 at 127,530-202,660 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 15 at 442,590-499,660 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 16 | printed page 12 | header: WSO200 User’s Manual -->

##### Electrical

| Parameter | Value | Comment |
| --- | --- | --- |
| Operating Voltage | 9 to 32 Volts | DC Voltage |
| Power Consumption | <50mA | Average Current Drain |
| Load Equivalence Number (LEN) | 1 | NMEA 2000® Spec. (1LEN = 50 mA) |
| Reverse Battery Protection | Yes | Indefinitely |
| Load Dump Protection | Yes | Energy Rated per SAE J1113 |

##### Mechanical

Parameter                         Value                               Comment Size                                 5.91” Diameter x 4.85” Tall Including Mounting Bracket (150mm Dia. x 123.2mm Tall) Weight                                     10 oz. (283 g)        Including Mounting Bracket Mounting                                        Pole             Fits 1”-14 TPI Standard Marine Mount

##### Environmental

| Parameter | Value |
| --- | --- |
| IEC 60945 Classification | Exposed |
| Degree of Protection | IP67 |
| Operating Temperature | -25°C to 55°C |
| Storage Temperature | -40°C to 70°C |
| Relative Humidity | 93%RH @40° per IEC60945-8.2 |
| Vibration | 2-13.2Hz @ ±1mm, 13.2-100Hz @ 7m/s2 per IEC 60945-8.7 |
| Rain and Spray | 12.5mm Nozzle @ 100liters/min from 3m for 30min per IEC 60945-8.8 |
| Solar Radiation | Ultraviolet B, A, Visible, and Infrared per IEC 60945-8.10 |
| Corrosion (Salt Mist)           4 times 7days @ 40°C, 95%RH after 2 hour Salt Spray Per IEC 60945-8.12 |  |
| Electromagnetic Emission | Conducted and Radiated Emission per IEC 60945-9 |
| Electromagnetic Immunity | Conducted, Radiated, Supply, and ESD per IEC 60945-10 |
| Safety Precautions               Dangerous Voltage, Electromagnetic Radio Frequency per IEC 60945-12 |  |

## 7 Technical Support

- If you require technical support for Maretron products, you can reach us in one of the following
- ways:

| Telephone: | +1-602-861-1707 |
| --- | --- |
| Toll-Free: | +1-866-550-9100 |
| Fax: | +1-602-861-1777 |
| E-mail: | ct_marinesupport@littelfuse.com |
| World Wide Web: | http://www.maretron.com |
| Mail: | Maretron, a Littelfuse Brand Attn: Technical Support 120 Intracoastal Pointe Dr. Jupiter, FL 33477 |

<!-- figure 1 on pdf page 16 at 209,84-262,161 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 17 | printed page 13 -->

<!-- omitted: "8 Maretron (2 Year) Limited Warranty" (pdf pages 17-19; 8 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 18 | printed page 14 | header: WSO200 User’s Manual -->
<!-- pdf page 19 -->
## Appendix A – NMEA 2000® Interfacing

#### WSO200 NMEA 2000® Periodic Data Transmitted PGNs

PGN 130306 – Wind Data The WSO200 uses this PGN to provide a regular transmission of apparent wind speed and direction data. The factory default for periodic transmission rate is ten times per second. The transmission of this PGN can be disabled (see PGN 126208 – NMEA Request Group Function – Transmission Periodic Rate). Field 1: SID – The sequence identifier field is used to tie related PGNs together. For example, the WSO200 will transmit identical SIDs for 130306 (Wind Data) and 130311 (Environmental Parameters) to indicate that the readings are linked together (i.e., the data from each PGN was taken at the same time although they are reported at slightly different times). 2: Wind Speed – This field is used to indicate the wind speed in units of 10mm/second. 3: Wind Direction – This field is used to indicate the wind direction in units of 0.0001 radians/second. 4: Wind Reference – This field is set to a value of 0x02 to indicate that the wind reading is an apparent wind speed and direction. 5: Reserved (21 bits) – This field is reserved by NMEA; therefore, this field always contains a value of 0x1FFFFF (the WSO200 sets all reserved bits to a logic 1)

PGN 130311 – Environmental Parameters The WSO200 uses this PGN to provide a regular transmission of outside temperature, relative humidity, and atmospheric pressure. The factory default for periodic transmission rate is twice per second. The transmission of this PGN can be disabled (see PGN 126208 – NMEA Request Group Function – Transmission Periodic Rate). Field 1: SID – The sequence identifier field is used to tie related PGNs together. For example, the WSO200 will transmit identical SIDs for 130306 (Wind Data) and 130311 (Environmental Parameters) to indicate that the readings are linked together (i.e., the data from each PGN was taken at the same time although they are reported at slightly different times). 2: Temperature Instance – The WSO200 sets this field to a value of 0x01 to indicate that the temperature reading is a reading of outside temperature. 3: Humidity Instance – The WSO200 sets this field to a value of 0x01 to indicate that the relative humidity reading is a reading of outside humidity. 4: Temperature – This field is used to indicate the outside air temperature in units of 0.01°K. 5: Humidity – This field is used to indicate the relative humidity in units of 0.004%. 6: Atmospheric Pressure – This field is used to indicate the barometric pressure in units of 100 Pa.

PGN 130312 – Temperature The WSO200 uses this PGN to provide a regular transmission of outside temperature. The factory default for periodic transmission rate is disabled. The transmission of this PGN can be enabled (see PGN 126208 – NMEA Request Group Function – Transmission Periodic Rate).

<!-- pdf page 20 | header: WSO200 User’s Manual -->

Field 1: SID – The sequence identifier field is used to tie related PGNs together. For example, the WSO200 will transmit identical SIDs for 130306 (Wind Data) and 130311 (Environmental Parameters) to indicate that the readings are linked together (i.e., the data from each PGN was taken at the same time although they are reported at slightly different times). 2: Temperature Instance – This field is used to distinguish the temperature reading from this device from those of other devices. The value of this field is user-programmable. 3: Temperature Source – The WSO200 sets this field to a value of 0x01 to indicate that the temperature reading is a reading of outside temperature. 4: Actual Temperature – This field is used to indicate the outside air temperature in units of 0.01°K. 5: Set Temperature – This field is not used by the WSO200 and is set to a value of “Data Not Available”. 6: Reserved

PGN 130313 – Humidity The WSO200 uses this PGN to provide a regular transmission of outside humidity. The factory default for periodic transmission rate is disabled. The transmission of this PGN can be enabled (see PGN 126208 – NMEA Request Group Function – Transmission Periodic Rate). Field 1: SID – The sequence identifier field is used to tie related PGNs together. For example, the WSO200 will transmit identical SIDs for 130306 (Wind Data) and 130311 (Environmental Parameters) to indicate that the readings are linked together (i.e., the data from each PGN was taken at the same time although they are reported at slightly different times). 2: Humidity Instance – This field is used to distinguish the humidity reading from this device from those of other devices. The value of this field is user-programmable. 3: Humidity Source – The WSO200 sets this field to a value of 0x01 to indicate that the temperature reading is a reading of outside humidity. 4: Actual Humidity – This field is used to indicate the outside humidity in units of 0.004%. 5: Set Humidity – This field is not used by the WSO200 and is set to a value of “Data Not Available”. 6: Reserved

PGN 130313 – Actual Pressure The WSO200 uses this PGN to provide a regular transmission of atmospheric pressure. The factory default for periodic transmission rate is disabled. The transmission of this PGN can be enabled (see PGN 126208 – NMEA Request Group Function – Transmission Periodic Rate). Field 1: SID – The sequence identifier field is used to tie related PGNs together. For example, the WSO200 will transmit identical SIDs for 130306 (Wind Data) and 130311 (Environmental Parameters) to indicate that the readings are linked together (i.e., the data from each PGN was taken at the same time although they are reported at slightly different times). 2: Pressure Instance – This field is used to distinguish the pressure reading from this device from those of other devices. The value of this field is user-programmable. 3: Pressure Source – The WSO200 sets this field to a value of 0x00 to indicate that the temperature reading is a reading of atmospheric pressure.

<!-- pdf page 21 -->

4: Pressure– This field is used to indicate the atmospheric pressure in units of 0.1Pa. 5: Set Humidity – This field is not used by the WSO200 and is set to a value of “Data Not Available”. 6: Reserved
