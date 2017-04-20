#-*- utf-8 --*-
import Analyze_csvfile
import sys
import struct
import os
import string
import array


# HCI command format
# op_code(2 octets) + length(1 octets) + param

# HCI ACL data packet
# Handle(12 bits) + PB FLAG(2 bits) + BC flag(2 bits) + length (2 octets) + data

# HCI synchronous data packets
# conn_handle(12 bits) + packetStatusFlag(2 bits) + reserved(2 bits) + length(1 octets)+ data

# HCI event packet
# event_code(1 octets) + length(1 octets) + param 

class HCI_Command:
    def __init__(self, str = []):
        self.hci_flag = []
        self.ocf      = []
        self.ogf      = []
        self.length   = []
        self.param    = []
        self.str = str[0:]
        self.HCICMD_init()
        
        
    def HCICMD_init(self):
        self.hci_flag = self.str[0]
        self.ocf      = (self.str[1] & 0xc0 ) << 8 | ((self.str[1] << 2 ) | self.str[2] >> 6)
        self.ogf      = self.str[2] & 0x3f
        self.length   = self.str[3]
        self.param[0:]   = self.str[4:]
        
        
    def HEX_print(self):
        for ch in self.str:
            print hex(ch),
        
    def  HCI_print(self):
        self.HEX_print()
        print "\n|- flag # %02x"%(self.hci_flag),
        print "|- ocf # %03x"%(self.ocf),
        print "|- ogf # %02x"%(self.ogf),
        print "|- len # %d"%(self.length),
        print "|- param # ",self.param 
        print "\n\n"
        
class HCI_Event:
    def __init__(self, str = []):
        self.str = str[0:]
        self.EventCode = []
        self.Length    = []
        self.param     = []
        
        self.HCIEvent_Init()
        self.HEX_Show()
        
        self.HCI_print()


    def HCIEvent_Init(self):
        self.EventCode = self.str[0]
        self.Length = self.str[1]
        self.param[0:] = self.str[2:]
        
    def HEX_Show(self):
        for num in self.str:
            print '0x%02x'%(num) ,

    def HCI_print(self):
        print '\n#- F -| %d'%(self.EventCode),
        print '#- Len: %d'%(self.Length),
        print '#- param: ' , self.param,
        print '\n\n'

def HCIEvent_print(evcode, evlen, evdata):
    print '##### Event Packet #####'
    code_num = int(evcode, 16)
    len_num = int(evlen, 16)

    print 'code: 0x%02x  len:0x%02x '%(code_num, len_num)
    print 'data: ',
    for char in evdata:
        print char,
    print "\n"
    pass

def ACLData_Print(data):
    data_len = int(data[0], 16) +  (int(data[1], 16) << 8 )
    data_CID = int(data[2], 16) +  (int(data[3], 16) << 8 )
    data_pyload = data[4:]

    print "__ ACL Data ___"
    print 'len: 0x%04x  CID: 0x%04x '%(data_len, data_CID)
    print 'data: ',
    for char in data_pyload:
        print char,
    print '\n'

def ACLPKT_print(handle, length, data):
    print "##### ACL Packet ####"
   # print handle, length, data
    handle_num = (int(handle[1], 16) << 8 ) + int(handle[0], 16)
    length_num = (int(length[1], 16) << 8 ) + int(length[0], 16)
    flag = (handle_num & 0xf000 ) >> 12;
    # print 'flag: 0x%x '%(flag)

    PB_flag = ( flag & 0xc ) >> 2;
    BC_flag = flag & 0x3;

    handle_num = handle_num & 0x0fff;


    print 'handle: 0x%04x  PB: 0x%01x BC:0x%01x length:0x%04x'%(handle_num, PB_flag, BC_flag, length_num)
    print 'data: ',
    for char in data:
        print char,
    print ''
    ACLData_Print(data)
    pass


def Analyze(filename):
    fops = open(filename)
    file_content = fops.readlines()
    split_content = [] 

    
    current_place = 0

    for line in file_content:
        split_content += line.split(" ")
    
    current_place = 0

    while(current_place < len(split_content)):

        if split_content[current_place] == '01':
            pass

        elif split_content[current_place] == '02':
            handle = split_content[current_place + 1: current_place + 3]
            length = split_content[current_place + 3: current_place + 5]
            
            if length[0] != "" and length[1] != "":
                length_num = int(length[0],16)  + ( int(length[1] ,16) << 8) 
                acl_data = split_content[current_place + 5: current_place + length_num + 5]
                current_place += 5 + length_num

                ACLPKT_print(handle, length, acl_data)



            else:
                print "error ..."
                return -1

        elif split_content[current_place] == '03':
            pass

        elif split_content[current_place] == '04':
            Ev_Code = split_content[current_place + 1]
            Ev_Len  = int( split_content[current_place + 2], 16)
            Ev_Data = split_content[current_place + 3: current_place + 3 + Ev_Len]
            HCIEvent_print(Ev_Code, split_content[current_place + 2], Ev_Data)
            current_place += Ev_Len +3
            # 
          #  HCIEvent_print(Ev_Code, split_content[current_place + 2], Ev_Data)

        else:
            print "error ..."
            return -1

    
if __name__ == "__main__":
    filename = sys.argv[1]
    print filename + '....'
    Analyze_csvfile.analyze_csvfile(filename)

    new_filename = "new_" + filename
    Analyze(new_filename)
