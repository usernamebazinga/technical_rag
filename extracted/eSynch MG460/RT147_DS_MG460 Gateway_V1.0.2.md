<!-- font check: Wingdings is not a standard text face; glyphs "" on pages 1. Verify against the rendered page before trusting or mapping. -->

<!-- font check: U+F0D8 (private-use code from Wingdings) on pages 1; the character carries no meaning as text, read the rendered page -->

<!-- pdf page 1 -->

MG460 Gateway
Maritime Cyber Security Gateway
A Maritime Gateway compliance to IEC61162-460 Cyber Security Standards

INTRODUCTION
Robustel’s MG460 Gateway represents a next-generation industrial
maritime gateway, designed to comply with IEC 61162-460 (Maritime
Safety and Security) and IEC 60945 standards. The MG460 Gateway serves
as a seamless interface between onboard vessel equipment and external
services, including cloud platforms and servers.

The MG460 Gateway enhances the security of the navigational equipment
network by implementing a multi-layered inspection firewall and access
control at both the network and transport layers, utilizing address, port,
and protocol-based rules. Powered by a robust 1.6 GHz quad-core CPU and
equipped with 64 GB eMMC Flash storage running a Debian Linux OS, the
MG460 Gateway is capable of executing complex applications and
facilitating efficient software deployment. Featuring 5 Gigabit Ethernet
ports (each equipped with its own firewall), 2 software-configurable serial
ports, 2 digital inputs, 2 relay outputs, and 3 protected USB ports, the
MG460 Gateway provides comprehensive connectivity options for various
field devices.

The Robustel Cloud Manager Service (RCMS) is a unified cloud-based
platform designed for real-time monitoring and centralized management of
industrial IoT devices. Fully compatible with Robustel routers and gateways,
RCMS delivers an interactive geospatial dashboard that enables users to
visualize device locations and track critical metrics such as data usage,
signal strength, and network status. To ensure seamless operations, the
platform facilitates over-the-air (OTA) updates for firmware, configurations,
and applications, minimizing downtime while optimizing system
performance. Experience robust, cloud-native device management by
registering at: https://rcms-cloud.robustel.net

APPLICATION EXAMPLE

                                                 PRODUCT DATASHEET

KEY FEATURES
 Comply with IEC 61162-1, IEC 61162-2, IEC 61162-460 Edition
  3, and IEC 60945 standards
 Achieve DNV Certification as 460-Gateway and 460-Wireless
  Gateway
 Utilize a high-performance compute engine with a 1.6 GHz
  CPU and 64 GB eMMC Flash for executing complex
  applications
 Establish a DMZ with file storage and application services for
  secure interconnection
 Enable remote access tunnels with VPN for secure connectivity
 Leverage a Linux Debian system for user software
  development and deployment
 Provide 5 x 1000 Mbps Ethernet ports, each with an individual
  firewall for enhanced security
 Connect industrial and legacy devices via 2 x
  RS-232/RS422/RS-485 (software configurable) ports
 Facilitate simple monitoring and control with 2 x Digital Inputs
  and 2 x Relay Outputs
 Expand storage capabilities with a microSD slot for recording
  system logs and navigation data
 Support dual SIM card slots for redundant communications
 Ensure uninterrupted network connectivity with an
  industrial-grade design
 Manage large device estates efficiently via RCMS (Robustel’s
  router/gateway management platform) and RobustVPN
  service

<!-- figure 1 on pdf page 1 at 0,0-593,211 pt | caption: none; nearest centred text below: "KEY FEATURES" | text-layer labels: PRODUCT DATASHEET | MG460 Gateway | Maritime Cyber Security Gateway | nearby labels: INTRODUCTION | KEY FEATURES | OCR text follows (tesseract, unverified; 2/5 words >= 60, mean confidence 47) -->
rabustel
Stel
<!-- end of figure 1 -->
<!-- figure 2 on pdf page 1 at 22,566-67,612 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/6 words >= 60, mean confidence 35) -->
of,
<!-- end of figure 2 -->
<!-- figure 3 on pdf page 1 at 146,566-227,612 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 1/1 words >= 60, mean confidence 69) -->
rebustel
<!-- end of figure 3 -->
<!-- figure 4 on pdf page 1 at 74,568-136,609 pt | caption: none | text-layer labels: none | OCR: no legible text (0/0 words >= 60, mean confidence 0) -->
<!-- figure 5 on pdf page 1 at 79,664-253,801 pt | caption: none | text-layer labels: none | OCR text follows (tesseract, unverified; 9/44 words >= 60, mean confidence 38) -->
200000
Radar
GYRO
Als
oo
Automatic System
Cargo system
<!-- end of figure 5 -->

