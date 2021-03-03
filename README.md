<!-- Branding -->

<p align="center">
  <img src="./svg/branding/logo.svg" width="20%">
</p>

<p align="center">
  <b>'Semi-Animated' Bibata cursors with rainbow colors</b> 
</p>

<!-- Badges -->

<p align="center">

  <!-- First Row -->

  <a href="https://github.com/ful1e5/Bibata_Cursor_Rainbow/actions">
    <img alt="GitHub Action Build" src="https://github.com/ful1e5/Bibata_Cursor_Rainbow/actions/workflows/ci.yml/badge.svg"/>
  </a>

  <!-- Second Row -->

  </br >
  <a href="https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html">
    <img alt="npm type definitions" src="https://img.shields.io/npm/types/typescript">
  </a>

  <a href="https://github.com/ful1e5/clickgen">
    <img alt="Clickgen" src="https://img.shields.io/badge/theme%20builder-clickgen-FD0542" />
  </a>
  
  
  <!-- Third Row -->

  </br >
  <a href="https://github.com/ful1e5/Bibata_Cursor_Rainbow/blob/main/LICENSE" >
    <img alt="License" src="https://img.shields.io/github/license/ful1e5/Bibata_Cursor_Rainbow?color=0081FB" />
  </a>

  <a href="https://github.com/ful1e5/Bibata_Cursor_Rainbow/releases" >
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ful1e5/Bibata_Cursor_Rainbow">
  </a>
  
  
  <!-- Fourth Row -->

  <br />
  <a href="https://www.pling.com/p/1445634/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Linux-grey?logo=linux" />
  </a>

  <a href="https://www.pling.com/p/1445634/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Windows-blue?logo=windows" />
  </a>

  <!-- Fifth Row -->

  <br />
  <a href="https://github.com/ful1e5">
    <img alt="Made By Kaiz"  src="https://kaiz.vercel.app/api/badge" width="133" />
  </a>

</p>

<!-- Intro -->

# Bibata Styles

- **Bibata Original :** Sharp edge Bibata Cursors
- **Bibata Modern :** Round edge Bibata Cursors

# Cursor Sizes

<kbd>22</kbd>
<kbd>24</kbd>
<kbd>28</kbd>
<kbd>32</kbd>
<kbd>40</kbd>
<kbd>48</kbd>
<kbd>56</kbd>
<kbd>64</kbd>
<kbd>72</kbd>
<kbd>80</kbd>
<kbd>88</kbd>
<kbd>96</kbd>

<!-- Preview -->

## Preview

<p align="center">
  <img title="Bibata Rainbow" width="90%" src="./svg/branding/preview.svg">
  </br>
  <sub>Bibata Rainbow</sub>
</p>

## Quick install

<p align="center">
  <a href="https://www.pling.com/p/1445634/#files-panel" >
    <img title="Bibata Pling Store" width="40%" src="https://imgur.com/VxSgrWw.png">
  </a>
</p>

## Manual Install

Latest `Stable` & `Development` releases can be downloaded from [Here](https://github.com/ful1e5/Bibata_Cursor_Rainbow/releases)

#### Linux/X11

```bash
# extract `Bibata-Rainbow.tar.gz`
tar -xvf Bibata-Rainbow.tar.gz

# For local users
mv Bibata_Rainbow-* ~/.icons/

# For all users
sudo mv Bibata_Rainbow-* /usr/share/icons/
```

#### Windows

1. unzip `.zip` file
2. Open unziped directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel_ > _Personalization and Appearance_ > _Change mouse pointers_, and select **Bibata Rainbow Cursors**.
5. Click '**Apply**'.

<!-- Build Dependencies -->

# Dependencies

## External Libraries

- libxcursor-dev
- libx11-dev
- libpng-dev (<=1.6)

#### Install External Libraries

##### macOS

```bash
brew install --cask xquartz
brew install libpng
```

##### Debain/ubuntu

```bash
sudo apt install libx11-dev libxcursor-dev libpng-dev
```

##### ArchLinux/Manjaro

```bash
sudo pacman -S libx11 libxcursor libpng
```

##### Fedora/Fedora Silverblue/CentOS/RHEL

```bash
sudo dnf install libX11-devel libXcursor-devel libpng-devel
```

## Build Dependencies

- [gcc](https://gcc.gnu.org/install/)
- [make](https://www.gnu.org/software/make/)
- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/)
- [python](https://www.python.org/downloads/) (<=3.8)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)

## Build From Scratch

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** & **dev** branch) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **ci**. GitHub **Actions** available inside [.github/workflows](https://github.com/ful1e5/Bibata_Cursor_Rainbow)/tree/main/.github/workflows) directory.

### Manual Build

> Check **[Makefile](./Makefile)** for more targets.

```bash
make
```

#### Build Only `XCursor` theme

```bash
make unix
```

#### Customize `XCursor` size

```bash
make unix X_SIZES=22            # Only built '22px' pixel-size.
make unix X_SIZES=22 24 32      # Multiple sizes are provided with  ' '(Space)
```

#### Install `XCursor` theme

```bash
make install            # install as user
  # OR
sudo make install       # install as root
```

#### Build Only `Windows` theme

```bash
make windows
```

#### Customize `Windows Cursor` size

```bash
make windows WIN_SIZE=96            # Supports only one pixel-size
```

> Windows installations steps are same as [these](#windows).

<!-- Other Interesting projects -->

# You may also like...

- [**Bibata**](https://github.com/ful1e5/Bibata_Cursor) - Material based cursors
- [**Bibata Extra**](https://github.com/ful1e5/Bibata_Extra_Cursor) - More Bibata!
- [**Bibata Adapta**](https://gitlab.com/cscs/Bibata_AdaptaBreath_Cursors) - Bibata Based Cursor Made for AdaptaBreath and Manjaro.
- [**Bibata Translucent**](https://github.com/Silicasandwhich/Bibata_Cursor_Translucent) - Bibata translucent is a translucent flavor of the Bibata.

<!-- Bug Report -->

# Bugs

Bugs 🐛 should be reported [here](https://github.com/ful1e5/Bibata_Cursor_Rainbow/issues) on the Github issues page.

<!-- Help -->

# Getting Help

You can create a **issue**, I will help you. 🙂

<!-- Contributions and Suggestion -->

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.

<!-- This project isn't possible without these 👇🏻-->

# Credit

- [Bibata](https://github.com/ful1e5/Bibata_Cursor)
- [Adwaita](https://github.com/GNOME/adwaita-icon-theme)
- [Dmz](https://github.com/GalliumOS/dmz-cursor-theme)
- [Yaru](https://github.com/ubuntu/yaru)
- Emojis are taken from [here](https://emojipedia.org/)
- Wedge loading from [loading.io](https://loading.io/spinner/wedges/-pie-wedge-pizza-circle-round-rotate) with **Microsoft** colors

<!-- Support -->

# Support

<a href="https://www.buymeacoffee.com/Nt7Wg4V" >
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" >
</a>
