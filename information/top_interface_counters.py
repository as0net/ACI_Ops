#!/bin//python

import re
try:
    import readline
except:
    pass
import urllib2
import json
import ssl
import trace
import logging
import os
import time
import itertools
import threading
import Queue
import interfaces.switchpreviewutil as switchpreviewutil
from localutils.custom_utils import *
import logging

# Create a custom logger
# Allows logging to state detailed info such as module where code is running and 
# specifiy logging levels for file vs console.  Set default level to DEBUG to allow more
# grainular logging levels
logger = logging.getLogger('aciops.' + __name__)

class interface():
    def __init__(self, kwargs):
        self.__dict__.update(**kwargs)
        self.name = '/'.join(self.affected.split('/')[4:-1])[6:-1]
        self.leaf = self.affected.split('/')[2]
        self.pod = self.affected.split('/')[1]
    def __repr__(self):
        return self.name

class rmonIf():
    def __init__(self, kwargs):
        self.__dict__.update(**kwargs)
        self.name = '/'.join(self.dn.split('/')[4:-1])[6:-1]
        self.leaf = self.dn.split('/')[2]
        self.pod = self.dn.split('/')[1]
    def __repr__(self):
        return self.dn

class eqpt():
    def __init__(self, kwargs):
        self.__dict__.update(**kwargs)
        self.name = '/'.join(self.dn.split('/')[4:-1])[6:-1]
        self.leaf = self.dn.split('/')[2]
        self.pod = self.dn.split('/')[1]
    def __repr__(self):
        return self.dn


class locall1PhysIf():
    def __init__(self, kwargs, interface = None, incounter = None , outcounter = None):
        self.__dict__.update(**kwargs)
        self.name = ''.join(self.dn.split('[')[1][:-1])
        self.leaf = self.dn.split('/')[2]
        self.pod = self.dn.split('/')[1]
        self.interface = interface
        self.incounter = incounter
        self.outcounter = outcounter
    def __repr__(self):
        return self.interface

