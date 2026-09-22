<!-- pdf page 1 -->

Evolution autopilot set-up and
commissioning with p70 / p70s /
p70R / p70Rs
Evolution autopilot installation
For information on installing and connecting an Evolution
autopilot system, refer to the installation instructions
that accompany the EV-1 and EV-2 units, as well as the
instructions that accompany your drive unit, as appropriate.

Commissioning pre-requisites
Before commissioning your autopilot system for the first
time, ensure that you have read through and understood
the entire commissioning instructions for your autopilot
system.
Before commissioning, you should also ensure the
following:
• All autopilot system components have been installed in
  accordance with the installation instructions supplied
  with the system components.
• All autopilot system components have been updated to
  the latest available software versions, available on the
  Raymarine website.
• A system schematic is available which includes all
  system components and required connections.
• The commissioning engineer is familiar with the vessel’s
  hull type, drive type and steering system.

Commissioning steps
The required commissioning steps should be carried out in
the correct order using the pilot controller display.
1. Power-up all of the components that make up your
   autopilot system.
2. Select the relevant vessel hull type for your vessel
   from the [Vessel Hull Type] menu: [Menu > Set-up >
   Autopilot Calibration > Vessel Settings > Vessel Hull
   Type]
 Note:
 Vessel hull type may have already been selected as
 part of the start-up wizard.

3. Complete the dockside calibration process., using the
   [Dockside wizard]:
4. If the system does NOT include a rudder reference
   transducer then, specify the hard-over time.
5. Complete compass linearization.
6. If required, lock the compass.

Powering on and off
The p70s / p70Rs automatically powers on when power is
supplied to the network it is connected to, unless it has
been powered off using the [Standby] button.
Document number: 82285 (Rev 7)   AA;46110;2023-07-07T14:07:13

1. If the display has been powered off using the standby
   button, press and hold [Standby] for approximately 2
   seconds, to power the display on again.
2. To power the display off, press and hold the [Standby]
   button for approximately 5 seconds.
   After 1 second, a 3 second countdown is displayed. The
   display cannot be powered off when the autopilot
   is engaged.

Using the Set-up Wizard
The set-up wizard guides you through the steps for setting
important preferences, such as preferred language and
correct vessel type.
The Set-up Wizard contains 3 steps: Language Selection,
Vessel Hull Type selection and Welcome Screen. When
powering the Pilot Controller for the first time, in an
unconfigured system, the Set-up Wizard is displayed
automatically, and the first 3 steps listed below will not
be required.

With the pilot in Standby mode:
1. Select [Menu].
2. Select [Set-up].
3. Select [Set-up Wizard].
4. Select the required language.
5. Select the required vessel type.
   The welcome screen will now be displayed and your
   choices have been saved.
6. Select [OK] to complete the Set-up Wizard.

Vessel hull type selection
The vessel hull type options are designed to provide
optimum steering performance for typical vessels.
It is important to complete the vessel hull type selection,
prior to performing dockside calibration, as it forms a key
part of the commissioning process. The vessel hull type
options can be accessed at any time when the autopilot
is in Standby, from the [Vessel Hull Type] menu: [Menu >
Set-up > Autopilot Calibration > Vessel Settings > Vessel
Hull Type].
Select the option that most closely matches your vessel’s
hull type and steering characteristics:
• [Power]
• [Power (slow turn)]
• [Power (fast turn)]
• [Sail]
• [Sail (Slow turn)]
• [Sail Catamaran]

 Note: It is important to be aware that steering forces
 (and therefore rate-of-turn) vary significantly depending
 on the combination of vessel hull type, steering system,
 and drive type. The available vessel hull type options
 are provided for guidance only. It may be possible to
 improve the steering performance of your vessel by
 selecting a different vessel hull type.
                                                Date: 07-2023

<!-- figure 1 on pdf page 1 at 304,137-559,185 pt | caption: none | text-layer labels: none | nearby labels: Using the Set-up Wizard | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 1 at 31,700-289,744 pt | caption: none | text-layer labels: none | nearby labels: Powering on and off | OCR: no legible text (0/2 words >= 60, mean confidence 32) -->

<!-- pdf page 2 | printed page 2 -->

When choosing a suitable vessel hull type, the emphasis
should be on a safe and dependable steering response.

