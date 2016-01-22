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

#if !defined __SA_WRITE_DIGITAL_PIN_PLUGIN_H__
#define __SA_WRITE_DIGITAL_PIN_PLUGIN_H__

#include <stdint.h>
#include "papi.h"

struct _write_digital_pin_plugin_data
{
uint8_t value;
};
typedef struct _write_digital_pin_plugin_data write_digital_pin_plugin_data;
static inline write_digital_pin_plugin_data write_digital_pin_plugin_parser_read(ZEPTO_PARSER* sa_po)
{
write_digital_pin_plugin_data sa_res;
sa_res.value = papi_parser_read_byte(sa_po);
return sa_res;
}
static inline void write_digital_pin_plugin_reply_write(REPLY_HANDLE sa_rh, uint8_t result)
{
papi_reply_write_byte(sa_rh, result);
}
struct _write_digital_pin_plugin_config
{
uint8_t pin_num;
};
typedef struct _write_digital_pin_plugin_config write_digital_pin_plugin_config;

typedef struct _write_digital_pin_plugin_persistent_state
{
uint8_t sa_dummy;
} write_digital_pin_plugin_persistent_state;

#ifdef __cplusplus
extern "C" {
#endif

uint8_t write_digital_pin_plugin_handler_init( const void* plugin_config, void* plugin_state );
uint8_t write_digital_pin_plugin_exec_init( const void* plugin_config, void* plugin_state );
uint8_t write_digital_pin_plugin_handler( const void* plugin_config, void* plugin_persistent_state, void* plugin_state, ZEPTO_PARSER* command, MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte );

#ifdef __cplusplus
}
#endif

#endif // __SA_WRITE_DIGITAL_PIN_PLUGIN_H__