# grbl_pico
Build grblHAL for RPi Pico Devices

## What Is It
 * Download and build the various repos needed for RPi Pico grblHAL firmware.

## HowTo
 * Type "make"

## Dependencies
 * gmake
 * cmake >= 3.13 (https://cmake.org/)
 * ninja >= 1.9.0 (https://ninja-build.org/)

## Notes
 * Uses pico sdk 2.0.0.
 * Dependencies are downloaded and cached in the ./dl directory.

## Status
 * Builds on Debian Linux.
 * Builds for the pico-cnc board (https://github.com/phil-barrett/PicoCNC)
 * Builds for pico (rp2040) boards.
 * Does not build for pico2 (rp2350) boards (not supported by grblHAL as of 2024-09-24).

