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

#include "papi.h"

#include "expression.h"

#define HAPI_GPIO_VALUE_LOW 0
#define HAPI_GPIO_VALUE_HIGH 1
#define HAPI_GPIO_TYPE_OUTPUT 0

void hapi_gpio_init(uint16_t pin_num) {}
void hapi_gpio_set_mode(uint16_t pin_num, uint8_t mode) {}


uint8_t expression_plugin_handler_init( const void* plugin_config, void* plugin_state )
{
	return PLUGIN_OK;
}

uint8_t expression_plugin_exec_init( const void* plugin_config, void* plugin_state )
{
    expression_plugin_config* pc = (expression_plugin_config*)plugin_config;
    hapi_gpio_init(pc->pin_led);
    hapi_gpio_set_mode(pc->pin_led, HAPI_GPIO_TYPE_OUTPUT);
    return PLUGIN_OK;
}

uint8_t expression_plugin_handler( const void* plugin_config, void* plugin_persistent_state,
    void* plugin_state, ZEPTO_PARSER* command, MEMORY_HANDLE reply,
    waiting_for* wf, uint8_t first_byte )
{
    expression_plugin_config* pc = (expression_plugin_config*)plugin_config;
    
    expression_plugin_data req = expression_plugin_parser_read(command);
    papi_sleep(req.delay_ms);
    uint8_t i = 0;
    papi_sleep(req.delay_ms);
    i = 1;
    papi_sleep(req.delay_ms);
    ++i;
    i--;
    uint8_t j = i + 6;
    j *= 10;
    
    

	papi_reply_write_byte( reply, i ); // answer with count
	return PLUGIN_OK;
}
