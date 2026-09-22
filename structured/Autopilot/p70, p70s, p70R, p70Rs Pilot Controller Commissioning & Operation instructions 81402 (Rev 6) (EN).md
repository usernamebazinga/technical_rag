# p70 / p70s / p70R / p70Rs

<!-- source: sources/Autopilot/p70, p70s, p70R, p70Rs Pilot Controller Commissioning & Operation instructions 81402 (Rev 6) (EN).pdf | extraction: extracted/Autopilot/p70, p70s, p70R, p70Rs Pilot Controller Commissioning & Operation instructions 81402 (Rev 6) (EN).md | structured by tools/structure.py; every line can be checked in the extraction -->

## Addenda and corrections

<!-- pdf page 48 | printed page 48 -->

###### Caution: Cross track error correction

When returning to TRACK mode the autopilot will correct the XTE in order to keep to the defined track leg. The direction of turn may not coincide with the bearing to waypoint and may be different from that expected.

Route completion The autopilot displays the Route Complete warning when you have reached the last waypoint on a route.

- Note: The ‘Route Complete’ alarm only sounds and displays in conjunction with a multifunction display.

###### Manual course change

- To avoid obstacles in your path, in track mode you can manually alter your course and then resume track mode.
- In track mode:
1. Make the required course change using the appropriate [-1°], [+1°], [-10°], [+10°] or using the [Rotary controller].
2. Once clear of the obstacle select [Track] to resume track mode.

###### Leaving track mode

To leave Track mode:
1. Press [AUTO] to return to Auto mode (autopilot control), or.
2. Press [STANDBY] to return to Standby mode (manual steering).

### 7.5 Wind vane mode

When the autopilot is in Wind Vane mode, it uses the wind angle as the primary heading reference. As changes in the true or apparent wind angle occur, it adjusts the locked heading to maintain the original wind angle.

Note:
- Wind Vane mode is only available when the Vessel hull type is set to [Race Sail] or [Sail Cruiser], when using the Set-up Wizard.
- If you change the vessel type after completing the Dockside calibration process (using the Dockside wizard), all commissioning settings will be reset to default settings, and you will need to complete the Dockside calibration process again.

1. Initial wind direction
2. Wind shift
3. New wind direction
4. Relative wind angle
5. Vessel turns to maintain the same relative wind angle You can only select [Wind Vane] mode if your autopilot is receiving suitable wind data. Autopilots can maintain a course relative to either an Apparent or True wind angle. The default setting is Apparent wind. If required, you can change this to True wind from the [Wind Type] menu.

<!-- figure 1 on pdf page 48 at 41,29-86,108 pt | caption: none | text-layer labels: none | nearby labels: Route completion | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 48 at 334,199-607,343 pt | caption: none | text-layer labels: none | nearby labels: 1. | Initial wind direction | 2. Wind shift | OCR: no legible text (0/2 words >= 60, mean confidence 40) -->

<!-- pdf page 1 -->

p70 / p70s / p70R / p70Rs Commissioning and Operation Instructions

p70 / p70s / p70R / p70Rs

## Commissioning & Operation Instructions

Document number: 81402 (Rev 6) | English (en-US) | Date: 11-2025 | Applicable software version: v3.13

<!-- figure 1 on pdf page 1 at 118,34-530,293 pt | caption: none; nearest centred text below: "p70 / p70s / p70R / p70Rs Commissioning and Operation Instructions" | text-layer labels: none | OCR text follows (tesseract, unverified; 21/35 words >= 60, mean confidence 64) -->
Raymarine
Raymarine
Wind
38°P
Wind
300
330
330
295
240
240,
Mag
Mag
Track
Track
Menu
+12
Auto
+10°
-10°
Auto
<!-- end of figure 1 -->

<!-- pdf page 2 -->

(no text layer on this page)

<!-- pdf page 3 -->

###### Legal notices

