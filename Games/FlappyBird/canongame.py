import pygame
import math
import random
import pathlib
import pickle
from vector import Vector2

  
# ======================================================================
# constants to help code readability
# ======================================================================

RANDOM_SEED               = 3
GAME_MODE_LIVE            = 0
GAME_MODE_REPLAY          = 1
GAME_STATE_INTRO          = 0
GAME_STATE_IN_PROGRESS    = 1
GAME_STATE_WAVE_OVER      = 2
GAME_STATE_LAST_BASE_LOST = 3
GAME_STATE_OVER           = 4
SCORE_PARTICAL_LIMIT      = 3

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ORIGINX = SCREEN_WIDTH // 2
ORIGINY = SCREEN_HEIGHT // 2

COLOUR_BLACK      = (0, 0, 0)
COLOUR_DARKBLUE   = (29, 43, 83)
COLOUR_PURPLE     = (126, 37, 83)
COLOUR_DARKGREEN  = (0, 135, 81)
COLOUR_BROWN      = (171, 82, 54)
COLOUR_DARKGREY   = (95, 87, 79)
COLOUR_LIGHTGREY  = (194, 195, 199)
COLOUR_WHITE      = (255, 241, 232)
COLOUR_RED        = (255, 0, 77)
COLOUR_ORANGE     = (255, 163, 0)
COLOUR_YELLOW     = (255, 236, 39)
COLOUR_GREEN      = (0, 228, 54)
COLOUR_BLUE       = (41, 173, 255)
COLOUR_LAVENDER   = (131, 118, 156)
COLOUR_PINK       = (255, 119, 168)
COLOUR_LIGHTPEACH = (255, 204, 170)

IDX_COLOUR_BLACK      = 0
IDX_COLOUR_DARKBLUE   = 1
IDX_COLOUR_PURPLE     = 2
IDX_COLOUR_DARKGREEN  = 3
IDX_COLOUR_BROWN      = 4
IDX_COLOUR_DARKGREY   = 5
IDX_COLOUR_LIGHTGREY  = 6
IDX_COLOUR_WHITE      = 7
IDX_COLOUR_RED        = 8
IDX_COLOUR_ORANGE     = 9
IDX_COLOUR_YELLOW     = 10
IDX_COLOUR_GREEN      = 11
IDX_COLOUR_BLUE       = 12
IDX_COLOUR_LAVENDER   = 13
IDX_COLOUR_PINK       = 14
IDX_COLOUR_LIGHTPEACH = 15

COLOUR_PALETTE = [COLOUR_BLACK    ,
                  COLOUR_DARKBLUE ,
                  COLOUR_PURPLE   ,
                  COLOUR_DARKGREEN,
                  COLOUR_BROWN    ,
                  COLOUR_DARKGREY ,
                  COLOUR_LIGHTGREY,
                  COLOUR_WHITE    ,
                  COLOUR_RED      ,
                  COLOUR_ORANGE   ,
                  COLOUR_YELLOW   ,
                  COLOUR_GREEN    ,
                  COLOUR_BLUE     ,
                  COLOUR_LAVENDER ,
                  COLOUR_PINK     ,
                  COLOUR_LIGHTPEACH]

# wave limits
MAX_BOMBERS   = 8
MAX_BLOCKERS  = 10
MAX_BRUTES    = 10
MAX_WAVE_TIME = 120 # length of wave in seconds

# scores
SCORE_TARGET_HIT  = 250
SCORE_BOMBER_HIT  = 500
SCORE_BRUTE_HIT   = 1000


# ======================================================================
# setup pygame
# ======================================================================
# set mixer to 512 value to stop buffering causing sound delay
# this must be called before anything else using mixer.pre_init()

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Cannon")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# ======================================================================
# load images and sounds
# ======================================================================

FILEPATH = pathlib.Path().cwd() 

# load sound effects
sound_boom      = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'boom.ogg')))
sound_big_boom  = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'big_boom.ogg')))
sound_gunfire   = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'gunfire.ogg')))
sound_dryfire   = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'dryfire.ogg')))
sound_blocker   = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'blocker.ogg')))
sound_base_boom = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'base_explode.ogg')))

# load background music
#pygame.mixer.music.load(str(FILEPATH.joinpath('sounds' ,'rolemusic_the_black_frame.ogg')))
sound_track_main           = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'rolemusic_the_black_frame.ogg')))
sound_track_main_game_over = pygame.mixer.Sound(str(FILEPATH.joinpath('sounds' ,'rolemusic_yellow_dust.ogg')))


myfont10 = pygame.font.Font(str(FILEPATH.joinpath('assets' ,'digitalix.ttf')), 10)
myfont20 = pygame.font.Font(str(FILEPATH.joinpath('assets' ,'digitalix.ttf')), 20)
myfont30 = pygame.font.Font(str(FILEPATH.joinpath('assets' ,'digitalix.ttf')), 30)
myfont80 = pygame.font.Font(str(FILEPATH.joinpath('assets' ,'digitalix.ttf')), 80)

SCOREFONT_TARGET_HIT  = myfont10.render(str(SCORE_TARGET_HIT) , 0, COLOUR_PALETTE[IDX_COLOUR_YELLOW])
SCOREFONT_BOMBER_HIT  = myfont10.render(str(SCORE_BOMBER_HIT) , 0, COLOUR_PALETTE[IDX_COLOUR_YELLOW])
SCOREFONT_BRUTE_HIT   = myfont10.render(str(SCORE_BRUTE_HIT)  , 0, COLOUR_PALETTE[IDX_COLOUR_YELLOW])

