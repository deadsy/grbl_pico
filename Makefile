
TOP = $(shell realpath .)

EXT = $(TOP)/ext

SDK_PATH = $(EXT)/sdk
TOOLS_PATH = $(EXT)/usr/bin
PICOTOOL = $(EXT)/usr/lib/cmake/picotool
PIOASM = $(EXT)/usr/lib/cmake/pioasm

BLD_PATH = $(TOP)/build

.PHONY: all
all: .stamp_ext

.PHONY: clean
clean:
	-rm -rf $(BLD_PATH)

.PHONY: clobber
clobber: clean
	make -C $(EXT) clean
	-rm .stamp_ext

.stamp_ext:
	make -C $(EXT) all
	touch $@
