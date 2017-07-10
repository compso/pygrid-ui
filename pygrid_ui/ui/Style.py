#******************************************************************************
# (c)2012 BlueBolt Ltd.  All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
# * Neither the name of BlueBolt nor the names of
# its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# Author:Rob Watson , Ashley Retallack - ashley-r@blue-bolt.com
# 
# File:style.py
# 
# 
#******************************************************************************

from PySide2.QtGui  import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
    
from os import path

import re

    
from .Color import Color


class Style(object):

    __currentStyle = None

    @staticmethod
    def registerCurrentStyle(style):
        Style.__currentStyle = style
        
    @staticmethod
    def currentStyle():
        return Style.__currentStyle or DarkStyle
    
    @classmethod
    def replaceColors(cls, styleobject, stylesheet):
        styleSheetString = ""
        
        for line in stylesheet:
            replaceItems = re.findall("(%\w+%)", line)
            for replaceItem in replaceItems:
                if hasattr(styleobject, replaceItem[1:-1]):
                    line = line.replace(replaceItem, str(getattr(styleobject, replaceItem[1:-1])))
                    
            styleSheetString += line
        return styleSheetString
        
    @classmethod
    def apply(cls, widget):
        raise NotImplementedError("Style.apply()")

    @classmethod
    def applyImpl(cls, styleobject, widget):
        
        style = QStyleFactory.create("CleanLooks")
        stylesheet = file(styleobject.FILE_PATH, "r")
        
        styleString = cls.replaceColors(styleobject, stylesheet)

        setattr(widget, "__style_object__", style)
        widget.setStyle(getattr(widget, "__style_object__"))
        widget.setStyleSheet(styleString)


class DarkStyle(Style):

    FILE_PATH = path.join(path.dirname(__file__), "..", "qss", "dark.qss")
    
    BACKGROUND_COLOR1 = Color(51, 51, 51)
    BACKGROUND_COLOR2 = Color(36, 36, 36)
    BACKGROUND_COLOR3 = Color(91, 91, 91)
    BACKGROUND_COLOR4 = Color(44, 44, 44)
    
    SELECTION_COLOR1 = Color(0, 0, 0)
    
    GRADIENT_COLOR1 = (Color(5, 5, 5), Color(61, 61, 61))

    TEXT_COLOR1 = Color(182, 182, 182)
    TEXT_COLOR2 = Color(182, 182, 182)
    
    BACKGROUND_SELECTED_COLOR1 = Color(220, 220, 220)
    BACKGROUND_SELECTED_COLOR2 = Color(220, 220, 220)
    
    BACKGROUND_COLOR_ALTERNATE1 = Color(55, 55, 55)
    
    BORDER_COLOR1 = Color(41, 41, 41)
    BORDER_COLOR2 = Color(65, 65, 65)
    BORDER_COLOR3 = Color(110, 110, 110)
    BORDER_COLOR4 = Color(0, 0, 0)
    
    @classmethod
    def apply(cls, widget):
        cls.applyImpl(DarkStyle, widget)
