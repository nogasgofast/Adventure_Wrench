#!/bin/bash

flatpak run --command=flathub-build org.flatpak.Builder --force-clean --disable-rofiles-fuse --user --install net.nogasgofast.adventure_wrench.yml
flatpak run --command=flatpak-builder-lint org.flatpak.Builder manifest net.nogasgofast.adventure_wrench.yml
