<!-- font check: Wingdings is not a standard text face; glyphs "" on pages 13. Verify against the rendered page before trusting or mapping. -->

<!-- font check: U+F025 (private-use code from Wingdings) on pages 13; the character carries no meaning as text, read the rendered page -->

<!-- font check: U+F02A (private-use code from Wingdings) on pages 13; the character carries no meaning as text, read the rendered page -->

<!-- font check: no ToUnicode map in Arial,Italic, Arial-Black, Arial-BoldMT, ArialMT, ArialMT-Bold; ligatures (fi, fl) or special glyphs may be missing from the text (pages 1-2, 9, 11-30, 32-34, 36-58, 63-65, 74, 82, 85, 92 checked against the rendered page) -->

<!-- pdf page 1 -->

em-trak A100

 HIGH P
M A RI    ERFOR
                  M A NC
      TIME
                           E

    P RO D
             UCT S

Fully integrated AIS Class A Transceiver

Product Manual

High Performance Maritime Products

www.em-trak.com

<!-- figure 1 on pdf page 1 at 0,0-593,839 pt | caption: none | text-layer labels: HIGH P | em-trak A100 | Fully integrated AIS Class A Transceiver | Product Manual | High Performance Maritime Products | www.em-trak.com | M A RI TIME | ERFOR | P RO D | M A NC | UCT S | E | OCR text follows (tesseract, unverified; 4/6 words >= 60, mean confidence 60) -->
~F)
m-trak WA
0
<!-- end of figure 1 -->

<!-- pdf page 2 -->

Thank you for purchasing this AIS Class A transceiver / Inland AIS.
 This product has been engineered to offer you the highest level of performance and
durability and we hope that it will provide many years of reliable service. We constantly
  strive to achieve the highest possible quality standards, should you encounter any
problems with this product, please contact your dealer who will be pleased to offer any
                                 assistance you require.

<!-- pdf page 3 | printed page 1 -->

Contents
1        Notices..............................................................................................5
1.1      Safety warnings ............................................................................................................................ 5
1.2      General notices............................................................................................................................. 5

2        Introduction......................................................................................7
2.1      About AIS...................................................................................................................................... 7
2.2      Static and dynamic vessel data .................................................................................................... 8
2.3      AIS operation licensing ................................................................................................................. 8

3        Operation..........................................................................................9
3.1      Display and controls...................................................................................................................... 9
3.2      Turning the transceiver on .......................................................................................................... 10
3.3      Display layout.............................................................................................................................. 10
3.4      Main operating screens............................................................................................................... 11
3.5      Target list .................................................................................................................................... 12
3.6      Own vessel and voyage data...................................................................................................... 12
3.7      Own dynamic data ...................................................................................................................... 13
3.8      Received messages.................................................................................................................... 14
3.9      Alarms screen ............................................................................................................................. 15
3.10 Target plot screen ....................................................................................................................... 16
3.11 Working with AIS text and Safety Related Messages (SRMs).................................................... 16
3.12 Handling alarms .......................................................................................................................... 18
3.13 Entering text................................................................................................................................ 19
3.14 Long range messages ................................................................................................................ 20
3.15 Passwords and security .............................................................................................................. 22
3.16 The configuration menu .............................................................................................................. 22
3.17 Tanker mode............................................................................................................................... 28
3.18 Units display - speed and distance ............................................................................................. 28
3.19 Inland AIS ................................................................................................................................... 29

4        Installation......................................................................................31
4.1      What’s in the box? ...................................................................................................................... 32
4.2      Preparing for installation ............................................................................................................. 33
4.3      Installation procedures................................................................................................................ 33
4.4      Connecting the equipment .......................................................................................................... 39
4.5      Configuring the transceiver ......................................................................................................... 49
4.6      Changing the password .............................................................................................................. 52
4.7      Confirming correct operation....................................................................................................... 52
4.8      Regional area settings ................................................................................................................ 52
4.9      Inland AIS ................................................................................................................................... 54

5        Technical Specifications...............................................................57
5.1      Applicable equipment standards................................................................................................. 57
5.2      Physical ...................................................................................................................................... 57
5.3      Environmental ............................................................................................................................ 57
5.4      Electrical .................................................................................................................................... 57

<!-- pdf page 4 | printed page 2 -->

5.5      Display and user interface ......................................................................................................... 58
5.6      Internal GNSS (dual mode GNSS receiver variants) .................................................................. 58
5.7      Internal GNSS (GPS only variants)............................................................................................. 58
5.8      TDMA transmitter ....................................................................................................................... 58
5.9      TDMA receivers .......................................................................................................................... 58
5.10 DSC receiver............................................................................................................................... 59
5.11 RF connections ........................................................................................................................... 59
5.12 Data interfaces............................................................................................................................ 60
5.13 Power and data connector information ....................................................................................... 60

6        Technical reference.......................................................................61
6.1      Interface sentences..................................................................................................................... 61
6.2      Transmission intervals ................................................................................................................ 62
6.3      Sensor data input port................................................................................................................. 62
6.4      Bi-directional data ports .............................................................................................................. 63
6.5      Output drive capability of bi-directional ports .............................................................................. 63
6.6      DGPS port................................................................................................................................... 63
6.7      RS232 port.................................................................................................................................. 63
6.8      Input data sentence formats ....................................................................................................... 63
6.9      Output data sentence formats..................................................................................................... 75
6.10 Priority of sensor ports ................................................................................................................ 80

7        Drawings ........................................................................................82
7.1      AIS transceiver overall dimensions............................................................................................. 82
7.2      Junction box overall dimensions ................................................................................................. 82
7.3      Dash mount bracket fixing holes (drill drawing) (not to scale) .................................................... 83
7.4      GNSS antenna drawing (not to scale)* ....................................................................................... 83

8        Annex A - ERI Ship types..............................................................83
9        Installation record .........................................................................87

<!-- pdf page 5 | printed page 3 -->

List of figures
Figure 1    The AIS network ................................................................................................................. 7
Figure 2    Transceiver front panel ....................................................................................................... 9
Figure 3    Display layout ................................................................................................................... 10
Figure 4    Selection of main operating screen .................................................................................. 11
Figure 5    Target list screen and vessel details view ........................................................................ 12
Figure 6    Own vessel and voyage data screen................................................................................ 12
Figure 7    Own dynamic data screen ................................................................................................ 13
Figure 8    Received messages screen.............................................................................................. 14
Figure 9    Message details view........................................................................................................ 14
Figure 10   Alarms screen................................................................................................................... 15
Figure 11   Alarm details view............................................................................................................. 15
Figure 12   Target plot screen............................................................................................................. 16
Figure 13   Target plot symbols .......................................................................................................... 16
Figure 14   Safety Related Message notification ................................................................................ 17
Figure 15   Message composition ....................................................................................................... 17
Figure 16   Alarm notification screen .................................................................................................. 19
Figure 17   Text entry.......................................................................................................................... 20
Figure 18   Long range interrogation notification; automatic response mode enabled ....................... 21
Figure 19   Long range interrogation notification; manual response mode enabled ........................... 21
Figure 20   Long range message list and details views ...................................................................... 21
Figure 21   Password entry screen ..................................................................................................... 22
Figure 22   Main menu structure ......................................................................................................... 23
Figure 23   Main menu screen ............................................................................................................ 24
Figure 24   The voyage data menu ..................................................................................................... 24
Figure 25   The messages menu ........................................................................................................ 25
Figure 26   The user settings menu .................................................................................................... 25
Figure 27   The installation menu........................................................................................................ 26
Figure 28   The maintenance menu .................................................................................................... 27
Figure 29   Diagnostics menu ............................................................................................................. 27
Figure 30   Tanker mode entry acknowledgement screen.................................................................. 28
Figure 31   Tanker mode exit screen when speed exceeds 3 knots................................................... 28
Figure 32   Typical AIS transceiver connection................................................................................... 31
Figure 33   What’s in the box .............................................................................................................. 32
Figure 34   AIS transceiver dimensions .............................................................................................. 34
Figure 35   Mounting the AIS transceiver............................................................................................ 34
Figure 36   Panel mounting the AIS transceiver ................................................................................. 35
Figure 37   Junction box dimensions .................................................................................................. 36
Figure 38   Mounting the junction box................................................................................................. 36
Figure 39   GNSS antenna location .................................................................................................... 37
Figure 40   GNSS antenna connection ............................................................................................... 37
Figure 41   VHF antenna installation................................................................................................... 38
Figure 42   VHF antenna connection .................................................................................................. 39
Figure 43   Connecting the junction box to the transceiver................................................................. 39
Figure 44   Junction box connections ................................................................................................. 41
Figure 45   Example connection to external display equipment.......................................................... 43
Figure 46   Connecting data interface cable shields ........................................................................... 43
Figure 47   Line termination options.................................................................................................... 44
Figure 48   Differential input connections............................................................................................ 45
Figure 49   Single ended input connection.......................................................................................... 45
Figure 50   Power connection ............................................................................................................. 46
Figure 51   Grounding the transceiver ................................................................................................ 47
Figure 52   PC data (RS232) connection ............................................................................................ 47
Figure 53   Vessel dimensions measurement..................................................................................... 50
Figure 54   Regional areas list screen ................................................................................................ 52
Figure 55   Regional area editing screen ............................................................................................ 53

<!-- pdf page 6 | printed page 4 -->

Figure 56   Regional area settings confirmation screen...................................................................... 53
Figure 57   Inland vessel dimensions.................................................................................................. 55
Figure 58   Blue sign switch connection.............................................................................................. 56
Figure 59   Input port schematic ......................................................................................................... 62
Figure 60   Data output port schematic............................................................................................... 63

<!-- pdf page 7 | printed page 5 -->

    Notices

1        Notices

            When reading this manual please pay particular attention to warnings marked with the
     !      warning triangle symbol shown on the left. These are important messages for safety,
            installation and usage of the transceiver.

1.1 Safety warnings
           This equipment must be installed in accordance with the instructions provided in this manual. Failure
     !     to do so will seriously affect its performance and reliability. It is strongly recommended that a trained
           technician installs and configures this product.
           This equipment is intended as an aid to navigation and is not a replacement for proper navigational
     !     judgement. Information provided by the equipment must not be relied upon as accurate. User
           decisions based upon information provided by the equipment are done so entirely at the users own
           risk.
          Do not install this equipment in a flammable atmosphere such as in an engine room or near to fuel
    !     tanks.
           It is recommended that this product is not installed in direct sunlight or under a windshield where it can
    !      be subjected to excessive solar heating.

           Do not attempt to service this equipment as doing so may cause fire, electric shock or malfunction and
     !     will invalidate the warranty. If any malfunctions are detected contact your supplier or service agent.

           Do not install the transceiver where rain or water may leak onto the equipment. This product has been
     !     designed for installation and use in an environment protected from moisture.

           NOT ALL SHIPS CARRY AIS. The Officer of the Watch (OOW) should always be aware that other
    !      ships and, in particular, leisure craft, fishing vessels and warships may not be fitted with AIS. Any AIS
           equipment fitted on other ships as a mandatory carriage requirement may also be off based on the
           Master’s professional judgement.

1.2 General notices

1.2.1     Position source
All marine Automatic Identification System (AIS) transceivers utilise a satellite based location system such as
the GLONASS or GPS satellite networks.
           The accuracy of a GNSS position fix is variable and affected by factors such as the antenna
    !      positioning, how many satellites are used to determine a position and for how long satellite
           information has been received.

1.2.2     Compass safe distance
The compass safe distance of this transceiver is 0.3m or greater for a 0.3° deviation.

1.2.3     Product category
This product is categorised as ‘protected’ in accordance with the definitions provided in IEC 60945.

1.2.4     Disposal of the transceiver and packaging
Please dispose of this AIS transceiver in accordance with the European WEEE Directive or with the applicable
local regulations for disposal of electrical equipment. Every effort has been made to ensure the packaging for
the transceiver is recyclable. Please dispose of the packaging in an environmentally friendly manner.

<!-- pdf page 8 | printed page 6 -->

Notices

1.2.5     Accuracy of this manual
This manual is intended as a guide to the installation, setup and use of this product. Every effort has been made
to ensure the accuracy of this manual, however due to continuous product development this manual may not
be accurate in all respects, therefore no guarantee is offered. If you are in any doubt about any aspect of this
product, please contact your dealer.

<!-- pdf page 9 | printed page 7 -->

    Introduction

2     Introduction

2.1 About AIS
The marine Automatic Identification System (AIS) is a location and vessel information reporting system. It
allows vessels equipped with AIS to automatically and dynamically share and regularly update their position,
speed, course and other information such as vessel identity with similarly equipped vessels. Position is derived
from GLONASS or GPS and communication between vessels is by Very High Frequency (VHF) digital
transmissions.
There are a number of types of AIS device as follows:
     ● Class A transceivers. These are designed to be fitted to commercial vessels such as cargo ships
       and large passenger vessels. Class A transceivers transmit at a higher VHF signal power than class
       B transceivers and therefore can be received by more distant vessels, and also transmit more
       frequently. Class A transceivers are mandatory on all vessels over 300 gross tonnes on international
       voyages and certain types of passenger vessels under the SOLAS mandate.
     ● Inland AIS stations. Similar to class A transceivers with additional features for use on Inland
       waterways.
     ● Class B transceivers. Similar to Class A transceivers in many ways, but are normally lower cost due
       to the less stringent performance requirements. Class B transceivers transmit at a lower power and at
       a lower reporting rate than Class A transceivers.
     ● AIS base stations. AIS base stations are used by Vessel Traffic Systems to monitor and control the
       transmissions of AIS transceivers.
     ● Aids to Navigation (AtoN) transceivers. AtoNs are transceivers mounted on buoys or other
       hazards to shipping which transmit details of their location to the surrounding vessels.
     ● AIS receivers. AIS receivers receive transmissions from Class A transceivers, Class B transceivers,
       AtoNs and AIS base stations but do not transmit any information about the vessel on which they are
       installed.
This product is a combined Class A AIS / Inland AIS transceiver.

Figure 1    The AIS network

<!-- figure 1 on pdf page 9 at 62,477-512,650 pt | caption: "Figure 1" | text-layer labels: none | OCR text follows (tesseract, unverified; 2/8 words >= 60, mean confidence 42) -->
“Sy SS
<!-- end of figure 1 -->

<!-- pdf page 10 | printed page 8 -->

Introduction

2.2 Static and dynamic vessel data
Information transmitted by an AIS transceiver is in two categories: static and dynamic data.
The vessel's dynamic data which includes location, speed over ground (SOG) and course over ground (COG)
is calculated automatically using the internal GNSS receiver.
Static data is information about the vessel which must be programmed into the AIS transceiver. This includes:
    ● Maritime Mobile Service Identity (MMSI)
    ● Vessel name
    ● Vessel call sign (if available)
    ● Vessel type
    ● Vessel dimensions

2.3 AIS operation licensing
In most countries the operation of an AIS transceiver is included under the vessel's marine VHF licence
provisions. The vessel on to which the AIS transceiver is to be installed must therefore possess a current VHF
radiotelephone licence which lists the AIS system, vessel Call Sign and MMSI number. Please contact the
relevant authority in your country for further information regarding ship’s radio licensing requirements.

<!-- pdf page 11 | printed page 9 | header: Operation -->

3      Operation

This section assumes that the transceiver has been installed in accordance with the instructions provided in
the Installation section of this manual.
Please read the warning notices at the front of this manual before operating the AIS transceiver.

3.1 Display and controls

                                Display

                               Sounder                                                     Menu key

                                                                                           Back or Cancel key

    Pilot plug (behind protective cover)                                                   Scroll wheel

                      Left function key                                                    Right function key

Figure 2        Transceiver front panel

The front panel of the transceiver is shown in Figure 2 with each control marked.
Menu key
This key provides access to the transceiver set up and configuration menu from any operating screen.
Back or Cancel key
This key cancels the current operation, moves to the previous menu level or acts as a backspace key
depending on the operation being carried out.
Scroll wheel
The scroll wheel is used to select information presented on the display, select menu items and edit text and
numeric information shown on the screen. The scroll wheel can also be pressed to confirm data entry or select
information presented on the display.
Right and left function keys
The function of these keys is shown in the display area directly above each key. The function depends on the
operation being carried out.
Sounder
The Sounder provides an audible ‘beep’ when a key is pressed. Key beeps can be activated or deactivated via
the User Settings menu.
Pilot Plug
The Pilot Plug provides an AIS connection for pilots using the IMO standard Pilot Plug connector.
Display
The display shows essential AIS operating information and allows for configuration of the transceiver. It is
recommended that the transceiver is connected to a compatible Radar or Electronic Chart Display System
(ECDIS) for monitoring of AIS vessels during navigation.

<!-- figure 1 on pdf page 11 at 191,187-452,333 pt | caption: none | text-layer labels: none | nearby labels: Display | Sounder | Menu key | OCR text follows (tesseract, unverified; 1/5 words >= 60, mean confidence 36) -->
0000
<!-- end of figure 1 -->

<!-- pdf page 12 | printed page 10 | header: Operation -->

3.2 Turning the transceiver on
The transceiver does not have a power switch and is designed to be permanently powered. When power is first
applied the display will show the text ‘Automatic Identification System’ for 5 seconds before the main operating
screen is shown.

3.3 Display layout
The display layout is shown in Figure 3. All operating screens show the time, status bar, scroll indicators and
relevant function keys. The time displayed is UTC time.
When no UTC time is available from the internal GNSS module the time display will show --:--:-- in place of the
time of day.

                  UTC time                                                                 Status bar

                                      HH:MM:SS

        Main display area                                                                  Scroll indicators

                                              Selec t            Screen

           Left function key                                                               Right function key

Figure 3       Display layout

3.3.1   Status bar icons
The status bar shows the current transceiver status using icons. The meaning of each icon is described in Table 1.

                      Icon          Description

                           OK       The transceiver is operating normally.

                               Tx   Shown for one second following each transmission.

                           Rx       Shown for one second following each received message.

                          INT       Shown when the internal GNSS receiver is set to GPS mode
                          GPS       and has a valid position fix.

                          EXT       Shown when a connected external GPS receiver has a valid
                          GPS       position fix.

                          INT       Shown when the internal GNSS receiver is set to GLONASS
                         GNSS       mode or GPS+GLONASS mode and has a valid position fix*.

                          EXT       Shown when a connected external GNSS receiver has a valid
                         GNSS       position fix*.

                          INT       Shown when the internal GPS receiver is set to GPS mode
                         DGPS       and has a valid differential position fix.

                          EXT       Shown when a connected external GPS receiver has a valid
                         DGPS       differential position fix.

<!-- figure 1 on pdf page 12 at 155,254-435,393 pt | caption: none | text-layer labels: HH:MM:SS | Selec t | Screen | nearby labels: Status bar | UTC time | OCR: no legible text (0/2 words >= 60, mean confidence 46) -->

<!-- pdf page 13 | printed page 11 | header: Operation -->

                 Icon         Description

                   INT        Shown when the internal GNSS receiver is set to GLONASS
                  DGNSS       mode or GPS+GLONASS mode and has a valid differential
                              position fix*.

                   EXT        Shown when a connected external GNSS receiver has a valid
                  DGNSS       differential position fix*.

                    NO        Shown when the internal GNSS receiver is set to GPS mode
                    GPS       and there is no valid internal or external GPS position fix.

                    NO        Shown when the internal GNSS receiver is set to GLONASS
                   GNSS       or GLONASS+GPS mode and there is no valid internal or
                              external GNSS position fix*.

                             Shown when unread AIS safety related text messages are
                              available.

                             Shown flashing when an alarm is active, shown constantly
                              when an alarm is active, but acknowledged.

                    1W        Shown when the transmitter is set to 1W mode.

                     IL       Shown when the AIS transceiver is operating in ‘Inland
                              Waterways’ mode.

* These icons are only displayed for transceiver variants that include a dual mode internal GNSS receiver.
Table 1    Status Icons

3.4 Main operating screens
In normal operation the display shows one of six main operating screens. The next screen can be selected at
any time by pressing the ‘Screen’ function key as shown in Figure 4. The following subsections describe each
of the operating screens in more detail.

                                       Target list             Own vessel &            Own dynamic
                                                               voyage data             data

                                       Target plot             Alarms                  Received
                                                                                       messages

Figure 4   Selection of main operating screen

<!-- figure 1 on pdf page 13 at 189,497-531,609 pt | caption: none | text-layer labels: Target list | Own vessel & voyage data | Own dynamic data | Target plot | Alarms | Received messages | OCR text follows (tesseract, unverified; 6/13 words >= 60, mean confidence 48) -->
I
I
I
I
I
I
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 13 at 62,518-172,612 pt | caption: "Figure 4" | text-layer labels: none | nearby labels: Figure 4 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 14 | printed page 12 | header: Operation -->

3.5 Target list
The target list screen is shown by default after power up. This screen shows the name (or MMSI), range (in
nautical miles) and bearing (in degrees) of other AIS equipped vessels. The nearest vessel is shown at the top
of the list. Only the 200 nearest vessels are shown in the target list, more distant vessels may be viewed if an
AIS enabled external display, RADAR or ECDIS is connected to the transceiver.

                                                                              INT
                                      13:20:47      OK                        GPS

                                     TARGET LIST:
                                     NAME/MMSI             RNG(NM)         BRG(deg)
                                     MARY ROSE             001.5           254.0
                                     REGENT                003.0           013.0
                                     ANNE GALLANT          012.5           135.5
                                     235789543             015.0           003.0
                                     456723557             030.0           087.5
                                                 Selec t               Screen

                                                                              INT
                                      13:20:47      OK                        GPS

                                     VESSEL DETAILS:
                                     Station type:         Class A
                                     MMSI:                 235687901
                                     Name:
                                     >> MARY ROSE
                                     Call Sign:            MYR7A
                                     IMO No:               4325640
                                           Prev. vessel              Nex t vessel

Figure 5    Target list screen and vessel details view

When the target list screen is displayed the scroll wheel can be used to move through the list. Full details of
the highlighted vessel can be shown by pressing the ‘Select’ function key, or pushing the scroll wheel. To return
to the target list from the vessel details screen press the Back key. Whilst the vessel details screen is displayed
it is possible to view details of the next and previous vessels in the vessel list using the left and right function
keys without returning to the target list screen.

3.6 Own vessel and voyage data
This screen shows own vessel and voyage related data. This data relates to the vessel on which the transceiver
is installed.

                                                                              INT
                                      13:20:47      OK                        GPS

                                     OWN VESSEL DATA:
                                     MMSI:          375570700
                                     Name:
                                     >> MERLIN
                                     Call Sign:     POS456
                                     IMO No:        5678901
                                     Destination:   SOUTHAMPTON
                                                                       Screen

Figure 6    Own vessel and voyage data screen

<!-- figure 1 on pdf page 14 at 194,144-394,401 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | RNG(NM) 001.5 003.0 012.5 015.0 030.0 | Selec t | 13:20:47 | Screen | INT GPS | OK | Class A 235687901 | MYR7A 4325640 | Prev. vessel | BRG(deg) 254.0 013.0 135.5 003.0 087.5 | Nex t vessel | OCR: no legible text (0/2 words >= 60, mean confidence 39) -->
<!-- figure 2 on pdf page 14 at 194,564-394,679 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | Screen | OCR: no legible text (0/4 words >= 60, mean confidence 21) -->

<!-- pdf page 15 | printed page 13 | header: Operation -->

The information displayed on this screen includes:
     ● MMSI - the Maritime Mobile Service Identity for the vessel on which the transceiver is installed.
     ● Vessel name
     ● Call sign
     ● Destination - the current voyage destination
     ● IMO Number (where applicable)
     ● ETA - Estimated Time of Arrival at the voyage destination
     ● Draught
     ● Navigational status - At anchor, underway etc
     ● Dimensions for internal GNSS antenna
     ● Crew - number of crew on board
     ● Type of ship/cargo
