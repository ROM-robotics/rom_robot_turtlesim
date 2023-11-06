from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    turtle_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="turtlesim"
    )
    nodes = [
        turtle_node,
    ]

    return LaunchDescription(nodes)
