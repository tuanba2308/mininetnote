#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, TCLink

def ControllerNet():

    net = Mininet( controller=RemoteController, switch=OVSSwitch,link=TCLink )
    
    info( "*** Creating (reference) controllers\n" )
    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )
    s7 = net.addSwitch( 's7' )
    info( "*** Creating hosts\n" )
    host11 = net.addHost( 'h11') #h11
    host12 = net.addHost( 'h12') #h12
    host4 = net.addHost('h4') #h4
    host61 = net.addHost('Server1') #h61
    host62 = net.addHost('Server2') #h62
    host63 = net.addHost('Decoy1') #h63
    host64 = net.addHost('Decoy2') #h64
    host71 = net.addHost('Decoy3') #h71
    host72 = net.addHost('Decoy4') #h72
    host21 = net.addHost('Client') #h21
    c0=net.addController('c',controller=RemoteController,ip='10.102.10.242',port=6653)
    info( "*** Creating links\n" )

    net.addLink( s1, host11 )
    net.addLink( s1, host12 )
    net.addLink( s2, host21 )
    net.addLink( s4, host4  )
    net.addLink( s7, host71 )
    net.addLink( s7, host72 )
    net.addLink( s6, host61 )
    net.addLink( s6, host62 )
    net.addLink( s6, host63 )
    net.addLink( s6, host64 )
    #net.addLink( s1, s2 ,bw = 0.1)
    net.addLink( s1, s2)
    net.addLink( s2, s3)
    net.addLink( s2, s5)
    net.addLink( s3, s4)
    net.addLink( s4, s5)
    net.addLink( s4, s6, bw=0.1)
    net.addLink( s4, s7, bw=0.1)
    net.addLink( s6, s7, )
    info( "*** Starting network\n" )
    net.build()
    net.start()

    #c0.start()
    #s1.start( [ c0 ] )
    #s2.start( [ c0 ])

    info( "*** Testing network\n" )
    #net.pingAll()

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
