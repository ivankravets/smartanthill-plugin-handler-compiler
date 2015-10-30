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
#include "sub_machine.h"
#include "sub_machine_state.h"


static sub_machine_plugin_state* sa_state = 0;
static waiting_for* sa_wf = 0;

uint8_t sub_machine_plugin_exec_init(const void* plugin_config, void* plugin_state)
{
sub_machine_plugin_state* sa_state = (sub_machine_plugin_state*)plugin_state;
sa_state->sa_result = PLUGIN_OK;
sa_state->sa_next = 0;
sa_state->sa_next2 = 0;
sa_state->sa_next3 = 0;
    return PLUGIN_OK;
}

uint8_t sub_machine_plugin_handler_init(const void* plugin_config,
                                    void* plugin_persistent_state)
{
    return PLUGIN_OK;
}

void helper_func_0()
{
    /* this function does not have states */
    /* nop */;
}

void helper_func_1()
{

switch(sa_state->sa_next2) {
case 0: break;
case 1: goto label_1;
default: ZEPTO_ASSERT(0);
}


//#line 38

    /* this function has two states */
    
papi_wait_handler_add_wait_for_timeout(sa_wf, 100);
sa_state->sa_next2 = 1;
{sa_state->sa_result = PLUGIN_WAITING; return;}

label_1:
if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))
{sa_state->sa_result = PLUGIN_WAITING; return;}
//#line 40

    
    sa_state->sa_next2 = 0;return;
}

void helper_func_2()
{

switch(sa_state->sa_next3) {
case 0: break;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
default: ZEPTO_ASSERT(0);
}


//#line 46

    /* this function call another function with states */

    
sa_state->sa_next3 = 1;
label_1: helper_func_1();
if(sa_state->sa_next2 != 0) return;
    helper_func_0();
sa_state->sa_next3 = 2;
{sa_state->sa_result = PLUGIN_DEBUG; return;}
label_2: /* nop */ ;
//#line 50

    
sa_state->sa_next3 = 3;
label_3: helper_func_1();
if(sa_state->sa_next2 != 0) return;

    sa_state->sa_next3 = 0;return;
}

uint8_t sub_machine_plugin_handler(const void* plugin_config,
    void* plugin_persistent_state, void* plugin_state, parser_obj* command,
    MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
sa_state = (sub_machine_plugin_state*)plugin_state;
sa_wf = wf;

switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
case 4: goto label_4;
case 5: goto label_5;
default: ZEPTO_ASSERT(0);
}


//#line 59

    helper_func_0();
sa_state->sa_next = 1;
return PLUGIN_DEBUG;
label_1: /* nop */ ;
//#line 60

    /* waiting function */
    
papi_wait_handler_add_wait_for_timeout(sa_wf, 1000);
sa_state->sa_next = 2;
return PLUGIN_WAITING;

label_2:
if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))
return PLUGIN_WAITING;
//#line 62

    
    helper_func_0();
sa_state->sa_next = 3;
return PLUGIN_DEBUG;
label_3: /* nop */ ;
//#line 64

    
sa_state->sa_next = 4;
label_4: helper_func_1();
if(sa_state->sa_next2 != 0) return sa_state->sa_result;
    
sa_state->sa_next = 5;
label_5: helper_func_2();
if(sa_state->sa_next3 != 0) return sa_state->sa_result;

    sa_state->sa_next = 0;return PLUGIN_OK;
}
