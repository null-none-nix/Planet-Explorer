from multiprocessing import Process, Pipe
from _thread import start_new_thread
from math import sin, cos, sqrt, exp, log10
from vector import bfont
# from text import texts
from world_types import world_list as world_t
from shapes import *
from shapes import gear as create_gear
from shapes import rotate_points as e_2d_rotate
from shapes import move as e_2d_move
import shapes
import objects
# from numba import jit
# import random_world
import vector
import pygame
import random
import time
import sys
import os
#import gc
# gc.set_threshold(700,10,10)
# print('ALL')

print(sys.path[0])
path = sys.path[0] + "/"

pygame.mixer.pre_init(44100, 16, 2, 64, allowedchanges=0)
pygame.mixer.init()
pygame.font.init()
pygame.init()
pygame.display.set_caption('异星探索')
icon = pygame.image.load(path+'/imgs/icon.png')
pygame.display.set_icon(icon)
#screen = pygame.display.set_mode((800,450),pygame.RESIZABLE)
mode = 1  # 1:主菜单 2:学习


def change_block_scale(addx, addy, addz, scalex, scaley, scalez, data):
    _data = e_3d_ssmove(data, [addx, addy, addz])
    for i in range(len(_data)):
        color = _data[i].pop()
        for i2 in range(len(_data[i])):
            _data[i][i2] = [_data[i][i2][0]*scalex, _data[i]
                            [i2][1]*scaley, _data[i][i2][2]*scalez]
        _data[i].append(color)
    return _data


'''
def decode_text(text):
    rtext = []
    rtype = []
    i = 0
    while i - 1 < len(text):
        for i2 in text_types:
            if text[i:i+2] == i2:
                i += 2 
                copyi = i
                while not text[i] == text_end:
                    i += 1
                rtext.append(text[copyi:i])
                rtype.append(i2)
                break
        i += 1
    return rtext,rtype

def tlen(text):waawwawa
    length = 0
    for i in text:
        length += 1
        if ord(i) > 887:
            length += 1
    return length

def load_text(swidth):
    global text,fonts
    strs,types = decode_text(text)
    _width = 0
    height = 0
    
    for i in range(len(strs)):
        if 
        
def docs():
    global screen
    fade_in = 0
    bg = (180,230,255)
    mn1c = (160,160,160)
    mn1w = 150
    mn1h = 50
    mn1tc = (255,255,255)
    mn1cy = 0
    mn1y = 0
    choose = 0
    _font = pygame.font.Font('font.ttc',30)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] < mn1w:
                    choose = mouse[1] // mn1h
                    mn1cy = choose*mn1h
        mn1y += (mn1cy-mn1y)/3
        screen.check(events)
        screen.fill((bg[0]*fade_in,bg[1]*fade_in,bg[2]*fade_in))
        if fade_in < 1:
            fade_in += 0.05
            screen.absrect((mn1c[0]*fade_in,mn1c[1]*fade_in,mn1c[2]*fade_in),(0,0,mn1w,screen.height))
        else:
            fade_in = 1
            screen.absrect(mn1c,(0,0,mn1w,screen.height))
            starty = 0
            for i in text:
                screen.abstext(_font,(mn1w//2,starty+mn1h//2),mn1tc,i)
                starty += mn1h
            surface = pygame.Surface((mn1w,mn1h))
            surface.fill((255,255,255))
            surface.set_alpha(100)
            screen.blit(surface,(0,int(mn1y)),center=False)
            
        mouse = pygame.mouse.get_pos()
        screen.absline((255,255,255),mouse[0]-8,mouse[1],mouse[0]+8,mouse[1],3)
        screen.absline((255,255,255),mouse[0],mouse[1]-8,mouse[0],mouse[1]+8,3)
        screen.update(30)
'''


def get_block_high(_list):
    return _list[1]


def get_line_high(_list):
    return list(map(get_block_high, _list))


