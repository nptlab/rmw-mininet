from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

net = Mininet()
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
s1 = net.addSwitch( 's1' )
c0 = net.addController( 'c0', controller=RemoteController, ip='192.168.56.1', port=6633 )
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.start()
print h1.cmd( 'ping -c1', h2.IP() )
CLI( net )
net.stop()
