
ovs-ofctl -O OpenFlow13 add-flow s2 in_port=1,actions=output:2

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=2,actions=output:1

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=1,actions=output:2

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=2,actions=output:1

ovs-ofctl -O OpenFlow13 add-flow s4 in_port=2,actions=output:1

ovs-ofctl -O OpenFlow13 add-flow s4 in_port=3,actions=output:1

ovs-ofctl -O OpenFlow13 add-flow s4 in_port=1,actions=output:3

ovs-ofctl -O OpenFlow13 add-flow s1 in_port=2,actions=output:1

ovs-ofctl -O OpenFlow13 add-flow s1 in_port=3,actions=output:1

ovs-ofctl -O OpenFlow13 add-group s1 group_id=5,type=select,bucket=output:2,bucket=output:3

ovs-ofctl -O OpenFlow13 add-flow s1 in_port=1,actions=group:5
