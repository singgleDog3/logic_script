#!/usr/bin/python
#-*- utf-8 -*-

import os 
import ErrorState


def ACL_Data(data, CID):
	if CID == 0x0001:
	    print "__ACL single __"
	    single_data = data[4:]
	    print "single data: ",
	    for char in single_data:
	        print char,
            print ""

	    code = int(single_data[0], 16)
	    if code == 0x02:
	        print "Connection Request ..."
		print "code: 0x02 ",
		identifier = int(single_data[1], 16)
		print "Identifier: 0x%02x"%(identifier),

		length = int(single_data[2],16) + (int(single_data[3] ,16) << 8)
		print "length: 0x%04x"%(length),
	
		PSM = int(single_data[4], 16) + (int(single_data[5], 16) << 8)
		print "PSM:0x%04x"%(PSM),

		SID = int(single_data[6], 16) + (int(single_data[7], 16 ) << 8)
		print "SID: 0x%04x"%(SID)
            elif code == 0x08:
                print "Echo Request ..."
                print "code: 0x%02x"%(code),
                identifier = int(single_data[1],16)
                print "identifier:0x%02x"%(indentifier),
                length = int(single_data[2],16) +(int(single_data[3],16) << 8)
                print "length:0x%04x "%(length),
                print "data:",
                for char in single_data[4:]:
                    print char,
                print ""
            elif code == 0x06:
                print "Disconnection Rquest ..."
                print "code:0x%02x"%(code),
                identifier = int(single_data[1], 16)
                print "identifier:0x%02x"%(identifier),
                length = int(single_data[2],16) + (int(single_data[3],16) <<8)
                print "length:0x%04x"%(length),
                dest_CID = int(single_data[4],16) + (int(single_data[5],16)<<8)
                print "dest_CID:0x%04x "%(dest_CID),
                sou_CID  = int(single_data[6],16) + (int(single_data[7],16) << 8)
                print "cou_CID:0x%04x"%(sou_CID)
            elif code == 0x04:
                print "Configuration Request ... "
                print "code:0x%02x"%(code),
                identifier = int(single_data[1],16)
                print "identifiler:0x%02x "%(identifier),
                length = int(single_data[2],16) + (int(single_data[3],16) << 8)
                print "length:0x%04x "%(length),
                dest_CID = int(single_data[4],16) + (int(single_data[5],16) << 16)
                print "dest-CID:0x%04x "%(dest_CID),
                flag = int(single_data[6],16)
                print "flag:0x%02x "%(flag),
                print "configuration: ",
                for char in single_data[7:]:
                    print char,
                print ""
            elif code == 0x05:
                print "Configuration Respose ... "
                print "code:0x%02x "%(code),

                identifier = int(single_data[1], 16)
                print "identifier:0x%02x "%(identifier),
                length = int(single_data[2],16) + (int(single_data[3],16)<<8)
                print "length:0x%04x"%(length),
                sou_CID = int(single_data[4],16) + (int(single_data[5],16)<<8)
                print "sou_CID: 0x%04x "%(sou_CID),
                flag = int(single_data[6], 16) + (int(single_data[7], 16) << 8)
                print "flag:0x%04x "%(flag),
                result = int(single_data[8],16) + (int(single_data[9], 16) << 8)
                print "result:0x%04x "%(result),
                config = int(single_data[10],16) + (int(single_data[11], 16)<<16)
                print "config: 0x%04x "%(config)

                

			


	print "\n"
