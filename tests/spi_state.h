/* Add copyright banner here */


#if !defined __SA_SPI_PLUGIN_STATE_H__
#define __SA_SPI_PLUGIN_STATE_H__

#include <stdint.h>


typedef struct _spi_plugin_state {
uint8_t sa_next;
uint16_t response;
} spi_plugin_state;

#endif // __SA_SPI_PLUGIN_STATE_H__
