from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import glob
import time
from functions.movie_functions import load_movie, load_next_stimulus
from modules.Serial_functions import open_serial, send_data_until_confirmation
from modules.functions import calibrate_lick_sensor, lick_detection, led_on, led_off, give_reward

n_trials = 500
valve_duration = 100  # in ms

test_mode = False
if not test_mode:
    serial_obj = open_serial(COM_port='COM3', baudrate=9600)
    # ADJUST_TOUCHLEVEL = 75
    # send_data_until_confirmation(serial_obj, header_byte=ADJUST_TOUCHLEVEL, data=[3])
    calibrate_lick_sensor(serial_obj)
    print('ready')

    give_reward(serial_obj, valve_duration=valve_duration)
#

sound_1 = sound.Sound(value='d', secs=0.5, octave=8, stereo=True, volume=0.5, loops=0, sampleRate=44100, hamming=True, name='', autoLog=True)
sound_2 = sound.Sound(value='c', secs=0.2, octave=4, stereo=True, volume=0.5, loops=0, sampleRate=44100, hamming=True, name='', autoLog=True)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Audiovisual_only_target'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
     core.quit()  # user pressed cancel
#

expInfo['date'] = data.getDateStr()  # add a simple timestamp

expInfo['expName'] = expName
image_list = (0.38, 0.38, 0.38)
#print image_list
trialnumber = 0
bias = np.zeros((n_trials, 4))
#print len(bias)
last_choice = ''
left = 0
right = 0
same = 0
opposite = 0
correct_trials = np.zeros((n_trials, 1))
reactiontime = np.zeros((n_trials, 1))
correctstim = ''
orientation_difference=0
orientation=0
correct_trial=0
save_reactiontime=0
save_correct=0
save_difference=0
save_orientation=0
correct_orientation=0
orientation_range=1
orientation_diff_list=[90]
touch_delay=0
lick_delay=0
correct_output=0
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s_%s' % \
           (expInfo['participant'], os.path.splitext(expName)[0], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=os.path.splitext(expName)[0], version='', extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None, savePickle=True, saveWideText=True, dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
# size=(1920, 1080)
win = visual.Window(size=(600, 400), fullscr=True, screen=1, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[-0.01, -0.01, -0.01], colorSpace='rgb',
                    blendMode='avg', useFBO=True, multiSample=True, numSamples=16)

win.mouseVisibile = False
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0  # couldn't get a reliable measure so guess
#

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

file_name = list(['example1.mp4',
                  'example1.mp4'])

target_mov = load_movie(win, file_name[0], noAudio=False, opacity=1., pos=(200, 0))
# distractor_mov = load_movie(win, file_name[1], noAudio=True, opacity=1., pos=(-200, 0))

# target_mov = visual.MovieStim3(win, file_name[0], flipVert=False, pos=[-200, 0], noAudio=False, loop=True)
# distractor_mov = visual.MovieStim3(win, file_name[1], flipVert=False, pos=[200, 0], noAudio=True, loop=True)

# target_mov.setAutoDraw(True)
# distractor_mov.setAutoDraw(True)

target_mov.stop()
# distractor_mov.stop()

# target_mov.play()
# distractor_mov.play()

