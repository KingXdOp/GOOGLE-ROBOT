from geopy.geocoders import Nominatim
from telethon import *
from telethon.tl import *

from FallenRobot import *
from FallenRobot import telethn as tbot
from FallenRobot.events import register

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps (.*)")
async def _(event):
    args = event.pattern_match.group(1)

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await tbot.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(latitude), float(longitude))
            ),
        )
        await event.reply(
            "Open with: [๐Google Maps]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")


__help__ = """
Sends you the gps location of the given query...

 โ /gps <location>*:* Get gps location.
โคออออโข๐๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ โโ๐[@THE_VIP_BOY](https://t.me/the_vip_boy)โฆโอ๐ฎ๐ณ๐
"""

__mod_name__ = "โป๏ธ๐๐๐๐"
