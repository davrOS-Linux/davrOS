#!/usr/bin/env bash

echo "Commencing Stage 1: Package Installation"
pacman -Syu - < pkg.txt
echo "Stage 1 Complete: Package Installation"
