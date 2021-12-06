#!/bin/bash

C1=message1
C2=message2

K1=key1.pem
K2=key2.pem

python3 rsa-cm.py -c1 $C1 -c2 $C2 -k1 $K1 -k2 $K2

#HTB{C0mmon_M0dUlu5S_1S_b4D}