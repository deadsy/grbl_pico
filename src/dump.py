#!/bin/python3

modules = (
    ("rp2040", "f1f67ce", "https://github.com/grblHAL/RP2040"),
    ("grbl", "3ef6763", "https://github.com/grblHAL/core"),
    ("motors", "87b9056", "https://github.com/grblHAL/Plugins_motor"),
    ("spindle", "e74a491", "https://github.com/grblHAL/Plugins_spindle"),
    ("trinamic", "7f98ff4", "https://github.com/terjeio/Trinamic-library"),
    ("sdcard", "fa60b71", "https://github.com/grblHAL/Plugin_SD_card"),
    ("keypad", "34cc8e9", "https://github.com/grblHAL/Plugin_I2C_keypad"),
    ("eeprom", "fd157b3", "https://github.com/grblHAL/Plugin_EEPROM"),
    ("fans", "3f261aa", "https://github.com/grblHAL/Plugin_fans"),
    ("bluetooth", "8298c1b", "https://github.com/grblHAL/Plugins_Bluetooth"),
    ("embroidery", "1e556ac", "https://github.com/grblHAL/Plugin_embroidery"),
    ("laser", "3b25965", "https://github.com/grblHAL/Plugins_laser"),
    ("plugins", "0d081ae", "https://github.com/grblHAL/Plugins_misc"),
    ("networking", "5fd1e25", "https://github.com/grblHAL/Plugin_networking"),
    ("webui", "1981aef", "https://github.com/grblHAL/Plugin_WebUI"),
)

comment = "#" + "".join(("-",) * 79)


def main():
    for name, rev, url in modules:
        print(f"\t.stamp_{name} \\")

    for name, rev, url in modules:
        ver_name = f"{name.upper()}_VER"
        url_name = f"{name.upper()}_URL"
        file_name = f"{name.upper()}_FILE"
        tgz_name = f"{name.upper()}_TGZ"
        dir_name = f"{name.upper()}_DIR"
        url = url + f"/tarball/$({ver_name})"

        print(comment)
        print(f"# {name} @ {rev}\n")
        print(f"{ver_name} = {rev}")
        print(f"{url_name} = {url}")
        print(f"{file_name} = {name}-$({ver_name}).tar.gz")
        print(f"{tgz_name} = $(DL_DIR)/$({file_name})")
        if name == "rp2040":
            print(f"{dir_name} = $(TOP)/src/{name}")
        else:
            print(f"{dir_name} = $(RP2040_DIR)/{name}")
        print()

        print(f"$({tgz_name}):")
        print("\tmkdir -p $(DL_DIR)")
        print(f"\twget $({url_name}) -O $({tgz_name})")
        print()

        print(f".stamp_{name}: $({tgz_name})")
        print(f"\tmkdir -p $({dir_name})")
        print(f"\ttar -C $({dir_name}) -zxf $({tgz_name}) --strip-components 1")
        print("\ttouch $@")
        print()

    print(comment)


main()
