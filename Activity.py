#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Comverter.py by:
#	Cristhofer Travieso <cristhofert97@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import json

from gettext import gettext as _
import gtk

from sugar import profile
from sugar import mime
from sugar.activity import activity
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import ToolbarButton
from sugar.graphics.icon import Icon
from sugar.graphics.colorbutton import ColorToolButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.radiotoolbutton import RadioToolButton
from sugar.graphics.objectchooser import ObjectChooser
from sugar.graphics.alert import Alert, NotifyAlert

class Activity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, True)

        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)

        toolbarbox.toolbar.insert(activity_button, 0)

        separator = gtk.SeparatorToolItem()
        separator.set_expand(False)
        separator.set_draw(True)
        toolbarbox.toolbar.insert(separator, -1)

        # RadioToolButton
        self._long_btn = RadioToolButton()
        self._long_btn.props.icon_name = "long"

        self._vol_btn = RadioToolButton()
        self._vol_btn.props.icon_name = "vol"
        self._vol_btn.props.group = self._long_btn

        self._area_btn = RadioToolButton()
        self._area_btn.props.icon_name = "area"
        self._area_btn.props.group = self._long_btn

        self._peso_btn = RadioToolButton()
        self._peso_btn.props.icon_name = "peso"
        self._peso_btn.props.group = self._long_btn

        self._vel_btn = RadioToolButton()
        self._vel_btn.props.icon_name = "vel"
        self._vel_btn.props.group = self._long_btn

        self._time_btn = RadioToolButton()
        self._time_btn.props.icon_name = "time"
        self._time_btn.props.group = self._long_btn

        toolbarbox.toolbar.insert(self._long_btn, -1)
        toolbarbox.toolbar.insert(self._vol_btn, -1)
        toolbarbox.toolbar.insert(self._area_btn, -1)
        toolbarbox.toolbar.insert(self._peso_btn, -1)
        toolbarbox.toolbar.insert(self._vel_btn, -1)
        toolbarbox.toolbar.insert(self._time_btn, -1)

        #
        separator = gtk.SeparatorToolItem()
        separator.set_expand(True)
        separator.set_draw(False)
        toolbarbox.toolbar.insert(separator, -1)

        stopbtn = StopButton(self)
        toolbarbox.toolbar.insert(stopbtn, -1)

        self.set_toolbar_box(toolbarbox)

        #Canvas
        canvas = Canvas()

        self.set_canvas(canvas)

        self.show_all()


class Canvas(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self)

        self.add(gtk.Label("Of "))
        self.add(gtk.Label("to"))

        self.show_all()