image_target       = pygame.image.load(str(FILEPATH.joinpath('png' ,'target.png'))).convert()
image_target_flash = pygame.image.load(str(FILEPATH.joinpath('png' ,'target_flash.png'))).convert()
image_bomber       = pygame.image.load(str(FILEPATH.joinpath('png' ,'bomber.png'))).convert()
image_bomber_flash = pygame.image.load(str(FILEPATH.joinpath('png' ,'bomber_flash.png'))).convert()
image_brute        = pygame.image.load(str(FILEPATH.joinpath('png' ,'brute.png'))).convert()
image_brute_flash  = pygame.image.load(str(FILEPATH.joinpath('png' ,'brute_flash.png'))).convert()
image_blocker      = pygame.image.load(str(FILEPATH.joinpath('png' ,'blocker.png'))).convert()
image_base_horz    = pygame.image.load(str(FILEPATH.joinpath('png' ,'base_horizontal.png'))).convert()
image_base_vert    = pygame.image.load(str(FILEPATH.joinpath('png' ,'base_vertical.png'))).convert()
image_reticule     = pygame.image.load(str(FILEPATH.joinpath('png' ,'reticule.png'))).convert()
image_tank         = pygame.image.load(str(FILEPATH.joinpath('png' ,'tank.png'))).convert()
image_bunny1       = pygame.image.load(str(FILEPATH.joinpath('png' ,'bunny1.png'))).convert()

# set the transparent colour, in my case black
image_target.set_colorkey(COLOUR_BLACK)
image_target_flash.set_colorkey(COLOUR_BLACK)
image_bomber.set_colorkey(COLOUR_BLACK)
image_bomber_flash.set_colorkey(COLOUR_BLACK)
image_brute.set_colorkey(COLOUR_BLACK)
image_brute_flash.set_colorkey(COLOUR_BLACK)
image_blocker.set_colorkey(COLOUR_BLACK)
image_base_horz.set_colorkey(COLOUR_BLACK)
image_base_vert.set_colorkey(COLOUR_BLACK)
image_reticule.set_colorkey(COLOUR_BLACK)
image_tank.set_colorkey(COLOUR_BLACK)
image_bunny1.set_colorkey(COLOUR_BLACK)

#=======================================================================
# Score Partical class
#=======================================================================

class ScorePartical():
    
    def __init__(self, pos, angle, speed, image):
        
        self.pos = Vector2(pos.x, pos.y)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0,0)     
        self.alpha = 255   
        self.acc.setFromAngle(angle)
        self.acc.mult(speed)
        self.image = image
        self.image.set_alpha(self.alpha)
        
    def update(self):
        
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.alpha -= abs(self.vel.y)
        self.alpha = max(0,self.alpha)
        self.image.set_alpha(self.alpha)
        
        # gravity hack
        self.vel.y += 0.5
        
    def draw(self):
        
        screen.blit(self.image, (self.pos.x, self.pos.y))
        
    def isOffScreen(self):
        
        return (self.pos.x < 0) or (self.pos.x > SCREEN_WIDTH) or (self.pos.y < 0) or (self.pos.y > SCREEN_HEIGHT)
        
    def isDead(self):
        
        return (self.alpha <= 0) or (self.isOffScreen())


#=======================================================================
# Partical class
#=======================================================================

class Partical():
    
    def __init__(self, pos, angle, speed, size, colour):
        
        self.pos = Vector2(pos.x, pos.y)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0,0)     
        self.size = size
        self.alpha = 255   
        self.acc.setFromAngle(angle)
        self.acc.mult(speed)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(colour)
        self.image.set_alpha(self.alpha)
        
    def update(self):
        
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.alpha -= abs(self.vel.y)
        self.alpha = max(0,self.alpha)
        self.image.set_alpha(self.alpha)
        
        # gravity hack
        self.vel.y += 0.2
        
    def draw(self):
        
        screen.blit(self.image, (self.pos.x, self.pos.y))
        
    def isOffScreen(self):
        
        return (self.pos.x < 0) or (self.pos.x > SCREEN_WIDTH) or (self.pos.y < 0) or (self.pos.y > SCREEN_HEIGHT)
        
    def isDead(self):
        
        return (self.alpha <= 0) or (self.isOffScreen())
    

#=======================================================================
# particlesystem class
#=======================================================================

class ParticleSystem():
    
    def __init__(self, x, y, mx = 20):
        
        self.pos = Vector2(x, y)
        self.particles = []
        self.max_particles = mx
        
    def killAll(self):
        
        self.particles = []
        
    def burstDirection(self, angle, spread, colour):
        
        self.killAll()
        for n in range(0, self.max_particles):
            if colour is None:
                c = COLOUR_PALETTE[random.randint(0, 15)]
            else:
                c = colour
            # vary the angle a little bit
            angle = (angle + random.uniform(-spread, spread)) % 360
            speed = random.uniform(0.1, 0.7)
            size = random.randint(4, 16)
            p = Partical(self.pos, angle, speed, size, c)
            self.particles.append(p)
            
    def burstCircle(self, colour):
        
        self.killAll()
        step = 360 // self.max_particles
        for n in range(0, self.max_particles):
            if colour is None:
                c = COLOUR_PALETTE[random.randint(0, 15)]
            else:
                c = colour
                
            angle = n * step
            speed = random.uniform(0.1, 0.7)
            size = random.randint(4, 16)
            if size < 5 and random.random() > 0.6:
                c = COLOUR_WHITE
            
            p = Partical(self.pos, angle, speed, size, c)
            self.particles.append(p)
    
    def scoreBurst(self, scoreimage):
        
        self.killAll()
        step = 360 // self.max_particles
        for n in range(0, self.max_particles):
            angle = n * step
            speed = 0.5
            p = ScorePartical(self.pos, angle, speed, scoreimage)
            self.particles.append(p)
            
    def update(self):
        
        cp = [p for p in self.particles if not p.isDead()]
        self.particles = cp
        for p in self.particles:
            p.update()
            p.draw()
        
    def isDead(self):
        
        return len(self.particles) == 0
        

