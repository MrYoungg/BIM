# -*- coding: utf8 -*-
# ***************************************************************************
# *   Copyright (c) 2014 Nathan Miller <Nathan.A.Mill@gmail.com>            *
# *   Copyright (c) 2014 Balázs Bámer                                       *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This library is free software; you can redistribute it and/or         *
# *   modify it under the terms of the GNU Library General Public           *
# *   License as published by the Free Software Foundation; either          *
# *   version 2 of the License, or (at your option) any later version.      *
# *                                                                         *
# *   This library  is distributed in the hope that it will be useful,      *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this library; see the file COPYING.LIB. If not,    *
# *   write to the Free Software Foundation, Inc., 59 Temple Place,         *
# *   Suite 330, Boston, MA  02111-1307, USA                                *
# *                                                                         *
# ***************************************************************************
"""The Surface Workbench GUI initialization."""

import os

import FreeCAD as App
import FreeCADGui as Gui


class PointCloudWorkbench(Gui.Workbench):
    """Surface workbench object."""

    # 找到对应的图标
    Icon = os.path.join(App.getResourceDir(),
                        "Mod", "Points",
                        "Resources", "icons", "PointsWorkbench.svg")
    # 在FreeCAD工具台列表中显示的名字
    MenuText = "PointCloud"
    # 在FreeCAD工具台列表中显示的详情
    ToolTip = "PointCloud workbench: deal with point cloud"

    def Initialize(self):
        """Initialize the module."""
        
    def GetClassName(self):
        return "Gui::PythonWorkbench"


Gui.addWorkbench(PointCloudWorkbench())
