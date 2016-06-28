# -*- coding:utf8 -*-

#    Copyright 2016 Mirantis, Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

PROJECTS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "branches": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "dst-repo": {
                "type": "string"
            },
            "project": {
                "type": "string"
            },
            "src-repo": {
                "type": "string"
            }
        },
        "required": [
            "branches",
            "dst-repo",
            "project",
            "src-repo"
        ]
    }
}