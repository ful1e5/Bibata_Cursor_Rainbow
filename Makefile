all: clean render build

unix: clean render bitmaps
	@cd builder && make setup build_unix

windows: clean render bitmaps
	@cd builder && make setup build_windows

.PHONY: all

clean:
	@rm -rf bitmaps themes
	
modern: clean render_modern build_modern
original:clean render_original build_original

#
# Render Bibata Bitmaps
#

render: bitmapper svg
	@cd bitmapper && make install render_modern render_original

render_original: bitmapper svg
	@cd bitmapper && make install render_original

render_modern: bitmapper svg
	@cd bitmapper && make install render_modern

#
# Build Bibata Unix & Windows cursors
#

build: bitmaps
	@cd builder && make setup build

build_unix: bitmaps
	@rm -rf themes
	@cd builder && make setup build_unix

build_windows: bitmaps
	@rm -rf themes
	@cd builder && make setup build_windows

build_modern: bitmaps
	@cd builder && make setup build_modern

build_original: bitmaps
	@cd builder && make setup build_original

#
# Installation
#

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