def settings():
    global screen, path, max_fps, FOV_effect, mode
    font1 = pygame.font.Font(path+'font.ttc', 35)
    font2 = pygame.font.Font(path+'font.ttc', 30)
    font3 = pygame.font.Font(path+'font.ttc', 15)
    select_fps = max_fps
    fpss = [30, 40, 60, 90, 120]
    fps_button_brightness = [0, 0, 0, 0, 0]
    fps_texts = ['人不能分辨的最低限度', '最低流畅的帧数', '流畅的帧数', '一些高刷新率显示器帧数', '人能感受到的上限']
    bgcolor = (20, 20, 20)
    select_color = (230, 255, 255)
    change_color = []
    for i in range(3):
        change_color.append((select_color[i]-bgcolor[i])//2)
    fps_less_time = 0
    while True:
        _mouse = screen.mouse_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(fpss)):
                    if 200+i*100 < _mouse[0] < 300+i*100 and 83 < _mouse[1] < 118:
                        select_fps = fpss[i]
                        sounds.sound(path+'sounds/2.wav', 0.7)
                abs_mouse = screen.abs_mouse_pos()
                if screen.neww-200+screen.ssx < abs_mouse[0] < screen.neww+screen.ssx and screen.newh-50+screen.ssy < abs_mouse[1] < screen.newh+screen.ssy:
                    sounds.sound(path+'sounds/2.wav', 0.7)
                    max_fps = select_fps
                    fps_less_time = 0
                if 0 < abs_mouse[0] < 200 and screen.newh-50+screen.ssy < abs_mouse[1] < screen.newh+screen.ssy:
                    mode = 1
                    return
                if 200 < _mouse[0] < 400 and 183 < _mouse[1] < 218:
                    FOV_effect = bool(not FOV_effect)
                    sounds.sound(path+'sounds/2.wav', 0.7)
        screen.check(events)
        screen.fill(bgcolor)
        screen.text(font1, (100, 100), (255, 255, 255), '最大帧数:', center=False)
        screen.text(font2, (1100, 100), (255, 255, 255),
                    '目前帧数:'+str(screen.fps), center=False)
        for i in range(len(fpss)):
            if fpss[i] != select_fps:
                # (190,230,255)
                screen.rect((bgcolor[0]+change_color[0]*fps_button_brightness[i],
                             bgcolor[1]+change_color[1] *
                             fps_button_brightness[i],
                             bgcolor[2]+change_color[2]*fps_button_brightness[i]), (200+i*100, 83, 100, 35))
                screen.text(font2, (250+i*100, 100), select_color,
                            str(fpss[i]), center=False)
                if 200+i*100 < _mouse[0] < 300+i*100 and 83 < _mouse[1] < 118:
                    fps_button_brightness[i] = min(
                        fps_button_brightness[i]+0.05, 1)
                    screen.rect(change_color, (150+i*100, 43, 200, 35))
                    screen.text(font3, (250+i*100, 60),
                                select_color, fps_texts[i])
                    # screen.circle(change_color,(250+i*100,75),4)
                else:
                    fps_button_brightness[i] = max(
                        fps_button_brightness[i]-0.05, 0)
            else:
                screen.rect(select_color, (200+i*100, 83, 100, 35))
                screen.text(font2, (250+i*100, 100), bgcolor,
                            str(fpss[i]), center=False)
                if 200+i*100 < _mouse[0] < 300+i*100 and 83 < _mouse[1] < 118:
                    screen.rect(change_color, (150+i*100, 43, 200, 35))
                    screen.text(font3, (250+i*100, 60),
                                select_color, fps_texts[i])
                    # screen.circle(change_color,(250+i*100,75),4)
        screen.text(font1, (100, 200), (255, 255, 255), 'FOV特效:', center=False)
        screen.rect(select_color, (200, 183, 200, 35))
        if FOV_effect:
            screen.text(font2, (300, 200), bgcolor, '开')
        else:
            screen.text(font2, (300, 200), bgcolor, '关')
        screen.absrect((64, 64, 64), (screen._rect.width -
                                      200, screen._rect.height-50, 200, 50))
        screen.abstext(font1, (screen._rect.width-100,
                               screen._rect.height-25), (255, 255, 255), '更新')
        screen.absrect((64, 64, 64), (0, screen._rect.height-50, 200, 50))
        screen.abstext(font1, (100, screen._rect.height-25),
                       (255, 255, 255), '退出')
        if screen.fps < max_fps - 5:
            fps_less_time += 1 / screen.fps
        else:
            fps_less_time = max(0, fps_less_time - 1 / screen.fps)
        if fps_less_time > 0.5:
            screen.text(font1, (600, 20), (200, 120, 200),
                        '您无法使程序运行速度达到%dfps(%.1fs)' % (max_fps, fps_less_time))
        render_mouse_pointer(_mouse)
        screen.update(max_fps)


def docs(Nid, Nid2):
    '''
    global docs_s
    print('docs?')
    docs_s.update()
    docs_s.deiconify()
    print('docs2?')
    _window.mainloop()
    '''
    print('UNFINISH')


def set_high1(a):
    #a += 0.01
    # return (a**2/exp(a/4)*log10(a)*1.2)**6/100000
    a *= 1.3
    return min((abs(a**2-sqrt(a)+exp(a)/100))/100+sqrt(a), 10)


#            0    1     2     3     4     5    6    7     8     9    10
high_data = [0,   0.05, 0.15, 0.35, 0.45, 0.5, 0.5, 0.55, 0.75, 0.9, 1]


def set_high2(a):
    if int(a) == a:
        return high_data[a]
    return high_data[int(a)]+(a-int(a))*(high_data[int(a)+1]-high_data[int(a)])


def round2(num):
    if num-int(num) >= 0.5:
        return int(num)+1
    return int(num)


def round3(num):
    rnum = num*10
    return round2(rnum)/10


def round4(num):
    return int(num*100)/100