<!-- omitted: "Trademark and patents notice" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Fair Use Statement" (pdf page 3; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Content notice" (pdf pages 3-5; 4 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 4 -->
<!-- pdf page 5 | printed page 5 -->
###### Checking hardware and software

###### CHAPTER 5 COMMISSIONING — EVOLUTION

5.1 Autopilot commissioning — main differences

<!-- pdf page 6 | printed page 6 -->

###### Checking the rudder alignment (Align

5.5 Compass linearization — Evolution

###### Accessing the compass deviation

###### CHAPTER 6 COMMISSIONING — SPX AND

###### Making temporary changes to pilot

###### Checking the rudder alignment (Align

6.8 Adjusting the hard-over time — SmartPilot

###### Disengaging the autopilot (Standby

<!-- pdf page 7 | printed page 7 -->

###### Rudder damping levels and deadband

###### CHAPTER 11 SYSTEM CHECKS AND

12.1 Raymarine technical support and

###### Checking hardware and software

###### APPENDIX A SUPPORTED NMEA 2000 PGN

###### APPENDIX B SOFTWARE RELEASE

<!-- pdf page 8 | printed page 8 -->

###### APPENDIX C DOCUMENT CHANGE

<!-- pdf page 9 | printed page 9 -->

## CHAPTER 1: IMPORTANT INFORMATION

### Safety warnings

###### Warning: Ensure safe navigation

This product is intended only as an aid to navigation and must never be used in preference to sound navigational judgment. Only official government charts and notices to mariners contain all the current information needed for safe navigation, and the captain is responsible for their prudent use. It is the user’s responsibility to use official government charts, notices to mariners, caution and proper navigational skill when operating this or any other Raymarine product.

###### Warning: Maintain a permanent watch

Always maintain a permanent watch, this will allow you to respond to situations as they develop. Failure to maintain a permanent watch puts yourself, your vessel and others at serious risk of harm.

###### Warning: Autopilot usage

Autopilots navigate a preset course and do NOT respond to hazards automatically. The operator must remain at the helm at all times and be ready to avoid hazards and warn passengers of course changes.

Important information

### Product warnings

###### Caution: Sun covers

- Sun covers are used to protect the display screen against the damaging effects of ultraviolet (UV) light. If your product is supplied with a sun cover always ensure it is fitted when the product is not in use.
- To avoid potential loss of the sun cover, ensure that the sun cover is removed when travelling at high speed, whether in the water or when the vessel is being towed.
- To avoid potential screen damage, ensure that the rear surface of the sun cover and the display screen are clean and free from debris before placing the sun cover on the screen.

###### Caution: Product cleaning

When cleaning products:
- Switch off power supply.
- Use a clean damp cloth to wipe clean.
- Do NOT use: abrasive, acidic, ammonia, solvent or other chemical-based cleaning products.
- Do NOT use a jet wash.

### Regulatory notices

###### TFT Displays

The colors of the display may seem to vary when viewed against a colored background or in colored light. This is a perfectly normal effect that can be seen with all color Thin Film Transistor (TFT) displays.

9

<!-- figure 1 on pdf page 9 at 274,91-314,214 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 9 at 41,94-86,214 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 9 at 41,218-314,370 pt | caption: none | text-layer labels: Warning: Maintain a permanent watch | Warning: Autopilot usage | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 10 | printed page 10 -->

###### Water ingress

Water ingress disclaimer Although the waterproof rating capacity of this product meets the stated water ingress protection standard (refer to the product’s Technical Specification), water intrusion and subsequent equipment failure may occur if the product is not installed correctly or subjected to high-pressure washing. Raymarine will not warrant products subjected to high-pressure washing.

<!-- omitted: "Disclaimer" (pdf page 10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "PSTI Compliance" (pdf page 10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
###### Product disposal

Dispose of this product in accordance with the WEEE Directive. The Waste Electrical and Electronic Equipment (WEEE) Directive requires the recycling of waste electrical and electronic equipment which contains materials, components and substances that may be hazardous and present a risk to human health and the environment when WEEE is not handled correctly. Equipment marked with the crossed-out wheeled bin symbol indicates that the equipment should not be disposed of in unsorted household waste. Local authorities in many regions have established collection schemes under which residents can dispose of waste electrical and electronic equipment at a recycling center or other collection point. For more information about suitable collection points for waste electrical and electronic equipment in your region, refer to the Raymarine website: https://bit.ly/rym-recycling

<!-- omitted: "Warranty policy and registration" (pdf page 10; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
###### IMO and SOLAS

The equipment described within this document is intended for use on leisure marine boats and workboats NOT covered by International Maritime Organization (IMO) and Safety of Life at Sea (SOLAS) Carriage Regulations.

<!-- figure 1 on pdf page 10 at 338,228-386,276 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 11 | printed page 11 -->

<!-- omitted: "Technical accuracy" (pdf page 11; 1 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- omitted: "Publication copyright" (pdf pages 11-12; 2 lines): legal, warranty or regulatory boilerplate; text in the extraction -->
<!-- pdf page 12 | printed page 12 -->
## CHAPTER 2: DOCUMENT INFORMATION

##### CHAPTER CONTENTS

<!-- pdf page 13 | printed page 13 -->

### 2.1 Applicable products

This document is applicable to the products shown below.

1. p70s (E70328) — 8 button pilot controller (sail).
2. p70Rs (E70329) — Rotary pilot controller (power).
3. p70 (E22166) — 8 button pilot controller (sail).
4. p70R (E22167) — Rotary pilot controller (power).

###### Compatible autopilot systems

Your product is compatible with the following autopilot systems:

1. Evolution autopilots (Connects via SeaTalk NG).
2. SPX SmartPilot (Connects via SeaTalk NG).
3. S1, S2 & S3 SmartPilot (Connects via SeaTalk 1 to SeaTalk NG adapter cable (Part number: A06047).

Document information

### 2.2 Product documentation

The following documentation is applicable to your product:

###### Applicable documents

Document         Description                 Link

| 81402 | p70 / p70R / p70s / p70Rs Commissioning and Operation Instructions (this document). | www.bit.ly/p70s-docs |
| --- | --- | --- |
| 87130 | p70 / p70R Mounting template. | www.bit.ly/p70-docs |
| 87260 | p70s / p70Rs Mounting template. | www.bit.ly/p70s-docs |
| 87424 | p70s / p70Rs Pilot Controller Installation Instructions | www.bit.ly/p70s-docs |
| 87426 | p70 / p70R Pilot Controller Installation Instructions | www.bit.ly/p70-docs |

###### Printed (hardcopy) product manuals

All applicable user documentation for your product is available on our website to view or download free-of-charge. If you would prefer a printed (hardcopy) product manual, a Print Shop service is available, enabling you to purchase a high-quality, professionally-printed manual for your product, delivered directly to your door. Printed manuals are ideal for keeping onboard your vessel, as a useful source of reference whenever you need assistance with your product. Printed manuals are provided by a third-party (Lulu Press). To order a printed manual, use the Lulu Press website link provided below. The manual will then be printed and delivered to the address you specify. Once an order is placed, it typically takes Lulu Press approximately 5 to 10 working days to print and deliver a printed manual.

13

<!-- figure 1 on pdf page 13 at 38,62-314,161 pt | caption: none | text-layer labels: none | nearby labels: 2.1 Applicable products | 1. | OCR below floor, text not used (6/17 words >= 60, mean confidence 45) -->

<!-- figure 2 on pdf page 13 at 38,264-314,348 pt | caption: none | text-layer labels: none | nearby labels: Compatible autopilot systems | 1. | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 96) -->
Raymarine
Raymarine
<!-- end of figure 2 -->

<!-- pdf page 14 | printed page 14 -->

Supplier         How to purchase

1. Click the following link.
2. In the displayed search field, enter the required document number, e.g. 81406 www.bit.ly/rym_printshop

Note:
- Accepted methods of payment for printed manuals are credit cards and PayPal.
- Printed manuals can be shipped worldwide.

### 2.3 Document conventions

The following conventions are used throughout this document:
- Highlight — The term ‘highlight’ refers to using the [UP] or [DOWN] buttons to highlight an item.
- Select — The term ‘select’ refers to using the [UP] or [DOWN] buttons to highlight an item, and then pressing the [OK] button to select the item.
- Scroll — The term ‘scroll’ refers to using the [UP] or [DOWN] buttons to move up or down a menu to an item that is not currently shown onscreen.
- Adjust — The term ‘adjust’ is used to denote using the [UP] or [DOWN] buttons to change a numeric value or slider bar control.
- Enable — The term ‘enable’ refers to using the [UP] or [DOWN] buttons to highlight a toggle switch and press [OK] to activate the switch (when activated the switch background will turn green and the toggle is positioned to the right).
- Disable — The term ‘disable’ refers to using the [UP] or [DOWN] buttons to highlight a toggle switch and press [OK] to deactivate the switch (when deactivated the switch background will turn gray and the toggle is positioned to the left).

### 2.4 Document illustrations

Your product and if applicable, its user interface may differ slightly from that shown in the illustrations in this document, depending on product variant and date of manufacture. All images are provided for illustration purposes only.

### 2.5 Glossary

A glossary of common terms and abbreviations used in this document can be found in the appendix. Refer to: p.76 — Glossary

<!-- pdf page 15 | printed page 15 -->

## CHAPTER 3: SOFTWARE DETAILS

##### CHAPTER CONTENTS

Software details                                    15

<!-- pdf page 16 | printed page 16 -->

### 3.1 Applicable software version

Product software is updated regularly to add new features and improve existing functionality. This document has been updated to reflect the following software version: Software name                       Applicable software version

p70-Series                          v3.13

The following changes have been introduced in this software version:
- Improvements to support MFD Wind vane mode. Check the website for the latest software: p70-Series software download link

www.bit.ly/p70-download

### 3.2 Software compatibility

The software version installed on Raymarine products must be compatible with the version of software installed on your display.

Note: Where possible, you should always update your Raymarine products’ software to the latest available versions.

### 3.3 Software updates

Raymarine regularly issues software updates for its products, which provide new and enhanced features and improved performance and usability. It’s important to ensure that you have the latest software for your products by regularly checking the Raymarine website for new software releases. To check for the latest software updates and the software update procedure for your specific product(s), refer to: www.bit.ly/rym-software Unless otherwise stated, software updates for Raymarine products are performed using a Raymarine MFD / chartplotter. • Where applicable, you should always backup your user data and settings before performing a software update.

- To update SeaTalk NG products, you must use the datamaster MFD / chartplotter which is physically connected to the SeaTalk NG backbone.
- Ethernet (RayNet) products can be updated from any MFD / chartplotter on the same network as the product to be updated.
- In order to perform a software update, any connected Autopilot or Radar must be switched to Standby.
- The MFD / chartplotter “Check online” feature is only available when connected to the Internet.

Note: If in doubt as to the correct procedure for updating your product software, refer to your dealer or Raymarine technical support.

###### Checking hardware and software information

- You can check current hardware details and software version from the [About display] menu.
1. Press the [Menu] button.
2. Select [Set-up].
3. Select [Diagnostics].
4. Select [About Display]. A range of information is displayed, including the software version and Serial number.
5. Use the [Up] and [Down] buttons to cycle through the information.

###### Caution: Installing software updates

- The software update process is carried out at your own risk. Before initiating the update process ensure you have backed up any important files.
- Ensure that the product(s) has a reliable power supply and that the update process is not interrupted.
- Damage caused by an incomplete update is not covered by Raymarine warranty.
- By downloading the software update package, you agree to these terms.

<!-- figure 1 on pdf page 16 at 334,334-379,468 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 17 | printed page 17 -->

###### Performing software updates

Software updates for this product are performed from a Raymarine MFD / Chartplotter. For instructions on how to update product software, refer to the software update instructions included in the Operation instructions for your MFD / Chartplotter:

| MFD / Chartplotter | Document | Link |
| --- | --- | --- |
| software |  |  |
| LightHouse 2 | Operation Instructions (81360) | www.bit.ly/LH2-docs |
| LightHouse 3 | Advanced Operation Instructions (81370) | www.bit.ly/LH3-docs |
| LightHouse 4 | Advanced Operation Instructions (81406) | www.bit.ly/LH4-docs |
| LightHouse Sport | Operation | www.bit.ly/element- |
| (Element) | Instructions (81388) | docs |

Software details                                                      17

<!-- pdf page 18 | printed page 18 -->

## CHAPTER 4: GETTING STARTED

##### CHAPTER CONTENTS

<!-- pdf page 19 | printed page 19 | header: Description -->

## Description

### 4.1 Commissioning

Before using your pilot controller to command your autopilot system, ensure that it has been correctly commissioned in accordance with the instructions provided in this document or the instructions provided with your autopilot system. • For commissioning your pilot controller and Evolution-Series autopilot system refer to: p.26 — Commissioning — Evolution autopilot system • For commissioning your pilot controller and SPX-Series autopilot system refer to: p.33 — Commissioning — SPX and SmartPilot systems

### 4.2 Controls

Use the physical buttons to operate the display. Each button has multiple functions.

Note: The p70s and p70Rs are pictured below. The p70 and p70R have the same control buttons as the p70s and p70Rs.

Description

1   [Left soft button]
- Cancel
- Back
- Select pilot mode 2   [Up] / [-1°]
- Decrease heading by 1°
- Move up in menu
- Increase numerical value 3   [Down] / [+1°]
- Increase heading by 1°
- Move down in menu
- Decrease numerical value 4   [Menu] / [Right soft button]
- Open menu
- Select menu item
- OK
- Save 5   [Standby] / [Power]
- Disengage autopilot (standby)
- Power on
- Power off
- Open Brightness page
- Cancel
- Back 6   [–10°] — Decrease heading by 10° 7   [+10°] — Increase heading by 10°

<!-- figure 1 on pdf page 19 at 38,278-314,365 pt | caption: none | text-layer labels: none | nearby labels: 4 | 5 | OCR text follows (tesseract, unverified; 8/10 words >= 60, mean confidence 75) -->
3
Menu
Menu
(0)
+10°
—10°
Auto
‘Auto
<!-- end of figure 1 -->

<!-- pdf page 20 | printed page 20 | header: Description -->

Description

8     [Auto] — Engage autopilot 9     [Rotary controller] • Turn clockwise to increase heading, move down through menu items or to increase a numerical value. • Turn counter-clockwise to decrease heading, move up through menu items or to decrease a numerical value. • Push the center of the rotary controller to select a menu option or save a change to a menu setting.

The p70s also supports the following combination button presses:
- [–1°] and [–10°]
- Perform an [Auto Turn] to port.
- In wind vane mode, perform an AutoTack to port.
- [+1°] and [+10°]
- Perform an [Auto Turn] to starboard.
- In wind vane mode, perform an AutoTack to starboard.

Note:
- Any combination button press which includes the [Standby] button will disengage your autopilot.
- By default, the [Auto Turn] angle is set to 90°. The turn angle can only be configured via a compatible MFD, using the [Drive Settings]: [Menu > Set-up > Autopilot Calibration > Drive Settings > Auto Turn].

### 4.3 Switching on the display

The display will automatically switch on when power is applied to the SeaTalk NG backbone, unless the display has previously been switched off using the [Power] button. If the [Power] button has been used to switch off the display then it must be used to switch the display back on again. With the display powered but switched off: 1. Press and hold the [Power] button until the screen turns on (approximately 2 seconds).

### 4.4 Switching off the display

The display can be switched off using the [Power] button.
1. Press and hold the [Power] button until the count down timer reaches zero and the screen turns off.

Note: When switched off, the display may still draw a small amount of power from the battery, if this is a concern unplug the SeaTalk NG power supply or switch off at the breaker.

### 4.5 Completing the set up wizard

- If the display is being switched on for the first time or after a factory reset the set up wizard will be launched. The set up wizard guides you through the following basic
- configuration settings:
1. Language selection
2. Boat type selection
3. Welcome message

Note: The set up wizard may be skipped if these settings have already been configured for another display in the system.

1. Select the user interface language that you want to use.
2. Select the boat type that closely matches your vessel’s hull type.
3. Select [Continue]. The large pilot view page is displayed.

<!-- figure 1 on pdf page 20 at 334,338-607,410 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 40/42 words >= 60, mean confidence 91) -->
Language
Boat Type
Welcome
English (UK)
Your i70 is now ready to
use.(For more settings,
including customizing your
English (US)
Power Cruiser 2 (<30kts)
favorite pages calibrating
transducers, open MENU)
Frangais
Power Cruiser 3 (>30kts)
Select
Select
Back
Back
Continue
<!-- end of figure 1 -->

<!-- pdf page 21 | printed page 21 -->

### 4.6 Autopilot functions and modes

Your autopilot has the following functions and modes. Pilot modes can be assigned to the [Left soft button] (Shortcut key).

###### Autopilot functions

- [Auto] — The autopilot is engaged and will automatically steers the vessel to maintain a heading. Auto is activated by pressing the [Auto] button.
- [Standby] — The autopilot is disengaged and you are free to steer the vessel manually.
- [Power Steer] — Power steer enables you to steer the vessel using the p70Rs or p70RRotary controller.

- Note: Power steer is not available on the p70s or p70.

- [Jog steer] — Jog allows you to move the tiller drive’s ram in and out using the [+] and [–] buttons on the p70s or p70.

Note:
- Jog steer is not available on the p70Rs or p70R.
- Jog steer is only available when a “sailing” vessel hull type and the [Tiller drive] type has been selected during commissioning.

###### Autopilot modes

Autopilot modes are activated from the [Modes] menu.
- [Wind vane] — The autopilot is engaged and will steer your vessel automatically to maintain a specified apparent or true wind angle.

Note: [Wind vane] mode is only available when a “sailing” vessel hull type has been selected during commissioning.

- [Track] — The autopilot is engaged and will automatically steer your vessel to a waypoint.
- [Pattern] — The autopilot is engaged and will automatically steer your vessel in a specified pattern.

Note: Pattern mode is only available when a “power” vessel hull type has been selected during commissioning.

### 4.7 Autopilot response levels

The Evolution-Series autopilot system includes response levels which allows the system to be configured for optimum performance depending on your current needs. The available response levels are: • [Leisure] — suitable for long passages where tight heading control is not critical. • [Cruising] — good course-keeping without overworking the system. • [Performance] — emphasis on tight heading control. The [Response level] is changed from the [Response Level] menu and then selecting [Save].

Note: In [Wind vane] mode the wind trim setting is automatically set by the selected autopilot response level.

### 4.8 Automatic turning

Automatic turning enables Evolution-Series autopilots to automatically turn to the next waypoint in a route. When the current waypoint arrival radius has been reached a countdown will commence, and when it reaches zero the vessel will automatically turn toward the next waypoint.

###### The Automatic turning feature requires your Evolution-Series

autopilot to be running software version 3.14 or later and your Axiom-Series or Axiom 2-Series display to be running LightHouse 4 v4.4.70 or later. Automatic turning is available when the [Vessel hull type] is set to one of the power options. [Vessel hull type] can be changed from the [Vessel settings] menu: [Menu > Set-up > Autopilot Calibration > Vessel Settings > Vessel Hull Type].

<!-- pdf page 22 | printed page 22 -->

Note:
- Automatic turning is NOT available when the autopilot is configured using a Sail [Vessel hull type].
- Waypoints must be farther apart than the [Arrival radius (pilot in track mode)] distance.

Automatic turning is disabled by default. Automatic turning can only be enabled and configured from an Axiom-Series or Axiom 2-Series display’s [Autopilot] settings menu: [Homescreen > Settings > Autopilot > Automatically turn to next waypoint].

### 4.9 Adjusting the display’s brightness

The display’s brightness level can be adjusted.
1. Press the [Power] button. The Display Brightness page is displayed.
2. Use the [Up] and [Down] buttons or the [Rotary controller] to adjust the brightness to the required level.
3. Select [Ok]. The Display Brightness page will time-out after 2 seconds, saving the new brightness level.

### 4.10 Shared Brightness

- Shared brightness enables simultaneous brightness adjustment of all products that are part of the same group. For example, these groups could be used to reflect the physical location of products on your
- vessel (e.g.: helm and flybridge). The following products are compatible with shared brightness:
- Alpha-Series Performance Displays
- LightHouse 4 MFDs.
- LightHouse 3 MFDs using software v3.4.102 or later.
- SeaTalk NG Instrument displays and Pilot controllers.
- SeaTalk NG VHF DSC Radios.
- RMK-9 and RMK-10 remote keypads. Any adjustments to the shared brightness level will be applied to all products assigned to the same group.

- Multiple brightness groups can be configured. For example, these groups could be used to reflect the physical location of products on
- your vessel e.g.: helm and flybridge.
- Shared brightness requires:
- All products to be compatible with the shared brightness function (see list of compatible products above).
- The [Shared brightness] setting set to On for all products in the brightness group.
- Products to be assigned to network groups.
- All the products in each group to be synchronized.

Note: If any display in the system has automatic brightness enabled, the brightness of all displays in the same group will be automatically adjusted and synchronized, whenever a brightness adjustment is made on any of the displays in the group.

<!-- figure 1 on pdf page 22 at 334,53-607,134 pt | caption: none | text-layer labels: none | nearby labels: LightHouse 4 / LightHouse 3 | Alpha-Series Performance Displays | VHF DSC Radio | Instrument display / Pilot controller | OCR text follows (tesseract, unverified; 18/26 words >= 60, mean confidence 67) -->
Screen lock
Power save
Tok
ate
Settings
ages.
st
Brightness
‘Shared brightness
Display mode
Auto
Color mode
Night
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 22 at 334,168-607,271 pt | caption: none | text-layer labels: none | nearby labels: VHF DSC Radio | Instrument display / Pilot controller | OCR text follows (tesseract, unverified; 4/4 words >= 60, mean confidence 95) -->
Shared Brightness
Unshare
OK
<!-- end of figure 2 -->

<!-- pdf page 23 | printed page 23 -->

###### Assigning A Network Group

- To enable the shared brightness and color, displays must be assigned to the same network group. Compatible instrument displays and pilot controllers will also share their color scheme.
- From the [Network Group] menu: [Menu > Set-up > System Set-up > Network Group]
1. Select the network group that you want to assign the display to.
- Available groups are:
- None (default)
- Helm 1
- Helm 2
- Cockpit
- Flybridge
- Mast
- Group 1 — Group 5
2. Select [Brightness/Color Group].
3. Select [This Group].
4. Select [Sync]. The System will now synchronize all displays assigned to the same group.
5. Select [OK].
6. Carry out steps 1 to 5 on all displays. When the brightness level is adjusted it will effect all displays assigned to the same group.

###### Unsharing the display

Displays can be removed from shared brightness so that brightness is individual to the display.

1. With the Shared brightness adjustment page displayed, select [Unshare] to revert to individual display brightness.
2. With the Display brightness page displayed, select [Share] to switch back to shared brightness.

### 4.11 Changing the color scheme

- The display’s color scheme can be changed.
- From the [Colors] menu: [Menu > Display Settings > Colors]
1. Select a color scheme from the list
- The available color schemes are:

<!-- figure 1 on pdf page 23 at 480,77-595,156 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 6/6 words >= 60, mean confidence 88) -->
2?
Display Brightness
72%
Share
OK
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 23 at 346,79-458,156 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 4/5 words >= 60, mean confidence 84) -->
Shared Brightness
OK
Unshare
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 23 at 346,288-607,482 pt | caption: none | text-layer labels: none | nearby labels: The available color schemes are: | OCR text follows (tesseract, unverified; 21/25 words >= 60, mean confidence 86) -->
Select Color
Select Color
Day1
Day2
Inverse
Day2
Inverse
Red/Black
Cancel
Select
Cancel
Select
Select Color
Day 2
Red/Black
Cancel
Select
<!-- end of figure 3 -->

<!-- pdf page 24 | printed page 24 -->

| Item | Color scheme |
| --- | --- |
| 1 | Day 1 |
| 2 | Day 2 |
| 3 | Inverse |
| 4 | Red/Black |

Note: If the display is part of a shared brightness network group the color scheme will change on all displays that support color schemes and are assigned to the same network group.

### 4.12 Setting the display response

- Display response determines how quickly the values displayed onscreen are changed when changes occur in the received data. Setting the display response to a low value will dampen data fluctuations to provide a more stable reading. Setting the display response to a higher value will reduce the damping to make readings more responsive.
- From the [Display Settings] menu: [Menu > Display Settings ]
1. Select [Display Response].
2. Select the data type:
- Speed
- Depth
- Wind Speed
- Wind Angle
- Heading
3. Adjust the value as required. By default response values are set to 12.
4. Select [Save].

### 4.13 Multiple data sources (MDS)

- MDS is a Raymarine scheme for managing multiple sources of
- identical data types on the same network (e.g.: in an MFD network you may have more than one source of GNSS (GPS) position data). The MFD will automatically select a preferred data source (device) to use for that data type.
- MDS can be used for the following data types:
- Depth
- Speed through water
- Heading
- GPS
- GPS Datum
- Wind
- Time & Date If you do not want to use the automatically selected data source you can manually select your preferred data source.

Note: For MDS to be available on your system, all products in the system that report data must be MDS-compliant. The system will report any products that are NOT MDS-compliant. It may be possible to upgrade the software for these non-compliant products, to make them compliant. Visit the Raymarine website to obtain the latest software for your products: https://bit.ly/rym-software If MDS-compliant software is not available for the product and you do NOT want to use the system’s preferred data source, you must remove any non-compliant products from the system. You should then be able to select your preferred data source. Once you have completed setting up your preferred data sources, you may be able to add non-compliant products back into the system.

###### Selecting a preferred data source

- You can select your preferred data source for data items that can be shown on the display.
- From the [System Set-up] menu: [Menu > Set-up > System Set-up]
1. Select [Data Sources].
2. Select the Data type.

<!-- pdf page 25 | printed page 25 -->

The unit will now search for and display a list of all sources for the selected data type.

3. Select your preferred data source, or
4. Select [Auto] to allow the system to decide. ‘ACTIVE’ is displayed next to the data source that is the current source for the data type.

<!-- figure 1 on pdf page 25 at 53,55-314,168 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/13 words >= 60, mean confidence 93) -->
Depth
00380016 STng ACTIVE
ST70 Depth Pod
00420065 STng
iTC-5 Converter
Back
Select
<!-- end of figure 1 -->

<!-- pdf page 26 | printed page 26 -->

## CHAPTER 5: COMMISSIONING — EVOLUTION AUTOPILOT SYSTEM

##### CHAPTER CONTENTS

<!-- pdf page 27 | printed page 27 -->

### 5.1 Autopilot commissioning — main differences between Evolution™ and SPX systems

The Evolution system provides a number of features which improve upon the commissioning process required by traditional autopilot systems. • Built-in heading and attitude sensor — no additional fluxgate compass is required. • Automatic set up — the rudder gain, counter rudder, manual compass calibration and AutoLearn settings required on older systems are no longer required. This results in a greatly simplified dockside calibration process.

### 5.2 Commissioning

###### Commissioning pre-requisites

Before commissioning your autopilot system for the first time, ensure that you have read through and understood the entire commissioning instructions for your autopilot system. Before commissioning, you should also ensure the following: • All autopilot system components have been installed in accordance with the installation instructions supplied with the system components. • All autopilot system components have been updated to the latest available software versions, available on the Raymarine website. • A system schematic is available which includes all system components and required connections. • The commissioning engineer is familiar with the vessel’s hull type, drive type and steering system.

###### Commissioning steps

The required commissioning steps should be carried out in the correct order using the pilot controller display. 1. Power-up all of the components that make up your autopilot system.

2. Select the relevant vessel hull type for your vessel from the [Vessel Hull Type] menu: [Menu > Set-up > Autopilot Calibration > Vessel Settings > Vessel Hull Type]

Note: Vessel hull type may have already been selected as part of the start-up wizard.

3. Complete the dockside calibration process., using the [Dockside wizard]:
4. If the system does NOT include a rudder reference transducer then, specify the hard-over time.
5. Complete compass linearization.
6. If required, lock the compass. Vessel hull type selection The vessel hull type options are designed to provide optimum steering performance for typical vessels. It is important to complete the vessel hull type selection, prior to performing dockside calibration, as it forms a key part of the commissioning process. The vessel hull type options can be accessed at any time when the autopilot is in Standby, from the [Vessel Hull Type] menu: [Menu > Set-up > Autopilot Calibration > Vessel Settings > Vessel Hull Type]. Select the option that most closely matches your vessel’s hull type and steering characteristics:
- [Power]
- [Power (slow turn)]
- [Power (fast turn)]
- [Sail]
- [Sail (Slow turn)]
- [Sail Catamaran]

Note: It is important to be aware that steering forces (and therefore rate-of-turn) vary significantly depending on the combination of vessel hull type, steering system, and drive type. The available vessel hull type options are provided for guidance only. It may be possible to improve the steering performance of your vessel by selecting a different vessel hull type.

<!-- pdf page 28 | printed page 28 -->

When choosing a suitable vessel hull type, the emphasis should be on a safe and dependable steering response.

### 5.3 Using the Dockside wizard

The dockside calibration process must be completed before the autopilot system can be used for the first time. The Dockside wizard guides you through the steps required for dockside calibration. The Dockside wizard contains different steps, depending on whether the system includes a rudder reference transducer: To access the wizard, ensure the autopilot is in standby, and then: 1. Select [Dockside Wizard] from the [Commissioning] menu [Menu > Set-up > Autopilot Calibration > Commissioning]. 2. Select [Continue] to initiate the dockside wizard.

###### Selecting a drive type

- Drive type selection is included in the dockside wizard. If your drive type is not listed, contact your Raymarine dealer for advice.
- With the [Drive Type] menu displayed:
1. Select your drive type.
- The drive types available are:
- Type 1 / Type 2 Linear
- Type 2 / Type 3 Hydraulic Linear
- I/O Stern
- Wheel Drive
- Tiller
- Sport Drive
- Verado
- Rotary Drive Type 1 / Type 2
- Hydraulic Pump Type 1 / Type 2 / Type 3 Drive type selection is also available when the autopilot is in standby,
- from the [Drive Type] menu: [Menu > Set-up > Autopilot Calibration > Vessel Settings > Drive type].

###### Aligning the rudder

For systems that have a rudder reference transducer fitted, Rudder alignment is included in the dockside wizard and occurs after drive type selection. For systems without a rudder reference transducer fitted, rudder alignment is not required. Scenario            Description

The following procedure only applies to vessels with a rudder reference transducer.

1. Select [Continue].
2. Center the rudder and select [OK].
3. Put the rudder all the way to port and press [OK].
4. Put the rudder all the way to starboard and press [OK].
5. Center the rudder and select [OK].
6. Select [Continue] when the task complete message is displayed to progress to the rudder limit page.

###### Setting the rudder limit

Rudder limit setting is included in the dockside wizard and comes after rudder alignment. Scenario            Description

For vessels without a rudder reference transducer: Rudder limit is set to 30 degrees and can be adjusted as required using the [Up] and [Down] buttons or the [Rotary controller]. For vessels with a rudder reference transducer: The rudder alignment process establishes the rudder limit. The rudder limit will be displayed with a message confirming that the rudder limit has been updated. If required, the limit can be adjusted using the [Up] and [Down] buttons or the [Rotary controller].

<!-- figure 1 on pdf page 28 at 334,115-607,161 pt | caption: none | text-layer labels: none | nearby labels: Scenario | Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 29 | printed page 29 -->

1. Ensure that the rudder limit is sufficient to prevent the steering mechanism impacting the end stops and placing the steering system under unnecessary load.

Important: It is recommended that the limit is set to approximately 5 degrees less then the maximum rudder angle.

2. Select [Continue] to move to the next step.

- Note: The rudder limit can be adjusted when the autopilot is in standby,
- from the [Drive Settings ] menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Rudder Limit].

