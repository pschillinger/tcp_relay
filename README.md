# TCP Relay
Very basic relay of ROS messages from one roscore to another roscore via TCP.

## Usage

Subscribe to messages in the network of roscore 1:

    roscore

    rosrun tcp_relay sub localhost:11401 /my_topic std_msgs/String

Publish these messages in the network of roscore 2:

    roscore -p 11312
    
    ROS_MASTER_URI=http://localhost:11312
    rosrun tcp_relay pub localhost:11401 /my_topic std_msgs/String
    
## Remarks

- Topic names can be different to realize remapping
- TCP socket is created on the machine of `pub`, so IP/hostname needs to be set accordingly