def create_world(width, _type):
    global all_map, objects
    all_map = []
    world = []
    _w = width
    last_time = time.time()
    for i in range(width):
        world.append([])
        for i2 in range(width):
            world[i].append([0, random.randint(0, 9)])
        if time.time() - last_time > 0.03:
            r_load('创建噪声')
            last_time = time.time()
    if _type == -1:
        for y in range(width):
            for x in range(width):
                world[y][x] = [2, y % 4.5*(x % 4.5)/4.5*2]
            if time.time() - last_time > 0.03:
                r_load('加载测试地图')
                last_time = time.time()
        for y in range(10):
            for x in range(10):
                world[y][x][0] = 1
            if time.time() - last_time > 0.03:
                r_load('改变纹理')
                last_time = time.time()
        for x in range(width//2-1-width % 2):
            for y in range(width//2-1-width % 2):
                # x*2 y*2 x*2+1/y*2+1
                if world[y*2+2][x*2][1] != world[y*2][x*2][1]:
                    if not 's'+str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1])) in list(world_t.keys()):
                        world_t['s'+str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1]))] = change_block_scale(0, 0.5, 0, 1, round3(world[y*2+2][x*2][1] - world[y*2][x*2][1])-0.5, 1,
                                                                                                                 world_t[4])
                    world[y*2+1][x*2][0] = 's' + \
                        str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1]))
                    world[y*2+1][x*2][1] = world[y*2][x*2][1]
            if time.time() - last_time > 0.03:
                r_load('改变纹理'+str(round4(x/width)*100)+'%')
                last_time = time.time()
    if _type == 0:
        for i in range(width*width*7):
            pos = [random.randint(0, width-1), random.randint(0, width-1)]
            world[pos[1]][pos[0]][1] = min((world[(pos[1]+1) % _w][pos[0] % _w][1]+world[(pos[1]+1) % _w][(pos[0]+1) % _w][1] +
                                            world[(pos[1]+1) % _w][(pos[0]-1) % _w][1] +
                                            world[(pos[1]-1) % _w][pos[0] % _w][1]+world[(pos[1]-1) % _w][(pos[0]+1) % _w][1] +
                                            world[(pos[1]-1) % _w][(pos[0]-1) % _w][1] +
                                            world[pos[1] % _w][(pos[0]+1) % _w][1]+world[pos[1] % _w][(pos[0]-1) % _w][1]) / (
                5.5 + random.random()*3), 9)
            if time.time() - last_time > 0.03:
                r_load('平滑噪声'+str(round4(i/width/width/7)*100)+'%')
                last_time = time.time()
        for x in range(width):
            for y in range(width):
                world[y][x][0] = 3
                #world[y][x][1] = set_high2(world[y][x][1])
            if time.time() - last_time > 0.03:
                r_load('改变高度'+str(round4(x/width)*100)+'%')
                last_time = time.time()
        for x in range(width):
            for y in range(width):
                world[y][x][1] = round3(world[y][x][1])
            if time.time() - last_time > 0.03:
                r_load('量化高度'+str(round4(x/width)*100)+'%')
                last_time = time.time()
        '''
        for x in range(width//2-1-width % 2):
            for y in range(width//2-1-width % 2):
                # x*2 y*2 x*2+1/y*2+1
                if world[y*2+2][x*2][1] != world[y*2][x*2][1]:
                    if not 's'+str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1])) in list(world_t.keys()):
                        world_t['s'+str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1]))] = change_block_scale(0, 0.5, 0, 1, round3(world[y*2+2][x*2][1] - world[y*2][x*2][1])-0.5, 1,
                                                                                                                 world_t[4])
                    world[y*2+1][x*2][0] = 's' + \
                        str(round3(world[y*2+2][x*2][1] - world[y*2][x*2][1]))
                    world[y*2+1][x*2][1] = world[y*2][x*2][1]
            if time.time() - last_time > 0.03:
                r_load('改变纹理'+str(round3(x/width)))
                last_time = time.time()
        '''
    '''
    for i in range(width):
        for i2 in range(width):
            if world[i][i2][1] < 9:
                world[i][i2][1] = 0
            else:
                world[i][i2][1] = 9
    '''
    # print(all_map)
    for i in range(width*3):
        objects.raw_map.append([])
        for i2 in range(width*3):
            objects.raw_map[i].append(0)
    for i in range(width):
        for i2 in range(width):
            if abs(world[(i+1) % _w][i2 % _w][1]-world[i][i2][1]) > 0:
                objects.raw_map[i*3+2][i2*3] = 1
                objects.raw_map[i*3+2][i2*3+1] = 1
                objects.raw_map[i*3+2][i2*3+2] = 1
            if abs(world[(i-1) % _w][i2 % _w][1]-world[i][i2][1]) > 0:
                objects.raw_map[i*3][i2*3] = 1
                objects.raw_map[i*3][i2*3+1] = 1
                objects.raw_map[i*3][i2*3+2] = 1
            if abs(world[i % _w][(i2+1) % _w][1]-world[i][i2][1]) > 0:
                objects.raw_map[i*3][i2*3+2] = 1
                objects.raw_map[i*3+1][i2*3+2] = 1
                objects.raw_map[i*3+2][i2*3+2] = 1
            if abs(world[i % _w][(i2-1) % _w][1]-world[i][i2][1]) > 0:
                objects.raw_map[i*3][i2*3] = 1
                objects.raw_map[i*3+1][i2*3] = 1
                objects.raw_map[i*3+2][i2*3] = 1
        if time.time() - last_time > 0.1:
            r_load('创建障碍'+str(round4(i/width)*100)+'%')
            last_time = time.time()
    objects.print_array(list(map(get_line_high, world)))
    objects.print_array(objects.raw_map)
    for i in range(width*2):
        all_map.append([])
        for i2 in range(width*2):
            # print(world[i][i2][0])
            all_map[-1].append(e_3d_ssmove(world_t[world[i % width]
                                                   [i2 % width][0]], [i2, world[i % width][i2 % width][1], i]))
            # print(i,i2,world[i][i2][0])
            e_3d_rot(all_map[-1][-1], [0, 0.5])
        if time.time() - last_time > 0.1:
            r_load('创建地图'+str(round4(i/width)*50)+'%')
            last_time = time.time()
    return world


