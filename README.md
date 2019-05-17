# rmw-mininet
Repository Lab SDN Wireless and Mobile Network Course


## Preparazione ambiente
Installare i seguenti applicativi:
- [Mininet](http://mininet.org/download/) 
- [Ryu controller](https://osrg.github.io/ryu/)

### Installazione di Mininet
Il metodo più veloce per installare mininet è di utilizzare l'immagine della macchina virtuale fornita 
dagli sviluppatori di Mininet disponibile al questo link: 
[Mininet VM](https://github.com/mininet/mininet/wiki/Mininet-VM-Images). 

##### Utenti Linux
Gli utenti Linux possono anche installare Mininet nativamente, tuttavia essendo che Mininet 
deve essere eseguito come *root* è consigliabile installare Mininet tramite macchina virtuale.

##### Utenti Windows/Mac
Gli utenti Windows e Mac possono utilizzare esclusivamente l'opzione tramite macchina virtuale.

#### Configurazione della macchina virtuale
Leggere attentamente le indicazioni fornite dagli sviluppatori di Mininet 
per la configurazione della macchina virtuale a seconda del programma di virtualizzazione utilizzato 
(anche se è consigliato l'utilizzo di **VirtualBox** ) disponibili qui: [Mininet VM Setup](http://mininet.org/vm-setup-notes/).


#### Accesso alla macchina virtuale
Le credenziali di accesso di default sono:
- login: `mininet`
- password: `mininet`

##### Accesso tramite SSH
Per una più comoda interazione con la macchina virtuale è possibile accedere tramite SSH
```
ssh mininet@<ip-address>
```
l'indirizzo ip della macchina virtuale per la connessione SSH lo si ottiene digitando 
il seguente comando dalla console della macchina virtuale:
```
ifconfig eth0
```
leggendo il campo inet addr

#### Test
Per verficare che Mininet funzioni correttamente:
- accedere alla VM di Mininet
- digitare `sudo mn` 
- output
```
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2
*** Adding switches:
s1
*** Adding links:
(h1, s1) (h2, s1)
*** Configuring hosts
h1 h2
*** Starting controller
c0
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet>  
```
- digitare `pingall`
- output
```
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
mininet>  
```
### Installazione di Ryu SDN controller


```pip install repoze.lru pyyaml rfc3986 stevedore oslo.i18 greenlet```