###### Checking the rudder drive

As part of the dockside calibration process, the system will check the drive connection. Once it has completed the check successfully, a message will appear asking if it is safe for the system to take the helm. During this procedure the autopilot will move the rudder. Ensure it is safe to proceed before pressing OK. When in dockside calibration mode, with the Motor Check page displayed: 1. Centre and let go of the rudder. 2. Disengage any rudder drive clutch. 3. Select [CONTINUE]. 4. Check it is safe to proceed before selecting [OK]. For vessels with a rudder reference transducer, the autopilot will now automatically move the rudder to port and then starboard. 5. For vessels without a rudder reference transducer: i. You will be asked to confirm that the rudder has turned to port by selecting [YES ] or [NO]. ii. Select [OK] if it is safe to engage the rudder in the opposite direction. iii. You will be asked to confirm the rudder turned to starboard by selecting [YES] or [NO]. 6. Dockside calibration is now complete, select [CONTINUE].

Note: If you confirmed a “NO” response for the rudder movement to both port and starboard, the wizard will exit. It is possible that the steering system did not move the rudder in any direction, and it will be necessary to check the steering system before completing the Dockside wizard procedure again.

###### Checking the rudder alignment (Align Rudder)

This procedure establishes port and starboard rudder limits for systems using a rudder reference transducer. Scenario             Description

The following procedure only applies to vessels with a rudder reference transducer.

1. Center the rudder and select [OK].
2. When prompted, turn the rudder hard to port and select [OK].
3. When prompted, turn the rudder hard to starboard and select [OK].
4. When prompted, turn the rudder back to the center and select [OK].

###### Hard-over time

The hard-over time setting can be specified as part of the Dockside wizard. Scenario             Description

The following procedure only applies to vessels without a rudder reference transducer.

- If you already know the hard-over time for your vessel’s steering system: enter this time during the Dockside wizard procedure.
- If you do NOT know the hard-over time for your vessel’s steering system: skip this step during the Dockside wizard procedure by selecting [SAVE] , then proceed

<!-- figure 1 on pdf page 29 at 334,175-607,221 pt | caption: none | text-layer labels: none | nearby labels: Scenario | Description | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 78) -->
Q
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 29 at 334,370-607,413 pt | caption: none | text-layer labels: none | nearby labels: Scenario | Description | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 30 | printed page 30 -->

to the p.29 — Checking the rudder drive section in this document to complete the Dockside wizard procedure. Once the wizard is complete, proceed to p.37 — Adjusting the hard-over time — SmartPilot and SPX, for information on how to calculate and adjust the hard-over time.

### 5.4 Adjusting the hard-over time — Evolution

On vessels without a rudder reference transducer, it is important to set a Hard Over Time. Before attempting to follow this procedure ensure you have read and understood the Rudder Check warning provided in this document. To estimate your hard over time follow the steps below: 1. With the autopilot in [Standby], manually turn the rudder / engine full to port. (For vessels with power steering the engine should be running when turning the rudder.) 2. Engage [Auto] mode. 3. Press the [+10] and [+1] buttons at the same time (p70/p70s) or use the [Rotary] (p70R/p70Rs) to alter your locked heading by 90 degrees. Use a stop watch to time the movement of the rudder / engine. 4. Estimate how long it would take to move the rudder from full port to full starboard. This estimate is your [Hard Over Time]. 5. Enter this estimate as your Hard Over Time. The Hard Over time setting can be accessed from the Drive Settings menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Hard Over Time]. 6. After setting your Hard Over Time, observe your autopilot’s behavior and if required, make small adjustments to the Hard Over Time value until a satisfactory result is achieved.

###### Warning: Rudder check

If no rudder reference has been fitted you MUST ensure that adequate provision is made to prevent the steering mechanism from impacting the end stops.

### 5.5 Compass linearization — Evolution autopilots

The EV unit’s internal compass needs to compensate for local and the Earth’s magnetic fields. This is achieved using an automatic process known as linearization.

###### Initial linearization

When the EV unit is first installed and powered-up (or after a factory reset or compass restart) linearization is required. A progress bar is displayed to indicate this:

The linearization process will start automatically after your vessel has turned approximately 100° at a speed of between 3 –15 knots. Linearization requires no user input, however at least a 270° turn is required before linearization can complete. The progress bar displays the progress, and will turn Red if the process is paused or otherwise interrupted. The time to complete linearization varies according to the characteristics of the vessel, the installation environment of the EV unit, and the levels of magnetic interference at the time of conducting the process. Sources of significant magnetic interference may increase the time required to complete the linearization process. Examples of such sources include: marine pontoons, metal-hulled vessels, and underwater cables. You can speed-up the linearization process by completing a full 360° turn (at a speed of 3 – 15 knots). You can also restart the linearization process at any time by selecting the [Restart Compass] menu item. Once the initial linearization is complete, the Deviation page is displayed and the current maximum compass deviation is shown:

<!-- figure 1 on pdf page 30 at 410,168-530,262 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 82) -->
30
10
20)
30
047°
True
Track Detecting magnetics...
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 30 at 41,372-86,434 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 30 at 226,372-314,432 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 31 | printed page 31 -->

###### Compass deviation

If the reported deviation is 45° or higher, it is highly recommended that the EV unit is moved and re-installed in a location which is subject to less magnetic interference. After the linearization process has successfully completed you can check the current deviation value at any time from the Diagnostics pages.

Note: If “- -” is displayed as the Deviation value, it means that linearization has not been successfully completed yet.

###### Check the compass heading data

As part of the autopilot system commissioning process, it is recommended that you check the compass heading value displayed, against a good known heading source on various headings. Do NOT rely on the reported heading until compass linearization and alignment is complete.

Note: Once the linearization process has completed, it is possible that the heading value may have a slight offset of 2 to 3 degrees. This is common where installation space is limited, and the EV unit cannot be properly aligned to the vessel's longitudinal axis. In this case, it is possible to manually adjust the Compass Offset value.

###### System monitoring and adaptation

To ensure optimum performance, after the initial linearization process is complete, the EV continues to monitor and adapt the compass linearization to suit current conditions.

- If the conditions for linearization are less than ideal, the automatic linearization process temporarily pauses until conditions improve again. The following conditions can cause the linearization process
- to temporarily pause:
- Boat speed < 3 knots.
- Boat speed > 15 knots.
- Rate-of-turn is too slow.
- Significant magnetic interference is present.

###### Accessing the compass deviation indicator

1. Select [MENU].
2. Select [Set-up].
3. Select [Diagnostics].
4. Select [About Pilot]. The details related to the pilot diagnostics are displayed.
5. Scroll down to the bottom of the list to view the entry for Deviation.

- Note: If “- -” is displayed as the Deviation value, it means that linearization has not been successfully completed yet.

###### Adjusting the Compass Offset

With the pilot in Standby:
1. From the [Vessel Settings] menu: ([Menu > Set-up > Autopilot Calibration > Vessel Settings]).
2. Select [Compass Offset].
3. Use the [+/- 10] button (p70/p70s) or [ROTARY] control (p70R/p70Rs) to adjust the compass offset as appropriate. The [Compass Offset] can be adjusted between –10° and +10°.

### 5.6 Compass lock

Once you are satisfied with the compass accuracy, you can lock the setting to prevent the system from completing a further automatic linearization in the future. This feature is particularly useful for vessels in environments that are exposed to strong magnetic disturbances on a regular basis (such as offshore wind farms or very busy rivers, for example). In

<!-- figure 1 on pdf page 31 at 38,29-314,139 pt | caption: none | text-layer labels: none | nearby labels: Compass deviation | OCR text follows (tesseract, unverified; 19/23 words >= 60, mean confidence 83) -->
Evolution
has
and compensated for local Earth’s magnetic
fields.
Max deviation:
6.4
Linearisation will continue in the background.
OK
<!-- end of figure 1 -->

<!-- pdf page 32 | printed page 32 -->

these situations it may be desirable to use the Compass lock feature to disable the continuous linearization process, as the magnetic interference may build a heading error over time.

Note: The compass lock may be released at any time, to allow the compass continual monitoring and adaptation to re-commence. This is particularly useful if planning a long voyage. The earth’s magnetic field will change significantly from one geographical location to another, and the compass can continually compensate for the changes, ensuring you maintain accurate heading data throughout the voyage.

###### Locking the compass

- Follow the steps below to lock the compass linearization.
- From the Commissioning menu: ([Menu > Set-up > Autopilot Calibration > Commissioning])
1. Select [Compass Lock].
2. Select [On]. The compass linearization is now locked.

<!-- pdf page 33 | printed page 33 -->

## CHAPTER 6: COMMISSIONING — SPX AND SMARTPILOT SYSTEMS

##### CHAPTER CONTENTS

<!-- pdf page 34 | printed page 34 -->

### 6.1 SPX and SmartPilot autopilot installation

For information on installing and connecting a SeaTalk NG SPX autopilot system or a SeaTalk SmartPilot autopilot system, refer to the installation instructions that accompanied your course computer.

### 6.2 Pilot response

The response level controls the relationship between course keeping accuracy and the amount of helm/ drive activity. Range is from 1 to 9.

###### Making temporary changes to pilot response

Pilot response is set up during commissioning of the SmartPilot system however you can make temporary changes to the pilot response at any time using the [Pilot response] menu: [Menu > Pilot Response]. The Pilot response level can be adjusted from level 1 to 9. • Levels 1 to 3 — Minimize the amount of pilot activity. This conserves power, but may compromise short-term course-keeping accuracy. • Levels 4 to 6 — Should give good course keeping with crisp, well controlled turns under normal operating conditions. • Levels 7 to 9 — Gives the tightest course keeping and greatest rudder activity (and power consumption). This can lead to a rough passage in open waters as the SPX system may ‘fight’ the sea. To adjust Pilot response follow the steps below: 1. From the Main menu highlight [Pilot response] and press [Select]. 2. Use the [UP ]and [DOWN ]buttons to change the response value to the required level. 3. Press [Save] to save the response value.

### 6.3 Commissioning

###### Commissioning pre-requisites

Before commissioning your autopilot system for the first time, ensure that you have read through and understood the entire commissioning instructions for your autopilot system.

Before commissioning, you should also ensure the following:
- All autopilot system components have been installed in accordance with the installation instructions supplied with the system components.
- All autopilot system components have been updated to the latest available software versions, available on the Raymarine website.
- A system schematic is available which includes all system components and required connections.
- The commissioning engineer is familiar with the vessel’s hull type, drive type and steering system.

###### Commissioning process

- Check you have adhered to commissioning pre-requisites
- Initial power on and set-up
- Dockside calibration (Dealer Settings on SeaTalk systems)
- Set hard over time (non-rudder reference systems only)
- Sea trial calibration
- System checks

### 6.4 Powering on and off

The p70s / p70Rs automatically powers on when power is supplied to the network it is connected to, unless it has been powered off using the [Standby] button. 1. If the display has been powered off using the standby button, press and hold [Standby] for approximately 2 seconds, to power the display on again. 2. To power the display off, press and hold the [Standby] button for approximately 5 seconds. After 1 second, a 3 second countdown is displayed. The display cannot be powered off when the autopilot is engaged.

<!-- pdf page 35 | printed page 35 -->

### 6.5 Using the Set-up Wizard

- The set-up wizard guides you through the steps for setting important preferences, such as preferred language and correct vessel type.
- The Set-up Wizard contains 3 steps: Language Selection, Vessel Hull Type selection and Welcome Screen. When powering the Pilot Controller for the first time, in an unconfigured system, the Set-up Wizard is displayed automatically, and the first 3 steps listed below will not be required.
- With the pilot in Standby mode:
1. Select [Menu].
2. Select [Set-up].
3. Select [Set-up Wizard].
4. Select the required language.
5. Select the required vessel type. The welcome screen will now be displayed and your choices have been saved.
6. Select [OK] to complete the Set-up Wizard.

###### Vessel hull type selection

The vessel hull type options are designed to provide optimum steering performance for typical vessels. It is important to complete the vessel hull type selection as part of the initial set-up wizard, as it forms a key part of the autopilot calibration process. You can also access the options at any time with the pilot in Standby by selecting [MENU > Set-up > Autopilot Calibration > Vessel Settings > Vessel Hull Type]. As a general guide, select the option that most closely matches your vessel type and steering characteristics. The options are: • [Race Sail]. • [Sail Cruiser]. • [Catamaran]. • [Workboat] . • [RIB]. • [Outboard Speedboat] • [Inboard Speedboat]

- [Power Cruiser 1 (<12 kts)]
- [Power Cruiser 2 (<30 kts)]
- [Power Cruiser 3 (>30 kts)]
- [Sport Fishing]
- [Pro Fishing] It is important to be aware that steering forces (and therefore rate-of-turn) vary significantly depending on the combination of vessel type, steering system, and drive type. Therefore, the available vessel hull type options are provided for guidance only. You may wish to experiment with the different vessel hull type options, as it might be possible to improve the steering performance of your vessel by selecting a different vessel type. When choosing a suitable vessel type, the emphasis should be on safe and dependable steering response.

Important: If you change the vessel type after completing the Dockside calibration process (using the Dockside wizard), all commissioning settings will be reset to default settings, and you will need to complete the Dockside calibration process again.

### 6.6 Dockside calibration

The dockside calibration process must be completed before your SPX autopilot system can be used for the first time. The Dockside wizard guides you through the steps required for dockside calibration. The Dockside wizard contains different steps, depending on whether the system includes a rudder reference transducer:

<!-- pdf page 36 | printed page 36 | header: Description -->

<!-- list markers drawn on the page, not in the text layer (from the rendered page): "transducer:" -->

For vessels without a rudder reference
- transducer:
- Drive Type selection.
- Rudder Limit setting.
- Rudder Drive check. For vessels with a rudder reference transducer:
- Drive Type selection.
- Align Rudder (rudder alignment).
- Rudder Limit setting.
- Rudder Drive check.

On older SeaTalk SmartPilot systems, the Dockside wizard is named Dealer Settings. For calibration details, please refer to: p.37 — Dealer settings

###### Using the Dockside wizard

- To access the dockside wizard follow the steps below: Ensure the pilot is in Standby.
1. Select [Menu].
2. Select [Set-up].
3. Select [Autopilot Calibration].
4. Select [Commissioning].
5. Select [Dockside Wizard].
6. Follow the on-screen instructions.

