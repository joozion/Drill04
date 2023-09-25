from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet_1.png')


def handle_events():
    global running
    global xdir, ydir, sheet

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                sheet = 1
            elif event.key == SDLK_LEFT:
                xdir -= 1
                sheet = 2
            elif event.key == SDLK_UP:
                ydir += 1
                sheet = 0
            elif event.key == SDLK_DOWN:
                ydir -= 1
                sheet = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
                sheet = 3
            elif event.key == SDLK_LEFT:
                xdir += 1
                sheet = 3
            elif event.key == SDLK_UP:
                ydir -= 1
                sheet = 3
            elif event.key == SDLK_DOWN:
                ydir += 1
                sheet = 3


running = True
frame = 0
sheet = 3
xdir, ydir = 0, 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()



while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 137, sheet * 137, 137, 136, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    if x < TUK_WIDTH and x > 0:
        x += xdir * 5
    elif x >= TUK_WIDTH:
        x = x - 5
    elif x <= 0:
        x = x + 5
    if y < TUK_HEIGHT and y > 0:
        y += ydir * 5
    elif y >= TUK_HEIGHT:
        y = y - 5
    elif y <= 0:
        y = y + 5
    delay(0.01)

close_canvas()
