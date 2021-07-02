all: clean render build

.PHONY: all

# Default
clean:
	@rm -rf bitmaps themes

render: bitmapper svg
	@cd bitmapper && make install render_modern render_original

build: bitmaps
	@cd builder && make setup build


# Specific platform build
unix: clean render bitmaps
	@cd builder && make setup build_unix

windows: clean render bitmaps
	@cd builder && make setup build_windows

# Bibata Modern
modern: clean render_modern build_modern

render_modern: bitmapper svg
	@cd bitmapper && make install render_modern

build_modern: bitmaps
	@cd builder && make setup build_modern


# Bibata Original
original:clean render_original build_original

render_original: bitmapper svg
	@cd bitmapper && make install render_original

build_original: bitmaps
	@cd builder && make setup build_original


# Installation
.ONESHELL:
SHELL:=/bin/bash

src = ./themes/Bibata-Rainbow-*
local := ~/.icons
local_dest := $(local)/Bibata-Rainbow-*

root := /usr/share/icons
root_dest := $(root)/Bibata-Rainbow-*

install: themes
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing 'Bibata-Rainbow' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src) $(local)/ && echo "> Installed!"
	@else
		@echo "> Installing 'Bibata-Rainbow' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root)/ && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing 'Bibata-Rainbow' cursors from '$(local)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing 'Bibata-Rainbow' cursors from '$(root)'..."
		@sudo rm -rf $(root_dest)
	@fi

reinstall: uninstall install

# generates binaries
BIN_DIR = ../bin
prepare: bitmaps themes
	# Bitmaps
	@rm -rf bin && mkdir bin
	@cd bitmaps && zip -r $(BIN_DIR)/bitmaps.zip * && cd ..
	@cd themes
	#
	# Bibata-Modern
	#
	@tar -czvf $(BIN_DIR)/Bibata-Rainbow-Modern.tar.gz Bibata-Rainbow-Modern
	@zip -r $(BIN_DIR)/Bibata-Rainbow-Modern-Windows.zip Bibata-Rainbow-Modern-Windows
	#
	# Bibata-Original
	#
	@tar -czvf $(BIN_DIR)/Bibata-Rainbow-Original.tar.gz Bibata-Rainbow-Original
	@zip -r $(BIN_DIR)/Bibata-Rainbow-Original-Windows.zip Bibata-Rainbow-Original-Windows
	@cd ..