<!-- pdf page 2 -->

SPECIFICATIONS
Hardware System                                                                 Software (Basic features of MG Core)
CPU                           Quad core Cortex-A53, 1.6 GHz                     Network protocols               PPP, PPPoE, TCP, UDP, DHCP, ICMP, NAT, HTTP, DNS, NTP,
NPU                           2.3 TOPS                                                                          SMTP, Telnet, VLAN, HTTPs, ARP, SSH2, DDNS, etc.

RAM                           4 GB DDR4                                         VPN tunnels                     IPsec, OpenVPN, GRE, DMVPN

Flash                         64 GB eMMC                                        Firewalls                       DMZ, anti-DoS, Filtering (IP/Domain name/MAC
                                                                                                                address), Port Mapping, Access Control
Cellular Interface
Version                       4G                            5G                  Remote management               Web, CLI, SMS
                                                                                Serial port protocols           Transparent, TCP Client/Server, UDP, Modbus RTU
Number of antennas            2                             4
                                                                                                                Gateway
Connector                     SMA-K
SIM                           2 x Mini SIM (2FF)
                                                                                SDK
                                                                                Operating system                MG Core (Based on Debian 11 Bullseye)
Ethernet Port
                                                                                Supported programming           C, C++, Python, Java, Node.js etc.
Number of ports               5 x RJ45, 10/100/1000 Mbps
                                                                                languages                       (for users to develop own applications)
                              Compliance with 1000BASE-T, LAN or WAN
                                                                                Debian Repository available
Magnet isolation protection   1 KV
                                                                                Flash available for SDK         62 GB
Serial Port
                                                                                RAM available for SDK           2.5 GB
Number of ports               2 x RS-232/RS422/RS-485 (software configurable)
Connector                     2 x 5-pin 3.5 mm terminal block
                                                                                App Center (Available Apps for MG Core)
                                                                                Apps*                           Language, RCMS
ESD protection                8 KV Air, 4 KV Contact
                                                                                *Request on demand. For more Apps please visit www.robustel.com.
Baud rate                     300 bps to 115200 bps
Signal                        RS-232: TXD, RXD, GND, CTS, RTS                   Cloud Platform
                                                                                Robustel Cloud Manager          RobustLink, RobustVPN, Operation Console
                              RS-485: Data+ (A), Data- (B), GND
                                                                                Service (RCMS)
                              RS422: RX+, RX-, TX+, TX-, GND
                                                                                Power Supply and Consumption
Console Port
                                                                                Connector                       2-pin 3.5 mm terminal block with lock
Number of ports               1 x RS-232
                                                                                Input voltage                   24 V DC, reverse polarity protection, surge protection
Connector                     RJ45
                                                                                Power consumption               Idle: 6.24 W@24 V
Baud rate                     115200 bps
                                                                                                                Max: 14.64 W@24 V
Signal                        TXD, RXD, GND
                                                                                Physical Characteristics
Digital Input Port
                                                                                Ingress protection              IP30
Number of ports               2 x DI, wet contact
                                                                                Housing & Weight                Metal, 649 g
Connector                     4-pin 3.5 mm terminal block
                                                                                Dimensions                      58 x 111 x 128 mm
Isolation                     Bi-directional optocoupler (DI)
                                                                                Installations                   Desktop, wall mounting and 35 mm DIN rail mounting
Absolute maximum VDC          + 30 V DC
                                                                                Operating temperature           -30 ~ +70 °C
Absolute maximum ADC          100 mA
                                                                                Storage temperature             -40 ~ +85 °C
Signal definition             DI1+, DI1-, DI2+, DI2-
                                                                                Relative humidity               5 ~ 95% RH (non-condensing)
Relay Output Port
Number of ports               2 x Relay Output
                                                                                Regulatory and Type Approvals
                                                                                Environmental                   RoHS2.0
Connector                     6-pin 3.5 mm terminal block
                                                                                EMI                             EN 55032 Conducted Emission Class B
Absolute maximum VDC          + 48 V DC
                                                                                                                EN 55032 Radiated Emission Class A
Absolute maximum ADC          100 mA
                                                                                EMS                             EN 61000-3-2 (Harmonic Current)
