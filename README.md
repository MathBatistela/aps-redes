<!-- Este projeto pode ser encontrado no GitHub atráves deste link: https://github.com/MathBatistela/aps_redes -->

# Descrição

O software consiste em, dado um certo IP e máscara de rede:
 * Validá-los
 
 * Retornar o número de bits de rede e host

 * A classe do IP
 
 * O IP da rede e o IP de broadcast
 
 * A faixa válida para IP's de host      
 
 * E o escopo a qual esse IP pertence (privado, loopback, etc..).          

# Execução

Crie, ou altere um arquivo .JSON com o seguinte padrão:

    { 
    "ipAddr": "192.168.0.1",
    "netMask": "255.255.255.0"
    }

Onde,

* ipAddr = Endereço de IP
* netMask = Máscara de IP

Logo, execute o seguinte comando:

```
python3 main.py nome_do_arquivo.json
```

# Exemplo de uso

Arquivo data.json:

    {
    "ipAddr": "192.168.0.1",
    "netMask": "255.255.255.0"
    }

Comando:
```
python3 main.py data.json
```

Output do terminal:
```
IP válido
Máscara válida
Número de bits da rede: 24
Número de bits de host: 8
Classe do IP: C
IP da rede: 192.168.0.0
IP de broadcast: 192.168.0.255
Número de hosts da rede: 254
Faixa de hosts válidos: 192.168.0.1 - 192.168.0.254
Escopo do IP: Private
```

Arquivo exportado net_stats.json:
```
{
"netBits": 24,
"hostBits": 8,
"ipClass": "C",
"netIp": "192.168.0.0",
"broadcastIp": "192.168.0.255",
"hostsNumber": 254,
"minHost": "192.168.0.1",
"maxHost": "192.168.0.254",
"netScope": "Private"
}
```
