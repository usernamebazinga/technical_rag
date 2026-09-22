# WSO200

<!-- source: sources/Maretron WSO200/WSO200 Datasheet.pdf | extraction: extracted/Maretron WSO200/WSO200 Datasheet.md | structured by tools/structure.py; every line can be checked in the extraction -->

<!-- pdf page 1 | printed page 1 -->

WSO200

## Ultrasonic Wind and Weather Station

| The second generation WSO200 is a marine grade ultrasonic weather sta- | The WSO200 provides these |
| --- | --- |
| tion that accurately measures wind speed and direction, air temperature, | functions: |
| barometric pressure, relative humidity, wind chill factor, heat index, and dew | • Apparent Wind Speed |
| points. The wind measurement is calculated using six ultrasonic sensors in |  |
| delta configuration, which means there are no moving parts to wear out or | • Apparent Wind Direction |
| to get caught in the rigging. Unlike mechanical anemometers and weather | • Atmospheric Pressure |
| measuring devices, the WSO200 is not affected by the common issues such | • Air Temperature |
| as bearing wear, salt and dirt build-up, or bird perching that can all result in | • Relative Humidity |

failure or data inaccuracy.

Precise wind speed and direction is easily achieved under tilt of up to 30°, as

## Second Generation Enhancements:

| can be the case with heeled sailboats or powerboats operating in pitching and | • User Replaceable Humidity Sensor |
| --- | --- |
| rolling seas. This makes the new Maretron weather station a gamechanger for | • Higher Signal to Noise Ratio |
| recreational boaters. | • Lower Power Consumption |

The WSO200 is NMEA 2000® certified. When combined with a Maretron DSM Series or dedicated TSM Series display or any device running N2KView® V3 software, all data is visible on the NMEA 2000 network for a truly plug and play experience. Add a Maretron depth, speed & temperature triducer (DST110), a Maretron GPS receiver (GPS200), and a Maretron compass (SSC300) to view true vessel referenced wind speed and direction as well as ground referenced speed and direction.

## The WSO200 mounts on a 1”-14 Standard Marine Mount and is waterproof to IP67 standards.

## NEW!

## PRODUCTS

| PART NUMBER | DESCRIPTION |
| --- | --- |
| WSO200 | Ultrasonic Wind/Weather Station |

### DSM410 & DSM570 Screen Shots

### N2KView Environment Screen

### ct_marinesales@littelfuse.com | www.maretron.com 1

<!-- figure 1 on pdf page 1 at 418,350-554,456 pt | caption: none | text-layer labels: none | nearby labels: • Lower Power Consumption | OCR text follows (tesseract, unverified; 14/14 words >= 60, mean confidence 96) -->
Apparent
Wind
30
30
60
60
90
90
120
120,
150
150
180
Knots
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 1 at 418,461-554,564 pt | caption: none; nearest centred text below: "DSM410 & DSM570 Screen Shots" | text-layer labels: none | nearby labels: DSM410 & DSM570 Screen Shots | OCR below floor, text not used (4/10 words >= 60, mean confidence 36) -->

<!-- figure 3 on pdf page 1 at 48,480-202,588 pt | caption: none | text-layer labels: NEW! | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 1 at 216,492-298,557 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 85) -->
2022
Best New
Product
<!-- end of figure 4 -->

<!-- figure 5 on pdf page 1 at 418,590-557,694 pt | caption: none; nearest centred text below: "N2KView Environment Screen" | text-layer labels: none | nearby labels: DSM410 & DSM570 Screen Shots | N2KView Environment Screen | OCR text follows (tesseract, unverified; 12/21 words >= 60, mean confidence 66) -->
N
2991
86°
57%
72°
21%
84°
03:55
04 24 05
04:48
<!-- end of figure 5 -->

<!-- figure 6 on pdf page 1 at 74,595-233,694 pt | caption: none | text-layer labels: none | nearby labels: PRODUCTS | OCR below floor, text not used (5/15 words >= 60, mean confidence 50) -->

<!-- figure 7 on pdf page 1 at 250,602-362,689 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 2 | printed page 2 -->

<!-- sub/superscripts on this page (from font sizes): 7m/s^2 -->

## SPECIFICATIONS

| PARAMETER | VALUE		                        COMMENT |
| --- | --- |
| Wind Speed Range | 0 to 99 knots (1 to 185 kph) |
| Wind Speed Resolution | 0.1 knot (0.19 kph) |
| Wind Speed Accuracy | +/-10% or 1 knot (1.9kph)		 Tilt 0° (operates to 30° tilt) |
| Wind Direction Accuracy | ± 5° 		 Tilt 0° (operates to 30° tilt) |
| Temperature Range | -25° to 55° C |
| Temperature Resolution | 0.18°F (0.1°C) |
| Temperature Accuracy | ±1.8°F (1°C) |
| Relative Humidity Range | 0-99% RH |
| Relative Humidity Resolution | 1% RH |
| Relative Humidity Accuracy | ± 4% RH |
| Barometric Pressure Range 		        26 to 32” HG (880 to 1080 mb) |  |
| Barometric Pressure Resolution | 0.03” HG (1 mb) |
| Barometric Pressure Accuracy | ±0.09” HG (±3 mb) |