- Note: You can cancel the Dockside wizard at any time by pressing the [Standby] button.

###### Selecting a drive type

Drive type selection is included in the dockside wizard. If your drive type is not listed, contact your Raymarine dealer for advice. With the [Drive Type] menu displayed:

1. Select your drive type. The drive types available are:
- Type 1 / Type 2 Linear
- Type 2 / Type 3 Hydraulic Linear
- I/O Stern
- Wheel Drive
- Tiller
- Sport Drive
- Verado
- Rotary Drive Type 1 / Type 2
- Hydraulic Pump Type 1 / Type 2 / Type 3 Drive type selection is also available when the autopilot is in standby, from the [Drive Type] menu: [Menu > Set-up > Autopilot Calibration > Vessel Settings > Drive type].

###### Checking the rudder alignment (Align Rudder)

This procedure establishes port and starboard rudder limits for systems using a rudder reference transducer. Scenario             Description

The following procedure only applies to vessels with a rudder reference transducer.

1. Center the rudder and select [OK].
2. When prompted, turn the rudder hard to port and select [OK].
3. When prompted, turn the rudder hard to starboard and select [OK].
4. When prompted, turn the rudder back to the center and select [OK].

<!-- figure 1 on pdf page 36 at 43,53-120,94 pt | caption: none | text-layer labels: none | nearby labels: Scenario | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 36 at 43,127-120,168 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 36 at 334,312-607,355 pt | caption: none | text-layer labels: none | nearby labels: Scenario | Description | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 93) -->
2
<!-- end of figure 3 -->

<!-- pdf page 37 | printed page 37 -->

###### Rudder Limit setting

Scenario             Description

For vessels without a rudder reference transducer: Rudder limit is set to 30 degrees and can be adjusted as required(*) using the [Up] and [Down] buttons or the [Rotary controller]. For vessels with a rudder reference transducer: The rudder alignment process establishes the rudder limit. The rudder limit will be displayed with a message confirming that the rudder limit has been updated. If required, the limit can be adjusted(*) using the [Up] and [Down] buttons or the [Rotary controller].

- Note: *In systems with an ACU-300 and a Constant Running pump, the rudder limit is set to 30 degrees, and cannot be changed.

###### Checking the rudder drive

As part of the dockside calibration process, the system will check the drive connection. Once it has completed the check successfully, a message will appear asking if it is safe for the system to take the helm. During this procedure the autopilot will move the rudder. Ensure it is safe to proceed before pressing OK. When in dockside calibration mode, with the Motor Check page displayed: 1. Centre and let go of the rudder. 2. Disengage any rudder drive clutch. 3. Select [CONTINUE]. 4. Check it is safe to proceed before selecting [OK]. For vessels with a rudder reference transducer, the autopilot will now automatically move the rudder to port and then starboard. 5. For vessels without a rudder reference transducer: i. You will be asked to confirm that the rudder has turned to port by selecting [YES ] or [NO].

ii. Select [OK] if it is safe to engage the rudder in the opposite direction.
iii. You will be asked to confirm the rudder turned to starboard by selecting [YES] or [NO].
6. Dockside calibration is now complete, select [CONTINUE].

Note: If you confirmed a “NO” response for the rudder movement to both port and starboard, the wizard will exit. It is possible that the steering system did not move the rudder in any direction, and it will be necessary to check the steering system before completing the Dockside wizard procedure again.

### 6.7 Dealer settings

The dockside calibration wizard is only available on a SeaTalk NG system. For SeaTalk systems, the [Dealer settings] should be set before going out on the water. The dealer settings menu can be accessed from: [Main menu > Set up > Auto pilot calibration > Dealer settings]. Once entered, the dealer settings menu will cycle through all available options. Options and limits are dependent on the course computer installed.

### 6.8 Adjusting the hard-over time — SmartPilot and SPX

On vessels without a rudder reference transducer, it is important to set a Hard Over Time. Before attempting to follow this procedure ensure you have read and understood the Rudder Check warning provided in this document. To estimate your hard over time follow the steps below: 1. Adjust your Rudder Gain setting to the maximum value, making a note of the original value. The Rudder Gain setting can be accessed from the Drive Setting menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Rudder Gain]. 2. With the autopilot in [Standby], manually turn the rudder / engine full to port. (For vessels with power steering the engine should be running when turning the rudder.) 3. Engage [Auto] mode.

<!-- figure 1 on pdf page 37 at 43,125-120,166 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 38 | printed page 38 -->

4. Press the [+10] and [+1] buttons at the same time (p70/p70s) or use the [Rotary] (p70R/p70Rs) to alter your locked heading by 90 degrees, use a stop watch to time the movement of the rudder / engine.
5. Estimate how long it would take to move the rudder from full port to full starboard. This estimate is your [Hard Over Time].
6. Enter this estimate as your Hard Over Time. The Hard Over time setting can be accessed from the Drive Settings menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Hard Over Time].
7. Change your Rudder Gain back to its original value.
8. After setting your Hard Over Time, observe your autopilot’s behavior and if required, make small adjustments to the Hard Over Time value until a satisfactory result it achieved.

###### Warning: Rudder check

If no rudder reference has been fitted you MUST ensure that adequate provision is made to prevent the steering mechanism from impacting the end stops.

### 6.9 Sea trial calibration

- Before you can use the autopilot open water checks are required. The water must be calm, with light or no wind. Leave plenty of room to manoeuvre. The Sea Trial wizard guides you through the steps required for Sea trial calibration.
- The Sea trial wizard includes the following steps:
- Swing compass
- Align compass to GPS
- Align compass manually
- Auto Learn. You can access the Sea trial wizard at any time from the
- Commissioning menu: [Menu > Set-up > Autopilot calibration > Commissioning].

- Note: Sailing vessels should perform the sea trial under engine power.

- Note: The Sea trial wizard can be cancelled at any time by pressing the [Standby] button.

###### Warning: Seatrial calibration

Ensure you have sufficient sea room for calibration. The seatrial calibration maneuvers require a clear, familiar area of water. Ensure you are not likely to collide with any vessel or other obstruction during calibration.

###### Warning: Maintain sensible speeds

###### Compass swing

You will need to turn your vessel in slow circles while the system automatically makes adjustments to account for compass deviation. Each 360-degree circle should take no less than two minutes, and you should complete at least two circles. 1. Start moving vessel in slow even circles, then press [START] . 2. Keep speed to below 2 knots. Watch the display to ensure your turn rate is not too fast. If the message ‘Slow Down’ is displayed reduce your rate of turn, this can be achieved by slowing down and / or steering in a wider circle. If a 'Slow Down' message is displayed the current circle will have to be repeated. 3. When the compass has been calibrated, a message will be displayed showing the detected deviation. If this is more than 15 degrees you will need to abort the calibration process and re-site the compass further away from metal items, then repeat the calibration process. If you still find a deviation of more than 15 degrees, contact your Raymarine dealer for advice. If the deviation is within acceptable limits, press [CONTINUE]. You can cancel Seatrial calibration at any time by pressing [STANDBY] .

<!-- figure 1 on pdf page 38 at 334,70-379,146 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 38 at 547,70-607,146 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 80) -->
ea
<!-- end of figure 2 -->

<!-- figure 3 on pdf page 38 at 334,151-607,192 pt | caption: none | text-layer labels: Warning: Maintain sensible speeds | The autopilot may make unexpected turns. | nearby labels: Compass swing | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 4 on pdf page 38 at 41,180-86,242 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 5 on pdf page 38 at 226,180-314,240 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 39 | printed page 39 -->

###### Aligning compass to GPS

Note: If you have a system without a source of GPS data, skip this section and proceed to Manual compass alignment.

If your system has a GPS connected to your data network (SeaTalk, SeaTalk NG, or NMEA), the autopilot is tuned to the GPS heading while you steer to a known magnetic heading. This step provides a rough alignment and minimizes the amount of compass fine-tuning required. As part of the align to GPS process, the autopilot system will compare the average heading with the average COG (Course Over Ground) value reported by the source of GPS data, and set an offset value so that the heading matches the COG value provided by the GPS. 1. To align the compass to GPS, steer the vessel on a steady course with minimal tide, increase speed to more than 3 knots, and then press [START] . 2. To begin the AutoLearn process, follow the on-screen instructions until the process completes, then press the [CONTINUE] button when displayed. You can cancel the Sea trial calibration process at any time by pressing [STANDBY] .

###### Aligning compass manually

Where no GPS is present manual alignment of the compass is required. 1. Continue to steer on a steady course and use the Use [+1°] and [-1°] buttons, or the [ROTARY] controller to adjust the heading displayed until it matches the vessel’s compass reading. 2. When complete press [CONTINUE] to begin [AutoLearn] .

###### Auto Learn

You must have significant clear water in front of the vessel to accommodate a series of maneuvers, which include sudden, sharp turns. There should be a clear area at least 100 m wide and 500 m ahead.

###### Caution: Autolearn

Please ensure sufficient free space ahead. (Minimum 100x500m long & significantly more for a high speed vessel.

###### Performing Auto learn

Auto learn is available from the Sea trial wizard, or from the [Commissioning menu]. Maintain a normal cruising speed (at least 3 kts) throughout the auto learn process. 1. Ensure there is sufficient free water in front of the vessel and select [continue]. A warning message is displayed. 2. Select [Continue] or press the [Ok] button. A warning message will be displayed letting you know that the vessel will zigzag and make Sudden SHARP TURNS. 3. Remove your hands from the wheel and press [Auto] to begin. During this procedure the autopilot will progress through the required steps. 4. If ‘PASS’ is displayed then select [Continue] or press the [Ok ] button to return to manual helm control. The autopilot will by placed in Standby mode. You have successfully completed the commissioning process for your SmartPilot system.

<!-- figure 1 on pdf page 39 at 334,89-607,173 pt | caption: none; nearest centred text below: "Caution: Autolearn" | text-layer labels: none | nearby labels: Caution: Autolearn | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 39 at 334,178-607,238 pt | caption: none | text-layer labels: Caution: Autolearn | nearby labels: Performing Auto learn | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 40 | printed page 40 -->

5. If ‘FAIL’ is displayed after completion of the Auto learn process then select [Continue] or press the [Ok] button. The Auto learn retry message is displayed.
6. You can retry the Auto learn process by selecting [Yes] or to cancel select [No].

- Note: The Sea trial wizard can be cancelled at any time by pressing the [Standby] button.

###### Caution: System changes

Any additional changes you make to your system settings may require you to repeat the calibration process.

### 6.10 Checking autopilot operation

After completing calibration, check the basic autopilot operation, as follows: 1. Steer onto a compass heading and hold a steady course at normal cruising speed. If necessary, steer the vessel manually for a short time to check how the vessel steers. 2. Ensure it is safe to engage the autopilot, then press [AUTO] to lock onto the current heading. The autopilot should hold a constant heading in calm sea conditions. 3. Use [-1°], [+1°], [-10°] and [+10°] or the [ROTARY] controller, to see how the SmartPilot alters the course to port and starboard. 4. Press [STANDBY] to return to manual steering.

###### Checking rudder gain

- To determine whether the rudder gain is set correctly, carry out the
- following test:

1. Rudder gain too low
2. Rudder gain too high
3. Correct rudder gain
1. Ensure you have set the autopilot response to level 5.
2. Drive your vessel at a typical cruising speed in clear water. It is easier to recognize the steering response in calm sea conditions where wave action does not mask steering performance.
3. Press [AUTO] to enter Auto mode, then alter course by 40°:
- This course change should result in a crisp turn followed by an overshoot of no more than 5°, If the rudder gain is adjusted correctly.
- If the course change causes a distinct overshoot (more than 5°) and/or there is a distinct ‘S’ in the course the rudder gain is too high.
- If the vessel’s performance is sluggish and it takes a long time to make the 40° turn, with no overshoot the rudder gain is too low. If necessary, adjust the rudder gain.

<!-- figure 1 on pdf page 40 at 334,74-607,192 pt | caption: none | text-layer labels: none | nearby labels: 1. | Rudder gain too low | 2. Rudder gain too high | OCR: no legible text (0/1 words >= 60, mean confidence 28) -->

<!-- figure 2 on pdf page 40 at 41,139-86,197 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 3 on pdf page 40 at 238,139-314,197 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 41 | printed page 41 -->

###### Checking counter rudder

Counter rudder is the amount of rudder your autopilot applies to try to prevent your vessel from over steering. A higher counter rudder setting results in more rudder being applied. To check the counter rudder setting: 1. Ensure you have set the autopilot response to level 5. 2. Drive your vessel at a typical cruising speed in clear water. 3. Press [AUTO] and if necessary engage the autopilot. 4. Make a 90° course change: • When rudder gain and counter rudder are both set correctly, the vessel performs a smooth continuous turn with minimal overshoot. • If the counter rudder is too low, the vessel will overshoot before returning slowly to the course. • If counter rudder is too high, the vessel will ‘fight’ the turn and make a series of short, sharp turns. This results in a very ‘mechanical’ feel as the vessel changes course. 5. If necessary, adjust the counter rudder setting. Counter Rudder is available from the [Drive Settings] menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Counter Rudder].

###### Rudder Damping

If the autopilot is ‘hunting’ (i.e. continuously moving the steering backwards and forwards by small amounts) when trying to position the rudder, the rudder damping setting will require adjustment to minimize this. Increasing the rudder damping value reduces hunting. The rudder damping value should be increased 1 level at a time until the autopilot stops hunting. Always ensure the lowest acceptable value is used. If required the Rudder Damping setting can be adjusted from the Drive Settings menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Rudder Damping].

###### AutoTrim settings

AutoTrim determines how quickly the autopilot applies ‘standing helm’ to correct for trim changes, caused, for example, by changes in the wind load on the superstructure, or an imbalance of engines.

Increasing the AutoTrim level reduces the time the autopilot takes to return to the correct course, but makes the vessel less stable. If the autopilot: • Gives unstable course keeping and the vessel ‘snakes’ around the desired course, decrease the AutoTrim level. • Hangs off course for excessive periods of time, increase the AutoTrim level.

- Note: AutoTrim is only available for SPX Autopilot systems.

<!-- pdf page 42 | printed page 42 -->

## CHAPTER 7: AUTOPILOT MODES

##### CHAPTER CONTENTS

<!-- pdf page 43 | printed page 43 -->

### 7.1 Auto

###### Caution: Maintain a permanent watch

Automatic course control makes it easier to steer your vessel, but it is NOT a substitute for good seamanship. ALWAYS maintain a permanent watch at the helm.

###### Automatically steering to a heading

1. Steady the vessel on the required heading.
2. For Wheel and Tiller drive systems see below instructions for engaging the autopilot.
- A — Wheel Pilot: Engage the wheel drive clutch by rotating the clutch lever clockwise (so the lever fully engages onto the locating pip (small protruding circle)).

Important: Always reach around (not through) the wheel to operate the wheel pilot’s clutch lever.

- B — Tiller Pilot: Place the pushrod end over the tiller pin. If necessary, extend or retract the pushrod using the [-1°], [+1°], [-10°], [+10°] buttons, or the [Rotary] control.

3. Press [AUTO] . The autopilot is now in Auto mode and will steer to the chosen locked heading.

###### Changing course in auto mode

Vessel course can be adjusted when the autopilot is engaged ([AUTO] mode). 1. Use the [–1°] button, [–10°] button, or turn the rotary controller counter-clockwise to change the vessel's course to port. Pressing the [–1°] button will increment the course to port by 1º and [–10°] will increment by 10°. Turning the rotary controller one click counter-clockwise will increment the course to port by 1° . 2. Use the [+1°] button, [+10°] button, or turn the rotary controller clockwise to change the vessel's course to starboard. Pressing [+1°] button will increment the course to starboard by 1º and [+10°] will increment by 10°. Turning the rotary controller one click clockwise will increment the course to Starboard by 1°. 3. Use the [–1°] and [–10°] buttons together to perform an [Auto Turn] to port. Pressing the buttons together will automatically turn the vessel to the angle specified in the [Auto Turn] setting, to port. 4. Use the [+1°] and [+10°] buttons together to perform an [Auto Turn] to starboard. Pressing the buttons together will automatically turn the vessel to the angle specified in the [Auto Turn] setting, to starboard. Example: pressing the [-1°] button 4 times, or turning the rotary 4 clicks counter-clockwise will result in a 4° course change to port.

Note: By default the [Auto Turn] angle is set to 90°. The turn angle can be configured via the Autopilot settings available on a compatible MFD, using the [Drive Settings] menu: [Menu > Set-up > Autopilot Calibration > Drive Settings > Auto Turn].

###### Disengaging the autopilot (Standby mode)

