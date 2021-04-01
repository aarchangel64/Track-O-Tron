cmake_minimum_required(VERSION 3.10)

project(Track-O-Tron)

add_subdirectory(src)
add_subdirectory(lib/serial)
add_executable(track-o-tron src/main.cpp)

# add_library(track-o-tron serial/serial.h)
target_link_libraries(track-o-tron PUBLIC serial)
target_include_directories(track-o-tron PUBLIC
  "${PROJECT_BINARY_DIR}"
  "${PROJECT_SOURCE_DIR}/lib/serial"
  )