Using the Dockside wizard
The dockside calibration process must be completed
before the autopilot system can be used for the first
time. The Dockside wizard guides you through the steps
required for dockside calibration.
The Dockside wizard contains different steps, depending
on whether the system includes a rudder reference
transducer:

 The following Dockside       The following Dockside
 wizard procedures apply      wizard procedures only
 to vessels that do NOT       apply to vessels that
 have a rudder reference      include a rudder reference
 transducer:                  transducer:
 • Drive Type selection.      • Drive Type selection
 • Rudder Limit setting.      • Rudder alignment (Align
                                Rudder)
 • Hard-over time setting
   (Raymarine recommends • Rudder Limit
   that this information is
                            • Rudder Drive check.
   specified once the
   dockside wizard and
   Rudder Drive check
   is complete, using the
   Hard Over Time menu
   option).
 • Rudder Drive check.

To access the wizard, ensure the autopilot is in standby,
and then:
1. Select [Dockside Wizard] from the [Commissioning]
   menu [Menu > Set-up > Autopilot Calibration >
   Commissioning].
2. Select [Continue] to initiate the dockside wizard.

Selecting a drive type
Drive type selection is included in the dockside wizard.
If your drive type is not listed, contact your Raymarine
dealer for advice.

With the [Drive Type] menu displayed:
1. Select your drive type.
   The drive types available are:
   • Type 1 / Type 2 Linear
   • Type 2 / Type 3 Hydraulic Linear
   • I/O Stern
   • Wheel Drive

   • Tiller
   • Sport Drive
   • Verado
   • Rotary Drive Type 1 / Type 2
   • Hydraulic Pump Type 1 / Type 2 / Type 3

Drive type selection is also available when the autopilot is
in standby, from the [Drive Type] menu: [Menu > Set-up >
Autopilot Calibration > Vessel Settings > Drive type].

Checking the rudder alignment (Align
Rudder)
This procedure establishes port and starboard rudder
limits for systems using a rudder reference transducer.

                               The following procedure
                               only applies to vessels
                               with a rudder reference
                               transducer.

1. Center the rudder and select [OK].
2. When prompted, turn the rudder hard to port and
   select [OK].
3. When prompted, turn the rudder hard to starboard and
   select [OK].
4. When prompted, turn the rudder back to the center
   and select [OK].

Rudder Limit setting

 For vessels without           For vessels with a rudder
 a rudder reference            reference transducer:
 transducer:                   The rudder alignment
 Rudder limit is set to        process establishes the
 30 degrees and can be         rudder limit. The rudder
 adjusted as required(*)       limit will be displayed with
 using the [Up] and [Down]     a message confirming that
 buttons or the [Rotary        the rudder limit has been
 controller].                  updated.
                               If required, the limit can be
                               adjusted(*) using the [Up]
                               and [Down] buttons or the
                               [Rotary controller].

 Note: *In systems with an ACU-300 and a Constant
 Running pump, the rudder limit is set to 30 degrees, and
 cannot be changed.

<!-- figure 1 on pdf page 2 at 31,62-289,108 pt | caption: none | text-layer labels: none | nearby labels: Using the Dockside wizard | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 2 at 304,161-559,206 pt | caption: none; nearest centred text below: "Checking the rudder alignment (Align Rudder)" | text-layer labels: none | OCR: no legible text (0/2 words >= 60, mean confidence 38) -->
<!-- figure 3 on pdf page 2 at 301,283-433,338 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 2 at 304,434-559,475 pt | caption: none | text-layer labels: none | nearby labels: Rudder Limit setting | OCR: no legible text (0/1 words >= 60, mean confidence 13) -->
<!-- figure 5 on pdf page 2 at 301,504-562,712 pt | caption: none | text-layer labels: none | nearby labels: Rudder Limit setting | OCR: no legible text (0/1 words >= 60, mean confidence 18) -->
<!-- figure 6 on pdf page 2 at 31,585-289,628 pt | caption: none | text-layer labels: none | nearby labels: Selecting a drive type | OCR: no legible text (0/1 words >= 60, mean confidence 32) -->
<!-- figure 7 on pdf page 2 at 304,758-559,808 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 3 | printed page 3 -->

Hard over time
The hard over time setting can be specified as part of the
Dockside wizard.

                               The following information
                               only applies to vessels
                               without a rudder reference
                               transducer.

