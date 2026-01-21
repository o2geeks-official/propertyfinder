from fastapi import FastAPI

from edyouapp_api.api.models.notifications import ApnsPayloadModel
from edyouapp_api.workers.apple_notifications import simple_apns, voip_apns

app = FastAPI()


@app.get(path="/not/{notification_type}")
async def read_root(notification_type: str):
    sim_d_t = "8041a826de140d0831b26076230ac2cf21935c465d5c4fa30993e1b076ce85bae5e663aea9f1b20136875974e3ffe045d4ca4c57fb94ba2beee1247dda25a40be806f595b5696f57a3f0acc404fa5e3f"
    v_d_t = "8064da2c1db409ec57e1fdd8bb2dff2637f8ca6bef458bc44473d559650fb4ec7225f2e3a982cc6c77a387403955e693df6637e36710595eca27e0860d77f85685572aa53bbeeaae15d0879e14538003"

    payload = ApnsPayloadModel(
        alert="wssay sardar reacted to post '#QR#app' at Wednesday 08 2023",
        badge=1,
        sound="default",
        custom=None,
    )
    if notification_type == "simple":
        payload.custom = {
            "notification_id": "123",
            "action_name": "notification_data.action_name",
            "action_id_name": "notification_data.action_id_name",
            "action_id": "notification_data.action_id",
        }
        await simple_apns(
            device_token=sim_d_t,
            message=payload.model_dump(),
        )
    else:
        payload.custom = {
            "notification_id": "123",
            "action_name": "notification_data.action_name",
            "action_id_name": "notification_data.action_id_name",
            "action_id": "notification_data.action_id",
        }
        await voip_apns(
            device_token=v_d_t,
            message=payload.model_dump(),
        )
    return {"Hello": "World"}
