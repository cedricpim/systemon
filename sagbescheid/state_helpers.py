#!/usr/bin/env python
# coding: utf-8
# Copyright © 2015 Wieland Hoffmann
# License: MIT, see LICENSE for details
from .state import State


def is_recovery(old, new):
    return old == State.failed and new == State.active


def is_failure(state):
    return state == State.failed


def is_ongoing_failure(old, new):
    return old == State.failed and new == State.failed
