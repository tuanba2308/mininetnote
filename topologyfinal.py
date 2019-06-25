#!/usr/bin/python

"""
#limit sw-sw
"""


from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, TCLink

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=RemoteController, switch=OVSSwitch,link=TCLink )
    
    info( "*** Creating (reference) controllers\n" )
    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    
    info( "*** Creating hosts\n" )
    host11 = net.addHost( 'h11')
    host12 = net.addHost( 'h12')
    host21 = net.addHost( 'h21')
    host22 = net.addHost( 'h22')
    c0=net.addController('c',controller=RemoteController,ip='10.102.10.242',port=6653)
    info( "*** Creating links\n" )

    net.addLink( s1, host11 )
    net.addLink( s1, host12 )
    net.addLink( s2, host21 )
    net.addLink( s2, host22 )
    net.addLink( s1, s2 ,bw = 0.1)
    
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
