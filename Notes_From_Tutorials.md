# Sim-Robot-Fun

## ros2 Jazzy Tutorials and Notes

### Basics

[Potential Udemy Course Series](<https://www.udemy.com/course/ros2-for-beginners/?couponCode=JUL_25>)

#### Notes
- **Nodes**: responsible for a singular, modular purpose (e.g. controlling wheel motors). Can send and receive data from other nodes via **topics**, **services**, **actions**, and **parameters**
- Messages move between nodes over **topics**. Topics do not have to be point-to-point. Many nodes can subscribe or publish to a single topic
    - messages are one-way. They go from a publisher to a subscriber
    - More information on messages can be found [here](<https://docs.ros.org/en/jazzy/Concepts/Basic/About-Interfaces.html#messages>)
- Services are request/response communication. The client (requester) is waiting for the server (responder) to make a short computation and return a result



- `ros2 run <package_name> <executable_name>` launches the executable `<executable_name>` from the package `<package_name>`. 
    - Example: `ros2 run turtlesim turtlesim_node` runs the `turtlesim_node` executable from the `turtlesim` package.
    - This does not tell you the node name, however. to do that you need to use the command `ros2 node list`
- Once you know the name of a node you can use `ros2 node info <node_name>` get the list of subscribers, publishers, services, and actions (i.e. the ROS graph connections) associated with that node 
- `ros2 topic echo <topic_name>` shows you the data being published on that topic
- `ros2 topic info <topic_name>` 

#### Key Links
- [ros2 Jazzy Basic Concepts](<https://docs.ros.org/en/jazzy/Concepts/Basic.html>)
- [Nodes Concepts Page](<https://docs.ros.org/en/jazzy/Concepts/Basic/About-Nodes.html>)

#### Tutorials Pages
- [Understanding Nodes Tutorial](<https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html>)
- [Understanding Topics Tutorial](<https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html>)

