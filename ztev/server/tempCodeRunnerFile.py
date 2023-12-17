#!/usr/bin/env python
from flask import Flask,redirect, render_template, url_for
from flask_oidc import OpenIDConnect
from config import *
from models import *
from resources.topic import TopicAPI
from resources.role import RoleGrantAPI
from resources.invite import InviteAPI
from resources.vote import VoteAPI
from resources.option import TopicOptionAPI
from jose import jwk, jwt
from jose.utils import base64url_decode
import os
