---
title: RDS connectivity with VPC peering
author: JP
date_created: 07-28-2016
format: markdown
---

The public IP of a *public* accessible RDS instance will resolve to EC2 instance query even when their VPCs are both peered with each other.

To resolve its private IP address, set **Public Accessible to No** (Modification Time: max of 5 minutes).

# VPC Setup

VPC A: 192.168.0.0/16  
VPC B: 172.16.0.0/16  
VPC Peering: Yes

# Tests

Public Accessible: Yes  
Result: Resolved public IP

    PS C:\Users\Administrator> tnc mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com -Port 1433
    WARNING: Ping to mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com failed -- Status: TimedOut  

    ComputerName           : mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com
    RemoteAddress          : 5x.xx.xxx.xxx
    RemotePort             : 1433
    InterfaceAlias         : Ethernet
    SourceAddress          : 172.16.255.105
    PingSucceeded          : False
    PingReplyDetails (RTT) : 0 ms
    TcpTestSucceeded       : True

Public Accessible: No  
Result: Resolved private IP

    PS C:\Users\Administrator> tnc mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com -Port 1433
    WARNING: Ping to mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com failed -- Status: TimedOut  

    ComputerName           : mssql.a123bcdefgh4.us-west-2.rds.amazonaws.com
    RemoteAddress          : 192.168.0.122
    RemotePort             : 1433
    InterfaceAlias         : Ethernet
    SourceAddress          : 172.16.255.105
    PingSucceeded          : False
    PingReplyDetails (RTT) : 0 ms
    TcpTestSucceeded       : True
