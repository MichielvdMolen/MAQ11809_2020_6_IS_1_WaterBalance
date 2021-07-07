from jupylet.sprite import Sprite
from jupylet.label import Label
from jupylet.app import App

app = App()

# The x and y components of the spaceship's velocity.
vx = 0
vy = 0

# The objects.
ship         = Sprite('images/ship1.png',  x=app.width/2,  y=app.height/2,  scale=0.5, angle = -45)
stars        = Sprite('images/stars.png',  scale=2.5)
alien        = Sprite('images/marvin.png', scale=0.1)
nemo         = Sprite('images/nemo.jpeg',  scale=0.8, x=app.height/2, y=app.height/2)
lauwersmeer  = Sprite('images/Lauwersmeer.jpeg', scale=0.4, x=app.height/2, y=app.height/2)
lauwersmeerc = Sprite('images/Lauwersmeer_karta.jpeg', scale=0.8, x=app.height/2, y=app.height/1)
wadden       = Sprite('images/wadden.jpeg', scale=0.8, x=app.height/2, y=app.height/2)
waddenc      = Sprite('images/wadden_karta.jpeg', scale=0.2, x=app.height/1.5, y=app.height/1)
rotterdam    = Sprite('images/rotterdam.jpeg', scale=1.0, x=app.height/2, y=app.height/2)
rotterdamc   = Sprite('images/rotterdam_karta.jpeg', scale=0.5, x=app.height/1.1, y=app.height/1.1)
zeeland      = Sprite('images/zeeland.jpeg', scale=1.2, x=app.height/2, y=app.height/2)
zeelandc     = Sprite('images/zeeland_karta.jpeg', scale=0.6, x=app.height/1.1, y=app.height/1.1)

draw_alien = False
draw_stars = False
draw_nemo  = False
draw_lauwersmeer  = False
draw_lauwersmeerc = False 
draw_wadden  = False
draw_waddenc = False 
draw_rotterdam  = False
draw_rotterdamc = False 
draw_zeeland  = False
draw_zeelandc = False 

# The x and y components of the spaceship's velocity.
vx = 0
vy = 0

# Current pressed state of the arrow keys.
up    = False
left  = False
right = False

@app.run_me_every(1/60)
def update_ship(ct, dt):
    global vx, vy

    if left:
        ship.angle += 150 * dt
        
    if right:
        ship.angle -= 120 * dt
        
    if up:
        vx += 3 * math.cos(math.radians(90 + ship.angle))
        vy += 3 * math.sin(math.radians(90 + ship.angle))

    #
    # Update ship position according to its velocity.
    #
    ship.x += vx * dt
    ship.y += vy * dt

    ship.wrap_position(app.width, app.height)
    

@app.run_me_every(1/60)
def rotate(ct, dt):
    
    alien.angle += 64 * dt

@app.event
def mouse_position_event(x, y, dx, dy):
    
    alien.x = x
    alien.y = y
    
@app.event
def render(ct, dt):
    
    app.window.clear()

    if draw_stars:
        stars.draw()    
    if draw_nemo:
        nemo.draw()
    if draw_lauwersmeer:
        lauwersmeer.draw() 
    if draw_lauwersmeerc:
        lauwersmeerc.draw()
    if draw_wadden:
        wadden.draw() 
    if draw_waddenc:
        waddenc.draw() 
    if draw_rotterdam:
        rotterdam.draw() 
    if draw_rotterdamc:
        rotterdamc.draw() 
    if draw_zeeland:
        zeeland.draw() 
    if draw_zeelandc:
        zeelandc.draw() 
    if draw_alien:
        alien.draw()
        
def set_nemo():
    global draw_stars, draw_alien, left, right, up, draw_nemo

    left       = False
    right      = False
    draw_stars = False
    draw_alien = False
    draw_nemo  = True

def set_lauwersmeer():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_lauwersmeer, draw_lauwersmeerc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False
    draw_lauwersmeer  = True
    draw_lauwersmeerc = True
    
    lauwersmeer.x, lauwersmeer.y = app.width/2, app.height/2
    lauwersmeerc.x, lauwersmeerc.y = app.width/1, app.height/1
    
