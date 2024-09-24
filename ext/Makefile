#------------------------------------------------------------------------------
# Makefile to get and build external dependencies.

TOP = $(shell realpath ..)
DL_DIR = $(TOP)/dl
USR_DIR = $(TOP)/ext/usr

.PHONY: all
all: .stamp_sdk .stamp_gnu_arm

.PHONY: clean
clean:
	-rm -rf $(USR_DIR)
	-rm -rf $(SDK_DIR)
	-rm .stamp*

#------------------------------------------------------------------------------
# pico sdk

SDK_VER = 1.5.0
SDK_URL = https://github.com/raspberrypi/pico-sdk/releases/download/1.5.0/sdk$(SDK_VER)-with-submodules.zip
SDK_FILE = pico-sdk-$(SDK_VER).zip
SDK_ZIP = $(DL_DIR)/$(SDK_FILE)
SDK_DIR = $(TOP)/ext/sdk

$(SDK_ZIP):
	mkdir -p $(DL_DIR)
	wget $(SDK_URL) -O $(SDK_ZIP)

.stamp_sdk: $(SDK_ZIP)
	mkdir -p $(SDK_DIR)
	unzip -q -d $(SDK_DIR) $(SDK_ZIP)
	touch $@

#------------------------------------------------------------------------------
# gnu arm tools

GNU_ARM_VER = 13.3.rel1
GNU_ARM_URL = https://developer.arm.com/-/media/Files/downloads/gnu/$(GNU_ARM_VER)/binrel/arm-gnu-toolchain-$(GNU_ARM_VER)-x86_64-arm-none-eabi.tar.xz
GNU_ARM_FILE = arm-gnu-toolchain-$(GNU_ARM_VER)-x86_64-arm-none-eabi.tar.xz
GNU_ARM_TXZ = $(DL_DIR)/$(GNU_ARM_FILE)

$(GNU_ARM_TXZ):
	mkdir -p $(DL_DIR)
	wget $(GNU_ARM_URL) -O $(GNU_ARM_TXZ)

.stamp_gnu_arm: $(GNU_ARM_TXZ)
	mkdir -p $(USR_DIR)
	tar -C $(USR_DIR) -Jxf $(GNU_ARM_TXZ) --strip-components 1
	touch $@

#------------------------------------------------------------------------------
