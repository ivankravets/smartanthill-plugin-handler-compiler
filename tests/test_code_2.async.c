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
struct _sa_state_t {
byte _sa_next;
};
//#line 23


byte my_plugin_handler_init(const void* plugin_config,void* plugin_state) {
struct _sa_state_t* _sa_state = (struct _sa_state_t*)plugin_state;
_sa_state->_sa_next = 0;
  const my_plugin_config* pc = (my_plugin_config*) plugin_config;
  zepto_set_pin(pc->request_pin_number,0);
}

//TODO: reinit? (via deinit, or directly, or implicitly)

byte my_plugin_handler(const void* plugin_config, void* plugin_state,
  ZEPTO_PARSER* command, REPLY_HANDLE reply, WaitingFor* waiting_for) {
struct _sa_state_t* _sa_state = (struct _sa_state_t*)plugin_state;
  const my_plugin_config* pc = (my_plugin_config*) plugin_config;

switch(_sa_state->_sa_next) {
case 0: goto label_0;
case 1: goto label_1;
case 2: goto label_2;
case 3: goto label_3;
default: assert(0);
}
label_0:;
//#line 34


  zepto_wait_for_pin_non_blocking(some0, 0);
_sa_state->_sa_next = 1;
return 1; /* WAIT */
label_1:;
//#line 36

  uint16_t data_read = zepto_read_from_pins(some0, 0);
  
  if(codition) {
    zepto_wait_for_pin_non_blocking(some1, 1);
_sa_state->_sa_next = 2;
return 1; /* WAIT */
label_2:;
//#line 40

    zepto_read_from_pins1(some1, 1);

    if(cond2) {
      zepto_wait_for_pin_non_blocking(some2, 2);
_sa_state->_sa_next = 3;
return 1; /* WAIT */
label_3:;
//#line 44

      zepto_read_from_pins2(some2, 2);
    }
    zepto_reply_append_byte1(reply1,0);
  }
  
  zepto_reply_append_byte1(reply1,0);

  _sa_state->_sa_next = 0;return 0;
}