mouse = event.Mouse(win=win, visible=False)
x, y = [None, None]
cross = visual.ShapeStim(win=win, name='cross', units='cm',
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=3,
    closeShape=False,
    lineColor='white'
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
print('Generating trials ...')
trials = data.TrialHandler(nReps=n_trials, method='random',
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials')
print('Done generating trials!')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    stop_session = False

    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(121.000000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(cross)
    trialComponents.append(target_mov)
    # trialComponents.append(distractor_mov)
    trialComponents.append(mouse)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
            
    # chosen_image=np.random.randint(0, high=len(image_list))
    # target_mov.setSF(image_list[chosen_image])
    # distractor_mov.setSF(image_list[chosen_image])
    # #target_mov.setImage(image_list[chosen_image])
    # #distractor_mov.setImage(image_list[chosen_image])
    trialnumber=trialnumber+1
    # orientation_list=[90]
    # orientation_list=(orientation_list)
    mouse.setPos((0, 0))

    #
    
    # ## bias correction
    if trialnumber < 10:
        if np.random.uniform(0, high=100) <= 50:
            # load_next_stimulus(target_mov=target_mov, distractor_mov=distractor_mov,
            #                    target_path=file_name[1], distractor_path=file_name[0], target_side_left=False)
            #
            # # target_mov = load_movie(win, file_path, noAudio=True, opacity=1.)
            # # distractor_mov = load_movie(win, file_path_2, noAudio=True, opacity=1.)
            # target_mov.play()
            # distractor_mov.play()

            '''
            orientation=orientation_list[np.random.randint(0,high=len(orientation_list),size=1)]
            target_mov.setOri(orientation)
            orientation_difference=orientation_diff_list[np.random.randint(0,high=orientation_range,size=1)]
            correct_orientation=int(orientation+orientation_difference)
            distractor_mov.setOri(correct_orientation)
            correctstim='right'
            '''
            correctstim = 'right'
        #
            
        if np.random.uniform(0, high=100) > 50:
            '''
            orientation=orientation_list[np.random.randint(0,high=len(orientation_list),size=1)]
            distractor_mov.setOri(orientation)
            orientation_difference=orientation_diff_list[np.random.randint(0,high=orientation_range,size=1)]
            correct_orientation=int(orientation+orientation_difference)
            target_mov.setOri(correct_orientation)
            correctstim='left'
            '''

            # # target_mov = load_movie(win, file_path_2, noAudio=True, opacity=1.)
            # # distractor_mov = load_movie(win, file_path, noAudio=False, opacity=1.)
            # load_next_stimulus(target_mov=target_mov, distractor_mov=distractor_mov,
            #                    target_path=file_name[1], distractor_path=file_name[0],
            #                    target_side_left=correctstim == 'left')
            # target_mov.play()
            # distractor_mov.play()

            correctstim = 'left'
        #
    else:
        # Use Bias-correction
        bias_left = np.abs(left)
        bias_right = np.abs(right)
        bias_same = np.abs(same)
        bias_opposite = np.abs(opposite)
        if np.abs(bias_left-bias_right) == np.abs(bias_same-bias_opposite):
            if np.random.uniform(0, high=100) <= 50:
                # orientation=orientation_list[np.random.randint(0,high=len(orientation_list),size=1)]
                # target_mov.setOri(orientation)
                # orientation_difference=orientation_diff_list[np.random.randint(0,high=orientation_range,size=1)]
                # correct_orientation=int(orientation+orientation_difference)
                # distractor_mov.setOri(correct_orientation)
                correctstim = 'right'
            else:
                correctstim = 'left'
            #
        #

        if np.abs(bias_left-bias_right) > np.abs(bias_same-bias_opposite):
            if bias_left > bias_right:
                correctstim = 'right'
            else:
                correctstim = 'left'
            #
        #

        if np.abs(bias_left-bias_right) < np.abs(bias_same-bias_opposite):
            if bias_same < bias_opposite:
                if last_choice == 'left':
                    correctstim = 'left'
                    
                if last_choice == 'right':
                    correctstim = 'right'
                #
                   
            if bias_same > bias_opposite:
                if last_choice == 'left':
                    correctstim = 'right'
                else:
                    correctstim = 'left'
                #
            #
        #
    #

    #

    # ##################################################################################################################
    # Update Stimuli:

    target_id = int(np.random.rand() < 0.5)
    distractor_id = 1 - target_id
    load_next_stimulus(target_mov=target_mov, distractor_mov=None,
                       target_path=file_name[target_id], distractor_path=file_name[distractor_id],
                       target_side_left=correctstim == 'left')
    target_mov.play()
    # distractor_mov.play()
    # ##################################################################################################################

    # gerion = 0

    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # mouse.setPos((0, 0))

        # # # # # # # # #
        # INSERT - GERION
        # if t > 6 and gerion == 0:
        #     if np.random.rand() > 0.5:
        #         mouse.setPos((1, 0))
        #         print('Simulated answer: LEFT')
        #     else:
        #         mouse.setPos((0, 1))
        #         print('Simulated answer: RIGHT')
        #     #
        # elif t > 20:
        #     core.quit()
        #
        # # # # # # # # #

        mouse_info = mouse.getPos()[0]
        # print(mouse_info)

        # target_mov.setPhase(t*2)
        # distractor_mov.setPhase(t*2)
        if t > 120:
            print('timeout')
            core.quit()
        # print mouse_info
        # update/draw components on each frame
        if mouse_info > 0:
            bias[trialnumber-1, 0] = 1  # colloumnds in bias array: 0=left, 1=right, 2=same. 3=opposite
            bias[trialnumber-1, 1] = 0
            last_choice = 'left'
        if mouse_info < 0:
            bias[trialnumber-1, 0] = 0
            bias[trialnumber-1, 1] = 1
            last_choice='right'
            
        # *cross* updates
        if t >= 0.5 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t  # underestimates by a little under one framef
            cross.frameNStart = frameN  # exact frame index
            cross.setAutoDraw(True)
        if cross.status == STARTED and t >= (0.5 + (0.5-win.monitorFramePeriod*0.75)):  # most of one frame period left
            cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        # *target_mov* updates
        if t >= 1.2 and target_mov.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_mov.tStart = t  # underestimates by a little under one frame
            target_mov.frameNStart = frameN  # exact frame index
            target_mov.setAutoDraw(True)
        if target_mov.status == STARTED and mouse_info != 0:  # most of one frame period left
            target_mov.setAutoDraw(False)
            if mouse_info > 0:
                # last_choice == 'left'
                # reactiontime[trialnumber-1] = 0
                save_reactiontime = 0
                if correctstim == 'left' and trialnumber > 0:
                    touch_delay = trialClock.getTime()
                    correct_trials[trialnumber-1] = 1.
                    correct_trial = 1.
                    sound_2 = sound.Sound(value='c', secs=0.2, octave=4, stereo=True, volume=1., loops=0,
                                          sampleRate=44100, hamming=True, name='', autoLog=True)
                    sound_2.play()
                    # # distractor_mov.setAutoDraw(False)
                    # target_mov.setAutoDraw(False)
                    # distractor_mov.stop()
                    target_mov.stop()
                    time.sleep(0.4)

                    if not test_mode:
                        led_on(serial_obj)
                        stop_session = lick_detection(win, serial_obj, valve_duration=valve_duration)
                        led_off(serial_obj)
                    #
                    lick_delay=trialClock.getTime()
                    mouse.setPos((0,0))
                    
                if correctstim=='right' and trialnumber>0:
                    correct_trial=0.
                    touch_delay=trialClock.getTime()
                    win.color=[1,1,1]
                    win.flip()
                    # sound_1 = sound.Sound(value='d', secs=0.5, octave=8, stereo=True, volume=0.5, loops=0, sampleRate=44100, bits=16, hamming=True, start=0, stop=-1, name='', autoLog=True)
                    sound_1 = sound.Sound(value='d', secs=0.5, octave=8, stereo=True, volume=1., loops=0,
                                          sampleRate=44100, hamming=True, name='', autoLog=True)
                    sound_1.play()
                    time.sleep(0.2)
                    mouse.setPos((0,0))
                    # target_mov.setAutoDraw(False)
                    # # distractor_mov.setAutoDraw(False)
                    target_mov.stop()
                    # distractor_mov.stop()

                    if not test_mode:
                        stop_session = lick_detection(win, serial_obj, rewarded=False, valve_duration=valve_duration)
                    #
                    win.color=[0,0,0]
                    win.flip()

                    lick_delay=trialClock.getTime()
                    mouse.setPos((0,0))

        # *distractor_mov* updates
        # if t >= 1.2 and distractor_mov.status == NOT_STARTED:
        #     # keep track of start time/frame for later
        #     distractor_mov.tStart = t  # underestimates by a little under one frame
        #     distractor_mov.frameNStart = frameN  # exact frame index
        #     distractor_mov.setAutoDraw(True)
        if mouse_info != 0.:  # most of one frame period left
            # distractor_mov.setAutoDraw(False)
            if mouse_info < 0:
                last_choice == 'right'
                reactiontime[trialnumber-1]=0
                save_reactiontime=0
                if correctstim=='right' and trialnumber>0:
                    touch_delay=trialClock.getTime()
                    correct_trials[trialnumber-1]=1.
                    correct_trial=1
                    sound_2 = sound.Sound(value='c', secs=0.2, octave=4, stereo=True, volume=0.5, loops=0,
                                          sampleRate=44100, hamming=True, name='', autoLog=True)
                    sound_2.play()
                    # distractor_mov.stop()
                    target_mov.stop()
                    time.sleep(0.4)

                    if not test_mode:
                        led_on(serial_obj)
                        stop_session = lick_detection(win, serial_obj, valve_duration=valve_duration)
                        led_off(serial_obj)
                    #
                    # distractor_mov.setAutoDraw(False)
                    # target_mov.setAutoDraw(False)

                    lick_delay=trialClock.getTime()
                    mouse.setPos((0,0))
                    
                if correctstim=='left' and trialnumber>0:
                    correct_trial=0.
                    touch_delay=trialClock.getTime()
                    win.color=[1,1,1]
                    win.flip()
                    # sound_1 = sound.Sound(value='d', secs=0.5, octave=8, stereo=True, volume=0.5, loops=0, bits=16,
                    #                       sampleRate=44100, hamming=True, start=0, stop=-1, name='', autoLog=True)
                    sound_1 = sound.Sound(value='d', secs=0.5, octave=8, stereo=True, volume=1., loops=0,
                                          sampleRate=44100, hamming=True, name='', autoLog=True)
                    sound_1.play()
                    time.sleep(0.2)
                    target_mov.setAutoDraw(False)
                    # distractor_mov.setAutoDraw(False)
                    win.flip()

                    if not test_mode:
                        stop_session = lick_detection(win, serial_obj, rewarded=False, valve_duration=valve_duration)
                    #

                    win.color=[0,0,0]
                    win.flip()

                    lick_delay=trialClock.getTime()
                    mouse.setPos((0,0))
                    
        save_orientation=int(orientation)
        save_correct=int(correct_trial)
        save_difference=int(np.abs(correct_orientation-orientation))
        save_reactiontime=float(save_reactiontime)
           
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t  # underestimates by a little under one frame
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            mouse.setPos((0,0))
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED and mouse_info!=0: #most of one frame period left
            mouse.status = STOPPED
        #if mouse.status == STARTED:  # only update if started and not stopped!
        #    buttons = mouse.getPressed()
        #    if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
        #        continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        
        # check for quit (the Esc key)
        if stop_session or endExpNow or event.getKeys(keyList=["escape"]):
            stop_session = True
            break
        #

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    if bias[trialnumber-1,0]+bias[trialnumber-2,0]==2:
        bias[trialnumber-1,2]=1
    if bias[trialnumber-1,0]+bias[trialnumber-2,0]==1:
        bias[trialnumber-1,3]=1
    if bias[trialnumber-1,1]+bias[trialnumber-2,1]==2:
        bias[trialnumber-1,2]=1
    if bias[trialnumber-1,1]+bias[trialnumber-2,1]==1:
        bias[trialnumber-1,3]=1
    
    if trialnumber>10:
        left=np.sum(bias[trialnumber-11:trialnumber-1,0])
        right=np.sum(bias[trialnumber-11:trialnumber-1,1])
        same=np.sum(bias[trialnumber-11:trialnumber-1,2])
        opposite=np.sum(bias[trialnumber-11:trialnumber-1,3])
    
    correct_output=correct_output+correct_trial
    print(correct_output/trialnumber)
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    # trials.addData('imagename', image_list[chosen_image])
    trials.addData('target_movie', file_name[target_id])
    trials.addData('distractor_movie', file_name[distractor_id])
    trials.addData('correct',save_correct)
    trials.addData('Difference',save_difference)
    trials.addData('touch_delay', touch_delay)
    trials.addData('lick_delay', lick_delay)
    trials.addData('orientation', save_orientation)
    trials.addData('correctstim', correctstim)
    trials.addData('last_choice', last_choice)
    #trials.addData('bias', bias)
    thisExp.nextEntry()

    try:
        if stop_session:
            break
        #
    except:
        pass
    #
#

win.close()
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
# while True:
#     time.sleep(1.)
# #
# while True:
#     if event.getKeys(keyList=["escape"]):
#         break
#     #
# #

# time.sleep(20.)
dlg = gui.DlgFromDict(dictionary={'press OK': 'press OK'}, title='Quit?')
core.quit()
