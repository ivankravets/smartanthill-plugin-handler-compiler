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

#if !defined __SA_EXPRESSION_PLUGIN_STATE_H__
#define __SA_EXPRESSION_PLUGIN_STATE_H__

#include <stdint.h>


typedef struct _expression_plugin_state {
uint8_t sa_next;
#line 49 "expression.c"
expression_plugin_data req;

uint8_t i;
} expression_plugin_state;

#endif // __SA_EXPRESSION_PLUGIN_STATE_H__
