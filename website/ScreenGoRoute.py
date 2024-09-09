from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

# from .db import dbORM
from . import DateToolKit as dtk

import base64
import imghdr
# from . import encrypt

from .SarahDBClient.db import db
from .SarahDBClient.db import dbORM
from .SarahDBClient import encrypt

import random
from . import function_pool
import datetime as dt
from . import id_generator
from datetime import datetime

User, Record = dbORM.get_all("UserFBET"), None
	
								# <!-- <img src="data:{{ getMIME( Task['image_raw'] ) }};base64,{{ Task['image_raw'] }}" style="background: white; aspect-ratio: 1/1; width: 40px; padding: 20px; object-fit: cover;"> -->


def go_to(screen_id, _redirect=False, **kwargs):
	if _redirect == False:
		u = dbORM.get_all("UserFBET")[f'{current_user.id}']

		def checkImagePassError(image_raw):
			try:
				rr = f"data:{function_pool.getMIME(image_raw)};base64,{image_raw}"
				return "false"
			except:
				return "true"

		return render_template("dashboard.html",
			CUser = u,		
			ImagePassError = checkImagePassError,

			ScreenID = screen_id,

			DTK = dtk,
			LengthFunc = len,
			ToJoin = function_pool.toJoin,
			DeviceType = function_pool.detectDeviceType(kwargs['request']),
			WhichDevice = function_pool.which_device,
			GetDBItem = function_pool.getDBItem,
			ToString = str,
			RoundFloat = round,
			referral_data = function_pool.referral_data(),
			CurrentDate = function_pool.getDateTime()[0],
			ToFloat = float,
			ToInt = int,
			CurrencyExchange = function_pool.CurrencyExchange(),
			RandomID = id_generator.generateTID,
			PythonEval = function_pool.python_eval,
			ToFloatToInt = function_pool.floatToInt,
			Thousandify = function_pool.thousandify,
			getMIME = function_pool.get_mime_type,
			TimeDifference = function_pool.calcTimeDifference,
			CurrentTime = function_pool.getDateTime()[1],
			HTMLBreak_ = function_pool.HTMLBreak
		)
	else:
		return redirect(url_for("views.dashboard"))
	