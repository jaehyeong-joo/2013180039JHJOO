from pico2d import *


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)

    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    elif dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    elif dir == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    elif dir == 2:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, 90)
    elif dir == 3:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, 90)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if dir == 1 or dir == -1:
        if x == 20 and dir == -1:
            x += 0
        elif x == 780 and dir == 1:
            x += 0
        else:
            x += dir

    delay(0.001)

close_canvas()
