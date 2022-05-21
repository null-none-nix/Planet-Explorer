from math import sin, cos, pi, sqrt

bgcolor = None


def get_circle_size(pos, radius):
    return radius / pos[2] * FOV


class Circle3d(object):
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.pos = pos
        self.color = color

    def render(self):
        vector.Screen.circle(self.color, shapes.e_2d_point(
            self.pos), get_circle_size(self.radius))


def e_3d_fill(surfaces, colorful):
    _surfaces = []
    for i in surfaces:
        color = i.pop()
        _surfaces.append(i)
        _surfaces[-1].append([color[0]+(bgcolor[0]-color[0])*colorful,
                              color[1]+(bgcolor[1]-color[1])*colorful,
                              color[2]+(bgcolor[2]-color[2])*colorful])
    return _surfaces


def e_3d_fill2(surface, colorful):
    for i in range(len(surfaces)):
        surfaces[i][-1] = [surfaces[i][-1][0]*colorful,
                           surfaces[i][-1][1]*colorful,
                           surfaces[i][-1][2]*colorful]
# def e_3d_fill_surfaces(surfaces,colorful):


def e_2d_point(pos):
    if pos[2] < 0.1:
        return False
    return [pos[0]/pos[2]*FOV+screen_c[0], screen_c[1]-pos[1]/pos[2]*FOV]


def e_3d_fill_surface(surface, colorful):
    # colorful 0~1
    global bgcolor
    surface[-1] = [surface[-1][0]+(bgcolor[0]-surface[-1][0])*colorful,
                   surface[-1][1]+(bgcolor[1]-surface[-1][1])*colorful,
                   surface[-1][2]+(bgcolor[2]-surface[-1][2])*colorful]


def e_2d_cut_gx1(p1, p2):
    # print(p1,p2)
    return [0, p1[1]+(-p1[0])/(p2[0]-p1[0])*(p2[1]-p1[1])]


def e_2d_cut_gx2(p1, p2):
    return [1200, p1[1]+(p1[0]-1200)/(p1[0]-p2[0])*(p2[1]-p1[1])]


def e_2d_cut_gy1(p1, p2):
    return [p1[0]+(-p1[1])/(p2[1]-p1[1])*(p2[0]-p1[0]), 0]


def e_2d_cut_gy2(p1, p2):
    return [p1[0]+(p1[1]-675)/(p1[1]-p2[1])*(p2[0]-p1[0]), 675]


def e_2d_cut_out__(p):
    if p[0] < 0 or p[1] < 0 or p[0] > 1200 or p[1] > 675:
        return True
    return False


def e_2d_cut_out2__(p):
    sw = 0
    if p[0] < 0:
        sw += 1
    if p[1] < 0:
        sw += 1
    if p[0] > 1200:
        sw += 1
    if p[1] > 675:
        sw += 1
    if sw == 2:
        return True
    return False


def e_2d_cut_set2__(p):
    if p[0] < 0:
        p[0] = 0
    if p[1] < 0:
        p[1] = 0
    if p[0] > 1200:
        p[0] = 1200
    if p[1] > 675:
        p[1] = 675


