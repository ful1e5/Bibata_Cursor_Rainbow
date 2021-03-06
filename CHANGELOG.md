# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added

- pling product page docs

## [Bibata Rainbow v1.1.0] - 04 Mar 2021

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

## [Bibata Rainbow v1.0.0] - 17 Nov 2020

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

[unreleased]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/compare/v1.1.0...main
[bibata rainbow v1.1.0]: https://github.com/ful1e5/Bibata_Cursor_Rainbow/compare/v1.1.0...main
[bibata rainbow v1.0.0]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.3...v1.0.0.br
