from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')

run = [load_image('knight_run_front.png'),
       load_image('knight_run_back.png'),
       load_image('knight_run_front_right.png'),
       load_image('knight_run_front_left.png')
       ]
run_frame = [6,6,6,6]

x = 600
y=500
frame = 0
looking =0

running = True

while (running):
    clear_canvas()
    x1, y1 = x, y
    x2, y2 = random.randint(50,TUK_WIDTH), random.randint(50,TUK_HEIGHT)
    if x1 < x2:
        looking = 2
    else:
        looking = 3
    frame = 0
    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        tuk_ground.draw(TUK_WIDTH / 2, TUK_HEIGHT / 2)
        run[looking].clip_draw(frame * (int(run[looking].w / run_frame[looking])), 0,
                               int(run[looking].w / run_frame[looking]), run[looking].h, x, y,
                               int(run[looking].w / run_frame[looking]) * 4, run[looking].h * 4)
        hand.draw(x2, y2)
        update_canvas()
        frame = (frame + 1) % run_frame[looking]
        delay(0.05)
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    running = False

        if not running:
            break

close_canvas()