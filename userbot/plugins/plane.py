# By STARKTM1
import asyncio

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern=r"plane"))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await asyncio.sleep(1)
    await event.edit("-✈------------")
    await asyncio.sleep(1)
    await event.edit("--✈-----------")
    await asyncio.sleep(1)
    await event.edit("---✈----------")
    await asyncio.sleep(1)
    await event.edit("----✈---------")
    await asyncio.sleep(1)
    await event.edit("-----✈--------")
    await asyncio.sleep(1)
    await event.edit("------✈-------")
    await asyncio.sleep(1)
    await event.edit("-------✈------")
    await asyncio.sleep(1)
    await event.edit("--------✈-----")
    await asyncio.sleep(1)
    await event.edit("---------✈----")
    await asyncio.sleep(1)
    await event.edit("----------✈---")
    await asyncio.sleep(1)
    await event.edit("-----------✈--")
    await asyncio.sleep(1)
    await event.edit("------------✈-")
    await asyncio.sleep(1)
    await event.edit("-------------✈")
    await asyncio.sleep(5)
    await event.delete()
