#!/usr/bin/env python

import elasticd
import os

elasticd.startup(os.path.dirname(os.path.realpath(__file__)) + '/../conf/settings.cfg')
