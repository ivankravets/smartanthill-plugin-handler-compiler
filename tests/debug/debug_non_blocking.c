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

#include "papi.h"
#include "debug.h"
#include "debug_state.h"
#line 20 "debug.c"
uint8_t debug_plugin_exec_init(const void* plugin_config, void* plugin_state)
{
*(uint8_t*)plugin_state = 0;
#line 22 "debug.c"
return PLUGIN_OK;
}

uint8_t debug_plugin_handler_init(const void* plugin_config, void* plugin_persistent_state)
{

return PLUGIN_OK;
}


uint8_t debug_plugin_handler(const void* plugin_config, void* plugin_persistent_state, void* plugin_state, parser_obj* command, MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
debug_plugin_state* sa_state = (debug_plugin_state*)plugin_state;
waiting_for* sa_wf = wf;
const debug_plugin_config* pc = (const debug_plugin_config*)plugin_config;
switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
case 4: goto label_4;
case 5: goto label_5;
case 6: goto label_6;
default: ZEPTO_ASSERT(0);
}
#line 39 "debug.c"
sa_state->data = papi_parser_read_encoded_uint16(command);
sa_state->sa_next = 1;
return PLUGIN_DEBUG;
label_1: /* nop */ ;
#line 40 "debug.c"
papi_start_sending_spi_command_16(pc->spi_id, 0x0003, 0x08, (sa_state->data), 0x02);
papi_wait_handler_add_wait_for_spi_send(sa_wf, pc->spi_id);
sa_state->sa_next = 2;
return PLUGIN_WAITING;
label_2:if(papi_wait_handler_is_waiting_for_spi_send(sa_wf, pc->spi_id))
{
return PLUGIN_WAITING;
}
#line 43 "debug.c"
papi_wait_handler_add_wait_for_timeout(sa_wf, 1000);
sa_state->sa_next = 3;
return PLUGIN_WAITING;
label_3:if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))
{
return PLUGIN_WAITING;
}
#line 46 "debug.c"
sa_state->response = 0;
sa_state->sa_next = 4;
return PLUGIN_DEBUG;
label_4: /* nop */ ;
#line 47 "debug.c"
papi_start_receiving_spi_data_16(pc->spi_id, 0x0000, 0x08, &(sa_state->response));
papi_wait_handler_add_wait_for_spi_receive(sa_wf, pc->spi_id);
sa_state->sa_next = 5;
return PLUGIN_WAITING;
label_5:if(papi_wait_handler_is_waiting_for_spi_receive(sa_wf, pc->spi_id))
{
return PLUGIN_WAITING;
}
#line 49 "debug.c"
papi_reply_write_encoded_uint16(reply, (sa_state->response));
sa_state->sa_next = 6;
return PLUGIN_DEBUG;
label_6: /* nop */ ;
sa_state->sa_next = 0;
#line 51 "debug.c"
return PLUGIN_OK;
}
