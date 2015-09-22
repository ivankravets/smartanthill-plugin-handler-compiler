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

#include <stdint.h>
typedef uint8_t byte;
struct _sa_state_t {
byte _sa_next;
byte some;
};
//#line 17


struct my_plugin_config { //constant structure filled with a configuration
                      //  for specific 'ant body part'
  byte bodypart_id;//always present
  byte request_pin_number;//pin to request sensor read
  byte ack_pin_number;//pin to wait for to see when sensor has provided the data
  byte reply_pin_numbers[4];//pins to read when ack_pin_number shows that the data is ready
};

byte my_plugin_handler_init(const void* plugin_config,void* plugin_state) {
  const struct my_plugin_config* pc = (struct my_plugin_config*) plugin_config;
  zepto_set_pin(pc->request_pin_number,0);
}

//TODO: reinit? (via deinit, or directly, or implicitly)

byte my_plugin_handler(const void* plugin_config, void* plugin_state,
  void* command, void* reply, void* waiting_for) {
struct _sa_state_t* _sa_state = (struct _sa_state_t*)plugin_state;
  const struct my_plugin_config* pc = (struct my_plugin_config*) plugin_config;

switch(_sa_state->_sa_next) {
case 0: goto label_0;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
case 4: goto label_4;
default: assert(0);
}
label_0:;
//#line 36


  //requesting sensor to perform read, using pc->request_pin_number
  zepto_set_pin(pc->request_pin_number,1);
  do_something(pc->request_pin_number);
  do_something_else();

  _sa_state->some = 4;
  //waiting for sensor to indicate that data is ready
  zepto_wait_for_pin_non_blocking(pc->ack_pin_number,1);
_sa_state->_sa_next = 1;
return 1; /* WAIT */
label_1:;
//#line 45

  zepto_read_from_pins(pc->reply_pin_numbers,4);

  //waiting for sensor to indicate that data is ready
  zepto_wait_for_pin_non_blocking(pc->ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 2;
return 1; /* WAIT */
label_2:;
//#line 49

  uint16_t data_read = zepto_read_from_pins2(pc->reply_pin_numbers,4);
  if (data_read != 0) {
    zepto_wait_for_pin_non_blocking(pc->ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 3;
return 1; /* WAIT */
label_3:;
//#line 52

    zepto_read_from_pins3(pc->reply_pin_numbers,4);
  } else {
      if ((_sa_state->some) != 0) {
        zepto_wait_for_pin_non_blocking(pc->ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 4;
return 1; /* WAIT */
label_4:;
//#line 56

        zepto_reply_append_byte(reply,(_sa_state->some));
      }
      else
        zepto_reply_append_byte2(reply,0);

      zepto_reply_append_byte3(reply,0);
  }
  zepto_reply_append_byte4(reply,0);

  _sa_state->_sa_next = 0;return 0;
}
