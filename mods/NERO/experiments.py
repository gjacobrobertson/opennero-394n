#import all client and server scripts
import NERO.module as module
import NERO.client
import NERO.agent
import NERO.constants as constants
import common
import common.menu_utils
import OpenNero

#import utility modules
import random
import math

MIN_DIST = 100
MAX_DIST = 250
FLAG_INTERVAL = 10000
STATS_INTERVAL = 100

experiment_tick = None
flag_ticks = 0
stats_ticks = 0

def log(tag, message):
    print "[{0}.{1}] {2}".format("experiments", tag, message)

def random_offset(min_dist, max_dist):
    angle = random.random() * 2 * math.pi
    dist = random.random() * (max_dist - min_dist) + min_dist
    x_offset = dist * math.cos(angle)
    y_offset = dist * math.sin(angle)
    return (x_offset, y_offset)

def update_flag(mod):
    #x_offset, y_offset = random_offset(MIN_DIST, MAX_DIST)
    x = mod.spawn_x[constants.OBJECT_TYPE_TEAM_0] - MIN_DIST
    y = mod.spawn_y[constants.OBJECT_TYPE_TEAM_0] - MIN_DIST
    log("update_flag", "New Flag Location {0},{1}".format(x, y))
    mod.change_flag([x, y, 0])

def log_stats(mod):
    team = constants.OBJECT_TYPE_TEAM_0
    distances = []
    for agent in mod.environment.teams[team]:
        pose = mod.environment.get_state(agent).pose
        flag_loc = (mod.flag_loc.x, mod.flag_loc.y, mod.flag_loc.z)
        distance = mod.environment.distance(flag_loc, pose)
        distances.append(distance)
    minimum = min(distances)
    mean = sum(distances) / len(distances)
    maximum = max(distances)
    log("stats", "min: {0}, mean: {1}, max: {2}".format(minimum, mean, maximum))

def train_flag_tick(dt):
    global flag_ticks, stats_ticks
    flag_ticks += 1
    stats_ticks += 1
    mod = NERO.module.getMod()
    if flag_ticks % FLAG_INTERVAL == 0:
        update_flag(mod)
        flag_ticks = 0
    if stats_ticks % STATS_INTERVAL == 0:
        log_stats(mod)
        stats_ticks = 0

def TrainFlag(ai):
    global experiment_tick
    experiment_tick = train_flag_tick
    mod = NERO.module.getMod()
    mod.deploy(ai)
    update_flag(mod)
    key = getattr(constants, "FITNESS_APPROACH_FLAG", None)
    mod.set_weight(key, 200)

