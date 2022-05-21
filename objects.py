from numpy import array
from shapes import Circle3d, e_3d_p_rot
from math import pi
from random import randint


def print_array(_list):
    print(array(_list))


class Queue(object):
    def __init__(self):
        self._list = []
        self.first_idx = 0

    def pop(self):
        self.first_idx += 1
        return [self._list[self.first_idx-1], self.first_idx-1]

    def push(self, data):
        self._list.append(data)

    def empty(self):
        return self.first_idx == len(self._list)

    def at(self, index):
        return self._list[index]


class PriorityQueue(object):
    def __init__(self):
        self._list = []

    def pop(self):
        return self._list.pop()

    def push(self, data, value):
        left = 0
        right = len(self._list)
        while left < right - 1:
            mid = (left + right) // 2
            if self._list[mid][1] > value:
                right = mid
            else:
                left = mid
        self._list.insert(left, [data, value])
        # print(len(self._list))

    def empty(self):
        return len(self._list) == 0


class PriorityQueue2(object):
    def __init__(self):
        self._list = []
        self.first_idx = 0

    def pop(self):
        self.first_idx += 1
        #print(len(self._list), self.first_idx)
        return [self._list[self.first_idx-1][0], self.first_idx-1]

    def push(self, data, value):
        left = self.first_idx
        right = len(self._list)
        while left < right - 1:
            mid = (left + right) // 2
            if self._list[mid][1] > value:
                right = mid
            else:
                left = mid
        self._list.insert(left, [data, value])

    def at(self, index):
        return self._list[index][0]

    def empty(self):
        return self.first_idx == len(self._list)