def e_3d_set_scale(xscale, yscale, zscale):
    global world_t
    for i in range(1, len(world_t)):
        for i2 in range(len(world_t[i])):
            for i3 in range(len(world_t[i][i2])-1):
                world_t[i][i2][i3] = [world_t[i][i2][i3][0]*xscale,
                                      world_t[i][i2][i3][1]*yscale, world_t[i][i2][i3][2]*zscale]


def music(mode, pipe, _pygame):
    global game_running
    _out_pipe, _in_pipe = pipe
    _in_pipe.close()
    sounds = [path+'BGM/JD1-lg.mp3']
    idx = 0
    try:
        while True:
            game_running = _out_pipe.recv()
            print("音乐:开始 | game_running:", game_running, " | mode:", mode)
            if game_running:
                if not _pygame.mixer.music.get_busy():
                    time.sleep(10)
                    while not _pygame.mixer.music.get_busy():
                        print(idx, sounds[idx % len(sounds)], game_running)
                        _pygame.mixer.music.load(sounds[idx % len(sounds)])
                        _pygame.mixer.music.play()
                    idx += 1
            else:
                _pygame.mixer.music.stop()
                print("音乐:停止")
    except:
        print(idx)


def build_map():
    global all_map_render, camera_p
    while True:
        ...


