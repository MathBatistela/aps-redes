"""------------------------------------------------------------------------------
    Descrição:    	Biblioteca responsável por receber um IP e uma mácara de rede, 
                    e retornar os dados de acordo com o método requisitado. 

    Autores:         	Matheus Batistela
  
    Data de criação:	30/11/2019
    Revisão:			05/12/2019
------------------------------------------------------------------------------"""
class IpCalculator:

    def __init__(self,ip_address,network_mask):
        self.ip_decimal = self.stringToIntList(ip_address)
        self.mask_decimal = self.stringToIntList(network_mask)
        self.ip_binary = self.binaryConvert(self.ip_decimal)
        self.mask_binary = self.binaryConvert(self.mask_decimal)

    @staticmethod
    def stringToIntList(string_list):
        _list = (string_list).split(".") 
        _list = list(map(int,_list))
        return _list

    @staticmethod
    def intListToString(ip_list):
        return '.'.join(list(map(str,ip_list)))

    @staticmethod
    def binaryConvert(d_list):
        b_list = []
        for dnumber in d_list:
            b_list.append('{0:08b}'.format(dnumber))    
        b_list = ''.join(b_list)
        return list(b_list)

    @staticmethod
    def decimalConvert(b_list):
        d_list = []
        for byte in range(0,len(b_list),8):
            d_list.append(int(''.join(b_list[byte:byte+8]),2))
        return d_list


    def isValidIp(self):
        for ip in self.ip_decimal:
            if(ip > 255 or ip < 0):
                return 0
        return 1

    def isValidMask(self):
        zero_find = 0
        for bit in self.mask_binary:
            if(bit == '0' and zero_find == 0):
                zero_find = 1
            elif(bit == '1' and zero_find == 1):
                return 0
        return 1

    def networkBits(self):
        n_bits = 0
        for bit in self.mask_binary:
            if(bit == '0'):
                return n_bits
            n_bits += 1

    def hostBits(self):
        return 32 - self.networkBits()

    def ipClass(self):
        first_byte = self.ip_decimal[0]
        if(first_byte >= 0 and first_byte <= 127): return 'A'
        elif(first_byte >= 128 and first_byte <= 191): return 'B'
        elif(first_byte >= 192 and first_byte <= 223): return 'C'
        elif(first_byte >= 224 and first_byte <= 239): return 'D'
        elif(first_byte >= 240 and first_byte <= 255): return 'E'

    def networkIp(self):
        n_bits = self.hostBits()
        network_ip = self.ip_binary[:]
        for bit in range(32-n_bits,32):
            network_ip[bit] = '0'            
        network_ip = self.decimalConvert(network_ip)
        return self.intListToString(network_ip)

    def broadcastIp(self):
        n_bits = self.hostBits()
        broadcast_ip = self.ip_binary[:]
        for bit in range(32-n_bits,32):
            broadcast_ip[bit] = '1'
        broadcast_ip = self.decimalConvert(broadcast_ip) 
        return self.intListToString(broadcast_ip)

    def nHosts(self):
        n_bits = self.hostBits()
        return 2**n_bits - 2

    def hostsRange(self):
        min_ip = self.stringToIntList(self.networkIp())
        max_ip = self.stringToIntList(self.broadcastIp())
        min_ip[3] = min_ip[3] + 1
        max_ip[3] = max_ip[3] - 1
        return self.intListToString(min_ip), self.intListToString(max_ip)

    def isReservedIp(self):
        ip = self.ip_decimal

        if(ip[0] == 127):
            return "Localhost (loopback)"

        elif(ip[0] == 0):
            return "Software configuration"

        elif(ip[0] == 10 or (ip[0] == 172 and (ip[1] >= 16 and ip[1] <=31 )) or 
        (ip[0] == 192 and (ip[1] == 168 or ip[1] == 18 or ip[1] == 19 or (ip[1] == 0 and ip[2] == 0))) or
        (ip[0] == 100 and (ip[1] >= 64 and ip[1] <= 127 ))):
            return "Private"

        elif((ip[0] == 169 and ip[1] == 254) or (ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255)):
            return "Subnet"

        elif((ip[0] == 192 and ip[1] == 88 and ip[2] == 99) or ip[1] == 224 or (ip[1] >= 224 and ip[1] <= 239) or
        (ip[1] >= 240 and ip[1] <= 255)):
            return "Reserved"
            
        elif((ip[0] == 203 and ip[1] == 0 and ip[2] == 13) or (ip[0] == 198 and ip[1] == 51 and ip[2] == 100) or
        (ip[0] == 192 and ip[1] == 0 and ip[2] == 2)):
            return "Documentation"
            
        else:
            return "Non-reserved"