The scroll wheel can be used to highlight an item of static or voyage data. To edit voyage or installation data see
the ‘Voyage data’ and ‘Installation’ menus in section 3.16 and also the installation information in section 4.

3.7 Own dynamic data
This screen shows current dynamic data from sensors connected to the transceiver and / or its built in GNSS
receiver. This is live information that is being periodically transmitted to other AIS equipped vessels.

The information displayed on this screen includes:
    ● Current date and time (UTC)
    ● Latitude
    ● Longitude
    ● SOG (Speed Over Ground)
    ● COG (Course Over Ground)
    ● Heading
    ● ROT (Rate Of Turn)
    ● Position accuracy
    ● RAIM status
    ● GNSS in use (internal or external)

                                   13:20:47   OK

INT
GPS

OWN DYNAMIC DATA:
Date:         06/01/2010
Time:         13:24:04
Lat:          51°16.7904N
Long:         002°27.9458
SOG:          010.0kts
COG:          134.0°

Figure 7   Own dynamic data screen

Screen

<!-- figure 1 on pdf page 15 at 194,535-394,652 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | Screen | OCR: no legible text (0/2 words >= 60, mean confidence 44) -->

<!-- pdf page 16 | printed page 14 | header: Operation -->

3.8 Received messages
This screen shows AIS text and Safety Related Messages (SRM) received from other AIS stations. The most
recently received message is shown at the top of the list. The date and time of reception, name or MMSI of the
sending station and type of message (text or SRM) are shown in the message list. To view the message content
select the required message using the scroll wheel, then either press the scroll wheel or the “View” function key.
The received messages screen is shown in Figure 8 and the message details screen in Figure 9. When unread
messages are available to view the message icon is shown in the status bar as described in section 3.3.1.

13:20:47   OK

INT
GPS

RECEIVED MESSAGES:
DATE    TIME   FROM      T YPE
29/01   10:00  MARY R... B R Safety
29/01   09:55  556444321 AD Safety
28/01   21:45  REGENT    B R Binar y

                                             V iew

Figure 8   Received messages screen

                                  13:20:47      OK
                                  MESSAGE DETAILS:
                                  Type:    Broadcast SRM
                                  MMSI:    235687901
                                  NAME:
                                  >>MARY ROSE
                                  Channel: A
                                  Date:    29/01/2010
                                             Back

Figure 9   Message details view

Screen

         INT
         GPS

Reply

<!-- figure 1 on pdf page 16 at 196,170-397,288 pt | caption: none | text-layer labels: 13:20:47 | OK | INT GPS | V iew | Screen | OCR text follows (tesseract, unverified; 2/4 words >= 60, mean confidence 60) -->
BR
BR
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 16 at 198,317-397,434 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | Back | Reply | OCR: no legible text (0/1 words >= 60, mean confidence 54) -->

<!-- pdf page 17 | printed page 15 | header: Operation -->

3.9 Alarms screen
This screen shows the status of AIS system alarms. If an active and not yet acknowledged alarm condition
exists the alarm icon in the status bar will flash. If an alarm condition occurs whilst not in the menu system an
acknowledgement screen will be shown immediately, this is described in section 3.12. If an alarm condition
occurs whilst editing a field in the menu system the alarm bell symbol flashes in the status bar.
The alarms screen shows the date and time of activation along with a brief description of any active alarm and
it’s acknowledge state — see Figure 10. Alarms that are active but not acknowledged by the operator have ‘No’
in the ‘ACK’ column. Once an alarm is acknowledged by the operator ‘Yes’ is displayed in the ‘ACK’ column.
An individual alarm can be selected from the list using the scroll wheel and it’s details viewed by either pressing
the scroll wheel or the “View” function key. The alarm details view is shown in Figure 11.

                                                                            INT
                                     13:20:47     OK                        GPS

                                    ALARMS LIST:
                                    DATE   TIME         ALARM                ACK
                                    25/11  16:13        No valid ROT...      Yes
                                    25/11  16:11        Heading lost...      Yes
                                    25/11  16:11        Ex ternal EPFS...    Yes

                                                V iew               Screen

Figure 10 Alarms screen

                                                                            INT
                                     13:20:47     OK                        GPS

                                    ALARM DETAILS:
                                    ALARM: No valid ROT information
                                    ID:    35
                                    DATE:  25/11/2010
                                    TIME:  16:13:30
                                    ACK:

                                                Exit

Figure 11 Alarm details view

           While alarm conditions are active and un-acknowledged, any connected external alarm system
      !    will remain activated.

<!-- figure 1 on pdf page 17 at 194,206-394,321 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | V iew | ACK Yes Yes Yes | Screen | OCR: no legible text (0/3 words >= 60, mean confidence 38) -->
<!-- figure 2 on pdf page 17 at 194,350-394,465 pt | caption: "Figure 11 Alarm details view" | text-layer labels: 13:20:47 | OK | INT GPS | Exit | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 66) -->
f
<!-- end of figure 2 -->

<!-- pdf page 18 | printed page 16 | header: Operation -->

3.10 Target plot screen
The target plot screen shows the location of other AIS equipped vessels and shore stations relative to your own
vessel. The target plot screen provides a basic overview of AIS targets and should not be regarded as a
substitute for display of AIS information on a dedicated electronic chart display system (ECDIS).
                                                                    Heading line (points up to signify heading up)

     Name of selected target         MARY ROSE                          235687901                 MMSI of selected target
         heading up mode            [H UP]                                 27 Tgts                Number of targets on display
            Range selected          12nm

                                    R ange                               Screen

                                                                                                  Selected target

                                                                                     Range selection key

Figure 12 Target plot screen

The plot range can be adjusted by pressing the ‘Range’ function key which cycles through the ranges 48, 24,
12, 6, 3, 1 and 0.5nm. The range relates to radius of the outer range ring shown on the screen.
Individual targets can be selected using the scroll wheel. When selected a square outline will appear around
the target, pressing the scroll wheel will display full vessel details. To return to the target plot screen from the
vessel details screen press the Back or Cancel key.
Different symbols are displayed for an AIS target depending on the type of target and its status, these are
shown in Figure 13. The own vessel symbol is always shown at the centre of the plot.

                                           Target (vessel)     AtoN

                                           Own vessel          Base station

                                             SAR               SART

Figure 13 Target plot symbols

The target plot screen will operate in heading up mode when a source of true heading data is connected to the
AIS (e.g., a gyro compass). If true heading information is not available the target plot will operate in ‘North up’
mode. The mode is displayed as either [H UP] or [N UP] at the top left of the screen. The text ‘No Heading’ is
also displayed on the target plot when operating in north up mode.

3.11 Working with AIS text and Safety Related Messages (SRMs)
AIS text messages and Safety Related Messages (SRMs) can be received from other AIS equipped vessels
and also sent to specific vessels (addressed messages) or sent to all vessels in range (broadcast messages).

3.11.1 Receiving AIS text and Safety Related Messages
Reception of an AIS text message is indicated by the presence of the message icon in the status bar. This icon
is shown whenever there are unread AIS text messages. Messages can be reviewed and replied to via the
messages screen; see section 3.8.
When a Safety Related Message is received the user will be notified immediately with a screen showing the
message. Standard text messages are not displayed on receipt, however the message icon will be displayed
on the status bar.

<!-- pdf page 19 | printed page 17 | header: Operation -->

                                                                       INT
                                   13:20:47     OK                     GPS

                                  SAFET Y RELATED MESSAGE:
                                  Type:    Broadcast SRM
                                  MMSI:    235687901
                                  NAME:
                                  >>MARY ROSE
                                  Channel: A
                                  Date:    29/01/2010
                                              Back             Reply

Figure 14 Safety Related Message notification

3.11.2 Sending AIS Text and Safety Related Messages
To compose a new text or Safety Related Message (SRM) press the ‘Menu’ key then select the ‘MESSAGES’
sub menu followed by the ‘NEW MESSAGE’ option. The new message screen is shown in Figure 15. To send
a message complete the following steps:
    1. Using the scroll wheel highlight the ‘TYPE’ field and select the type of message you wish to send. The
       available options are ‘Broadcast’, ‘Addressed’, ‘Broadcast SRM’ and ‘Addressed SRM’. Click the scroll
       wheel to confirm the message type.
    2. For addressed message types only select the ‘TO’ field and press the scroll wheel. Enter the MMSI of
       the vessel the message should be sent to using the scroll wheel. See section 3.13 for instructions on
       using the scroll wheel to enter data.
    3. Select the ‘MESSAGE’ field and enter your message. Note that the length of a message is limited as
       follows:
         ○ Addressed SRM 156 characters
         ○ Broadcast SRM 161 characters
         ○ Addressed text 151 characters
         ○ Broadcast text 156 characters
    4. Press the ‘Send’ function key to transmit the message.
When an addressed message is sent the addressee will return an acknowledgement on receipt of the
message. If this acknowledgement is not received a warning will be displayed.

                                                                       INT
                                   13:20:47     OK                     GPS

                                  NEW MESSAGE:
                                  Type:              Broadcast SRM
                                  MMSI:              Not required
                                  Channel:           Auto
                                  Message:

                                         Back/Send              Edit

Figure 15 Message composition

           Warning: Class B transceivers are permitted to receive broadcast Safety Related Messages
           and broadcast text messages, however this function is not mandatory. Class B transceivers are
     !     not able to receive addressed Safety Related or text messages. There is therefore no guarantee
           that text messages or SRMs sent to a Class B transceiver will be received.

<!-- figure 1 on pdf page 19 at 194,82-394,197 pt | caption: "Figure 14 Safety Related Message notification" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Reply | OCR: no legible text (0/1 words >= 60, mean confidence 48) -->
<!-- figure 2 on pdf page 19 at 194,506-394,624 pt | caption: "Figure 15 Message composition" | text-layer labels: 13:20:47 | INT GPS | OK | Back/Send | Broadcast SRM Not required Auto | Edit | OCR: no legible text (0/1 words >= 60, mean confidence 44) -->

<!-- pdf page 20 | printed page 18 | header: Operation -->

3.12 Handling alarms
The transceiver performs self checking functions continuously. If a self check fails an alarm will occur. Possible
alarm conditions are listed in Table 2.

      Alarm condition                   Description

      Transmitter malfunction           This alarm will occur if the MMSI has not been configured.
                                        This alarm can occur if there is a fault with the transmitter or if
                                        the antenna VSWR exceeds allowable limits. The alarm will be
                                        cleared if the transmitter recovers normal operation or the VSWR
                                        measurement returns to an allowable value. If this alarm condi-
                                        tion persists contact your dealer or installer.

      Antenna VSWR exceeds limit        This alarm condition can occur if the VSWR (Voltage Standing
                                        Wave Ratio) of the AIS antenna exceeds pre-defined limits. This
                                        alarm is cleared if the VSWR returns to an allowable value. If this
                                        alarm condition persists contact your dealer or installer.

      Receiver channel x malfunc-       This alarm occurs should the receiver hardware malfunction. The
      tion                              receiver is identified by the value of x. If the receiver returns to
                                        normal operation this alarm will be cleared. If this alarm condition
                                        persists contact your dealer or installer.

      External EPFS lost                This alarm occurs if the position from the external Electronic
                                        Position Fixing System (i.e. GNSS) is invalid or lost.

      No sensor position in use         This alarm occurs if the transceiver has no valid position informa-
                                        tion from any connected sensor.

      No valid COG information          This alarm occurs if the transceiver has no valid Course Over
                                        Ground information from any connected sensor.

      No valid SOG information          This alarm occurs if the transceiver has no valid Speed Over
                                        Ground information from any connected sensor.

      Heading lost or invalid           This alarm occurs if the transceiver has no valid heading infor-
                                        mation from any connected sensor, or if the heading is unde-
                                        fined.

      No valid ROT information          This alarm occurs if the transceiver has no Rate Of Turn informa-
                                        tion from connected sensors or via internal calculation.

      NavStatus incorrect               This alarm will occur if the navigation status is in conflict with the
                                        current speed of the vessel. For example the alarm will activate if
                                        the Navigation status is set to moored, but the vessel speed is
                                        greater than 3 knots. Correct the navigation status to clear this
                                        alarm.

      UTC Sync Invalid                  This alarm occurs if UTC time synchronisation is lost. This indi-
                                        cates that the internal GNSS receiver cannot determine the cor-
                                        rect time. Check connections to the internal GNSS antenna.

<!-- pdf page 21 | printed page 19 | header: Operation -->

      Alarm condition                     Description

      Active AIS SART                     An active AIS SART (Search and Rescue Transponder) mes-
                                          sage has been received. The SART will be displayed as the top
                                          item in the target list. Select this item to see the location of the
                                          SART.

      Internal / External GNSS mis-       This alarm occurs if the difference in position reported by the
      match                               internal and external GNSS receivers is too large. Check the
                                          vessel dimensions and GNSS antenna locations have been
                                          entered correctly.

      Heading sensor offset               This alarm occurs if the difference between the course over
                                          ground and heading data is greater than 45° for more than 5 min-
                                          utes. This alarm only occurs if the vessel speed over ground is
                                          greater than 5 knots.

Table 2     Alarm conditions
A new alarm will be indicated by display of the alarm notification screen (see Figure 16). The alarm icon in the
status bar will flash whilst an alarm is active and not acknowledged by the user.

                                                                          INT
                                       13:20:47   OK                      GPS

                                      ALARM NOTIFICATION:
                                      ID     ALARM
                                      35:    No valid ROT information
                                      32:    Heading lost/invalid
                                      25:    Ex ternal EPFS lost

                                             Goto List              Ack

Figure 16 Alarm notification screen

From the alarm notification screen you have the option to immediately acknowledge the alarm by pressing the
‘ACK’ function key, or to view the active alarms list by pressing the ‘Goto List’ function key. Once an alarm is
acknowledged it will remain in the alarms list whilst the underlying alarm condition is active. The presence of
active but acknowledged alarm conditions is indicated by continuous display of the alarm icon in the status bar.

3.13 Entering text
The scroll wheel is used to enter text when updating settings or inputting new information. To enter or change
the text first select the field you wish to edit using the scroll wheel. The selected field is highlighted with white
text on a black background.
If the field is editable the ‘Edit’ function key will be shown. Either press this function key, or push the scroll wheel
to enter edit mode.
If text is already present in the field a solid block will now appear at the first character position, otherwise at the
first character position. Use the scroll wheel to move the block to the character position you wish to edit, then
press the scroll wheel. The selection will now flash, and rotating the scroll wheel will select the character for
this position. When the correct character is selected press the scroll wheel to fix the character and move to the
next character position. To ‘backspace’ (delete) a character simply press the ‘Back’ key. When you have
completed entering text press the ‘Save’ function key to save the updated information. Figure 17 explains the
text entry process.

<!-- figure 1 on pdf page 21 at 194,319-394,432 pt | caption: "Figure 16 Alarm notification screen" | text-layer labels: 13:20:47 | INT GPS | OK | Goto List | Ack | OCR: no legible text (0/2 words >= 60, mean confidence 36) -->

<!-- pdf page 22 | printed page 20 | header: Operation -->

                                                   INT
             10:05:20      OK                      GPS

            Own static and voyage data:
            MMSI: 123456789
            NAME: MERLIN
            DESTINATION: SOUTH
            ETA: 06/06/10 1400Hrs

                         Edit             Screen

                                                   INT
             10:05:23      OK                      GPS

            Own static and voyage data:
            MMSI: 123456789
            NAME: MERLIN
            DESTINATION: SOU T H
            ETA: 06/06/10 1400Hrs

                        Cancel            Save

                                                   INT
             10:05:25      OK                      GPS

            Own static and voyage
                              Q data:
            MMSI: 123456789 R
            NAME: MERLIN       S
            DESTINATION: S O U T H
                              U
            ETA: 06/06/10 1400Hrs
                               V
                              W
                        Cancel            Save

Figure 17 Text entry

3.14 Long range messages

1   2

3   4

5   6

If the transceiver is connected to a long range communication system via the long range communications port
then long range interrogations may be received. These are requests for information from a distant base station
beyond normal AIS operation range.
The transceiver can be configured to automatically respond to Long range (LR) interrogations, or you can opt
to respond to any interrogation manually. Automatic response is the default setting, see section 3.16 for details
of the menu option used to change this setting. Note that in automatic mode all requested information is
returned if it is available.
When a Long range interrogation is received you will be alerted by a notification screen as shown in Figure 18
(when automatic response is enabled) or Figure 19 (when manual response is enabled).
In automatic response mode simply review and acknowledge the notification screen using the ‘Acknowledge’
function key to return to the previous operating screen. In manual response mode you should review the
request and select either the ‘Respond’ or ‘Decline’ function key as appropriate.

<!-- figure 1 on pdf page 22 at 323,86-471,149 pt | caption: none; nearest centred text below: "2" | text-layer labels: none | nearby labels: 2 | 1 | OCR: no legible text (0/1 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 22 at 100,137-301,254 pt | caption: none | text-layer labels: 10:05:20 | INT GPS | OK | Edit | Screen | nearby labels: INT GPS | OK | 10:05:23 | 1 | OCR text follows (tesseract, unverified; 2/4 words >= 60, mean confidence 55) -->
t
4
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 22 at 325,170-387,233 pt | caption: none | text-layer labels: none | nearby labels: 2 | 1 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 22 at 406,170-466,233 pt | caption: none | text-layer labels: none | nearby labels: 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 22 at 103,266-301,384 pt | caption: none | text-layer labels: INT GPS | Cancel | Save | OK | 10:05:23 | nearby labels: Edit | 3 | OK | 10:05:25 | Screen | OCR: no legible text (0/3 words >= 60, mean confidence 28) -->
<!-- figure 6 on pdf page 22 at 325,300-387,362 pt | caption: none | text-layer labels: none | nearby labels: 3 | 4 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 7 on pdf page 22 at 406,302-466,362 pt | caption: none | text-layer labels: none | nearby labels: 4 | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 61) -->
Ne
<!-- end of figure 7 -->
<!-- figure 8 on pdf page 22 at 103,401-301,516 pt | caption: "Figure 17 Text entry" | text-layer labels: INT GPS | Cancel | OK | 10:05:25 | Save | nearby labels: Cancel | 5 | Save | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 40) -->
t
SO
<!-- end of figure 8 -->
<!-- figure 9 on pdf page 22 at 325,432-387,494 pt | caption: none | text-layer labels: none | nearby labels: 5 | 6 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 10 on pdf page 22 at 406,434-466,494 pt | caption: none | text-layer labels: none | nearby labels: 6 | OCR: no legible text (0/1 words >= 60, mean confidence 20) -->

<!-- pdf page 23 | printed page 21 | header: Operation -->

                                                                         INT
                                   13:20:47      OK                      GPS

                                  Long range interrogation:
                                  Date:            31/03/2010
                                  Time:            13:15:39
                                  MMSI:            001245368
                                  Name:
                                  >> RES
                                  Response automatically sent
                                                           Ack nowledge

Figure 18 Long range interrogation notification; automatic response mode enabled

                                                                         INT
                                   13:20:47      OK                      GPS

                                  Long range interrogation:
                                  Date:              31/03/2010
                                  Time:              13:15:39
                                  MMSI:              001245368
                                  Name:
                                  >> RES
                                  Set default responses
                                              Decline         Respond

Figure 19 Long range interrogation notification; manual response mode enabled

A list of received Long range interrogation messages is available at any time via the main menu ‘Messages’
sub menu. See section 3.16 for more details. The Long range message list shows the time and date of
reception of each message along with the sending base station’s MMSI. Full details on each Long range
interrogation in the list can be viewed by pressing the ‘View’ function key. The Long range message list and
details views are shown in Figure 20.

                                                                         INT
                                   13:20:47       OK                     GPS

                                  LONG RANGE MESSAGES:
                                  DATE   TIME   FROM                T YPE
                                  08/01  15:52  002543887           Speed
                                  08/01  15:30  002543887           Position
                                  06/01  09:25  002564410           Course

                                               V iew

                                                                         INT
                                    13:20:47      OK                     GPS

                                   MESSAGE DETAILS:
                                   Date:            08/01/10
                                   Time:            07:35:39
                                   MMSI:            002543887
                                   Name:
                                   >> RES
                                   Response automatically sent
                                               Back               Back

Figure 20 Long range message list and details views

<!-- figure 1 on pdf page 23 at 194,89-394,206 pt | caption: "Figure 18 Long range interrogation notification; automatic response mode enabled" | text-layer labels: 13:20:47 | INT GPS | OK | Ack nowledge | OCR: no legible text (0/1 words >= 60, mean confidence 29) -->
<!-- figure 2 on pdf page 23 at 194,237-394,355 pt | caption: "Figure 18 Long range interrogation notification; automatic response mode enabled" | text-layer labels: 13:20:47 | INT GPS | OK | Decline | Respond | OCR: no legible text (0/1 words >= 60, mean confidence 59) -->
<!-- figure 3 on pdf page 23 at 196,475-397,614 pt | caption: none | text-layer labels: 13:20:47 | INT GPS | OK | T YPE Speed Position Course | V iew | nearby labels: 13:20:47 | INT GPS | OK | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 60) -->
t
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 23 at 198,619-397,736 pt | caption: "Figure 20 Long range message list and details views" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Back | OCR: no legible text (0/1 words >= 60, mean confidence 52) -->

<!-- pdf page 24 | printed page 22 | header: Operation -->

3.15 Passwords and security
Certain important information stored within the transceiver can not be changed without knowledge of the
password. The protected information includes:
     ● MMSI number
     ● Name of vessel
     ● Call sign
     ● IMO number
     ● Vessel dimensions and GNSS antenna locations
     ● Type of ship
     ● Data interface configuration
When trying to edit any of the above information you will be prompted to enter the password.

           The default password is 00000000 (eight zeros). The password may have been changed during
      !    installation. For further information on changing the password refer to section 4.6.

The password entry screen is shown in Figure 21. Use the scroll wheel to select the required digit, then push
the scroll wheel to edit the value of that digit. Entered password digits are masked by asterisks, when complete
press the scroll wheel to enter the password.

                                                        INT
                   10:05:21     OK                      GPS

                   ENTER PASSWORD:
                                     8
                                                                 1                2
                                     9
                                     A......
                                     0
                                     B
                                     C

                              Edit             Screen

Figure 21 Password entry screen

3.16 The configuration menu
The transceiver configuration menu can be accessed at any time by pressing the ‘Menu’ key. The menu is
navigated by rotating the scroll wheel to select a sub-menu or menu item, and pressing the scroll wheel to
select that sub-menu or menu item. Pressing the Back or Cancel key will go back to the previous menu level,
or exit the menu system if you are currently viewing the top level menu. Figure 23 shows the main menu screen.
You can return to the top level menu at any time by pressing the ‘Menu’ key, and exit the menu system at any
time by pressing and holding the Back or Cancel key for one second.
The main menu structure is shown in Figure 22. Some menu items are password protected and can only be
accessed using the password (see section 3.15).
Certain menu items are only available in Inland AIS mode. Please refer to section 3.19.

