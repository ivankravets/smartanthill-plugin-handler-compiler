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
#include "sleep.h"
#include "sleep_state.h"
#line 20 "sleep.c"
uint8_t sleep_plugin_exec_init(const void* plugin_config, void* plugin_state)
{
*(uint8_t*)plugin_state = 0;
#line 22 "sleep.c"
return PLUGIN_OK;
}

uint8_t sleep_plugin_handler_init(const void* plugin_config, void* plugin_persistent_state)
{

return PLUGIN_OK;
}


uint8_t sleep_plugin_handler(const void* plugin_config, void* plugin_persistent_state, void* plugin_state, parser_obj* command, MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
sleep_plugin_state* sa_state = (sleep_plugin_state*)plugin_state;
waiting_for* sa_wf = wf;
switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
default: ZEPTO_ASSERT(0);
}
#line 36 "sleep.c"
papi_wait_handler_add_wait_for_timeout(sa_wf, 10000);
sa_state->sa_next = 1;
return PLUGIN_WAITING;
label_1:if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))
{
return PLUGIN_WAITING;
}
sa_state->sa_next = 0;
#line 38 "sleep.c"
return PLUGIN_OK;
}
