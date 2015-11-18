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
    return PLUGIN_OK;
}

uint8_t sub_machine2_plugin_handler_init(const void* plugin_config,
                                    void* plugin_persistent_state)
{
    return PLUGIN_OK;
}

bool flag(bool value)
{
    /* this function has two states */
    papi_sleep( 100 );
    return !value;
}

void helper_func_0()
{
    /* this function does not have states */
    /* nop */;
}

void helper_func_1()
{
    /* this function has two states */
    papi_sleep( 100 );
    
    return;
}

uint8_t helper_func_2()
{
    /* this function call another function with states */

    helper_func_1();
    helper_func_0();
    helper_func_1();
    
    return PLUGIN_OK;
}

uint8_t sub_machine2_plugin_handler(const void* plugin_config,
    void* plugin_persistent_state, void* plugin_state, parser_obj* command,
    MEMORY_HANDLE reply, waiting_for* wf, uint8_t first_byte)
{
    helper_func_0();
    /* waiting function */
    papi_sleep( 1000 );
    
    helper_func_0();
    uint8_t res = helper_func_2();
    if(flag(true)) {
        helper_func_0();
    } else {
        return res;    
    }

    return PLUGIN_OK;
}