def main(import_apic,import_cookie):
    global apic
    global cookie
    cookie = import_cookie
    apic = import_apic
    interfaceorder = {}
    #clear_screen()
    #location_banner('Top Interface Problems')
    while True:
        clear_screen()
        location_banner('Top Interface Counters')
        print('\nWhould you like to see counters for: \n  1.) Entire ACI Fabric\n  2.) Per Leaf\n\n')
        while True:
            ask = custom_raw_input('Please Select Number: ')
            if not ask.isdigit():
                continue
            elif ask == '1':
                while True:
                    clear_screen()
                    location_banner('Top Interface Counters')
    
                    url = """https://{apic}/api/class/rmonIfIn.json?order-by=rmonIfIn.errors|desc&page=0&page-size=30&query-target-filter=and(wcard(rmonIfIn.dn,"phys-"),gt(rmonIfIn.errors,"1"))""".format(apic=apic)
                 #   result = GetResponseData(url, cookie)
                 #   rmoifinlist = [rmonIf(x['rmonIfIn']['attributes']) for x in result]
                    print('\x1b[2;40H*** Warning, (bps) rate is based on 5 min interval that resets every 300 sec to 0 \n' +
                          '\x1b[3;40H    if all output rate displays 0 then wait between 1-10 sec to refresh ***\n')
                    print('\x1b[7;2H' + ('*' * 20))
                    print(" Top 50 Input Errors")
                    print('*' * 20)
               #     if rmoifinlist:
               #         for x in rmoifinlist:
               #             print("{} {} {}: {}".format( x.pod, x.leaf, x.name, x.errors))
               #     else:
               #         print("No Input errors found")
                        #print(x.pod, x.leaf, x.name, x.errors)
                    #for x in result:
                    #    print(x['rmonIfIn']['attributes']['dn'],x['rmonIfIn']['attributes']['errors'])
                    url = """https://{apic}/api/class/rmonIfOut.json?order-by=rmonIfOut.errors|desc&page=0&page-size=30&query-target-filter=and(wcard(rmonIfOut.dn,"phys-"),gt(rmonIfOut.errors,"1"))""".format(apic=apic)
                #    result = GetResponseData(url, cookie)
                #    rmoifoutlist = [rmonIf(x['rmonIfOut']['attributes']) for x in result]
                    counter = 0
                    print('\x1b[7;39H{}'.format('*' * 20))
                    print("\x1b[8;39HTop 50 Output Errors")
                    print('\x1b[9;39H{}'.format('*' * 20))
                #    if rmoifoutlist:
                #        for x in rmoifoutlist:
                #            print("\x1b[{};38H{} {} {}: {}".format(10 + counter, x.pod, x.leaf, x.name, x.errors))
                #            counter += 1
                #    else:
                #        print("\x1b[10;38HNo Output errors found")
              #      url = """https://{apic}/api/node/class/fabricNode.json?query-target-filter=and(eq(fabricNode.role,"spine"))""".format(apic=apic)
              #      result = GetResponseData(url, cookie)
              #      spinelist = [x['fabricNode']['attributes']['dn'] for x in result]
               #     url = """https://{apic}/api/class/eqptEgrTotal5min.json?query-target-filter=not(wcard(eqptEgrTotal5min.dn,"po"))&order-by=eqptEgrTotal5min.bytesRate|desc&page=0&page-size=75""".format(apic=apic)
               #     result = GetResponseData(url, cookie)
               #     eqptoutlist = [eqpt(x['eqptEgrTotal5min']['attributes']) for x in result]
               #     counter = 0
                    print(' \x1b[7;75H{}'.format('*' * 40))
                    print(" \x1b[8;75HTop 50 Input (bps) Rate [Access Ports]")
                    print(' \x1b[9;75H{}'.format('*' * 40))
               #     upto50counter = 1
               #     for x in eqptoutlist:
               #         if 'topology/{}/{}'.format(x.pod,x.leaf) not in spinelist and not re.findall(r'\/4[9]|\/5[0-9]', x.name):
               #             print("\x1b[{};75H{} {} {}: {}".format(10 + counter, x.pod, x.leaf, x.name, int(round(float(x.bytesRate))) * 8))
               #             if upto50counter == 50:
               #                 
               #                 break
               #             else:
               #                 upto50counter += 1
               #                 counter += 1
               #             #counter += 1
               #     url = """https://{apic}/api/class/eqptIngrTotal5min.json?order-by=eqptIngrTotal5min.bytesRate|desc&page=0&page-size=75""".format(apic=apic)
               #     result = GetResponseData(url, cookie)
               #     eqptinlist = [eqpt(x['eqptIngrTotal5min']['attributes']) for x in result]
               #     counter = 0
                    print('\x1b[7;121H{}'.format('*' * 40))
                    print("\x1b[8;121HTop 50 Output (bps) Rate [Access Ports]")
                    print('\x1b[9;121H{}'.format('*' * 40))
               #     upto50counter = 1
               #     for x in eqptinlist:
               #         #import pdb; pdb.set_trace()
               #         if 'topology/{}/{}'.format(x.pod,x.leaf) not in spinelist and not re.findall(r'\/4[9]|\/5[0-9]', x.name):
               #             print("\x1b[{};120H{} {} {}: {}".format(10 + counter, x.pod, x.leaf, x.name, int(round(float(x.bytesRate))) * 8))
               #             if upto50counter == 50:
               #                 break
               #             else:
               #                 upto50counter += 1
               #                 counter += 1
                    print(' loading...')
                    url = """https://{apic}/api/class/l1PhysIf.json?rsp-subtree-class=l1PhysIf,eqptIngrTotal5min,eqptEgrTotal5min,rmonIfIn,rmonIfOut&rsp-subtree=full&rsp-subtree-include=stats""".format(apic=apic)
                    result = GetResponseData(url, cookie)
                    print(url)
                    errorlist = []
                    for x in result:
                        if x['l1PhysIf'].get('children') and len(x['l1PhysIf']['children']) > 2:
                            errorlist.append(locall1PhysIf(x['l1PhysIf']['attributes'], interface=x['l1PhysIf']['attributes']['dn'],
                                    incounter=x['l1PhysIf']['children'][3]['rmonIfIn']['attributes']['errors'],
                                    outcounter=x['l1PhysIf']['children'][2]['rmonIfOut']['attributes']['errors']))
                        else:
                            errorlist.append(locall1PhysIf(x['l1PhysIf']['attributes'], interface=x['l1PhysIf']['attributes']['dn'],
                                    incounter=x['l1PhysIf']['children'][1]['rmonIfIn']['attributes']['errors'],
                                    outcounter=x['l1PhysIf']['children'][0]['rmonIfOut']['attributes']['errors']))
                    upto50counter = 1
                   # for num,x in enumerated(sorted(errorlist, key=lambda x: float(x.incounter), reverse=True)):
                    #    if upto50counter == 1:
              
                    for num,errorline in enumerate(sorted(errorlist, key=lambda x: float(x.incounter), reverse=True)):
                        if interfaceorder.get(num):
                            a = " {} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod, errorline.leaf, errorline.name, int(errorline.incounter))
                            interfaceorder[num].append(a)
                        else:
                            a = list()
                          #interfaceorder[num] = list(str(errorline))
                            a.append(" {} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod, errorline.leaf, errorline.name, int(errorline.incounter)))
                            interfaceorder[num] = list(a)
                   #     else:
                   #         print("{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(x.pod, x.leaf, x.name, int(x.incounter)))
                   #  #   {}: {}".format( x.pod, x.leaf, x.name, x.errors))
                        if upto50counter == 50:
                            break
                        else:
                            upto50counter += 1
                            counter += 1
                    upto50counter = 1
                    counter = 0
                   # import pdb; pdb.set_trace()
                    for num,errorline in enumerate(sorted(errorlist, key=lambda x: float(x.outcounter), reverse=True)):
                        if interfaceorder.get(num):
                            a = " {} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod, errorline.leaf, errorline.name, int(errorline.outcounter))
                            interfaceorder[num].append(a)
                        else:
                            a = list()
                          #interfaceorder[num] = list(str(errorline))
                            a.append(" {} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod, errorline.leaf, errorline.name, int(errorline.outcounter)))
                            interfaceorder[num] = list(a)
                        if upto50counter == 50:
                            break
                        else:
                            upto50counter += 1
                            counter += 1
              
                   # import pdb; pdb.set_trace()
                    ratelist = []
                    for x in result:
                        #import pdb; pdb.set_trace()
                        if 'epg' in x['l1PhysIf']['attributes']['usage'] or 'fex-fabric' in x['l1PhysIf']['attributes']['mode']:
                            if x['l1PhysIf'].get('children') and len(x['l1PhysIf']['children']) > 2:
                                ratelist.append(locall1PhysIf(x['l1PhysIf']['attributes'], interface=x['l1PhysIf']['attributes']['dn'],
                                        incounter=x['l1PhysIf']['children'][0]['eqptIngrTotal5min']['attributes']['bytesRate'],
                                        outcounter=x['l1PhysIf']['children'][1]['eqptEgrTotal5min']['attributes']['bytesRate']))
                    upto50counter = 1
                    counter = 0
                    for num,errorline in enumerate(sorted(ratelist, key=lambda x: float(x.incounter), reverse=True)):
                        if interfaceorder.get(num):
                            a = "{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod,errorline.leaf,errorline.name, int(round(float(errorline.incounter))) * 8)
                            interfaceorder[num].append(a)
                        else:
                            a = list()
                          #interfaceorder[num] = list(str(errorline))
                            a.append("{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(x.pod,x.leaf,x.name, int(round(float(x.incounter))) * 8))
                            interfaceorder[num] = list(a)
                        if upto50counter == 50:
                            break
                        else:
                            upto50counter += 1
                            counter += 1
                    counter = 0
                    upto50counter = 1
                    for num,errorline in enumerate(sorted(ratelist, key=lambda x: float(x.outcounter), reverse=True)):
                        if interfaceorder.get(num):
                            a = "{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod,errorline.leaf,errorline.name, int(round(float(errorline.outcounter))) * 8)
                            interfaceorder[num].append(a)
                        else:
                            a = list()
                          #interfaceorder[num] = list(str(errorline))
                            a.append("{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(errorline.pod,errorline.leaf,errorline.name, int(round(float(errorline.outcounter))) * 8))
                            interfaceorder[num] = list(a)
                        if upto50counter == 50:
                            break
                        else:
                            upto50counter += 1
                            counter += 1
                    #import pdb; pdb.set_trace()
                    for num,x in enumerate(sorted(interfaceorder, key=lambda x: int(x))):
                        if num == 0:
                            print("\x1b[10;0H{:50} {:50} {:59} {:60}".format(interfaceorder[x][0],interfaceorder[x][1],interfaceorder[x][2],interfaceorder[x][3]))
                        else:
                            print("{:50} {:50} {:59} {:60}".format(interfaceorder[x][0],interfaceorder[x][1],interfaceorder[x][2],interfaceorder[x][3]))
                #    for num,x in enumerate(sorted(ratelist, key=lambda x: float(x.incounter), reverse=True)):
                #        print("\x1b[{};75H{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(10 + counter,x.pod,x.leaf,x.name, int(round(float(x.incounter))) * 8))
                #        #print("\x1b[{};120H{} {} {}: {}".format(10 + counter, x.pod, x.leaf, x.name, int(round(float(x.bytesRate))) * 8))
                #        if upto50counter == 50:
                #            break
                #        else:
                #            upto50counter += 1
                #            counter += 1
                #    upto50counter = 1
                #    counter = 0
                 #   for num,x in enumerate(sorted(ratelist, key=lambda x: float(x.outcounter), reverse=True)):
                 #       #print(int(round(float(x.incounter))) * 8)
                 #       print("{} {} {}: \x1b[1;33;40m{:,}\x1b[0m".format(x.pod,x.leaf,x.name, int(round(float(x.outcounter))) * 8))
                 #       if upto50counter == 50:
                 #           break
                 #       else:
                 #           upto50counter += 1
                 #           counter += 1
                    ask = custom_raw_input("\nRefresh [y]: ") or 'y'
                    if ask != '' and ask[0].lower() == 'y':
                        continue
                    else:
                        break
                      
                 #   import pdb; pdb.set_trace()
                 #   ingresslist = []
                 #   for x in result:
                 #       if x['l1PhysIf'].get('children'):
                 #           if 'epg' in x['l1PhysIf']['attributes']['usage'] or 'fex-fabric' in x['l1PhysIf']['attributes']['mode']:
                 #               ingresslist.append((x['l1PhysIf']['attributes']['dn'], (x['l1PhysIf']['children'][0]['eqptIngrTotal5min']['attributes']['bytesRate'])))
                 #   for x in sorted(ingresslist, key=lambda x: float(x[1]), reverse=True):
                 #       if int(round(float(x[1]))) * 8 != 0:
                 #           pass
                 #           print('{} {}'.format(x[0], int(round(float(x[1]))) * 8))
                 #   egresslist = []
                 #   for x in result:
                 #       if x['l1PhysIf'].get('children'):
                 #           if 'epg' in x['l1PhysIf']['attributes']['usage'] or 'fex-fabric' in x['l1PhysIf']['attributes']['mode']:
                 #               egresslist.append((x['l1PhysIf']['attributes']['dn'], (x['l1PhysIf']['children'][1]['eqptEgrTotal5min']['attributes']['bytesRate'])))
    #         
                 #   upto50counter = 1
                 #   for x in sorted(egresslist, key=lambda x: float(x[1]), reverse=True):
                 #       if int(round(float(x[1]))) * 8 != 0:
                 #           print('{} {}'.format(x[0], int(round(float(x[1]))) * 8))
                 #   for x in eqptinlist:
                 #       #import pdb; pdb.set_trace()
                 #       if 'topology/{}/{}'.format(x.pod,x.leaf) not in spinelist and not re.findall(r'\/4[9]|\/5[0-9]', x.name):
                 #           print("\x1b[{};120H{} {} {}: {}".format(10 + counter, x.pod, x.leaf, x.name, int(round(float(x.bytesRate))) * 8))
                 #           if upto50counter == 50:
                 #               break
                 #           else:
                 #               upto50counter += 1
                 #               counter += 1
              
                #    url = """https://{apic}/api/node/class/eventRecord.json?order-by=eventRecord.created|desc&page=0&page-size=60&query-target-filter=or(eq(eventRecord.code,"E4205125"),eq(eventRecord.code,"E4215671"))""".format(apic=apic)
                #    result = GetResponseData(url, cookie)
                # #   for x in result:
                #    interfacelist = [interface(x['eventRecord']['attributes']) for x in result]
                #    for x in interfacelist:
                #        print("{} {} {}: {}".format(x.pod, x.leaf, x.name, x.descr))
                        #import pdb; pdb.set_trace()
                  #      print(x['eventRecord']['attributes']['affected'],x['eventRecord']['attributes']['descr'])
              
                   # custom_raw_input('#Press Enter to continue...')
              