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
		print "\n"

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
			


	print "\n"
