#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def configure_logging_destinations():
    """Definiciones y configuraciones iniciales."""
    handler_console = logging.StreamHandler()
    handler_file = logging.FileHandler('pycones2017.log')

    formatter = logging.Formatter('%(name)-8s: %(levelname)-8s (%(message)s)')

    handler_console.setFormatter(formatter)
    logger.addHandler(handler_console)

    handler_file.setFormatter(formatter)
    logger.addHandler(handler_file)

    logger.setLevel("DEBUG")


def main():
    """Registra mensajes de distintos niveles."""
    logger.debug("Detalles de implementación...")
    logger.info("%s", "Mensajes informativos")
    logger.warning("Aviso")
    logger.error("Error")
    logger.critical("Fallo crítico")


if __name__ == '__main__':
    configure_logging_destinations()
    main()
