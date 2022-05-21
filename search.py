variables = [] # name
classes = [] #[name,functions->[function,varnames]]
functions = [] #[name,varnames]

def append_var(name):
    global variables
    variables.append(name)

def append_class(name,_class):
    # functions: dir(_class)
    fs = dir(_class)
    varnames = []
    for i in range(len(fs)-1,-1,-1):
        if fs[i][0:2] == '__' and fs[i][-2:len(fs[i])] == '__':
            fs.pop(i)
        else:
            varnames.insert(0,)
    classes.append([name,fs])

def append_function(function):
    functions.append([function.__name__,function.__code__.co_varnames])

def search_word(word,keywords):
    idxs = []
    nothing_to_search = False
    start_idx = 0
    while not nothing_to_search:
        nothing_to_search = True
        for i in range(len(keywords)):
            if len(keywords[i]) >= len(word) + start_idx:
                #print(keywords[i][start_idx:start_idx+len(word)])
                if keywords[i][start_idx:start_idx+len(word)] == word:
                    idxs.append(i)
                    nothing_to_search = False
        start_idx += 1
    return idxs

def insert_char(string,char,insert_index):
    return string[0:insert_index+1] + char + string[insert_index+1:len(string)]

def delete_char(string,delete_index):
    return string[0:delete_index] + string[delete_index+1:len(string)]

def search(text,index):
    global variables

if __name__ == '__main__':
    import pygame,sys
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((600,300))
    font = pygame.font.Font("/Volumes/Untitled/编程机器/font.ttc",30)
    text = ''
    choose_idx = -1
    clock = pygame.time.Clock()
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    choose_idx = max(-1,choose_idx-1)
                elif event.key == pygame.K_RIGHT:
                    choose_idx = min(len(text)-1,choose_idx+1)
                else:
                    for key_i in '1234567890qwertyuiopasdfghjklzxcvbnm':
                        if eval('event.key==pygame.K_'+key_i):
                            text = insert_char(text,key_i,choose_idx)
                            choose_idx += 1
                            break
                    if event.key == pygame.K_BACKSPACE:
                        text = delete_char(text,choose_idx)
                        choose_idx = max(-1,choose_idx-1)
                    if event.key == pygame.K_SPACE:
                        text = insert_char(text,' ',choose_idx)
                        choose_idx += 1
                print(choose_idx)
        _text = font.render(text[0:choose_idx+1],True,(255,255,255))
        _width = _text.get_rect().width
        screen.blit(_text,(0,0))
        pygame.draw.rect(screen,(255,255,255),(_width-1,0,3,30))
        _text = font.render(text[choose_idx+1:len(text)],True,(255,255,255))
        screen.blit(_text,(_width,0))
        pygame.display.update()
        clock.tick(30)
