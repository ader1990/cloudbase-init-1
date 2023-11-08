# Copyright 2023 Cloudbase Solutions Srl
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# https://github.com/python/cpython/blob/3.10/LICENSE
# _dot_lookup, _importer, _get_target

from unittest import mock


# https://github.com/python/cpython/blob/3.10/Lib/unittest/mock.py#L1246
def _dot_lookup(thing, comp, import_path):
    try:
        return getattr(thing, comp)
    except AttributeError:
        __import__(import_path)
        return getattr(thing, comp)


# https://github.com/python/cpython/blob/3.10/Lib/unittest/mock.py#L1254
def _importer(target):
    components = target.split('.')
    import_path = components.pop(0)
    thing = __import__(import_path)

    for comp in components:
        import_path += ".%s" % comp
        thing = _dot_lookup(thing, comp, import_path)
    return thing


# https://github.com/python/cpython/blob/3.10/Lib/unittest/mock.py#L1612
def _get_target(target):
    try:
        target, attribute = target.rsplit('.', 1)
    except (TypeError, ValueError):
        raise TypeError("Need a valid target to patch. You supplied: %r" %
                        (target,))
    getter = lambda: _importer(target)
    return getter, attribute


# Note(avladu): use the py 3.10 and lower importer for mock
# https://github.com/python/cpython/blob/3.10/Lib/unittest/mock.py#L1246
# Otherwise, the unit tests that use importlib with context are not
# running in an isolated manner, leading to various transient failures.
mock._get_target = _get_target
