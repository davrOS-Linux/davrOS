#!/usr/bin/env bash

echo "[davrOS]: stage 1: Package Upgrades"

# install all the packages listed in the pkg.txt file using pacman
pacman -Syu --needed - < pkg.txt
