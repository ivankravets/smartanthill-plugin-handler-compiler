/*****************************************************************************
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
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
    
*****************************************************************************/

#if !defined __SA_SUB_MACHINE2_PLUGIN_STATE_H__
#define __SA_SUB_MACHINE2_PLUGIN_STATE_H__

#include <stdint.h>


typedef struct _sub_machine2_plugin_state1 {
uint8_t sa_next;
} sub_machine2_plugin_state1;

typedef struct _sub_machine2_plugin_state2 {
uint8_t sa_next;
} sub_machine2_plugin_state2;

typedef struct _sub_machine2_plugin_state3 {
uint8_t sa_next;
} sub_machine2_plugin_state3;

typedef struct _sub_machine2_plugin_state {
uint8_t sa_next;
#line 72 "sub_machine2.c"
uint8_t res;
} sub_machine2_plugin_state;

#endif // __SA_SUB_MACHINE2_PLUGIN_STATE_H__
