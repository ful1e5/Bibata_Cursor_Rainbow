#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FIXME: Remove this module after `clickgen` PNGProvider & `XPackager` patched.
# Issues:
#  => https://github.com/ful1e5/clickgen/issues/22
#  => https://github.com/ful1e5/clickgen/issues/23

import re
from pathlib import Path
from string import Template
from typing import Dict, List, Union

from clickgen.util import LikePath

THEME_FILES_TEMPLATES: Dict[str, Template] = {
    "cursor.theme": Template("[Icon Theme]\nName=$theme_name\nInherits=$theme_name"),
    "index.theme": Template(
        '[Icon Theme]\nName=$theme_name\nComment=$comment\nInherits="hicolor"'
    ),
}


def XPackager(directory: Path, theme_name: str, comment: str) -> None:
    """ Create a crispy `XCursors` theme package. """

    # Writing all .theme files
    files: Dict[str, str] = {}
    for file, template in THEME_FILES_TEMPLATES.items():
        files[file] = template.safe_substitute(theme_name=theme_name, comment=comment)

    for f, data in files.items():
        fp: Path = directory / f
        fp.write_text(data)


class PNGProvider(object):
    """Provide organized `.png` files."""

    bitmaps_dir: Path
    __pngs: List[str] = []

    def __init__(self, bitmaps_dir: LikePath) -> None:
        """Init `PNGProvider`.

        :bitmaps_dir: path to directory where `.png` files are stored.
        """
        super().__init__()
        self.bitmaps_dir = Path(bitmaps_dir)
        for f in sorted(self.bitmaps_dir.iterdir()):
            self.__pngs.append(f.name)

        if len(self.__pngs) == 0:
            raise FileNotFoundError(
                f"'*.png' files not found in '{self.bitmaps_dir.absolute()}'"
            )

    def get(self, key: str) -> Union[List[Path], Path]:
        """Get `.png` file/s from key.
        This method return file location in `pathlib.Path` instance.

        Also, this method is not supported directory sync, Which means creating a new file or deleting a file not affect this method.

        The only way to sync the directory is, By creating a new instance of the `PNGProvider` class.

        :key: Without extension it search for multiple files, Else search the key with `.png` extension.
        """
        k = key.split(".")
        if len(k) == 1:
            r = re.compile(fr"^{k[0]}(?:-\d+)?.png$")
        else:
            r = re.compile(fr"^{k[0]}(?:-\d+)?.{k[1]}$")

        matched_pngs = filter(r.match, self.__pngs)

        paths = list(set(map(lambda x: self.bitmaps_dir / x, matched_pngs)))
        if len(paths) == 1:
            return paths[0]
        return paths
