#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

# Info
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/Bibata_Cursor_Rainbow"

# XCursor
X_DELAY: int = 50


# Windows Cursor
WIN_DELAY = 2

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "crossed_circle.png": {"xhot": 100, "yhot": 100},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need an extension and frame numbers.
    "bd_double_arrow": {"xhot": 98, "yhot": 100},
    "bottom_left_corner": {"xhot": 31, "yhot": 172},
    "bottom_right_corner": {"xhot": 170, "yhot": 172},
    "bottom_side": {"xhot": 100, "yhot": 164},
    "bottom_tee": {"xhot": 100, "yhot": 164},
    "center_ptr": {"xhot": 98, "yhot": 131},
    "circle": {"xhot": 48, "yhot": 25},
    "context-menu": {"xhot": 48, "yhot": 25},
    "copy": {"xhot": 48, "yhot": 25},
    "cross": {"xhot": 98, "yhot": 96},
    # "crosshair": {"xhot": 99, "yhot": 99},
    "dnd_no_drop": {"xhot": 86, "yhot": 79},
    "dnd-ask": {"xhot": 86, "yhot": 79},
    "dnd-copy": {"xhot": 86, "yhot": 79},
    "dnd-link": {"xhot": 86, "yhot": 79},
    "dnd-move": {"xhot": 86, "yhot": 79},
    "dotbox": {"xhot": 100, "yhot": 100},
    "fd_double_arrow": {"xhot": 98, "yhot": 100},
    "grabbing": {"xhot": 106, "yhot": 79},
    "hand1": {"xhot": 113, "yhot": 95},
    "hand2": {"xhot": 88, "yhot": 32},
    "left_ptr": {"xhot": 53, "yhot": 36},
    "left_side": {"xhot": 35, "yhot": 100},
    "left_tee": {"xhot": 165, "yhot": 95},
    "link": {"xhot": 48, "yhot": 25},
    "ll_angle": {"xhot": 34, "yhot": 165},
    "lr_angle": {"xhot": 167, "yhot": 164},
    "move": {"xhot": 100, "yhot": 100},
    "pencil": {"xhot": 37, "yhot": 161},
    "plus": {"xhot": 100, "yhot": 100},
    "pointer-move": {"xhot": 48, "yhot": 25},
    "question_arrow": {"xhot": 102, "yhot": 102},
    "right_ptr": {"xhot": 150, "yhot": 29},
    "right_side": {"xhot": 163, "yhot": 98},
    "right_tee": {"xhot": 30, "yhot": 96},
    "sb_down_arrow": {"xhot": 100, "yhot": 126},
    "sb_h_double_arrow": {"xhot": 100, "yhot": 100},
    "sb_left_arrow": {"xhot": 86, "yhot": 100},
    "sb_right_arrow": {"xhot": 113, "yhot": 100},
    "sb_up_arrow": {"xhot": 99, "yhot": 86},
    "sb_v_double_arrow": {"xhot": 100, "yhot": 100},
    "tcross": {"xhot": 98, "yhot": 100},
    "top_left_corner": {"xhot": 29, "yhot": 27},
    "top_right_corner": {"xhot": 170, "yhot": 28},
    "top_side": {"xhot": 98, "yhot": 34},
    "top_tee": {"xhot": 98, "yhot": 29},
    "ul_angle": {"xhot": 34, "yhot": 35},
    "ur_angle": {"xhot": 164, "yhot": 34},
    "vertical-text": {"xhot": 100, "yhot": 100},
    "xterm": {"xhot": 100, "yhot": 100},
    "zoom-in": {"xhot": 90, "yhot": 89},
    "zoom-out": {"xhot": 93, "yhot": 90},
    # Truly animated
    "left_ptr_watch": {"xhot": 50, "yhot": 28, "delay": 25},
    "wait": {"xhot": 100, "yhot": 100, "delay": 25},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    "right_ptr": {"to": "Alternate", "position": "top_left"},
    "cross": {"to": "Cross"},
    "left_ptr": {"to": "Default", "position": "top_left"},
    "bd_double_arrow": {"to": "Diagonal_1"},
    "fd_double_arrow": {"to": "Diagonal_2"},
    "pencil": {"to": "Handwriting"},
    "question_arrow": {"to": "Help", "position": "top_left"},
    "sb_h_double_arrow": {"to": "Horizontal"},
    "xterm": {"to": "IBeam", "position": "top_left"},
    "hand2": {"to": "Link", "position": "top_left"},
    "hand1": {"to": "Move"},
    "circle": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow": {"to": "Vertical"},
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy"},
}