def e_2d_cut(surface):
    _s = 0
    cut = False
    # print(surface)
    for i in range(len(surface)-1, -1, -1):
        if e_2d_cut_out__(surface[i]):
            _s += 1
            if e_2d_cut_out2__(surface[i]):
                _s -= 1
                e_2d_cut_set2__(surface[i])
            if _s > 2:
                surface.pop(i+1)
            cut = True
        else:
            _s = 0

    # if e_2d_cut_out__(surface[-1]):
    #    _s += 1
    #    if _s > 2:
    #        surface.pop(0)
    #    cut = True
    '''
    L = len(surface)
    #print(surface)
    changes = []
    for i in range(L):
        changes.append(False)
    if cut and L > 2:
        i = 0
        while i < L:
            if surface[i][0] < 0:
                if e_2d_cut_out__(surface[(i+1)%L]) and not changes[(i-1)%L]:
                    # ((i-1)%L,0) > 0
                    surface[i] = e_2d_cut_gx1(surface[i],surface[(i-1)%L])
                    changes[i] = True
                else:
                    surface[i] = e_2d_cut_gx1(surface[i],surface[(i+1)%L])
                    changes[i] = True
                    if not e_2d_cut_out__(surface[(i-1)%L]) and not changes[(i+1)%L]:
                        surface.append(e_2d_cut_gx1(surface[i],surface[(i-1)%L]))
                        changes.insert(i,True)
                        L += 1
                        i += 1
            if surface[i][1] < 0:
                if e_2d_cut_out__(surface[(i+1)%L]) and not changes[(i-1)%L]:
                    surface[i] = e_2d_cut_gy1(surface[i],surface[(i-1)%L])
                    changes[i] = True
                else:
                    surface[i] = e_2d_cut_gy1(surface[i],surface[(i+1)%L])
                    changes[i] = True
                    if not e_2d_cut_out__(surface[(i-1)%L]) and not changes[(i+1)%L]:
                        surface.append(e_2d_cut_gy1(surface[i],surface[(i-1)%L]))
                        changes.insert(i,True)
                        L += 1
                        i += 1
            if surface[i][0] > 1200:
                if e_2d_cut_out__(surface[(i+1)%L]) and not changes[(i-1)%L]:
                    surface[i] = e_2d_cut_gx2(surface[i],surface[(i-1)%L])
                    changes[i] = True
                else:
                    surface[i] = e_2d_cut_gx2(surface[i],surface[(i+1)%L])
                    changes[i] = True
                    if not e_2d_cut_out__(surface[(i-1)%L]) and not changes[(i+1)%L]:
                        surface.append(e_2d_cut_gx2(surface[i],surface[(i-1)%L]))
                        changes.insert(i,True)
                        L += 1
                        i += 1
            if surface[i][1] > 675:
                if e_2d_cut_out__(surface[(i+1)%L]) and not changes[(i-1)%L]:
                    surface[i] = e_2d_cut_gy2(surface[i],surface[(i-1)%L])
                    changes[i] = True
                else:
                    surface[i] = e_2d_cut_gy2(surface[i],surface[(i+1)%L])
                    changes[i] = True
                    if not e_2d_cut_out__(surface[(i-1)%L]) and not changes[(i+1)%L]:
                        surface.append(e_2d_cut_gy2(surface[i],surface[(i-1)%L]))
                        changes.insert(i,True)
                        L += 1
                        i += 1
            i += 1
    #print(surface)
    '''
    try:
        L = len(surface)
        changes = []
        for i in range(L):
            changes.append(False)
        if cut and L > 2:
            i = 0
            while i < L:
                if surface[i][0] < 0:
                    if e_2d_cut_out__(surface[(i+1) % L]) or changes[(i+1) % L]:
                        surface[i] = e_2d_cut_gx1(
                            surface[i], surface[(i-1) % L])
                        changes[i] = True
                    else:
                        if not (e_2d_cut_out__(surface[(i-1) % L]) or changes[(i-1) % L]):
                            surface.insert(i, e_2d_cut_gx1(
                                surface[i], surface[(i-1) % L]))
                            changes.insert(i, True)
                            L += 1
                            i += 1
                            surface[i] = e_2d_cut_gx1(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                        else:
                            surface[i] = e_2d_cut_gx1(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                if surface[i][1] < 0:
                    if e_2d_cut_out__(surface[(i+1) % L]) or changes[(i+1) % L]:
                        surface[i] = e_2d_cut_gy1(
                            surface[i], surface[(i-1) % L])
                        changes[i] = True
                    else:
                        if not (e_2d_cut_out__(surface[(i-1) % L]) or changes[(i-1) % L]):
                            surface.insert(i, e_2d_cut_gy1(
                                surface[i], surface[(i-1) % L]))
                            changes.insert(i, True)
                            L += 1
                            i += 1
                            surface[i] = e_2d_cut_gy1(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                        else:
                            surface[i] = e_2d_cut_gy1(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                if surface[i][0] > 1200:
                    if e_2d_cut_out__(surface[(i+1) % L]) or changes[(i+1) % L]:
                        surface[i] = e_2d_cut_gx2(
                            surface[i], surface[(i-1) % L])
                        changes[i] = True
                    else:
                        if not (e_2d_cut_out__(surface[(i-1) % L]) or changes[(i-1) % L]):
                            surface.insert(i, e_2d_cut_gx2(
                                surface[i], surface[(i-1) % L]))
                            changes.insert(i, True)
                            L += 1
                            i += 1
                            surface[i] = e_2d_cut_gx2(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                        else:
                            surface[i] = e_2d_cut_gx2(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                if surface[i][1] > 675:
                    if e_2d_cut_out__(surface[(i+1) % L]) or changes[(i+1) % L]:
                        surface[i] = e_2d_cut_gy2(
                            surface[i], surface[(i-1) % L])
                        changes[i] = True
                    else:
                        if not (e_2d_cut_out__(surface[(i-1) % L]) or changes[(i-1) % L]):
                            surface.insert(i, e_2d_cut_gy2(
                                surface[i], surface[(i-1) % L]))
                            changes.insert(i, True)
                            L += 1
                            i += 1
                            surface[i] = e_2d_cut_gy2(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                        else:
                            surface[i] = e_2d_cut_gy2(
                                surface[i], surface[(i+1) % L])
                            changes[i] = True
                i += 1
    except:
        None
        # print(surface)


def e_2d_surface(surface):
    # print(surface)
    i = 0
    while i < len(surface)-1:
        surface[i] = e_2d_point(surface[i])
        if not surface[i]:
            surface.pop(i)
            i -= 1
        i += 1


def e_2d_surfaces(surfaces):
    for i in range(len(surfaces)):
        e_2d_surface(surfaces[i])


def e_3d_p_rot(point, angles):
    pos = [0, 0, 0]
    pos[0] = point[0]*cos(angles[0])+point[2]*sin(angles[0])
    pos[2] = point[2]*cos(angles[0])-point[0]*sin(angles[0])

    pos[1] = point[1]*cos(angles[1])+pos[2]*sin(angles[1])
    pos[2] = pos[2]*cos(angles[1])-point[1]*sin(angles[1])

    return pos


def e_3d_rot(surfaces, angles):
    for i in range(len(surfaces)):
        for i2 in range(len(surfaces[i])-1):
            surfaces[i][i2] = e_3d_p_rot(surfaces[i][i2], angles)


def e_3d_smove(surface, change):
    _surface = []
    # print(surface)
    for i in surface:
        if i != surface[-1]:
            _surface.append([i[0]+change[0], i[1]+change[1], i[2]+change[2]])
        else:
            _surface.append(i)
    return _surface


def e_3d_ssmove(surfaces, change):
    _surfaces = []
    # print("surfaces:",surfaces)
    for i in surfaces:
        _surfaces.append(e_3d_smove(i, change))
    return _surfaces


def e_3d_smove2(surface, change):
    # print(surface)
    for i in range(len(surface)-1):
        surface[i][0] += change[0]
        surface[i][1] += change[1]
        surface[i][2] += change[2]


def e_3d_ssmove2(surfaces, change):
    # print("surfaces:",surfaces)
    for i in range(len(surfaces)):
        e_3d_smove2(surfaces[i], change)


def e_2d_dis(pos):
    return -pos[1]*10000+sqrt(pos[0]**2+pos[2]**2)


def e_2d_sort_key(surface):
    minn = float('inf')
    for i in surface:
        if i != surface[-1]:
            minn = min(minn, e_2d_dis(i))
    return minn


def e_2d_sort_key2(surface):
    minn = float('inf')
    for i in surface:
        if i != surface[-1]:
            minn = min(minn, i[2])
    return minn


def e_2d_dis2(pos):
    return sqrt(pos[0]**2+pos[1]**2+pos[2]**2)


def e_2d_sort_key3(surface):
    if type(surface) == class_ball:
        return e_2d_dis2(surface.pos)-surface.radius
    minn = float('inf')
    for i in surface:
        if i != surface[-1]:
            minn = min(minn, e_2d_dis2(i))
    return minn


def e_2d_sort_key4(surface):
    if type(surface) == Circle3d:
        return e_2d_dis2(surface.pos)
    _sum = 0
    for i in surface:
        if i != surface[-1]:
            _sum += e_2d_dis2(i)
    return _sum/(len(surface)-1)


def gear(radius, radius2, num, num2, num3):
    '''
    num >= 4
    0 <= num2,num3 < 0.5
    '''
    rlist = []
    radius3 = radius + (radius2 - radius) * num3
    radius4 = radius2 - (radius2 - radius) * num3
    for i in range(num):
        rlist.append(rotate(radius3, 0, i*2/num*pi))
        rlist.append(rotate(radius4, 0, i*2/num*pi))
        rlist.append(rotate(radius2, 0, (i*2+num2)/num*pi))
        rlist.append(rotate(radius2, 0, (i*2+1-num2)/num*pi))
        rlist.append(rotate(radius4, 0, (i*2+1)/num*pi))
        rlist.append(rotate(radius3, 0, (i*2+1)/num*pi))
        rlist.append(rotate(radius, 0, (i*2+1+num2)/num*pi))
        rlist.append(rotate(radius, 0, (i*2+2-num2)/num*pi))
    return rlist


def rotate(x, y, alpha):
    return [x*cos(alpha)-y*sin(alpha), x*sin(alpha)+y*cos(alpha)]


def rotate_points(point_list, alpha):
    _list = []
    for i in point_list:
        _list.append(rotate(i[0], i[1], alpha))
    return _list


def move(pointlist, addx, addy):
    _pointlist = []
    for i in pointlist:
        _pointlist.append([i[0]+addx, i[1]+addy])
    return _pointlist


class_ball = Circle3d
if __name__ == '__main__':
    import pygame
    import time
    import sys
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    count = 4
    while True:
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        pygame.draw.aalines(screen, (0, 255, 0), True, move(
            gear(40, 70, count, 0.15, 0.15), 100, 100))
        pygame.display.update()
        time.sleep(1)
