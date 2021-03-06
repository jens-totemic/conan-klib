import os
import shutil
from conans import ConanFile, CMake, tools


class KlibConan(ConanFile):
    name = "klib"
    version = "2019.02.08" # there's no version number, so use date
    source_subfolder = "sources"
    scm = {
        "type": "git",
        "subfolder": source_subfolder,
        "url": "https://github.com/totemic/klib.git",
        # latest commit, 2019.02.08, 
        "revision": "e5387c7e18885e66cde66a4c6cd4c897e206c3d2"
    }

    homepage = "https://github.com/attractivechaos/klib"
    description = "A standalone and lightweight C library"
    url = "https://github.com/jens-totemic/conan-klib"
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]
               }
    default_options = {"fPIC": True}
    generators = "cmake"
    exports_sources = ["lib_Makefile_add.am", "CMakeLists.txt"]

    def source(self):
        shutil.copy("CMakeLists.txt",
                    os.path.join(self.source_subfolder, "CMakeLists.txt"))

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["klib"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("c")
#			self.cpp_info.libs.append("dl")
            self.cpp_info.libs.append("pthread")
        elif self.settings.os == "FreeBSD":
#			self.cpp_info.libs.append("compat")
            self.cpp_info.libs.append("pthread")
        else:
            self.cpp_info.libs.append("c")
            self.cpp_info.libs.append("pthread")