<!-- figure 1 on pdf page 24 at 330,360-480,417 pt | caption: none; nearest centred text below: "2" | text-layer labels: none | nearby labels: 1 | 2 | OCR: no legible text (0/3 words >= 60, mean confidence 20) -->
<!-- figure 2 on pdf page 24 at 117,393-318,511 pt | caption: "Figure 21 Password entry screen" | text-layer labels: 10:05:21 | INT GPS | OK | ENTER PASSWORD: | 8 9 0 . . . . . . A B C | Edit | Screen | nearby labels: 1 | OCR text follows (tesseract, unverified; 1/4 words >= 60, mean confidence 17) -->
$5
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 24 at 335,439-397,501 pt | caption: none | text-layer labels: none | nearby labels: 1 | 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 24 at 418,439-476,501 pt | caption: none | text-layer labels: none | nearby labels: 2 | OCR: no legible text (0/1 words >= 60, mean confidence 27) -->

<!-- pdf page 25 | printed page 23 | header: Operation -->

             VOYAGE DATA                                          NAVIGATIONAL STATUS

                                                                  DESTINATION

                                                                  ETA

                                                                  LOAD STATUS*

                                                                  BLUE CONES*

                                                                  STATIC DRAUGHT*

                                                                  CREW*

                                                                  PASSENGERS*

                                                                  SHIPBOARD PERSONNEL*

                                                                  ASSISTING TUG BOATS*

                                                                  DRAUGHT**

                                                                  SHIP TYPE

                                                                  CARGO TYPE

                                                                  NUMBER ON BOARD**

             MESSAGES                                             NEW MESSAGE

                                                                  MESSAGE INBOX

                                                                  SENT MESSAGES

                                                                  LONG RANGE MESSAGES

             USER SETTINGS                                        KEY BEEP

                                                                  DISPLAY

                                                                  LONG RANGE CONFIGURATION

                                                                  SET LANGUAGE

                                                                  UNITS

                                                                  SART TEST

             INSTALLATION                                         SET IDENTIFICATION

                                                                  DIMENSIONS

                                                                  CHANGE PASSWORD

                                                                  REGIONAL AREAS

                                                                  SENSOR CONFIGURATION

                                                                  INLAND AIS

                                                                  GNSS SETTINGS †

             MAINTENANCE                                          SYSTEM INFORMATION

                                                                  DIAGNOSTICS

                                                                  SENSOR STATUS

                                                                  ENTER FEATURE CODE

                                                                  COMMUNICATION TEST
 ** Shown in ‘High Seas’ mode only
 * Shown in ‘Inland AIS’ mode only
 † Shown only in variants with dual mode internal GNSS receiver

Figure 22 Main menu structure

<!-- figure 1 on pdf page 25 at 105,307-445,374 pt | caption: none | text-layer labels: MESSAGES | NEW MESSAGE | MESSAGE INBOX | SENT MESSAGES | LONG RANGE MESSAGES | nearby labels: CARGO TYPE | NUMBER ON BOARD** | USER SETTINGS | KEY BEEP | DISPLAY | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 26 | printed page 24 | header: Operation -->

                                                                      INT
                                   13:20:47     OK                    GPS

                                  MAIN MENU:
                                  VOYAGE DATA
                                  MESSAGES
                                  USER SET TINGS
                                  INSTALLATION
                                  MAINTENANCE

                                              Back              Selec t

Figure 23 Main menu screen

3.16.1 Voyage data menu
The voyage data menu provides quick access to the most commonly changed AIS transceiver parameters.

                                                                      INT
                                   13:20:47     OK                    GPS

                                  VOYAGE DATA:
                                  Nav Status:
                                  >>(15) not defined (default)
                                  Destination:
                                  >>Not Available
                                  ETA:               --:--:--
                                  Draught:           Not Available
                                              Back

Figure 24 The voyage data menu

From this menu you can set the following parameters:
    ● Navigational status - select the most appropriate navigational status for your vessel from the list.
       ○ Under way using engine
       ○ At anchor
       ○ Not under command
       ○ Restricted manoeuvrability
       ○ Constrained by her draught
       ○ Moored
       ○ Aground
       ○ Engaged in fishing
       ○ Under way sailing
       ○ Not defined (default)
    ● Destination - enter the destination for the current voyage, 20 characters maximum.
    ● ETA - enter the estimated time and date of arrival at the destination. The date format is DD/MM and
      the time format HH:MM using a 24 hour clock and UTC time.
    ● Draught - enter the maximum present static draught for your vessel in metres. The format for this
      value is xx.x m (e.g., 02.5m). The maximum draught is 25.5m, you should enter this value if your
      draught exceeds 25.5m.
    ● Cargo/ship type - see section 4.5.4.
    ● Number on board - number of crew on board, up to 8191 maximum.

<!-- figure 1 on pdf page 26 at 194,84-394,202 pt | caption: "Figure 23 Main menu screen" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Selec t | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 26 at 194,276-394,389 pt | caption: "Figure 24 The voyage data menu" | text-layer labels: 13:20:47 | OK | INT GPS | Back | OCR: no legible text (0/1 words >= 60, mean confidence 43) -->

<!-- pdf page 27 | printed page 25 | header: Operation -->

3.16.2 Messages menu
The messages menu provides access to AIS text and safety related message functions along with long range
messaging functions.

                                                                    INT
                                    13:20:47     OK                 GPS

                                   MESSAGES:
                                   NEW MESSAGE
                                   MESSAGE INBOX
                                   SENT MESSAGES
                                   LONG RANGE MESSAGES

                                               Back           Selec t

Figure 25 The messages menu

The available options are:
    ● New message - takes you to the message composition screen as described in section 3.8.
    ● Message Inbox - takes you to the received message list view as described in section 3.8.
    ● Sent messages - shows a list of recently sent messages.
    ● Long range messages - view a list of received long range messages as described in section 3.14.

3.16.3 User settings menu
The user setting menu provides access to user configurable preferences for the transceiver. All user settings
are stored within the transceiver and will be maintained if the power supply is switched off.

                                                                    INT
                                    13:20:47     OK                 GPS

                                   USER SET TINGS:
                                   KEY BEEP
                                   DISPLAY
                                   LONG RANGE CONFIGURATION
                                   SET LANGUAGE
                                   UNITS

                                               Back           Selec t

Figure 26 The user settings menu

The available options are:
    ● Key beep - the key press beep can be enabled or disabled.
    ● Display - brightness and contrast adjustment for the LCD display along with selection of day or night
      operating mode. In night mode the display colours are inverted (light text on a dark background).
    ● Long range configuration
        ○ Long range configuration - settings for the long range interface by connection to external
          equipment
        ○ With automatic response enabled a reply will automatically be sent to any Long Range
          interrogations received. You will be notified that an interrogation has occurred as described in
          section 3.14. This is the default setting.
        ○ With manual response enabled you will be given the opportunity to respond or decline to respond
          to any Long Range interrogations received. The notification is described in section 3.14.
        ○ Long range broadcast - enable or disable long range broadcast AIS messages - set to Auto by
          default.
    ● Set language - select the user interface language from the available language options.

<!-- figure 1 on pdf page 27 at 194,118-394,230 pt | caption: "Figure 25 The messages menu" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Selec t | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 27 at 194,401-394,513 pt | caption: "Figure 26 The user settings menu" | text-layer labels: 13:20:47 | OK | INT GPS | Back | Selec t | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 28 | printed page 26 | header: Operation -->

     ● Units - select between Nautical and Metric units for distance and speed display
     ● SART Test - select if AIS SART Test mode is on or off. Messages from AIS Search and Rescue
       Transceivers in test mode will only be displayed when SART Test is on.

3.16.4 Installation menu
The installation menu provides access to settings that are required during installation of the transceiver. Please
refer to the installation section of this manual for more detailed information on installation settings and
requirements. Some settings in the installation menu are password protected and should only be adjusted by
authorised personnel.

                                                                     INT
                                    13:20:47     OK                  GPS

                                    INSTALLATION:
                                    SET IDENTIFICATION
                                    DIMENSIONS
                                    CHANGE PASSWORD
                                    REGIONAL AREAS
                                    SENSOR CONFIGURATION
                                    INLAND AIS
                                               Back            Selec t

Figure 27 The installation menu

The available settings and options are:
     ● Set identification - entry of vessel identification information including MMSI number, name, call sign,
       vessel type and IMO number. This menu is password protected.
     ● Dimensions - entry of vessel dimensions and location of internal and external GNSS antennas. This
       menu is password protected.
     ● Change password - entry of a new system password. This menu is password protected.
     ● Regional areas - through this menu option the user can list, edit and add regional area definitions.
       See section 4.8. This menu is password protected.
     ● Sensor configuration - this sub menu allows the communication speed of the three sensor data input
       ports. See section 4.4.3. This menu is password protected.
     ● Inland AIS – this menu option allows selection of either standard (SOLAS) AIS operation or Inland
       AIS operation. See section 3.19 for further details
     ● GNSS settings – The operating mode of the internal GNSS receiver can be configured to one of the
       following options:
        Note - This option is only displayed for transceiver variants with dual mode internal GNSS.
        ○ GLONASS and GPS (combined operation, default)
        ○ GPS only
        ○ GLONASS only

<!-- figure 1 on pdf page 28 at 191,192-392,305 pt | caption: "Figure 27 The installation menu" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Selec t | OCR: no legible text (0/1 words >= 60, mean confidence 58) -->

<!-- pdf page 29 | printed page 27 | header: Operation -->

3.16.5 Maintenance menu
The maintenance menu provides access to system information and operating diagnostics. These features are
intended for use by authorised installers and service agents only. Access to some maintenance features are
protected by the password.
                                                                      INT
                                     13:20:47     OK                  GPS

                                    MAINTENANCE:
                                    SYSTEM INFORMATION
                                    DIAGNOSTICS
                                    SENSOR STATUS
                                    ENTER FEATURE CODE
                                    COMMUNICATION TEST

                                                Back           Selec t

Figure 28 The maintenance menu

The available settings and options are:
     ● System information - selecting this item will display internal configuration information.
     ● Diagnostics - selecting this item will display internal diagnostic information. See section 3.16.6.
     ● Sensor status - will display the status of external sensors.
     ● Enter feature code - entry of codes to enable system features (installer use only).
     ● Communication test - Conduct an AIS communication test with another AIS equipped vessel. This
       test sends an AIS message to another vessel an checks for a response. Where possible the
       transceiver will automatically select a target vessel in the range 15nm to 25nm. If no vessels are
       available in the recommended test range the closest vessel will be selected.

3.16.6 Diagnostics
Certain diagnostics information is provided to assist with installation and maintenance of the transceiver. This
can be accessed via the Maintenance menu. Figure 29 shows the diagnostics menu page. A number of
features can be accessed via the diagnostics menu:
     ● Internal GNSS status provides GNSS lock status, number of satellites in view and in use and the
       mode of use.
     ● ADC and VSWR data provides internal system information for use in installation and maintenance
       only.
     ● Sensor port status provides details of sensor port settings.

                                                                      INT
                                     13:20:47     OK                  GPS

                                    DIAGNOSTICS:
                                    INTERNAL GPS STATUS
                                    ADC and VSWR
                                    SENSOR PORT STATUS

                                                Decline       Respond

Figure 29 Diagnostics menu

<!-- figure 1 on pdf page 29 at 194,130-394,237 pt | caption: "Figure 28 The maintenance menu" | text-layer labels: 13:20:47 | INT GPS | OK | Back | Selec t | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 29 at 194,552-394,669 pt | caption: "Figure 29 Diagnostics menu" | text-layer labels: 13:20:47 | OK | INT GPS | Decline | Respond | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 30 | printed page 28 | header: Operation -->

3.17 Tanker mode
To comply with ISGOTT International Safety Guide for Oil Tankers & Terminals a 1W transmission mode is
provided in the AIS transceiver. When the vessel type is defined as a tanker (see section 4.5.4) and the
navigation status is set to ‘Moored’ (see section 4.5.4) then the transmitter power will be automatically reduced
to 1W. An acknowledgement screen as shown in Figure 30 is displayed when this set of conditions is met. A
‘1W’ icon is displayed in the status bar when tanker mode is enabled (see section 3.3).

                                                                            INT
                                     13:20:47     OK                        GPS

                                    TANKER MODE:

                                                  Entering Tanker Mode

                                                       Transmit Power is
                                                        Low Power (1W )

                                                                    Ack nowledge

Figure 30 Tanker mode entry acknowledgement screen

This mode is automatically disabled if the vessel type or navigation status conditions no longer apply. An
acknowledgement screen similar to Figure 31 is displayed when tanker mode has been disabled. Tanker mode
is also disabled if the vessel speed exceeds 3 knots as it is assumed that the vessel is no longer moored above
this speed. In this case the navigation status should be adjusted appropriately and a prompt is displayed as
shown in Figure 31. Selecting the ‘Change’ option will display the voyage data settings where the navigation
status can be updated.

                                                                            INT
                                     13:20:47     OK                        GPS

                                    TANKER MODE:
                                                   Exiting Tanker Mode
                                                    Transmit Power is
                                                   High Power (12.5W )
                                                   Change Nav. Status?
                                                   ( Currently moored )
                                                Back                  Change

Figure 31 Tanker mode exit screen when speed exceeds 3 knots

3.18 Units display - speed and distance
When operating in Class A (SOLAS) mode the default units for speed and distance are knots (kn) and nautical
miles (nm) respectively.
When operating in Inland AIS mode the default units for speed and distance are kilometers per hour (km/h) and
kilometers (km).
It is possible to override the default units through the ‘User settings’ menu. Press the menu key and then select
‘User settings’ followed by ‘Units’. You can now select either nautical or metric display of speed and distance
regardless of the AIS mode.

<!-- figure 1 on pdf page 30 at 196,158-397,276 pt | caption: "Figure 30 Tanker mode entry acknowledgement screen" | text-layer labels: 13:20:47 | INT GPS | OK | TANKER MODE: | Entering Tanker Mode | Transmit Power is Low Power (1W ) | Ack nowledge | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 30 at 196,396-397,511 pt | caption: "Figure 31 Tanker mode exit screen when speed exceeds 3 knots" | text-layer labels: 13:20:47 | INT GPS | OK | TANKER MODE: | Change Nav. Status? ( Currently moored ) | Back | Change | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 31 | printed page 29 | header: Operation -->

3.19 Inland AIS
The transceiver supports both standard ‘high seas’ operation and ‘Inland AIS’ operation. Inland AIS is an
extension of AIS intended for use on board vessels navigating Inland waterways.
During installation the transceiver will be configured appropriately for either high seas or inland operation.
When the transceiver is configured for inland operation the ‘IL’ icon will be displayed on the status bar (see
section 3.3.1). Information on enabling / disabling inland AIS mode along with additional configuration required
for inland operation can be found in section 4.9.

3.19.1 Own vessel and voyage data display in Inland AIS mode
Additional own vessel and voyage related data is displayed on the main operating screens in inland AIS mode.
The following additional information is displayed on the own vessel data screen (as described in section 3.6):
     ● Blue sign status is displayed as either ‘Yes’ (the sign is set), ‘No’ (the sign is not set) or ‘Unavailable’
       when the blue sign switch is not installed. If a blue sign switch is installed it should be manually
       switched to the appropriate setting during navigation (see section 3.19.4).
     ● The IMO number is set to ‘0’ or ‘0000000’ when operating in inland AIS mode.
     ● The dimensions of the vessel are set to the maximum rectangular size of the convoy when operating
       in inland AIS mode.
     ● The ENI (unique European Vessel Identification Number) for the vessel is shown.
     ● The ship (or combination type) is shown using an ERI classification code. A table of ERI codes is
       provided in section 8 for reference.
     ● The load status of the vessel is displayed as ‘Loaded’, ‘Unloaded’ or ‘Unavailable’.
     ● The number of crew, passengers and other shipboard personnel will be displayed.

3.19.2 Target vessel details display in Inland AIS mode
Additional detail relating to target vessels is available when operating in Inland AIS mode. The additional
information is only displayed for target vessels which are also equipped with an Inland AIS transceiver and are
transmitting inland AIS data.
The target vessel details display described in section 3.5 will show the following additional data:
     ● Blue sign status is displayed as either ‘Yes’ (the sign is set), ‘No’ (the sign is not set) or ‘Unavailable’.
     ● The IMO number is not shown for Inland target vessels, the ENI (unique European Vessel
       Identification Number) for the vessel is shown instead.
     ● The displayed dimensions of the vessel are the maximum rectangular size of the convoy.
     ● The target vessel destination is displayed as a UN location code and ERI terminal code.
     ● The ship (or combination type) is shown using an ERI classification code. A table of ERI codes is
       provided in section 8 for reference.
     ● The load status of the vessel is displayed as ‘Loaded’, ‘Unloaded’ or ‘Unavailable’.
     ● Quality of speed, course and heading information will be shown as ‘high’ when the target vessel is
       using an approved sensor to generate this data, or low if the data is derived from internal GNSS only.
     ● The number of crew, passengers and other shipboard personnel will be displayed.

3.19.3 Setting voyage data in Inland AIS mode
Additional voyage related information is required for Inland operation along with some changes to the standard
AIS configuration. The following additional information must be entered into the AIS transceiver:
     ● The vessels load status as ‘Loaded’, ‘Unloaded’ or ‘Unavailable’.
     ● The number of blue cones or blue flag status for the cargo (1, 2 or 3 blue cones, or blue flag).
     ● The static draught of the vessel to the nearest centimeter.
     ● The number of crew (0 to 254 or unknown), passengers (0 to 8190 or unknown) and other shipboard
       personnel (0 to 254 or unknown).

<!-- pdf page 32 | printed page 30 | header: Operation -->

     ● The number of assisting tugboats (from 0 to 6).
The additional identification information can be entered via the main menu. Press the ‘Menu' key then select
the ‘Voyage data’ sub-menu. When the AIS transceiver is operating in Inland AIS mode the voyage data entry
screen will be extended to allow input of the additional information described above.
The following standard AIS voyage information must be updated for Inland AIS:
     ● Destination
The voyage destination should be entered using UN terminal location codes and ERI terminal codes where
possible.

3.19.4 Blue sign operation
A ‘blue sign’ switch may optionally be connected to the AIS transceiver during installation. This switch sets the
‘blue sign’ status in transmitted inland AIS position reports to either ‘Set’ or ‘Not set’. If a blue sign switch is not
installed the blue sign status is transmitted as ‘not available’.
If a blue sign switch is installed it should be set according to the current navigational situation. The current blue
sign status will be displayed on the own vessel data screen.

<!-- pdf page 33 | printed page 31 | header: Installation -->

4    Installation

The transceiver has been designed for ease of installation. The transceiver is a ‘one box’ design containing
both the transceiver and display. An external junction box is provided to simplify connection of sensor and
display data wiring. A typical system and connection diagram is provided in Figure 32.

                      VHF antenna               GNSS antenna

    Above decks

    Below decks

                   Junction box

                      Displays
                   (ECDIS, RADAR)

Figure 32 Typical AIS transceiver connection

The main elements of installation are:

                              Optional PC

Pilot equipment               12/24V DC Supply

        Ship’s sensor data
      (DGPS, GYRO, Heading)

1. Mount the transceiver and junction box in a suitable location.
2. Install VHF antenna according to manufacturers instructions.
3. Install the GNSS antenna.
4. Connect data interfaces.
5. Apply power and configure the transceiver.
6. Confirm correct operation.
7. Complete the installation log.

<!-- figure 1 on pdf page 33 at 120,154-507,559 pt | caption: "Figure 32 Typical AIS transceiver connection" | text-layer labels: VHF antenna | GNSS antenna | Optional PC | Junction box | Pilot equipment | 12/24V DC Supply | nearby labels: Displays (ECDIS, RADAR) | Ship’s sensor data (DGPS, GYRO, Heading) | OCR text follows (tesseract, unverified; 1/17 words >= 60, mean confidence 29) -->
000
<!-- end of figure 1 -->

<!-- pdf page 34 | printed page 32 | header: Installation -->

4.1 What’s in the box?
Figure 33 shows the items included with your AIS transceiver purchase. The following section gives a brief
overview of each item. Please ensure all items are present and if any of the items are missing please contact
your dealer.
         Transceiver             Panel mount brackets           Mounting template
                                                                                               Junction box

                                    Trunnion bracket
                                                                                       Product manual
         Data cable         GNSS antenna                Power cable       Screws
                                                                                                       Quick
                                                                                                    installation
                                                                                        CD             guide

                                                                                                      Quick
                                                                                                    operation
                                                                                                      guide

Figure 33 What’s in the box

    ● AIS transceiver
        The main transceiver and display.
    ● Data cable
        A 1m (3.3ft) long, 50 way data cable to connect the transceiver serial data ports to the junction box.
    ● Junction box
        Provides screw terminals for the data connections to ships sensors and display systems.
    ● Power cable
        A 2m (6.6ft) long power cable to supply the transceiver. The power cable also includes alarm output
        connections.
    ● Trunnion bracket
        Bracket for mounting the transceiver above a flat surface (e.g., on top of an instrument panel).
    ● Panel mount brackets
        Clamp brackets used when mounting the transceiver through a panel (flush mount).
    ● Fixing screws
        Eight fixing screws are provided for mounting the transceiver (when using the trunnion bracket) and
        the junction box.
    ● User and installation manual
        This document - please read thoroughly before attempting to install and commission the transceiver.
    ● Quick start guide
        The quick start guide gives a handy one page reference for the installation process.
    ● GNSS antenna
        A GNSS antenna for the internal GNSS receiver supplied with 10m of co-axial cable.
    ● Support tools CD
        Software tools for configuration of the AIS transceiver and this user manual in other languages.
    ● Mounting template
        Template for cutting an aperture when panel mounting the transceiver.

<!-- figure 1 on pdf page 34 at 304,146-423,221 pt | caption: none | text-layer labels: none | nearby labels: Mounting template | Power cable | Screws | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 34 at 62,149-170,235 pt | caption: none; nearest centred text below: "Data cable" | text-layer labels: none | nearby labels: Transceiver | Data cable | OCR: no legible text (0/3 words >= 60, mean confidence 10) -->
<!-- figure 3 on pdf page 34 at 194,149-287,216 pt | caption: none; nearest centred text below: "Trunnion bracket" | text-layer labels: none | nearby labels: Panel mount brackets | Trunnion bracket | GNSS antenna | OCR: no legible text (0/5 words >= 60, mean confidence 36) -->
<!-- figure 4 on pdf page 34 at 437,161-526,213 pt | caption: none | text-layer labels: none | nearby labels: Junction box | Product manual | OCR: no legible text (0/3 words >= 60, mean confidence 17) -->
<!-- figure 5 on pdf page 34 at 416,228-526,338 pt | caption: none | text-layer labels: Product manual | CD | Quick installation guide | Quick operation guide | OCR text follows (tesseract, unverified; 2/2 words >= 60, mean confidence 62) -->
I
J
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 34 at 167,240-351,343 pt | caption: "Figure 33 What’s in the box" | text-layer labels: GNSS antenna | Power cable | nearby labels: Trunnion bracket | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 87) -->
O
<!-- end of figure 6 -->
<!-- figure 7 on pdf page 34 at 62,249-163,348 pt | caption: "Figure 33 What’s in the box" | text-layer labels: none | nearby labels: Data cable | Figure 33 What’s in the box | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 8 on pdf page 34 at 356,257-411,314 pt | caption: none | text-layer labels: none | nearby labels: Screws | CD | OCR text follows (tesseract, unverified; 1/4 words >= 60, mean confidence 51) -->
j7
<!-- end of figure 8 -->

<!-- pdf page 35 | printed page 33 | header: Installation -->

4.2 Preparing for installation
In addition to the items provided with the transceiver the following items will be required to complete the
installation:

4.2.1   VHF Antenna
Connection of a suitable VHF antenna will be required for the AIS transceiver to operate. A standard marine
band VHF antenna such as that used with VHF voice radios is sufficient. The antenna cable should be
terminated with a PL-259 (or UHF) connector. Please take note of the warnings listed at the start of this manual
regarding the installation and use of antennas.

