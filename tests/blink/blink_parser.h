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

#if !defined __SA_BLINK_PLUGIN_PARSER_H__
#define __SA_BLINK_PLUGIN_PARSER_H__

#include <stdint.h>
#include "papi.h"


typedef struct _blink_plugin_data {
uint16_t delay_ms;
uint8_t total_blinks;
} blink_plugin_data;

static inline
blink_plugin_data blink_plugin_parser_read(ZEPTO_PARSER* po)
{
blink_plugin_data sa_res;
sa_res.delay_ms = papi_parser_read_encoded_uint16(po);
sa_res.total_blinks = papi_parser_read_byte(po);
return sa_res;
}


static inline
void blink_plugin_reply_write(REPLY_HANDLE mem_h, uint8_t made_blinks)
{
papi_reply_write_byte(mem_h, made_blinks);
}

#endif // __SA_BLINK_PLUGIN_PARSER_H__
