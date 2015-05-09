cmake_minimum_required(VERSION 2.8)

project("TwoSat")

SET(CMAKE_CXX_FLAGS "-std=c++11")
SET(CMAKE_DXX_FLAGS_DEBUG "-g")

#add_executable(twoSat two_sat.cpp)

#enable_testing()

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Link "test" with what we want to test
add_executable(runTests papadimitriou_2sat.cpp papadimitriou_2sat.t.cpp)
target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)
