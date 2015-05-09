cmake_minimum_required(VERSION 2.8)

project("TwoSat")

SET(CMAKE_CXX_FLAGS "-std=c++11")
SET(CMAKE_DXX_FLAGS_DEBUG "-g")

#add_executable(twoSat two_sat.cpp)

#enable_testing()

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
set(SRC_FILES 2sat.cpp 2sat.h 2sat.t.cpp)

# Link "test" with what we want to test
add_executable(runTests two_sat.cpp two_sat.t.cpp)
target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)