The autopilot can be disengaged by following the steps below.
1. Press [Standby].
2. For Wheel and Tiller drive systems, refer to the instructions below for disengaging the autopilot to return to manual steering.
- Wheel Pilot: Disengage the wheel drive clutch by rotating the clutch lever counter-clockwise (so that the lever disengages fully from the locating pip (small protruding circle)).

<!-- figure 1 on pdf page 43 at 41,50-86,108 pt | caption: none | text-layer labels: none | nearby labels: 7.1 Auto | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- figure 2 on pdf page 43 at 53,305-314,439 pt | caption: none | text-layer labels: none | OCR: no legible text (0/3 words >= 60, mean confidence 19) -->

<!-- pdf page 44 | printed page 44 -->

- Tiller Pilot: Remove the drive unit from the tiller pin. If necessary, extend or retract the pushrod using the [-1°], [+1°], [-10°], or [+10°] buttons, or the [Rotary] control.

Important: On wheel drive systems, always ensure that the clutch is fully disengaged before you disembark from the vessel.

### 7.2 Mode menu

Pilot modes are accessed from the [Mode] menu. The available modes are determined by the type of connected autopilot system and the Vessel Hull Type selected during the Set-up Wizard. The following modes are available:

###### Evolution™ autopilots

- [Pattern] — Available for Power vessels.
- [Track] — Available for all vessels.
- (1)[Wind vane] — Available for Sailing vessels.
- (2)[Power Steer] — Available on p70R / p70Rs and joystick only.

###### SPX SmartPilot autopilots

- [Pattern] — Available for Motor and Fishing vessels.
- [Track] — Available for all vessels.
- (1)[Wind vane] — Available for Sailing vessels.
- (2)[Power Steer] — Available on p70R / p70Rs and joystick only.

Note:
(1) [Wind vane] mode is only available if there is a connected source of wind data.
(2) [Power steer] mode is only available on vessels fitted with a rudder reference transducer / position sensor.

The mode menu also provides a shortcut key option that enables a mode to be assigned to the [Left Soft] button (the default option is [Track] ).

### 7.3 Patterns

Fishing patterns are available, that can be used with their default settings or adjusted to your own preference. Fishing patterns require GNSS (GPS) data to be available on your system. The following patterns are available:

1. [Circle] — The direction and radius of the pattern can be adjusted.
2. [Zig Zag] — The direction, angle and length of the pattern can be adjusted.
3. [Cloverleaf] — The direction and radius of the pattern can be adjusted.
4. [Spiral] — The direction, radius and increment of the pattern can be adjusted.
5. [Circle against] — The direction, radius and distance of the pattern can be adjusted.
6. [Figure 8] — The direction and radius of the pattern can be adjusted.
7. [Pattern search] — The direction, width, height, width increment and height increment of the pattern can be adjusted.
8. [180 turn] — The direction and radius of the pattern can be adjusted.
9. [Box search] — The direction, width and height of the pattern can be adjusted.

Using a ﬁshing pattern
1. Press the [RIGHT SOFT ]button to open the menu.
2. Using the [UP] and [DOWN] buttons highlight [Mode] and press [SELECT].
3. Using the [UP] and [DOWN] buttons highlight [Pattern] and press [SELECT].

<!-- figure 1 on pdf page 44 at 334,101-607,185 pt | caption: none | text-layer labels: none | nearby labels: 1. | OCR below floor, text not used (1/6 words >= 60, mean confidence 36) -->

<!-- pdf page 45 | printed page 45 -->

4. Using the [UP] and [DOWN] buttons highlight the fishing pattern you wish you use and press [SELECT].
5. The pattern settings screen shall be displayed, showing the parameters currently set for the selected pattern. If you want to change any of the parameters:
i. Select the parameter you want to change, then press [EDIT].
ii. Use the [UP] and [DOWN] buttons to set the value you want, then press [SAVE] to save the setting and return to the Pattern settings screen.
iii. Repeat steps i and ii as necessary, for the other parameters.
6. Where appropriate, engage the wheel pilot clutch or attached the tiller pushrod.
7. With the pattern settings screen displayed, press [AUTO] . The autopilot then steers the boat over the fishing pattern you selected. To return to manual steering at any time, press [STANDBY] and then, where appropriate, disengage the wheel pilot clutch or tiller pushrod. The 2 most commonly used fishing patterns are available from the [Mode] menu as [Pattern 1] and [Pattern 2], you may select and then complete steps 5 and 6 above to quickly use your favorite patterns.

### 7.4 Track mode

In Track mode, the autopilot automatically steers your vessel to a target waypoint or along a route plotted on your MFD. It makes any course corrections necessary to keep your vessel on course, automatically compensating for tidal streams and leeway. Track mode is available only if you have connected the autopilot to a suitable MFD that has autopilot control enabled.

3. Final waypoint in route.

###### Using track mode

Start with your connected chartplotter following a route. From the menu: 1. Select [Mode]. 2. Select [Track] . The display will show the bearing to the next planned waypoint, and the direction in which the vessel will turn onto the track line. 3. If it is safe for the vessel to turn onto the new course, select [Track] . The autopilot turns your vessel onto the new course with the display showing the heading required for the correct track.

- Note: If the vessel is more than 0.3 nm from the track, the Large Cross Track Error warning will sound.

###### Waypoint arrival circle

The Waypoint arrival circle is an imaginary boundary line placed around a waypoint which, when reached, triggers the waypoint arrival alarm. As the alarm is triggered by the waypoint arrival circle and not the waypoint your vessel may still be some distance from the actual waypoint when the alarm sounds. The size of the waypoint

<!-- figure 1 on pdf page 45 at 38,343-314,446 pt | caption: none | text-layer labels: none | nearby labels: 1. | Current goto / waypoint. | 2. Subsequent waypoints in a route. | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 46 | printed page 46 -->

| arrival circle can be customized, if the arrival circle is changed so that | Waypoint arrival |
| --- | --- |
| the radius is 0.3 nm or greater from the waypoint this can result in | As the vessel arrives at the target waypoint’s arrival circle the MFD |
| a cross track error alarm. | will select the next target waypoint in the route and transmit this to the autopilot. A Waypoint advance warning is displayed that will identify the bearing to the next waypoint and the direction the vessel will turn to acquire the new track. |

| 1.   Next waypoint | 1.   Next waypoint |
| --- | --- |
| 2. Bearing to next waypoint | 2. Waypoint arrival circle |
| 3.   Track line | 3.   Target waypoint |
| 4.   Waypoint arrival circle | 4.   Next waypoint arrival circle |
| 5. Cross track error | 5. Next target waypoint 6. Previous waypoint Waypoint advance warning The autopilot activates the Waypoint Advance warning in track mode whenever the target waypoint name changes. This occurs when: • you select automatic acquisition by pressing [Track] from Auto. • you request waypoint advance by pressing [Track] for 1 second in track mode (with SeaTalk navigators only). • the boat arrives at the target and the navigator accepts the next waypoint. • you activate the Man Overboard (MOB) function. When the warning sounds, the autopilot continues on its current heading but displays: • the bearing to the next waypoint. |

<!-- figure 1 on pdf page 46 at 38,70-314,230 pt | caption: none | text-layer labels: none | nearby labels: 1. | Next waypoint | 1. | 2. Bearing to next waypoint | OCR text follows (tesseract, unverified; 3/7 words >= 60, mean confidence 52) -->
1?
2?
an
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 46 at 334,101-607,238 pt | caption: none | text-layer labels: none | nearby labels: 1. | Next waypoint | 2. Waypoint arrival circle | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 48) -->
1?
<3
<!-- end of figure 2 -->

<!-- pdf page 47 | printed page 47 -->

- the direction the boat will turn to take up that bearing.

- Arriving at a waypoint As you approach each waypoint, an alarm sounds and the waypoint arrival notification is displayed. The notification includes options so you can choose how to proceed.
- When the waypoint arrival alarm is triggered:
1. Check that it is safe to turn onto the new heading.
2. If it is NOT safe or you do not want to advance to the next
- waypoint you can:
i. Select [Cancel] or [Auto] to remain on the same heading, or
ii. Select [Standby] to return to manual steering.
3. If it is safe select [TRACK] to accept the new heading and proceed to the next waypoint.

1. Next waypoint.
2. Track line.
3. Waypoint arrival circle.
4. [Track] — Track to next waypoint.
5. [Standby] — Manual helm control.
6. [Auto] or [Cancel] — Maintain current locked heading.

Note: If you do not press [Track] to accept the Waypoint advance, the autopilot will maintain the current heading and continue sounding the warning.

Cross track error Cross track error (XTE) is the distance between the current position and a planned track line. There are a number of reasons why you may have a cross track error (XTE), for example: • Pressing the track button at a position some distance from the route. • Course change to avoid an obstacle. • Waypoint arrival under certain conditions. If the cross track error is greater than 0.3 nm, the SmartPilot will sound the Large cross track error alarm and show whether you are to the port (Pt) or starboard (Stb) of the planned track.

1. Target waypoint
2. Course correction that will initially turn away from the actual waypoint in order to reacquire the track line.
3. Cross track error
4. Track line

Note: The cross track error alarm will continue to display and sound until it is reduced to less than 0.3 nm.

<!-- figure 1 on pdf page 47 at 38,197-314,362 pt | caption: none | text-layer labels: none | nearby labels: 1. | Next waypoint. | 2. Track line. | 1. | OCR below floor, text not used (3/15 words >= 60, mean confidence 29) -->

<!-- figure 2 on pdf page 47 at 334,228-607,362 pt | caption: none | text-layer labels: none | nearby labels: 1. | Target waypoint | OCR text follows (tesseract, unverified; 3/4 words >= 60, mean confidence 61) -->
*4
ff
a
<!-- end of figure 2 -->

<!-- pdf page 49 | printed page 49 -->

###### Using wind vane mode

You can select [Wind vane] mode from either [STANDBY] or [AUTO ] mode: 1. Steady the vessel onto the required wind angle. 2. Select [Wind vane] mode from the modes menu: [Menu > Mode > Wind vane]. This will enable Wind vane mode and lock the current wind angle. The display shows the locked heading (e.g. 128°) and the wind angle (e.g. WIND 145P indicates a wind angle of 145° to port). 3. The autopilot will then adjust the vessel’s heading to maintain the locked wind angle.

###### Operating hints for Wind vane mode

- Always trim your sails carefully to minimize the amount of standing helm.
- Reef the headsail and mainsail a little early rather than too late.
- In Wind vane mode the autopilot will react to long-term wind shifts, but will not correct for short-term changes such as gusts.
- In gusty and unsteady inshore conditions, it is best to sail a few degrees further off the wind so that changes in wind direction can be tolerated.
- Avoid using AutoTack in conditions where the wind may shift suddenly.

###### Caution: Allow time

Always allow adequate time for course changes.

###### Caution: Major course changes

When making major course changes, the trim on the boat may change substantially. Due to this, the autopilot may take some time to settle accurately onto the new course.

Accidental gybes The gybe inhibit feature stops the vessel from turning away from the wind if you accidentally perform an AutoTack in the wrong direction.

- Note: For the gybe inhibit feature to work, the autopilot requires suitable wind data.

With gybe inhibit set to [Prevent Gybe]:
- you will be able to perform an AutoTack through the wind.
- the autopilot will prevent the boat from performing an AutoTack away from the wind. With gybe inhibit set to [Allow Gybe]:
- you can perform an AutoTack through or away from the wind.

- Note: Gybe inhibit feature can be changed from the Sail Boat
- Settings menu: [Menu > Set-up > Autopilot Calibration > Sail Boat Settings > Gybe Inhibit ].

###### Adjusting the locked wind angle

1. You can adjust the locked wind angle by using the [-1°], [+1°], [-10°] and [+10°] buttons, or the [ROTARY] controller to change course. For example, to bear away by 10° when the boat is on a starboard tack:
i. Press [-10°] to turn the boat 10° to port – the locked wind angle and locked heading will both change by 10°.
ii. The autopilot will then adjust the locked heading as required to maintain the new wind angle.

Note: Because turning the vessel affects the relationship between the true and apparent wind angles, you should only use this method to make minor adjustments to the wind angle. For major changes, return to [STANDBY] mode, steer onto the new heading, and then re-select [Wind vane] mode.

###### Leaving Wind vane mode

To leave Wind vane mode:
1. Press [AUTO] to return to Auto mode (autopilot control); or:
2. Press [STANDBY] to return to Standby mode (manual steering).

<!-- pdf page 50 | printed page 50 -->

###### Wind Shift Alarm

###### Evolution autopilot

If the autopilot detects a wind shift of more than 30° for 60 seconds it will trigger the Wind Shift Alarm.

###### SPX and SmartPilot

If the autopilot detects a wind shift of more than 15° it will trigger the Wind Shift Alarm.

###### Enabling or disabling the Wind Shift alarm

- The Wind Shift alarm is enabled by default, but you can enable or disable it manually, at any time.
- In Wind Vane mode:
1. Select [Sail Boat Settings] from the [Autopilot Calibration] menu: ([Menu > Set-up > Autopilot Calibration > Sail Boat Settings]).
2. Select [Wind Shift Alarm].
3. Select Off to disable the alarm, or On to enable the alarm.

###### Responding to the wind shift warning

1. To cancel the warning, and retain the existing wind angle and heading, press [Cancel].
2. Alternatively, to cancel the warning and return to the previous heading:
i. Adjust the locked wind angle using the [-1°], [+1°], [-10°] and [+10°] buttons or the [Rotary] controller.
ii. Press [Standby ] to return to manual steering, steer to the required heading, and then press [Cancel] to return to Wind Vane mode using the new wind angle.

###### Using AutoTack in Wind Vane mode

The autopilot has a built-in automatic tack facility (AutoTack) which turns your vessel "relative" to the wind angle you're currently on, and then tacks the vessel to put you on the opposite relative wind angle.

1. Starting position
2. Tack
3. Wind direction
4. Final position AutoTack is always relative to wind angle and is not adjustable. In Wind Vane mode:
1. Using a p70 / p70s:
i. Press the [-1°] and [-10°] buttons at the same time to Tack to port.
ii. Press the [+1°] and [+10°] buttons at the same time to Tack to starboard.
2. Using a p70R/ p70Rs:
i. Select [Tack Port] from the main menu to Tack to port.
ii. Select [Tack Starboard] from the main menu to Tack to starboard. When you AutoTack in Wind Vane mode, the vessel turns through the AutoTack angle. The autopilot will then trim the heading to mirror the locked wind angle from the previous tack.

<!-- figure 1 on pdf page 50 at 334,84-607,228 pt | caption: none | text-layer labels: none | nearby labels: 1. | Starting position | 2. Tack | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 51 | printed page 51 -->

### 7.6 Power steer

Power steer mode enables you to use the rotary controller of the p70Rs or a connected joystick to directly steer the vessel on a manual heading. Power steer has 2 options: • [Proportional] — The rudder will behave in proportion to the movement of the rotary control or joystick. • [Bang Bang (Joystick only)] — The rudder will move, and remain in the same direction in which the joystick is moved.

###### Engaging power steer mode

To engage [Power steer ]mode:
1. Go to the [Mode menu] found in [Main menu > Mode].
2. Highlight [Power steer ]and press [SELECT]. You can change the type of steering at any time i.e. Proportional or Bang Bang by going to the [Power steer] settings in the [Drive settings] menu: [Main menu > Set up > Auto pilot calibration > Drive settings > Power steer].

- Note: In order to use Bang Bang mode a connected joystick is required, the p70Rs rotary will only perform in Proportional mode.

### 7.7 Jog steer (tiller pilots only)

If you have a tiller drive installed on a SeaTalk network, you can use the pilot controller to operate the ram in Jog steer mode. Jog steer mode enables you to use the pilot controller’s [-1°], [+1°], [-10°], [+10°] buttons, or the [ROTARY] controller to move the ram in and out to aid in connecting and disconnecting the ram.

- Note: Jog Steer can only be used whilst your autopilot is in [STANDBY] .

###### Using jog steer (tiller drives only)

1. Ensure your autopilot is in [STANDBY] mode.
2. To retract the ram: Use the [-1°] and [-10°] buttons, or turn the rotary controller counter-clockwise.

3. To extend the ram: Use the [+1°] and [+10°] buttons, or turn the rotary controller clockwise.

### 7.8 Shortcut key

- When in pilot view you can assign pilot modes to the [LEFT SOFT] button as a shortcut depending on which vessel type has been set up. The following pilot modes can be assigned as shortcuts:
- Track (default) — All vessels
- Pattern — Power and fishing vessels
- Power steer — All vessels (Rotary only)
- Wind vane — Sailing vessels

###### Assigning the shortcut key