def start_game(gamemode):
    # 1200*675
    global screen, FOV, world_t, screen_c, bgcolor, camera_xpz, cammera_p, camera_p2, camera_p3, camera_Vx, camera_Vy, camera_speed,\
        camera_cspeed, world, world_w, world_scale, game_running, copy_render, time_l, game_speed, game_speed2, loaded, all_map
    create_world_mode = 0
    # start_new_thread(r_loading,())
    #_out_pipe,_in_pipe = Pipe(True)
    #load_p = Process(target=r_loading,args=((_out_pipe,_in_pipe),))
    # load_p.start()
    world_scale = [1, 1, 1]
    e_3d_set_scale(world_scale[0], world_scale[1], world_scale[2])
    if gamemode == 0:
        world_w = 100
        world = create_world(world_w, create_world_mode)
    elif gamemode == -1:
        world_w = 50
        world = create_world(world_w, -1)
    DEBUG = True
    debug_font = pygame.font.Font(path+'font.ttc', 17)
    debug_font2 = pygame.font.Font(path+'font.ttc', 13)
    game_running = True
    camera_p[2] = 25
    # start_new_thread(music,tuple([create_world_mode]))
    render_surface_len = 0
    robots = []
    start_new_thread(_r_loading, ())
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load(path+'BGM/异星悬崖.mp3')
    pygame.mixer.music.play(-1)
    loaded = False
    for i in range(5):
        robots.append(objects.Robot1([2*3, 2*3], 2, 5))
        robots[-1].init(world_w*3-1, [])
        robots[-1].target = [random.randint(
            0, world_w*3), random.randint(0, world_w*3)]
        robots[-1].pos = [random.randint(
            0, world_w*3), random.randint(0, world_w*3)]
        while not robots[-1].search() or robots[-1].pos == robots[-1].target:
            robots[-1].target = [random.randint(
                0, world_w*3), random.randint(0, world_w*3)]
            robots[-1].pos = [random.randint(
                0, world_w*3), random.randint(0, world_w*3)]
    print(robots[0].target)
    objects.init_search_place()
    loaded = True
    expand_x = 9
    mini_map_render_width = 150
    mini_map_width = world_w*3
    mini_map_scale = mini_map_render_width/mini_map_width
    mini_map = pygame.Surface((mini_map_render_width, mini_map_render_width))
    bind_id = -1
    # print(robots[0].path)
    while True:
        hide_mouse = False
        mouse_click = False
        shapes.bgcolor = bgcolor
        shapes.FOV = FOV
        shapes.screen_c = screen_c
        render_surface_len = 0
        if screen.fps != 0:
            game_speed = (60 / screen.fps) * game_speed2
        else:
            game_speed = game_speed2
        # print(game_speed)
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    DEBUG = not DEBUG
                if event.key == pygame.K_e:
                    game_speed2 /= 2
                if event.key == pygame.K_q:
                    game_speed2 *= 2
                    game_speed2 = min(game_speed2, 8)
                if event.key == pygame.K_TAB:
                    bind_id += 1
                    if bind_id == len(robots):
                        bind_id = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
        screen.check(events)
        screen.fill(bgcolor)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and camera_Vx < camera_speed:
            camera_Vx += camera_cspeed * game_speed
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and camera_Vx > -camera_speed:
            camera_Vx -= camera_cspeed * game_speed
        else:
            if camera_Vx > 0:
                camera_Vx -= camera_cspeed * game_speed
            if camera_Vx < 0:
                camera_Vx += camera_cspeed * game_speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and camera_Vy < camera_speed:
            camera_Vy += camera_cspeed * game_speed
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and camera_Vy > -camera_speed:
            camera_Vy -= camera_cspeed * game_speed
        else:
            if camera_Vy > 0:
                camera_Vy -= camera_cspeed * game_speed
            if camera_Vy < 0:
                camera_Vy += camera_cspeed * game_speed
        if abs(camera_Vx) < camera_cspeed * game_speed:
            camera_Vx = 0
        if abs(camera_Vy) < camera_cspeed * game_speed:
            camera_Vy = 0
        if FOV_effect:
            FOV = 600 - abs(camera_Vx * 300) - abs(camera_Vy * 600)
        else:
            FOV = 600
        #camera_p[1] = max(0.1,camera_p[1])
        # if random.randint(1,100) == 1:
        #    print(camera_p[1])
        camera_p[0] += camera_Vx * game_speed
        camera_p[1] += camera_Vy * game_speed
        # camera_p2 = [int(camera_p[0])%world_w,int(camera_p[1])%world_w] old
        camera_p2 = [int(camera_p[0]), int(camera_p[1])]
        camera_p3 = [camera_p[0]-camera_p2[0], camera_p[1]-camera_p2[1]]

        # print(camera_p,camera_p2,camera_p3,camera_Vx,camera_Vy)

        # get max high
        _sum = 0
        for y in [-5, -4, -3, -2, -1]:
            for x in [-2, -1, 0, 1, 2]:
                _sum += world[(y+camera_p2[1]) %
                              world_w][(x+camera_p2[0]) % world_w][1]
        _midnum = _sum / 25
        if _midnum < world[(camera_p2[1]-3) % world_w][camera_p2[0] % world_w][1]:
            camera_p[2] += (world[(camera_p2[1]-3) % world_w]
                            [camera_p2[0] % world_w][1]+5-camera_p[2])/15
        else:
            camera_p[2] += (_midnum+5-camera_p[2])/15

        '''
        render_list = []
        for y in range(camera_p2[1]-1,camera_p2[1]-19,-1):
            for x in range(camera_p2[0]-((y-camera_p2[1])//4+8),camera_p2[0]+((y-camera_p2[1])//4+9)):
                
                # 正常
                """
                if DEBUG:
                    if y == camera_p2[1]-3 and x == camera_p2[0] == camera_p2[0]:
                        render_list += e_3d_fill(e_3d_ssmove(world_t[world[y%world_w][x%world_w][0]],
                                                             [(x-camera_p[0])*world_scale[0],
                                                              world[y%world_w][x%world_w][1],
                                                              (y-camera_p[1])*world_scale[2]]),
                                                 0)
                    else:
                        render_list += e_3d_fill(e_3d_ssmove(world_t[world[y%world_w][x%world_w][0]],
                                                             [(x-camera_p[0])*world_scale[0],
                                                              world[y%world_w][x%world_w][1],
                                                              (y-camera_p[1])*world_scale[2]]),
                                                 min(1,(y-camera_p[1]+8)/13))
                else:
                """
                render_list += e_3d_fill(e_3d_ssmove(world_t[world[y%world_w][x%world_w][0]],
                                                         [(x-camera_p[0])*world_scale[0],
                                                          world[y%world_w][x%world_w][1],
                                                          (y-camera_p[1])*world_scale[2]]),
                                             min(1,max(0,y-camera_p[1]+4)/3))
                render_surface_len += len(world_t[world[y%world_w][x%world_w][0]])

        render_list.sort(key=e_2d_sort_key,reverse=True)
        e_3d_rot(render_list,(0,0.5))
        e_3d_ssmove2(render_list,(0,0,camera_p[2]))
        e_2d_surfaces(render_list)
        '''
        _camera_p = [camera_p[0] % world_w, camera_p[1] % world_w]
        if _camera_p[0] < world_w/2:
            _camera_p[0] += world_w
        if _camera_p[1] < world_w/2:
            _camera_p[1] += world_w
        render_list = []
        #world_w2 = int(input())
        rot_add_camera = e_3d_p_rot(
            [-_camera_p[0], -camera_p[2], -_camera_p[1]], (0, 0.5))
        #rot_add_camera[1] -= camera_p[2]
        #rot_add_camera = [-camera_p[0],-camera_p[2],-camera_p[1]]
        _camera_p2 = [int(_camera_p[0]), int(_camera_p[1])]
        for y in range(_camera_p2[1]+15, _camera_p2[1], -1):
            for x in range(_camera_p2[0]-int((y-_camera_p2[1])/1.25)-expand_x, _camera_p2[0]+int((y-_camera_p2[1])/1.25)+expand_x):
                render_list += e_3d_fill(e_3d_ssmove(all_map[y][x], rot_add_camera),
                                         min(1, max(0, (y-_camera_p[1]-12))/3))
                #render_surface_len += len(e_3d_ssmove(all_map[y%world_w][x%world_w],rot_add_camera))
        # print(render_list)
        for i in range(len(robots)):
            robots[i].tick(screen.wait_time*game_speed,
                           mini_map, mini_map_scale)
            if bind_id == i:
                robots[i].bind_camera(camera_p, world_w)
        # print(camera_p)
        # robots[0].bind_camera(camera_p, world_w)
        for i in robots:
            #print(i.return_render_surfaces([0, 0.5], camera_p, world_w))
            render_list += i.return_render_surfaces(
                [0, 0.5], [_camera_p[0], _camera_p[1], camera_p[2]], world_w)
        render_list.sort(key=e_2d_sort_key4, reverse=True)
        # print(render_list)
        e_2d_surfaces(render_list)
        # print(render_list)
        # '''

        time_l[1] = time.time()
        for _surface in render_list:
            if type(_surface) == Circle3d:
                _surface.render()
                continue
            color = _surface.pop()
            e_2d_cut(_surface)
            if len(_surface) > 2:
                screen.polygon(color, _surface)
        time_l[2] = time.time()
        flipped_map = pygame.transform.flip(mini_map, False, True)
        screen.screen.blit(flipped_map, (screen._rect.width-mini_map_render_width,
                                         screen._rect.height-mini_map_render_width))
        AbsMousePos = pygame.mouse.get_pos()
        robot_index = -1
        for i in robots:
            robot_index += 1
            screen.abscircle((0, 255, 0), (screen._rect.width-mini_map_render_width+i.render_pos[0] * mini_map_scale %
                                               mini_map_render_width, screen._rect.height -
                                               i.render_pos[1]*mini_map_scale
                                               % mini_map_render_width), 1, 1)
            if objects.dis2d(AbsMousePos, (screen._rect.width-mini_map_render_width+i.render_pos[0] * mini_map_scale %
                                               mini_map_render_width, screen._rect.height -
                                               i.render_pos[1]*mini_map_scale
                                               % mini_map_render_width)) < 10:
                hide_mouse = True
                screen.abscircle((100, 255, 100), (screen._rect.width-mini_map_render_width+i.render_pos[0] * mini_map_scale %
                                                   mini_map_render_width, screen._rect.height -
                                                   i.render_pos[1]*mini_map_scale
                                                   % mini_map_render_width), 4, 2)
                if mouse_click:
                    bind_id = robot_index
        screen.abscircle((255, 255, 255), (screen._rect.width-mini_map_render_width+camera_p[0] * mini_map_scale*3 %
                                           mini_map_render_width, screen._rect.height -
                                           camera_p[1]*mini_map_scale*3
                                           % mini_map_render_width), 2, 1)
        # print(len(render_list))
        if DEBUG:
            #text = 'render_list:'+str(render_surface_len)
            text = '按F4退出DEBUG    '
            text = text + '  camera: ' + \
                str([int(camera_p[0]*10)/10, int(camera_p[1]*10) /
                     10, int(camera_p[2]*10)/10])+' & '+str(_camera_p2)
            screen.abstext(debug_font, (20, 50),
                           (255, 255, 255), text, center=False)
            text = 'camera speed: ' + \
                str(int(camera_Vx*100)/100)+' '+str(int(camera_Vy*100)/100)
            screen.abstext(debug_font, (20, 70),
                           (255, 255, 255), text, center=False)
            text = '3d运算: '+str(int((time_l[1]-time_l[0])*1000))+'ms | 渲染: '+str(int((time_l[2]-time_l[1])*1000)) +\
                   'ms | ALL: '+str(int((time_l[2]-time_l[0])*1000))+'ms | 大: '+str(int((time_l[1]-time_l[0])*1000) >
                                                                                    int((time_l[2]-time_l[1])*1000))
            screen.abstext(debug_font, (20, 90),
                           (255, 255, 255), text, center=False)
            if bind_id >= 0:
                for i in range(-4, 5):
                    for i2 in range(-4, 5):
                        # if objects.raw_map[(int(robots[0].render_pos[1])+i) % world_w][(int(robots[0].render_pos[0])+i2) % world_w]:
                        if objects.raw_map[(int(robots[bind_id].render_pos[1])+i) % (world_w*3)
                                           ][(int(robots[bind_id].render_pos[0])+i2) % (world_w*3)]:
                            screen.absrect((255, 255, 255),
                                           (50+i2*7, 150+i*7, 8, 8))
                        else:
                            screen.absrect2((255, 255, 255),
                                            (50+i2*7, 150+i*7, 8, 8))
                        if objects.searched[(int(robots[bind_id].render_pos[1])+i) % (world_w*3)
                                            ][(int(robots[bind_id].render_pos[0])+i2) % (world_w*3)]:
                            screen.abscircle(
                                (0, 255, 255), (50+i2*7+4, 150+i*7+4), 1)
                if abs(robots[bind_id].target[0]-robots[bind_id].render_pos[0]) <= 4 and \
                        abs(robots[bind_id].target[1]-robots[bind_id].render_pos[1]) <= 4:
                    screen.absrect2((255, 0, 0), (int(robots[bind_id].target[0]-robots[bind_id].render_pos[0])*7+50,
                                                  int(robots[bind_id].target[1]-robots[bind_id].render_pos[1])*7+150, 8, 8))
            else:
                screen.abstext(debug_font2, (20, 115),
                               (200, 255, 255), '您没有选中机器人', center=False)
                screen.abstext(debug_font2, (20, 130),
                               (200, 255, 255), '按Tab选中机器人', center=False)
            screen.absrect2((0, 255, 0), (50, 150, 8, 8))
            text = 'speed:' + str(int(game_speed2*100))+'%'
            screen.abstext(debug_font, (20, 210),
                           (255, 255, 255), text, center=False)
            text = 'render_list: '+str(len(render_list))+'多边形'
            screen.abstext(debug_font, (20, 230),
                           (255, 255, 255), text, center=False)
        # pygame.display.update()
        if not hide_mouse:
            render_mouse_pointer(screen.mouse_pos())
        screen.update(max_fps)
        time_l[0] = time.time()


