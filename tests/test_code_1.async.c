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


struct my_plugin_config { //constant structure filled with a configuration
                      //  for specific 'ant body part'
  byte bodypart_id;//always present
  byte request_pin_number;//pin to request sensor read
  byte ack_pin_number;//pin to wait for to see when sensor has provided the data
  byte reply_pin_numbers[4];//pins to read when ack_pin_number shows that the data is ready
};

byte my_plugin_handler_init(const void* plugin_config,void* plugin_state) {
  /* state machine */const my_plugin_config* pc = (my_plugin_config*) /* before */plugin_config;
  /* replaced */(pc->request_pin_number,0/* after */);
}

//TODO: reinit? (via deinit, or directly, or implicitly)

byte my_plugin_handler(const void* plugin_config, void* plugin_state,
  ZEPTO_PARSER* command, REPLY_HANDLE reply, WaitingFor* waiting_for) {
  /* state machine */const my_plugin_config* pc = (my_plugin_config*) /* before */plugin_config;

  //requesting sensor to perform read, using pc->request_pin_number
  /* replaced */(pc->request_pin_number,1/* after */);

  //waiting for sensor to indicate that data is ready
  zepto_wait_for_pin(pc->ack_pin_number,1);

  uint16_t data_read = /* replaced */(pc->reply_pin_numbers,4/* after */);
  /* replaced */(reply,data_read/* after */);
  return 0;
}
