"""------------------------------------------------------------------------------ 
    Descrição:    	Código responsável por importar,mostrar e exportar dados de
                    um arquivo .json contendo um IP e máscara de rede. 

    Autores:         	Matheus Batistela
  
    Data de criação:	30/11/2019
    Revisão:			05/12/2019
------------------------------------------------------------------------------"""

import json
import sys
import ipnetcalc as ipc

def getData(json_file):
        with open(json_file, "r") as read_file:
            data = json.load(read_file)

        return data["ipAddr"], data["netMask"]

def printData(ip):
    print("IP válido" if ip.isValidIp() else "IP inválido")
    print("Máscara válida" if ip.isValidMask() else "Máscara inválida")
    print("Número de bits da rede: " + str(ip.networkBits()))
    print("Número de bits de host: " + str(ip.hostBits()))
    print("Classe do IP: " + ip.ipClass())
    print("IP da rede: " + ip.networkIp())
    print("IP de broadcast: " + ip.broadcastIp())
    print("Número de hosts da rede: " + str(ip.nHosts()))
    min_host, max_host = ip.hostsRange()
    print("Faixa de hosts válidos: " + min_host + " - " + max_host)
    print("Escopo do IP: " + ip.isReservedIp())

def exportData(ip):
    min_host, max_host = ip.hostsRange()
    data_output = {
        "netBits": ip.networkBits(),
        "hostBits": ip.hostBits(), 
        "ipClass": ip.ipClass(), 
        "netIp": ip.networkIp(),
        "broadcastIp": ip.broadcastIp(),
        "hostsNumber": ip.nHosts(),
        "minHost": min_host,
        "maxHost": max_host,
        "netScope": ip.isReservedIp()
    }

    with open("net_stats.json", 'w') as output_file:
            json.dump(data_output, output_file, indent=0)


def main ():
    if(len(sys.argv) <= 1):
        print("Erro: É necessário um arquivo .json como parâmetro")
        exit()
    elif(len(sys.argv) > 2):
        print("Erro: Número de parâmetros excedido")
        exit()

    ip_address, network_mask = getData(sys.argv[1])

    ip = ipc.IpCalculator(ip_address,network_mask)

    printData(ip)
    exportData(ip)

if __name__ == "__main__":
    main();