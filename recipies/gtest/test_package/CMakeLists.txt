cmake_minimum_required(VERSION 3.18)
project(fmtTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(gtestTest test.cpp)

find_package(GTest CONFIG REQUIRED)
target_link_libraries(gtestTest PRIVATE
    GTest::gtest
    GTest::gtest_main
)
