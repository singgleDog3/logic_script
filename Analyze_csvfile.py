import sys
import struct

def analyze_csvfile(filename):
    fop = open(filename) 
    file_content = fop.readlines()
    new_filename = 'new_' + filename
    new_fop = open(new_filename, 'wb') 
    
    pkt_num = 0

    for line in file_content:
        word = line.split(";")[2].strip()
       # print word,len(word)
        if word[0:4] == 'Stop':
            #print 'stop ...'
            pass

        elif word[0:5] == 'Start':
            #    print 'start ...'
            pass
        elif word == '':
            pass

        else:
            hex_num = hex(int(word,2))
            if len(hex_num) == 3:
                # print '0'+hex_num[2],
                hex_str = '0' + hex_num[2] + ' '
            else :
                # print hex_num[2:4],
                hex_str = hex_num[2:4] + ' '
            # print hex_str,
            new_fop.write(hex_str)
            pkt_num += 1
        
if __name__ == "__main__":

    filename = sys.argv[1]

    analyze_csvfile(filename)

    # print filename





