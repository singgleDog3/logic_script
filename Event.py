#!/usr/bin/python 
#-*- utf-8 -*-

import os
import ErrorState

def Error_str(ErrorNo):
	error_value = Error_State.values()
	error_str = error_value[ErrorNo]
	return error_str
	pass


def EventData_print(code, data):
	print "\n__Event Data__"
	if code == 0x01:
		print "Inquiry compeleted ..."
		state = int(data[0],16)
		if state == 0x00:
			print "Inquiry Command completed Successfully"
		else:
			error_str = Error_str(state)
			print error_str
	elif code == 0x02:
		print "Inquiry Result ..."
		num_response = data[0]
		BD_ADDR = data[1:6]
		repetiton_mode = data[7]
		device = data[9:12]
		clock_offset = data[12:13]
		pass
	elif code == 0x13:
		print "Numner of compeleted Packet ... "
	elif code == 0x04:
		print "connection request ..."
		BD_Addr = data[0:6]
		device  = data[6:9]
		link_type = data[9]
		
		print "addr: ",
		for char in BD_Addr:
			print char,
		print "device: ",
		for char in device:
			print char,
		print "link_type: ",
		for char in link_type:
			print char,
		print "\n"
	elif code == 0x05:
		print "disconnection compeleted ..."
		state = int(data[0], 16)
		if state == 0x00:
			print "Disconnection has cuured ..",
		else:
			error_str = Error_str(state)
			print error_str,

		conn_handle = int(data[1], 16) + (int(data[2], 16) << 8)
		print "conn_handle: %03x"%(conn_handle & 0X0FFF)

		reason = int(data[3], 16)
		print "reason: 0x%02x"%(reason)

	elif code == 0x1d:
		print "connection packet type change ..."
		state = int(data[0], 16)
		if state == 0x00:
				print "State: 0x%x "%(state),
		else:
			error_str = Error_str(state)
			print error_str,
		conn_handle = int(data[1], 16) + (int(data[2], 16) << 8)
		print "conn_handle: 0x%03x"%(conn_handle & 0x0fff),

		link_type = int(data[3], 16) + ( int(data[4], 16) << 8)
		print "Link_type: 0x%04x"%(link_type)
	
	elif code == 0x0e:
		print "command compeleted ..."
		num_packet = int(data[0], 16)
		print "Num_packet: 0x%02x"%(num_packet),

		cmd_opcode = int(data[1], 16) + ( int(data[2],16) << 8)
		print "cmd_opecode: 0x%04x"%(cmd_opcode),
		
		return_param = data[3:]
		print "return_param: ",
		for char in return_param:
			print char,

	elif code == 0x03:
		print "connection request ..."
		status = int(data[0], 16)
		if status == 0x00:
			print "state: 0x%02x"%(status),
		else:
			err_str = Error_str(status)
			print err_str,

		conn_handle = int(data[1], 16) +( int(data[2], 16) << 8)
		print "conn_handle: 0x%03x"%(conn_handle & 0x0fff),

		BD_Addr = data[3:8]
		print "BD_Addr: ",
		for char in BD_Addr:
			print char,

		link_type = int(data[9], 16)
		if link_type == 0x00:
			print "link_tpye: SCO"
		elif link_type == 0x01:
			print "Link_type: ACL(data channel)"
	
	elif code == 0x1b:
		print "Max slot change ... "
		conn_handle = int(data[0], 16) + (int(data[1], 16) << 8)
		print "conn_handle: 0x%03x"%(conn_handle&0x0fff),

		max_slot = int(data[2], 16)
		print "max_slot: 0x%02x"%(max_slot)
