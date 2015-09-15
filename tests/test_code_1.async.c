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


struct _sa_state_data_t {
byte some;
};

byte my_plugin_handler_init(const void* plugin_config,void* plugin_state) {
void = (void)plugin_config;
zepto_set_pin(pc(op)request_pin_number,);
}

//TODO: reinit? (via deinit, or directly, or implicitly)

byte my_plugin_handler(const void* plugin_config, void* plugin_state,
  ZEPTO_PARSER* command, REPLY_HANDLE reply, WaitingFor* waiting_for) {
_sa_state_data_t* _sa_state = (_sa_state_data_t*)plugin_state;
void = (void)plugin_config;
switch(_sa_state->_sa_next) {
case 0:
{
zepto_set_pin(pc(op)request_pin_number,);
do_something(pc(op)request_pin_number);
do_something_else();
_sa_state->some = ;
zepto_wait_for_pin(pc(op)ack_pin_number,);
_sa_state->_sa_next = 1; return WAIT;
}
case 1:
{
zepto_read_from_pins(pc(op)reply_pin_numbers,);
zepto_wait_for_pin(pc(op)ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 2; return WAIT;
}
case 2:
{
void = zepto_read_from_pins2(pc(op)reply_pin_numbers,);
if(data_read(op))
{
zepto_wait_for_pin(pc(op)ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 3; return WAIT;
}
else
{
if((_sa_state->some)(op))
{
zepto_wait_for_pin(pc(op)ack_pin_number,(_sa_state->some));
_sa_state->_sa_next = 4; return WAIT;
}
else
{
zepto_reply_append_byte2(reply,);
}
_sa_state->_sa_next = 5; return NEXT;
}
_sa_state->_sa_next = 6; return NEXT;
}
case 3:
{
zepto_read_from_pins3(pc(op)reply_pin_numbers,);
_sa_state->_sa_next = 6; return NEXT;
}
case 4:
{
zepto_reply_append_byte(reply,(_sa_state->some));
_sa_state->_sa_next = 5; return NEXT;
}
case 5:
{
zepto_reply_append_byte3(reply,);
_sa_state->_sa_next = 6; return NEXT;
}
case 6:
{
zepto_reply_append_byte4(reply,);
_sa_state->_sa_next = 0;
return ;
}
}
assert(false);
}