4.2.2   Antenna cables
The supplied GNSS antenna is provided with 10 metres (32.8ft) of cable. If this is not sufficient to reach
between the desired GNSS antenna location and the AIS transceiver you will require an extension cable.
Please contact your dealer for details. For reference the GNSS antenna connector type on the AIS transceiver
is a TNC receptacle and is intended to mate with a TNC jack connector on the GNSS antenna cable.

4.2.3   GNSS antenna mount
A mounting bracket is required for the supplied GNSS antenna. The antenna has a standard one inch 14 TPI
pole mount thread. You should source and install a compatible antenna bracket suitable for the installation
location.

4.2.4   Data interface cables
Suitable screened, multi core cable will be required to connect the ships sensor (DGPS, Gyro etc.) data ports
to the AIS junction box.

4.3 Installation procedures
Before beginning installation of your AIS transceiver, please ensure you have the necessary additional items
as detailed in section 4.2. It is strongly recommended that you read all of the instructions in this manual prior
to installation.
If after reading this manual you are unsure about any aspect of the installation process please contact your
dealer for advice. The following sections explain the installation process step by step for each of the main
system elements.

4.3.1   Step 1 - Installing the AIS transceiver
Please note the following guidelines when selecting a location for your AIS transceiver:
     ● The AIS transceiver must be fitted in a location where it is at least 30cm (1ft) from a compass or any
       magnetic device.
     ● There should be adequate space around the AIS transceiver for routing of cables. See Figure 34 for
       details of the AIS transceiver dimensions.
     ● The ambient temperature around the AIS transceiver should be maintained between -15°C and +55°
       (5°F to 131°F). Ensure adequate ventilation is present when panel mounting the transceiver.
     ● The AIS transceiver should not be located in a flammable or hazardous atmosphere such as in an
       engine room or near to fuel tanks.
     ● The AIS transceiver must be installed in a 'below decks' environment protected from the weather.
     ● The transceiver is supplied with four self tapping screws for attachment of the AIS transceiver to a
       suitable surface using the trunnion bracket. Please refer to Figure 35 for guidance.
     ● The transceiver is supplied with panel mount clamps for flush mounting through an instrument panel.
       Please refer to Figure 36 for guidance. Access behind the panel is required when using this mounting
       option.
     ● The AIS transceiver should be mounted in a location where the display is visible to the user at the
       position from which the vessel is normally operated.

<!-- pdf page 36 | printed page 34 | header: Installation -->

● An AC power port should be available near to the pilot plug. A pilot plug is located on the front panel
  of the AIS transceiver and can also be relocated using the junction box. Please refer to section 4.4.2
  for guidance.

                                172 mm

                                195 mm

              105 mm

Figure 34 AIS transceiver dimensions

Figure 35 Mounting the AIS transceiver

157 mm

    112 mm

             85 mm

<!-- figure 1 on pdf page 36 at 134,132-304,283 pt | caption: none; nearest centred text below: "195 mm" | text-layer labels: none | nearby labels: 172 mm | 195 mm | OCR: no legible text (0/4 words >= 60, mean confidence 6) -->
<!-- figure 2 on pdf page 36 at 330,288-483,425 pt | caption: none | text-layer labels: 112 mm | nearby labels: 157 mm | 85 mm | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 96) -->
112mm
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 36 at 127,307-304,425 pt | caption: "Figure 34 AIS transceiver dimensions" | text-layer labels: none | nearby labels: 105 mm | 195 mm | OCR text follows (tesseract, unverified; 1/6 words >= 60, mean confidence 40) -->
0000
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 36 at 186,477-414,732 pt | caption: "Figure 34 AIS transceiver dimensions" | text-layer labels: none | OCR text follows (tesseract, unverified; 2/13 words >= 60, mean confidence 32) -->
LZ
Z
<!-- end of figure 4 -->

<!-- pdf page 37 | printed page 35 | header: Installation -->

Figure 36 Panel mounting the AIS transceiver

4.3.2       Step 2 - Installing the junction box
The transceiver receives data from the ship’s sensors via the 50 way data cable which connects to the rear of
the transceiver. The other end of this cable is connected to the junction box which provides a convenient screw
terminal system for connection of ships sensor data cables.
              To meet IMO requirements the AIS transceiver must be able to transmit at least Speed over
        !     Ground (SOG), Course over Ground (COG) and Rate of Turn (ROT) information. This data is
              obtained by connecting data outputs from the ship’s DGPS, Gyrocompass and other sensors to
              the transceiver via the junction box.

Please note the following guidelines when selecting a location for the junction box:
    ● There should be adequate space around the junction box for routing of cables. See Figure 37 for
      details of the junction box dimensions.
    ● The ambient temperature around the junction box should be maintained between -15°C and +55°
      (5°F to 131°F).
    ● The junction box should not be located in a flammable or hazardous atmosphere such as in an engine
      room or near to fuel tanks.
    ● The junction box must be installed in a 'below decks' environment protected from the weather.
    ● The transceiver is supplied with four self tapping screws for attachment of the junction box to a
      suitable surface. Please refer to Figure 38 for guidance.
    ● The junction box must be located within 1m (3.2ft) of the AIS transceiver to allow for the length of the
      supplied data interface cable.

<!-- figure 1 on pdf page 37 at 79,89-519,420 pt | caption: "Figure 36 Panel mounting the AIS transceiver" | text-layer labels: none | OCR: no legible text (0/15 words >= 60, mean confidence 30) -->

<!-- pdf page 38 | printed page 36 | header: Installation -->

                                          165 mm

                       58 mm

                       52 mm

                                          178 mm                               76 mm

Figure 37 Junction box dimensions

Figure 38 Mounting the junction box

4.3.3   Installing the GNSS antenna
The AIS transceiver includes an internal GNSS receiver for time synchronisation. An independent GNSS
antenna is required for this receiver in addition to any GNSS equipment already installed on board.
For mounting of the GNSS antenna supplied with your AIS transceiver you will require a one inch 14 TPI pole
mount. Contact your dealer to source a mount suitable for the installation location.
Please note the following guidelines when selecting a location for the GNSS antenna:
    ● The GNSS antenna mount should be secured to a rigid surface.
    ● The GNSS antenna should be located where it has a clear, unobstructed view of the sky overhead.
    ● The GNSS antenna should be mounted as high as possible, however it is not recommend the antenna
      is mounted on a top of a high mast where the motion of the vessel will cause the antenna to swing
      and potentially reduce the accuracy of the GNSS position. See Figure 39 for guidance.

<!-- figure 1 on pdf page 38 at 165,94-339,204 pt | caption: none | text-layer labels: none | nearby labels: 58 mm | 165 mm | OCR: no legible text (0/7 words >= 60, mean confidence 16) -->
<!-- figure 2 on pdf page 38 at 163,218-339,285 pt | caption: "Figure 37 Junction box dimensions" | text-layer labels: 52 mm | nearby labels: 178 mm | OCR text follows (tesseract, unverified; 1/4 words >= 60, mean confidence 43) -->
L
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 38 at 361,218-461,285 pt | caption: none | text-layer labels: none | nearby labels: 76 mm | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 38 at 201,329-378,566 pt | caption: "Figure 37 Junction box dimensions" | text-layer labels: none | OCR text follows (tesseract, unverified; 1/7 words >= 60, mean confidence 36) -->
J
<!-- end of figure 4 -->

<!-- pdf page 39 | printed page 37 | header: Installation -->

    ● If possible mount the antenna at least 5m (16ft) from any RADAR or Satellite communications
      antennas, and ensure the GNSS antenna is not in the beam path from any RADAR antenna.
    ● Route the GNSS antenna cable through the pole mount and then to the AIS transceiver. If extension
      cables are required all junctions should be made using appropriate co-axial connectors and made
      watertight.
    ● Connect the GNSS antenna cable to the GNSS connector on the AIS transceiver as shown in Figure 40.

                                                                             GNSS antenna mounted
                                                                             on a rigid surface

                                           GNSS antenna should
                                           be at least 5m (16ft)                   Away from RADAR
                                           from RADAR or Satellite                 beam path
                                           communication
                                           antennas

Figure 39 GNSS antenna location

                                              GNSS antenna connection

Figure 40 GNSS antenna connection

4.3.4   Installing the VHF antenna
The AIS transceiver requires a dedicated VHF antenna for communications. A standard marine VHF antenna
is suitable.

<!-- figure 1 on pdf page 39 at 81,178-497,446 pt | caption: "Figure 39 GNSS antenna location" | text-layer labels: none | nearby labels: GNSS antenna mounted on a rigid surface | Away from RADAR beam path | OCR: no legible text (0/16 words >= 60, mean confidence 6) -->
<!-- figure 2 on pdf page 39 at 170,506-416,655 pt | caption: "Figure 39 GNSS antenna location" | text-layer labels: none | nearby labels: GNSS antenna connection | OCR text follows (tesseract, unverified; 2/20 words >= 60, mean confidence 30) -->
fo)
yy
<!-- end of figure 2 -->

<!-- pdf page 40 | printed page 38 | header: Installation -->

Please note the following guidelines when selecting and locating the AIS VHF antenna:
    ● The VHF antenna should be located as high as possible and positioned as far from other antennas as
      possible.
    ● The VHF antenna should have omnidirectional vertical polarization.
    ● Where possible the VHF antenna should be installed at least 3m (10ft) away from other transmitting
      radio, satellite and RADAR antennas.
    ● Ideally the AIS VHF antenna should be mounted directly above or below the ship’s primary VHF
      radiotelephone antenna, with no horizontal separation and with a minimum of 2m vertical separation.
      If it is located on the same horizontal level as other antennas, the distance apart should be at least
      10m. Refer to Figure 41 for further guidance.
    ● The VHF antenna cable should be kept as short as possible to minimise signal loss. High quality, low
      loss coaxial cable appropriate to the installation location should be used.
    ● The VHF antenna cable should be terminated in a PL-259 co-axial connector for connection to the
      AIS transceiver.
    ● Any outdoor installed connectors in the antenna cables should be waterproof by design.
    ● Antenna cables should be installed in separate signal cable channels at least 10cm (4ins) away from
      power supply cables. Crossing of cables should be done at right angles and sharp bends in the
      antenna cables should be avoided.
    ● Connect the VHF antenna cable to the VHF connector on the AIS transceiver as shown in Figure 42.

                                                         VHF antenna          Positioned at least 3m (10ft)
                                                                              from other transitting radio,
                                                                              satellite and RADAR antennas

Figure 41 VHF antenna installation

<!-- figure 1 on pdf page 40 at 74,353-480,619 pt | caption: "Figure 41 VHF antenna installation" | text-layer labels: VHF antenna | OCR: no legible text (0/3 words >= 60, mean confidence 19) -->

<!-- pdf page 41 | printed page 39 | header: Installation -->

                                                           VHF antenna connection

Figure 42 VHF antenna connection

4.4 Connecting the equipment
With the transceiver, junction box and antenna installed it is now possible to connect the equipment in
preparation for commissioning.

4.4.1   Antenna connections
If antenna connections have not already been made the GNSS and VHF antennas should now be connected
to the transceiver. Refer to Figure 40 and Figure 42 for guidance.

4.4.2   Data connections
The transceiver is supplied with a 1m (3.2ft) 50 way data cable for interconnection of the transceiver and
junction box.
Connect the junction box to the transceiver using the data cable as indicated in Figure 43.

                                                                        Transceiver
                           Junction box

Figure 43 Connecting the junction box to the transceiver

<!-- figure 1 on pdf page 41 at 172,89-418,237 pt | caption: "Figure 42 VHF antenna connection" | text-layer labels: none | nearby labels: VHF antenna connection | OCR text follows (tesseract, unverified; 4/18 words >= 60, mean confidence 34) -->
ie
O
7
S22
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 41 at 139,494-445,681 pt | caption: "Figure 43 Connecting the junction box to the transceiver" | text-layer labels: Transceiver | Junction box | OCR: no legible text (0/3 words >= 60, mean confidence 10) -->

<!-- pdf page 42 | printed page 40 | header: Installation -->

4.4.3       Sensor configuration
The transceiver has seven NMEA0183 (IEC61162-1/2) data ports for connection of ship’s sensors and display
equipment as described in Table 3. There are three input ports for ship’s sensor data and three bidirectional
ports for connection of display equipment such as Radar or electronic chart displays. It is recommended that
an AIS compatible electronic charting system is connected to the transceiver for display of AIS targets. To
comply with IMO regulations the AIS must be connected to speed over ground (SOG), course over ground
(COG), heading, rate of turn (ROT) and position information sources.
The three sensor ports are input only data ports for the connection of data from ships sensors. The four
remaining ports are bi-directional high speed connections supporting data input and output from the AIS. These
ports are suitable for connection to ECDIS, AIS enabled RADAR displays and Pilot equipment.
All data input connections are optically isolated.

 Data port             Function                      Type                          Default Baud rate

 1                     Sensor 1 input                Receive only                  4800
                       (DGNSS -
                       COG/SOG/LAT/LON)

 2                     Sensor 2 input                Receive only                  4800
                       (Rate of Turn)

 3                     Sensor 3 input                Receive only                  4800
                       (Gyro heading)

 4                     External display / ECDIS      Bi-directional                38400

 5                     Pilot port                    Bi-directional                38400

 6                     Long Range                    Bi-directional                38400

 7                     DGPS beacon receiver          Bi-directional                4800

Table 3        Serial data ports
All sensor ports can be configured via the sensor configuration menu which can be found under the Main
menu>Installation>Sensor configuration menu option.
The sensor configuration menu also includes the ability to disable the requirement for external GNSS sensors
to provide a DTM (Datum) sentence, as not all external GNSS devices provide this sentence.
An option for NMEA0183 Compatibility is provided to enable interface with older equipment supporting
NMEA0183 interface versions prior to version 3.01.
              If an external GNSS device which does not provide a DTM sentence is connected to the
        !     transceiver and the transceiver is configured to require DTM sentences, the external GNSS data
              will not be accepted by the transceiver. If no DTM sentence is required the WGS84 datum will be
              used as a coordinate origin and the external GNSS device must be configured to output position
              using this datum.

4.4.4       Junction box connections
The junction box provides screw terminal connections for each of the seven data ports. The connections and
functions of each connection are defined in Table 4. All connections are labeled on the junction box PCB for
clarity. A diagram showing connections available inside the junction box is provided in Figure 44.

<!-- pdf page 43 | printed page 41 | header: Installation -->

Use of shielded cable is recommended when connecting ships sensors and display systems to the junction box
Connect the cable shield to the terminal block marked ‘GND’ for the appropriate interface. It is possible to
remove the PCB from the junction box enclosure to aid connection of cables to the screw terminals during
installation.

            Do not connect the shield of both the external equipment and the junction box. Connect at only
      !     one end.

                                                                           To transceiver

          Bidirectional data ports                                                                                  Termination jumpers      Sensor data inputs

                                EXT_DISP_IN         PILOT_IN         DGPS_IN         LR_IN           SEN1          SEN2           SEN3
                                A    B GND      A       B GND    A      B GND    A     B GND     A     B GND   A     B GND   A      B GND

                                  A    B GND        A    B GND       A   B GND       A      B GND COM NC NO    GND GND GND       SM BS COM
                                 EXT_DISP_OUT        PILOT_OUT        DGPS_OUT           LR_OUT      ALARM        SHIELD          SWITCHES

                                                                                Cable glands

Figure 44 Junction box connections

<!-- figure 1 on pdf page 43 at 81,223-512,509 pt | caption: "Figure 44 Junction box connections" | text-layer labels: EXT_DISP_IN A B GND | A B GND EXT_DISP_OUT | A | PILOT_IN B GND | A B GND PILOT_OUT | A | DGPS_IN B GND | A | A B GND DGPS_OUT | LR_IN B GND | A | A | SEN1 B GND | B GND COM NC NO LR_OUT ALARM | A | SEN2 B GND | GND GND GND SHIELD | A | SEN3 B GND | SM BS COM SWITCHES | nearby labels: To transceiver | Bidirectional data ports | Termination jumpers | Sensor data inputs | Cable glands | OCR text follows (tesseract, unverified; 3/38 words >= 60, mean confidence 24) -->
iL
U
C
<!-- end of figure 1 -->

<!-- pdf page 44 | printed page 42 | header: Installation -->

               Junction box signal
 Data port                                 Description                     Function
               label

 Sensor 1      SEN1 A                      Sensor port 1 input A           Connect to data source, typically
                                                                           ships primary GNSS at 4800baud.
               SEN1 B                      Sensor port 1 input B           This port can be configured to
               SEN1 GND                    Sensor port 1 isolated ground   operate at either 4800 or 38400
                                                                           baud*.

 Sensor 2      SEN2 A                      Sensor port 2 input A           Connect to data source, typically
                                                                           gyro or heading. This port can be
               SEN2 B                      Sensor port 2 input B           configured to operate at either
               SEN2 GND                    Sensor port 2 isolated ground   4800 or 38400 baud*.

 Sensor 3      SEN3 A                      Sensor port 3 input A           Connect to data source, typically
                                                                           ROT or speed. This port can be
               SEN3 B                      Sensor port 3 input B           configured to operate at either
               SEN3 GND                    Sensor port 3 isolated ground   4800 or 38400 baud*.

 External      EXT_DISP_IN A               External display input A        Connect to the data output of an
 display                                                                   external display system, typically
               EXT_DISP_IN B               External display input B        an ECDIS. This port operates at
               EXT_DISP_IN GND             External display input ground   38400 baud.
                                           (isolated)

               EXT_DISP_OUT A              External display output A       Connect to the data input of an
                                                                           external display system, typically
               EXT_DISP_OUT B              External display output B       an ECDIS. This port operates at
               EXT_DISP_OUT GND            External display output         38400 baud.
                                           ground

 Pilot         PILOT_IN A                  External display input A        Connections for the pilot port.
                                                                           These connections duplicate the
               PILOT_IN B                  External display input B        pilot plug on the front panel of the
               PILOT_IN GND                External display input ground   transceiver and can be used to
                                           (isolated)                      relocate the pilot plug if required.

               PILOT_OUT A                 External display output A       If relocating the pilot plug note
               PILOT_OUT B                 External display output B       that AMP/Receptacle (Square
                                                                           Flanged (-1) or Free-Hanging
               PILOT_OUT GND               External display output         (-2)), Shell size 11, 9-pin, Std. Sex
                                           ground                          206486-1/2 or equivalent with the
                                                                           following terminations must be
                                                                           used.
                                                                           - TX A is connected to Pin 1
                                                                           - TX B is connected to Pin 4
                                                                           - RX A is connected to Pin 5
                                                                           - RX B is connected to Pin 6
                                                                           - Shield is connected to Pin 9

Table 4     Serial data port connections
*This setting relates to IEC61162-1 or IEC61162-2 operation.

<!-- pdf page 45 | printed page 43 | header: Installation -->

An example of connection to external display equipment is provided in Figure 45, and connections to other
equipment and sensors follow the same scheme. To determine the ‘A’ and ‘B’ signal lines on external
equipment use a digital volt meter to measure the signal line voltage referenced to ground. If the voltmeter
shows a negative voltage the ‘A’ signal line is being measured, a positive voltage indicates the ‘B’ signal line.

  EXT_DISP_IN         PILOT_IN         DGPS_IN         LR_IN           SEN1          SEN2           SEN3
  A    B GND      A       B GND    A      B GND    A     B GND     A     B GND   A     B GND   A      B GND

    A    B GND        A    B GND       A   B GND       A      B GND COM NC NO    GND GND GND       SM BS COM
   EXT_DISP_OUT        PILOT_OUT        DGPS_OUT           LR_OUT      ALARM        SHIELD          SWITCHES

EXT_DISP_IN                        PILOT_IN
A    B GND                    A        B GND

                                                                           EXT_DISP_IN A
                                                                           EXT_DISP_IN B

                                                                       EXT_DISP_OUT A
                                                                       EXT_DISP_OUT B
 A    B GND                        A    B GND
EXT_DISP_OUT                        PILOT_OUT

                             External display system.
                                           e.g. ECDIS

                             Transmit A
                             Transmit B

                             Receive A
                             Receive B

Connect shield if required

Figure 45 Example connection to external display equipment

Shielded cable should be used for data interface connections and the shield should be connected to the ground
at the 'talker' end of the connection. If the transceiver is being connected to a display system then the cable
shield should be connected to ground at the transceiver junction box as shown in Figure 46.

                              EXT_DISP_IN       PILOT_IN      DGPS_IN         LR_IN           SEN1           SEN2           SEN3
                              A+ B- GND       A+ B- GND     A+ B- GND    A+     B- GND   A+    B- GND   A+    B- GND   A+    B- GND

                               A+ B- GND       A+ B- GND     A+ B- GND    A+     B- GND COM NC NO        GND GND GND    BS SM GND
                               EXT_DISP_OUT     PILOT_OUT     DGPS_OUT         LR_OUT      ALARM            SHIELD       SWITCHES

                                               Connect cable shield to GND terminal

                                                  Do not connect shield at this end

Figure 46 Connecting data interface cable shields

<!-- figure 1 on pdf page 45 at 60,127-440,329 pt | caption: "Figure 45 Example connection to external display equipment" | text-layer labels: EXT_DISP_IN A B GND | A B GND EXT_DISP_OUT | A | PILOT_IN B GND | A B GND PILOT_OUT | EXT_DISP_IN A B GND | A B GND EXT_DISP_OUT | A | DGPS_IN B GND | A B GND DGPS_OUT | A | LR_IN B GND | A | A | SEN1 B GND | B GND COM NC NO LR_OUT ALARM | A | SEN2 B GND | GND GND GND SHIELD | A | SEN3 B GND | SM BS COM SWITCHES | PILOT_IN A B GND | EXT_DISP_IN A EXT_DISP_IN B | EXT_DISP_OUT A EXT_DISP_OUT B | A B GND PILOT_OUT | Connect shield if required | nearby labels: Receive A Receive B | OCR text follows (tesseract, unverified; 2/22 words >= 60, mean confidence 32) -->
99728
1
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 45 at 480,240-524,312 pt | caption: none | text-layer labels: none | nearby labels: External display system. e.g. ECDIS | Transmit A Transmit B | Receive A Receive B | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 45 at 151,417-425,736 pt | caption: "Figure 46 Connecting data interface cable shields" | text-layer labels: EXT_DISP_IN A+ B- GND | A+ B- GND EXT_DISP_OUT | PILOT_IN A+ B- GND | A+ B- GND PILOT_OUT | DGPS_IN A+ B- GND | A+ | A+ B- GND DGPS_OUT | LR_IN B- GND | A+ | A+ | SEN1 B- GND | A+ | B- GND COM NC NO LR_OUT ALARM | SEN2 B- GND | GND GND GND SHIELD | A+ | SEN3 B- GND | BS SM GND SWITCHES | Connect cable shield to GND terminal | Do not connect shield at this end | OCR text follows (tesseract, unverified; 8/40 words >= 60, mean confidence 33) -->
a
GND GND GND GND GND
com
X
<!-- end of figure 3 -->

<!-- pdf page 46 | printed page 44 | header: Installation -->

The junction box provides jumpers to select alternative line termination configurations for data input
connections from remote equipment. The line termination options are:
     ● None - no line termination, suitable for short cable runs less than 10m (as supplied).
     ● R           - 120 Ohm line termination, suitable for longer cable runs greater than 10m.
     ● RC          - AC 120 Ohm / 1uF termination. Not used.
Select the appropriate line termination option for each data input connection using the jumper adjacent to the data
input connection in the junction box. The jumper positions for each termination option are shown in Figure 47.

                         No line termination                120 Ohm line          120 Ohm / 1uF line
                               (default)                   termination (R)         termination (RC)

