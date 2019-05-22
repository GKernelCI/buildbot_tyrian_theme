# Copyright 2018 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v3

from buildbot.www.plugin import Application

# create the interface for the setuptools entry point
ep = Application(__name__, "Buildbot Tyrian UI Theme")
