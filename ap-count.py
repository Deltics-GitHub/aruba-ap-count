#!/bin/python2.7
import netsnmp
from collections import Counter
import argparse 

def argsparser ():
    parser = argparse.ArgumentParser()
#    parser.add_argument("-v", "--verbose", help = "be verbose", action = "store_true")
    parser.add_argument("-H", "--host", help = "host", required=True)
    parser.add_argument("-c", "--community", help = "snmp community for host", required=True)
    return parser.parse_args()

args = argsparser()

oid = netsnmp.VarList('.1.3.6.1.4.1.14823.2.2.1.1.2.1.1.7')
snmp_res = netsnmp.snmpwalk(oid, Version=2, DestHost=args.host, Community=args.community)
ap = Counter(snmp_res).keys() # equals to list(set(words))
number = Counter(snmp_res).values() # counts the elements' frequency
res = "\n".join("{} {}".format(x, y) for x, y in zip(ap, number))
print(res)

perfdata1 = ('| {}'.format({a : b for a,b in zip(ap, number)}))
perfdata2 = perfdata1.replace(":", "=")
perfdata3 = perfdata2.replace("{", "")
perfdata4 = perfdata3.replace("}", "")
print(perfdata4)

