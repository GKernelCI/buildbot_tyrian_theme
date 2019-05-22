# Tyrian for Buildbot

_Gentoo Theme for Buildbot_

[![GPL-3.0-or-later License][license-badge]](COPYING)

## Installation

To install from source,

```terminal
python install -r requirements.txt

python setup.py install
```

Then add the plugin to the buildbot webserver configuration,

```python
c['www'] = dict(port=8010,
                plugins=dict(waterfall_view={}, console_view={}, grid_view={}, tyrian_view={}))
```

An example configuration has been provided, (See: [`example/master.cfg`](example/master.cfg)).

To view the example,

```terminal
cd example
buildbot create-master
buildbot start
```

## Resources

- [How to package Buildbot plugins][buildbot-plugins]
- [Tyrian – The new look of gentoo.org][tyrian]

[license-badge]: https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg?style=flat-square
[buildbot-plugins]: https://docs.buildbot.net/current/developer/plugins-publish.html
[tyrian]: https://gitweb.gentoo.org/sites/tyrian-theme.git
