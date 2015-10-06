# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from os.path import dirname
from xml.etree import ElementTree
from smartanthill_phc import banner


def write_composer_file(prefix, zepto_plugin):
    '''
    Write file test with parser and composer functions
    '''

    include_guard = "__SA_%s_PLUGIN_PARSER_H__" % prefix.upper()
    struct_name = prefix + "_plugin_data"
    parser_name = prefix + "_plugin_parser_read"
    writer_name = prefix + "_plugin_reply_write"

    request_elements = _get_elements(zepto_plugin.get_request_fields())
    response_elements = _get_elements(zepto_plugin.get_response_fields())

    txt = banner.get_copyright_banner()

    txt += "\n"

    txt += "#if !defined %s\n" % include_guard
    txt += "#define %s\n\n" % include_guard

    txt += "#include <stdint.h>\n"
    txt += "#include \"papi.h\"\n\n\n"

    txt += _write_parser_func(struct_name, parser_name, request_elements)
    txt += "\n\n"
    txt += _write_composer_func(writer_name, response_elements)
    txt += "\n"

    txt += "#endif // %s\n" % include_guard

    return txt


class _Element(object):

    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type


def _get_elements(fields):

    result = []
    for current in fields:
        t = "".join(current['type'].split())
        if t == "encoded-uint[max=1]":
            c_type = "uint8_t"
        elif t == "encoded-uint[max=2]":
            c_type = "uint16_t"
        elif t == "encoded-int[max=2]":
            c_type = "int16_t"
        else:
            assert False

        result.append(_Element(current['name'], c_type))

    return result


def _get_parser_func_name(name):

    if name == 'uint8_t':
        return 'byte'
    elif name == 'uint16_t':
        return 'encoded_uint16'
    elif name == 'int16_t':
        return 'encoded_signed_int16'
    else:
        assert False


def _write_parser_func(struct_name, func_name, elements):

    if len(elements) == 0:
        return "/* empty parser */\n\n"
    elif len(elements) == 1:

        txt = "inline\n"
        txt += "%s %s(ZEPTO_PARSER* po)\n" % (elements[0].c_type, func_name)
        txt += "{\n"
        pn = _get_parser_func_name(elements[0].c_type)
        txt += "return papi_parser_read_%s(po);\n" % pn
        txt += "}\n"

        return txt
    else:

        txt = "typedef struct _%s {\n" % struct_name

        for each in elements:
            txt += "%s %s;\n" % (each.c_type, each.name)

        txt += "} %s;\n\n" % struct_name

        txt += "inline\n"
        txt += "%s %s(ZEPTO_PARSER* po)\n" % (struct_name, func_name)
        txt += "{\n"

        txt += "%s sa_res;\n" % struct_name
        for each in elements:
            pn = _get_parser_func_name(each.c_type)
            txt += "sa_res.%s = papi_parser_read_%s(po);\n" % (each.name, pn)
        txt += "return sa_res;\n"

        txt += "}\n"

        return txt


def _write_composer_func(func_name, elements):

    if len(elements) == 0:
        return "/* empty composer */\n\n"
    else:
        txt = "inline\n"
        txt += "void %s(REPLY_HANDLE mem_h" % func_name

        for each in elements:
            txt += ", %s %s" % (each.c_type, each.name)

        txt += ")\n{\n"

        for each in elements:
            pn = _get_parser_func_name(each.c_type)
            txt += "papi_reply_write_%s(mem_h, %s);\n" % (pn, each.name)

        txt += "}\n"

        return txt


class ZeptoPlugin(object):
    '''
    Copy and paste from zepto-compiler project,
    Remove this class and replace with a dependency to zepto-compiler project

    '''

    def __init__(self, manifest_path):
        self.xml = ElementTree.parse(manifest_path).getroot()
        self._source_dir = dirname(manifest_path)

    def get_source_dir(self):
        return self._source_dir

    def get_id(self):
        return self.xml.get("id")

    def get_name(self):
        return self.xml.get("name")

    def get_description(self):
        return self.xml.find("description").text

    def get_request_fields(self):
        items = self._get_items_by_path(
            "./request",
            ("type", "name", "title", "min", "max", "default")
        )
        return self._cast_attributes(items)

    def get_response_fields(self):

        elements = self.xml.find("./response")
        if elements is None:
            return []
        items = []
        for element in elements:
            data = {}
            for attr in ("name", "type", "min", "max"):
                data[attr] = element.get(attr, None)

            meaning = element.find('./meaning')
            if meaning is not None:
                data['meaning'] = meaning.get('type')

                conversion = meaning.find('./linear-conversion')
                if conversion is not None:
                    data["conversion"] = "linear-conversion"
                    for key in("input-point0", "output-point0",
                               "input-point1", "output-point1"):
                        data[key] = conversion.get(key, None)

            items.append(data)
        return items

    def get_peripheral(self):
        return self._get_items_by_path(
            "./configuration/peripheral",
            ("type", "name", "title")
        )

    def get_options(self):
        items = self._get_items_by_path(
            "./configuration/options",
            ("type", "name", "title", "min", "max", "default")
        )
        return self._cast_attributes(items)

    def _get_items_by_path(self, path, attrs):
        elements = self.xml.find(path)
        if elements is None:
            return []
        items = []
        for element in elements:
            data = {}

            for attr in attrs:
                data[attr] = element.get(attr, None)

            _values = element.find("./values")
            if _values is not None:
                data['_values'] = []
                for _v in _values:
                    data['_values'].append(
                        {"value": _v.get("value"), "title": _v.get("title")})

            items.append(data)
        return items

    def _cast_attributes(self, items):
        for item in items:
            for attr in ("min", "max", "default"):
                if item[attr] is None:
                    continue
                item[attr] = self._cast_to_type(item['type'], item[attr])
            if "_values" in item:
                for _v in item['_values']:
                    _v['value'] = self._cast_to_type(item['type'], _v['value'])
        return items

    @staticmethod
    def _cast_to_type(type_, value):
        if "int" in type_:
            value = int(value)
        elif "float" in type_:
            value = float(value)
        return value
