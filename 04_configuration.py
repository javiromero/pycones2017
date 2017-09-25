#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# logging.basicConfig()  # ¡TRAMPA!
# logging.debug("Esto también dispara la configuración por defecto.")  # ¡TRAMPA!
logging.basicConfig(format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", level="ERROR")
abuelo = logging.getLogger('abuelo')
abuelo.setLevel('DEBUG')
padre = logging.getLogger('abuelo.padre')
padre.setLevel('INFO')
hijo = logging.getLogger('abuelo.padre.hijo')
hijo.setLevel('WARNING')


def main():
    abuelo.debug("Mensaje 1 DEBUG")
    abuelo.info("Mensaje 1 INFO")
    abuelo.warning("Mensaje 1 WARNING")

    padre.debug("Mensaje 2 DEBUG")
    padre.info("Mensaje 2 INFO")
    padre.warning("Mensaje 2 WARNING")

    hijo.debug("Mensaje 3 DEBUG")
    hijo.info("Mensaje 3 INFO")
    hijo.warning("Mensaje 3 WARNING")


if __name__ == '__main__':
    main()
