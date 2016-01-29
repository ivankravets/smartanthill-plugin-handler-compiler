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

#include <stdio.h>
#include <stdlib.h>

#include "papi.h"

#define PREFIX(name) _PREFIX(SA_PLUGIN_ID, name)
#define _PREFIX(id, name) __PREFIX(id, name)
#define __PREFIX(id, name) id##name


int main(int argc, char *argv[]) {

    PREFIX(_plugin_config) config;
    PREFIX(_plugin_persistent_state) persist;
    char state_buffer[1024];
    
    uint8_t result = PREFIX(_plugin_exec_init)(&config, state_buffer);
    
    if (result != 0) {
        printf("Error, exec_init returned %d", result);
        return 1;
    }
    
    
    result = PREFIX(_plugin_handler_init)(&config, &persist);
    
    if (result != 0) {
        printf("Error, handler_init returned %d", result);
        return 1;
    }
    
    parser_obj parser = 0;
    MEMORY_HANDLE reply = 0;
    waiting_for waiting = 0;
    
    do {
        result = PREFIX(_plugin_handler)(&config, &persist, state_buffer, &parser, reply, &waiting, 0);
    } while (result > 0);
    
    if (result != 0) {
        printf("Error, handler returned %d", result);
        return 1;
    }
    printf("Ok");
    return 0;
}

void ZEPTO_ASSERT(bool condition) {assert(condition);}


// Request parsing functions:
uint8_t papi_parser_read_byte( parser_obj* po ) {return 0;}
uint16_t papi_parser_read_encoded_uint16( parser_obj* po ) {return 0;}
uint16_t papi_parser_read_encoded_signed_int16( parser_obj* po ) {return 0;}
//TODO: add vector-related functions

//Writing functions:
void papi_reply_write_byte( REPLY_HANDLE mem_h, uint8_t val ) {}
void papi_reply_write_encoded_uint16( REPLY_HANDLE mem_h, uint16_t num ) {}
void papi_reply_write_encoded_signed_int16( REPLY_HANDLE mem_h, int16_t sx ) {}
//TODO: add vector-related functions

//Misc functions:
void papi_init_parser_with_parser( parser_obj* po, const parser_obj* po_base ) {}
bool papi_parser_is_parsing_done( parser_obj* po ) {return false;}
uint16_t papi_parser_get_remaining_size( parser_obj* po ) {return 0;}

//EEPROM access
bool papi_eeprom_write( uint16_t plugin_id, const uint8_t* data ) {return false;}
bool papi_eeprom_read( uint16_t plugin_id, uint8_t* data ) {return false;}

void papi_eeprom_flush() {}

//Non-blocking calls to access hardware

bool papi_read_digital_pin( uint16_t pin_num ) {return false;}
void papi_write_digital_pin( uint16_t pin_num, bool value ) {}

void papi_start_sending_spi_command_16( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz) {}
void papi_start_sending_spi_command_32( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint32_t command, uint8_t command_sz) {}
void papi_start_sending_i2c_command_16( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz) {}
void papi_start_sending_i2c_command_32( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint32_t command, uint8_t command_sz) {}

void papi_start_receiving_spi_data_16( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t* data) {}
void papi_start_receiving_spi_data_32( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint32_t* data) {}
void papi_start_receiving_i2c_data_16( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t* data) {}
void papi_start_receiving_i2c_data_32( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint32_t* data) {}

void papi_cancel_spi_send( uint8_t spi_id ) {}
void papi_cancel_spi_receive( uint8_t spi_id ) {}
void papi_cancel_i2c_send( uint8_t i2c_id ) {}
void papi_cancel_i2c_receive( uint8_t i2c_id ) {}

//Blocking calls
void papi_sleep( uint16_t millisec ) {}

//Blocking calls to access hardware
void papi_wait_for_spi_send( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz ) {}
void papi_wait_for_i2c_send( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz ) {}
void papi_wait_for_spi_receive( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t* data ) {}
void papi_wait_for_i2c_receive( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t* data ) {}
void papi_wait_for_wait_handler( waiting_for* wf ) {}

//Helper functions to fill WAITING_FOR structure
void papi_init_wait_handler( waiting_for* wf ) {}
void papi_wait_handler_add_wait_for_spi_send( waiting_for* wf, uint8_t spi_id ) {}
void papi_wait_handler_add_wait_for_i2c_send( waiting_for* wf, uint8_t i2c_id ) {}
void papi_wait_handler_add_wait_for_spi_receive( waiting_for* wf, uint8_t spi_id ) {}
void papi_wait_handler_add_wait_for_i2c_receive( waiting_for* wf, uint8_t i2c_id ) {}
void papi_wait_handler_add_wait_for_timeout( waiting_for* wf, SA_TIME_VAL tv ) {}
bool papi_wait_handler_is_waiting_for_spi_send( const waiting_for* wf, uint8_t spi_id ) {return false;}
bool papi_wait_handler_is_waiting_for_i2c_send( const waiting_for* wf, uint8_t i2c_id ) {return false;}
bool papi_wait_handler_is_waiting_for_spi_receive( const waiting_for* wf, uint8_t spi_id ) {return false;}
bool papi_wait_handler_is_waiting_for_i2c_receive( const waiting_for* wf, uint8_t i2c_id ) {return false;}
bool papi_wait_handler_is_waiting_for_timeout( SA_TIME_VAL* remaining, const waiting_for* wf ) {return false;}
//TODO: think about parameters

//Yet unsorted calls
void papi_gravely_power_inefficient_micro_sleep( SA_TIME_VAL* timeval ) {}
