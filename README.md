# Dependencies

- Ubuntu 22.04 jammy jellyfisch
- Ros2 humble hawskbill installation guide https://docs.ros.org/en/humble/Installation.html
- Configuring environment https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html
- Python version 3.10.12
- Pip version 22.0.2
- Setuptools-75.6.0 
- Wheel 0.45.1
- Numpy 2.2.0
- Pandas 2.2.3
- Large File Storage:
  - Sudo apt install git-lfs
  - Go into folder with src-> git lfs install -> git lfs pull
- Gazebo Harmonic:
  - wget https://gazebosim.org/repos/gz-archive-keyring.gpg -O - | sudo apt-key add –
  - sudo sh -c 'echo "deb [arch=amd64] http://packages.osrfoundation.org/gz/gz-ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/gazebo-stable.list'
  - sudo apt update
  - sudo apt install gz-harmonic
  - apt-get install ros-humble-ros-gzharmonic

- Nav2 msgs:
  - sudo apt-get install ros-humble-nav2-msgs
- Rosdep
  - colcon build --symlink-install --install-base ./install


