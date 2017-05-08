---
title: How to fix “The filesystem is already X blocks long. Nothing to do!” when resizing a volume of an EC2 instance
author: JP
date_created: 06-29-2016
format: markdown
---

# Error message

    [root@ip-192-168-255-7 ~]# resize2fs -p /dev/xvda1
    resize2fs 1.41.12 (17-May-2010)
    The filesystem is already 2096896 blocks long. Nothing to do!

    [root@ip-192-168-255-7 ~]#

# How to fix this?

* SSH to your EC2 instance: `ssh -i my-key.pem ec2-user@hostname`
* Get the device name: `lsblk` (/dev/xvda is the device name, /dev/xvda1 is the partition)
* Open partition table manipulator for Linux for /dev/xvda device: `fdisk /dev/xvda`
* Change the display units to sectors: **u**
* Print the partition table: **p**
* Delete a partition: **d**
* Add a new partition: **n**
* Primary partition: **p**
* Partition number: **1**
* First sector: **2048**
* Last sector: Press **Enter** to use the default value
* Print the partition table: **p**
* Toggle a bootable flag: **a**
* Partition number: **1**
* Write table to disk and exit: **w**
* Reboot the instance: `reboot`
* Show filesystem: `df -h /dev/xvda1`

# Example

    [root@ip-192-168-255-7 ~]# lsblk
    NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
    xvda 202:0 0 20G 0 disk
    └─xvda1 202:1 0 8G 0 part /
    [root@ip-192-168-255-7 ~]# fdisk /dev/xvda

    WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
    switch off the mode (command 'c') and change display units to
    sectors (command 'u').

    Command (m for help): u
    Changing display/entry units to sectors

    Command (m for help): p

    Disk /dev/xvda: 21.5 GB, 21474836480 bytes
    255 heads, 63 sectors/track, 2610 cylinders, total 41943040 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00057cbb

    Device Boot Start End Blocks Id System
    /dev/xvda1 * 2048 16777215 8387584 83 Linux

    Command (m for help): d
    Selected partition 1

    Command (m for help): n
    Command action
    e extended
    p primary partition (1-4)
    p
    Partition number (1-4): 1
    First sector (63-41943039, default 63): 2048
    Last sector, +sectors or +size{K,M,G} (2048-41943039, default 41943039):
    Using default value 41943039

    Command (m for help): p

    Disk /dev/xvda: 21.5 GB, 21474836480 bytes
    255 heads, 63 sectors/track, 2610 cylinders, total 41943040 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00057cbb

    Device Boot Start End Blocks Id System
    /dev/xvda1 2048 41943039 20970496 83 Linux

    Command (m for help): a
    Partition number (1-4): 1

    Command (m for help): w
    The partition table has been altered!

    Calling ioctl() to re-read partition table.

    WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
    The kernel still uses the old table. The new table will be used at
    the next reboot or after you run partprobe(8) or kpartx(8)
    Syncing disks.
    [root@ip-192-168-255-7 ~]# reboot

    Broadcast message from centos@ip-192-168-255-7.company.internal
    (/dev/pts/0) at 10:05 ...

    The system is going down for reboot NOW!
    [root@ip-192-168-255-7 ~]# Connection to omd.company.com closed by remote host.
