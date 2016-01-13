/*******************************************************************************
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
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*******************************************************************************/


#if !defined __SA_STATELESS_PLUGIN_H__
#define __SA_STATELESS_PLUGIN_H__

#include <stdint.h>
#include "papi.h"

//TODO there is a dependency issue, 'parser' must be over 'state' here 
#include "stateless_parser.h"
#include "stateless_state.h"


typedef struct _stateless_plugin_config
{
    uint16_t pin_led;
} stateless_plugin_config;

typedef struct _stateless_plugin_persistent_state
{
    uint8_t dummy_byte;
} stateless_plugin_persistent_state;

#ifdef __cplusplus
extern "C" {
#endif

uint8_t stateless_plugin_handler_init( const void* plugin_config, void* plugin_state );
uint8_t stateless_plugin_exec_init( const void* plugin_config, void* plugin_state );
uint8_t stateless_plugin_handler( const void* plugin_config, void* plugin_persistent_state,
    void* plugin_state, ZEPTO_PARSER* command, MEMORY_HANDLE reply,
    waiting_for* wf, uint8_t first_byte );

#ifdef __cplusplus
}
#endif

#endif // __SA_BLINK_PLUGIN_H__