- In order to assign a pilot mode as a shortcut mapped to the [LEFT
- SOFT] button follow the steps below:
1. Navigate to the [Shortcut] menu: Menu > Mode > Shortcut.
2. Select the required pilot mode.
3. Press [SAVE] .

<!-- pdf page 52 | printed page 52 -->

## CHAPTER 8: PILOT VIEWS

##### CHAPTER CONTENTS

<!-- pdf page 53 | printed page 53 -->

| 8.1 Available pilot views | • Locked heading — Auto , Wind Vane mode and Pattern mode. |
| --- | --- |
| Pilot views are used to display course and system data on the pilot | 7.   Heading type: |
| controller’s display screen. | • Magnetic |
| Pilot views are accessed from the [Pilot View] menu. The available | • True |
| pilot views are: |  |
| • [Graphic] | Note: |
| • [Large] | The heading type is determined by the language selected |
| • [Standard] | during the Set-up Wizard. |
| • [Multiple] |  |
| • [2D View] | 8. Shortcut button (Left Soft button) • Track (default) |
| 8.2 Graphic view | • Pattern |
| The Graphic view displays a partial compass. | • Wind Vane Rolling road Initiating [Track] when the pilot view is set to [Graphic view] will display the [Rolling road] view. |

| 1.     Rudder position |  |
| --- | --- |
| 2. Pilot Mode |  |
| 3.     Mode status: |  |
| • Locked wind angle — Wind Vane mode. | 1.   DTW (Distance To Waypoint) |
| • Pattern symbol — Pattern mode. | 2. Destination waypoint |
| • Power Steer symbol — Power Steer mode. | 3.   TTG (Time To Go) |
| 4.     Partial compass | 4.   Destination waypoint name |
| 5. Wind direction indicator | 5. Locked Heading |
| 6. Heading: | 6. XTE (Cross Track Error) |
| • Current heading — Standby and Power Steer mode. | 7.   Vessel position |
| Pilot views | 53 |

<!-- figure 1 on pdf page 53 at 108,226-245,312 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 15/21 words >= 60, mean confidence 74) -->
[20
2-4 Wind Vane A
330
4
we
304
674
Mag 7
Hdg
3 Track
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 53 at 401,269-538,360 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 21/24 words >= 60, mean confidence 78) -->
1 27
30
10
5-4 Track
Waypoint 7 4
DTW: 6 nm
TTG: 1h02m
LH: 051°M
XTE: 0.13nm 6
7—
Track
<!-- end of figure 2 -->

<!-- pdf page 54 | printed page 54 -->

| 8.3 Large view | 8.4 Standard view |
| --- | --- |
| The Large view has been optimized to provide the largest possible | The Standard view provides large-sized heading data combined with |
| sized text for heading data. | data boxes which provide further information. |

| 1.   Rudder position | 1.   Rudder position |
| --- | --- |
| 2. Pilot mode | 2. Pilot mode |
| 3.   Mode related info: | 3.   Mode related info: |
| • Current Heading (In Auto) | • Current Heading (In Auto) |
| • Destination waypoint name (In Track mode) | • Destination waypoint name (In Track mode) |
| • Locked wind angle (In Wind vane mode) | • Locked wind angle (In Wind vane mode) |
| • Pattern symbol (In Pattern mode) | • Pattern symbol (In Pattern mode) |
| • Power Steer symbol (In Power steer mode) | • Power Steer symbol (In Power steer mode) |
| 4.   Heading: | 4.   Heading: |

- Current Heading — (In Standby and Power steer modes)              • Current Heading — (In Standby and Power steer modes)
- Locked Heading — (In Auto, Track, Wind vane and Pattern
- Locked Heading — (In Auto, Track, Wind vane and Pattern             modes) modes)
5. Heading type (Magnetic or True)
5. Heading type (Magnetic or True)
6. Shortcut button (Left soft button):
6. Shortcut button (Left soft button):
- Track (default)
- Track (default)
- Pattern
- Pattern                                                           • Wind Vane
- Wind Vane                                                    7.   Data boxes:
- TWS (default) (True Wind Speed)
- Depth (default)

<!-- figure 1 on pdf page 54 at 401,82-538,178 pt | caption: none | text-layer labels: none | OCR below floor, text not used (4/15 words >= 60, mean confidence 50) -->

<!-- figure 2 on pdf page 54 at 108,84-245,168 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/11 words >= 60, mean confidence 74) -->
1
10
30
2 Auto
Hdg 2
6 Track
<!-- end of figure 2 -->

<!-- pdf page 55 | printed page 55 -->

| • SOG (default) (Speed Over Ground) | Note: Data items can be customized from the Pilot view menu: [Menu > Pilot view > Data Boxes] |
| --- | --- |
| Note: |  |
| Data items can be customized from the Pilot view menu: |  |
| [Menu > Pilot view > Data Boxes] | 4.   Shortcut button (Left soft button): • Track (default) |
| 8.5 Multiple view | • Pattern |

The Multiple view includes multiple data boxes for displaying        • Wind Vane information.

### 8.6 2D View

The 2D view includes a full compass dial and data boxes for displaying information.

| 1.     Rudder position |  |
| --- | --- |
| 2. Mode related info: |  |
| • Current Heading (In Auto) |  |
| • Destination waypoint name (In Track mode)              1.   Rudder position |  |
| • Locked wind angle (In Wind vane mode) | 2. Compass |
| • Pattern symbol (In Pattern mode) | 3.   Heading line |
| • Power Steer symbol (In Power steer mode) | 4.   Pilot Mode |
| 3.     Data boxes: | 5. Destination waypoint |
| • TWS (default) (True Wind Speed) | 6. Mode related info: |
| • Depth (default) | • Current Heading (In Auto) |
| • SOG (default) (Speed Over Ground) | • Destination waypoint name (In Track mode) |
| • DTW (default) (Distance To Waypoint) | • Locked wind angle (Wind vane mode) |
| • XTE (default) (Cross Track Error) | • Pattern symbol In Pattern mode) |
| • Heading (default) | • Power Steer symbol (In Power steer mode) |
| Pilot views | 55 |

<!-- figure 1 on pdf page 55 at 108,166-245,247 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 13/15 words >= 60, mean confidence 87) -->
1
2
Depth(ft)
15 62 21
DTW(nm)
XTE(nm)
Heading(M)
01
304°
5 Track
<!-- end of figure 1 -->

<!-- figure 2 on pdf page 55 at 401,204-542,295 pt | caption: none | text-layer labels: none | OCR below floor, text not used (8/22 words >= 60, mean confidence 49) -->

<!-- pdf page 56 | printed page 56 -->

| 7.   Wind direction indicator | 8.8 Setting up data boxes |
| --- | --- |
| 8. Vessel position indicator | The [Standard], [Multiple] and [2D View] pilot views include data |
| 9.   Data boxes: | boxes which you can customize to display different data. With your chosen Pilot view displayed: |
| • TWS (default) (True Wind Speed) | 1. Select the [Pilot View] menu. |
| • Depth (default) | 2. Select [Data Boxes] . |
| • SOG (default) (Speed Over Ground) | 3. Select the Data box that you want to change. A list of available data is displayed. |
| Note: | 4. Select the relevant data type from the list. |
| Data items can be customized from the Pilot view menu: |  |
| [Menu > Pilot view > Data Boxes] | Data items The following data types are available which can be displayed in |
| 10. Heading: | the data boxes: |

- Current heading — Standby and Power Steer mode.            • [Heave]
- [Depth]
- Locked heading — Auto , Wind Vane mode and Pattern mode.
- [XTE] (Cross Track Error)
11. Shortcut button (Left Soft button)
- [DTW] (Distance to waypoint)
- Track (default)
- [BTW] (Bearing to waypoint)
- Pattern
- [AWA] (Apparent wind angle)
- Wind Vane
- [AWS] (Apparent wind speed)
12. Track line
- [TWS] (True wind speed) 8.7 Setting the default pilot view                                • [TWA] (True wind angle)

| To set the pilot view to your desired layout: | • [COG] (Course Over ground) |
| --- | --- |
| 1. Go to the [Pilot view ]menu. | • [SOG] (Speed Over ground) |
| 2. Select [View type]. | • [Speed] (Speed Through Water) |
| 3. Highlight the required view: | • [Log] |
| • [Graphic] | • [Trip] |
| • [Large] | • [Sea Temp] |
| • [Standard] | • [Time] |
| • [Multiple] | • [Date] |
| • [2D View] | • [Rate of turn] |
| 4. Press the [Select ] soft button to save the view as default.   • [Heading] |  |

<!-- pdf page 57 | printed page 57 -->

## CHAPTER 9: PILOT CONTROLLER ALARMS

##### CHAPTER CONTENTS

Pilot controller alarms               57

<!-- pdf page 58 | printed page 58 -->

### 9.1 Pilot alarms

Pilot alarms are generated by the connected autopilot. They are also transmitted on the SeaTalk NG network. The following alarms can be displayed on the Pilot controller:

###### Calibration alarms

- Calibration required — Indicates that the autopilot has not been fully calibrated. Initiated in Standby mode, for a few seconds after initial power-up. Resolve by performing Dockside and Seatrial calibration.
- Detecting magnetics — Compass linearization required.
- Magnetic fields detected — Initial linearization complete, further linearization will be performed in the background.
- Turn rate too high — Indicates an excessive rate of turn whilst linearizing the fluxgate compass. Initiated during calibration. To resolve this issue, reduce the vessel’s rate of turn.

###### Navigation alarms

- Auto release — Triggered when the user has taken back control of the steering whilst the autopilot is engaged (e.g.: Auto, Track mode etc.), using the fly-by-wire steering wheel. The autopilot will drop to standby and the alarm will time out after 10 seconds.
- Large cross track error — Indicates cross track error (XTE) is greater than 0.3 nm. Alarm is triggered in Track mode or on entry to Track mode from any other mode. To resolve this issue, try:
- Manually steering back on course and entering track mode again.
- Reset XTE on the multifunction display.
- Changing autopilot settings.
- Loss of waypoint data — Indicates that the source of the waypoint data (i.e.: MFD) has been lost. The autopilot will drop out of track mode and into auto mode and continue on the last locked heading.
- No navigation data — Indicates absence of one of the following primary control data items:
- Compass – Auto, Track & Wind modes.
- XTE – Track mode.
- Wind angle – Wind vane mode.

- Off course — The off course alarm is triggered during active navigation when your vessel is more than the specified number of degrees off its track. Resolve by changing pilot mode, or changing / correcting the vessel’s course.
- Route complete — Triggered by the MFD when the last waypoint in a route has been reached.
- Waypoint advance — Indicates change in waypoint name or ID, and the direction in which to turn to the new waypoint. Triggered in Track mode.
- Wind Shift — Indicates that TWA (True Wind Angle) has changed by more than 15 degrees. Triggered in Wind vane mode only. Resolve by changing course or changing pilot mode. Will also resolve if TWA reverts back to its original value.

###### Hardware and fault alarms

- Clutch short — Indicates a short circuit in the drive unit’s clutch. The autopilot will power down.
- Current limit — Drive overload current exceeded. The autopilot will drop to standby and the alarm will time out after 10 seconds. To resolve this issue, try checking the drive unit and connections for stall or short circuit conditions.
- Drive short — Indicates a short circuit in the drive unit. The autopilot will power down.
- Drive stopped — Indicates a rudder stall condition has persisted, or that the power has been removed from the drive unit. Triggered in Auto, Track & Wind modes. To resolve this issue, check output from autopilot, drive unit and connections. The autopilot will drop to standby and the alarm will time out after 10 seconds.

Note: In Drive-By-Wire (DBW) systems which contain an EV-2 and a Volvo® Penta EVC drive interface unit, one second must pass after turning the boat's steering wheel before the autopilot can be engaged using the [Auto] button on your autopilot controller. If less than one second has passed before the [Auto] button is selected, the Drive stopped alarm will be displayed.

- EEPROM corruption — A corruption of critical configuration data has occurred. The autopilot will drop to standby and the alarm will time out after 10 seconds.

<!-- pdf page 59 | printed page 59 -->

- Pilot start up — Will display start up for 20 seconds every time the autopilot is powered up
- Rate gyro fault — The gyro sensor has failed.
- Rudder reference unit failure — Rudder Reference connection has been lost, or exceeded its limits (the Rudder reference transducer has failed while in auto; angle is more than 50 degrees or connection to rudder reference is lost). The autopilot will drop to standby and the alarm will time out after 10 seconds.
- Solenoid short — Indicates a short circuit in the solenoid. The autopilot will power down.
- SeaTalk 1 fail — SeaTalk channel 1 has a communication problem.
- SeaTalk 2 fail — SeaTalk channel 2 has a communication problem.
- SeaTalk fail — SeaTalk data transmission problem. The autopilot will drop to standby and the alarm will time out after 10 seconds. To resolve this issue, try:
- Checking connections for short or open circuit.
- Checking system for a device fault.
- Power & motor cables are swapped — this alarm occurs when the motor pair of cables and the power pair of cables are swapped. To resolve this issue, swap the motor and power cables at the course computer.

###### Device connection or data source alarms

When an alarm is triggered that indicates that a device is not detected or a required data source is missing, first check that the device / data source is operational and that all cables and connections are secure and free from damage. • No compass – Compass is not detected. • No control head — The course computer has lost communications with the Pilot controller, this alarm is generated by the course computer. The autopilot will drop to standby and the alarm will time out after 10 seconds. • No drive detected — Communication between the EV unit and ACU has been lost or cannot be established. To resolve this issue, try: – Check LED diagnostics indicators. Pilot controller alarms

- Check output from EV and ACU units.
- No pilot — The Pilot controller has lost communications with the course computer; this alarm is generated by the Pilot controller.
- No speed data — No speed data is being received. Check Speed transducer.
- No Wind data — Triggered in Wind vane mode when no Wind angle data has been received for 30 seconds or more. The autopilot will drop out of wind vane mode and revert to auto mode.

###### AutoLearn alarms

For AutoLearn failures, first try restarting the AutoLearn process.
- AutoLearn fail 1 (not carried out) — AutoLearn has not been carried out.
- AutoLearn fail 2 (Manual intervention) — Manual intervention during AutoLearn.
- AutoLearn fail 3 (Compass or drive error) — Investigate compass fault or drive fault.
- AutoLearn fail 4 — AutoLearn has failed due to compass or drive error.
- AutoLearn fail 5 — AutoLearn has failed due to the motor reaching its current limit.
- AutoLearn fail 6 — AutoLearn has failed because the vessel went into a spin (i.e. the motor did not drive the rudder back to the opposite side).

59

<!-- pdf page 60 | printed page 60 -->

## CHAPTER 10: SETUP MENU

##### CHAPTER CONTENTS

<!-- pdf page 61 | printed page 61 -->

### 10.1 Set up menu

- The set up menu provides a range of tools and settings to configure the pilot controller.
- [Autopilot Calibration] — Commissioning and calibration settings.
- SeaTalk NG autopilots:
- Vessel settings
- Drive settings
- Sailboat settings
- Commissioning
- SeaTalk autopilots:
- User settings
- Dealer settings
- Seatrial calibration
- [User Preferences] — Configure the following options:
- Time & Date — Refer to: p.63 — Time and date
- Units — Refer to: p.63 — Units of measurement
- Language — Refer to: p.63 — User interface languages
- Variation — Refer to: p.64 — Variation
- Key Beep — Refer to: p.64 — Key beep
- [System set up] — Configure network groups and data sources.
- The following options are available:
- Network group — Refer to: p.64 — Network group
- Brightness / Color Group — Refer to: p.64 — Brightness and color group
- Data Sources — Refer to: p.64 — Data sources
- About System Set Up — Provides information about the System set-up menu.
- [Simulator] — Enables and disables simulator mode. The simulator produces simulated data to enable you to practice operating the display.

Note: The simulator will not produce simulated data if live data sources are present on the SeaTalk NG network. Setup menu

- [Factory reset] — Delete user settings and restore the display to its factory default settings.
- [Diagnostics] — Information About the display, devices connected to the network and the diagnostics self test. The following options are available:
- About Display — View hardware and software details for your display.
- About Pilot — View autopilot hardware and software details for your system.
- About System — Allows you to search the SeaTalk NG network for connected devices, and displays information about detected products.
- Self Test — The product has a built-in self test which can help to diagnose faults. The following tests are performed during a self test: ♦ Memory test ♦ Button test ♦ Display test ♦ Buzzer test ♦ Illumination test
- [Set-up wizard] — Launch the initial set-up wizard.

### 10.2 Autopilot calibration menu

The Autopilot Calibration menu options are determined by the connected autopilot system. The settings available in the Calibration menu are shown below. For details on how to calibrate and commission your autopilot refer to the Commissioning chapters: • Commissioning Evolution autopilots: p.26 — Commissioning — Evolution autopilot system • Commissioning SPX autopilots: p.33 — Commissioning — SPX and SmartPilot systems

