# Franka Lock Unlock (ROS2)

Locking and unlocking of Franka Emika Panda joint brakes programmatically. Open or close all joint locks either from the command-line, or from any Python program.

Also supports the activation of the Franka Control Interface (FCI) and other options.

## Problem Description

While the Franka Panda is a great robot for research and industrial use cases, it lacks the option of unlocking or locking its joints from a different source other than the Franka Desk Web UI. However, this is crucial if you want to automate the entire startup and shutdown phase of the robot. That is now possible with the introduction of this package.

## Command-Line Usage
Ensure to have python3 installed.

```
usage: ./__init__.py [-h] [-u] [-l] [-w] [-r] [-p] [-c] [-i] hostname username password

positional arguments:
  hostname          The Franka Desk IP address or hostname, for example "1.2.3.4".
  username          The Franka Desk username, usually "admin".
  password          The Franka Desk password.

optional arguments:
  -h, --help        show this help message and exit
  -u, --unlock      Unlock the brakes. Otherwise, lock them.
  -l, --relock      Relock the brakes on exit.
  -w, --wait        Wait in case the robot web UI is currently in use.
  -r, --request     Request control by confirming physical access to the robot in case the robot web UI is currently in use.
  -p, --persistent  Keep the connection to the robot open persistently.
  -c, --fci         Activate the FCI.
  -i, --home        Home the gripper.
```

## ROS Package

This repository exports a ROS package. This is useful for starting up the robot and FCI by means of a single launch file that also spawns the `franka_ros` interface at the same time. It will speed up your entire robot workflow dramatically.

The ROS package can be installed and invoked by the following commands.

### Installation

```
git clone https://github.com/drewskoots/franka_lock_unlock
colcon build --packages-select franka_lock_unlock
```

### Simple Usage

```
ros2 run franka_lock_unlock __init__.py <PARAMS>
```

### Advanced Usage

If you want to launch the `franka_control` node while unlocking the joints, ensure to add the `respawn=true` parameter to the node tag, such that the control node retries to connect to the robot until all joints have been fully unlocked and the FCI has been activated.

<pre>
&lt;node name="franka_control" pkg="franka_control" type="franka_control_node" output="screen" <b>respawn="true"</b> /&gt;
</pre>

The following launch file unlocks the joints, activates the FCI and connects to the robot via ROS. Also, it allows to re-lock the brakes automatically as soon as the launch file is exited via `SIGINT` or `SIGTERM` (`CTRL+C`).

```
roslaunch franka_lock_unlock franka_start.launch hostname:=<HOSTNAME> username:=<USERNAME> password:=<PASSWORD>
```
