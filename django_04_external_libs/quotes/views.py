import logging
import requests

from django.http import HttpResponse


logger = logging.getLogger(__name__)

def index(request):
    """Recupera una cita diaria y la devuelve formateada junto a su autor."""

    logger.info("Recuperamos una cita y la devolvemos formateada.")
    logger.warning("Sólo permite 10 llamadas por hora. Puede explotar.")
    try:
        logger.info("Conectando a quotes.rest...")
        response = requests.get('http://quotes.rest/qod.json?category=inspire')
        quote = response.json()['contents']['quotes'][0]['quote']
        author = response.json()['contents']['quotes'][0]['author']
    except:
        logger.error("Máximo de conexiones por hora alcanzado.")
        quote = "Sh*t happens"
        author = "Anonymous"

    body = (
        "<div style='margin: 10em; text-align: justified;'>"
        "<h1>{quote}</h1>"
        "<p style='text-align: right'>{author}</p>"
        "</div>".format(quote=quote, author=author))
    return HttpResponse(body)
