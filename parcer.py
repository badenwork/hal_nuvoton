#!/bin/env python3

import re

FILE = "dts/m2354/sys.h"

# Searc like this
# (SYS_GP[A-H]_MFP[LH]_P[A-H](\d?)MFP_*)\w+

RE = r"#define (SYS_GP([A-H])_MFP[LH]_P[A-H](\d{1,2})MFP_([A-Z\d_]*))\s+"
parser = re.compile(RE)

with open(FILE, "r") as f:
    for line in f:
        match = parser.search(line)
        if match:
            register = match.group(1)
            port = match.group(2)
            pin = match.group(3)
            mfp = match.group(4)
            print(f"#define P{port}{pin}MFP_{mfp}\t\tNVT_PINMUX('{port}', {pin}, {register})") 