Figure 47 Line termination options

Along with data port connections the junction box also provides connections to the AIS transceiver alarm relay
contacts. The common and normally open alarm contacts are duplicates of the alarm relay connections
available at the power connector (see Table 5) whilst the normally closed contact is only provided at the junction
box. The alarm relay connections are described in Table 5. Use the alarm connections appropriate to the
vessels alarm system.

            Junction box alarm
                                               Function                                   Contact rating
            connection

            COM                                Alarm relay common connection
                                                                                          220V or 2A or 60W
            NC                                 Alarm relay normally closed connection     maximum
            NO                                 Alarm relay normally open connection

Table 5          Alarm relay connections

4.4.5       NMEA 0183 connection guidance
The NMEA 0183 outputs (TX signals) in this product are fully isolated from the vessel supply.
However it is possible to cause damage to these ports if a NMEA 0183 (IEC61162-2) data output
signal is connected to the vessel ground in your installation. This situation can occur when
connecting the transceiver data outputs to equipment with a ‘single ended’ input. A connection from
the data outputs to vessel ground will defeat the isolation and can lead to permanent damage to the
transceivers and connected equipment.
The EXT_DISP_OUT A and EXT_DISP_OUT B (or PILOT_OUT A and PILOT_OUT B) signals
should only be connected to the isolated data input of other equipment. Equipment that is compliant
with NMEA0 0183 or IEC61162-1/-2 will have a matching pair of input connections marked RX-A and
RX-B 0r RX+ and RX-. Some chart plotters do not have matching isolated inputs and may require
one signal to be connected to ground.
              Do not connect any of the transceiver data outputs signals to ground. If your
        !     equipment does not have isolating inputs then an isolating interface adapter is
              required to protect the transceiver and other equipment from damage.
We recommend the use of Actisense NBF-3 in applications that require additional isolation or
connection to display equipment with ‘single ended’ inputs.
If you are not sure about connecting your transceiver to other equipment please contact technical
support for advice

<!-- pdf page 47 | printed page 45 | header: Installation -->

                              TRANSCEIVER JUNCTION BOX

          EXT_DISP_IN            PILOT_IN            DGPS_IN             LR_IN            SEN1           SEN2            SEN3
          A    B GND         A       B GND       A      B GND        A     B GND      A     B GND    A     B GND    A      B GND

            A    B GND           A    B GND          A   B GND           A      B GND COM NC NO      GND GND GND        SM BS COM
           EXT_DISP_OUT           PILOT_OUT           DGPS_OUT               LR_OUT      ALARM          SHIELD           SWITCHES

                   EXT_DISP_OUT B

                   EXT_DISP_OUT A

Figure 48 Differential input connections
                         TRANSCEIVER JUNCTION BOX

         EXT_DISP_IN         PILOT_IN            DGPS_IN         LR_IN                SEN1          SEN2           SEN3
         A    B GND      A       B GND       A      B GND    A     B GND          A     B GND   A     B GND   A      B GND

           A    B GND        A    B GND          A   B GND       A      B GND COM NC NO         GND GND GND       SM BS COM
          EXT_DISP_OUT        PILOT_OUT           DGPS_OUT           LR_OUT      ALARM             SHIELD          SWITCHES

                       ECDIS, ECS OR
                      CHART PLOTTER

                    RX (B) /-VE

                    RX (A) /+VE

NMEA 0183 BUFFER
                          LAPTOP

LISTENER   TALKER

            EXT_DISP_OUT B                RX (B) /-VE   B /-VE   GND

            EXT_DISP_OUT A                RX (A) /+VE   A /+VE   RX

Figure 49 Single ended input connection

<!-- figure 1 on pdf page 47 at 69,108-428,293 pt | caption: "Figure 48 Differential input connections" | text-layer labels: EXT_DISP_IN A B GND | A | A B GND EXT_DISP_OUT | PILOT_IN B GND | A | A B GND PILOT_OUT | DGPS_IN B GND | LR_IN B GND | A | A B GND DGPS_OUT | A | A | SEN1 B GND | A | B GND COM NC NO LR_OUT ALARM | SEN2 B GND | A | GND GND GND SHIELD | SEN3 B GND | SM BS COM SWITCHES | EXT_DISP_OUT B | EXT_DISP_OUT A | nearby labels: TRANSCEIVER JUNCTION BOX | Figure 48 Differential input connections | OCR text follows (tesseract, unverified; 3/32 words >= 60, mean confidence 35) -->
A_B GI
oo
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 47 at 440,137-512,293 pt | caption: none | text-layer labels: none | nearby labels: ECDIS, ECS OR CHART PLOTTER | RX (B) /-VE | RX (A) /+VE | OCR: no legible text (0/2 words >= 60, mean confidence 22) -->
<!-- figure 3 on pdf page 47 at 67,353-296,533 pt | caption: "Figure 48 Differential input connections" | text-layer labels: EXT_DISP_IN A B GND | A | PILOT_IN B GND | A | DGPS_IN B GND | A | LR_IN B GND | A | SEN1 B GND | A | SEN2 B GND | A | SEN3 B GND | A B GND EXT_DISP_OUT | A B GND PILOT_OUT | A B GND DGPS_OUT | A | B GND COM NC NO LR_OUT ALARM | GND GND GND SHIELD | SM BS COM SWITCHES | EXT_DISP_OUT B | EXT_DISP_OUT A | nearby labels: Figure 48 Differential input connections | TRANSCEIVER JUNCTION BOX | RX (B) /-VE | RX (A) /+VE | Figure 49 Single ended input connection | OCR text follows (tesseract, unverified; 4/33 words >= 60, mean confidence 28) -->
da
3
oo
GND
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 47 at 442,372-509,533 pt | caption: none | text-layer labels: GND | RX | nearby labels: LAPTOP | B /-VE | A /+VE | OCR: no legible text (0/2 words >= 60, mean confidence 46) -->

<!-- pdf page 48 | printed page 46 | header: Installation -->

4.4.6     Power and alarm connections
Power is connected to the transceiver via the supplied four way power and alarm cable as shown in Figure 50.

                                          Power connection

Figure 50 Power connection

The power and alarm cable contains four wires which should be connected according to Table 6.

        Wire colour            Function                              Connect to

        Brown                  Power supply +                        12V or 24V DC power supply from
                                                                     ships emergency power source*

        Black                  Power supply -                        Power supply ground

        White                  Alarm relay normally open contact     Bridge alarm system

        Blue                   Alarm relay common contact            Bridge alarm system

Table 6        Power supply connections
*Connection to an emergency power source is an IMO requirement for SOLAS vessels.
The power supply current ratings and recommended fusing or circuit breaker currents are as follows:
     ● A 12VDC supply should be able to provide 4.0A and be fused at 8.0A.
     ● A 24VDC supply should be able to provide 2.0A and should be fused at 4.0A.
The alarm relay is rated to 220VDC or 2ADC or 60W maximum. The alarm connections provided at the power
connections are a duplicate of the those available via the junction box and described in section 4.4.

4.4.7     Grounding the transceiver
The transceiver is fully isolated from the vessels power supply by its internal power supply circuit. If a ground
connection is required for the shield of data connections then a connection must be made to the vessels
electrical ground. A grounding stud is provided on the rear of the transceiver chassis for this purpose as

<!-- figure 1 on pdf page 48 at 177,113-423,261 pt | caption: "Figure 50 Power connection" | text-layer labels: none | nearby labels: Power connection | OCR text follows (tesseract, unverified; 2/13 words >= 60, mean confidence 36) -->
XS
f
<!-- end of figure 1 -->

<!-- pdf page 49 | printed page 47 | header: Installation -->

indicated in Figure 51. Two M4 nuts and a shake proof washer are provided with the product fixings. A
grounding cable terminated in a suitable ring crimp should be clamped to the earth stud using the fixings
provided.

                                          Ground stud

Figure 51 Grounding the transceiver
            Do not connect the ground stud to the negative power supply line. This will defeat power supply
    !        isolation and may result in equipment damage.

4.4.8       PC data connection
A 9 way D-type connector is provided on the rear panel of the transceiver. This interface allows direct
connection to a PC RS232 interface and can be used for installation, diagnostics or external display
connection. The default configuration for this interface allows connection of an ECDIS or charting system and
duplicates the ‘External display’ port in the junction box.

                            PC data (RS232) connection

Figure 52 PC data (RS232) connection

              The RS232 port is galvanically isolated from the incoming power supply, however if connecting
        !     to a PC the use of an isolating RS232 to USB convertor is strongly recommended.

The pin allocation for the 9 way D-type socket on the rear panel of the transceiver is shown in Table 7

<!-- figure 1 on pdf page 49 at 184,113-430,261 pt | caption: "Figure 51 Grounding the transceiver" | text-layer labels: none | nearby labels: Ground stud | OCR text follows (tesseract, unverified; 2/27 words >= 60, mean confidence 30) -->
OS
KO)
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 49 at 177,434-423,583 pt | caption: "Figure 52 PC data (RS232) connection" | text-layer labels: none | nearby labels: PC data (RS232) connection | OCR text follows (tesseract, unverified; 2/17 words >= 60, mean confidence 37) -->
q
NO
<!-- end of figure 2 -->

<!-- pdf page 50 | printed page 48 | header: Installation -->

.

      Transceiver 9 Way
                            Signal                     Function
      D-type pin

      1                     No connection

      2                     RS232 Transmit             Connect to PC RS232 receive

      3                     RS232 Receive              Connect to PC RS232 transmit

      4                     No connection

      5                     RS232 Ground               Connect to PC RS232 ground

      6                     No connection

      7                     No connection

      8                     No connection

      9                     No connection

Table 7   Pin allocation for the 9 way D-type socket

<!-- pdf page 51 | printed page 49 | header: Installation -->

4.5 Configuring the transceiver
Once all connections have been made the transceiver can be powered and configured for operation. During
configuration information about the vessel on which the transceiver is installed is entered into the transceiver.
It is important this information is entered accurately as it will be broadcast to other AIS equipped vessels and
shore stations.
Once configuration is completed the installation record found at the rear of this manual should be completed
and retained on board the vessel.

4.5.1   Pre configuration checks
To proceed with configuration the following steps should already have been completed:
     ● The transceiver is fixed to the vessel
     ● VHF and GNSS antennas have been installed and connected to the transceiver
     ● The data cable has been connected between the transceiver and junction box
     ● Ships sensors and AIS enabled display equipment have been connected to the junction box
     ● Power has been connected to the transceiver and the transceiver is operational (the display is active).
The following configuration instructions assume the installer is familiar with the transceiver user interface,
details of which can be found in the Operation section of this manual.

4.5.2   Configure vessel identification information
The transceiver must be configured with information about the vessel on which it is installed prior to operation.
The following information is required:
     ● MMSI - Vessel MMSI number (Maritime Mobile Service Identity), this can usually be found on the
       ships VHF radio license and should be the same MMSI as used for the VHF / DSC radio.
     ● Name - Vessel Name (limited to 20 characters)
     ● Call sign - Vessel radio call sign (limited to 7 characters)
     ● IMO No. - Vessels IMO identification number (if applicable)
     ● Dimensions giving the location of the GNSS antenna connected to the AIS transceiver (Internal GNSS)
     ● Dimensions giving the location of the GNSS antenna connected to any external position source
       connected to the AIS transceiver
To enter the vessel identification information press the ‘Menu’ key and select the ‘Installation’ then ‘Set
identification’ option. You will be prompted to enter a password at this stage, the default password is ‘00000000’
(eight zeros). Refer to section 3.15 for more information on passwords and security. The vessels MMSI, Name,
Call sign and IMO number can be entered on the screen displayed after successful password entry.

4.5.3   Configuring the internal GNSS receiver
The internal GNSS receiver can be configured to operate in one of three modes:
     ● GLONASS and GPS – in this mode the position fix is derived from both the GLONASS and GPS
       network in parallel. This mode is the default setting and gives the best performance.
     ● GPS – in this mode only GPS satellites are used for the position fix.
     ● GLONASS – in this mode only GLONASS satellites are used for the position fix.
The operating mode can be selected from the ‘GNSS settings’ option in the ‘Installation’ menu.
To enter the GNSS antenna locations go back to the main menu and select the ‘Dimensions’ then ‘Internal’ or
'External’ option as appropriate. Dimensions for both the internal and external GNSS antennas must be entered
if an external GNSS is connected to the AIS transceiver. The antenna dimensions should be entered in metres
according to the diagram provided in Figure 53

<!-- pdf page 52 | printed page 50 | header: Installation -->

.

                                           Ref C           Antenna

                      Stern                                                                  Bow
                                   Ref B                             Ref A

                                                   Ref D

                      Ref A + Ref B = Length in metres          Ref C + Ref D = Beam in metres

Figure 53 Vessel dimensions measurement

4.5.4   Configure voyage related data
The transceiver must be configured with information about its voyage prior to operation. The following
information is required:
    ● Nav Status - Navigational status selected from the list below:
        ○ 0 - Under way using engine.
        ○ 1 - At anchor.
        ○ 2 - Not under command.
        ○ 3 - Restricted manoeuvrability.
        ○ 4 - Constrained by her draught.
        ○ 5 - Moored.
        ○ 6 - Aground.
        ○ 7 - Engaged in fishing.
        ○ 8 - Under way sailing.
        ○ 9 to 14 - reserved for future use.
        ○ 15 - not defined (default setting).
    ● Destination - Ships next destination port (limited to 20 characters).
    ● ETA - Estimated time / date of arrival at destination (using UTC time).
    ● Draught - Maximum present static draught to the nearest 1/10th of a metre.
    ● Ship type - select the most appropriate ship type from the list. Ship types are also shown in Table 8.
    ● Cargo type - if appropriate select a hazardous cargo type from the list. Cargo types are also shown in
      Table 9.
    ● Crew - Number of crew on board (optional).
To enter the vessel identification information press the ‘Menu’ key and select the ‘Voyage Data’ option. The
vessels Nav. status, Destination, ETA, Draught, Type and number of crew can then be entered.

<!-- figure 1 on pdf page 52 at 177,94-397,197 pt | caption: none | text-layer labels: Antenna | Ref C | Ref B | Ref A | Ref D | nearby labels: Stern | Bow | Ref A + Ref B = Length in metres | Ref C + Ref D = Beam in metres | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 53 | printed page 51 | header: Installation -->

                                                                                                 Type
  Vessel type
                                                                                                 code
  Reserved (do not use)                                                                           1[n]
  Wing in ground craft                                                                            2[n]
  Fishing                                                                                         30
  Towing                                                                                          31
  Towing and length of tow exceeds 200m or breadth exceeds 25m                                    32
  Engaged in dredging or underwater operations                                                    33
  Engaged in diving operations                                                                    34
  Engaged in military operations                                                                  35
  Sailing                                                                                         36
  Pleasure craft                                                                                  37
  (HSC) High speed craft                                                                          4[n]
  Pilot vessel                                                                                    50
  Search and rescue vessel                                                                        51
  Tug                                                                                             52
  Port tender                                                                                     53
  Vessel with anti-pollution facilities                                                           54
  Law enforcement vessel                                                                          55
  Spare - for local use                                                                           56
  Spare - for local use                                                                           57
  Medical transports (under the 1949 Geneva conventions and additional protocols)                 58
  Ships according to RR Resolution No. 18 (Mob-83) - Relating to the Procedure for Identifying    59
  and Announcing the Position of Ships and Aircraft of States Not Parties to an Armed Conflict
  Passenger ship                                                                                  6[n]
  Cargo ship                                                                                      7[n]
  Tanker                                                                                          8[n]
  Other type of ship                                                                              9[n]

Table 8     Vessel types and their corresponding vessel type codes

Cargo type

All ships of this type

Second digit
(where not predefined)
            0

  Carrying DG, HS, or MP, IMO hazard or pollutant category X    1
  Carrying DG, HS, or MP, IMO hazard or pollutant category Y    2
  Carrying DG, HS, or MP, IMO hazard or pollutant category Z    3
  Carrying DG, HS, or MP, IMO hazard or pollutant category OS   4
  Reserved (do not use)                                         5
  Reserved (do not use)                                         6
  Reserved (do not use)                                         7
  Reserved (do not use)                                         8
  No additional information                                     9

Table 9   Type codes for vessels carrying cargo

<!-- figure 1 on pdf page 53 at 469,521-531,708 pt | caption: none | text-layer labels: none | nearby labels: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 54 | printed page 52 | header: Installation -->

4.6 Changing the password
Following configuration of the transceiver the password should be changed from its default value of ‘00000000’.
Password change is carried out by selecting the main menu ‘Installation’ menu, then the ‘Change password’
submenu.
A prompt for the existing password will be shown, followed by entry of the new password then confirmation of
the new password before the new password is stored and active. The password should be recorded on the
installation record found in section 9.

4.7 Confirming correct operation
Following entry of the vessel identification and voyage related information the transceiver will commence
normal operation. To complete the installation correct operation should be verified as follows:
    1. Exit the menu system and return to the main operating screens. Press the 'Screen' key until the ‘Own
       dynamic data’ screen is displayed.
    2. Check that the displayed position, course, speed and heading are correct by comparing to the display
       associated to the connected position source and other data sources.
    3. Check that the status icon display shows ‘OK’ and that the ‘TX’ icon flashes periodically.
    4. If the vessel is in an area where other AIS equipped vessels are present press the ‘Screen’ key until
       the ‘Target list' screen is displayed. Check that data from other AIS equipped vessels is displayed.
    5. Carry out a communication test with another Class A AIS equipped vessel. Go to the Maintenance
       menu, select the communication test option then press the 'Send' button to run the test. The result will
       be reported on the screen.
The transceiver is now operational and should remain powered unless authorised by the local maritime
authority. The installation record at the rear of this manual should be completed and left on board the vessel.

4.8 Regional area settings
The transceiver can be manually programmed with regional area settings. These settings control the AIS radio
channel and transmission settings within a predefined area. Regional settings can also be remotely configured
by the local maritime authority via transmissions from an AIS base station. Manual entry of regional area
settings should only be carried out if required by the local maritime authority.
The transceiver can store eight regional area settings including both remote and manual entries.

4.8.1   Creating a new regional area setting
To enter a new regional area setting press the ‘Menu' key and select the ‘Installation' and then the ‘Regional
areas’ sub-menu. The display now shows a list of the current regional area settings as shown in Figure 54.

                                                                      INT
                                    13:20:47    OK                    GPS

                                   REGIONAL AREA SET TINGS:
                                     Lat NE Long NE   Lat SW     Long SW
                                   > --°--N ---°--E   --°--N     ---°--E

                                               New             Edit

Figure 54 Regional areas list screen

To create the new area setting press the ‘New' function key and the edit screen shown in Figure 55 will be
displayed.

<!-- figure 1 on pdf page 54 at 196,552-397,669 pt | caption: "Figure 54 Regional areas list screen" | text-layer labels: 13:20:47 | INT GPS | OK | New | Long SW ---°--E | Edit | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 55 | printed page 53 | header: Installation -->

                                                                           INT
                                     13:20:47     OK                       GPS

                                    EDIT REGIONAL AREA:
                                    In Use:         No
                                    Time of In Use: --:--:--
                                    Info Source:    Not Available
                                    Channel A:      2087
                                    Channel B:      2088
                                    Channel A BW:   Default
                                                Back

Figure 55 Regional area editing screen

     1. The scroll wheel can now be used to scroll to the field to edit.
     2. Select the field by pushing the scroll wheel or pressing the 'Edit’ function key.
     3. Enter a value, or select from a list of possible values using the scroll wheel.
     4. Press the ‘OK’ or ‘Cancel' function key to confirm or cancel the entry.
     5. Repeat the process 1 - 4 for each field to be edited.
     6. Press the ‘Back/Save’ function key to save the regional area setting and return to the area settings list
     7. You will be prompted to confirm storage of the regional area setting with the display shown in Figure 56.
     8. After confirmation of the regional settings the settings are stored and may take effect immediately de-
        pending on the location of the vessel.

                                                                           INT
                                     13:20:47    OK                        GPS

                                    SAVE REGIONAL AREA:
                                    Are you sure you want to save the
                                    edited Regional Area?

                                    Area settings may take effec t
                                    immediately!

                                                No                   Yes

Figure 56 Regional area settings confirmation screen

4.8.2   Editing an existing regional area setting
To edit an existing regional area setting press the ‘Menu' key and select the ‘Installation' and then the ‘Regional
areas’ sub-menu. The display now shows a list of the current regional area settings as shown in Figure 54. Use
the scroll wheel to scroll to and select the regional area setting entry to be edited, then follow the instructions
for creating a new regional area setting in section 4.8.1.

<!-- figure 1 on pdf page 55 at 194,91-394,206 pt | caption: "Figure 55 Regional area editing screen" | text-layer labels: 13:20:47 | INT GPS | OK | Back | OCR: no legible text (0/1 words >= 60, mean confidence 45) -->
<!-- figure 2 on pdf page 55 at 191,386-392,499 pt | caption: "Figure 56 Regional area settings confirmation screen" | text-layer labels: 13:20:47 | INT GPS | OK | SAVE REGIONAL AREA: | No | Yes | OCR: no legible text (0/2 words >= 60, mean confidence 25) -->

<!-- pdf page 56 | printed page 54 | header: Installation -->

4.9 Inland AIS
The transceiver supports both Class A (high seas / SOLAS) AIS operation and Inland AIS operation. Switching
between Class A and Inland AIS is possible via the menu system and this setting should be made at installation
depending on the environment the vessel operates in. Additional vessel and voyage information is required for
transmission when operating in Inland AIS mode and this should be configured as described in the following
sections.

               The transceiver stores Class A (high seas) and Inland AIS vessel and voyage data separately
        !      so two independent configurations are required, one for Class A and one for Inland AIS. If the
               transceiver is being installed on board an Inland vessel then the standard vessel and voyage
               data configuration should be carried out prior to the additional Inland configuration described
               below.

4.9.1       Switching between ‘Class A’ and ‘Inland AIS’ modes
To switch between operating modes press the ‘Menu’ key and select the ‘Installation' sub menu followed by the
‘Inland AIS’ then the ‘Inland configuration’ option. Finally set the ‘Inland AIS’ setting to ‘Enabled’ or ‘Disabled’
before saving the setting. When the transceiver is configured to operate in Inland AIS mode the ‘IL’ icon is
shown permanently in the status bar.

4.9.2       Entering Inland vessel identification settings
Additional vessel identification information is required for Inland operation along with some changes to the
standard AIS configuration. The following additional information must be entered into the AIS transceiver:
     ● The vessels ENI (unique European Identifier) - this is an 8 digit number allocated to the vessel.
     ● The ship type as an ERI code (4 digits) selected from the table provided in section 8.
     ● A quality setting for the speed, course and heading data sources connected to the AIS is required.
       The quality setting can be ‘high’ or ‘low’ for each data source. The low setting should be used unless
       a type approved sensor (e.g., a gyro providing heading information) is connected to the AIS
       transceiver.
The additional identification information can be entered via the main menu. Press the ‘Menu' key then navigate
through the ‘Installation’, 'Inland AIS’ submenus to select the ‘Inland vessel data’ menu.
The following standard AIS vessel identification information must be updated for Inland AIS:
     ● The IMO number should be set to ‘0’ or ‘00000000’ for an Inland vessel.
     ● The standard AIS ship type should be set to the most applicable ship type - refer to the ship type table
       in section 9.
These updates are all made using the process described in section 4.5.

4.9.3       Entering Inland vessel dimensions
Inland vessel dimensions are entered using the ‘Installation’ then ‘Dimension’ menu option whilst the
transceiver is in Inland mode. The Inland vessel dimension entry screen allows both the main vessel and
additional barge extension dimensions to be entered.
Referring to Figure 57 the following dimensions can be configured. Dimensions marked with an asterisk must
be provided.

