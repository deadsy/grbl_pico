#------------------------------------------------------------------------------

TOP = $(shell realpath .)

EXT = $(TOP)/ext
SRC = $(TOP)/src

SDK_PATH = $(EXT)/sdk
TOOLS_PATH = $(EXT)/usr/bin

#------------------------------------------------------------------------------

# pick a board
BOARD = pico
#BOARD = pico2
#BOARD = vgaboard
#BOARD = pimoroni_pico_plus2_rp2350

# pick a compiler
#COMPILER = pico_riscv_gcc
COMPILER = pico_arm_gcc
#COMPILER = pico_arm_cortex_m0plus_gcc
#COMPILER = pico_arm_cortex_m33_gcc

# pick a platform
PLATFORM = rp2040
#PLATFORM = rp2350-riscv
#PLATFORM = rp2350-arm-s

BLD_PATH = $(TOP)/build
SRC_PATH = $(TOP)/src/rp2040

.PHONY: all
all: .stamp_ext .stamp_src
	cmake -GNinja -S $(SRC_PATH) -B $(BLD_PATH) \
		-DPICO_SDK_PATH=$(SDK_PATH) \
		-DPICO_TOOLCHAIN_PATH=$(TOOLS_PATH) \
		-DPICO_PLATFORM=$(PLATFORM) \
		-DPICO_COMPILER=$(COMPILER) \
		-DPICO_BOARD=$(BOARD)
	ninja -C $(BLD_PATH)

#------------------------------------------------------------------------------

.PHONY: clean
clean:
	-rm -rf $(BLD_PATH)

.PHONY: clobber
clobber: clean
	make -C $(EXT) clean
	make -C $(SRC) clean
	-rm .stamp*

.stamp_ext:
	make -C $(EXT) all
	touch $@

.stamp_src:
	make -C $(SRC) all
	touch $@

#------------------------------------------------------------------------------