## NMEA 2000® PARAMETER GROUP NUMBERS (PGNs)

PARAMETER 		         PGN#		 PGN NAME

#### DEFAULT RATE

|  |  | 130306 130310 130311 | Wind Data Environmental Parameters Environmental Parameters | 10 Times/Second 10 Times/Second 2 Times/Second |
| --- | --- | --- | --- | --- |
| Periodic Data PGNs |  | 130312 130313 130314 126464 | Temperature Humidity Actual Pressure PGN List (Transmit and Receive) | 2 Times/Second 2 Times/Second 2 Times/Second N/A |
| Response to Requested PGNs |  | 126996 126998 059392 059904 060416 | Product Information Configuration Information ISO Acknowledge ISO Request ISO Transport Protocol, Connection Management         N/A | N/A N/A N/A N/A |
| Protocol PGNs |  | 060160 060928 065240 126208 | ISO Transport Protocol, Data Transfer ISO Address Claim ISO Address Command NMEA Complex Request/Command/Ack. | N/A N/A N/A N/A |
| Maretron Proprietary PGNs |  | 126720 | Device Configuration Information | N/A |

## ELECTRICAL

## MECHANICAL

| PARAMETER 		                           VALUE		 COMMENT | PARAMETER 		             VALUE		 COMMENT |
| --- | --- |
| Operating Voltage		             9 to 32 Volts		DC Voltage | Size		      5.91” Dia. x 4.85” Tall		  Including Mounting Bracket |
| Power Consumption		                <50mA		     Average Current Drain | (150mm Dia. x 123.2mm Tall) |
| Load Equivalence Number (LEN)		       1		 NMEA 2000® Spec. (1LEN = 50mA) | Weight		        10 oz. (283g)		 Including Mounting Bracket |
| Reverse Battery Protection		         Yes		     Indefinitely | Mounting		 Pole		                      Fits 1"-14 TPI Standard Marine Mount |
| Load Dump Protection		               Yes		     Energy Rated per SAE J1113 |  |
| ENVIRONMENTAL | CERTIFICATIONS |
| PARAMETER 		                                           VALUE | PARAMETER 		 COMMENT |
| IEC 60945 Classification		                           Exposed | NMEA 2000® Standard		Certified |
| Degree of Protection		                                 IP67 | Maritime Navigation and Radio 		 IEC 61162-3 |
| Operating Temperature		                           -25°C to 55°C | Communication Equipment & Systems |
| Storage Temperature		                             -40°C to 70°C | Maritime Navigation and Radio        EC 60945 |
| Relative Humidity                        93%RH @40° per IEC60945-8.2 | Communication Equipment & Systems |
| Vibration		                   2-13.2Hz @ ±1mm, 13.2-100Hz @ 7m/s^2 per IEC 60945-8 | FCC and CE Mark		                    Electromagnetic Compatibility |
| Rain and Spray		         12.5mm Nozzle @ 100liters/min from 3m for 30min per IEC 60945-8.8 |  |
| Solar Radiation		Ultraviolet B, A, Visible, and Infrared per IEC 60945-8.10 |  |
| Corrosion (Salt Mist)		  4 times 7 days @ 40°C, 95%RH after 2 hour Salt Spray Per IEC 60945-8.12 |  |
| Thermal Shock		10 cycles -25°C to +55°C. Total test time 80 hours, 2 hour soak at each temperature |  |
| Electromagnetic Emission		           Conducted and Radiated Emission per IEC60945-9 |  |
| Electromagnetic Immunity		        Conducted, Radiated, Supply, and ESD per IEC 60945-10 |  |
| Safety Precautions         Dangerous Voltage, Electromagnetic Radio Frequency per IEC 60945-12 |  |

### 2 www.maretron.com | 866.550.9100

<!-- figure 1 on pdf page 2 at 425,55-559,209 pt | caption: none | text-layer labels: none | nearby labels: DEFAULT RATE | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 2 at 307,223-494,418 pt | caption: none | text-layer labels: none | nearby labels: MECHANICAL | VALUE		 COMMENT | PARAMETER | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 2 at 509,516-559,598 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 2 at 235,518-326,612 pt | caption: none | text-layer labels: none | nearby labels: VALUE | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