<!-- pdf page 57 | printed page 55 | header: Installation -->

  EC                   BI

               CI                     Antenna
                    Stern
  BS                                             Bow

  ED

              EB                      LS                                     EA

Figure 57 Inland vessel dimensions

  Dimension            Description

  LS                   Total length of the vessel to the nearest 10cm*

  BS                   Total beam of the vessel to the nearest 10cm*

  BI                   Distance from the stern to the internal GNSS antenna to the nearest 10cm*

  CI                   Distance from the port side to the internal GNSS antenna to the nearest 10cm*

  BE                   Distance from the stern to the external GNSS antenna to the nearest 10cm (only
                       required if an external GNSS source is connected to the transceiver)

  CE                   Distance from the port side to the external GNSS antenna to the nearest 10cm
                       (only required if an external GNSS source is connected to the transceiver)

  EA                   Bow combination extension (additional length of barges at bow) to the nearest
                       10cm

  EB                   Stern combination extension (additional length of barges at stern) to the nearest
                       10cm

  EC                   Port combination extension (additional beam of barges on port side) to the nearest
                       10cm

  ED                   Starboard combination extension (additional beam of barges on starboard side) to
                       the nearest 10cm

Table 10   Inland vessel dimensions

<!-- figure 1 on pdf page 57 at 79,91-507,312 pt | caption: "Figure 57 Inland vessel dimensions" | text-layer labels: BI | Antenna | CI | Stern | Bow | nearby labels: EC | BS | ED | EB | LS | EA | Figure 57 Inland vessel dimensions | OCR text follows (tesseract, unverified; 5/16 words >= 60, mean confidence 45) -->
A
v
A
i!
lt
<!-- end of figure 1 -->

<!-- pdf page 58 | printed page 56 | header: Installation -->

4.9.4       Entering Inland vessel voyage settings
Additional voyage related information is required for Inland operation along with some changes to the standard
AIS configuration. The following additional information must be entered into the AIS transceiver:
     ● The vessels load status as ‘Loaded’, ‘Unloaded’ or ‘Unavailable’ if not relevant to the vessel type.
     ● The number of blue cones or blue flag status for the cargo (1, 2 or 3 blue cones, or blue flag).
     ● The static draught of the vessel to the nearest centimetre.
     ● The number of crew, passengers and other shipboard personnel.
     ● The number of assisting tugboats (from 0 to 6).
The additional identification information can be entered via the main menu. Press the ‘Menu' key then select
the ‘Voyage data’ sub-menu. When the AIS transceiver is operating in Inland AIS mode the voyage data entry
screen will be extended to allow input of the additional information described above.
The following standard AIS voyage information must be updated for Inland AIS:
     ● Destination
The voyage destination should be entered using UN terminal location codes and ERI terminal codes where
possible.

4.9.5       Blue sign switch
When operating in Inland mode it is possible to connect a ‘blue sign’ switch to the AIS transceiver.
Settings for the blue sign switch are available via the main menu by selecting the ‘Installation’ option followed
by the 'Inland configuration’ sub menu.
Select the ‘Blue sign settings’ option to set up the blue sign switch. The switch can be set to ‘Available’ if a blue
sign switch is connected or 'Unavailable’ if no switch is connected.
The external switch should be of a latching single pole type and is connected to the ‘Switches’ terminals of the
junction box as shown in Figure 58. When the connected switch is made (short circuit) the blue sign status will
be set and transmitted accordingly in Inland AIS position reports.

        !      Do not connect a voltage source to the blue sign switch connections.

                     EXT_DISP_IN         PILOT_IN         DGPS_IN         LR_IN           SEN1          SEN2           SEN3
                     A    B GND      A       B GND    A      B GND    A     B GND     A     B GND   A     B GND   A      B GND

                       A    B GND        A    B GND       A   B GND       A      B GND COM NC NO    GND GND GND       SM BS COM
                      EXT_DISP_OUT        PILOT_OUT        DGPS_OUT           LR_OUT      ALARM        SHIELD          SWITCHES

                                                                                                                                  Blue sign switch

Figure 58 Blue sign switch connection

4.9.6       Alarm masking
Inland AIS installations do not typically include connection of external GNSS, Heading or Rate of Turn sensors
to the transceiver. The system alarms associated with these sensors can be disabled in Inland mode through
the 'Installation', 'Inland AIS', 'Alarm Masking' screen.

<!-- figure 1 on pdf page 58 at 98,487-500,655 pt | caption: "Figure 58 Blue sign switch connection" | text-layer labels: EXT_DISP_IN A B GND | A B GND EXT_DISP_OUT | A | PILOT_IN B GND | A B GND PILOT_OUT | A | DGPS_IN B GND | A B GND DGPS_OUT | LR_IN B GND | A | A | A | SEN1 B GND | B GND COM NC NO LR_OUT ALARM | A | SEN2 B GND | GND GND GND SHIELD | A | SEN3 B GND | SM BS COM SWITCHES | nearby labels: Blue sign switch | OCR text follows (tesseract, unverified; 3/39 words >= 60, mean confidence 23) -->
_A_B GND A
<!-- end of figure 1 -->

<!-- pdf page 59 | printed page 57 | header: Technical Specifications -->

5      Technical Specifications

5.1 Applicable equipment standards

 IEC61993-2 Edi-        Class A shipborne equipment of the universal automatic identification system (AIS)
 tion 2 (2012)          – Operational and performance requirements, methods of test and required test
                        results

 IEC60945 (2002)        Maritime navigation and radio communication equipment and systems –
                        General requirements – Methods of testing and required test results

 IEC61162-1(2010)       Maritime navigation and radio communication equipment and systems –
                        Digital interfaces - Single talker and multiple listeners

 IEC61162-2 (1998)      Maritime navigation and radio communication equipment and systems –
                        Digital interfaces - Single talker and multiple listeners, high speed transmission

 ITU-R M.1371-5         Technical characteristics for an automatic identification system using time division
                        multiple access in the VHF maritime mobile band

 IEC61108-1(2003)       Global Navigation Satellite Systems (GNSS) –
                        Part 1: Global positioning system (GPS) - Receiver equipment - Performance stan-
                        dards, methods of testing and required test results

 CCNR VTT 1.2           Central commission for Navigation on the Rhine, Inland AIS Equipment
 (2013)                 - Vessel Tracking and Tracing Standard for Inland Navigation

5.2 Physical

 Transceiver dimensions       195mm x 105mm x 157mm (WxHxD, see 7.1 for drawing)

 Transceiver weight           1.5kg

 Junction box dimensions      178mm x 76mm x 52mm (see 7.2 for drawing)

 Junction box weight          0.35kg

 Compass safe distance        300mm (Transceiver)

5.3 Environmental

 Operating temperature range          -15°C to +55°C

 Maximum operating humidity           90% at +40°C, non-condensing

 Water ingress rating                 IP52

5.4 Electrical

    Supply voltage                             12 to 24V DC (absolute min 10.8V, absolute max 31.2 V)

    Power consumption                          < 12W

    Current consumption @12 VDC supply         0.9A typical, 4.0A peak

    Current consumption @24 VDC supply         0.5A typical, 2.0A peak

<!-- figure 1 on pdf page 59 at 480,132-538,384 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 59 at 244,559-538,624 pt | caption: none | text-layer labels: none | nearby labels: -15 ° C to +55 ° C | 90% at +40 ° C, non-condensing | IP52 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 59 at 136,660-253,744 pt | caption: none | text-layer labels: none | nearby labels: < 12W | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 59 at 368,660-535,744 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 60 | printed page 58 | header: Technical Specifications -->

5.5 Display and user interface

 Display                 248 x 128 pixel monochrome LCD with adjustable backlight

 Keypad                  Two function keys and two menu keys with adjustable backlight

 Rotary control          Encoder with push function and adjustable backlight

 Sounder                 2.4kHz buzzer

5.6 Internal GNSS (dual mode GNSS receiver variants)

 Receiver channels          32 channels GPS and GLONASS operating modes

 Time to first fix          Typically 30 seconds

 Frequency                  L1 GPS band, 1575.42MHz and L1 GLONASS band 1597.1 - 1609.5MHz

 Accuracy                   2.5m CEP / 5.0m SEP without differential correction
                            2.0m CEP / 3.0m SEP with SBAS or RTCM DGPS correction

 Antenna requirement        Active antenna (5V bias) with gain >15dB

5.7 Internal GNSS (GPS only variants)

 Receiver channels          16 channels

 Time to first fix          Typically 36 seconds

 Frequency                  L1 band, 1575.42MHz

 Accuracy                   2.5m CEP / 5.0m SEP without differential correction
                            2.0m CEP / 3.0m SEP with SBAS or RTCM DGPS correction

 Antenna requirement        Active antenna (5V bias) with gain >15dB

5.8 TDMA transmitter

Frequency range              156.025MHz to 162.025MHz

Channel bandwidth            25kHz

Output power                 1W or 12.5W (automatic selection)

Data transmission rate       9600 bits/s

Modulation mode              25kHz GMSK

5.9 TDMA receivers

 Number of receivers                  2

 Frequency range                      156.025MHz to 162.025MHz

 Channel bandwidth                    25kHz

 Sensitivity                          <-107dBm for 20% PER

<!-- figure 1 on pdf page 60 at 103,94-155,178 pt | caption: none | text-layer labels: none | nearby labels: Display | Keypad | Rotary control | Sounder | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 60 at 232,94-538,178 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 60 at 215,518-538,621 pt | caption: none | text-layer labels: none | nearby labels: 156.025MHz to 162.025MHz | 25kHz | 1W or 12.5W (automatic selection) | 9600 bits/s | 25kHz GMSK | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 60 at 115,657-215,741 pt | caption: none | text-layer labels: none | nearby labels: 2 | 25kHz | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 60 at 234,657-538,741 pt | caption: none | text-layer labels: none | nearby labels: 2 | 156.025MHz to 162.025MHz | 25kHz | <-107dBm for 20% PER | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 61 | printed page 59 | header: Technical Specifications -->

 Modulation mode                      25kHz GMSK

 Adjacent channel selectivity         70dB

 Spurious response rejection          70dB

5.10 DSC receiver

 Number of receivers                  1

 Frequency                            156.525MHz (Channel 70)

 Channel bandwidth                    25kHz

 Sensitivity                          -107dBm @ BER <10-2

 Modulation mode                      25kHz AFSK

 Adjacent channel selectivity         70dB

 Spurious response rejection          70dB

5.11 RF connections

 VHF antenna connection         SO-239 / UHF

 VHF port impedance             50 Ohms

 GNSS antenna connection        TNC female

 GNSS port impedance            50 Ohms

<!-- figure 1 on pdf page 61 at 55,70-538,134 pt | caption: none | text-layer labels: Modulation mode | 25kHz GMSK | Adjacent channel selectivity | 70dB | Spurious response rejection | 70dB | nearby labels: 5.10 DSC receiver | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 61 at 115,168-215,312 pt | caption: none | text-layer labels: none | nearby labels: 1 | 25kHz | 70dB | 70dB | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 61 at 234,168-538,312 pt | caption: none | text-layer labels: none | nearby labels: 1 | 156.525MHz (Channel 70) | 25kHz | -107dBm @ BER <10 -2 | 25kHz AFSK | 70dB | 70dB | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 61 at 237,348-538,432 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 62 | printed page 60 | header: Technical Specifications -->

5.12 Data interfaces

 Sensor data input ports

 Number of ports      3

 Standard             IEC61162-1

 Baud rate            4800 baud

 Port impedance       54k Ohms

 Bidirectional data ports (including pilot port)

 Number of ports      4

 Standard             IEC61162-1 / -2

 Baud rate            4800 or 38400 baud (default)

 Port impedance       54K Ohms

 Differential correction port

 Standard             ITU 823-2 / RTCM SC-104

 Baud rate            4800 baud

 Port impedance       54K Ohms

 RS232 port

 Standard             IEC61162-1 / -2 over RS232

 Baud rate            38400 baud

 Port impedance       5K Ohms

 Blue sign port

 Port impedance       10K Ohm

 Silent mode port

 Port impedance       10K Ohm

5.13 Power and data connector information

 Power connector                LTW                  Mating half   LTW
                                BSD-04PMMS-SC7001                  BSD-04BFFM-SL6A02

 Pilot plug connector           TYCO                 Mating half   TYCO
                                206486-2                           206485-1

 50 way data connector          Harting              Mating half   Harting
                                09665526612                        09670505615

 RS232 connector                Harting              Mating half   Harting
                                09661526612                        09670095615

<!-- pdf page 63 | printed page 61 | header: Technical reference -->

6    Technical reference

6.1 Interface sentences
The IEC61162 sentences accepted by and output by the transceiver serial data ports are listed in Table 11
below.

      Data port             Input sentences                       Output sentences

      Sensor 1              DTM, GBS, GGA, GLL, GNS, HDT,         N/A
      Sensor 2              RMC, ROT, THS, VBW, VTG,
      Sensor 3

      External display      ABM, ACA, ACK, AIR, BBM, DTM,         ABK, ACA, ALR, EPV, LR1, LR2,
      Pilot                 EPV, GBS, GGA, GLL, GNS, HDT,         LR3, LRF, LRI, TRL, TXT, SSD,
      Long range            LRF, LRI, RMC, ROT, SSD, VBW,         VDM, VDO, VER, VSD,
                            VSD, VTG, SPW, THS

      DGPS                  RTCM SC-104 binary format             RTCM SC-104 binary format

      RS232                 ABM, ACA, ACK, AIR, BBM, DTM,         ABK, ACA, ALR, EPV, LR1, LR2,
                            EPV, GBS, GGA, GLL, GNS, HDT,         LR3, LRF, LRI, TXT, VDM, VDO
                            LRF, LRI, RMC, ROT, SSD, THS,
                            VBW, VSD, VTG,

Table 11   IEC61162 sentences input and output

<!-- pdf page 64 | printed page 62 | header: Technical reference -->

6.2 Transmission intervals
The IEC61162 sentences are in general output in response to a specific event, such as initiation of a binary
message via the user interface. Certain messages are output over the ports at regular transmission intervals.
Table 12 lists each sentence type and the transmission interval.

Output sentence
                  Transmission interval
type

VDO               once a second

ALR (inactive)    once a minute

ALR (active)      once every thirty seconds

Comments

Own vessel VDL reports. When a
report is not generated by the
transceiver a ‘dummy’ VDO is gen-
erated in its place.

An ALR sentence for each internal
alarm is output as a single block
once every minute whilst all alarms
are inactive

Once an alarm becomes active the
transmission interval switches to
once every thirty seconds. The
active alarm is not reported as part
of the block of inactive alarms
during this period.

       ABK, ACA, LR1,        Only transmitted when specifically
       LR2, LR3, LRF,        initiated by an external event
       LRI, TXT,
       VDM,RTCM

Table 12   IEC61162 transmission interval for periodic sentences

6.3 Sensor data input port
The sensor data input port schematic is shown in Figure 59. The optional 120 Ohm termination is selectable
via a jumper in the junction box and should be fitted in the ‘R’ position when long cables connecting to the
data source are required - see section 4.4.4. Each sensor data input port is isolated from other data port
inputs and from the transceiver’s internal power supply.

             In junction box
         B                     Input B
             Jumper
Data input
   port      120 Ohms
                               Input GND
         A                     Input A
       GND

Figure 59 Input port schematic

Isolated
supply +

              To UART

   Isolated
   supply -

A logical low input is defined as: A-B < -0.2V.
A logical high input is defined as: A-B > +0.2V.
The input impedance is approximately 54 kOhms without the junction box jumper fitted, and 120 Ohms with
the jumper fitted.

<!-- figure 1 on pdf page 64 at 203,542-492,640 pt | caption: "Figure 59 Input port schematic" | text-layer labels: none | nearby labels: Isolated supply + | Input B | To UART | Input GND Input A | Isolated supply - | OCR text follows (tesseract, unverified; 7/14 words >= 60, mean confidence 58) -->
3V3
GND
2 COMPARATOR
GND
Lf DK?
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 64 at 96,571-175,624 pt | caption: none | text-layer labels: In junction box | Jumper | 120 Ohms | nearby labels: B | Data input port | A | Input B | Input GND Input A | GND | OCR: no legible text (0/3 words >= 60, mean confidence 26) -->

<!-- pdf page 65 | printed page 63 | header: Technical reference -->

6.4 Bi-directional data ports
The input circuitry of the bi-directional data ports is identical to the input circuitry for the sensor data input
ports described in the preceding section. The output circuitry consists of a differential line driver IC (Texas
Instruments AM26LV31E) and is shown in Figure 60.

                                                                           220 Ohms
                                                                10 Ohms    @100MHz
                                                                                       B

                         From UART
                                                                                        Data output port
                                                                                       A

                                                                10 Ohms    220 Ohms
                                                                           @100MHz

                                                                                      GND
                                                                100 Ohms

                                     GND

Figure 60 Data output port schematic

              Each bi-directional data port input is isolated from other data port inputs and from the
              transceivers internal power supply. The bi-directional data port outputs are not isolated from
        !     each other or the transceivers internal power supply. The transceivers internal power supply is
              fully isolated from the external supply.

6.5 Output drive capability of bi-directional ports
Bi-directional ports can supply an output current of up to 30mA. The output voltages are 0 (low) and 3.3V
(high). Effective load resistance should be in excess of 100 Ohms.

6.6 DGPS port
The DPGS correction port is intended for connection to a DGPS beacon receiver. The port has the same
physical characteristics as the bi-directional data ports as described in the preceding sections. If connection of
a beacon receiver is not required this port can be re-configured as an additional bi-directional port to
IEC61162-2. See section 3.16 for port configuration options.

6.7 RS232 port
The RS232 port carries IEC61162 data via RS232 and is intended for connection to a PC during installation
and service. The port can also be used to connect to PC based charting applications for display of AIS data.

6.8 Input data sentence formats
All data input is via IEC61162 / NMEA 0183 sentences. The sentences used by the AIS transceiver are
documented in the subsequent sections. The sentence structure tables describe each field in the sentence
starting from the left most field, (field 1), after the sentence identifier. All sentences are terminated with the
IEC61162 checksum shown as ‘*hh’. For details of the checksum calculation please refer to IEC61162-1.

6.8.1       ABM - Addressed binary and safety related message
This sentence allows external applications to transmit binary and safety messages using the AIS transceiver

<!-- figure 1 on pdf page 65 at 191,158-399,202 pt | caption: none | text-layer labels: 10 Ohms | nearby labels: 220 Ohms @100MHz | From UART | B | A | 10 Ohms | 100 Ohms | 220 Ohms @100MHz | GND | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 66 | printed page 64 | header: Technical reference -->

via AIS messages 6 and 12.

 !--ABM,x,x,x,xxxxxxxxx,x,x.x,s--s,x*hh<CR><LF>

 Field                       Description
 number

 1          x=               Total number of sentences needed to transfer the message

 2          x=               Sentence number

 3          x=               Sequential Message identifier

 4          xxxxxxxxx =      The MMSI of destination AIS transceiver for the ITU-R M.1371 message

 5          x=               AIS channel for broadcast of the radio message

 6          x.x =            ITU-R M.1371 message ID

 7          s--s =           Encapsulated data

 8          x=               Number of fill-bits, 0-5

6.8.2   ACA - AIS regional channel assignment message
This sentence is used to both enter and obtain channel management information.

  $--ACA,x,llll.ll,a,yyyyy.yy,a,llll.ll,a,yyyyy.yy,a,x,xxxx,x,xxxx,x,x,x,a,x,hhmmss.ss*hh<CR><LF>

 Field                       Description
 number

 1          x=               Sequence Number, 0 to 9

 2          llll.ll,a =      Region Northeast corner latitude - N/S

 3          yyyyy.yy,a =     Region Northeast corner longitude - E/W

 4          llll.ll,a =      Region Southwest corner latitude - N/S

 5          yyyyy.yy,a =     Region Southwest corner longitude - E/W

 6          x=               Transition Zone Size

 7          xxxx =           Channel A

 8          x=               Channel A bandwidth

 9          xxxx =           Channel B

 10         x=               Channel B bandwidth

 11         x=               Tx/Rx mode control

 12         x=               Power level control

 13         a=               Information source

 14         x=               In-Use Flag

 15         hhmmss.ss =      Time of “in-use” change

<!-- figure 1 on pdf page 66 at 273,91-538,307 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 66 at 134,115-184,307 pt | caption: none | text-layer labels: none | nearby labels: x = | x = | x = | xxxxxxxxx = | x = | x.x = | s--s = | x = | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 67 | printed page 65 | header: Technical reference -->

6.8.3   ACK - Acknowledge alarm
This sentence is used to acknowledge an alarm condition reported by the transceiver.

 $--ACK,xxx,*hh<CR><LF>

 Field                       Description
 number

 1          xxx =            Identification number of the alarm source to be acknowledged.

6.8.4   AIR - AIS Interrogation request
This sentence supports ITU-R M.1371 message 15. It provides external applications with the means to initiate
requests for specific ITU-R M.1371 messages from remote AIS stations.

 $--AIR,xxxxxxxxx,x.x,x,x.x,x,xxxxxxxxx,x.x,x*hh<CR><LF>

 Field                       Description
 number

 1          xxxxxxxxx =      MMSI of interrogated station-1

 2          x.x =            ITU-R M.1371 message requested from station-1

 3          x=               Message sub-section (Reserved for future use)

 4          x.x =            Number of second message from station-1

 5          x=               Message sub-section (Reserved for future use)

 6          xxxxxxxxx =      MMSI of interrogated station-2

 7          x.x =            Number of message requested from station-2

 8          x=               Message sub-section (Reserved for future use)

6.8.5   BBM -Binary broadcast message
This sentence allows generation of ITU-R M.1371 binary broadcast messages (message 8) or broadcast
safety related messages (message 14). The content of the message is defined by the application.

 !--BBM,x,x,x,x,x.x,s--s,x*hh<CR><LF>

 Field                       Description
 number

 1          x=               Total number of sentences needed to transfer the message, 1 to 9

 2          x=               Sentence number, 1 to 9

 3          x=               Sequential message identifier, 0 to 9

 4          x=               AIS channel for broadcast of the radio message

 5          x.x =            ITU-R M.1371 message ID, 8 or 14

 6          s--s =           Encapsulated data

 7          x=               Number of fill-bits, 0 to 5

<!-- figure 1 on pdf page 67 at 55,110-538,187 pt | caption: none | text-layer labels: $--ACK,xxx,*hh<CR><LF> | Field number | 1 | Description | xxx = | nearby labels: 6.8.4 | AIR - AIS Interrogation request | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 67 at 327,247-538,463 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 67 at 134,271-184,463 pt | caption: none | text-layer labels: none | nearby labels: xxxxxxxxx = | x.x = | x = | x.x = | x = | xxxxxxxxx = | x.x = | x = | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 68 | printed page 66 | header: Technical reference -->

6.8.6   DTM - Datum reference
Logical geodetic datum and datum offsets from a reference datum.

 $--DTM,ccc,a,x.x,a,x.x,a, x.x,ccc*hh<CR><LF>

 Field                         Description
 number

 1           ccc =             Local datum

 2           a=                Local datum subdivision code - NOT USED

 3           x.x, a =          Lat offset, min, N/S - NOT USED

 5           x.x,a =           Longitude offset, min, E/W - NOT USED

 7           x.x =             Altitude offset, (meter) - NOT USED

 8           ccc =             Reference datum

