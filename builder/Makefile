all: setup build

bitmaps_dir = "../bitmaps"

.PHONY: all

.ONESHELL:
SHELL:=/bin/bash

X_SIZES ?=22 24 28 32 40 48 56 64 72 80 88 96
WIN_CANVAS_SIZE ?= 32
WIN_SIZE ?= 24

setup:
	@python3 -m pip install clickgen --user

build: build_modern build_original

build_modern: build.py
	@python3 build.py -p "$(bitmaps_dir)/Bibata-Rainbow-Modern" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)

build_original: build.py
	@python3 build.py -p "$(bitmaps_dir)/Bibata-Rainbow-Original" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)


build_unix: build_modern_unix build_original_unix

build_modern_unix: build.py
	@python3 build.py unix -p "$(bitmaps_dir)/Bibata-Rainbow-Modern" --xsizes $(X_SIZES)

build_original_unix: build.py
	@python3 build.py unix -p "$(bitmaps_dir)/Bibata-Rainbow-Original" --xsizes $(X_SIZES)


build_windows: build_modern_windows build_original_windows

build_modern_windows: build.py
	@python3 build.py windows -p "$(bitmaps_dir)/Bibata-Rainbow-Modern" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)

build_original_windows: build.py
	@python3 build.py windows -p "$(bitmaps_dir)/Bibata-Rainbow-Original" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
