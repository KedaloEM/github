cmake_minimum_required(VERSION 3.3)
project(thread)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")

set(SOURCE_FILES main.cpp)
add_executable(thread ${SOURCE_FILES})