Possible datum and reference datum values are:
     ● WGS84 = W84
     ● WGS72 = W72
     ● SGS85 = S85
     ● PE90 = P90
     ● User defined =999 (only available for “Local datum”)
     ● IHO datum code ( „ -„- „ -„- -„- )

<!-- figure 1 on pdf page 68 at 244,110-538,285 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 69 | printed page 67 | header: Technical reference -->

6.8.7    EPV - Command or report equipment property value
This sentence can be used to set or query specific transceiver settings as listed in the table below the
sentence definition.

  $--EPV,x,xxxxxxxxx,xxxx.xxxx*hh <CR><LF>

  Field                          Description
  number

  1             x                Sentence status flag
                                 C = Command
                                 R = Response

  2             xx               Destination equipment type. The destination equipment field identifies the
                                 device type for which the sentence is targeted. The destination equipment
                                 field is the talker identifier mnemonic of the equipment for which the sen-
                                 tence is valid.

                                 Set to AI for AIS.

  3             xxxxxxxxx        Unique identifier. The unique identifier identifies the same equipment irre-
                                 spective of command versus response. For commands it identifies the
                                 equipment intended to receive the command. For responses it identifies the
                                 equipment that actually received the command. Under normal conditions the
                                 response will be received from the equipment for which the command was
                                 intended. Equipment should only send one or more response sentences in
                                 response to command sentences received and should not use response
                                 sentences for general reporting. For AIS Class A the unique identifier is the
                                 MMSI. The unique identifier may be null.

  4             xxxx             Property identifier for property to be set. See table below.

  5             xxxx             Value of property to be set. See table below.

   Property identi-         property meaning                                Value range
        fier

        10 to100       Reserved

          101          Sensor 1 baud                  4 800, 9 600, 14 400, 19 200, 38 400

          102          Sensor 2 baud                  4 800, 9 600, 14 400, 19 200, 38 400

          103          Sensor 3 baud                  4 800, 9 600, 14 400, 19 200, 38 400

          104          Long-range baud                4 800, 9 600, 14 400, 19 200, 38 400

          105          DGNSS baud                     4 800, 9 600, 14 400, 19 200, 38 400

          106          MMSI                           000000000, 200000000 ... 799999999, 982000000 ...
                                                      987999999

          107          IMO number                     0000000 ... 9999999

          108          Long-range interface           “A” = automatic
                       configuration
                                                      “M” = manual

<!-- pdf page 70 | printed page 68 | header: Technical reference -->

         109          Long-range AIS broad-      Valid channel according to ITU-R M.1084-5. See 8.3
                      cast channel 1
                                                 Default value 0 indicates no transmission of message 27

         110          Long-range AIS broad-      Valid channel according to ITU-R M.1084-5. See 8.3
                      cast channel 2
                                                 Default value 0 indicates no transmission of message 27

         111          Change administrator       New administrator password
                      password

         112          Change user password       New user password

         113          AIS-SART test mode         0 = normal mode
                                                 1 = display and output AIS-SART in test mode

   All other values   Reserved

Example:

A practical example is an ECDIS setting the baud rate for the Port1 of an AIS transponder. The ECDIS would
send the following command (MMSI of the AIS is 503123450):
$EIEPV,C,AI,503123450,101,38400*hh
The AIS would send the following response
$AIEPV,R,AI503123450,101,38400*hh
Another practical example is a radar setting the MMSI and IMO number of an AIS transponder and using a
password. It is assumed that the MMSI is not yet set and therefore the value is 0. The radar would send the
following sentences:
$RASPW,EPV,000000000,1,SESAME*hh
$RAEPV,C,AI,000000000,106,503123450*hh
$RASPW,EPV,503123450,1,SESAME*hh
$RAEPV,C,503123450,107,9241061*hh

The AIS would send the following sentences:
$AIEPV,R,AI,503123450,106,503123450*hh
$AIEPV,R,AI,503123450,107,9241061*hh

6.8.8   GBS - GNSS satellite fault detection
This sentence is used to support GNSS receiver autonomous integrity monitoring (RAIM). Given that a GNSS
receiver is tracking enough satellites to perform integrity checks of the positioning quality of the position
solution, a message is needed to report the output of this process to other systems to advise the system user.
With the RAIM in the GNSS receiver, the receiver can isolate faults to individual satellites and not use them in
its position and velocity calculations. Also, the GNSS receiver can still track the satellite and easily judge
when it is back within tolerance.
This sentence shall be used for reporting this RAIM information. To perform this integrity function, the GPS
receiver must have at least two observables in addition to the minimum required for navigation. Normally
these observables take the form of additional redundant satellites.

 $--GBS, hhmmss.ss, x.x, x.x, x.x, xx, x.x, x.x, x.x *hh <CR><LF>

 Field                        Description
 number

 1             hhmmss.ss      UTC time of the GGA or GNS fix associated with this sentence

 2             x.x            Expected error in latitude

 3             x.x            Expected error in longitude

<!-- figure 1 on pdf page 70 at 76,638-538,753 pt | caption: none | text-layer labels: Description | hhmmss.ss | x.x | Expected error in latitude | x.x | Expected error in longitude | nearby labels: Field number | 1 | 2 | 3 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 71 | printed page 69 | header: Technical reference -->

 $--GBS, hhmmss.ss, x.x, x.x, x.x, xx, x.x, x.x, x.x *hh <CR><LF>

 4           x.x              Expected error in altitude - NOT USED

 5           xx               ID number of most likely failed satellite - NOT USED

 6           x.x              Probability of missed detection for most likely failed satellite - NOT USED
 7           x.x              Estimate of bias on most likely failed satellite - NOT USED

 8           x.x              Standard deviation of bias estimate - NOT USED

6.8.9   GGA - Global positioning system (GPS) fix data
This sentence provides time, position and fix related data from a GPS receiver.

 $--GGA, hhmmss.ss, llll.ll, a, yyyyy.yy, a, x, xx, x.x, x.x, M, x.x, M, x.x, xxxx*hh<CR><LF>

 Field                        Description
 number

 1           hhmmss.ss        UTC time of position fix

 2           llll.ll, a       Latitude N/S

 3           yyyyy.yy, a      Longitude E/W

 4           x                GPS quality indicator

 5           xx               No. of satellites in use, 00-12 - NOT USED

 6           x.x              Horizontal dilution of precision - NOT USED
 7           x.x              Antenna altitude above/below mean sea level (geoid) - NOT USED
 8           M                Units of antenna altitude, m - NOT USED

 9           x.x              Geoidal separation - NOT USED

 10          M                Units of geoidal separation, m - NOT USED

 11          x.x              Age of diff. GPS data - NOT USED

 12          xxxx             Differential reference station ID 0000-1023 - NOT USED

6.8.10 GLL - Geographic position, latitude and longitude
This sentence provides the latitude and longitude for vessel position along with fix time and status.

 $--GLL, llll.ll, a, yyyyy.yy, a, hhmmss.ss, A, a *hh<CR><LF>

 Field                        Description
 number

 1            llll.ll, a      Latitude, N/S

 2           yyyyy.yy, a      Longitude, E/W

<!-- figure 1 on pdf page 71 at 356,70-538,194 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 71 at 129,94-182,194 pt | caption: none | text-layer labels: none | nearby labels: x.x | xx | x.x | x.x | x.x | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 71 at 249,242-538,542 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 4 on pdf page 71 at 76,593-538,688 pt | caption: none | text-layer labels: Description | llll.ll, a | Latitude, N/S | yyyyy.yy, a | Longitude, E/W | nearby labels: Field number | 1 | 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 72 | printed page 70 | header: Technical reference -->

 $--GLL, llll.ll, a, yyyyy.yy, a, hhmmss.ss, A, a *hh<CR><LF>

 3          hhmmss.ss        Time of position (UTC)

 4          A                Status: A = data valid V = data invalid

 5          a                Mode indicator:
                             A = Autonomous
                             D = Differential
                             E = Estimated (dead reckoning)
                             M = Manual input
                             S = Simulator
                             N = Data not valid

6.8.11 GNS - GNSS fix data
This sentence provides fix data for a single or combined satellite navigation system. The sentence provides
data for GPS, GLONASS and possible future satellite systems and combinations thereof.

 $-- GNS, hhmmss.ss, llll.ll, a, yyyyy.yy, a, c--c,xx,x.x,x.x,x.x,x.x,x.x *hh<CR><LF>

 Field                       Description
 number

 1          hhmmss.ss        Time of position (UTC)

 2          llll.ll, a       Latitude N/S

 3          yyyyy.yy, a      Longitude E/W

 4          c--c             Mode indicator

 5          xx               Number of satellites in use, 00-99 - NOT USED

 6          x.x              Horizontal dilution of precision (HDOP) - NOT USED
 7          x.x              Antenna altitude, m, above mean-sea-level - NOT USED
 8          x.x              Geoidal separation, m - NOT USED

 9          x.x              Age of differential data - NOT USED

 10         x.x              Differential reference station ID - NOT USED

6.8.12 HDT - Heading, true
Actual vessel heading in degrees produced by a true heading system or device.

 $--HDT, x.x, T*hh<CR><LF>

 Field                       Description
 number

 1          x.x, T           Heading, degrees true

<!-- figure 1 on pdf page 72 at 335,70-538,225 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 72 at 55,593-538,669 pt | caption: none | text-layer labels: $--HDT, x.x, T*hh<CR><LF> | Field number | 1 | Description | x.x, T | Heading, degrees true | nearby labels: 6.8.12 HDT - Heading, true | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 73 | printed page 71 | header: Technical reference -->

6.8.13 LRF - Long range function
This sentence is used in long range interrogation requests and interrogation replies.

 $--LRF,x,xxxxxxxxx,c--c,c--c,c--c*hh<CR><LF>

 Field                        Description
 number

 1           x                Sequence number, 0 to 9

 2           xxxxxxxxx        MMSI of requestor

 3           c--c             Name of requestor, 1 to 20 character string

 4           c--c             Function request, 1 to 26 characters from:
                              A = Ship’s name, call sign and IMO number
                              B = Date and time of message composition
                              C = Position
                              E = Course over ground
                              F = Speed over ground
                              I = Destination and ETA
                              O = Draught
                              P = Ship / Cargo type
                              U = Ship’s length, breadth and type
                              W = Persons on board

 5           c--c             Function reply status:
                              2 = Information available and provided in the following LR1, LR2, or LR3 sen-
                              tence
                              3 = Information not available from AIS transceiver
                              4 = Information is available but not provided (i.e. restricted access determined
                              by ship's master)

6.8.14 LRI - Long range interrogation
The long-range interrogation of the AIS is accomplished through the use of two sentences. The pair of
interrogation sentences, a LRI-sentence followed by a LRF-sentence, provides the information needed by an
AIS to determine if it must construct and provide the reply sentences (LRF, LR1, LR2, and LR3).

 $--LRI,x,a,xxxxxxxxx,xxxxxxxxx,llll.ll,a,yyyyy.yy,a,llll.ll,a,yyyyy.yy,a*hh<CR><LF>

 Field                        Description
 number

 1           x                Sequence number, 0-9

 2           a                Control Flag

 3           xxxxxxxxx        MMSI of “requestor”

 4           xxxxxxxxx        MMSI of “destination”

 5           llll.ll,a        Latitude - N/S

 6           yyyyy.yy,a       Longitude - E/W (north-east co-ordinate)
 7           llll.ll,a        Latitude - N/S
 8           yyyyy.yy,a       Longitude - E/W (south-west co-ordinate)

<!-- pdf page 74 | printed page 72 | header: Technical reference -->

6.8.15 RMC - Recommended minimum specific GNSS data
Time, date, position, course and speed information provided by a GNSS receiver. All data fields should be
provided and null fields only used when data is temporarily unavailable.

 $--RMC, hhmmss.ss, A, llll.ll,a, yyyyy.yy, a, x.x, x.x, xxxxxx, x.x,a, a*hh<CR><LF>

 Field                        Description
 number

 1           hhmmss.ss        Time of position fix (UTC)

 2           A                Status: A = data valid V = navigation receiver warning

 3           llll.ll, a       Latitude, N/S

 4           yyyyy.yy, a      Longitude, E/W

 5           x.x              Speed over ground, knots

 6           x.x              Course over ground, degrees true
 7           xxxxxx           Date: dd/mm/yy - NOT USED
 8           x.x, a           Magnetic variation, degrees, E/W - NOT USED

 10          a                Mode indicator:
                              A = Autonomous mode
                              D = Differential mode
                              E = Estimated (dead reckoning) mode
                              M = Manual input mode
                              S = Simulator mode
                              N = Data not valid

6.8.16 ROT - Rate of turn
This sentence provides rate of turn and direction of turn information.

 $--ROT, x.x, A*hh<CR><LF>

 Field                        Description
 number

 1           x.x              Rate of turn, °/min, "-" = bow turns to port

 2           A                Status: A = data valid, V = data invalid

6.8.17 SPW - Security password sentence
This sentence can be used for authentication. For this purpose the sentence has to be applied before the
protected sentence (for example EPV, SSD).
Other sentences may not be interleaved between the password sentence and protected sentence and the
time between the SPW and the protected sentence should be limited. The password protected sentence pair
should be sent without unnecessary delay between sentences. The recommendation is 1 s maximum
time-out. Note that any of the signals may be lost and timed out.
If the password is not accepted (for example because it is incorrect) the command is refused using the NAK

<!-- figure 1 on pdf page 74 at 244,122-538,432 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 74 at 76,482-538,578 pt | caption: none | text-layer labels: Description | x.x | A | Status: A = data valid, V = data invalid | nearby labels: $--ROT, x.x, A*hh<CR><LF> | Field number | 1 | 2 | 6.8.17 SPW - Security password sentence | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 75 | printed page 73 | header: Technical reference -->

sentence.

 $--SPW,cccc,c--c,x,c--c*hh<CR><LF>

 Field                        Description
 number

 1           cccc             Password protected sentence. The following sentence formatter that should
                              be protected (for example EPV)

 2           c-c              Unique identifier, for AIS the unique identifier is the MMSI

 3           x                Password level,
                              1 = User level password
                              2= Administrator level password
                              3-9 = Reserved.

 4           c--c*            Password, text, up to 32 characters

Example:
The password could be changed with a SPW+EPV sentence pair.
$IISPW,EPV,211000001,2,SESAME*hh
$IIEPV,C,AI,211000001,111,HEUREKA143*hh
With response
$AIEPV,R,AI,211000001,111,HEUREKA143*hh
or NAK or nothing.

6.8.18 SSD - AIS ship static data
This sentence is used to enter static parameters into the ship’s AIS transceiver. The parameters in this
message provide contents for various ITU-R M.1371 messages.

 $--SSD,c--c,c--c,xxx,xxx,xx,xx,c,aa*hh<CR><LF>

 Field                        Description
 number

 1           c--c             Ship's Call Sign, 1 to 7 characters

 2           c--c             Ship's Name, 1 to 20 characters

 3           xxx              Pos. ref., "A," distance from bow, 0 to 511 metres

 4           xxx              Pos. ref., "B," distance from stern, 0 to 511 metres

 5           xx               Pos. ref., "C," distance from port beam, 0 to 63 metres

 6           xx               Pos. ref., "D," distance from starboard beam, 0 to 63 metres
 7           c                DTE indicator flag
 8           aa               Source identifier

6.8.19 THS - True Heading and Status
This sentence is used to enter the actual vessel heading in degrees True produced by any device or system
producing true heading. This sentence includes a “Mode indicator” field providing critical safety related

<!-- figure 1 on pdf page 75 at 239,91-538,276 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 75 at 134,115-184,276 pt | caption: none | text-layer labels: none | nearby labels: cccc | c-c | x | c--c* | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 76 | printed page 74 | header: Technical reference -->

information about the heading data, and replaces the HDT sentence.

 $--THS,x.x,a*hh<CR><LF>

 Field                       Description
 number

 1          x.x              Heading, degrees True

 2          a                Mode indicator 1 characters
                             A = Autonomous mode
                             E = Estimated (dead reckoning) mode
                             M = Manual input mode
                             S = Simulator mode
                             V = Data not valid (including standby)

6.8.20 VBW - Dual ground / water speed
This sentence conveys both water and ground referenced speed data.

 $--VBW, x.x, x.x, A, x.x, x.x, A, x.x, A, x.x, A*hh<CR><LF>

 Field                       Description
 number

 1          x.x              Longitudinal water speed, knots - NOT USED

 2          x.x              Transverse water speed, knots - NOT USED

 3          A                Status: water speed, (A = data valid, V = data invalid) - NOT USED

 4          x.x              Longitudinal ground speed, knots

 5          x.x              Transverse ground speed, knots

 6          A                Status, ground speed, (A = data valid, V = data invalid)
 7          x.x              Stern transverse water speed, knots - NOT USED
 8          A                Status: stern water speed, (A = data valid, V = data invalid) - NOT USED

 9          x.x              Stern transverse ground speed, knots - NOT USED

 10         A                Status: stern ground speed, (A = data valid, V = data invalid) - NOT USED

6.8.21 VSD - Voyage static data
This sentence is used to enter information about the ship’s voyage.

 $--VSD,x.x,x.x,x.x,c--c,hhmmss.ss,xx,xx,x.x,x.x*hh<CR><LF>

 Field                       Description
 number

 1          x.x              Type of ship and cargo category, 0 to 255

 2          x.x              Maximum present static draught, 0 to 25.5 metre

 3          x.x              Persons on-board, 0 to 8191

 4          c--c             Destination, 1-20 characters

 5          hhmmss.ss        Estimated time of arrival at destination (UTC)

<!-- pdf page 77 | printed page 75 | header: Technical reference -->

 $--VSD,x.x,x.x,x.x,c--c,hhmmss.ss,xx,xx,x.x,x.x*hh<CR><LF>

 6           xx                 Estimated day of arrival at destination, 00 to 31 (UTC)
 7           xx                 Estimated month of arrival at destination, 00 to 12 (UTC)
 8           x.x                Navigational status, 0 to 15

 9           x.x                Regional application flags, 0 to 15

6.8.22 VTG - Course over ground and ground speed
The vessels actual course and speed relative to ground.

 $--VTG, x.x, T, x.x, M, x.x, N, x.x, K,a*hh<CR><LF>

 Field                          Description
 number

 1           x.x, T             Course over ground, degrees true

 2           x.x, M             Course over ground, degrees magnetic - NOT USED

 3           x.x, N             Speed over ground, knots

 4           x.x, K             Speed over ground, km/h

 5           a                  Mode indicator:
                                A = Autonomous mode
                                D = Differential mode
                                E = Estimated (dead reckoning) mode
                                M = Manual input mode
                                S = Simulator mode
                                N = Data not valid

6.9 Output data sentence formats
All data output is via IEC61162 / NMEA 0183 sentences. The sentences used by the AIS transceiver are
documented in the subsequent sections. The sentence structure tables describe each field in the sentence
starting from the left most field, (field 1), after the sentence identifier. All sentences are terminated with the
IEC61162 checksum shown as ‘*hh’. For details of the checksum calculation please refer to IEC61162-1.
All sentences start with the delimiter “$” or “!” followed by the talker equipment type identifier. The identifier for
AIS is “AI”, e.g., “AIABK”.

6.9.1   ABK - Addressed and binary broadcast acknowledgement
The ABK sentence is generated when a transaction, initiated by reception of an ABM, AIR, or BBM sentence
is completed or terminated.

 $--ABK,xxxxxxxxx,a,x.x,x,x*hh<CR><LF>

 Field                          Description
 number

 1           xxxxxxxxx          MMSI of the addressed destination AIS transceiver

 2           a                  AIS channel of reception

<!-- figure 1 on pdf page 77 at 76,626-538,722 pt | caption: none | text-layer labels: Description | xxxxxxxxx | a | AIS channel of reception | nearby labels: $--ABK,xxxxxxxxx,a,x.x,x,x*hh<CR><LF> | Field number | 1 | 2 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 78 | printed page 76 | header: Technical reference -->

 $--ABK,xxxxxxxxx,a,x.x,x,x*hh<CR><LF>

 3           x.x             ITU-R M.1371 message ID

 4           x               Message Sequence Number

 5           x               Type of acknowledgement

6.9.2   ACA - AIS Channel assignment message
See section 6.8.2.

6.9.3   ALR - Set alarm state
This sentence is used to indicate local alarm conditions and status along with alarm acknowledgement status.

 $--ALR,hhmmss.ss,xxx,A, A,c--c*hh<CR><LF>

 Field                       Description
 number

 1           hhmmss.ss       Time of alarm condition change, UTC

 2           xxx             Local alarm number (identifier)

 3           A               Alarm condition (A = threshold exceeded, V = not exceeded)

 4           A               Alarm's acknowledge state, A = acknowledged, V = unacknowledged
 5           c--c            Alarm's description text

6.9.4   EPV - Command or report equipment property value
See section 6.8.7.

6.9.5   LRF - AIS long range function
See section 6.8.13.

6.9.6   LRI - AIS long-range interrogation
See section 6.8.14.

6.9.7   LR1 - Long range reply with destination for function request ‘A’
The LR1 sentence identifies the destination for the reply and contains information requested by the ‘A’
function character.

 $--LR1,x,xxxxxxxxx,xxxxxxxxx,c--c,c--c,xxxxxxxxx*hh<CR><LF>

 Field                       Description
 number

 1           x               Sequence Number, 0 to 9

 2           xxxxxxxxx       MMSI of responder

 3           xxxxxxxxx       MMSI of requestor (reply destination)

 4           c--c            Ship's name, 1 to 20 characters
 5           c--c            Call Sign, 1 to 7 characters

 6           xxxxxxxxx       IMO Number, 9-digit number

<!-- figure 1 on pdf page 78 at 253,70-538,154 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 78 at 124,94-182,154 pt | caption: none | text-layer labels: none | nearby labels: x.x | x | x | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 78 at 244,588-538,765 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 43) -->

<!-- pdf page 79 | printed page 77 | header: Technical reference -->

6.9.8   LR2 - Long range reply for function requests ‘B’, ‘C’, ‘E’ and ‘F’
The LR2 sentence contains the information requested by the B, C, E and F function characters.

 $--LR2,x,xxxxxxxxx,xxxxxxxx,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x.x,T,x.x,N*hh<CR><LF>

 Field                        Description
 number

 1           x                Sequence Number, 0 to 9

 2           xxxxxxxxx        MMSI of responder

 3           xxxxxxxxx        Date: ddmmyyyy, 8 digits

 4           hhmmss.ss        Time of position, UTC
 5           llll.ll,a        Latitude, N/S

 6           yyyyy.yy,a       Longitude, E/W

 7           x.x,T            Course over ground, degrees True

 8           x.x,N            Speed over ground, knots

6.9.9   LR3 - Long range reply for function requests ‘I’, ‘O’, ‘P’, ‘U’, and ‘W’
The LR3 sentence contains the information requested by the I, O, P, U and W function characters.

 $--LR3,x,xxxxxxxxx,c--c,xxxxxx,hhmmss.ss,x.x,cc,x.x,x.x,x.x,x.x*hh<CR><LF>

 Field                        Description
 number

 1           x                Sequence Number, 0 to 9

 2           xxxxxxxxx        MMSI of “responder”

 3           c--c             Voyage destination, 1 to 20 characters

 4           xxxxxx           ETA Date: ddmmyy
 5           hhmmss.ss        ETA Time, value to nearest second

 6           x.x              Draught, value to 0,1 metre

 7           cc               Ship/cargo (ITU-R M.1371, Table 18)

 8           x.x              Ship length, value to nearest metre

 9           x.x              Ship breadth, value to nearest metre

 10          x.x              Ship type

 11          x.x              Persons, 0 to 8191

6.9.10 SSD - AIS ship static data
See section 6.8.18.

