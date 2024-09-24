#------------------------------------------------------------------------------
# Makefile to get grblHal sources.

TOP = $(shell realpath ..)
DL_DIR = $(TOP)/dl

.PHONY: all
all: \
	.stamp_rp2040 \
	.stamp_grbl \
	.stamp_motors \
	.stamp_spindle \
	.stamp_trinamic \
	.stamp_sdcard \
	.stamp_keypad \
	.stamp_eeprom \
	.stamp_fans \
	.stamp_bluetooth \
	.stamp_embroidery \
	.stamp_laser \
	.stamp_plugins \
	.stamp_networking \
	.stamp_webui \

.PHONY: clean
clean:
	-rm -rf $(RP2040_DIR)
	-rm .stamp*

#-------------------------------------------------------------------------------
# rp2040 @ f1f67ce

RP2040_VER = f1f67ce
RP2040_URL = https://github.com/grblHAL/RP2040/tarball/$(RP2040_VER)
RP2040_FILE = rp2040-$(RP2040_VER).tar.gz
RP2040_TGZ = $(DL_DIR)/$(RP2040_FILE)
RP2040_DIR = $(TOP)/src/rp2040

$(RP2040_TGZ):
	mkdir -p $(DL_DIR)
	wget $(RP2040_URL) -O $(RP2040_TGZ)