#=======================================================================
# particlesystemController class
#=======================================================================

class ParticleSystemController():
    
    def __init__(self):
        
        self.systems = []
        
    def spawn(self, x, y, mx):
        
        system = ParticleSystem(x, y, mx)
        self.systems.append(system)
        return system
        
    def spawnBurstDirection(self, x, y, angle, spread, max_particles = 20, colour=None):
        
        system = self.spawn(x, y, max_particles)
        system.burstDirection(angle, spread, colour)
        
    def spawnBurstCircle(self, x, y, max_particles = 20, colour=None):
        
        system = self.spawn(x, y, max_particles)
        system.burstCircle(colour)
        
    def spawnScoreBurst(self, x, y, scoreimage):
        
        system = self.spawn(x, y, SCORE_PARTICAL_LIMIT)
        system.scoreBurst(scoreimage)
        
    def killAll(self):
        
        self.systems = []
    
    def update(self):
        
        cp = [ps for ps in self.systems if not ps.isDead()]
        self.systems = cp
        for s in self.systems:
            s.update()       

        
#=======================================================================
# Star class
#=======================================================================

class Star():
    
    def __init__(self):
        
        self.position = Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.velocity = Vector2(0.0, 1 + random.random() * 10)
        self.size = random.randint(1,4)
        self.image = pygame.Surface([self.size, self.size])
        self.rect = self.image.get_rect()
        self.image.fill(COLOUR_BLUE)

    def reset(self):
        
        self.position.y = 0
        self.position.x = random.randint(0, SCREEN_WIDTH)
        self.velocity.y = 1 + random.random() * 10
        
    def update(self):
        
        # add a little to vel each frame to make it look a bit 
        # like gravity is pulling it down like rain
        # reset() will set vel back to a baseline
        
        self.velocity.y += 0.02
        self.position.add(self.velocity)
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        
    def draw(self):
        
        screen.blit(self.image, self.rect)


#=======================================================================
# Starfield class
#=======================================================================

class StarField():
    
    def __init__(self):
        
        self.stars = []
        self.max_stars = 40
        
        for i in range(0, self.max_stars):
            star = Star()
            self.stars.append(star)
            
    def update(self):
        
        for star in self.stars:
            star.update()
            
            if star.position.y > SCREEN_HEIGHT:
                star.reset()
                
    def draw(self):
        
        for star in self.stars:
            star.draw()


# ======================================================================
# cannonball class
# ======================================================================
class Cannonball():

    def __init__(self, x, y):
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.size = 8
        self.mass = 20
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(COLOUR_PINK)
        self.isflying = False
        self.dead = False
        
    def launch(self, f):
        
        self.applyForce(f)
        self.isflying = True
        
    def applyForce(self, f):
        
        # make a copy to preserve the original vector values
        fcopy = f.getCopy()
        fcopy.div(self.mass)
        self.acc.add(fcopy)
        
    def update(self):
        
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.constrain()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
    def constrain(self):
        
        if self.pos.y > SCREEN_HEIGHT - self.size:
            self.pos.y = SCREEN_HEIGHT - self.size
            self.vel.mult(0)
            
    def outOfPlay(self):
        
        return self.pos.x < 0 or self.pos.x > SCREEN_WIDTH or self.pos.y >= SCREEN_HEIGHT - self.size
            
    def isDead(self):
        
        return self.outOfPlay() or self.dead
        
    def draw(self):
        
        if not self.isDead():
            screen.blit(self.image, self.rect)

# ======================================================================
# target class
# ======================================================================

class Target():

    def __init__(self, x, y, w, h):
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(-0.5 + random.random() * -2.5, 0)
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = image_target
        self.dead = False
        self.lastflash = 0
        self.thisframe = 0
        self.flash = False
        
    def isDead(self):
        
        return self.dead == True
        
    def update(self):
        
        self.thisframe += 1
        if self.thisframe - self.lastflash > 3:
            self.flash = not self.flash
            self.lastflash = self.thisframe
        
        if self.flash:
            self.image = image_target_flash
        else:
            self.image = image_target
                
        self.pos.add(self.vel)
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
            
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
    def draw(self):
        
        screen.blit(self.image, self.rect)

# ======================================================================
# blocker class
# ======================================================================

class Blocker():

    def __init__(self, x, y, w, h):
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(-1 + random.random() * -0.5, 0)
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = image_blocker
        self.dead = False
        
    def isDead(self):
        
        return self.dead == True
        
    def update(self):
        
        self.pos.add(self.vel)
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
            
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
    def draw(self):
        
        screen.blit(self.image, self.rect)
        
# ======================================================================
# bomber class
# ======================================================================

