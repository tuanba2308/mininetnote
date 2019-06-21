#!/usr/bin/python

"""
#Multi controller voi 2 local controller
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
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )
    s7 = net.addSwitch( 's7' )

    info( "*** Creating hosts\n" )
    hosts1 = [ net.addHost( 'h%d' % n ) for n in ( 11, 12 ) ]
    hosts2 = [ net.addHost( 'h%d' % n ) for n in ( 21, 22 ) ]
    hosts3 = [ net.addHost( 'h%d' % n ) for n in ( 31, 32 ) ]
    hosts4 = [ net.addHost( 'h%d' % n ) for n in ( 41, 42 ) ]
    hosts5 = [ net.addHost( 'h%d' % n ) for n in ( 51, 52 ) ]
    hosts6 = [ net.addHost( 'h%d' % n ) for n in ( 61, 62 ) ]
    hosts7 = [ net.addHost( 'h%d' % n ) for n in ( 71, 72 ) ]
    c0=net.addController('c',controller=RemoteController,ip='10.102.10.242',port=6653)
    info( "*** Creating links\n" )
    for h in hosts1:
        net.addLink( s1, h,bw=7 )
    for h in hosts2:
        net.addLink( s2, h,bw=7 )
    for h in hosts3:
        net.addLink( s3, h,bw=7 )
    for h in hosts4:
        net.addLink( s4, h,bw=7 )
    for h in hosts5:
        net.addLink( s5, h,bw=7 )
    for h in hosts6:
        net.addLink( s6, h,bw=7 )
    for h in hosts7:
        net.addLink( s7, h,bw=7 )
    net.addLink( s1, s2,bw=7 )
    net.addLink( s2, s3,bw=7 )
    net.addLink( s3, s4,bw=7 )
    net.addLink( s4, s5,bw=7 )
    net.addLink( s5, s6,bw=7 )
    net.addLink( s7, s1,bw=7 )
    net.addLink( s7, s2,bw=7 )
    info( "*** Starting network\n" )
    net.build()
    net.start()

    #c0.start()
    #s1.start( [ c0 ] )
    #s2.start( [ c0 ])

    info( "*** Testing network\n" )
    net.pingAll()

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
