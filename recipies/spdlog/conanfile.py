import os

from conans import ConanFile, tools, CMake


class FmtConan(ConanFile):
    name = "spdlog"
    version = "1.8.2"
    license = "The MIT License (MIT) Copyright (c) 2016 Gabi Melman."
    author = "Gabi Melman"
    url = "https://github.com/gabime/spdlog.git"
    description = "Very fast, header-only/compiled, C++ logging library."
    topics = ("c++", "logging", "performance")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "header_only": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "header_only": False, "fPIC": True}

    def source(self):
        self.run("git clone {0}".format(self.url))
        self.run("cd spdlog && git checkout tags/v{0} -b v{0}-branch".format(self.version))

    def build(self):
        cmake_release = CMake(self, build_type="Release")
        cmake_release.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"
        cmake_release.configure(source_folder="./spdlog")
        cmake_release.build()
        cmake_release.install()

        cmake_debug = CMake(self, build_type="Debug")
        cmake_debug.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"
        cmake_debug.configure(source_folder="./spdlog")
        cmake_debug.build()
        cmake_debug.install()

    def package(self):
        pass

    def package_id(self):
        pass
