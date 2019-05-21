# rmw-mininet
Repository Lab SDN Wireless and Mobile Network Course


## Preparazione ambiente
Seguire i seguenti passi:
- Installazione dell'emulatore [Mininet](http://mininet.org) 
- Installazione del controller SDN [Ryu](https://osrg.github.io/ryu/)
- Verificare il corretto funzionamento

### Installazione di Mininet
Il metodo più veloce per installare Mininet  è di utilizzare l'immagine della macchina virtuale fornita 
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
- password sudo: `mininet`

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
Il controller SDN Ryu può essere installato sulla macchina host oppure sulla macchina virtuale


#### Opzione macchina Host
Questa opzione è preferibile in quanto permette l'utilizzo diretto di IDE di sviluppo e facilità il debug.

Suggerisco di create un nuovo ambiente python 2.7, per chi avesse installato anaconda 
può creare un nuovo ambiente ([Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)):
 utilizzando il seguente comando:

```conda create -n <nome ambiente> python=2.7 anaconda```

una volta completata l'installazione, attivate l'ambiente con il seguente comando:

```conda activate <nome ambiente>```

prodecete quindi all'installazione di Ryu e Mininet (per sfruttare le funzioni di autocompletamento dell'IDE)
- Ryu `pip install ryu`
- Mininet `pip install git+https://github.com/mininet/mininet.git `


#### Opzione macchina virtuale
Per chi volesse installare direttamente Ryu sulla macchina virtuale fornita da Mininet, 
la procedura è un po' più complicata perchè la VM fornita da Mininet si basa su Ubuntu 14.04 
mentre la documentazione di Ryu suggerisce l'utilizzo di Ubuntu 16.04+.

Installate pip

```sudo apt install python-pip```

Seguite attentamente le istruzioni presenti sulla pagina di Ryu [Getting Started](https://ryu.readthedocs.io/en/latest/getting_started.html)

Una volta termina l'installazione lanciate il controller ryu utilizando il comando:

```ryu-manager <path-to-file>/controller.py```

Qualora si verificassero degli errori riguardanti la mancanza di pacchetti installateli.

Alcuni dei pacchetti che potrebbero mancare sono elencati qui sotto (lista non esaustiva)
- repoze.lru 
- pyyaml
- rfc3986 
- stevedore 
- oslo.i18 
- greenlet

Installateli usando il comando:

```sudo pip install repoze.lru pyyaml rfc3986 stevedore oslo.i18 greenlet```


### Test di fuzionamento Mininet con controller remoto Ryu

#### Ryu su macchina host e Mininet su VM

##### ping
Al fine di verificare la connessione tra host e vm eseguite un ping test. Recuperate l'indirizzo IP impostato sull'interfaccia eth0 della macchina virtuale.

Esempio di output  `ifconfig eth0`:

```inet addr:192.168.56.101  Bcast:192.168.56.255  Mask:255.255.255.0```

- indirizzo IP VM: 192.168.56.101
- indirizzo IP host NAT: 192.168.56.1 (primo indirizzo della sottorete 192.168.56.0/24)

Dalla VM lanciate il comando: `ping 192.168.56.1`, mentre dall'host lanciate il comando: `ping 192.168.56.101`
**deve funzionare in entrambe le direzioni**. Se non funziona potrebbe essere un problema di firewall, 
cercate soluzioni rete in base al vostro sistema operativo ed eventuali sofware antivirus installati.

##### Connessione TCP

Una volta verificata la raggiungibilità IP dei due sistemi, verificare che sia possibile stabile una connessione 
TCP tra la VM e l'host 

- sulla macchina host lanciate lo script python `test_socket.py`
- sulla VM lanciare il comando `nc -vz 192.168.56.1` il risultato dovrà essere 
`Connection to 192.168.56.1 6633 port [tcp/*] succeeded!` 

Se non funziona potrebbe essere un problema di firewall, cercate soluzioni rete in base al vostro sistema operativo ed eventuali sofware antivirus installati.


##### Mininet e Ryu
- Nel file `simple_topology.py`, modificate la string `<IP address of the controller>` mettendo l'indirizzo IP della macchina host (192.168.56.1 in questo esempio)
- Copiate lo script `simple_topology.py` sulla macchina virtuale
- Sulla macchina host posizionatevi sulla cartella del file `controller_test.py` e lanciate il comando `ryu-manager controller_test.py`, il suo output sarà:
```
loading app controller_test.py
loading app ryu.controller.ofp_handler
instantiating app controller_test.py of Controller
instantiating app ryu.controller.ofp_handler of OFPHandler
```

- Sulla macchina virtuale posizionatevi sulla cartella del file `simple_topology.py` e lanciate il comando `sudo python simple_topology.py`
 che avvierà Mininet e creerà una semplicissima topologia di rete.
- Sulla console del controller Ryu dovrà comparire qualcosa del tipo

```
OFPSwitchFeatures received: datapath_id=0x0000000000000001 n_buffers=256 n_tables=254 n_ports=3capabilities=0x000000c7
```  
