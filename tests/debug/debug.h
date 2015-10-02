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
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
*****************************************************************************/


#if !defined __SA_DEBUG_PLUGIN_H__
#define __SA_DEBUG_PLUGIN_H__

#include "papi.h"

//constant structure filled with a configuration for specific 'ant body part'
typedef struct _debug_plugin_config
{
    uint8_t spi_id;
} debug_plugin_config;

typedef struct _debug_plugin_persistent_state
{
    uint16_t last_sent_id;
} debug_plugin_persistent_state;

#ifdef __cplusplus
extern "C" {
#endif

uint8_t debug_plugin_handler_init( const void* plugin_config, void* plugin_persistent_state );
uint8_t debug_plugin_exec_init( const void* plugin_config, void* plugin_state );
uint8_t debug_plugin_handler( const void* plugin_config, void* plugin_persistent_state, void* plugin_state, parser_obj* command, MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte );

#ifdef __cplusplus
}
#endif

#endif // __SA_DEBUG_PLUGIN_H__