• If you already know the hard-over time for your vessel’s
  steering system: enter this time during the Dockside
  wizard procedure.
• If you do NOT know the hard-over time for your vessel’s
  steering system: skip this step during the Dockside
  wizard procedure by selecting [SAVE], then proceed
  to Checking the rudder drive section in this document
  to complete the Dockside wizard procedure. Once the
  wizard is complete, proceed to in this document for
  information on how to calculate and adjust the hard-over
  time.

Checking the rudder drive
As part of the dockside calibration process, the system will
check the drive connection. Once it has completed the
check successfully, a message will appear asking if it is
safe for the system to take the helm.
During this procedure the autopilot will move the rudder.
Ensure it is safe to proceed before pressing OK.

When in dockside calibration mode, with the Motor Check
page displayed:
1. Centre and let go of the rudder.
2. Disengage any rudder drive clutch.
3. Select [CONTINUE].
4. Check it is safe to proceed before selecting [OK].
   For vessels with a rudder reference transducer, the
   autopilot will now automatically move the rudder to
   port and then starboard.
5. For vessels without a rudder reference transducer:
   i. You will be asked to confirm that the rudder has
        turned to port by selecting [YES ] or [NO].
   ii. Select [OK] if it is safe to engage the rudder in the
        opposite direction.
   iii. You will be asked to confirm the rudder turned to
        starboard by selecting [YES] or [NO].
6. Dockside calibration is now complete, select
   [CONTINUE].
 Note:
 If you confirmed a “NO” response for the rudder
 movement to both port and starboard, the wizard will
 exit. It is possible that the steering system did not move
 the rudder in any direction, and it will be necessary
 to check the steering system before completing the
 Dockside wizard procedure again.

           Warning: Rudder check
           If no rudder reference has been fitted you
           MUST ensure that adequate provision is
           made to prevent the steering mechanism from
           impacting the end stops.

Adjusting the hard-over time — Evolution
On vessels without a rudder reference transducer, it is
important to set a Hard Over Time.
Before attempting to follow this procedure ensure you
have read and understood the Rudder Check warning
provided in this document.

To estimate your hard over time follow the steps below:
1. With the autopilot in [Standby], manually turn the
   rudder / engine full to port. (For vessels with power
   steering the engine should be running when turning
   the rudder.)
2. Engage [Auto] mode.
3. Press the [+10] and [+1] buttons at the same time
   (p70/p70s) or use the [Rotary] (p70R/p70Rs) to alter
   your locked heading by 90 degrees. Use a stop watch
   to time the movement of the rudder / engine.
4. Estimate how long it would take to move the rudder
   from full port to full starboard. This estimate is your
   [Hard Over Time].
5. Enter this estimate as your Hard Over Time. The Hard
   Over time setting can be accessed from the Drive
   Settings menu: [Menu > Set-up > Autopilot Calibration
   > Drive Settings > Hard Over Time].
6. After setting your Hard Over Time, observe your
   autopilot’s behavior and if required, make small
   adjustments to the Hard Over Time value until a
   satisfactory result is achieved.

Compass linearization — Evolution
autopilots
The EV unit’s internal compass needs to compensate for
local and the Earth’s magnetic fields. This is achieved
using an automatic process known as linearization.
Initial linearization
When the EV unit is first installed and powered-up (or after
a factory reset or compass restart) linearization is required.
A progress bar is displayed to indicate this:

The linearization process will start automatically after
your vessel has turned approximately 100° at a speed
of between 3 –15 knots. Linearization requires no user
input, however at least a 270° turn is required before
linearization can complete. The progress bar displays the

<!-- figure 1 on pdf page 3 at 301,31-347,103 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 3 at 31,82-160,137 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 3 at 31,273-289,319 pt | caption: none | text-layer labels: none | nearby labels: Checking the rudder drive | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 3 at 304,461-559,504 pt | caption: none; nearest centred text below: "Compass linearization — Evolution autopilots" | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 3 at 375,655-485,741 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 5/12 words >= 60, mean confidence 52) -->
325°
78 130°
30.2
Track
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 3 at 31,756-289,806 pt | caption: none | text-layer labels: none | OCR: no legible text (0/2 words >= 60, mean confidence 23) -->