class Bomber():

    def __init__(self, x, y, w, h, vy, a):
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, vy)
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = image_bomber
        self.dead = False
        self.lastflash = 0
        self.thisframe = 0
        self.flash = False
        self.angle = a
        
    def isDead(self):
        
        return self.dead == True
        
    def isOffScreen(self):
        
        return self.pos.y > SCREEN_HEIGHT
        
    def update(self):
        
        self.angle += 1
        if self.angle > 360:
            self.angle = 0
        
        self.thisframe += 1
        if self.thisframe - self.lastflash > 10:
            self.flash = not self.flash
            self.lastflash = self.thisframe
        
        if self.flash:
            self.image = image_bomber_flash
        else:
            self.image = image_bomber
        
        
        if self.isOffScreen():
            self.pos.y = 0
        
        self.pos.add(self.vel)
        
        offset = 2 * math.cos(math.radians(self.angle))
        self.pos.x += offset
        
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y
        
    def draw(self):
        
        screen.blit(self.image, self.rect)
        
# ======================================================================
# brute class
# ======================================================================

class Brute():

    def __init__(self, x, y, tx, ty, a):
        
        self.pos    = Vector2(x, y)
        self.vel    = Vector2(0, 0)
        self.width  = 32
        self.height = 24
        self.rect   = pygame.Rect(x, y, self.width, self.height)
        self.image  = image_brute
        self.lastflash = 0
        self.thisframe = 0
        self.flash = False
        self.dead   = False
        self.angle  = a
        self.radius = 1
        self.radius_step = 0.1
        
        # get a vector to carry us to the target
        tv = Vector2(tx,ty)
        tv.sub(self.pos)
        tv.normalise()
        tv.mult(0.6)
        self.vel.set(tv)
        
    def isDead(self):
        
        return self.dead == True
        
    def update(self):
        
        self.thisframe += 1
        if self.thisframe - self.lastflash > 20:
            self.flash = not self.flash
            self.lastflash = self.thisframe
        
        if self.flash:
            self.image = image_brute_flash
        else:
            self.image = image_brute
        
        self.radius += self.radius_step
        if self.radius < 0 or self.radius > 40:
            self.radius_step = -self.radius_step
        
        self.angle += 1
        if self.angle > 360:
            self.angle = 0
            
        xoff = math.cos(math.radians(self.angle)) 
        yoff = math.sin(math.radians(self.angle)) 
        
        self.pos.add(self.vel)
        #self.dead = self.pos.y > SCREEN_HEIGHT or self.pos.y < 0 or self.pos.x < 0 or self.pos.x > SCREEN_WIDTH

        self.rect.x = self.pos.x + (xoff * self.radius)
        self.rect.y = self.pos.y + (yoff * self.radius)
        
    def draw(self):
        
        screen.blit(self.image, self.rect)


# ======================================================================
# base class
# ======================================================================

class Base():

    def __init__(self, x, y, w, h, img):
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = img
        self.dead = False
        
    def isDead(self):
        
        return self.dead == True
        
    def update(self):
        
        self.pos.add(self.vel)
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
            
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
    def draw(self):
        
        screen.blit(self.image, self.rect)
        
# ======================================================================
# scoreboard class
# ======================================================================

class Scoreboard():
    
    def __init__(self):
        
        self.score = 0
        self.targetscore = 0 # lerp to this
        self.needTableUpdate = True
        
        try:
            self.highscores = pickle.load(open("highscores.pkl", "rb"))
        except:
            self.highscores = [i * 250 for i in range(0, 10)]
            
        self.highscores.sort(reverse=True)
        
    def add(self, n):
        
        self.targetscore += n
        
    def reset(self):
        
        self.score = 0
        self.targetscore = 0
        self.needTableUpdate = True
        
    def finish(self):
        
        # in case the lerping didn't get time to finish
        self.score = self.targetscore
        
        if self.needTableUpdate:
            if self.score > min(self.highscores):
                self.highscores.append(self.score)
                self.highscores.sort(reverse=True)
                self.highscores.pop()
                self.save()
                self.needTableUpdate = False
    
    def drawHighScoreTable(self):
            
        alpha = 200
        xoff = 760
        yoff = 40
        highlight_done = False
        
        textsurf = myfont30.render('HIGHSCORES.', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (xoff,yoff))
        
        yoff += 40
        
        for i, line in enumerate(self.highscores):
            
            alpha -= 14
            msg = '{:02d} ... {}'.format(i+1, line)
            textsurf = myfont30.render(msg, 0, COLOUR_RED)
            
            if line == self.score and not highlight_done:
                textsurf.set_alpha(255)
                highlight_done = True
            else:
                textsurf.set_alpha(alpha)
                
            screen.blit(textsurf, (xoff, yoff + (i * 40)))
        
    def save(self):
        
        pickle.dump(self.highscores, open( "highscores.pkl", "wb" ))
        
    def update(self):
        
        if self.score != self.targetscore:
            self.score = self.lerp(self.score, self.targetscore, 0.02)
        
    def lerp(self, mn, mx, norm):
    
        return math.ceil(((mx - mn) * norm + mn))
        
    def draw(self, fired, maxballs, wavenumber, seconds):
        
        msg = 'WAVE {} ::: FIRED {}/{} ::: SCORE {} ::: {}'.format(wavenumber, fired, maxballs, self.score, seconds)
        textsurf = myfont20.render(msg, 0, COLOUR_RED)
        textsurf.set_alpha(160)
        screen.blit(textsurf, (40,20))

# ======================================================================
# reticule/crosshair class
# ======================================================================

