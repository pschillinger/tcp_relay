cmake_minimum_required(VERSION 2.8.3)
project(tcp_relay)
# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED)
catkin_package()
catkin_python_setup()

install(PROGRAMS bin/relay_topics
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)