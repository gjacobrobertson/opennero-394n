#import all client and server scripts
import NERO.module as module
import NERO.client
import NERO.agent
import NERO.constants as constants
import common
import common.menu_utils
import OpenNero

import random
import math
import threading

def ModMain(mode = ""):
    NERO.client.ClientMain()

def ModTick(dt):
    # don't start the external menu if we are running in headless mode!
    if OpenNero.getAppConfig().rendertype == 'null':
        return
    script_server = module.getServer()
    data = script_server.read_data()
    while data:
        module.parseInput(data.strip())
        #script_server.write_data(data)
        data = script_server.read_data()

def StartEvolving():
    mod = NERO.module.getMod()
    mod.deploy('rtneat')

def TrainFlag(ai):
    mod = NERO.module.getMod()
    mod.set_weight("FITNESS_APPROACH_FLAG", 200)
    update_flag(mod)
    mod.deploy(ai)

def random_offset(min_dist, max_dist):
    angle = random.random() * 2 * math.pi
    dist = random.random() * (max_dist - min_dist) + min_dist
    x_offset = dist * math.cos(angle)
    y_offset = dist * math.sin(angle)
    return (x_offset, y_offset)

def update_flag(mod):
    threading.Timer(60.0, update_flag, [mod]).start()
    x_offset, y_offset = random_offset(20, 150)
    x = mod.spawn_x[constants.OBJECT_TYPE_TEAM_0] + x_offset
    y = mod.spawn_y[constants.OBJECT_TYPE_TEAM_0] + y_offset
    print "New Flag Location", x, y
    mod.change_flag([x, y, 0])
