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

struct my_plugin_config { //constant structure filled with a configuration
                      //  for specific 'ant body part'
  byte bodypart_id;//always present
  byte request_pin_number;//pin to request sensor read
  uint8_t spi_id;
  byte ack_pin_number;//pin to wait for to see when sensor has provided the data
  byte reply_pin_numbers[4];//pins to read when ack_pin_number shows that the data is ready
};

byte my_plugin_handler_init(const void* plugin_config,void* plugin_state) {
    const struct my_plugin_config* pc = (struct my_plugin_config*) plugin_config;
    papi_write_digital_pin(pc->request_pin_number, 0);
    return 0;
}

//TODO: reinit? (via deinit, or directly, or implicitly)

byte my_plugin_handler(const void* plugin_config, void* plugin_state,
  ZEPTO_PARSER* command, REPLY_HANDLE reply, WAITING_FOR* waiting_for) {
    const struct my_plugin_config* pc = (struct my_plugin_config*) plugin_config;
    
    //send sensor message
    papi_write_digital_pin(pc->request_pin_number, true);
    papi_wait_for_spi_send(pc->spi_id, 0x1010, 0x0a, 0x00ff, 0x04);

    //waiting for sensor response
    uint16_t response;
    papi_wait_for_spi_receive( pc->spi_id,  0x1010, 0x0a, &response );
    
    papi_reply_write_encoded_uint16( reply, response );

    return 0;
}