<!-- pdf page 4 | printed page 4 -->

progress, and will turn Red if the process is paused or
otherwise interrupted. The time to complete linearization
varies according to the characteristics of the vessel, the
installation environment of the EV unit, and the levels
of magnetic interference at the time of conducting the
process. Sources of significant magnetic interference may
increase the time required to complete the linearization
process. Examples of such sources include: marine
pontoons, metal-hulled vessels, and underwater cables.
You can speed-up the linearization process by completing
a full 360° turn (at a speed of 3 – 15 knots). You can also
restart the linearization process at any time by selecting
the [Restart Compass] menu item.
Once the initial linearization is complete, the Deviation
page is displayed and the current maximum compass
deviation is shown:

Compass deviation
If the reported deviation is 45° or higher, it is highly
recommended that the EV unit is moved and re-installed in
a location which is subject to less magnetic interference.
After the linearization process has successfully completed
you can check the current deviation value at any time from
the Diagnostics pages.
 Note:
 If “- -” is displayed as the Deviation value, it means that
 linearization has not been successfully completed yet.

Check the compass heading data
As part of the autopilot system commissioning process,
it is recommended that you check the compass heading
value displayed, against a good known heading source on
various headings. Do NOT rely on the reported heading
until compass linearization and alignment is complete.
 Note:
 Once the linearization process has completed, it is
 possible that the heading value may have a slight offset
 of 2 to 3 degrees. This is common where installation
 space is limited, and the EV unit cannot be properly
 aligned to the vessel's longitudinal axis. In this case, it is
 possible to manually adjust the Compass Offset value.

System monitoring and adaptation
To ensure optimum performance, after the initial
linearization process is complete, the EV continues to
monitor and adapt the compass linearization to suit current
conditions.
If the conditions for linearization are less than ideal, the
automatic linearization process temporarily pauses until
conditions improve again. The following conditions can
cause the linearization process to temporarily pause:
• Boat speed < 3 knots.
• Boat speed > 15 knots.
• Rate-of-turn is too slow.
• Significant magnetic interference is present.

Accessing the compass deviation indicator
1. Select [MENU].
2. Select [Set-up].
3. Select [Diagnostics].
4. Select [About Pilot].
   The details related to the pilot diagnostics are
   displayed.
5. Scroll down to the bottom of the list to view the entry
   for Deviation.
 Note: If “- -” is displayed as the Deviation value, it means
 that linearization has not been successfully completed
 yet.

Adjusting the Compass Offset
With the pilot in Standby:
1. From the [Vessel Settings] menu: ([Menu > Set-up >
   Autopilot Calibration > Vessel Settings]).
2. Select [Compass Offset].
3. Use the [+/- 10] button (p70/p70s) or [ROTARY]
   control (p70R/p70Rs) to adjust the compass offset as
   appropriate.
   The [Compass Offset] can be adjusted between –10°
   and +10°.

Compass lock
Once you are satisfied with the compass accuracy, you
can lock the setting to prevent the system from completing
a further automatic linearization in the future.
This feature is particularly useful for vessels in
environments that are exposed to strong magnetic
disturbances on a regular basis (such as offshore wind
farms or very busy rivers, for example). In these situations
it may be desirable to use the Compass lock feature
to disable the continuous linearization process, as the
magnetic interference may build a heading error over time.
 Note:
 The compass lock may be released at any time, to allow
 the compass continual monitoring and adaptation to
 re-commence. This is particularly useful if planning a
 long voyage. The earth’s magnetic field will change
 significantly from one geographical location to another,
 and the compass can continually compensate for the
 changes, ensuring you maintain accurate heading data
 throughout the voyage.

Locking the compass
Follow the steps below to lock the compass linearization.

From the Commissioning menu: ([Menu > Set-up >
Autopilot Calibration > Commissioning])
1. Select [Compass Lock].
2. Select [On].
The compass linearization is now locked.

<!-- figure 1 on pdf page 4 at 105,223-218,307 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 20/22 words >= 60, mean confidence 88) -->
Evolution has successfully detected
and compensated for local Earth's magnetic
fields
Max deviation:
6.4
Linearisation will continue in the
round,
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 4 at 304,367-559,417 pt | caption: none | text-layer labels: none | nearby labels: Compass lock | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
