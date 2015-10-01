// Copyright (C) 2015 OLogN Technologies AG
//
// This source file is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License version 2
// as published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#include "papi.h"
#include "spi.h"
#include "spi_state.h"

uint8_t spi_plugin_exec_init(const void* plugin_config, void* plugin_state)
{
    return PLUGIN_OK;
}

uint8_t spi_plugin_handler_init(const void* plugin_config,
                                    void* plugin_persistent_state)
{
    return PLUGIN_OK;
}


uint8_t spi_plugin_handler(const void* plugin_config,
    void* plugin_persistent_state, void* plugin_state, parser_obj* command,
    MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
    const spi_plugin_config* pc = (const spi_plugin_config*) plugin_config;
    
    //send sensor message
    uint16_t data = papi_parser_read_encoded_uint16( command );
    papi_wait_for_spi_send(pc->spi_id, 0x0003, 0x08, data, 0x02);

    // give sensor some time to process
    papi_sleep( 1000 );   

    //waiting for sensor response
    uint16_t response = 0;
    papi_wait_for_spi_receive( pc->spi_id,  0x0000, 0x08, &response );
    
    papi_reply_write_encoded_uint16( reply, response );

    return PLUGIN_OK;
}
