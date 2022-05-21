# vector #
from math import sin, cos
#from numba import jit
import pygame
import time
import sys

pygame.init()
pygame.font.init()
bfont = pygame.font.Font('/System/Library/Fonts/AppleSDGothicNeo.ttc', 20)


class Screen(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self._rect = screen.get_rect()
        self.width = self._rect.width
        self.height = self._rect.height
        self.neww = self.width
        self.newh = self.height
        self.scale = 1
        self.ssx = 0
        self.ssy = 0
        self.check_time = 0
        self.time2 = 100
        self.fps = 0
        self.wait_time = 0
        self.videoresize = 10
        self.debug = False
        self.grid = []
        self.init_grid()
        self.fps_time = 0

    def init_grid(self):
        self.grid = []
        for i in range(self.height+1):
            self.grid.append([])
            for i2 in range(self.width+1):
                self.grid[-1].append(self.cpoint((i2, i)))

    def line(self, color, startx, starty, endx, endy, width=1):
        pygame.draw.line(self.screen, color, self.cpoint2(
            [startx, starty]), self.cpoint2([endx, endy]), max(1, int(width*self.scale)))

    def absline(self, color, startx, starty, endx, endy, width=1):
        pygame.draw.line(self.screen, color, (startx, starty),
                         (endx, endy), width)

    def lines(self, color, points, width=1):
        pygame.draw.lines(self.screen, color, False, tuple(
            map(self.cpoint2, points)), max(1, int(width*self.scale)))

    def abslines(self, color, points, width=1):
        pygame.draw.lines(self.screen, color, False, points, width)

    def polygon(self, color, points):
        pygame.draw.polygon(self.screen, color,
                            tuple(map(self.cpoint2, points)))

    def abspolygon(self, color, points):
        pygame.draw.polygon(self.screen, color, points)

    def circle(self, color, pos, radius, width=0):
        pygame.draw.circle(self.screen, color, self.cpoint2(pos), max(
            1, int(radius*self.scale)), int(width*self.scale))

    def abscircle(self, color, pos, radius, width=0):
        pygame.draw.circle(self.screen, color, pos, radius, width)

    def rect(self, color, rect):
        pygame.draw.rect(self.screen, color, self.cpoint2(
            [rect[0], rect[1]])+(rect[2]*self.scale, rect[3]*self.scale))

    def absrect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def absrect2(self, color, rect):
        pygame.draw.rect(self.screen, color, rect, 1)

    def cpoint(self, pos):
        return int(self.ssx + pos[0]*self.scale), int(self.ssy + pos[1]*self.scale)

    def cpoint2(self, pos):
        try:
            if pos[0] < 0 or pos[1] < 0:
                raise IndexError('list index out of range')
            return self.grid[int(pos[1])][int(pos[0])]
        except:
            return self.cpoint([int(pos[0]), int(pos[1])])

    def fill(self, color):
        self.screen.fill(color)

    def text(self, font, pos, color, text, center=True):
        f = font.render(text, True, color)
        rect = f.get_rect()
        pos = self.cpoint(pos)
        self.screen.blit(f, (pos[0]-rect.width/2, pos[1]-rect.height/2))

    def abstext(self, font, pos, color, text, center=True):
        f = font.render(text, True, color)
        if center:
            rect = f.get_rect()
            self.screen.blit(f, (pos[0]-rect.width/2, pos[1]-rect.height/2))
        else:
            self.screen.blit(f, pos)

    def blit(self, surface, pos, center=True):
        if not center:
            self.screen.blit(surface, (pos[0], pos[1]))
        else:
            rect = surface.get_rect()
            self.screen.blit(
                surface, (pos[0]-rect.width//2, pos[1]-rect.height//2))

    def svg(image):
        '''渲 染 矢 量 图'''
        if image.angle == 0:
            for surface in image.check():
                if surface[0] == 1:  # 一条线
                    self.line(
                        self.screen, surface[1], surface[2], surface[3], surface[4], surface[5], surface[6])
                elif surface[0] == 2:  # 多条线
                    self.lines(self.screen, surface[1], surface[2], surface[3])
                elif surface[0] == 3:  # 多边形
                    self.polygon(self.screen, surface[1], surface[2])
                elif surface[0] == 4:  # 矩形
                    self.rect(self.screen, surface[1], surface[2])
        # else:

    def check(self, event_get):
        global debug
        events = []
        for event in event_get:
            events.append(event)
            if event.type == pygame.VIDEORESIZE:
                self.videoresize = 60
                self.neww = event.size[0]
                self.newh = event.size[1]
                self.screen = pygame.display.set_mode(
                    (self.neww, self.newh), pygame.RESIZABLE)
                if self.neww / self.width > self.newh / self.height:
                    self.scale = self.neww / self.width
                else:
                    self.scale = self.newh / self.height
                self.ssx = (self.neww - self.width * self.scale) // 2
                self.ssy = (self.newh - self.height * self.scale) // 2
                self.init_grid()
                self._rect = self.screen.get_rect()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    self.debug = bool(not self.debug)
            if event.type == pygame.QUIT:
                pygame.quit()
        self.check_time = time.time()
        return events

    def mouse_pos(self):
        pos = pygame.mouse.get_pos()
        return (pos[0]-self.ssx)/self.scale, (pos[1]-self.ssy)/self.scale

    def abs_mouse_pos(self):
        return pygame.mouse.get_pos()

    def update(self, maxfps):
        global bfont
        if self.debug:
            text = 'ssx:'+str(self.ssx)+'|'
            text += 'ssy:'+str(self.ssy)+'|'
            text += 'scale:'+str(int(self.scale*100)/100)+'|'
            text += '(' + str(self.neww) + ',' + str(self.newh) + ')'
            text += ' fps:'+str(self.fps)
            text += ' videoresize:'+str(self.videoresize > 0)
            f = bfont.render(text, True, (255, 255, 0))
            self.screen.blit(f, (20, 20))
        #pygame.display.flip()
        pygame.display.update()
        self.videoresize = max(self.videoresize-1, 0)
        self.clock.tick(maxfps)
        self.time2 = time.time()
        self.fps = int(1 / (self.time2 - self.check_time))
        self.fps_time = self.time2 - self.check_time
        self.wait_time = self.time2 - self.check_time


def init(screenw, screenh):
    screen = pygame.display.set_mode((screenw, screenh), pygame.RESIZABLE)
    return screen


'''
class SVG(object):
    def __init__(self,centerx,centery,scale=1,angle=0):
        self.surfaces = []
        self.csurfaces = []
        self.angle = angle
        self.centerx = x
        self.centery = y
        self.scale = scale

    def add_line(self,color,startx,starty,endx,endy,width=1):
        self.surfaces.append([1,color,startx,starty,endx,endy,width])

    def add_lines(self,color,points,width=1):
        self.surfaces.append([2,color,points,width])

    def add_polygon(self,color,points):
        self.surfaces.append([3,color,points])

    def add_rect(self,color,rect):
        self.surfaces.append([4,color,rect])

    def check(self):
        self.csurfaces = []
        if angle == 0:
            for i in self.surfaces:
                if i[0] == 1:
                    start = rotate([i[2],i[3]])
                    end = rotate([i[4],i[5]])
                    self.csurfaces.insert(0,[1,i[1],start[0],start[1],end[0],end[1],i[6]])
                elif i[0] == 2:
                    self.csurfaces.insert(0,[1,i[1],[]])
                    for i2 in i[2]:
                        self.csurfaces[0].append(
'''


def rotate(x, y, angle):
    x2 = x*cos(angle)-y*sin(angle)
    y2 = x*sin(angle)-y*cos(angle)
    return x2, y2


if __name__ == '__main__':
    s = Screen(init(800, 450))
    while True:
        s.check(pygame.event.get())
        s.fill((0, 0, 0))
        s.rect((0, 255, 0), (100, 100, 200, 200))
        s.line((255, 255, 255), 0, 0, 100, 100, 3)
        s.polygon((255, 0, 0), ((200, 200), (200, 300), (300, 300), (300, 200)))
        s.circle((255, 255, 255), (400, 225), 10)
        s.text(bfont, (200, 200), (255, 255, 255), '(200,200)')
        s.text(bfont, (200, 300), (255, 255, 255), '(200,300)')
        s.text(bfont, (300, 200), (255, 255, 255), '(300,200)')
        s.text(bfont, (300, 300), (255, 255, 255), '(300,300)')
        s.text(bfont, (400, 225), (0, 0, 255), '中央')
        mouse = s.mouse_pos()
        mouse2 = pygame.mouse.get_pos()
        s.line((255, 0, 255), mouse[0]-20, mouse[1], mouse[0]+20, mouse[1], 5)
        s.line((255, 0, 255), mouse[0], mouse[1]-20, mouse[0], mouse[1]+20, 5)
        s.text(bfont, (mouse[0], mouse[1]-30), (255, 0, 255),
               '鼠标:'+str(mouse2)+'  相对坐标:'+str(mouse))
        s.update(30)