###### Rudder damping levels and deadband angles

For autopilot systems which include a rudder angle reference sensor / transducer, rudder damping is used to prevent Evolution-Series autopilot system over-activity, characterized by 61

<!-- pdf page 62 | printed page 62 -->

“hunting” maneuvers. A number of rudder damping levels are available to address this behavior. Rudder damping levels relate to “deadband angles”, and can be configured using your autopilot control head (e.g. p70s/p70Rs or MFD). A higher damping level is intended to eliminate pilot and helm over-activity. Typically, the appropriate rudder damping level is the lowest acceptable value. However, it is important to be aware that the rudder damping scaling has been changed in recent versions of the ACU-Series units, which include newer processor and software versions (these units can be identified with an “A” appended to their SKU).

Important: The rudder damping levels can have a significant impact on your autopilot performance. If you are unsure as to how to adjust these settings to best suit your autopilot system, please refer to your dealer or Raymarine product support.

The following table lists the rudder damping levels and deadband angles that are available with both old and new versions of the ACU-Series software:

| Rudder | Existing | Existing | New Deadband |
| --- | --- | --- | --- |
| damping level    Deadband | angle (ACU-100,   angle (ACU-300)   Series software ACU-150, ACU-200, ACU-400) | Deadband | angle (ACU- version v3.11 or later) |
| 1 | 0.1° | 0.15° | 0.1° |
| 2 | 0.2° | 0.30° | 0.2° |
| 3 | 0.3° | 0.45° | 0.3° |
| 4 | 0.4° | 0.60° | 0.4° |
| 5 | 0.5° | 0.75° | 0.7° |
| 6 | 0.6° | 0.9° | 0.9° |
| 7 | 0.7° | 1.05° | 1.1° |
| 8 | 0.8° | 1.20° | 1.6° |
| 9 | 0.9° | 1.35° | 2.2° |

It’s important to check the rudder damping level currently configured on your autopilot control head, to ensure it matches your needs. The rudder damping value should be increased one level at a time until the autopilot stops hunting.

###### Adjusting the Rudder Damping level

Use the following menu path to adjust the Rudder Damping level:
1. [Menu > Set-up > Autopilot Calibration > Drive Settings > Rudder Damping].

###### Sail boat settings

These settings are only available to sail boats. The Sail Boat settings menu can be accessed from: [Menu > Set-up > Autopilot Calibration > Sail Boat Settings].

- Note: When connected to a SeaTalk ® system the Sail boat settings listed
- below are part of the [User settings ] menu: [Menu > Set-up > Autopilot Calibration > User Settings].

- Note: The following features are only available if wind data is available:

- [Gybe inhibit] — With gybe inhibit set to [Allow Gybe], the autopilot will allow the vessel to tack through / into and away from the wind. With gybe inhibit set to [Prevent Gybe], you can only tack through / into the wind. Gybe inhibit does not effect Auto turn.
- [Wind Type] — This option determines whether the vessel steers to Apparent or True wind in Wind vane mode.
- [Wind Trim Response] — Wind Trim Response controls how quickly the autopilot responds to changes in wind direction. Higher wind trim settings will result in a system that is more responsive to wind changes. Wind trim is set to level 5 by default.

- Note: Not available on Evolution autopilots.

- [Wind Shift Alarm] — This option enables you to switch the Wind shift alarm On (default) and Off.

<!-- pdf page 63 | printed page 63 -->

- Note: Not available on SeaTalk ® and SPX smartpilots.

### 10.3 User preferences menu

###### Time and date

The [Time & Date] menu provides date and time format options and a time offset setting to compensate for any time zone difference between local time and the Universal Time Constant (UTC). The following options are available:

| [Time format] | [Date format] | [Time offset] |
| --- | --- | --- |
| [24 hour] | [MM/DD/YYYY] | –13 to +13 hours in 0.5 hour increments. |
| [am/pm] | [DD/MM/YYYY] |  |

###### Units of measurement

The [Units] menu enables you to specify the measurement units used for data. The following options are available:

| [Speed] units | [Distance (long)] units | [Distance (short)] units |
| --- | --- | --- |
| • Kts — knots | • nm — Nautical | • ft — Feet |
| • MPH — miles per | miles |  |
| hour | • sm — Statute | • m — Metres |
| • KPH — Kilometers | miles |  |
| per hour | • km — Kilometers |  |
| [Depth] units | [Wind speed] units | [Temperature] units |
| • Feet | • Kts — Knots | • ºC — Degrees centigrade |
| • m — Metres | • MS — Metres per second | • ºF — Degrees |
| • fa — Fathoms |  | fahrenheit |

Setup menu

| [Flow rate] units | [Heading] type | [Pressure] units |
| --- | --- | --- |
| • G/H (UK) — UK | • True | • PSI — Pounds per |
| gallons per hour | • Mag — Magnetic | square inch |
| • G/H (US) — US |  | • BAR — Bar |
| gallons per hour |  | • kPa — Kilo |
| • LTR/H — Liters |  | pascals |
| per hour |  |  |
| [Volume] units | [Position units]      [Economy units] |  |
| • GAL(UK) — UK | • DDºMM’.MMM | • Distance per |
| gallons | • DD:MM:SS | volume |
| • GAL(US) — US |  | • Volume per |
| gallons | • DD:MM:SS.S | distance |
| • LTR — liter | • DD:MM.MMM • DDºMM’SS • DDºMM.MMM’ | • Litres per 100km Note: Only Available on i70 and i70s. |

###### User interface languages

- The [Language] menu allows you to select the language that will be used for the display’s user interface.
- The following options are available:
- Languages:

| English | English | Chinese | Croatian | Danish |
| --- | --- | --- | --- | --- |
| (UK) | (US) |  |  |  |
| Dutch | Finnish | French | German | Greek |
| Italian | Japanese | Korean | Norwegian | Polish |
| Por- | Russian | Spanish | Swedish | Turkish |

tuguese (Brazilian)

63

<!-- figure 1 on pdf page 63 at 334,228-602,286 pt | caption: none | text-layer labels: • DDºMM.MMM’ | Note: Only Available on i70 and i70s. | nearby labels: • DD:MM:SS.S | • LTR — liter | • DD:MM.MMM | distance | • Litres per 100km | • DDºMM’SS | User interface languages | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 64 | printed page 64 -->

###### Variation

Variation is the local difference between True North (which does not change) and Magnetic North, which changes slightly each year. Typically, cartography uses True North, and Magnetic North is the direction in which a magnetic compass points. Variation changes depending on your geographic location and date. The [Variation] menu provides options to compensate for variation. The following options are available: • [Variation mode] — Variation mode can be set to the following: – [On] — With variation switched on, you can set the amount of variation compensation, using the [Variation range] option (see below). – [Off] — With variation switched off, variation compensation will not be used. – [Slave] — When networked to another device (e.g.: an MFD or pilot controller) providing magnetic variation, the display will automatically switch to slave mode and use the variation provided by that device. • [Variation range] — When [Variation mode] is switched on, your magnetic heading readings will be adjusted (compensated) by the amount specified.

###### Key beep

By default, every time a button is pressed, the display emits an audible beep. The beep can be enabled or disabled using the Key beep option.

### 10.4 System Set-up menu

###### Network group

- The [Network group] menu allows you to add multiple displays to a group so that when the color scheme or brightness is changed on one display the changes are applied to all displays in that group.
- The groups available are:
- None
- Helm 1
- Helm 2

- Cockpit
- Flybridge
- Mast There are also 5 undefined groups available.

###### Brightness and color group

- The [Brightness / color group] menu enables synchronization of the display’s brightness and color scheme to be the same as other displays in the same network group.
- The following options are available:
- This display
- This group

###### Data sources

- The [Data sources] menu enables you to view available data sources and, if required, select your preferred data sources.
- The available data sources are:
- GPS position
- GPS Datum
- Time & Date
- Heading
- Depth
- Speed
- Wind

<!-- pdf page 65 | printed page 65 -->

## CHAPTER 11: SYSTEM CHECKS AND TROUBLESHOOTING

##### CHAPTER CONTENTS

System checks and troubleshooting                      65

<!-- pdf page 66 | printed page 66 -->

### 11.1 Troubleshooting

The troubleshooting section provides possible causes and the corrective action required for common problems that are associated with the installation and operation of your product. Before packing and shipping, all products are subjected to comprehensive testing and quality assurance programs. If you do experience problems with your product, this section will help you to diagnose and correct problems to restore normal operation. If after referring to this section you are still having problems with your product, please refer to the Technical support and servicing section of this manual for useful links and contact details.

### 11.2 Power up troubleshooting

###### Product does not turn on or keeps turning off

Possible causes     Possible solutions

Blown fuse /        1.   Check condition of the SeaTalk NG tripped breaker          backbone power connection 5 A fuse and if applicable distribution panel breaker, replace if necessary. 2. If the fuse keeps blowing check for cable damage, broken connector pins or incorrect wiring. Poor / damaged      1.   Check the vessel’s battery voltage and / insecure cables        the condition of the battery terminals and connections          and power supply cables, ensuring connections are secure, clean and free from corrosion. Replace if necessary. 2. Check all SeaTalk NG cabling and connections for signs of damage or corrosion. Replace if necessary. 3.   Check all SeaTalk NG connectors are correctly orientated, fully inserted and in the locked position. 4.   With the display turned on, try flexing the display’s spur cable near to the display’s connector to see if this causes the display to restart or lose power. Replace if necessary. 5. With the product under load, using a multi-meter, check for high voltage drop across all connectors / fuses etc, and replace if necessary. Incorrect power     1.   The power supply may be wired connection               incorrectly, ensure the SeaTalk NG power connection instructions have been followed and that the backbone has one single source of 12 V dc power.

<!-- pdf page 67 | printed page 67 -->

###### Product will not start up (restart loop)

Product causes                    Possible solutions

| Power supply and | 1.   Refer to ‘Product does not turn on or |
| --- | --- |
| connection | keeps turning off’ information above. |
| Software | 1.   In the unlikely event that the product’s |
| corruption | software has become corrupted, try downloading and installing the latest software from the Raymarine website. refer to your Multifunction Display’s operation instructions for details on updating software for SeaTalk NG devices. 2. In the case of a restart loop attempt a fac- tory reset using the following instructions: p.67 — Performing a Factory Reset |

###### Performing a Factory Reset

To reset your unit to factory default settings follow the steps below.

Note: Performing a factory reset will erase all saved data and customized settings.

1. Press the [Menu] button.
2. Select [Set Up].
3. Select [Factory Reset].
4. Select [Yes] . Your unit will now reset itself to factory default settings.

System checks and troubleshooting

### 11.3 System data troubleshooting

Aspects of the installation can cause problems with the data shared between connected equipment. Such problems, their possible causes and solutions are described here.

###### Expected data is unavailable at all displays

Possible causes     Possible solutions

| Data is not being | 1. | Check the relevant product and or |
| --- | --- | --- |
| received at the |  | network cabling and connections (e.g. |
| display. |  | SeaTalk NG backbone) for signs of damage or corrosion, and replace if necessary. |
| Data source | 1. | Check the source of the missing data (e.g. |
| (e.g. instrument |  | transducer or engine interface) for signs |
| display or engine |  | of damage or corrosion, and replace if |
| interface) is not |  | necessary. |
| operating. | 2. If possible, check that the data source is correctly powered and operational. 3. | Refer to the instructions provided with the equipment to ensure it has been correctly installed. |
| Software | 1. | Ensure all products have the latest |
| mismatch |  | software installed. |

between equipment may prevent communication.

67

<!-- pdf page 68 | printed page 68 -->

###### Expected data is missing from some but not all displays

Possible causes      Possible solutions

| Connection | 1.   Check the product’s SeaTalk NG spur |
| --- | --- |
| problem. | cable and connections for signs of damage or corrosion, and replace if necessary. |
| Software | 1.   In the unlikely event that the product’s |
| corruption. | software has become corrupted, try downloading and installing the latest software from the Raymarine website. refer to your Multifunction Display’s operation instructions for details on updating software for SeaTalk NG devices. 2. In the case of a restart loop attempt a fac- tory reset using the following instructions: p.67 — Performing a Factory Reset |
| Software | 1.   Ensure all products have the latest |
| mismatch | software installed. |

between equipment may prevent communication.

###### Incorrect data reported

Possible causes      Possible solutions

| Transducer | 1.   Switch off power supply to system and |
| --- | --- |
| calibration error. | switch back on again. 2. Re-calibrate or re-configure data source following instructions provided with the relevant devices. |

### 11.4 Miscellaneous troubleshooting

Miscellaneous problems and their possible causes and solutions are described here.

###### Display behaves erratically

Frequent unexpected resets, system crashes and other erratic behavior Possible causes    Possible solutions

| Intermittent | 1.   Check relevant fuses and breakers. |
| --- | --- |
| problem with |  |
| power to the | 2. Check that the power supply cable is |
| display. | sound and that all connections are tight and free from corrosion. 3.   Check that the power source is of the correct voltage and sufficient current. |
| Software | 1.   Ensure all products have the latest |
| mismatch | software installed. |
| between |  |
| equipment |  |
| may prevent |  |
| communication. |  |
| Corrupt data / | 1.   In the unlikely event that the product’s |
| other unknown | software has become corrupted, try |
| issue. | downloading and installing the latest software from the Raymarine® website. Refer to your multifunction display’s operation instructions for details on updating software for SeaTalk NG devices. 2. Check the data source for correct operation. |

<!-- pdf page 69 | printed page 69 -->

## CHAPTER 12: TECHNICAL SUPPORT

##### CHAPTER CONTENTS

Technical support                                                  69

<!-- pdf page 70 | printed page 70 -->

### 12.1 Raymarine technical support and servicing

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

<!-- pdf page 71 | printed page 71 -->

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

###### Checking hardware and software information

- You can check current hardware details and software version from the [About display] menu.
1. Press the [Menu] button.
2. Select [Set-up].
3. Select [Diagnostics].
4. Select [About Display]. A range of information is displayed, including the software version and Serial number.
5. Use the [Up] and [Down] buttons to cycle through the information.

### 12.2 Learning resources

Raymarine has produced a range of learning resources to help you get the most out of your products.

###### Video tutorials

Raymarine official channel on YouTube Technical support

- http://www.youtube.com /user/RaymarineInc

###### Training courses

- Raymarine regularly runs a range of in-depth training courses to help you make the most of your products. Visit the Training section of the
- Raymarine website for more information:
- www.bit.ly/rym-training

###### Technical support forum

You can use the Technical support forum to ask a technical question about a Raymarine product or to find out how other customers are using their Raymarine equipment. The resource is regularly updated with contributions from Raymarine customers and staff: • www.bit.ly/rym-support

71 (no text layer on this page)

<!-- pdf page 72 | printed page 72 -->

<!-- pdf page 73 | printed page 73 -->

###### Appendix A Supported NMEA 2000 PGN list

###### Administration PGNs

- 59392 — ISO Acknowledge (Receive / Transmit)
- 59904 — ISO Request (Receive)
- 60928 — ISO Address Claim (Receive / Transmit)
- 126208 — NMEA — Request, Commanded, Acknowledged Group Function (Receive / Transmit)
- 126464 — PGN Transmit and Receive List (Receive / Transmit)
- 126996 — Product Information (Receive / Transmit) Raymarine® provides field programmability of the Device and System Instances within PGN 60928 which can be commanded via use of PGN 126208 as required by the latest [NMEA 2000] standard.

###### Data PGNs

- 126992 — System Time (Receive / Transmit)
- 126993 — Heartbeat (Receive / Transmit)
- 127237 — Heading/Track Control (Receive)
- 127245 — Rudder (Receive / Transmit)
- 127250 — Vessel Heading (Receive)
- 127251 — Rate of Turn (Receive)
- 127257 — Attitude (Receive)
- 127258 — Magnetic Variation (Receive / Transmit)
- 128259 — Speed, (Receive)
- 128267 — Water Depth (Receive)
- 128275 — Distance Log (Receive)
- 129025 — Position, Rapid Update (Receive)
- 129026 — COG & SOG, Rapid Update (Receive)
- 129029 — GNSS Position Data (Receive)
- 129033 — Time & Date (Receive)
- 129044 — Datum (Receive / Transmit) Supported NMEA 2000 PGN list

- 129283 — Cross Track Error (Receive)
- 129284 — Navigation Data (Receive)
- 129291 — Set & Drift, Rapid Update (Receive)
- 130306 — Wind Data (Receive)
- 130310 — Environmental Parameters (Receive)
- 130311 — Environmental Parameters (Receive)
- 130576 — Small Craft Status (Receive)
- 130577 — Direction Data (Receive)