.stamp_rp2040: .stamp_rp2040 $(RP2040_TGZ)
	mkdir -p $(RP2040_DIR)
	tar -C $(RP2040_DIR) -zxf $(RP2040_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# grbl @ 3ef6763

GRBL_VER = 3ef6763
GRBL_URL = https://github.com/grblHAL/core/tarball/$(GRBL_VER)
GRBL_FILE = grbl-$(GRBL_VER).tar.gz
GRBL_TGZ = $(DL_DIR)/$(GRBL_FILE)
GRBL_DIR = $(RP2040_DIR)/grbl

$(GRBL_TGZ):
	mkdir -p $(DL_DIR)
	wget $(GRBL_URL) -O $(GRBL_TGZ)

.stamp_grbl: .stamp_rp2040 $(GRBL_TGZ)
	mkdir -p $(GRBL_DIR)
	tar -C $(GRBL_DIR) -zxf $(GRBL_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# motors @ 87b9056

MOTORS_VER = 87b9056
MOTORS_URL = https://github.com/grblHAL/Plugins_motor/tarball/$(MOTORS_VER)
MOTORS_FILE = motors-$(MOTORS_VER).tar.gz
MOTORS_TGZ = $(DL_DIR)/$(MOTORS_FILE)
MOTORS_DIR = $(RP2040_DIR)/motors

$(MOTORS_TGZ):
	mkdir -p $(DL_DIR)
	wget $(MOTORS_URL) -O $(MOTORS_TGZ)

.stamp_motors: .stamp_rp2040 $(MOTORS_TGZ)
	mkdir -p $(MOTORS_DIR)
	tar -C $(MOTORS_DIR) -zxf $(MOTORS_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# spindle @ e74a491

SPINDLE_VER = e74a491
SPINDLE_URL = https://github.com/grblHAL/Plugins_spindle/tarball/$(SPINDLE_VER)
SPINDLE_FILE = spindle-$(SPINDLE_VER).tar.gz
SPINDLE_TGZ = $(DL_DIR)/$(SPINDLE_FILE)
SPINDLE_DIR = $(RP2040_DIR)/spindle

$(SPINDLE_TGZ):
	mkdir -p $(DL_DIR)
	wget $(SPINDLE_URL) -O $(SPINDLE_TGZ)

.stamp_spindle: .stamp_rp2040 $(SPINDLE_TGZ)
	mkdir -p $(SPINDLE_DIR)
	tar -C $(SPINDLE_DIR) -zxf $(SPINDLE_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# trinamic @ 7f98ff4

TRINAMIC_VER = 7f98ff4
TRINAMIC_URL = https://github.com/terjeio/Trinamic-library/tarball/$(TRINAMIC_VER)
TRINAMIC_FILE = trinamic-$(TRINAMIC_VER).tar.gz
TRINAMIC_TGZ = $(DL_DIR)/$(TRINAMIC_FILE)
TRINAMIC_DIR = $(RP2040_DIR)/trinamic

$(TRINAMIC_TGZ):
	mkdir -p $(DL_DIR)
	wget $(TRINAMIC_URL) -O $(TRINAMIC_TGZ)

.stamp_trinamic: .stamp_rp2040 $(TRINAMIC_TGZ)
	mkdir -p $(TRINAMIC_DIR)
	tar -C $(TRINAMIC_DIR) -zxf $(TRINAMIC_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# sdcard @ fa60b71

SDCARD_VER = fa60b71
SDCARD_URL = https://github.com/grblHAL/Plugin_SD_card/tarball/$(SDCARD_VER)
SDCARD_FILE = sdcard-$(SDCARD_VER).tar.gz
SDCARD_TGZ = $(DL_DIR)/$(SDCARD_FILE)
SDCARD_DIR = $(RP2040_DIR)/sdcard

$(SDCARD_TGZ):
	mkdir -p $(DL_DIR)
	wget $(SDCARD_URL) -O $(SDCARD_TGZ)

.stamp_sdcard: .stamp_rp2040 $(SDCARD_TGZ)
	mkdir -p $(SDCARD_DIR)
	tar -C $(SDCARD_DIR) -zxf $(SDCARD_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# keypad @ 34cc8e9

KEYPAD_VER = 34cc8e9
KEYPAD_URL = https://github.com/grblHAL/Plugin_I2C_keypad/tarball/$(KEYPAD_VER)
KEYPAD_FILE = keypad-$(KEYPAD_VER).tar.gz
KEYPAD_TGZ = $(DL_DIR)/$(KEYPAD_FILE)
KEYPAD_DIR = $(RP2040_DIR)/keypad

$(KEYPAD_TGZ):
	mkdir -p $(DL_DIR)
	wget $(KEYPAD_URL) -O $(KEYPAD_TGZ)

.stamp_keypad: .stamp_rp2040 $(KEYPAD_TGZ)
	mkdir -p $(KEYPAD_DIR)
	tar -C $(KEYPAD_DIR) -zxf $(KEYPAD_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# eeprom @ fd157b3

EEPROM_VER = fd157b3
EEPROM_URL = https://github.com/grblHAL/Plugin_EEPROM/tarball/$(EEPROM_VER)
EEPROM_FILE = eeprom-$(EEPROM_VER).tar.gz
EEPROM_TGZ = $(DL_DIR)/$(EEPROM_FILE)
EEPROM_DIR = $(RP2040_DIR)/eeprom

$(EEPROM_TGZ):
	mkdir -p $(DL_DIR)
	wget $(EEPROM_URL) -O $(EEPROM_TGZ)

.stamp_eeprom: .stamp_rp2040 $(EEPROM_TGZ)
	mkdir -p $(EEPROM_DIR)
	tar -C $(EEPROM_DIR) -zxf $(EEPROM_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# fans @ 3f261aa

FANS_VER = 3f261aa
FANS_URL = https://github.com/grblHAL/Plugin_fans/tarball/$(FANS_VER)
FANS_FILE = fans-$(FANS_VER).tar.gz
FANS_TGZ = $(DL_DIR)/$(FANS_FILE)
FANS_DIR = $(RP2040_DIR)/fans

$(FANS_TGZ):
	mkdir -p $(DL_DIR)
	wget $(FANS_URL) -O $(FANS_TGZ)

.stamp_fans: .stamp_rp2040 $(FANS_TGZ)
	mkdir -p $(FANS_DIR)
	tar -C $(FANS_DIR) -zxf $(FANS_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# bluetooth @ 8298c1b

BLUETOOTH_VER = 8298c1b
BLUETOOTH_URL = https://github.com/grblHAL/Plugins_Bluetooth/tarball/$(BLUETOOTH_VER)
BLUETOOTH_FILE = bluetooth-$(BLUETOOTH_VER).tar.gz
BLUETOOTH_TGZ = $(DL_DIR)/$(BLUETOOTH_FILE)
BLUETOOTH_DIR = $(RP2040_DIR)/bluetooth

$(BLUETOOTH_TGZ):
	mkdir -p $(DL_DIR)
	wget $(BLUETOOTH_URL) -O $(BLUETOOTH_TGZ)

.stamp_bluetooth: .stamp_rp2040 $(BLUETOOTH_TGZ)
	mkdir -p $(BLUETOOTH_DIR)
	tar -C $(BLUETOOTH_DIR) -zxf $(BLUETOOTH_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# embroidery @ 1e556ac

EMBROIDERY_VER = 1e556ac
EMBROIDERY_URL = https://github.com/grblHAL/Plugin_embroidery/tarball/$(EMBROIDERY_VER)
EMBROIDERY_FILE = embroidery-$(EMBROIDERY_VER).tar.gz
EMBROIDERY_TGZ = $(DL_DIR)/$(EMBROIDERY_FILE)
EMBROIDERY_DIR = $(RP2040_DIR)/embroidery

$(EMBROIDERY_TGZ):
	mkdir -p $(DL_DIR)
	wget $(EMBROIDERY_URL) -O $(EMBROIDERY_TGZ)

.stamp_embroidery: .stamp_rp2040 $(EMBROIDERY_TGZ)
	mkdir -p $(EMBROIDERY_DIR)
	tar -C $(EMBROIDERY_DIR) -zxf $(EMBROIDERY_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# laser @ 3b25965

LASER_VER = 3b25965
LASER_URL = https://github.com/grblHAL/Plugins_laser/tarball/$(LASER_VER)
LASER_FILE = laser-$(LASER_VER).tar.gz
LASER_TGZ = $(DL_DIR)/$(LASER_FILE)
LASER_DIR = $(RP2040_DIR)/laser

$(LASER_TGZ):
	mkdir -p $(DL_DIR)
	wget $(LASER_URL) -O $(LASER_TGZ)

.stamp_laser: .stamp_rp2040 $(LASER_TGZ)
	mkdir -p $(LASER_DIR)
	tar -C $(LASER_DIR) -zxf $(LASER_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# plugins @ 0d081ae

PLUGINS_VER = 0d081ae
PLUGINS_URL = https://github.com/grblHAL/Plugins_misc/tarball/$(PLUGINS_VER)
PLUGINS_FILE = plugins-$(PLUGINS_VER).tar.gz
PLUGINS_TGZ = $(DL_DIR)/$(PLUGINS_FILE)
PLUGINS_DIR = $(RP2040_DIR)/plugins

$(PLUGINS_TGZ):
	mkdir -p $(DL_DIR)
	wget $(PLUGINS_URL) -O $(PLUGINS_TGZ)

.stamp_plugins: .stamp_rp2040 $(PLUGINS_TGZ)
	mkdir -p $(PLUGINS_DIR)
	tar -C $(PLUGINS_DIR) -zxf $(PLUGINS_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# networking @ 5fd1e25

NETWORKING_VER = 5fd1e25
NETWORKING_URL = https://github.com/grblHAL/Plugin_networking/tarball/$(NETWORKING_VER)
NETWORKING_FILE = networking-$(NETWORKING_VER).tar.gz
NETWORKING_TGZ = $(DL_DIR)/$(NETWORKING_FILE)
NETWORKING_DIR = $(RP2040_DIR)/networking

$(NETWORKING_TGZ):
	mkdir -p $(DL_DIR)
	wget $(NETWORKING_URL) -O $(NETWORKING_TGZ)

.stamp_networking: .stamp_rp2040 $(NETWORKING_TGZ)
	mkdir -p $(NETWORKING_DIR)
	tar -C $(NETWORKING_DIR) -zxf $(NETWORKING_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
# webui @ 1981aef

WEBUI_VER = 1981aef
WEBUI_URL = https://github.com/grblHAL/Plugin_WebUI/tarball/$(WEBUI_VER)
WEBUI_FILE = webui-$(WEBUI_VER).tar.gz
WEBUI_TGZ = $(DL_DIR)/$(WEBUI_FILE)
WEBUI_DIR = $(RP2040_DIR)/webui

$(WEBUI_TGZ):
	mkdir -p $(DL_DIR)
	wget $(WEBUI_URL) -O $(WEBUI_TGZ)

.stamp_webui: .stamp_rp2040 $(WEBUI_TGZ)
	mkdir -p $(WEBUI_DIR)
	tar -C $(WEBUI_DIR) -zxf $(WEBUI_TGZ) --strip-components 1
	touch $@

#-------------------------------------------------------------------------------
