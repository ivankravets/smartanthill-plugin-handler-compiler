/*****************************************************************************
    Copyright (C) 2015 OLogN Technologies AG

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 2 as
    published by the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

*****************************************************************************/

#if !defined __SA_WRITE_DIGITAL_PIN_PLUGIN_PARSER_H__
#define __SA_WRITE_DIGITAL_PIN_PLUGIN_PARSER_H__

#include <stdint.h>
#include "papi.h"


static inline
uint8_t write_digital_pin_plugin_parser_read(ZEPTO_PARSER* po)
{
return papi_parser_read_byte(po);
}


static inline
void write_digital_pin_plugin_reply_write(REPLY_HANDLE mem_h, uint8_t result)
{
papi_reply_write_byte(mem_h, result);
}

#endif // __SA_WRITE_DIGITAL_PIN_PLUGIN_PARSER_H__
