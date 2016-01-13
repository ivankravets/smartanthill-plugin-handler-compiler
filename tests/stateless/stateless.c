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

#include "stateless.h"

#define HAPI_GPIO_VALUE_LOW 0
#define HAPI_GPIO_VALUE_HIGH 1
#define HAPI_GPIO_TYPE_OUTPUT 0

void hapi_gpio_init(uint16_t pin_num) {}
void hapi_gpio_set_mode(uint16_t pin_num, uint8_t mode) {}


uint8_t stateless_plugin_handler_init( const void* plugin_config, void* plugin_state )
{
	return PLUGIN_OK;
}

uint8_t stateless_plugin_exec_init( const void* plugin_config, void* plugin_state )
{
    stateless_plugin_config* pc = (stateless_plugin_config*)plugin_config;
    hapi_gpio_init(pc->pin_led);
    hapi_gpio_set_mode(pc->pin_led, HAPI_GPIO_TYPE_OUTPUT);
    return PLUGIN_OK;
}

uint8_t stateless_plugin_handler( const void* plugin_config, void* plugin_persistent_state,
    void* plugin_state, ZEPTO_PARSER* command, MEMORY_HANDLE reply,
    waiting_for* wf, uint8_t first_byte )
{
    stateless_plugin_config* pc = (stateless_plugin_config*)plugin_config;
    stateless_plugin_data req = stateless_plugin_parser_read(command);

    papi_write_digital_pin(pc->pin_led, HAPI_GPIO_VALUE_HIGH);
    uint8_t i = 0;
    while(i < req.total_blinks) {
        i++;
    }

	stateless_plugin_reply_write( reply, i ); // answer with total_blinks
	return PLUGIN_OK;
}
