import tkinter as tk
import random as random
import time
window = tk.Tk()

x = 100
y = 100
direction = 0
impath = 'gifs'  # Ensure this path is correct
idle_frames = [tk.PhotoImage(file=impath + 'idle.gif', format=f'gif -index {i}') for i in range(11)]  # Change range to match the number of frames in your GIF
walking_frames = [tk.PhotoImage(file=impath + 'walking.gif', format=f'gif -index {i}') for i in range(6)]  # Change range to match the number of frames in your GIF
walking_frames2 = [tk.PhotoImage(file=impath + 'walking2.gif', format=f'gif -index {i}') for i in range(6)]  # Change range to match the number of frames in your GIF
label = tk.Label(window)
label.pack()
animationFrames = idle_frames
currentAnimation = 2

def checkBounds():
    global x, y
    maxX = window.winfo_screenwidth()
    maxY = window.winfo_screenheight()
    width = animationFrames[0].width()
    height = animationFrames[0].height()

    if x + width > maxX:
        x = maxX - width
    elif x < 0:
        x = 0
    if y + height > maxY:
        y = maxY - height
    elif y < 0:
        y = 0

def movement(timeMoving, directionX, directionY):
    global currentAnimation
    returnValue = False
    end_time = time.time() + timeMoving
    if directionX < 0:
        currentAnimation = 1
    else:
        currentAnimation = 2
    def step():
        global x, y, currentAnimation
        if time.time() >= end_time:
            currentAnimation = 0
            returnValue = True
            return
        x += directionX
        y += directionY
        checkBounds()
        window.geometry(f"+{int(x)}+{int(y)}")
        window.after(30, step)
    step()
    return returnValue
    
    
#0 is idle, 1 is left, 2 is right for currentAnimation
def updateFrame(frame_index):
    global walking_frames, walking_frames2, idle_frames, currentFrames, currentAnimation
    if currentAnimation == 0:
        animationFrames = idle_frames
    elif currentAnimation == 1:
        animationFrames = walking_frames2
    else:
        animationFrames = walking_frames
    currentFrames = animationFrames
    label.configure(image=animationFrames[frame_index])
    window.after(225, updateFrame, (frame_index + 1) % len(animationFrames))
    width = animationFrames[0].width()
    height = animationFrames[0].height()
    window.geometry(f"{width}x{height}")


def movementLogic(randomTime):
    global currentAnimation
    movementX = random.randint(-3, 3)
    movementY = random.randint(-3, 3)
    testingValue = movement(randomTime, movementX, movementY)
    print("Testing: ", testingValue)
    print("Xdirection: ", movementX)
    print("Ydirection: ", movementY)
    print("Time: ",randomTime)

#basically the problem is that I can move and animate at the same time
#but I don't know how to call them again after it finished and do idle for a short while
    

#movement(6, -1, 1)

def setup():
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-transparentcolor", "#658DD1")
    updateFrame(0)
    
setup()
ij = 0
while ij == 0:
    randomTime = random.randint(1, 10)
    movementLogic(randomTime)
    time.sleep(randomTime)


