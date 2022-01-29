# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added

- Bibata-Zebra link added
- pling link updated inside PLING.bbcode
- Add symlink for `top_left_arrow` cursor ful1e5/BreezeX_Cursor#10 ful1e5/BreezeX_Cursor#11
- Uninstall docs ful1e5/apple_cursor#79 ful1e5/apple_cursor#80

### Changed

- sponsorships updated
- minimal docs inside `README.md`
- Fix `None` value warning in `builder/symlinks.py`
- Github Action renamed to `build`

## [v1.1.2] - 25 Jul 2021

### Added

- Support button inside `PLING.bbcode` product page
- `make prepare` command for preparing bibata binaries
- `pyrightconfig.json` init

### Changed

- Removed **clean** target from `builder/Makefile`
- Compact code inside `builder/*`
- Remove `setup.py`
- Builder code moved to `src`
- Import `src` module directly inside `build.py`
- `Makefile` build commands re-arrange with groups
- Dynamic determine **Windows canvas size** on **Windows cursor size** inside `build.py`

## [v1.1.1] - 30 Mar 2021

### Added

- pling product page docs
- **2 space** format in `bitmapper`
- `brbpkg` installed as user in **make** command
- Supports clickgen v1.1.9
- `PNGProvider` imported from `clickgen.util`
- `builder/brbpkg` docstring in _reST_ with sphinx supports

### Changed

- python3 `virtualenv` commands removed from `builder/Makefile`
- Removed `builder/brbpkg/extra.py` module (all funtions _imported_ from `clickgen`)
- clean builder cache on every **make** commands

## [v1.1.0] - 04 Mar 2021

### Added

- Add Windows support
- `.svg` files separated to `<root>/svg`
- Customizable Windows & UNIX cursors
- Easy build system with `Make` supports
- Make docs in[README.md](./README.md#manual-build)
- use builtin clickgen WinPackager for Windows package
- Constant frames in animated cursors
- Smooth animation in Windows cursors
- `install` & `uninstall` with `make` commands

### Changed

- Individual cursor build with clickgen v1.1.8 #93
- puppeteer 'single-process' args removed
- All Bitmapping code structured in `bitmapper` directory
- builder code structured inside `builder` directory
- `builder` package renamed to `brbpkg`
- Symblinks provided by `brbpkg`(new Bibata Rainbow builder)
- Automatic build environment setup with `make`
- Logging file removed
- Fix dnf runtime requirements packages ful1e5/apple_cursor#34
- Fix grabbing cursors symlinks #87
- Fix Cursors not available for Login Window in Linux Mint 20 #88
- Dirty pixel in `move` cursor fixed #94

## [v1.0.0] - 17 Nov 2020

> First version of **Bibata_Cursor_Rainbow** is published on **Bibata_Cursor** repo

### Added

- **Bibata Rainbow** (semi-animated) cursors. **#55**
- **Bibata Rainbow** workflow file added `bibata-rainbow-ci.yml`
- **semi-animated** cursors `.svg` parsing support in `bibata-core`
- `PLING.bbcode` for Bibata Rainbow
- Tagging guid in [CHANGELOG.md](./CHANGELOG.md#tags)
- Bibata Rainbow's **branding** assets in `packages/rainbow/src/svgs/branding`

### Changed

- `build` workflow changed to `bibata-ci`
- **Bibata** workflow file names changed to `bibata-ci.yml` & `bibata-pr.yml`
- Optimize **BitmapsGenerator** browser.

[unreleased]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/compare/v1.1.2...main
[v1.1.2]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/compare/v1.1.2...v1.1.1
[v1.1.1]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/compare/v1.1.1...v1.1.0
[v1.1.0]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/tree/v1.1.0
[v1.0.0]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.3...v1.0.0.br