Signal definition             NC1, NO1, COM1, NC2, NO2, COM2
                                                                                                                EN 61000-3-3 (Voltage Flicker)
USB Port                                                                                                        EN 61000-4-2 (ESD) Contact Level 3, Air Level 3
Number of ports               2 x USB 3.0 (host), Type A, 5V, 900mA
                                                                                                                EN 61000-4-3 (RS) Level 3
                              1 x USB 2.0 (OTG), Type C
                                                                                                                EN 61000-4-4 (EFT) Level 3
Wi-Fi Interface                                                                                                 EN 61000-4-5 (Surge) Level 3
Wi-Fi                         Wi-Fi 2.4 GHz/5 GHz , 2 × 2 MU-MIMO
                                                                                                                EN 61000-4-6 (CS) Level 2
                              IEEE 802.11 a/b/g/n/ac/ax
                                                                                                                EN 61000-4-11 (Dips)
GNSS Interface
Version                       4G
Number of antennas            1
Connector                     SMA-K
Technology                    GPS
Others
SD                            1 x microSD
HDMI                          1 x HDMI
Reset button                  1 x RST
LED indicators                1 x RUN, 1 x Signal, 1 x MDM, 1 x VPN, 2 x USR
Watchdog                      External

<!-- pdf page 3 -->

ORDERING INFORMATION
   Model   Order   Wi-Fi   GNSS   Frequency Bands*   Country   Certification   Package Contains
           Code                                      /Region

MG460-A5ZAZ-NU   A014700002   -   -   -

1 x MG460 Gateway (B C ode: B014700001)
1 x DIN Rail Mounting Kit

                                                                                                                                       1 x MG460 Gateway (B C ode: B014700002)
   MG460-A5CAZ-NU             A014700003          √            -        -                                                    CE
                                                                                                                                       1 x DIN Rail Mounting Kit
                                                                                                                           UKCA
                                                                                                                           RCM
                                                                                                                            CB
                                                                        4G:                                                 FCC
                                                                        LTE FDD: B1/2/3/4/5/7/8/12/13/18                               1 x MG460 Gateway (B C ode: B014700003)
MG460-A5AAZ-4L-A06GL          A014700004          -           √                                                              IC
                                                                        /19/20/25/26/28                                                1 x DIN Rail Mounting Kit
                                                                        LTE TDD: B38/39/40/41

                                                                        3G:
                                                                        WCDMA: B1/2/4/5/6/8/19
                                                                                                                                       1 x MG460 Gateway (B C ode: B014700004)
MG460-A5BAZ-4L-A06GL          A014700005          √           √         2G:                                       Global               1 x DIN Rail Mounting Kit
                                                                        GSM: B2/3/5/8

                                                                        5G NR:
                                                                        NSA:
                                                                        n1/2/3/5/7/8/12/13/14/18/20/25/                                1 x MG460 Gateway (B C ode: B014700005)
MG460-A5AAZ-5G-A25GL          A014700006          -            -        26/28/29/30/38/40/41/48/66/70/                                 1 x DIN Rail Mounting Kit
                                                                        71/75/76/77/78/79
                                                                        SA:
                                                                        n1/2/3/5/7/8/12/13/14/18/20/25/
                                                                        26/28/29/30/38/40/41/48/66/70/                       CE
                                                                        71/75/76/77/78/79                                  UKCA
                                                                        4G:                                                RCM
                                                                        LTE FDD:                                            FCC
                                                                        B1/2/3/4/5/7/8/12/13/14/17/18/                       IC        1 x MG460 Gateway (B C ode: B014700006)
MG460-A5BAZ-5G-A25GL          A014700007          √            -        19/20/25/26/28/29/30/32/66/71                                  1 x DIN Rail Mounting Kit
                                                                        LTE TDD:
                                                                        B34/38/39/40/41/42/43/48
                                                                        LAA: B46

                                                                        3G:
                                                                        WCDMA: B1/2/4/5/8/19
*For more information about frequency bands in different countries, please contact your Robustel sales representative.

                                                                                                                                                        Email: info@robustel.com
                                                                                                                                                     Website: www.robustel.com
                                                                                                                                          ©2025 Guangzhou Robustel Co., Ltd.
                                                                                                                           All rights reserved. Subject to change without notice.

<!-- figure 1 on pdf page 3 at 0,739-593,840 pt | caption: none | text-layer labels: none | OCR: no legible text (0/1 words >= 60, mean confidence 42) -->
