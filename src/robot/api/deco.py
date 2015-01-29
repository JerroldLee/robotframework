#  Copyright 2008-2014 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


def keyword(name=None):
    """Decorator to set custom keyword names to functions and methods.

    This decorator creates the ``robot_name`` attribute on the decorated
    keyword method or function.  Robot Framework checks for this attribute when
    determining the keyword's name.

    library.py::

        @keyword(name='Login Via User Panel')
        def login(username, password):
            # ...

    tests.robot::

        Login Via User Panel    myusername    mypassword

    If ``name`` is not given, the actual name of the keyword will not be
    affected, but the ``robot_name`` attribute will still be created.
    This can be useful for marking methods as keywords in a dynamic library.
    In this usage it is possible to also omit parenthesis when using the
    decorator::

        @keyword
        def func():
            # ...
    """
    if callable(name):
        return keyword()(name)
    def _method_wrapper(func):
        func.robot_name = name
        return func
    return _method_wrapper