def dis2d(pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def out_of_map(map_width, pos):
    return not(0 <= pos[0] < map_width and 0 <= pos[1] < map_width)


def angle_dis(angle1, angle2):
    return min(abs(angle1-angle2), angle1-angle2+16, angle2-angle1+16)


def turn_way(angle1, angle2):
    if abs(angle1-angle2) <= 8:
        if angle1 < angle2:
            return 1
        return -1
    if angle1 < angle2:
        return -1
    return 1


def _move3d(surfaces, addx, addy, addz):
    _surfaces = []
    for i in range(len(surfaces)):
        _surfaces.append([])
        for i2 in range(len(surfaces[i])-1):
            _surfaces[i].append(
                [surfaces[i][i2][0]+addx, surfaces[i][i2][1]+addy, surfaces[i][i2][2]+addz])
        _surfaces[i].append(surfaces[i][-1])
    return _surfaces


def e_3d_rot(surfaces, angles):
    _surfaces = []
    for i in range(len(surfaces)):
        _surfaces.append([])
        for i2 in range(len(surfaces[i])-1):
            _surfaces[i].append(e_3d_p_rot(surfaces[i][i2], angles))
        _surfaces[i].append(surfaces[i][-1])
    return _surfaces


class Robot1(object):
    def __init__(self, pos, movement_speed, rotate_speed):
        self.pos = pos
        self.angle = 0
        self.render_pos = self.pos
        self.render_angle = self.angle
        self.path = []
        self.target = []
        self.code = []
        self.type = []
        self.map_width = None
        self.next_way = None
        self.speed = movement_speed
        self.rotate_speed = rotate_speed
        self.mode = 0  # 自由探索
        self.tick_time = 0
        self.high = 8.64

    def init(self, width, code):
        self.map_width = width
        self.code = code

    def return_render_surfaces(self, rotate_angles, camera_position, world_w):
        # print(e_3d_rot(_move3d(e_3d_rot([[[0, 0, 0], [0, 0, 0]]], [get_rotate_angle(self.render_angle), rotate_angles[1]]),
        #                       self.render_pos[0]-world_w-camera_position[0], self.high-camera_position[2], self.render_pos[1]-camera_position[1]), rotate_angles))
        if abs(self.render_pos[0]/3-camera_position[0]) > abs(self.render_pos[0]/3-camera_position[0]+self.map_width/3):
            if abs(self.render_pos[1]/3-camera_position[1]) < abs(self.render_pos[1]/3-camera_position[1]+self.map_width/3):
                return e_3d_rot(_move3d(e_3d_rot(robot_body, [1.57-get_rotate_angle(self.render_angle), 0]),
                                        self.render_pos[0]/3-camera_position[0]+self.map_width/3,self.high-camera_position[2],
                                        self.render_pos[1]/3-camera_position[1]), rotate_angles)
            else:
                return e_3d_rot(_move3d(e_3d_rot(robot_body, [1.57-get_rotate_angle(self.render_angle), 0]),
                                        self.render_pos[0]/3-camera_position[0]+self.map_width/3,self.high-camera_position[2],
                                        self.render_pos[1]/3-camera_position[1]+self.map_width/3), rotate_angles)
        else:
            if abs(self.render_pos[1]/3-camera_position[1]) < abs(self.render_pos[1]/3-camera_position[1]+self.map_width/3):
                return e_3d_rot(_move3d(e_3d_rot(robot_body, [1.57-get_rotate_angle(self.render_angle), 0]),
                                        self.render_pos[0]/3-camera_position[0],self.high-camera_position[2],
                                        self.render_pos[1]/3-camera_position[1]), rotate_angles)
            else:
                return e_3d_rot(_move3d(e_3d_rot(robot_body, [1.57-get_rotate_angle(self.render_angle), 0]),
                                        self.render_pos[0]/3-camera_position[0],self.high-camera_position[2],
                                        self.render_pos[1]/3-camera_position[1]+self.map_width/3), rotate_angles)

    def set_target(self):
        pq = Queue()
        pq.push([self.pos, None])
        done = False
        book = []
        for i in range(self.map_width):
            book.append([])
            for i2 in range(self.map_width):
                book[i].append(False)
        while not (done or pq.empty()):
            point_data, point_index = pq.pop()
            pos, last_point_index = point_data
            if not searched[pos[1]][pos[0]]:
                done = True
                self.target = pos.copy()
                break
            # print(pos,step)
            for way in search_ways:
                if randint(0, 2) > 0:
                    continue
                check_way, to, dis = way
                can_go = True
                for bk in check_way:
                    if out_of_map(self.map_width, [pos[0]+bk[0], pos[1]+bk[1]]):
                        can_go = False
                        break
                    # elif raw_map[(self.map_width-(pos[1]+bk[1])) % self.map_width][(self.map_width-(pos[0]+bk[0])) % self.map_width]:
                    elif raw_map[pos[1]+bk[1]][pos[0]+bk[0]]:
                        can_go = False
                        break
                if can_go:
                    if not book[pos[1]+to[1]][pos[0]+to[0]]:
                        book[pos[1]+to[1]][pos[0]+to[0]] = True
                        pq.push([[pos[0]+to[0], pos[1]+to[1]], point_index])
        if done:
            # print_array(book)
            # print(maxvalue)
            self.path = []
            pos = self.target
            last_index = point_index
            while pos != self.pos:
                self.path.insert(0, pos)
                last_point = pq.at(last_index)
                last_index = last_point[1]
                pos = last_point[0].copy()
            # print(self.path)
            if len(self.path) < 2:
                return True
            while self.path[-1] == self.path[-2]:
                self.path.pop(-1)
                if len(self.path) < 2:
                    return True
            return True
        else:
            return False

    def tick(self, time, mini_map, mini_map_scale):
        global searched
        self.tick_time += time
        if len(self.path) == 0:
            self.set_target()
            self.search()
            # self.next_way = -1
            return
        nextdpos = [self.path[0][0]-self.pos[0], self.path[0][1]-self.pos[1]]
        self.next_way = search_ways_dict[hash(tuple(nextdpos))]
        nextangle = search_ways_angle[self.next_way]
        if self.angle != nextangle:
            if self.tick_time >= angle_dis(nextangle, self.angle)/self.rotate_speed:
                self.tick_time -= angle_dis(nextangle,
                                            self.angle)/self.rotate_speed
                self.angle = nextangle % 16
                self.render_angle = self.angle
            else:
                self.render_angle = (self.angle + angle_dis(nextangle, self.angle) * turn_way(
                    self.angle, nextangle) * (self.tick_time/angle_dis(nextangle, self.angle)*self.rotate_speed)) % 16
                if self.render_angle >= 16:
                    self.render_angle -= 16
                return
        if self.next_way != -1:
            if self.mode == 0:
                while self.tick_time >= search_ways[self.next_way][2] / self.speed:
                    self.tick_time -= search_ways[self.next_way][2] / self.speed
                    self.pos = self.path.pop(0)
                    if len(self.path) == 0:
                        break
                    nextdpos = [self.path[0][0]-self.pos[0],
                                self.path[0][1]-self.pos[1]]
                    self.next_way = search_ways_dict[hash(tuple(nextdpos))]
                    nextangle = search_ways_angle[self.next_way]
                    print("nextangle:", nextangle)
                    if self.angle != nextangle:
                        if self.tick_time >= angle_dis(nextangle, self.angle)/self.rotate_speed:
                            self.tick_time -= angle_dis(nextangle,
                                                        self.angle)/self.rotate_speed
                            self.angle = nextangle % 16
                            self.render_angle = self.angle
                            # print("角度1")
                        else:
                            # print("角度2")
                            self.render_angle = (self.angle + angle_dis(nextangle, self.angle) * turn_way(
                                self.angle, nextangle) * (self.tick_time/angle_dis(nextangle, self.angle)*self.rotate_speed)) % 16
                            if self.render_angle >= 16:
                                self.render_angle -= 16
                            break
                if len(self.path) != 0:
                    self.render_pos = [self.pos[0]+(self.path[0][0]-self.pos[0])*(self.tick_time /
                                                                                  search_ways[self.next_way][2] * self.speed),
                                       self.pos[1]+(self.path[0][1]-self.pos[1])*(self.tick_time /
                                                                                  search_ways[self.next_way][2] * self.speed)]
                else:
                    self.render_pos = self.pos.copy()
                searched[int(self.render_pos[1])][int(
                    self.render_pos[0])] = True
                mini_map.set_at((int(self.render_pos[0]*mini_map_scale), int(
                    self.render_pos[1]*mini_map_scale)), (64, 64, 64))
        if len(self.path) == 0:
            self.set_target()

    def bind_camera(self, camera, world_w):
        camera[0] += (self.render_pos[0]/3-camera[0])/2
        camera[1] += (self.render_pos[1]/3-camera[1]-5)/2

    def search(self):
        pq = PriorityQueue2()
        pq.push([self.pos, 0, None], dis2d(self.pos, self.target))
        done = False
        book = []
        maxvalue = self.map_width ** 2
        for i in range(self.map_width):
            book.append([])
            for i2 in range(self.map_width):
                book[i].append(maxvalue+1)
        while not (done or pq.empty()):
            point_data, point_index = pq.pop()
            pos, step, last_point_index = point_data
            if pos[0] == self.target[0] and pos[1] == self.target[1]:
                done = True
                break
            # print(pos,step)
            for way in search_ways:
                check_way, to, dis = way
                can_go = True
                for bk in check_way:
                    if out_of_map(self.map_width, [pos[0]+bk[0], pos[1]+bk[1]]):
                        can_go = False
                        break
                    # elif raw_map[(self.map_width-(pos[1]+bk[1])) % self.map_width][(self.map_width-(pos[0]+bk[0])) % self.map_width]:
                    elif raw_map[pos[1]+bk[1]][pos[0]+bk[0]]:
                        can_go = False
                        break
                if can_go:
                    if book[pos[1]+to[1]][pos[0]+to[0]] > maxvalue:
                        book[pos[1]+to[1]][pos[0]+to[0]] = step+dis
                        pq.push([[pos[0]+to[0], pos[1]+to[1]], step+dis, point_index],
                                dis2d([pos[0]+to[0], pos[1]+to[1]], self.target)+step+dis)
        if done:
            # print_array(book)
            # print(maxvalue)
            self.path = []
            pos = self.target
            last_index = point_index
            while pos != self.pos:
                self.path.insert(0, pos)
                last_point = pq.at(last_index)
                last_index = last_point[2]
                pos = last_point[0].copy()
            # print(self.path)
            if len(self.path) < 2:
                return True
            while self.path[-1] == self.path[-2]:
                self.path.pop(-1)
                if len(self.path) < 2:
                    return True
            return True
        else:
            return False


raw_map = []
searched = []
search_ways = []
search_ways_dict = {}
search_ways_angle = []
search_ways_angle_dict = {}
search_way_len = 0


def add_way(check_ways, to, dis, angle):
    global search_ways, search_ways_dict, search_way_len
    search_ways.append([check_ways, to, dis])
    search_ways_dict[hash(tuple(to))] = search_way_len
    search_ways_angle.append(angle)
    search_way_len += 1
    search_ways_angle_dict[angle] = to


def set_map(map_of_world, width):
    global raw_map
    for i in range(width):
        raw_map.append([])
        for i2 in range(width):
            raw_map[i].append(not (map_of_world[i][i2] in [1, 2, 3]))


def init_search_place():
    for i in range(len(raw_map)):
        searched.append([])
        for i2 in range(len(raw_map)):
            searched[i].append(False)


add_way([[0, 1], [0, 2], [0, 3]], [0, 3], 3, 0)
add_way([[0, -1], [0, -2], [0, -3]], [0, -3], 3, 8)
add_way([[1, 0], [2, 0], [3, 0]], [3, 0], 3, 4)
add_way([[-1, 0], [-2, 0], [-3, 0]], [-3, 0], 3, 12)
add_way([[0, 1], [0, 2], [1, 1], [1, 2], [1, 3]], [1, 3], 3, 1)
add_way([[0, -1], [0, -2], [1, -1], [1, -2], [1, -3]], [1, -3], 3, 7)
add_way([[0, 1], [0, 2], [-1, 1], [-1, 2], [-1, 3]], [-1, 3], 3, 15)
add_way([[0, -1], [0, -2], [-1, -1], [-1, -2], [-1, -3]], [-1, -3], 3, 9)
add_way([[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]], [2, 2], 2.7, 2)
add_way([[0, -1], [1, 0], [1, -1], [1, -2], [2, -1], [2, -2]], [2, -2], 2.7, 6)
add_way([[0, 1], [-1, 0], [-1, 1], [-1, 2], [-2, 1], [-2, 2]], [-2, 2], 2.7, 14)
add_way([[0, -1], [-1, 0], [-1, -1], [-1, -2],
         [-2, -1], [-2, -2]], [-2, -2], 2.7, 10)
add_way([[0, 1]], [0, 1], 1, 0)
add_way([[0, -1]], [0, -1], 1, 8)
add_way([[-1, 0]], [-1, 0], 1, 12)
add_way([[1, 0]], [1, 0], 1, 4)
add_way([[1, 0], [0, 1], [1, 1]], [1, 1], 1.4, 2)
add_way([[-1, 0], [0, 1], [-1, 1]], [-1, 1], 1.4, 14)
add_way([[1, 0], [0, -1], [1, -1]], [1, -1], 1.4, 6)
add_way([[-1, 0], [0, -1], [-1, -1]], [-1, -1], 1.4, 10)
# /*print(search_ways)*/
robot_body = [[[-0.3, 0.36, 0.17], [-0.186, 0.504, 0.17], [-0.186, 0.696, 0.17], [0.186, 0.696, 0.17], [0.186, 0.504, 0.17], [0.3, 0.36, 0.17], (128, 128, 128)], [[-0.21, 0.408, 0.171], [-0.138, 0.48, 0.171], [-0.138, 0.648, 0.171], [0.138, 0.648, 0.171], [0.138, 0.48, 0.171], [0.21, 0.408, 0.171], (168, 166, 160)], [[-0.026, 0.628, 0.172], [0.026, 0.628, 0.172], [0.026, 0.47, 0.172], [-0.026, 0.47, 0.172], (63, 255, 67)], [[0.066, 0.628, 0.172], [0.118, 0.628, 0.172], [0.118, 0.47, 0.172], [0.066, 0.47, 0.172], (63, 255, 67)], [[-0.066, 0.628, 0.172], [-0.118, 0.628, 0.172], [-0.118, 0.47, 0.172], [-0.066, 0.47, 0.172], (63, 255, 67)], [[-0.3, 0.36, -0.17], [-0.186, 0.504, -0.17], [-0.186, 0.696, -0.17], [0.186, 0.696, -0.17], [0.186, 0.504, -0.17], [0.3, 0.36, -0.17], (128, 128, 128)], [[-0.21, 0.408, -0.171], [-0.138, 0.48, -0.171], [-0.138, 0.648, -0.171], [0.138, 0.648, -0.171], [0.138, 0.48, -0.171], [0.21, 0.408, -0.171], (168, 166, 160)], [[-0.026, 0.628, -0.172], [0.026, 0.628, -0.172], [0.026, 0.47, -0.172], [-0.026, 0.47, -0.172], (63, 255, 67)], [[0.066, 0.628, -0.172], [0.118, 0.628, -0.172], [0.118, 0.47, -0.172], [0.066, 0.47, -0.172], (63, 255, 67)], [[-0.066, 0.628, -0.172], [-0.118, 0.628, -0.172], [-0.118, 0.47, -0.172], [-0.066, 0.47, -0.172], (63, 255, 67)], [[0.186, 0.696, -0.17], [-0.186, 0.696, -0.17], [-0.186, 0.696, 0.17], [
    0.186, 0.696, 0.17], (219, 217, 208)], [[-0.186, 0.67, -0.17], [-0.186, 0.504, -0.17], [-0.25, 0.42, -0.17], [-0.25, 0.57, -0.17], (209, 207, 198)], [[-0.186, 0.67, 0.17], [-0.186, 0.504, 0.17], [-0.25, 0.42, 0.17], [-0.25, 0.57, 0.17], (209, 207, 198)], [[-0.186, 0.67, 0.17], [-0.186, 0.67, -0.17], [-0.186, 0.696, -0.17], [-0.186, 0.696, 0.17], (128, 128, 128)], [[-0.186, 0.67, 0.17], [-0.186, 0.67, -0.17], [-0.25, 0.57, -0.17], [-0.25, 0.57, 0.17], (214, 212, 203)], [[-0.25, 0.42, 0.17], [-0.25, 0.57, 0.17], [-0.25, 0.57, -0.17], [-0.25, 0.42, -0.17], (209, 207, 198)], [[-0.25, 0.42, 0.17], [-0.25, 0.42, -0.17], [-0.3, 0.36, -0.17], [-0.3, 0.36, 0.17], (135, 135, 135)], [[0.186, 0.67, 0.17], [0.25, 0.67, 0.17], [0.25, 0.42, 0.17], [0.186, 0.504, 0.17], (209, 207, 198)], [[0.186, 0.67, -0.17], [0.25, 0.67, -0.17], [0.25, 0.42, -0.17], [0.186, 0.504, -0.17], (209, 207, 198)], [[0.186, 0.67, 0.17], [0.186, 0.67, -0.17], [0.186, 0.696, -0.17], [0.186, 0.696, 0.17], (128, 128, 128)], [[0.186, 0.67, -0.17], [0.25, 0.67, -0.17], [0.25, 0.67, 0.17], [0.186, 0.67, 0.17], (229, 227, 218)], [[0.25, 0.67, -0.17], [0.25, 0.42, -0.17], [0.25, 0.42, 0.17], [0.25, 0.67, 0.17], (219, 217, 208)], [[0.25, 0.42, 0.17], [0.25, 0.42, -0.17], [0.3, 0.36, -0.17], [0.3, 0.36, 0.17], (135, 135, 135)]]


def get_rotate_angle(what_is_this):
    return (8-what_is_this)/8*pi


if __name__ == '__main__':
    import pygame
    import vector
    from math import pi
    from shapes import move, rotate
    pygame.init()
    raw_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    init_search_place()
    screen = vector.Screen(pygame.display.set_mode(
        (len(raw_map)*50, len(raw_map)*50), pygame.RESIZABLE))
    print(raw_map)
    r = Robot1([0, 0], 2, 5)
    r.init(9, [])
    r.target = [8, 8]
    print(r.search())
    print(r.path)
    max_fps = 30
    for i in range(100*max_fps):
        screen.check(pygame.event.get())
        screen.fill((255, 255, 255))
        for i2 in range(len(raw_map)):
            for i3 in range(len(raw_map[i2])):
                if raw_map[i2][i3]:
                    screen.rect((0, 255, 0), (i3*50, i2*50, 50, 50))
        if screen.fps == 0:
            r.tick(1/max_fps)
        else:
            r.tick(1/screen.fps)
        screen.rect(
            (0, 0, 255), (r.render_pos[0]*50+10, r.render_pos[1]*50+10, 30, 30))
        endpos = move([rotate(0, -50, get_rotate_angle(r.render_angle))],
                      r.render_pos[0]*50+25, r.render_pos[1]*50+25)
        screen.line(
            (255, 0, 0), r.render_pos[0]*50+25, r.render_pos[1]*50+25, endpos[0][0], endpos[0][1])
        # print(r.render_angle)
        screen.update(max_fps)
