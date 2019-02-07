cmake_minimum_required(VERSION 3.5)

include(GNUInstallDirs)

add_library(common_obj OBJECT
#        bgzf.c
        kalloc.c
        keigen.c
#        kexpr.c
#        khmm.c
#        kmath.c
#        knetfile.c
#        knhx.c
#        kopen.c
        ksa.c
#        kson.c
        kstring.c
#        ksw.c
        kthread.c
#        kurl.c
        )
set_property(TARGET common_obj PROPERTY POSITION_INDEPENDENT_CODE ON)

add_library(klib STATIC $<TARGET_OBJECTS:common_obj>)

target_link_libraries(klib ${LIBS_SYSTEM})
set_target_properties(klib PROPERTIES PUBLIC_HEADER
        "kalloc.h;kavl.h;kbit.h;kbtree.h;kdq.h;keigen.h;ketopt.h;kgraph.h;khash.h;klist.h;krng.h;kseq.h;ksort.h;kstring.h;kthread.h;kvec.h")
#        bgzf.h;kexpr.h;khmm.h;kmath.h;knetfile.h;knhx.h;kson.h;ksw.h;kurl.h

install(TARGETS klib
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/klib
        COMPONENT library
        )
