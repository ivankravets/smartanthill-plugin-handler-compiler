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


#if !defined __SA_MY_1_PLUGIN_H__
#define __SA_MY_1_PLUGIN_H__

//#include <simpleiot/siot_common.h>
//#include <simpleiot/siot_data_types.h>
//#include <simpleiot_hal/siot_mem_mngmt.h>
//#include <simpleiot/siot_gd_protocol.h> // for packet flags


typedef struct _my_1_plugin_config //constant structure filled with a configuration for specific 'ant body part'
{
    uint8_t dummy;
    uint8_t bodypart_id;   //always present
    uint8_t request_pin_number;//pin to request sensor read
    uint8_t ack_pin_number;//pin to wait for to see when sensor has provided the data
} my_1_plugin_config;

typedef struct _my_1_plugin_persistent_state
{
    uint8_t state; //'0' means 'be ready to process incoming command', '1' means 'prepare reply'
    uint16_t last_sent_id;
    uint16_t currChainID[2];
    uint16_t currChainIdBase[2];
    uint8_t first_byte;
    uint16_t chain_id[2];
    uint16_t chain_ini_size;
    uint16_t reply_to_id;
    uint16_t self_id;
} my_1_plugin_persistent_state;

#ifdef __cplusplus
extern "C" {
#endif

uint8_t my_1_plugin_handler_init( const void* plugin_config, void* plugin_persistent_state );
uint8_t my_1_plugin_exec_init( const void* plugin_config, void* plugin_state );
uint8_t my_1_plugin_handler( const void* plugin_config, void* plugin_persistent_state, void* plugin_state, parser_obj* command, MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte );

#ifdef __cplusplus
}
#endif

#endif // __SA_MY_1_PLUGIN_H__