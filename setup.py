#!/usr/bin/env python
#
# Copyright 2018 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from buildbot_pkg import setup_www_plugin
except ImportError:
    import sys
    print("Please install buildbot_pkg module in order to install that package, or use the pre-build .whl modules available on pypi", file=sys.stderr)
    sys.exit(1)

setup_www_plugin(
    name='buildbot-tyrian-theme',
    description='Buildbot Tyrian UI Theme plugin',
    author=u'Lucas Ramage',
    author_email=u'ramage.lucas@protonmail.com',
    setup_requires=['buildbot_pkg'],
    url='https://gitlab.com/oxr463/buildbot_tyrian_theme',
    license='GNU GPL',
    packages=['buildbot_tyrian_view'],
    package_data={
        '': [
            'VERSION',
            'static/*'
        ]
    },
    entry_points="""
        [buildbot.www]
        tyrian_view = buildbot_tyrian_view:ep
    """
)
