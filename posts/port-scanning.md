---
title: Port Scanning
author: JP
date_created: 06-01-2016
format: markdown
---

# telnet

## Installation

For RHEL-based operating systems: `yum install -y telnet`

For Debian-based operating systems: `apt-get install -y telnet`

## Example

    JPs-MBPr:~ jpd$ telnet jpdoria.com 22
    Trying 52.8.60.126...
    Connected to jpdoria.com.
    Escape character is '^]'.
    SSH-2.0-OpenSSH_6.6.1
    quit
    Protocol mismatch.
    Connection closed by foreign host.
    JPs-MBPr:~ jpd$

# nc

## Installation

For RHEL-based operating systems: `yum install -y nc`

For Debian-based operating systems: `apt-get install -y netcat`

## Example of TPC port scan

    JPs-MBPr:~ jpd$ nc -zvv jpdoria.com 80
    found 0 associations
    found 1 connections:
    1: flags=82&lt;CONNECTED,PREFERRED&gt;
    outif en0
    src 10.0.0.101 port 53973
    dst 52.8.60.126 port 80
    rank info not available
    TCP aux info available  

    Connection to jpdoria.com port 80 [tcp/http] succeeded!
    JPs-MBPr:~ jpd$

## Example of UDP port scan

    JPs-MBPr:~ jpd$ nc -zvvu jpdoria.com 1194
    found 0 associations
    found 1 connections:
    1: flags=82&lt;CONNECTED,PREFERRED&gt;
    outif (null)
    src 10.0.0.101 port 58938
    dst 52.8.60.126 port 1194
    rank info not available 

    Connection to jpdoria.com port 1194 [udp/openvpn] succeeded!
    JPs-MBPr:~ jpd$

## Example of port scan using range

    JPs-MBPr:~ jpd$ nc -zvv jpdoria.com 79-80
    nc: connectx to jpdoria.com port 79 (tcp) failed: Operation timed out
    found 0 associations
    found 1 connections:
    1: flags=82&lt;CONNECTED,PREFERRED&gt;
    outif en0
    src 10.0.0.101 port 54038
    dst 52.8.60.126 port 80
    rank info not available
    TCP aux info available  

    Connection to jpdoria.com port 80 [tcp/http] succeeded!
    JPs-MBPr:~ jpd$
