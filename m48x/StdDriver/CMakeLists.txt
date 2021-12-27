# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2020 Linumiz
# Author: Saravanan Sekar <saravanan@linumiz.com>

zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_HAL src/sys.c)

zephyr_library_sources(src/clk.c)
zephyr_library_sources(src/gpio.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/uart.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/usci_uart.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/spim.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/usbd.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/fmc.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/i2c.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/crc.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/eadc.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/ecap.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/timer.c)
zephyr_library_sources_ifdef(CONFIG_HAS_NUMICRO_UART src/crypto.c)
