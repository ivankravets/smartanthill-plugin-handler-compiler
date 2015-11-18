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
#include "sub_machine2.h"
#include "sub_machine2_state.h"

uint8_t sub_machine2_plugin_exec_init(const void* plugin_config, void* plugin_state)
{
*(uint8_t*)plugin_state = 0;
    return PLUGIN_OK;
}

uint8_t sub_machine2_plugin_handler_init(const void* plugin_config,
                                    void* plugin_persistent_state)
{
    return PLUGIN_OK;
}

bool flag(void* sa_state0, waiting_for* sa_wf, uint8_t* sa_result, bool value)
{
sub_machine2_plugin_state1* sa_state = (sub_machine2_plugin_state1*)sa_state0;

switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
default: ZEPTO_ASSERT(0);
}


//#line 32

    /* this function has two states */
    
papi_wait_handler_add_wait_for_timeout(sa_wf, 100);
sa_state->sa_next = 1;
*sa_result = PLUGIN_WAITING;
return 0;

label_1:
if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf)) {
*sa_result = PLUGIN_WAITING;
return 0;
}
//#line 34

    sa_state->sa_next = 0;return !value;
}

void helper_func_0()
{
    /* this function does not have states */
    /* nop */;
}

void helper_func_1(void* sa_state0, waiting_for* sa_wf, uint8_t* sa_result)
{
sub_machine2_plugin_state2* sa_state = (sub_machine2_plugin_state2*)sa_state0;

switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
default: ZEPTO_ASSERT(0);
}


//#line 45

    /* this function has two states */
    
papi_wait_handler_add_wait_for_timeout(sa_wf, 100);
sa_state->sa_next = 1;
*sa_result = PLUGIN_WAITING;
return;

label_1:
if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf)) {
*sa_result = PLUGIN_WAITING;
return;
}
//#line 47

    
    sa_state->sa_next = 0;return;
}

uint8_t helper_func_2(void* sa_state0, waiting_for* sa_wf, uint8_t* sa_result)
{
sub_machine2_plugin_state3* sa_state = (sub_machine2_plugin_state3*)sa_state0;

switch(sa_state->sa_next) {
case 0: break;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
default: ZEPTO_ASSERT(0);
}


//#line 53

    /* this function call another function with states */

    
*(uint8_t*)(sa_state + 1) = 0;
sa_state->sa_next = 1;
label_1: helper_func_1((void*)(sa_state + 1), sa_wf, sa_result);
if(*(uint8_t*)(sa_state + 1) != 0) return 0;
    helper_func_0();
sa_state->sa_next = 2;
*sa_result = PLUGIN_DEBUG;
return 0;
label_2: /* nop */ ;
//#line 57

    
*(uint8_t*)(sa_state + 1) = 0;
sa_state->sa_next = 3;
label_3: helper_func_1((void*)(sa_state + 1), sa_wf, sa_result);
if(*(uint8_t*)(sa_state + 1) != 0) return 0;
    
    sa_state->sa_next = 0;return PLUGIN_OK;
}

uint8_t sub_machine2_plugin_handler(const void* plugin_config,
    void* plugin_persistent_state, void* plugin_state, parser_obj* command,
    MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
sub_machine2_plugin_state* sa_state = (sub_machine2_plugin_state*)plugin_state;
waiting_for* sa_wf = wf;
uint8_t sa_result0 = PLUGIN_OK;
uint8_t* sa_result = &sa_result0;

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


//#line 66

    helper_func_0();
sa_state->sa_next = 1;
return PLUGIN_DEBUG;
label_1: /* nop */ ;
//#line 67

    /* waiting function */
    
papi_wait_handler_add_wait_for_timeout(sa_wf, 1000);
sa_state->sa_next = 2;
return PLUGIN_WAITING;

label_2:
if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf)) {
return PLUGIN_WAITING;
}
//#line 69

    
    helper_func_0();
sa_state->sa_next = 3;
return PLUGIN_DEBUG;
label_3: /* nop */ ;
//#line 71

    
*(uint8_t*)(sa_state + 1) = 0;
sa_state->sa_next = 4;
label_4: sa_state->res = helper_func_2((void*)(sa_state + 1), sa_wf, sa_result);
if(*(uint8_t*)(sa_state + 1) != 0) return *sa_result;
    
*(uint8_t*)(sa_state + 1) = 0;
sa_state->sa_next = 5;
label_5: ;/*nop*/
int zc_temp_var = flag((void*)(sa_state + 1), sa_wf, sa_result, true);
if(*(uint8_t*)(sa_state + 1) != 0) return *sa_result;if((zc_temp_var)) {
        helper_func_0();
sa_state->sa_next = 6;
return PLUGIN_DEBUG;
label_6: /* nop */ ;
//#line 74

    } else {
        sa_state->sa_next = 0;return (sa_state->res);    
    }

    sa_state->sa_next = 0;return PLUGIN_OK;
}
