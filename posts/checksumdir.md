---
title: checksumdir
author: JP
date_created: 06-03-2016
format: markdown
---

# Installation

`pip install checksumdir`

# Usage

When do I use this? When I’m comparing two directories. `diff` command is a good alternative for comparing too.

Command to use: `checksumdir -a md5 <directory>`

# Examples

    jpd-mbpr:Desktop jpd$ mkdir test-directory
    jpd-mbpr:Desktop jpd$ checksumdir -a md5 test-directory/
    d41d8cd98f00b204e9800998ecf8427e
    jpd-mbpr:Desktop jpd$ touch test-directory/empty-file.txt
    jpd-mbpr:Desktop jpd$ checksumdir -a md5 test-directory/
    74be16979710d4c4e7c6647856088456
    jpd-mbpr:Desktop jpd$ echo 'Hello!' >> test-directory/empty-file.txt
    jpd-mbpr:Desktop jpd$ checksumdir -a md5 test-directory/
    ff0e1d21eb2c778d145c79233fc13e6e
    jpd-mbpr:Desktop jpd$ > test-directory/empty-file.txt
    jpd-mbpr:Desktop jpd$ checksumdir -a md5 test-directory/
    74be16979710d4c4e7c6647856088456
    jpd-mbpr:Desktop jpd$ rm test-directory/empty-file.txt
    jpd-mbpr:Desktop jpd$ checksumdir -a md5 test-directory/
    d41d8cd98f00b204e9800998ecf8427e
    jpd-mbpr:Desktop jpd$ rm -fr test-directory/
    jpd-mbpr:Desktop jpd$
