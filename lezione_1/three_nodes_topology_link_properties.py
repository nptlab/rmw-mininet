from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

#importazione di TCLink
from mininet.link import TCLink

# Creazione dell'oggetto rete
# NB specificare il tipo di link
net = Mininet(link= TCLink )
# Creazione dei nodi Host
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
h3 = net.addHost( 'h3' )
# Creazione dello switch
s1 = net.addSwitch( 's1' )
# Creazione dell'handler del controller remoto che si connettera' a Ryu
c0 = net.addController( 'c0', controller=RemoteController, ip='<IP address of the controller>', port=6633 )
# Creazione dei link
net.addLink( h1, s1 , delay = '2ms')
net.addLink( h2, s1 , delay = '2ms')
net.addLink( h3, s1 , delay = '20ms')
# Attivazione della rete emulata
net.start()
# Escuzione del comando ping (fallisce)
print h1.cmd( 'ping -c1', h2.IP() )
# Apertura della Command Line Interface (CTRL + d per usire)
CLI( net )
# Distruzione della rete emulata
net.stop()
