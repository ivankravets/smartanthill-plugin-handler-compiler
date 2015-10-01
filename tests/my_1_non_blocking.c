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
#include "my_1.h"
#include "my_1_state.h"

uint8_t my_1_plugin_exec_init( const void* plugin_config, void* plugin_state ) {
my_1_plugin_state* sa_state = (my_1_plugin_state*)plugin_state;
sa_state->sa_next = 0;
    return PLUGIN_OK;
}

uint8_t my_1_plugin_handler_init(const void* plugin_config, void* plugin_persistent_state) {
    const my_1_plugin_config* pc = (const my_1_plugin_config*) plugin_config;
    papi_write_digital_pin(pc->request_pin_number, 0);
    
    return PLUGIN_OK;
}

//TODO: reinit? (via deinit, or directly, or implicitly)

uint8_t my_1_plugin_handler(const void* plugin_config,
    void* plugin_persistent_state, void* plugin_state, parser_obj* command,
    MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte) {
my_1_plugin_state* sa_state = (my_1_plugin_state*)plugin_state;
    const my_1_plugin_config* pc = (const my_1_plugin_config*) plugin_config;

switch(sa_state->sa_next) {
case 0: goto label_0;
case 1: goto label_1;
case 2: goto label_2;
default: sa_state->sa_next = 0; return -1; /* TBD */
}
label_0:;
//#line 36

    
    //send sensor message
    papi_write_digital_pin(pc->request_pin_number, true);
    papi_start_sending_spi_command_16(pc->ack_pin_number, 0x1010, 0x0a, 0x00ff, 0x04);
sa_state->sa_next = 1;
return PLUGIN_WAITING;
label_1: if(papi_wait_handler_is_waiting_for_spi_send(wf, pc->ack_pin_number)) return PLUGIN_WAITING;
//#line 40


    //waiting for sensor response
    sa_state->response = 0;
    papi_start_receiving_spi_data_16( pc->ack_pin_number,  0x1010, 0x0a, &(sa_state->response) );
sa_state->sa_next = 2;
return PLUGIN_WAITING;
label_2: if(papi_wait_handler_is_waiting_for_spi_receive(wf, pc->ack_pin_number)) return PLUGIN_WAITING;
//#line 44

    
    papi_reply_write_encoded_uint16( reply, (sa_state->response) );

    sa_state->sa_next = 0;return 0;
}