class Reticule():
    
    def __init__(self):
        
        self.pos = Vector2(0,0)
        self.image = image_reticule
        self.bullets_loaded = 0
        
        
    def lerp(self, mn, mx, norm):
        
        return math.ceil(((mx - mn) * norm + mn))
        
    def update(self, mousex, mousey, bullets_loaded):
        
        self.pos.x = self.lerp(self.pos.x, mousex, 0.2)
        self.pos.y = self.lerp(self.pos.y, mousey, 0.2)
        self.bullets_loaded = bullets_loaded
        
    def draw(self):
        
        screen.blit(image_tank,(10,550))
        
        x = 0
        for n in range(0, self.bullets_loaded):
            pygame.draw.rect(screen, COLOUR_PINK, [self.pos.x-32, (self.pos.y - 20) + x, 8, 8])
            x += 10
            
        screen.blit(self.image,(self.pos.x -16,self.pos.y-16))

    
# ======================================================================
# game class
# ======================================================================

class Game():

    def __init__(self):
        
        self.gamemode           = GAME_MODE_LIVE
        self.gamestate          = GAME_STATE_INTRO
        self.slowmotion         = False
        self.fps                = 50
        self.replay_length      = 0
        self.gamestate_delay    = 0
        self.current_tick       = 0
        self.wave_start_tick    = 0
        self.wave_seconds       = 60
        self.wave_number        = 0
        self.maxballs           = 50
        self.max_burst_fire     = 4
        self.shots_fired        = 0
        self.shots_fired_total  = 0
        self.shot_accuracy      = 0
        self.targets_killed     = 0
        self.bombers_killed     = 0
        self.brutes_killed      = 0
        self.blockers_hit       = 0
        self.bullet_bonus       = 0
        self.cannon_pos_x       = 30
        self.cannon_pos_y       = 550
        self.cannon_firepower   = 180
        
        self.targets_killed_this_wave = 0
        self.bombers_killed_this_wave = 0
        self.brutes_killed_this_wave  = 0
        self.shot_accuracy_this_wave  = 0

        self.reticule   = Reticule()
        self.starfield  = StarField()
        self.psc        = ParticleSystemController()
        self.scoreboard = Scoreboard()
        
        self.balls     = []
        self.bases     = []
        self.targets   = []
        self.blockers  = []
        self.bombers   = []
        self.brutes    = []
        self.recording = []
        
        self.gravity = Vector2(0,0.3)
        
        self.startGame()

    def toggleSlowMotion(self):
        
        if self.gamemode == GAME_MODE_REPLAY:
            self.slowmotion = not self.slowmotion

    def getDrag(self, ball):
        
        c = 0.012
        speed = ball.vel.mag()
        dragMag = c * speed * speed
        drag = ball.vel.getCopy()
        drag.mult(-1)
        drag.normalise()
        drag.mult(dragMag)
        return drag
        
    def startReplay(self):
        
        if self.gamestate == GAME_STATE_OVER:
            self.gamemode = GAME_MODE_REPLAY
            self.replay_length = len(self.recording)
            self.startGame()
            self.playGameMainSong()
            self.gamestate = GAME_STATE_IN_PROGRESS   
        
    def startGame(self):
        
        self.thisframe          = 0
        self.current_tick       = 0
        self.wave_number        = 0
        self.shots_fired        = 0
        self.shots_fired_total  = 0
        self.shot_accuracy      = 0
        self.targets_killed     = 0
        self.bombers_killed     = 0
        self.brutes_killed      = 0
        self.blockers_hit       = 0
        
        self.targets_killed_this_wave = 0
        self.bombers_killed_this_wave = 0
        self.brutes_killed_this_wave  = 0
        
        self.scoreboard.reset()
        self.psc.killAll()
        self.spawnBases()
        self.spawnWave()

    def spawnBases(self):
        
        self.bases = []
        for x in range(0, 2):
            b = Base(400 + x * 300, 580, 120, 16, image_base_horz)
            self.bases.append(b)
        for y in range(0, 2):
            b = Base(10, 60 + y * 200, 16, 120, image_base_vert)
            self.bases.append(b)        
        
    def clearOldWave(self):
        
        self.targets  = []
        self.blockers = []
        self.bombers  = []
        self.brutes   = []

    def prepareWave(self):
        
        self.clearOldWave()
        self.balls = []
        self.wave_start_tick = self.current_tick
        self.wave_seconds = MAX_WAVE_TIME
        self.bullet_bonus = 0
        self.wave_number += 1
        
        # reset wave target hits
        self.targets_killed_this_wave = 0
        self.bombers_killed_this_wave = 0
        self.brutes_killed_this_wave  = 0  
        self.shot_accuracy_this_wave  = 0  
        self.shots_fired              = 0 

        
    def spawnTargets(self):
        
        for x in range(0, 5 + self.wave_number):
            t = Target(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(10, SCREEN_HEIGHT-200), 40, 24)
            self.targets.append(t)
            
    def spawnBlockers(self):
        
        for x in range(0, min(self.wave_number, MAX_BLOCKERS)):
            b = Blocker(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(10, SCREEN_HEIGHT-200), 32, 40)
            self.blockers.append(b)
            
    def spawnBombers(self):
        
        for x in range(0, min(self.wave_number, MAX_BOMBERS)):
            b = Bomber(random.randint(300, 900), random.randint(-400, 0), 32, 28, 0.1 + (random.random() * 0.4), random.randint(0,360))
            self.bombers.append(b)
            
    def spawnBrutes(self):
        
        # if only 1 base remains, spawn a 'brute' wave
        
        if len(self.bases) == 1:
            
            tx = self.bases[0].pos.x
            ty = self.bases[0].pos.y
            
            for x in range(0, min(self.wave_number, MAX_BRUTES)):
                
                if tx == 10:
                    # base is on screen left
                    x = SCREEN_WIDTH + random.randrange(0, SCREEN_WIDTH)
                    y = random.randrange(-200, SCREEN_HEIGHT + 200)
                else:
                    x = random.randrange(-500, SCREEN_WIDTH + 500)
                    y = random.randrange(-1000, 0)
                
                b = Brute(x, y, tx, ty, random.randint(0,360))
                self.brutes.append(b)
    
    def spawnWave(self):
        
        random.seed(RANDOM_SEED)
        
        self.prepareWave()
        self.spawnTargets()
        self.spawnBlockers()
        self.spawnBombers()
        self.spawnBrutes()

    def checkCollisions(self):
        
        self.collideBrutesWithBases()
        self.collideBrutesWithBalls()
        self.collideBallsWithBases()
        self.collideTargetsWithBases()
        self.collideBombersWithBases()
        self.collideBombersWithBalls()
        self.collideBlockersWithBalls()
        self.collideTargetsWithBalls()
        self.clearTheDead()   
        
    def collideBrutesWithBases(self):
        
        # do brute collisions
        for brute in self.brutes:
            for base in self.bases:
                if brute.rect.colliderect(base.rect):
                    brute.dead = True
                    base.dead  = True
                    self.psc.spawnBurstDirection(brute.pos.x, brute.pos.y, 270, 2, 50)
                    sound_base_boom.play()      
        
    def collideBrutesWithBalls(self):
        
        for brute in self.brutes:
            for ball in self.balls:
                if brute.rect.colliderect(ball.rect):
                    brute.dead = True
                    ball.dead  = True
                    self.brutes_killed += 1
                    self.brutes_killed_this_wave += 1
                    self.scoreboard.add(SCORE_BRUTE_HIT)
                    self.psc.spawnBurstDirection(ball.pos.x, ball.pos.y, 270, 2, 50)
                    self.psc.spawnScoreBurst(ball.pos.x, ball.pos.y,SCOREFONT_BRUTE_HIT)
                    sound_big_boom.play()
    
    def collideBallsWithBases(self):
        
        for ball in self.balls:
            for base in self.bases:
                if ball.rect.colliderect(base.rect):
                    base.dead = True
                    ball.dead = True
                    self.psc.spawnBurstDirection(ball.pos.x, ball.pos.y, 270, 2, 100)
                    sound_base_boom.play()
        
    def collideTargetsWithBases(self):
        
        for target in self.targets:
            if target.pos.x <= SCREEN_WIDTH: # check only if onscreen
                for base in self.bases:
                    if target.rect.colliderect(base.rect):
                        base.dead = True
                        target.dead = True
                        self.psc.spawnBurstCircle(target.pos.x, target.pos.y, 50, COLOUR_YELLOW)
                        sound_base_boom.play()
        
    def collideBombersWithBases(self):
        
        for bomber in self.bombers:
            if bomber.pos.y > 0: # check only if onscreen
                for base in self.bases:
                    if bomber.rect.colliderect(base.rect):
                        base.dead = True
                        bomber.dead = True
                        self.psc.spawnBurstDirection(bomber.pos.x, bomber.pos.y, 270, 20, 200)
                        sound_base_boom.play()
        
    def collideBombersWithBalls(self):
        
        for bomber in self.bombers:
            if bomber.pos.y > 0: # check only if onscreen
                for ball in self.balls:
                    if bomber.rect.colliderect(ball.rect):
                        bomber.dead = True
                        ball.dead = True
                        self.bombers_killed += 1
                        self.bombers_killed_this_wave += 1
                        self.scoreboard.add(SCORE_BOMBER_HIT)
                        self.psc.spawnBurstDirection(ball.pos.x, ball.pos.y, 270, 20, 50, COLOUR_YELLOW)
                        self.psc.spawnScoreBurst(ball.pos.x, ball.pos.y,SCOREFONT_BOMBER_HIT)
                        sound_big_boom.play()        
        
    def collideBlockersWithBalls(self):
        
        for blocker in self.blockers:
            if blocker.pos.x <= SCREEN_WIDTH: # only do collision checks if is onscreen
                for ball in self.balls:
                    if blocker.rect.colliderect(ball.rect):
                        
                        # check bottom hit
                        if abs(blocker.rect.bottom - ball.rect.top) < 10 and ball.vel.y < 0:
                            ball.vel.y *= -1
                            
                        # check top hit
                        if abs(blocker.rect.top - ball.rect.bottom) < 10 and ball.vel.y > 0:
                            ball.vel.y *= -1
                            
                        # check left hit
                        if abs(blocker.rect.left - ball.rect.right) < 10 and ball.vel.x > 0:
                            ball.vel.x *= -1
                            ball.pos.x -= 8
                            
                         # check right hit
                        if abs(blocker.rect.right - ball.rect.left) < 10 and ball.vel.x < 0:
                            ball.vel.x *= -1 
                            ball.pos.x += 8
                        
                        self.blockers_hit += 1
                        sound_blocker.play()
        
    def collideTargetsWithBalls(self):
        
        for target in self.targets:
            if target.pos.x <= SCREEN_WIDTH: # only do collision checks if the target is onscreen
                for ball in self.balls:
                    if not target.isDead() and target.rect.colliderect(ball.rect):
                        target.dead = True
                        ball.dead = True
                        self.targets_killed += 1
                        self.targets_killed_this_wave += 1
                        self.scoreboard.add(SCORE_TARGET_HIT)
                        boomsize = random.randint(5, 30)
                        self.psc.spawnBurstCircle(ball.pos.x, ball.pos.y, boomsize, COLOUR_RED)
                        self.psc.spawnScoreBurst(ball.pos.x, ball.pos.y,SCOREFONT_TARGET_HIT)
                        if boomsize > 20:
                            sound_big_boom.play()
                        else:
                            sound_boom.play()        
        
    def clearTheDead(self):
        
        tc = [t for t in self.targets if not t.isDead()]
        self.targets = tc
        
        bc = [b for b in self.balls if not b.isDead()]
        self.balls = bc
        
        bl = [b for b in self.bombers if not b.isDead()]
        self.bombers = bl
        
        ba = [b for b in self.bases if not b.isDead()]
        self.bases = ba
        
        br = [b for b in self.brutes if not b.isDead()]
        self.brutes = br
        
        
    def fireCannon(self, mousex, mousey):
        
        if self.shots_fired < self.maxballs and len(self.balls) < self.max_burst_fire:
            b = Cannonball(self.cannon_pos_x, self.cannon_pos_y)
            f = Vector2(mousex, mousey)
            f.sub(b.pos)
            f.normalise()
            f.mult(self.cannon_firepower) 
            b.launch(f)
            self.balls.append(b)
            sound_gunfire.play()
            self.shots_fired += 1
        else:
            sound_dryfire.play()

    def spacebarPressed(self):
        
        # handles when spacebar is pressed
        if self.gamestate in [GAME_STATE_INTRO, GAME_STATE_OVER] or self.gamemode == GAME_MODE_REPLAY:
            self.gamemode = GAME_MODE_LIVE
            self.clearReplayRecording()
            self.startGame()
            self.playGameMainSong()
            self.gamestate = GAME_STATE_IN_PROGRESS
    
    def clearReplayRecording(self):
        
        self.recording = []
            
    def updateGameStats(self):

        # _this_wave fields are reset to zero in prepareWave()
    
        if self.shots_fired > 0:
            self.shot_accuracy_this_wave = ((self.targets_killed_this_wave + self.bombers_killed_this_wave + self.brutes_killed_this_wave) / self.shots_fired) * 100
        else:
            self.shot_accuracy_this_wave = 0
        
        # calculates the bonus and stats at wave end
        self.bullet_bonus = (self.maxballs - self.shots_fired) * (10 * len(self.bases))
        self.shots_fired_total += self.shots_fired
        total_kills_so_far = self.targets_killed + self.bombers_killed + self.brutes_killed
        
        if self.shots_fired_total > 0:
            self.shot_accuracy = (total_kills_so_far / self.shots_fired_total) * 100
        else:
            self.shot_accuracy = 0
            
        self.scoreboard.add(self.bullet_bonus)
               
    def drawIntroScreen(self):
        
        textsurf = myfont80.render('LAST', 0, COLOUR_RED)
        textsurf.set_alpha(160)
        screen.blit(textsurf, (20,20))
        textsurf = myfont80.render('BUNNER!', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (20,120))
        textsurf = myfont30.render('press spacebar!', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (20,540))
        self.scoreboard.drawHighScoreTable()
        screen.blit(image_bunny1, (486, 64))
        
    def drawWaveOver(self):
        
        self.gamestate_delay += 1
        
        if self.gamestate_delay == 1:
            self.updateGameStats()
        else:            
            textsurf = myfont80.render('Wave Cleared!', 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,20))
            
            textsurf = myfont20.render('Targets killed ... ' + str(self.targets_killed), 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,140))
            
            textsurf = myfont20.render('Bombers killed ... ' + str(self.bombers_killed), 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,180))
            
            textsurf = myfont20.render('Brutes killed ... ' + str(self.brutes_killed), 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,220))
            
            msg = 'Wave accuracy ... {:.2f}'.format(self.shot_accuracy_this_wave)
            textsurf = myfont20.render(msg, 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,260))
        
            msg = 'Game accuracy ... {:.2f}'.format(self.shot_accuracy)
            textsurf = myfont20.render(msg, 0, COLOUR_RED)
            textsurf.set_alpha(150)
            screen.blit(textsurf, (20,300))

            textsurf = myfont20.render('Bullet bonus ... ' + str(self.bullet_bonus), 0, COLOUR_RED)
            textsurf.set_alpha(100)
            screen.blit(textsurf, (20,340))

        if self.gamestate_delay > self.fps * 5:
            self.gamestate = GAME_STATE_IN_PROGRESS
            self.gamestate_delay = 0
            self.spawnWave()
            
    def drawLastBaseLost(self):
        
        self.gamestate_delay += 1
        
        if self.gamestate_delay == 1:
            self.updateGameStats() 
            self.playGameOverSong()
            
        elif self.gamestate_delay > self.fps * 4:
            self.gamestate = GAME_STATE_OVER
            self.gamestate_delay = 0
       
    def playGameOverSong(self):
        
        sound_track_main.fadeout(500)
        sound_track_main_game_over.set_volume(0.2)
        sound_track_main_game_over.play()
        
    def playGameMainSong(self):
        
        sound_track_main_game_over.stop()
        sound_track_main.set_volume(0.2)
        sound_track_main.play(-1)
        
    def drawGameOver(self):
        
        textsurf = myfont80.render('DEDZ !!!', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (20,20))
        
        textsurf = myfont20.render('Targets killed ... ' + str(self.targets_killed), 0, COLOUR_RED)
        textsurf.set_alpha(200)
        screen.blit(textsurf, (20,140))
        
        textsurf = myfont20.render('Bombers killed ... ' + str(self.bombers_killed), 0, COLOUR_RED)
        textsurf.set_alpha(200)
        screen.blit(textsurf, (20,180))
        
        textsurf = myfont20.render('Brutes killed ... ' + str(self.brutes_killed), 0, COLOUR_RED)
        textsurf.set_alpha(200)
        screen.blit(textsurf, (20,220))
    
        msg = 'Accuracy ... {:.2f}'.format(self.shot_accuracy)
        textsurf = myfont20.render(msg, 0, COLOUR_RED)
        textsurf.set_alpha(200)
        screen.blit(textsurf, (20,260))
        
        textsurf = myfont30.render('You Scored ... {}'.format(self.scoreboard.score), 0, COLOUR_RED)
        textsurf.set_alpha(200)
        screen.blit(textsurf, (20,300))
        
        textsurf = myfont30.render('R = View Replay.', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (20, 480))
        
        textsurf = myfont30.render('Spacebar = Play Again.', 0, COLOUR_RED)
        textsurf.set_alpha(255)
        screen.blit(textsurf, (20, 540))
        
        self.scoreboard.drawHighScoreTable()
            
    def draw(self, mousex, mousey, click):
        
        if self.gamestate == GAME_STATE_INTRO:
            
            self.starfield.update()
            self.starfield.draw()
            self.drawIntroScreen()
            
        elif self.gamestate == GAME_STATE_IN_PROGRESS:
            
            self.current_tick += 1
            
            self.wave_seconds = MAX_WAVE_TIME - (self.current_tick - self.wave_start_tick) // 60
            
            self.reticule.update(mousex, mousey, self.max_burst_fire - len(self.balls))
            
            if click:
                self.fireCannon(mousex, mousey)
                
            self.scoreboard.update()
            self.starfield.update()
            self.psc.update()
            
            for ball in self.balls:
                if ball.isflying:
                    ball.applyForce(self.gravity)
                    ball.applyForce(self.getDrag(ball))
                ball.update()
                
            for target in self.targets:
                target.update()
                
            for blocker in self.blockers:
                blocker.update()
                
            for bomber in self.bombers:
                bomber.update()
                
            for base in self.bases:
                base.update()
                
            for brute in self.brutes:
                brute.update()
                
            self.checkCollisions()
            
            self.starfield.draw()
            self.reticule.draw()
            self.scoreboard.draw(self.shots_fired, self.maxballs, self.wave_number, self.wave_seconds)
            
            for target in self.targets:
                target.draw()
                
            for blocker in self.blockers:
                blocker.draw()
                
            for bomber in self.bombers:
                bomber.draw()
                
            for brute in self.brutes:
                brute.draw()
                
            for ball in self.balls:
                ball.draw()
                
            for base in self.bases:
                base.draw()
        
        elif self.gamestate == GAME_STATE_WAVE_OVER:
            
            self.starfield.update()
            self.starfield.draw()
            self.psc.update()
            self.drawWaveOver()
            
        elif self.gamestate == GAME_STATE_LAST_BASE_LOST:
            
            self.starfield.update()
            self.starfield.draw()
            self.psc.update()
            self.drawLastBaseLost()
            pygame.mixer.music.stop()
            
        elif self.gamestate == GAME_STATE_OVER:
            
            self.scoreboard.finish()
            self.starfield.update()
            self.starfield.draw()
            self.drawGameOver()
                     
            
    def run(self):
        
        done = False
        
        while not done:
            
            if self.slowmotion:
                pygame.time.wait(50)
            
            if len(self.bases) > 0:
                if len(self.targets) == 0 or self.wave_seconds == 0:
                    self.gamestate = GAME_STATE_WAVE_OVER
            else:
                if self.gamestate == GAME_STATE_IN_PROGRESS:
                    self.gamestate = GAME_STATE_LAST_BASE_LOST
            
            if self.gamemode == GAME_MODE_LIVE:
                mousex, mousey = pygame.mouse.get_pos()
                
            click = False
    
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:  
                    done = True
                    
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        done = True
                    elif (event.key == pygame.K_SPACE):
                        game.spacebarPressed()
                    elif (event.key == pygame.K_r):
                        self.startReplay()
                    elif (event.key == pygame.K_s):
                        self.toggleSlowMotion()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        click = True
                        
            if self.gamestate == GAME_STATE_IN_PROGRESS:
                if self.gamemode == GAME_MODE_LIVE: 
                    self.recording.append( (mousex, mousey, click) )
                else:
                    # game is showing a replay of last game
                    if self.thisframe < self.replay_length:
                        mousex, mousey, click = self.recording[self.thisframe]
                        self.thisframe += 1
                
            screen.fill(COLOUR_BLACK)
            game.draw(mousex, mousey, click)
            
            # ~ fps = str(int(clock.get_fps()))
            # ~ fps_text = myfont20.render(fps, 0, COLOUR_WHITE)
            # ~ screen.blit(fps_text, (20, 540))
            
            clock.tick(self.fps)
            pygame.display.flip()
        
game = Game()
game.run()
pygame.quit()