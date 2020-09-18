from pico2d import *

open_canvas()

grass = load_image ('grass.png')
ch = load_image('animation_sheet.png')

grass.draw_now(400,30)
ch.draw_now(400,80)

x = 0
frame_index=0
action = 0;
while x < 800:
    clear_canvas()
    grass.draw(400,30)
    ch.clip_draw(frame_index*100,100*action,100,100,x,85)
    update_canvas()

    get_events()
    # for e in evts:
    # print(e)

    x+=2
    delay(0.02)
    #frame_index +=10
    #if sx > = 8 : frame_index=0
    frame_index = (frame_index + 1) % 8

    if x % 100 == 0:
        action = (action+1)%4
    


delay(2)
close_canvas()
