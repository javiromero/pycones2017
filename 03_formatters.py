#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import subprocess

logger = logging.getLogger(__name__)


class TTSHandler(logging.Handler):
    def emit(self, record):
        msg = self.format(record)
        cmd = ['espeak', '-s180', '-ven+f3', msg]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.communicate()


def configure_logging_formats():
    """Definiciones y configuraciones iniciales."""
    handler_console = logging.StreamHandler()
    fmt = '%(name)-8s: %(levelname)-8s (%(message)s)'
    formatter_console = logging.Formatter(fmt)
    handler_console.setFormatter(formatter_console)
    logger.addHandler(handler_console)

    handler_file = logging.FileHandler('pycones2017.log', mode='w')
    fmt = '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s'
    formatter_file = logging.Formatter(fmt)
    handler_file.setFormatter(formatter_file)
    logger.addHandler(handler_file)

    # FIXME: UNMUTE THE LAPTOP!!!
    handler_tts = TTSHandler(level='WARNING')
    fmt = '%(levelname)s'
    formatter_tts = logging.Formatter(fmt)
    handler_tts.setFormatter(formatter_tts)
    logger.addHandler(handler_tts)

    logger.setLevel("DEBUG")



def main():
    """Registra mensajes de varios tipos."""
    logger.debug("Detalles de implementación...")
    logger.info("%s", "Mensajes informativos")
    logger.warning("Aviso")
    logger.error("Error")
    logger.critical("Fallo crítico")


if __name__ == '__main__':
    configure_logging_formats()
    main()