73

<!-- pdf page 74 | printed page 74 -->

###### Appendix B Software release history

The list below is a cumulative list of the software releases, since the initial release (v1.04; December 2011). This list includes new features only. It does NOT include software maintenance items, such as bug fixes or performance improvements. To download the software, and view the complete list of all software updates, including new features, bug fixes, and performance improvements, visit: p70-Series software download link

www.bit.ly/p70-download

###### Software v3.13 (02-2024)

- Improvements to support MFD Wind vane mode.

###### Software v3.12 (03-2023)

- Support for LightHouse 4 v4.4.87 features.
- User Interface (UI) design aligned with i70 / i70s UI.

###### Software v3.09 (09-2019)

- Corrected translation errors for Polish & Russian languages.

###### Software v3.08 (01-2019)

- Safety improvements:
- Pilot controller can now detect key lock-up and trigger buzzer for 10 seconds.
- Pilot controller will drop to standby if it is the only controller in the system.
- Shortcut to activate Wind vane mode moved; this can no longer be activated by pressing Auto + Standby.

###### Software v3.07 (08-2016)

- Translation correction.
- Variation setting is now applied locally and globally on the SeaTalk NG network. This corrects a No Navigation Data alarm when interfaced with a SeaTalk 1 autopilot.

###### Software v3.06 (06-2016)

- Support for hardware changes.

###### Software v3.05 (05-2016)

- Improvements to Track acquisition and Track keeping.
- Wind vane steering performance improvements.
- Added Progress bar for Compass linearization.
- Windshift alarm improvements and on / off toggle.
- Compass calibration process improvements.

###### Software v2.17 (08-2014)

- Added speed input source selection during autopilot calibration.
- Various fixes and improvements.

###### Software v2.12 (10-2013)

- Added rudder bar to Dockside calibration wizard (Rudder alignment).
- Fixed “No Pilot” alarm when connected to multiple MFDs with autopilot control enabled.

###### Software v2.11 (06-2013)

- Added compatibility with Evolution autopilots.
- Added About System diagnostics page.

###### Software v1.08 (07-2012)

- Fixed issue where Standby key is locked when auto is activated from second controller.
- Fixed issue where display won’t power back up after shutdown using power key.

###### Software v1.06 (02-2012)

- General bug fixes and improvements.

###### Software v1.04 (12-2011)

- Initial release.

<!-- pdf page 75 | printed page 75 -->

| Appendix C Document change history | • General update to bring inline with latest i70 documentation. |
| --- | --- |
| Documentation for current products is regularly updated to | • Updated and restructured to latest standards. |
| ensure accuracy and reflect changing product features and / or | • Updated screenshots to reflect new UI introduced in v3.12 |
| specifications. Changes made to this document since its first release | software. |
| are listed below. | • Added Glossary and document change history to Appendix. |
| Document number:               Document name: | • Added Position units of measure options to User preferences. |
| 81402                          p70s /p70Rs / p70 / p70R Operation |  |
| Instructions | Changes: |
| Changes: | Revision      Date                Applicable software version(s) |
| Revision                Date                  Applicable software version(s)    02            June 2021           v3.09 |  |
| 06                      October 2025          v3.13 | • Removed details referring to pressing Auto and Standby together to activate Wind vane mode. This shortcut was removed in v3.08 |
| • Changed connection to compatible autopilot systems to refer to | software. |
| SeaTalk 1 to SeaTalk NG adapter cable instead of the SeaTalk 1 |  |
| to SeaTalk NG Converter. | • Updated layout to A5 format. |

| • Updated layout and format of the Document change history. | Changes: |
| --- | --- |
| Changes: | Revision      Date                Applicable software version(s) |

Revision                Date                  Applicable software version(s)    01            June 2021           v3.09

| 05                      September 2025 | v3.13 • First public release. |
| --- | --- |
| • Minor editorial improvements. | Note: |
| Changes: | This document (81402) replaces the “operations” details contained in another document (81365), which is now obsolete. |
| Revision                Date | Applicable software version(s) |

04                      October 2024          v3.13

- Added Automatic turning details.

###### Changes:

| Revision | Date | Applicable software version(s) |
| --- | --- | --- |
| 03 | March 2024 | v3.13 |

- Updated Auto Turn details to include angle adjustment. Document change history                                                                                                                              75

<!-- pdf page 76 | printed page 76 | header: Term / Meaning -->

## Term / Meaning

###### Appendix D Glossary

###### Navigation glossary

Common terms and abbreviations used in navigation. Term                Meaning

Active navigation   Active navigation is the term used when the display is performing navigation to a destination point. The destination point can be a ‘Goto’ (to an onscreen cursor position or a single waypoint), or part of a ‘Follow’ (to a waypoint within a route). AIS (Automatic      A tracking system enabling you to receive Identification      positional information broadcast by other System)             vessels, and to transmit positional information for your own vessel. AIS is used to identify, locate and track marine vessels in the chart and radar applications. An AIS receiver or transceiver is required to view AIS information. Auto range          A mode that ranges the chart application automatically, to ensure both the vessel and target waypoint are always visible. Course Over         COG is the actual direction of travel, relative Ground (COG)        to fixed land. Vessel heading may differ from COG due to the effects of currents, tide and wind. COG is transmitted by GNSS (GPS) receivers. Supported data: • NMEA 2000: PGN 129026 • NMEA 0183: RMC Course up (CU /     The chart or radar is orientated so as to show C-up)               your current course directly ahead of your vessel icon. The chart will rotate so that your Course Over Ground (COG) is always upward on the screen.

Term                Meaning

| Cross Track Error | The amount of deviation from your intended |
| --- | --- |
| (XTE) | course, expressed as a distance. In the event that you steer off-track, you can create a new course to the target by selecting “Restart XTE” on your pilot controller or multifunction display. |
| Direction of | The direction a target is travelling in relation |
| Relative Motion | to your own vessel’s direction and speed. |
| (DRM) |  |
| Follow | The action whereby the display is placed in active navigation following a route. |
| GNSS (Global | A constellation of Earth orbiting satellites |
| Navigation | that can be used to plot latitude, longitude, |
| Satellite System) | altitude, Course Over Ground (COG), and Speed Over Ground (SOG). Current available GNSS are: • GPS (USA) • BeiDou (China) • Galileo (EU) • GLONASS (Russia) |
| Goto | The action whereby the display is placed in active navigation travelling to a cursor location or a single waypoint. |
| Head up (HU / | The chart or radar is orientated so as to |
| H-up) | show your current heading directly ahead of your vessel icon at all times. As your vessel changes direction, the chart or radar image rotates accordingly to reflect the new bearing. In Head-up, the motion mode is fixed to Relative motion. |

<!-- pdf page 77 | printed page 77 | header: Term / Term / Meaning / Meaning -->

## Term / Term / Meaning / Meaning

Heading (HDG)       Compass direction of travel. Heading can be relative to True north or Magnetic north. Heading can be transmitted from a ship’s compass or heading sensor. Supported data: • NMEA 2000: PGN 127237 / 127250 • NMEA 0183: HDG / HDM / HDT Latitude (Lat)      A geographic coordinate which indicates the position of a point on the Earth that is either north or south of the equator. When provided as a coordinate, the number of degrees is determined in relation to how far (0° to 90°) north or south the coordinate is from the Earth’s equator — where 90° refers to either the North Pole or South Pole and 0° refers to the equator. One degree of latitude is approximately equivalent to 60 nautical miles. Longitude (Lon)     A geographic coordinate which indicates the position of a point on the Earth that is either east or west of the prime meridian. When provided as a coordinate, the number of degrees is determined in relation to how far (0° to 180°) east or west the coordinate is from the prime meridian. North up (NU /      The chart or radar image is orientated so that N-up)               true north is always upward on the screen. As your vessel changes direction, vessel icon (chart) or ship heading line (radar) rotate accordingly to show your relative position to true north. Rate of Turn        RoT is the speed at which your vessel turns (RoT)               in a given direction, typically when under autopilot control.

Navigation glossary

Relative Motion     In the Chart and Radar applications, relative (RM)                motion mode fixes your vessel’s position and the chart or radar image moves relative to your vessel. In Relative Motion mode you can use the [Boat position] setting to determine whether the vessel position is fixed in the Center of the chart display or has a Partial offset, or Full offset. Selecting the partial or full offset has the effect of increasing the view ahead. Route (RTE)         A series of waypoints typically used to assist with journey planning and navigation. A route is displayed on screen as a series of waypoints linked by a line. Speed of Relative   The velocity of a target relative to your own Motion (SRM)        vessel’s velocity (E.g.: If you are travelling in the same direction as a target, the relative speed will be the difference between your vessel’s speed and the target’s speed. If you are travelling towards / away from each other then relative speed is the combination of both vessel’s speeds). Speed Over          The actual speed of travel, relative to fixed Ground (SOG)        land. Vessel speed may differ from STW due to the effects of currents, tide and wind. SOG is transmitted by GNSS (GPS) receivers. Supported data: • NMEA 2000: PGN 129026 • NMEA 0183: RMC Speed Through       The speed of your vessel through the water, Water (STW)         also known as boat speed. Due to tide and current this will be different than Speed Over Ground (SOG). STW is measured by a speed transducer. Supported data: • NMEA 2000: PGN 128259 • NMEA 0183: VHW

77

<!-- pdf page 78 | printed page 78 | header: Term / Meaning -->

## Term / Meaning

Term               Meaning

Time To Go (TTG)   The time remaining until you reach the destination point. Track              A visible trail displayed in the Chart app on a multifunction display, showing the passage you have taken. The trail consists of a series of track points which are created automatically. You can save the track to create a permanent record of where you have been. You can also create a new route from a track. True Motion (TM)   True Motion mode fixes the chart position and the vessel icon moves across the screen. As the vessel’s position approaches the edge of the screen, the chart image is automatically redrawn to reveal the area ahead of the vessel. As the vessel’s position approaches the edge of the display, the image is automatically redrawn to reveal the area ahead of the vessel.

Note: True Motion mode is not available when the orientation is set to “Head-up”.

Waypoint (WPT)     A position marked on the screen to indicate a location to navigate to. Waypoint positions are defined by Longitude / Latitude coordinates, and can be saved for future use. As well as acting as position markers, waypoints are also the building blocks used to create routes. Waypoints can be created and displayed in the Chart, Radar, and Fishfinder apps on a multifunction display.

###### Sailing glossary

Common terms and abbreviations used in sailing. Term               Meaning

Apparent Wind      The wind flow observed when the vessel is in motion, relative to the vessel’s heading. Apparent wind is different from True wind in that it takes into account your vessel’s movement, i.e.: speed and direction of travel. Apparent wind is the raw data that is reported by wind transducers, which can then be used in conjunction with other data sources to calculate True wind. Supported data: • NMEA 2000: PGN 130306 • NMEA 0183: MWV Apparent Wind      The wind angle observed when the vessel is Angle (AWA)        in motion, relative to the vessel’s heading. AWA is a combination of the true angle of the wind and the angle that is experienced due to the direction and speed of travel. Apparent Wind      The wind speed observed when the vessel is Speed (AWS)        in motion. AWS is a combination of the true speed of the wind and the speed at which you are travelling.

<!-- figure 1 on pdf page 78 at 125,266-290,319 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 79 | printed page 79 | header: Term / Term / Meaning / Meaning -->

## Term / Term / Meaning / Meaning

Close-hauled /     Generally, when sailing upwind, the tighter Beating            the angle at which the vessel sails with respect to the wind, the faster the vessel will travel. When a vessel’s sails are pulled in tightly to the vessel’s centerline in order to maximize the vessel’s speed when travelling upwind, it is known as sailing “Close-hauled” or “beating”. There's a "no-go" zone directly into the wind where a vessel cannot sail in a forward motion. Also, sailing too close to the wind ("pinching") can reduce both speed and efficiency in terms of the vessel’s forward motion. Therefore, maximizing forward motion when sailing upwind requires the optimization of both the vessel’s sail rigging and the vessel’s angle with respect to the wind direction, which is typically 30 to 45 degrees. Distance to Tack   The travel distance remaining until you need to tack. Distance to Line   Distance remaining to the closest point along the race start line. Downwind           Moving in the direction that the wind is blowing. Ground Wind        The direction of the wind relative to north, as Direction (GWD)    observed on land. This is the actual direction the wind is blowing. In addition to Apparent Wind Angle (AWA), Course Over Ground (COG) from a GNSS receiver is also required in order to calculate GWD. Ground Wind        The wind speed observed when stationary, as Speed (GWS)        observed on land. GWS is the actual speed at which the wind is blowing over land. In addition to Apparent Wind Speed (AWS), Speed Over Ground (SOG) data from a GNSS receiver is also required in order to calculate GWS.

Sailing glossary

| Header | A wind shift which causes your vessel to turn more downwind. |
| --- | --- |
| Laylines | Vector lines showing the course the boat will take when sailing at the optimum angle to the wind, on either tack. |
| Leeway | The difference in angle between desired heading and actual course, caused by sideways movement of a sailing boat due to the wind. |
| Lift | A wind shift which allows your boat to turn upwind and closer to your destination. |
| Line bias | The distance advantage conferred by crossing the start line at the favored end (the end which is more upwind) of the race start line. |
| Polar table | A performance profile for a vessel, showing the vessel speed achievable at varying angles to the wind, with varying wind speed. In sailing, the Velocity Made Good (VMG) principle demonstrates that travelling in a straight line is not always the quickest route, and polars enable you to optimize your vessel's performance to its best advantage, by improving the accuracy of laylines to display how far you need to sail on a current tack to reach a target waypoint after tacking, and taking wind conditions into consideration. |
| RSW-Wired | The Raymarine Smart Wind transducer series. |
| (Raymarine Smart   The RSW-Wired series of transducers include |  |
| Wind) | a built-in attitude sensor, which is used to provide more accurate readings than standard wind transducers. |
| Sail plan | Sail configuration recommendations based on wind conditions. |
| Sailing upwind | Sailing close to the wind direction. |

79

<!-- pdf page 80 | printed page 80 | header: Term / Meaning -->

## Term / Meaning

| Tack | A course change made by a sailing vessel, by turning its heading into and through the wind. |
| --- | --- |
| Tacking | The zig-zag maneuver a sailing vessel makes when travelling upwind. |
| Time To Burn | The time remaining during race start |
| (TTB) | countdown before the vessel needs to start moving towards the start line at full speed. |
| Time to Tack | The amount of time remaining until you need to tack, if the current course and speed are maintained based on the calculated laylines. |
| True Wind | The actual wind flow; the wind flow that you experience on the water, when stationary. True wind is calculated from Apparent wind data from a wind transducer and STW (Speed Through Water) data from a speed transducer. |
| True Wind Angle | The angle of the wind over water, relative to |
| (TWA) | the vessel’s bow, observed when stationary. |
| True Wind | The direction of the wind relative to North. |
| Direction (TWD) | This is the actual direction in which the wind is blowing. In addition to Speed Through Water (STW), Heading data is also required in order to calculate TWD. |
| True Wind Speed | The wind speed observed when stationary, |
| (TWS) | on the water. TWS is the actual speed at which the wind is blowing over water. |
| Velocity Made | Sailing term related to the component of a sail |
| Good (VMG) | vessel’s velocity vector that is in the direction of true wind. |
| Wind shift | The amount of variation in True Wind Direction (TWD) over time. |

<!-- pdf page 81 -->

(no text layer on this page)

<!-- pdf page 82 -->

(no text layer on this page)

<!-- pdf page 83 -->

#### Index

#### A

Auto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20–21, 43 AutoLearn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39, 59 Autopilot set-up AutoTack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20, 49–50

#### B

Brightness. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22, 64 Shared . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22–23

#### C

Commissioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19, 61 Commissioning pre-requisites. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27, 34 Compass linearization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27, 30 Compass lock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27, 31 Cross track error. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46–47

#### D

Data sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24, 64 Dockside wizard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27–29, 36 Drive type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28, 36

<!-- pdf page 84 -->

#### E

#### F

#### G

Glossary Gybe inhibit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49, 62

#### H

#### J

#### L

#### M

Menus

#### N

Navigation

#### O

#### P

<!-- pdf page 85 -->

Pilot Views Power off . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20, 34 Power on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20, 34 Power Steer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21, 44

#### R

Rudder alignment check). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29, 36

#### S

Sailing

Set-up wizard. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20, 61 Standby. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19, 21

#### T

Technical support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70–71 Track mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21, 45

#### U

<!-- pdf page 86 -->

#### V

#### W

Warranty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10, 70 Waypoint advance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46, 58 Waypoint arrival . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46–47 Wind vane mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21, 48–49
