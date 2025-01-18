#!/bin/python3

modules = (
    ("rp2040", "4a87c4d", "https://github.com/grblHAL/RP2040"),
    ("grbl", "5f135ed", "https://github.com/grblHAL/core"),
    ("motors", "431145a", "https://github.com/grblHAL/Plugins_motor"),
    ("spindle", "54ab2ab", "https://github.com/grblHAL/Plugins_spindle"),
    ("trinamic", "59ab5aa", "https://github.com/terjeio/Trinamic-library"),
    ("sdcard", "5350a9c", "https://github.com/grblHAL/Plugin_SD_card"),
    ("keypad", "05c2acc", "https://github.com/grblHAL/Plugin_I2C_keypad"),
    ("eeprom", "c87febc", "https://github.com/grblHAL/Plugin_EEPROM"),
    ("fans", "61d80fa", "https://github.com/grblHAL/Plugin_fans"),
    ("bluetooth", "aa0e42b", "https://github.com/grblHAL/Plugins_Bluetooth"),
    ("embroidery", "602b262", "https://github.com/grblHAL/Plugin_embroidery"),
    ("laser", "a95e09e", "https://github.com/grblHAL/Plugins_laser"),
    ("plugins", "5cf8493", "https://github.com/grblHAL/Plugins_misc"),
    ("networking", "23bb4d5", "https://github.com/grblHAL/Plugin_networking"),
    ("webui", "df8f1db", "https://github.com/grblHAL/Plugin_WebUI"),
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
