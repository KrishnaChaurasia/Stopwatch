# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
minute = 0
sec = 0
ms = 0
x = 0
y = 0
flag = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time, minute, sec, ms
    time = t
    if(time/600 != 0):
        minute = minute + time/600
        time = time - 100*int((time/100))
        sec = time/10
        ms = time%10
        time = 0  
    elif(time/100 != 0):
        sec = time/10
        ms = time%10        
    elif(time/10 != 0):
        sec = time/10;
        ms = time%10
    else:
        ms = time

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global flag
    timer.start()
    flag = 1
    
def stop():
    global x, y, ms, flag
    timer.stop()
    if(flag != 0):
        if(ms == 0):
            x += 1
        y += 1
    
    
def reset():
    global time, minute, sec, ms, x, y, flag
    timer.stop()
    time = 0
    minute = 0
    sec = 0
    ms = 0
    x = 0
    y = 0
    flag = 0

# define event handler for timer with 0.1 sec interval
def ticks():
    global time
    time += 1
    
# define draw handler
def draw(canvas):
    global time, minute, sec, ms, x, y
    format(time)
    if(len(str(sec)) == 1):
        strsec = "0" + str(sec)
    else:
        strsec = str(sec)            
    canvas.draw_text(str(x) + "/" + str(y), [150,36], 36, "White")
    canvas.draw_text(str(minute) + ":" + strsec + "." + str(ms), [75, 100], 36, "White") 
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# register event handlers
timer = simplegui.create_timer(100, ticks)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