def e_render_3d(surfaces):
    global time_l
    screen.fill(bgcolor)
    for _surface in surfaces:
        color = _surface.pop()
        e_2d_cut(_surface)
        if len(_surface) > 2:
            screen.polygon(color, _surface)
    time_l[2] = time.time()


def r_loading_set_volume():
    for i in range(100):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()*0.95)
        time.sleep(0.01)
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(1)


def _r_loading():
    global screen, loading_level, loaded, turn_index, circle_brightness
    # start_new_thread(r_loading_set_volume,())
    font = pygame.font.Font(path+'font.ttc', 40)
    while not loaded:
        screen.check(pygame.event.get())
        screen.fill((0, 0, 30))
        if loading_level == 0:
            screen.text(font, (600, 337), (255, 255, 255), '生成机器')
        for i in range(len(circle_brightness)):
            circle_brightness[i] = max(circle_brightness[i]-0.1, 0)
        if turn_index % 3 == 0:
            circle_brightness[turn_index//3] = 1
        turn_index += 1
        if turn_index >= len(circle_brightness)*3:
            turn_index = 0
        for i in range(len(circle_brightness)):
            screen.circle((int(circle_brightness[i]*255), int(circle_brightness[i]*255), int(circle_brightness[i]*225+30)),
                          (600+circle_data[i][0]*circle_range, 437+circle_data[i][1]*circle_range), circle_radius, 0)
        screen.update(30)


def r_loading(pipe):
    global screen, loaded, loading_level
    _out_pipe, _in_pipe = pipe
    _in_pipe.close()
    loaded = False
    # start_new_thread(r_loading_set_volume,())
    font = pygame.font.Font(path+'font.ttc', 50)
    while not loaded:
        loaded = _out_pipe.recv()
        screen.check(pygame.event.get())
        screen.fill((0, 0, 30))
        if loading_level == 0:
            screen.text(font, (600, 337), (255, 255, 255), '加载中...')
        for i in range(len(circle_brightness)):
            circle_brightness[i] = max(circle_brightness[i]-0.1, 0)
        if turn_index % 3 == 0:
            circle_brightness[turn_index//3] = 1
        turn_index += 1
        if turn_index >= len(circle_brightness)*3:
            turn_index = 0
        for i in range(len(circle_brightness)):
            screen.circle((int(circle_brightness[i]*255), int(circle_brightness[i]*255), int(circle_brightness[i]*225+30)),
                          (600+circle_data[i][0]*circle_range, 437+circle_data[i][1]*circle_range), circle_radius, 0)
        screen.update(10)


def r_load(text):
    global screen, loaded, loading_level, circle_data, circle_brightness, turn_index
    loaded = False
    # start_new_thread(r_loading_set_volume,())
    font = pygame.font.Font(path+'font.ttc', 40)
    screen.check(pygame.event.get())
    screen.fill((0, 0, 30))
    if loading_level == 0:
        screen.text(font, (600, 337), (255, 255, 255), text)
    for i in range(len(circle_brightness)):
        circle_brightness[i] = max(circle_brightness[i]-0.1, 0)
    if turn_index % 3 == 0:
        circle_brightness[turn_index//3] = 1
    turn_index += 1
    if turn_index >= len(circle_brightness)*3:
        turn_index = 0
    for i in range(len(circle_brightness)):
        screen.circle((int(circle_brightness[i]*255), int(circle_brightness[i]*255), int(circle_brightness[i]*225+30)),
                      (600+circle_data[i][0]*circle_range, 437+circle_data[i][1]*circle_range), circle_radius, 0)
    pygame.display.update()


def mainmenu():
    global screen, mode, show_docs, sounds
    brightness = 0
    _font = pygame.font.Font(path+'font.ttc', 75)
    _fontm = pygame.font.Font(path+'font.ttc', 50)
    _posfont = pygame.font.Font(path+'font.ttc', 20)
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(path+'BGM/intro-2.mp3')
        pygame.mixer.music.play(-1)
    fade_in = True
    fade_out = False
    select = 0
    mouseselect = -1
    menu = ['测试', '文档', '探索', '设置']
    menubrightness = [0, 0, 0, 0]
    pygame.mouse.set_visible(False)
    #gear = create_gear(10,17.5,8,0.15,0.15)
    #gear_angle = 0
    while mode == 1:
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    select = (select+1) % len(menu)
                    sounds.sound(path+'sounds/2.wav', 0.1)
                if event.key == pygame.K_UP:
                    select = select-1
                    if select < 0:
                        select += len(menu)
                    sounds.sound(path+'sounds/2.wav', 0.1)
                if event.key == pygame.K_SPACE:
                    if select == 0:
                        print('测试!')
                        mode = 2
                    if select == 1:
                        print('文档!')
                        # if not show_docs:
                        # start_new_thread(docs,(1,1))
                    if select == 2:
                        print('登录!')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseselect != -1:
                    if mouseselect == 0:
                        print('测试!')
                        mode = 2
                    if mouseselect == 1:
                        print('文档!')
                        # if not show_docs:
                        #show_docs = True
                        # start_new_thread(docs,(1,1))
                        # print('ok')
                    if mouseselect == 2:
                        print('登录!')
                    if mouseselect == 3:
                        mode = 3
        screen.check(events)
        screen.fill((0, 0, int(30*brightness)))

        if fade_in:
            if brightness < 0.99:
                brightness += (1-brightness)/20
            else:
                brightness = 1
                fade_in = False

        screen.abstext(_font, (int(screen.neww/2), 70), (int(120*brightness),
                                                         int(200*brightness), int(255*brightness)), '异星探索')
        _mouseselect = False
        mouse2 = screen.mouse_pos()
        for i in range(len(menu)):
            if menubrightness[i] > 0 and i != mouseselect:
                menubrightness[i] = max(0, menubrightness[i]-0.03)
            if i == mouseselect and menubrightness[i] < 1:
                menubrightness[i] = min(1, menubrightness[i]+0.05)
            if menubrightness[i] > 0:
                screen.absrect((int(10*brightness+10*menubrightness[i]), int(10*brightness+10*menubrightness[i]),
                                int(40*brightness+10*menubrightness[i])), (int(screen.neww/2-300), 200+i*80-30, 600, 60))
            if int(screen.neww/2+300) > mouse[0] > int(screen.neww/2-300) and int(200+i*80-41) < mouse[1] < int(200+i*80+40):
                mouseselect = i
                _mouseselect = True
            if select == i:
                if mouseselect == -1:
                    screen.absrect((int(10*brightness), int(10*brightness), int(40*brightness)),
                                   (int(screen.neww/2-300), 200+i*80-30, 600, 60))
                screen.abstext(_fontm, (int(screen.neww/2), 200+i*80), (int(200*brightness), int(120*brightness),
                                                                        int(200*brightness)), menu[i])
            else:
                screen.abstext(_fontm, (int(screen.neww/2), 200+i*80), (int(200*brightness), int(255*brightness),
                                                                        int(255*brightness)), menu[i])
        if not _mouseselect:
            mouseselect = -1
        # screen.polygon((50,50,50),move(e_2d_rotate(gear,gear_angle),int(screen.neww/2+250),440))
        screen.absline((255, 255, 255),
                       mouse[0]-8, mouse[1], mouse[0]+8, mouse[1], 3)
        screen.absline((255, 255, 255),
                       mouse[0], mouse[1]-8, mouse[0], mouse[1]+8, 3)
        # screen.text(_posfont,(mouse2[0],mouse2[1]-20),(255,255,255),str(tuple(map(int,mouse2))))
        screen.update(max_fps)
        #gear_angle += 1 / screen.fps


def render_mouse_pointer(mouse, abspos=False):
    if abspos:
        screen.absline((255, 255, 255),
                       mouse[0]-8, mouse[1], mouse[0]+8, mouse[1], 3)
        screen.absline((255, 255, 255),
                       mouse[0], mouse[1]-8, mouse[0], mouse[1]+8, 3)
    else:
        screen.line((255, 255, 255), mouse[0]-8,
                    mouse[1], mouse[0]+8, mouse[1], 3)
        screen.line((255, 255, 255), mouse[0],
                    mouse[1]-8, mouse[0], mouse[1]+8, 3)


class Sounds(object):
    def __init__(self, names):
        self.names = names
        self.sounds = {}
        self.times = {}
        for name in self.names:
            self.sounds[name] = []
            for i in range(8):
                # print(name)
                self.sounds[name].append([pygame.mixer.Sound(name), 0])
            self.times[name] = pygame.mixer.Sound(name).get_length()

    def add_sound(self, name, volume):
        _time = time.time()
        try:
            for i in range(len(self.sounds[name])):
                if _time - self.sounds[name][i][1] > self.times[name]:
                    self.sounds[name][i][0].set_volume(volume)
                    self.sounds[name][i][0].play()
                    self.sounds[name][i][1] = _time
                    break
                # else:
                #    print(self.times[name])
        except:
            return

    def sound(self, name, volume=1):
        self.add_sound(name, volume)


sounds = Sounds([path+'sounds/2.wav'])
max_fps = 60
FOV = 600
# //多声音测试
'''
sounds.sound(names[0],1)
time.sleep(0.1)
sounds.sound(names[0],0.7)
time.sleep(0.1)
sounds.sound(names[0],0.5)
time.sleep(0.1)
sounds.sound(names[0],0.3)
time.sleep(0.1)
sounds.sound(names[0],0.1)
'''
show_docs = False
print('done0')
#docs_s = tkinter.Tk()
# docs_s.withdraw()
screen = vector.Screen(pygame.display.set_mode((1200, 675), pygame.RESIZABLE))
# screen.screen.set_alpha(0)
screen_c = (600, 337)
#bgcolor = [200,255,255]
bgcolor = [20, 20, 30]
game_running = False
print('done')
camera_xpz = 0
camera_p = [0, 0, 0]
camera_p2 = [0, 0, 0]
camera_p3 = [0, 0, 0]
camera_p4 = [0, 0, 0]
camera_Vx = 0
camera_Vy = 0
camera_speed = 0.15
camera_cspeed = 0.0025
world, world_w, world_scale = None, None, None
copy_render = []
all_map = []
time_l = [0, 0, 0]
game_speed = 0
game_speed2 = 1
loaded = True
loading_level = 0
circle_brightness = [0, 0, 0, 0, 0, 0, 0, 0]
turn_index = 0
circle_data = ((0.7071067811865476, 0.7071067811865475),
               (6.123233995736766e-17, 1.0),
               (-0.7071067811865475, 0.7071067811865476),
               (-1.0, 1.2246467991473532e-16),
               (-0.7071067811865477, -0.7071067811865475),
               (-1.8369701987210297e-16, -1.0),
               (0.7071067811865475, -0.7071067811865477),
               (1.0, -2.4492935982947064e-16))
circle_range = 30
circle_radius = 10
FOV_effect = True
#out_pipe,in_pipe = Pipe(True)
#play_music = Process(target=music,args=(0,(out_pipe,in_pipe),pygame))
# play_music.start()
# out_pipe.close()
while True:
    if mode == 1:
        mainmenu()
        sounds.sound(path+'sounds/2.wav', 0.7)
    if mode == 2:
        pygame.mixer.music.fadeout(1000)
        # in_pipe.send(False)
        # in_pipe.send(True)
        # time.sleep(100)
        start_game(0)
    if mode == 3:
        settings()
