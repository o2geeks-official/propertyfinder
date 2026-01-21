import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from edyouapp_api.api.routers.admin_tasks import attach_admin_tasks
from edyouapp_api.api.routers.analysis_user_data import attach_post_analysis
from edyouapp_api.api.routers.apanel_invite import invite_apanel_attach
from edyouapp_api.api.routers.apanel_support import attach_apanel_support
from edyouapp_api.api.routers.apanel_user import attach_apanel_user
from edyouapp_api.api.routers.apanel_waitlist import attach_apanel_waitlist
from edyouapp_api.api.routers.app_status import attach_app_status
from edyouapp_api.api.routers.block import attach_block_user
from edyouapp_api.api.routers.calendar import attach_calender
from edyouapp_api.api.routers.call import attach_call
from edyouapp_api.api.routers.deals import attach_deals
from edyouapp_api.api.routers.ejabberd import attach_ejabberd
from edyouapp_api.api.routers.email_validation import attach_validate_email
from edyouapp_api.api.routers.events import attach_event
from edyouapp_api.api.routers.favourites import attach_favourites
from edyouapp_api.api.routers.file_api import attach_file_api
from edyouapp_api.api.routers.follows import attach_follows
from edyouapp_api.api.routers.foryou import attach_foryou
from edyouapp_api.api.routers.friends import attach_friends
from edyouapp_api.api.routers.groups import attach_groups
from edyouapp_api.api.routers.institutes import attach_institutes
from edyouapp_api.api.routers.invite import attach_invite
from edyouapp_api.api.routers.leader_board import attach_leader_board
from edyouapp_api.api.routers.login import attach_login
from edyouapp_api.api.routers.market import attach_marketplace
from edyouapp_api.api.routers.music import attach_music
from edyouapp_api.api.routers.notification_settings import attach_notification_settings
from edyouapp_api.api.routers.notifications import attach_notifications
from edyouapp_api.api.routers.poll import attach_poll
from edyouapp_api.api.routers.post import attach_post
from edyouapp_api.api.routers.profile import attach_user_profile
from edyouapp_api.api.routers.reels import attach_reels
from edyouapp_api.api.routers.register import attach_register
from edyouapp_api.api.routers.report import attach_report_stuff
from edyouapp_api.api.routers.school import attach_school
from edyouapp_api.api.routers.search import attach_search
from edyouapp_api.api.routers.suggest import attach_suggest
from edyouapp_api.api.routers.suggest_v1 import attach_suggest_v1
from edyouapp_api.api.routers.unfollow import attach_unfollow_user
from edyouapp_api.api.routers.user import attach_user
from edyouapp_api.api.routers.webhook import attach_webhook
from edyouapp_api.asgi import get_application
from edyouapp_api.api.routers.apscheduler import attach_apscheduler

app: FastAPI = get_application()

attach_apscheduler(app=app)
attach_app_status(app=app)
attach_file_api(app=app)
attach_marketplace(app=app)
attach_deals(app=app)
attach_apanel_user(app)
attach_apanel_support(app)
invite_apanel_attach(app)
attach_apanel_waitlist(app)
attach_institutes(app)
attach_register(app)
attach_validate_email(app)
attach_login(app)
attach_user(app)
attach_admin_tasks(app)
attach_leader_board(app)
attach_unfollow_user(app)
attach_report_stuff(app)
attach_block_user(app)
attach_follows(app)
attach_poll(app)
attach_reels(app)
attach_user_profile(app)
attach_friends(app)
attach_post(app)
attach_groups(app)
attach_school(app)
attach_search(app)
attach_favourites(app)
attach_event(app)
attach_calender(app)
attach_notifications(app)
attach_notification_settings(app)
attach_foryou(app)
attach_suggest(app)
attach_suggest_v1(app)
attach_invite(app)
attach_ejabberd(app)
attach_call(app)
attach_post_analysis(app)
attach_music(app)
attach_webhook(app)

static_path_str = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "static",
)
app.mount(
    "/social/static",
    StaticFiles(directory=static_path_str),
    name="social/static",
)