6.9.11 TRL - AIS Transmitter non-functioning log
This sentence is specific to AIS. It is intended to support the retrieval of the AIS non-functioning log
information.
This satisfies the requirement that the AIS class units log the last 10 times of more than 15 min when the unit

<!-- figure 1 on pdf page 79 at 244,110-538,326 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 80 | printed page 78 | header: Technical reference -->

was not transmitting position reports. This includes times when the unit was switched off and times when the
transceiver was inactivated by any other means.
This sentence is used to output the logged non-functioning times. On a query for this sentence up to 10
sentences will be output, one sentence for each logged no-functioning time.
This sentence is always generated as a response to a query even when no log entries exist.

 $--TRL,x.x,x.x,x,xxxxxxxx,hhmmss.ss,xxxxxxxx,hhmmss.ss,x,*hh<CR><LF>

 Field                       Description
 number

 1          x.x              Total number of log entries, 0 to 9

 2          x.x              Log entry number, 1 to total number of log entries

 3          x                Sequential message identifier, 0 to 9

 4          xxxxxxxx         Switch off date, in the format “ddmmyyyy”
 5          hhmmss,.ss       Switch off UTC time, required resolution is in minutes, the seconds may be set
                             to 0 and the fractional part may be omitted
 6          xxxxxxxx         Switch on date, in the format “ddmmyyyy”
 7          hhmmss.ss        Switch on UTC time, required resolution is in minutes, the seconds may be set
                             to 0 and the fractional part may be omitted
 8          x                Reason code, reason for TX non-functioning
                             1 = power off
                             2= silent mode
                             3 = transmission switched off by channel management command
                             4 = equipment malfunction
                             5= invalid configuration

6.9.12 TXT - Text transmission
For the transmission of short text messages from the AIS equipment. These messages relate to the status of
the equipment.

 $--TXT,xx,xx,xx,c--c*hh<CR><LF>

 Field                       Description
 number

 1          xx               Total number of messages, 01 to 99

 2          xx               Message number, 01 to 99

 3          xx               Text identifier, 01-99

 4          c--c             Text message, ASCII, up to 61 characters

6.9.13 VER - Version
This sentence is used to provide identification and version information about a device. This sentence is
produced as a reply to a query. In order to meet the 79-character requirement, a “multi-sentence message”
may be needed to convey all the Data fields.

<!-- figure 1 on pdf page 80 at 342,139-538,453 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 81 | printed page 79 | header: Technical reference -->

 $--VER,x,x,aa,c--c,c--c,c--c,c--c,c--c,c--c,x,*hh<CR><LF>

 Field                        Description
 number

 1           x                Total number of sentences needed, 1 to 9

 2           x                Sentence number, 1 to 9

 3           aa               Device type, Set to “AI” for AIS

 4           c--c             Vendor ID, NMEA 0183 - 3 character “manufacturer’s mnemonic code”
 5           c--c             Unique identifier, 15 characters maximum
 6           c--c             Manufacturers serial number. 32 characters maximum
 7           c--c             Model code (product code), 32 characters maximum
 8           c--c             Software version, 32 characters maximum
 9           c--c             Hardware revision, 32 characters maximum
 10          x                Sequential message identifier, 1 to 9

6.9.14 VDM - VHF data link message
This sentence is used to transfer the contents of a received AIS message (as defined in ITU-R M.1371) as
received on the VHF Data Link (VDL) using 6 bit ASCII data encapsulation.

 !--VDM,x,x,x,a,s--s,x*hh<CR><LF>

 Field                        Description
 number

 1           x                Total number of sentences needed to transfer the message, 1 to 9

 2           x                Sentence number, 1 to 9

 3           x                Sequential message identifier, 0 to 9

 4           a                AIS Channel, "A" or "B"
 5           s--s             Encapsulated ITU-R M.1371 radio message
 6           x                Number of fill-bits, 0 to 5

6.9.15 VDO - VHF data link own vessel message
This sentence is used to provide the information assembled for broadcast by the AIS transceiver. It uses 6 bit
ASCII data encapsulation.

 !--VDO,x,x,x,a,s--s,x*hh<CR><LF>

 Field                        Description
 number

 1           x                Total number of sentences needed to transfer the message, 1 to 9

 2           x                Sentence number, 1 to 9

<!-- figure 1 on pdf page 81 at 304,91-538,355 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 81 at 225,417-538,597 pt | caption: none | text-layer labels: none | nearby labels: Description | Sentence number, 1 to 9 | Sequential message identifier, 0 to 9 | AIS Channel, "A" or "B" | Encapsulated ITU-R M.1371 radio message | Number of fill-bits, 0 to 5 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 82 | printed page 80 | header: Technical reference -->

 !--VDO,x,x,x,a,s--s,x*hh<CR><LF>

 3            x                  Sequential message identifier, 0 to 9

 4            a                  AIS Channel, "A" or "B"
 5            s--s               Encapsulated ITU-R M.1371 radio message
 6            x                  Number of fill-bits, 0 to 5

6.9.16 VSD - AIS voyage static data
See section 6.8.21.

6.10 Priority of sensor ports
The transceiver automatically assigns a priority scheme to connected sensors. Data from the highest priority
sensor will always be used. Sensor input priority is independently for:

     ● Position
     ● COG+SOG
     ● Heading
     ● Rate-of-Turn

The sensor input ports have the following priority order

 Port                   Priority (1 highest)

 Sen 1                  1

 Sen 2                  2

 Sen 3                  3

 RS232                  4

 Ext. display           5

 Pilot                  6

 Long range             7

Table 13   Port priority order

6.10.1 Position priority scheme
Position information is taken from the highest priority source reporting DTM with WGS84 or datum override
and RMC. If no RMC sentences are available, position shall be taken from the highest priority source
reporting DTM with WGS84 or datum override and any one of:

     ● GGA
     ● GNS
     ● GLL

The following sentences are only processed only if they are from the currently selected position source:

<!-- figure 1 on pdf page 82 at 225,70-538,178 pt | caption: none | text-layer labels: none | nearby labels: Sequential message identifier, 0 to 9 | AIS Channel, "A" or "B" | Encapsulated ITU-R M.1371 radio message | Number of fill-bits, 0 to 5 | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 83 | printed page 81 | header: Technical reference -->

    ● RMC
    ● GGA
    ● GNS
    ● GLL
    ● GBS
    ● GRS
    ● GSA
    ● GSV
    ● GFA

When no position has been received on the selected port for 30 seconds, the port is deselected as a position
source, and a new source selected as described above.

6.10.2 Course and Speed priority scheme
COG and SOG are taken from the highest priority source reporting any one of:

    ● RMC (with DTM=WGS84 or datum override)
    ● VTG
    ● VBW

VTG and VBW are only processed if they are from the currently selected COG & SOG source.

When no COG+SOG has been received on the selected port for 30 seconds, the port shall be deselected as
a COG+SOG source, and a new source selected as described above.

6.10.3 Heading priority scheme
Heading shall be taken from the highest priority sensor reporting any one of:

    ● HDT
    ● THS

HDT and THS are only processed if they are from the currently selected Heading source.

When no heading has been received on the selected port for 30 seconds, the port shall be deselected as a
heading source, and a new source selected as described above

6.10.4 Rate of Turn priority scheme
Rate-of-Turn shall be taken from the highest priority sensor reporting ROT.

ROT shall only be processed if they are from the currently selected Rate-of-Turn source.

When no Rate-of-Turn has been received on the selected port for 30 seconds, the port shall be deselected as
a Rate-of-Turn source, and a new source selected as described above.

<!-- pdf page 84 | printed page 82 -->

Drawings

7   Drawings

7.1 AIS transceiver overall dimensions

                              172 mm

                                          157 mm

                              195 mm          112 mm

             105 mm                                    85 mm

7.2 Junction box overall dimensions

                                 165 mm

                      58 mm

                      52 mm

                                 178 mm      76 mm

<!-- figure 1 on pdf page 84 at 148,158-318,309 pt | caption: none; nearest centred text below: "195 mm" | text-layer labels: none | nearby labels: 172 mm | 195 mm | OCR: no legible text (0/6 words >= 60, mean confidence 17) -->
<!-- figure 2 on pdf page 84 at 344,314-497,451 pt | caption: none | text-layer labels: 112 mm | nearby labels: 157 mm | 85 mm | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 58) -->
112mm
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 84 at 141,333-318,451 pt | caption: none | text-layer labels: none | nearby labels: 105 mm | 195 mm | OCR: no legible text (0/4 words >= 60, mean confidence 22) -->
<!-- figure 4 on pdf page 84 at 160,523-335,636 pt | caption: none | text-layer labels: none | nearby labels: 58 mm | 165 mm | OCR: no legible text (0/2 words >= 60, mean confidence 50) -->
<!-- figure 5 on pdf page 84 at 158,648-335,717 pt | caption: none | text-layer labels: 52 mm | 178 mm | OCR text follows (tesseract, unverified; 1/2 words >= 60, mean confidence 67) -->
ile
<!-- end of figure 5 -->
<!-- figure 6 on pdf page 84 at 356,648-457,717 pt | caption: none | text-layer labels: 76 mm | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 85 | printed page 83 | header: Annex A - ERI Ship types -->

7.3 Dash mount bracket fixing holes (drill drawing) (not to scale)

                                                                           Drill for screw size No. 8 (4-PL)
                              120.0mm                                      Tap drill size No. 29 (3mm drill is sufficient)

                                                                  40.0mm

7.4 GNSS antenna drawing (not to scale)*

                                  75mm

                                                     68mm

                 TNC (male)

                                                                            10m RG58 cable

                                                                                  TNC (male)

* An equivalent alternative GPS antenna may be supplied with transceiver variants without the dual mode
internal GNSS receiver. The dimensions of the supplied antenna may vary from those shown here.

8    Annex A - ERI Ship types

The table below should be used to convert the UN ERI Ship type (used in Inland AIS) to the IMO ship type
used in standard AIS operation. ERI ship types are transmitted in Inland AIS message type 10 whereas the

<!-- figure 1 on pdf page 85 at 60,118-373,271 pt | caption: none | text-layer labels: 40.0mm | 120.0mm | nearby labels: 7.4 GNSS antenna drawing (not to scale)* | OCR: no legible text (0/1 words >= 60, mean confidence 55) -->
<!-- figure 2 on pdf page 85 at 175,331-430,631 pt | caption: none | text-layer labels: 68mm | nearby labels: 75mm | TNC (male) | 10m RG58 cable | TNC (male) | OCR text follows (tesseract, unverified; 3/5 words >= 60, mean confidence 57) -->
A
y
iF
<!-- end of figure 2 -->

<!-- pdf page 86 | printed page 84 | header: Annex A - ERI Ship types -->

ITU vessel type is transmitted in AIS message 5.

                                    ERI Code (Inland AIS)                                       ITU AIS
                                                                                              Vessel type
                                                                                                  code

  Full     U                  Ship Name (EN)                        Vorschlag Via              1st    2nd
  code                                                                                        digit   digit

  8000     No   Vessel, type unknown                        Unbekannter Schiffstyp             9       9

  8010     V    Motor Freighter                             Motorgüterschiff (MGS)             7       9

  8020     V    Motor tanker                                Motortankschiff (MTS)              8       9

  8021     V    Motor tanker, liquid cargo, type N          Motortankschiff, Flüssigfracht,    8       0
                                                            Typ N

  8022     V    Motor tanker, liquid cargo, type C          Motortankschiff, Flüssigfracht,    8       0
                                                            Typ C

  8023     V    Motor tanker, dry cargo as if liquid (e.g   Motortankschiff, Trockenfracht     8       9
                cement)

  8030     V    Container Vessel                            Containerschiff                    7       9

  8040     V    Gas tanker                                  Gas-Tankschiff                     8       0

  8050     C    Motor freighter, tug                        Motorzugschiff                     7       9

  8060     C    Motor tanker, tug                           Motortankzugschiff                 8       9

  8070     C    Motor freighter with one or more ships      Gekoppelte Fahrzeuge, MGS          7       9
                alongside

  8080     C    Motor freighter with tanker                 Gekoppelte Fahrzeuge, mind.        8       9
                                                            1 MTS

  8090     C    Motor freighter pushing one or more         Schubverband, MGS                  7       9
                freighters

  8100     C    Motor freighter pushing at least one        Schubverband, mind. 1 TSL          8       9
                tank-ship

  8110     No   Tug, freighter                              Schlepp-Güterschiff                7       9

  8120     No   Tug, tanker                                 Schlepp-Tankschiff                 8       9

  8130     C    Tug freighter, coupled                      Gekoppelte                         3       1
                                                            Schlepp-Güterschiffe

  8140     C    Tug, freighter/tanker, coupled              Gekoppeltes Schlepp-Schiff,        3       1
                                                            min. 1 Schl.TS

  8150     V    Freightbarge                                Schubleichter (SL)                 9       9

  8160     V    Tankbarge                                   Tankschubleichter (TSL)            9       9

  8161     V    Tankbarge, liquid cargo, type N             Tankschubleichter,                 9       0
                                                            Flüssigfracht Typ N

<!-- pdf page 87 | printed page 85 | header: Annex A - ERI Ship types -->

8162   V   Tankbarge, liquid cargo, type C           Tankschubleichter,              9   0
                                                     Flüssigfracht, Typ C

6163   V   Tankbarge, dry cargo as if liquid (e.g    Tankschubleichter,              9   9
           cement)                                   Trockenfracht

8170   V   Freightbarge with containers              Tankschubleichter mit           8   9
                                                     Containern

8180   V   Tankbarge, gas                            Tankschubleichter für Gas       9   0

8210   C   Pushtow, one cargo barge                  Motorschubschiff mit 1 SL       7   9

8220   C   Pushtow, two cargo barges                 Motorschubschiff mit 2 SL       7   9

8230   C   Pushtow, three cargo barges               Motorschubschiff mit 3 SL       7   9

8240   C   Pushtow, four cargo barges                Motorschubschiff mit 4 SL       7   9

8250   C   Pushtow, five cargo barges                Motorschubschiff mit 5 SL       7   9

8260   C   Pushtow, six cargo barges                 Motorschubschiff mit 6 SL       7   9

8270   C   Pushtow, seven cargo barges               Motorschubschiff mit 7 SL       7   9

8280   C   Pushtow, eight cargo barges               Motorschubschiff mit 8 SL       7   9

8290   C   Pushtow, nine or more barges              Motorschubschiff mit mehr als   7   9
                                                     8 SL

8310   C   Pushtow, one tank/gas barge               Motorschubschiff mit 1 TSL      8   0

8320   C   Pushtow, two barges at least one tanker   Motorschubschiff mit 2 SL –     8   0
           or gas barge                              min.1 TSL

       C   Pushtow, three barges at least one
8330       tanker or gas barge

Motorschubschiff mit 3 SL –   8   0
min.1 TSL

8340   C    Pushtow, four barges at least one tanker   Motorschubschiff mit 4 SL –   8   0
            or gas barge                               min.1 TSL

8350   C    Pushtow, five barges at least one tanker   Motorschubschiff mit 5 SL –   8   0
            or gas barge                               min. 1 TSL

8360   C    Pushtow, six barges at least one tanker    Motorschubschiff mit 6 SL –   8   0
            or gas barge                               min. 1 TSL

8370   C    Pushtow, seven barges at least one         Motorschubschiff mit 7 SL –   8   0
            tanker or gas barge                        min. 1 TSL

8380   C    Pushtow, eight barges at least one         Motorschubschiff mit 8 SL –   8   0
            tanker or gas barge                        min.1 TSL

8390   C    Pushtow, nine or more barges at least      Motorschubschiff >8 SL –      8   0
            one tanker or gas barge                    min.1 TSL

8400   V    Tug, single                                Motorzugschiff                5   2

8410   No   Tug, one or more tows                      Motorzugschiff                3   1

<!-- pdf page 88 | printed page 86 | header: Annex A - ERI Ship types -->

8420   C   Tug, assisting a vessel or linked         Motorzugschiff assistierend   3   1
           combination

8430   V   Pushboat, single                          Motorschubschiff              9   9

8440   V   Passenger ship, ferry, cruise ship, red   Motorfahrgastschiff           6   9
           cross ship

8441   V   Ferry                                     Fähre                         6   9

8442   V   Red cross ship                            Krankentransport              5   8

8443   V   Cruise ship                               Kabinenschiff                 6   9

8444   V   Passenger ship without accommodation      Ausflugsschiff                6   9

8450   V   Service vessel, police patrol, port
           service

Bundes-, Einsatzfahrzeug   9   9

8460   V   Vessel, work maintenance craft, floating   Arbeitsfahrzeug                  3   3
           derrick, cable- ship, buoy-ship, dredge

8470   C   Object, towed, not otherwise specified     Geschlepptes Objekt              9   9

8480   V   Fishing boat                               Fischerboot                      3   0

8490   V   Bunkership                                 Bunkerboot                       9   9

8500   V   Barge, tanker, chemical                    Tankschubleichter, chemische     8   0
                                                      Stoffe

8510   C   Object, not otherwise specified            Objekt, nicht näher bezeichnet   9   9

1500   V   General cargo Vessel maritime              Frachtschiff (See)               7   9

1510   V   Unit carrier maritime                      Containerschiff (See)            7   9

1520   V   Bulk carrier maritime                      Massengutschiff (See)            7   9

1530   V   Tanker                                     Tankschiff (Kein Gas) (See)      8   0

1540   V   Liquefied gas tanker                       Seegehendes Gas-Tankschiff       8   0
                                                      (See)

1850   V   Pleasure craft, longer than 20 metres      Sportboot > 20 m (See)           3   7

1900   V   Fast ship                                  Schnelles Schiff                 4   9

1910   V   Hydrofoil                                  Tragflügelboot                   4   9

<!-- pdf page 89 | printed page 87 -->

    Installation record

9     Installation record

The following installation record should be completed and retained on board the vessel once the AIS
transceiver has been installed and commissioned.

Vessel details
 Vessel name

 Flag state

 IMO number                                        MMSI number

 Owner                                             Radio call sign

 Type of vessel                                    Gross registered tonnage

 Length (m)                                        Beam (m)

 AIS transceiver serial number
 (see underside of transceiver or packaging
 label)

 Junction box serial number (see label on junc-
 tion box)

 Installation password (if changed from default)

 Transceiver software version number

 UI software version number

GNSS antenna locations
 Internal GNSS antenna location (all dimensions in meters, refer to the diagram below)

A=   B=

C=   D=

External GNSS antenna location (all dimensions in meters, refer to the diagram below)

A=   B=

C=   D=

                     Ref C           Antenna

Stern                                                                  Bow
             Ref B                             Ref A

                             Ref D

Ref A + Ref B = Length in metres          Ref C + Ref D = Beam in metres

<!-- figure 1 on pdf page 89 at 112,146-538,408 pt | caption: none | text-layer labels: MMSI number | Radio call sign | Gross registered tonnage | Beam (m) | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 89 at 55,427-538,513 pt | caption: none | text-layer labels: A= | B= | C= | D= | A= | B= | C= | D= | nearby labels: UI software version number | GNSS antenna locations | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 3 on pdf page 89 at 189,535-409,640 pt | caption: none | text-layer labels: Antenna | Ref C | Ref B | Ref A | Ref D | nearby labels: Stern | Bow | Ref A + Ref B = Length in metres | Ref C + Ref D = Beam in metres | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 90 | printed page 88 -->

Installation record

Connected equipment type (where applicable note equipment model and AIS data port in each case)
 (D)GPS receiver

 Gyro compass

 ROT indicator

 Speed log

 ECDIS

 Radar

 Other equipment

 Power supply

The following drawings should be provided and attached to this installation record:
      ● Antenna layout for VHF and GNSS antennas
      ● AIS arrangement drawing
      ● Block diagram showing interconnection of equipment

Maintenance record

 Modification record number        Details (enter details of modifications to the transceiver including software
                                   updates)

 1

 2

 3

 4

 5

 6

 8

 9

 10

Installer detail
 Installed by (name)

 Installation company name

 Date of installation

 Vessel location at installation

 Signature

<!-- figure 1 on pdf page 90 at 100,108-538,281 pt | caption: none | text-layer labels: none | nearby labels: (D)GPS receiver | Gyro compass | ROT indicator | Speed log | ECDIS | Radar | Other equipment | Power supply | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 2 on pdf page 90 at 55,629-538,746 pt | caption: none | text-layer labels: Installed by (name) | Installation company name | Date of installation | Vessel location at installation | Signature | nearby labels: 10 | Installer detail | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->

<!-- pdf page 91 -->

(no text layer on this page)

<!-- pdf page 92 -->

                                                                                                                HIGH P
                                                                                                           MARI          ERFOR
                                                                                                                                 M A NC
                                                                                                               TIME
                                                                                                                                          E

em-trak A100
                                                                                                                    PRO D
                                                                                                                            UCT S

Features and speciﬁcation

• High performance                           • Small                                        • Transmit off function
• Reliable                                   • Easy to use                                  • Radar type display
• Rugged                                     • Easy to install                              • Certiﬁed for inland & deep sea

Power                                        VHF Transceiver                                Designed to meet
• 12 to 24V DC                               • Transmitter x 1                              the following standards:
• Power consumption 10W                      • Receiver x 3                                 • IEC61993-2
                                             • Frequency: 156.025 to 162.025 MHz              IEC standard, Class A shipborne equipment
GPS Receiver (AIS Internal)                    in 25KHz steps                               • IEC60945 Edn 4.0 ‘Protected’ category
                                             • Output power 12.5W (1W setting available).     IEC standard, environmental requirements
• IEC 61108-1 compliant
                                             • Channel bandwidth: 25KHz                     • ITU-RM.1371-5
                                                                                              Universal AIS Technical Characteristics
                                             • Channel step: 25KHz
Data Interfaces                                                                             • IEC61162-1/2 Edn. 2.0
                                             • Modulation modes
• RS232 38.4k baud bi-directional                                                             IEC standards, digital interfaces
                                             • 25KHz GMSK (AIS, TX and RX)
  (PC connection)                                                                           • IEC61108-1
                                             • 25KHz AFSK (DSC, RX only)                      IEC standard, GPS receiver equipment
• IEC61162-2 bi-directional interfaces x 3
                                             • Bit rate - 9600 b/s (GMSK) and
• IEC61162-1/2 sensor inputs x 3               1200 b/s (FSK)
• DGPS correction data input                 • Rx Sensitivity -109dBM @ 20% PER
  (ITU-R M.823-2)
                                             • Co-channel rejection 10dB
• NMEA0183 compliant
                                             • Adjacent channel selectivity 70dB
                                             • Spurious response rejection 70dB

Product Order Information
• Product Name: em-trak A100 AIS
  Class A transceiver
• Product Code: 405-0025

The em-trak A100 is an aid to navigation and must not be relied upon to provide
accurate navigation information. AIS is not a replacement for vigilant human lookouts
and other navigation aids such as Radar. The performance of the A100 may be
seriously impaired if not installed as instructed in the user manual, or due to other
factors such as weather and or nearby transmitting devices. Compatibility with other
systems may vary and is reliant on the third party systems recognising the standard
outputs from the A100. em-trak reserves the right to update and change these
speciﬁcations at any time and without notice.

High Performance Maritime Products

www.em-trak.com

Head Ofﬁce:                    Regional Ofﬁce:
Wireless House,                470 Atlantic Avenue,
Westfield Industrial Estate,   4th ﬂoor,
Midsomer Norton,               Boston, MA 02210
Bath, BA3 4BS                  United States
United Kingdom 201-0091 V1
T +44 (0)1761 409559           T +1 617 273 8001
F +44 (0)1761 410093
                                                      201-0118:4