def set_wadden():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_wadden, draw_waddenc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False
    draw_wadden  = True
    draw_waddenc = True

    wadden.x, wadden.y = app.width/2, app.height/2
    waddenc.x, waddenc.y = app.width/1.0, app.height/1.2
    
def set_rotterdam():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_rotterdam, draw_rotterdamc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_rotterdam  = True
    draw_rotterdamc = True
    
    rotterdam.x, rotterdam.y = app.width/2, app.height/2
    rotterdamc.x, rotterdamc.y = app.width/1.1, app.height/1.1
    
def set_zeeland():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_zeeland, draw_zeelandc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_zeeland  = True
    draw_zeelandc = True
    
    zeeland.x, zeeland.y = app.width/2, app.height/2
    zeelandc.x, zeelandc.y = app.width/1.1, app.height/1.1    
    
def check_my_answer_nemo(x, y, z):
    if x == 'does not' and y == 'do' and z == 'winter':
        print('Hoera! Your answer is correct! Are you ready to go fishing with me? We need to find Nemo!')
        set_nemo()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'does not'          : print('x is incorrect')
        if y != 'do'                : print('y is incorrect')
        if z != 'winter'            : print('z is incorrect')  
        return False

def check_my_answer_lauwersmeer(x, y1, y2, z):
#   if x == 'do' and y1 == 'constant' and y2 == 'precipitation' and z == ('2014/2015', '2015/2016', '2017/2018', '2019/2020'):
    if x == 'do' and y1 == 'constant' and y2 == 'precipitation' and '2014/2015' in z and '2015/2016' in z and '2017/2018' in z and '2019/2020' in z:
        print('Hoera! Your answer is correct! Do you think Nemo is in Lauwersmeer? No, Lauwersmeer is popular for record-size pikes and zanders.')
        set_lauwersmeer()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'do'                : print('x  is incorrect')
        if y1 != 'constant'          : print('y1 is incorrect')
        if y2 != 'precipitation'     : print('y2 is incorrect')
        if z != ('2014/2015', '2015/2016', '2017/2018', '2019/2020'): 
            print('z is incorrect')    
            if '2014/2015' in z          : print('   but 2014/2015 is correct')   
            if '2015/2016' in z          : print('   but 2015/2016 is correct')
            if '2017/2018' in z          : print('   but 2017/2018 is correct')
            if '2019/2020' in z          : print('   but 2019/2020 is correct')    
        return False 
    
def check_my_answer_wadden(x, y, z, u1, u2):
    if x == 'more' and y == ('a','b','c') and z == 'less' and u1 == '2018/2019' and u2 == 'Makkink':
        print('Hoera! Your answer is correct! Let us search further for my Nemo around the Wadden sea islands! Ah, he is also not there. In Wadden you can only find sea bass.')
        set_wadden()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'more'          : print('x  is incorrect')
        if y!= ('a','b','c')     : 
            print('y  is incorrect')
            if 'a' in y              : print('   but a  is correct') 
            if 'b' in y              : print('   but b  is correct') 
            if 'c' in y              : print('   but c  is correct')     
        if z  != 'less'          : print('z  is incorrect')
        if u1 != '2018/2019'     : print('u1 is incorrect, write something like \'2000/2001\'. ')
        if u2 != 'Makkink'       : print('u2 is incorrect')    
        return False

def check_my_answer_rotterdam(x, y):
    dy = 200
    if x == 'last' and 500-dy <= y <= 500+dy:
        print('Hoera! Your answer is correct! Do you think Nemo might be in Rotterdam fishing area? I don not think so. Rotterdam is a great seabass angling spot.')
        set_rotterdam()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'last'              : print('x  is incorrect')
        if y<500-dy  or y>500+dy     : print('y  is incorrect')
        return False   
    
def check_my_answer_zeeland(x1, x2, y, z):
    if x1 == 'is' and x2 == 2 and y == 'is not' and z >= 2:
        print('Hoera! Your answer is correct! But, still no Nemo. Zeeland currently is a fantastic varied area for sea anglers, not clown fishes. Do you think we will find him in Integration skills 2?')
        set_zeeland()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x1 != 'is'              : print('x1 is incorrect')
        if x2 != 2                 : print('x2 is incorrect')
        if y  != 'is not'          : print('y2 is incorrect')
        if z<2                     : print('z  is incorrect')    
        return False    