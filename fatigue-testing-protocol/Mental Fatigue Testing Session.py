#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on March 24, 2025, at 12:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

document.body.style.cursor='auto';


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'Mental Fatigue Testing Session'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age (years)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\sofia\\Desktop\\YEAR5\\Thesis\\Code\\Inducing Mental Fatigue\\Data Collection\\mental-fatigue-battery-testing-session\\Mental Fatigue Testing Session.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
elapsedTime = util.Clock()
key_resp = keyboard.Keyboard()
instrHeaderText = visual.TextStim(win=win, name='instrHeaderText',
    text='Introduction',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-4.0);
text = visual.TextStim(win=win, name='text',
    text='Welcome to the testing session\n\nBefore you begin, please make sure that you are sitting comfortably in a quiet environment where you will not be interrupted. Please also ensure that your computer is connected to a power source and will not enter sleep mode\n\nIn this session you will spend 2-3 hours repeating the tasks that you learned in the training session. There will be multiple chances for you to take rest breaks if you need to\n\nIf you decide that you do not want to continue you can press the escape key at any time to quit the experiment. If you quit, your data will not be saved\n\nBefore the tasks begin, you will complete some ratings. Please press the right arrow on your keyboard to continue',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "F_ISA"
F_ISAClock = core.Clock()
mouse_22 = event.Mouse(win=win)
x, y = [None, None]
mouse_22.mouseClock = core.Clock()
Timer = util.Clock()
slider = visual.Slider(win=win, name='slider',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("very low (alert)", "low", "medium", "very high (fatigued)"), ticks=(1, 2, 3, 4, 5),
    granularity=0, style=('rating', 'whiteOnBlack'),
    color='LightGray', font='Arial',
    flip=False)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Please rate your level of mental fatigue  from 1-5:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse_visibility = visual.Polygon(
    win=win, name='mouse_visibility',
    edges=180, size=(0.25, 0.25),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "instrBRUMSpre"
instrBRUMSpreClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='On the next few screens there are lists of words that describe feelings people have\n\nPlease read each one carefully. Then click the answer which best describes how you feel right now\n\nMake sure you answer every question\n\nPlease press the mouse to begin\n\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
BRUMSheader = visual.TextStim(win=win, name='BRUMSheader',
    text='Rating Scale Instructions',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BRUMS_1"
BRUMS_1Clock = core.Clock()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
mouse_visibility_fix = visual.Polygon(
    win=win, name='mouse_visibility_fix',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
slider1 = visual.Slider(win=win, name='slider1',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider2 = visual.Slider(win=win, name='slider2',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider3 = visual.Slider(win=win, name='slider3',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider4 = visual.Slider(win=win, name='slider4',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider5 = visual.Slider(win=win, name='slider5',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider6 = visual.Slider(win=win, name='slider6',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider7 = visual.Slider(win=win, name='slider7',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider8 = visual.Slider(win=win, name='slider8',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Rating Scales: Page 1 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
panicky = visual.TextStim(win=win, name='panicky',
    text='Panicky',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
lively = visual.TextStim(win=win, name='lively',
    text='Lively',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
confused = visual.TextStim(win=win, name='confused',
    text='Confused',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
wornout = visual.TextStim(win=win, name='wornout',
    text='Worn Out',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
depressed = visual.TextStim(win=win, name='depressed',
    text='Depressed',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
downheartened = visual.TextStim(win=win, name='downheartened',
    text='Downheartened',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
annoyed = visual.TextStim(win=win, name='annoyed',
    text='Annoyed',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
exhausted = visual.TextStim(win=win, name='exhausted',
    text='Exhausted',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "BRUMS_2"
BRUMS_2Clock = core.Clock()
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
mouse_visibility_fix_2 = visual.Polygon(
    win=win, name='mouse_visibility_fix_2',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
slider9 = visual.Slider(win=win, name='slider9',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider10 = visual.Slider(win=win, name='slider10',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider11 = visual.Slider(win=win, name='slider11',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider12 = visual.Slider(win=win, name='slider12',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider13 = visual.Slider(win=win, name='slider13',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider14 = visual.Slider(win=win, name='slider14',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider15 = visual.Slider(win=win, name='slider15',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider16 = visual.Slider(win=win, name='slider16',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Rating Scales: Page 2 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
mixedup = visual.TextStim(win=win, name='mixedup',
    text='Mixed-up',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
sleepy = visual.TextStim(win=win, name='sleepy',
    text='Sleepy',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
bitter = visual.TextStim(win=win, name='bitter',
    text='Bitter',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
unhappy = visual.TextStim(win=win, name='unhappy',
    text='Unhappy',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
anxious = visual.TextStim(win=win, name='anxious',
    text='Anxious',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
worried = visual.TextStim(win=win, name='worried',
    text='Worried',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
energetic = visual.TextStim(win=win, name='energetic',
    text='Energetic',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
miserable = visual.TextStim(win=win, name='miserable',
    text='Miserable',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "BRUMS_3"
BRUMS_3Clock = core.Clock()
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
mouse_visibility_fix_3 = visual.Polygon(
    win=win, name='mouse_visibility_fix_3',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
slider17 = visual.Slider(win=win, name='slider17',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider18 = visual.Slider(win=win, name='slider18',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider19 = visual.Slider(win=win, name='slider19',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider20 = visual.Slider(win=win, name='slider20',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider21 = visual.Slider(win=win, name='slider21',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider22 = visual.Slider(win=win, name='slider22',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider23 = visual.Slider(win=win, name='slider23',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider24 = visual.Slider(win=win, name='slider24',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_11 = visual.TextStim(win=win, name='text_11',
    text='Rating Scales: Page 3 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
muddled = visual.TextStim(win=win, name='muddled',
    text='Muddled',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
nervous = visual.TextStim(win=win, name='nervous',
    text='Nervous',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
angry = visual.TextStim(win=win, name='angry',
    text='Angry',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
active = visual.TextStim(win=win, name='active',
    text='Active',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
tired = visual.TextStim(win=win, name='tired',
    text='Tired',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
badtempered = visual.TextStim(win=win, name='badtempered',
    text='Bad tempered',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
alert = visual.TextStim(win=win, name='alert',
    text='Alert',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
uncertain = visual.TextStim(win=win, name='uncertain',
    text='Uncertain',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);

# Initialize components for Routine "instrAXCPTbreak1"
instrAXCPTbreak1Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()
instrHeaderText_2 = visual.TextStim(win=win, name='instrHeaderText_2',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text="Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "AXCPTtrial"
AXCPTtrialClock = core.Clock()
Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];


cue_text = visual.TextStim(win=win, name='cue_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break1 = visual.TextStim(win=win, name='break1',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-2.0);
distractor1 = visual.TextStim(win=win, name='distractor1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
break2 = visual.TextStim(win=win, name='break2',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-4.0);
distractor2 = visual.TextStim(win=win, name='distractor2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
break3 = visual.TextStim(win=win, name='break3',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "AXCPTprobe"
AXCPTprobeClock = core.Clock()
probe_text = visual.TextStim(win=win, name='probe_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AXCPT_resp = keyboard.Keyboard()

# Initialize components for Routine "AXCPTfeedback"
AXCPTfeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text = visual.TextStim(win=win, name='AXCPTfeedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrNBACKbreak2"
instrNBACKbreak2Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
instrHeaderText_3 = visual.TextStim(win=win, name='instrHeaderText_3',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackFirst3Trials"
NBackFirst3TrialsClock = core.Clock()
Back2minus1=[]
Back2minus2=[]
Back2minus3=[]
NBackText_1 = visual.TextStim(win=win, name='NBackText_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackRemainderTrials"
NBackRemainderTrialsClock = core.Clock()
NBackText_2 = visual.TextStim(win=win, name='NBackText_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "NBackFeedback"
NBackFeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text_2 = visual.TextStim(win=win, name='AXCPTfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrSEARCHbreak3"
instrSEARCHbreak3Clock = core.Clock()
instrHeaderText_5 = visual.TextStim(win=win, name='instrHeaderText_5',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "searchTrial"
searchTrialClock = core.Clock()
orientList = [0, 90, 180, 270]
PosList = [[.45, -.45], [.45, -.15], [.45, .15], [.45, .45], [.15, -.45], [.15, -.15], [.15, .15], [.15, .45], [-.15, -.45], [-.15, -.15], [-.15, .15], [-.15, .45], [-.45, -.45], [-.45, -.15], [-.45, .15], [-.45, .45]]
key_resp_14 = keyboard.Keyboard()
targetStim = visual.TextStim(win=win, name='targetStim',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
searchStim2 = visual.TextStim(win=win, name='searchStim2',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
searchStim3 = visual.TextStim(win=win, name='searchStim3',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
searchStim4 = visual.TextStim(win=win, name='searchStim4',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
searchStim5 = visual.TextStim(win=win, name='searchStim5',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
searchStim6 = visual.TextStim(win=win, name='searchStim6',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
searchStim7 = visual.TextStim(win=win, name='searchStim7',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
searchStim8 = visual.TextStim(win=win, name='searchStim8',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
searchStim9 = visual.TextStim(win=win, name='searchStim9',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
searchStim10 = visual.TextStim(win=win, name='searchStim10',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
searchStim11 = visual.TextStim(win=win, name='searchStim11',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "searchFeedback"
searchFeedbackClock = core.Clock()
msg = ' '
searchFeedbackText = visual.TextStim(win=win, name='searchFeedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrMENTROTbreak4"
instrMENTROTbreak4Clock = core.Clock()
key_resp_13 = keyboard.Keyboard()
instrHeaderText_15 = visual.TextStim(win=win, name='instrHeaderText_15',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mentRotTrial"
mentRotTrialClock = core.Clock()
mentRotStimulus = visual.ImageStim(
    win=win,
    name='mentRotStimulus', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.935, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
MROT_resp = keyboard.Keyboard()

# Initialize components for Routine "mentRotFeedback"
mentRotFeedbackClock = core.Clock()
msg = ' '
NBackfeedback_text_2 = visual.TextStim(win=win, name='NBackfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrNBACKbreak5"
instrNBACKbreak5Clock = core.Clock()
key_resp_8 = keyboard.Keyboard()
instrHeaderText_9 = visual.TextStim(win=win, name='instrHeaderText_9',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackFirst3Trials"
NBackFirst3TrialsClock = core.Clock()
Back2minus1=[]
Back2minus2=[]
Back2minus3=[]
NBackText_1 = visual.TextStim(win=win, name='NBackText_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackRemainderTrials"
NBackRemainderTrialsClock = core.Clock()
NBackText_2 = visual.TextStim(win=win, name='NBackText_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "NBackFeedback"
NBackFeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text_2 = visual.TextStim(win=win, name='AXCPTfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrAXCPTbreak6"
instrAXCPTbreak6Clock = core.Clock()
key_resp_6 = keyboard.Keyboard()
instrHeaderText_7 = visual.TextStim(win=win, name='instrHeaderText_7',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text="Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "AXCPTtrial"
AXCPTtrialClock = core.Clock()
Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];


cue_text = visual.TextStim(win=win, name='cue_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break1 = visual.TextStim(win=win, name='break1',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-2.0);
distractor1 = visual.TextStim(win=win, name='distractor1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
break2 = visual.TextStim(win=win, name='break2',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-4.0);
distractor2 = visual.TextStim(win=win, name='distractor2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
break3 = visual.TextStim(win=win, name='break3',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "AXCPTprobe"
AXCPTprobeClock = core.Clock()
probe_text = visual.TextStim(win=win, name='probe_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AXCPT_resp = keyboard.Keyboard()

# Initialize components for Routine "AXCPTfeedback"
AXCPTfeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text = visual.TextStim(win=win, name='AXCPTfeedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrSEARCHbreak7"
instrSEARCHbreak7Clock = core.Clock()
instrHeaderText_11 = visual.TextStim(win=win, name='instrHeaderText_11',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "searchTrial"
searchTrialClock = core.Clock()
orientList = [0, 90, 180, 270]
PosList = [[.45, -.45], [.45, -.15], [.45, .15], [.45, .45], [.15, -.45], [.15, -.15], [.15, .15], [.15, .45], [-.15, -.45], [-.15, -.15], [-.15, .15], [-.15, .45], [-.45, -.45], [-.45, -.15], [-.45, .15], [-.45, .45]]
key_resp_14 = keyboard.Keyboard()
targetStim = visual.TextStim(win=win, name='targetStim',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
searchStim2 = visual.TextStim(win=win, name='searchStim2',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
searchStim3 = visual.TextStim(win=win, name='searchStim3',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
searchStim4 = visual.TextStim(win=win, name='searchStim4',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
searchStim5 = visual.TextStim(win=win, name='searchStim5',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
searchStim6 = visual.TextStim(win=win, name='searchStim6',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
searchStim7 = visual.TextStim(win=win, name='searchStim7',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
searchStim8 = visual.TextStim(win=win, name='searchStim8',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
searchStim9 = visual.TextStim(win=win, name='searchStim9',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
searchStim10 = visual.TextStim(win=win, name='searchStim10',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
searchStim11 = visual.TextStim(win=win, name='searchStim11',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "searchFeedback"
searchFeedbackClock = core.Clock()
msg = ' '
searchFeedbackText = visual.TextStim(win=win, name='searchFeedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrMENTROTbreak8"
instrMENTROTbreak8Clock = core.Clock()
key_resp_10 = keyboard.Keyboard()
instrHeaderText_13 = visual.TextStim(win=win, name='instrHeaderText_13',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "mentRotTrial"
mentRotTrialClock = core.Clock()
mentRotStimulus = visual.ImageStim(
    win=win,
    name='mentRotStimulus', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.935, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
MROT_resp = keyboard.Keyboard()

# Initialize components for Routine "mentRotFeedback"
mentRotFeedbackClock = core.Clock()
msg = ' '
NBackfeedback_text_2 = visual.TextStim(win=win, name='NBackfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrNBACKbreak9"
instrNBACKbreak9Clock = core.Clock()
key_resp_9 = keyboard.Keyboard()
instrHeaderText_10 = visual.TextStim(win=win, name='instrHeaderText_10',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackFirst3Trials"
NBackFirst3TrialsClock = core.Clock()
Back2minus1=[]
Back2minus2=[]
Back2minus3=[]
NBackText_1 = visual.TextStim(win=win, name='NBackText_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NBackRemainderTrials"
NBackRemainderTrialsClock = core.Clock()
NBackText_2 = visual.TextStim(win=win, name='NBackText_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
NBack_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "NBackFeedback"
NBackFeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text_2 = visual.TextStim(win=win, name='AXCPTfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrSEARCHbreak10"
instrSEARCHbreak10Clock = core.Clock()
instrHeaderText_12 = visual.TextStim(win=win, name='instrHeaderText_12',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "searchTrial"
searchTrialClock = core.Clock()
orientList = [0, 90, 180, 270]
PosList = [[.45, -.45], [.45, -.15], [.45, .15], [.45, .45], [.15, -.45], [.15, -.15], [.15, .15], [.15, .45], [-.15, -.45], [-.15, -.15], [-.15, .15], [-.15, .45], [-.45, -.45], [-.45, -.15], [-.45, .15], [-.45, .45]]
key_resp_14 = keyboard.Keyboard()
targetStim = visual.TextStim(win=win, name='targetStim',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
searchStim2 = visual.TextStim(win=win, name='searchStim2',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
searchStim3 = visual.TextStim(win=win, name='searchStim3',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
searchStim4 = visual.TextStim(win=win, name='searchStim4',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
searchStim5 = visual.TextStim(win=win, name='searchStim5',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
searchStim6 = visual.TextStim(win=win, name='searchStim6',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
searchStim7 = visual.TextStim(win=win, name='searchStim7',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
searchStim8 = visual.TextStim(win=win, name='searchStim8',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
searchStim9 = visual.TextStim(win=win, name='searchStim9',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
searchStim10 = visual.TextStim(win=win, name='searchStim10',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
searchStim11 = visual.TextStim(win=win, name='searchStim11',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=1.0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "searchFeedback"
searchFeedbackClock = core.Clock()
msg = ' '
searchFeedbackText = visual.TextStim(win=win, name='searchFeedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrMENTROTbreak11"
instrMENTROTbreak11Clock = core.Clock()
key_resp_11 = keyboard.Keyboard()
instrHeaderText_14 = visual.TextStim(win=win, name='instrHeaderText_14',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "mentRotTrial"
mentRotTrialClock = core.Clock()
mentRotStimulus = visual.ImageStim(
    win=win,
    name='mentRotStimulus', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.935, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
MROT_resp = keyboard.Keyboard()

# Initialize components for Routine "mentRotFeedback"
mentRotFeedbackClock = core.Clock()
msg = ' '
NBackfeedback_text_2 = visual.TextStim(win=win, name='NBackfeedback_text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrAXCPTbreak12"
instrAXCPTbreak12Clock = core.Clock()
key_resp_7 = keyboard.Keyboard()
instrHeaderText_8 = visual.TextStim(win=win, name='instrHeaderText_8',
    text='Optional rest break',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text="Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "createLoopTimer"
createLoopTimerClock = core.Clock()

# Initialize components for Routine "timer"
timerClock = core.Clock()
probeVal = []
timer_text = visual.TextStim(win=win, name='timer_text',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "AXCPTtrial"
AXCPTtrialClock = core.Clock()
Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];


cue_text = visual.TextStim(win=win, name='cue_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break1 = visual.TextStim(win=win, name='break1',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-2.0);
distractor1 = visual.TextStim(win=win, name='distractor1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
break2 = visual.TextStim(win=win, name='break2',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-4.0);
distractor2 = visual.TextStim(win=win, name='distractor2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
break3 = visual.TextStim(win=win, name='break3',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "AXCPTprobe"
AXCPTprobeClock = core.Clock()
probe_text = visual.TextStim(win=win, name='probe_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AXCPT_resp = keyboard.Keyboard()

# Initialize components for Routine "AXCPTfeedback"
AXCPTfeedbackClock = core.Clock()
msg = ' '
AXCPTfeedback_text = visual.TextStim(win=win, name='AXCPTfeedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instrBRUMSpost"
instrBRUMSpostClock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='Thank you for completing the tasks\n\nOn the next few screens there are lists of words that describe feelings people have\n\nPlease read each one carefully. Then click the answer which best describes how you feel right now\n\nMake sure you answer every question\n\nPlease press the mouse to begin\n\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
BRUMSheader_2 = visual.TextStim(win=win, name='BRUMSheader_2',
    text='Rating Scale Instructions',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BRUMS_1"
BRUMS_1Clock = core.Clock()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
mouse_visibility_fix = visual.Polygon(
    win=win, name='mouse_visibility_fix',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
slider1 = visual.Slider(win=win, name='slider1',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider2 = visual.Slider(win=win, name='slider2',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider3 = visual.Slider(win=win, name='slider3',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider4 = visual.Slider(win=win, name='slider4',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider5 = visual.Slider(win=win, name='slider5',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider6 = visual.Slider(win=win, name='slider6',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider7 = visual.Slider(win=win, name='slider7',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider8 = visual.Slider(win=win, name='slider8',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Rating Scales: Page 1 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
panicky = visual.TextStim(win=win, name='panicky',
    text='Panicky',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
lively = visual.TextStim(win=win, name='lively',
    text='Lively',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
confused = visual.TextStim(win=win, name='confused',
    text='Confused',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
wornout = visual.TextStim(win=win, name='wornout',
    text='Worn Out',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
depressed = visual.TextStim(win=win, name='depressed',
    text='Depressed',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
downheartened = visual.TextStim(win=win, name='downheartened',
    text='Downheartened',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
annoyed = visual.TextStim(win=win, name='annoyed',
    text='Annoyed',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
exhausted = visual.TextStim(win=win, name='exhausted',
    text='Exhausted',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "BRUMS_2"
BRUMS_2Clock = core.Clock()
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
mouse_visibility_fix_2 = visual.Polygon(
    win=win, name='mouse_visibility_fix_2',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
slider9 = visual.Slider(win=win, name='slider9',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider10 = visual.Slider(win=win, name='slider10',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider11 = visual.Slider(win=win, name='slider11',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider12 = visual.Slider(win=win, name='slider12',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider13 = visual.Slider(win=win, name='slider13',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider14 = visual.Slider(win=win, name='slider14',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider15 = visual.Slider(win=win, name='slider15',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider16 = visual.Slider(win=win, name='slider16',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Rating Scales: Page 2 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
mixedup = visual.TextStim(win=win, name='mixedup',
    text='Mixed-up',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
sleepy = visual.TextStim(win=win, name='sleepy',
    text='Sleepy',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
bitter = visual.TextStim(win=win, name='bitter',
    text='Bitter',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
unhappy = visual.TextStim(win=win, name='unhappy',
    text='Unhappy',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
anxious = visual.TextStim(win=win, name='anxious',
    text='Anxious',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
worried = visual.TextStim(win=win, name='worried',
    text='Worried',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
energetic = visual.TextStim(win=win, name='energetic',
    text='Energetic',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
miserable = visual.TextStim(win=win, name='miserable',
    text='Miserable',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "BRUMS_3"
BRUMS_3Clock = core.Clock()
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
mouse_visibility_fix_3 = visual.Polygon(
    win=win, name='mouse_visibility_fix_3',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
slider17 = visual.Slider(win=win, name='slider17',
    size=(0.75, 0.1), pos=(0.1, 0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider18 = visual.Slider(win=win, name='slider18',
    size=(0.75, 0.1), pos=(0.1, 0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider19 = visual.Slider(win=win, name='slider19',
    size=(0.75, 0.1), pos=(0.1, 0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider20 = visual.Slider(win=win, name='slider20',
    size=(0.75, 0.1), pos=(0.1, 0.0), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider21 = visual.Slider(win=win, name='slider21',
    size=(0.75, 0.1), pos=(0.1, -0.2), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider22 = visual.Slider(win=win, name='slider22',
    size=(0.75, 0.1), pos=(0.1, -0.4), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider23 = visual.Slider(win=win, name='slider23',
    size=(0.75, 0.1), pos=(0.1, -0.6), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
slider24 = visual.Slider(win=win, name='slider24',
    size=(0.75, 0.1), pos=(0.1, -0.8), units=None,
    labels=("Not at all", "A little", "Moderately", "Quite a bit", "Extremely"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='White', font='Arial',
    flip=False)
text_11 = visual.TextStim(win=win, name='text_11',
    text='Rating Scales: Page 3 of 3\n\nDescribe how you feel right now\n',
    font='Arial',
    units='norm', pos=(0, 0.82), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
muddled = visual.TextStim(win=win, name='muddled',
    text='Muddled',
    font='Arial',
    pos=(-0.5, 0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
nervous = visual.TextStim(win=win, name='nervous',
    text='Nervous',
    font='Arial',
    pos=(-0.5, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
angry = visual.TextStim(win=win, name='angry',
    text='Angry',
    font='Arial',
    pos=(-0.5, 0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
active = visual.TextStim(win=win, name='active',
    text='Active',
    font='Arial',
    pos=(-0.5, 0.0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
tired = visual.TextStim(win=win, name='tired',
    text='Tired',
    font='Arial',
    pos=(-0.5, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
badtempered = visual.TextStim(win=win, name='badtempered',
    text='Bad tempered',
    font='Arial',
    pos=(-0.5, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
alert = visual.TextStim(win=win, name='alert',
    text='Alert',
    font='Arial',
    pos=(-0.5, -0.6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
uncertain = visual.TextStim(win=win, name='uncertain',
    text='Uncertain',
    font='Arial',
    pos=(-0.5, -0.8), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='End of Experiment\n\nThank you for taking part\n\nPlease email Ellie with your participant ID\n\nYou will then receive instructions about how to claim the compensation for your time\n\nPress the space bar to close the experiment',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_12 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
BRUMSheader.setAlignHoriz('center')

instrHeaderText_2.setAlignHoriz('center')
instrHeaderText_3.setAlignHoriz('center')
instrHeaderText_5.setAlignHoriz('center')
instrHeaderText_9.setAlignHoriz('center')
instrHeaderText_7.setAlignHoriz('center')
instrHeaderText_11.setAlignHoriz('center')
instrHeaderText_13.setAlignHoriz('center')
instrHeaderText_10.setAlignHoriz('center')
instrHeaderText_12.setAlignHoriz('center')
instrHeaderText_14.setAlignHoriz('center')
instrHeaderText_8.setAlignHoriz('center')

text_2.setAlignHoriz('center')
text_8.setAlignHoriz('center')
text_9.setAlignHoriz('center')
text_10.setAlignHoriz('center')
text_11.setAlignHoriz('center')
text_3.setAlignHoriz('center')
text_5.setAlignHoriz('center')
text_19.setAlignHoriz('center')
text_13.setAlignHoriz('center')
text_7.setAlignHoriz('center')
text_15.setAlignHoriz('center')
text_17.setAlignHoriz('center')
text_14.setAlignHoriz('center')
text_16.setAlignHoriz('center')
text_18.setAlignHoriz('center')
text_12.setAlignHoriz('center')
text_20.setAlignHoriz('center')

BRUMSheader_2.setAlignHoriz('center')
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [key_resp, instrHeaderText, text]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText* updates
    if instrHeaderText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText.frameNStart = frameN  # exact frame index
        instrHeaderText.tStart = t  # local t and not account for scr refresh
        instrHeaderText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText.started', instrHeaderText.tStartRefresh)
thisExp.addData('instrHeaderText.stopped', instrHeaderText.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "F_ISA"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_22
gotValidClick = False  # until a click is received
slider.reset()
# keep track of which components have finished
F_ISAComponents = [mouse_22, slider, text_4, mouse_visibility]
for thisComponent in F_ISAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
F_ISAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "F_ISA"-------
while continueRoutine:
    # get current time
    t = F_ISAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=F_ISAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider.getRating() > 0:
        continueRoutine = false
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
    # Check slider for response to end routine
    if slider.getRating() is not None and slider.status == STARTED:
        continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *mouse_visibility* updates
    if mouse_visibility.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility.frameNStart = frameN  # exact frame index
        mouse_visibility.tStart = t  # local t and not account for scr refresh
        mouse_visibility.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility.setAutoDraw(True)
    if mouse_visibility.status == STARTED:  # only update if drawing
        mouse_visibility.setPos((mouse_22.getPos()[0], mouse_22.getPos()[1]), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in F_ISAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "F_ISA"-------
for thisComponent in F_ISAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_22.started', mouse_22.tStart)
thisExp.addData('mouse_22.stopped', mouse_22.tStop)
thisExp.nextEntry()
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('F_ISA.duration', Timer.getTime())
thisExp.addData('mouse_visibility.started', mouse_visibility.tStartRefresh)
thisExp.addData('mouse_visibility.stopped', mouse_visibility.tStopRefresh)
# the Routine "F_ISA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instrBRUMSpre"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
gotValidClick = False  # until a click is received
# keep track of which components have finished
instrBRUMSpreComponents = [text_8, mouse_4, BRUMSheader]
for thisComponent in instrBRUMSpreComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrBRUMSpreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrBRUMSpre"-------
while continueRoutine:
    # get current time
    t = instrBRUMSpreClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrBRUMSpreClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *BRUMSheader* updates
    if BRUMSheader.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BRUMSheader.frameNStart = frameN  # exact frame index
        BRUMSheader.tStart = t  # local t and not account for scr refresh
        BRUMSheader.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BRUMSheader, 'tStartRefresh')  # time at next scr refresh
        BRUMSheader.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrBRUMSpreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrBRUMSpre"-------
for thisComponent in instrBRUMSpreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
thisExp.addData('BRUMSheader.started', BRUMSheader.tStartRefresh)
thisExp.addData('BRUMSheader.stopped', BRUMSheader.tStopRefresh)
# the Routine "instrBRUMSpre" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_1"-------
continueRoutine = True
# update component parameters for each repeat
BRUMSTimer = util.Clock()
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
slider1.reset()
slider2.reset()
slider3.reset()
slider4.reset()
slider5.reset()
slider6.reset()
slider7.reset()
slider8.reset()
# keep track of which components have finished
BRUMS_1Components = [mouse_3, mouse_visibility_fix, slider1, slider2, slider3, slider4, slider5, slider6, slider7, slider8, text_9, panicky, lively, confused, wornout, depressed, downheartened, annoyed, exhausted]
for thisComponent in BRUMS_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_1"-------
while continueRoutine:
    # get current time
    t = BRUMS_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider1.getRating() > 0 and slider2.getRating() > 0 and slider3.getRating() > 0 and slider4.getRating() > 0 and slider5.getRating() > 0 and slider6.getRating() > 0 and slider7.getRating() > 0 and slider8.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix* updates
    if mouse_visibility_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix.frameNStart = frameN  # exact frame index
        mouse_visibility_fix.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix.setAutoDraw(True)
    if mouse_visibility_fix.status == STARTED:  # only update if drawing
        mouse_visibility_fix.setPos((mouse_3.getPos()[0], mouse_3.getPos()[1]), log=False)
    
    # *slider1* updates
    if slider1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider1.frameNStart = frameN  # exact frame index
        slider1.tStart = t  # local t and not account for scr refresh
        slider1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider1, 'tStartRefresh')  # time at next scr refresh
        slider1.setAutoDraw(True)
    
    # *slider2* updates
    if slider2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider2.frameNStart = frameN  # exact frame index
        slider2.tStart = t  # local t and not account for scr refresh
        slider2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider2, 'tStartRefresh')  # time at next scr refresh
        slider2.setAutoDraw(True)
    
    # *slider3* updates
    if slider3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider3.frameNStart = frameN  # exact frame index
        slider3.tStart = t  # local t and not account for scr refresh
        slider3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider3, 'tStartRefresh')  # time at next scr refresh
        slider3.setAutoDraw(True)
    
    # *slider4* updates
    if slider4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider4.frameNStart = frameN  # exact frame index
        slider4.tStart = t  # local t and not account for scr refresh
        slider4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider4, 'tStartRefresh')  # time at next scr refresh
        slider4.setAutoDraw(True)
    
    # *slider5* updates
    if slider5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider5.frameNStart = frameN  # exact frame index
        slider5.tStart = t  # local t and not account for scr refresh
        slider5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider5, 'tStartRefresh')  # time at next scr refresh
        slider5.setAutoDraw(True)
    
    # *slider6* updates
    if slider6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider6.frameNStart = frameN  # exact frame index
        slider6.tStart = t  # local t and not account for scr refresh
        slider6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider6, 'tStartRefresh')  # time at next scr refresh
        slider6.setAutoDraw(True)
    
    # *slider7* updates
    if slider7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider7.frameNStart = frameN  # exact frame index
        slider7.tStart = t  # local t and not account for scr refresh
        slider7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider7, 'tStartRefresh')  # time at next scr refresh
        slider7.setAutoDraw(True)
    
    # *slider8* updates
    if slider8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider8.frameNStart = frameN  # exact frame index
        slider8.tStart = t  # local t and not account for scr refresh
        slider8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider8, 'tStartRefresh')  # time at next scr refresh
        slider8.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *panicky* updates
    if panicky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        panicky.frameNStart = frameN  # exact frame index
        panicky.tStart = t  # local t and not account for scr refresh
        panicky.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(panicky, 'tStartRefresh')  # time at next scr refresh
        panicky.setAutoDraw(True)
    
    # *lively* updates
    if lively.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lively.frameNStart = frameN  # exact frame index
        lively.tStart = t  # local t and not account for scr refresh
        lively.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lively, 'tStartRefresh')  # time at next scr refresh
        lively.setAutoDraw(True)
    
    # *confused* updates
    if confused.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confused.frameNStart = frameN  # exact frame index
        confused.tStart = t  # local t and not account for scr refresh
        confused.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confused, 'tStartRefresh')  # time at next scr refresh
        confused.setAutoDraw(True)
    
    # *wornout* updates
    if wornout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wornout.frameNStart = frameN  # exact frame index
        wornout.tStart = t  # local t and not account for scr refresh
        wornout.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wornout, 'tStartRefresh')  # time at next scr refresh
        wornout.setAutoDraw(True)
    
    # *depressed* updates
    if depressed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        depressed.frameNStart = frameN  # exact frame index
        depressed.tStart = t  # local t and not account for scr refresh
        depressed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(depressed, 'tStartRefresh')  # time at next scr refresh
        depressed.setAutoDraw(True)
    
    # *downheartened* updates
    if downheartened.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downheartened.frameNStart = frameN  # exact frame index
        downheartened.tStart = t  # local t and not account for scr refresh
        downheartened.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downheartened, 'tStartRefresh')  # time at next scr refresh
        downheartened.setAutoDraw(True)
    
    # *annoyed* updates
    if annoyed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        annoyed.frameNStart = frameN  # exact frame index
        annoyed.tStart = t  # local t and not account for scr refresh
        annoyed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(annoyed, 'tStartRefresh')  # time at next scr refresh
        annoyed.setAutoDraw(True)
    
    # *exhausted* updates
    if exhausted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exhausted.frameNStart = frameN  # exact frame index
        exhausted.tStart = t  # local t and not account for scr refresh
        exhausted.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exhausted, 'tStartRefresh')  # time at next scr refresh
        exhausted.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_1"-------
for thisComponent in BRUMS_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix.started', mouse_visibility_fix.tStartRefresh)
thisExp.addData('mouse_visibility_fix.stopped', mouse_visibility_fix.tStopRefresh)
thisExp.addData('slider1.response', slider1.getRating())
thisExp.addData('slider1.rt', slider1.getRT())
thisExp.addData('slider1.started', slider1.tStartRefresh)
thisExp.addData('slider1.stopped', slider1.tStopRefresh)
thisExp.addData('slider2.response', slider2.getRating())
thisExp.addData('slider2.rt', slider2.getRT())
thisExp.addData('slider2.started', slider2.tStartRefresh)
thisExp.addData('slider2.stopped', slider2.tStopRefresh)
thisExp.addData('slider3.response', slider3.getRating())
thisExp.addData('slider3.rt', slider3.getRT())
thisExp.addData('slider3.started', slider3.tStartRefresh)
thisExp.addData('slider3.stopped', slider3.tStopRefresh)
thisExp.addData('slider4.response', slider4.getRating())
thisExp.addData('slider4.rt', slider4.getRT())
thisExp.addData('slider4.started', slider4.tStartRefresh)
thisExp.addData('slider4.stopped', slider4.tStopRefresh)
thisExp.addData('slider5.response', slider5.getRating())
thisExp.addData('slider5.rt', slider5.getRT())
thisExp.addData('slider5.started', slider5.tStartRefresh)
thisExp.addData('slider5.stopped', slider5.tStopRefresh)
thisExp.addData('slider6.response', slider6.getRating())
thisExp.addData('slider6.rt', slider6.getRT())
thisExp.addData('slider6.started', slider6.tStartRefresh)
thisExp.addData('slider6.stopped', slider6.tStopRefresh)
thisExp.addData('slider7.response', slider7.getRating())
thisExp.addData('slider7.rt', slider7.getRT())
thisExp.addData('slider7.started', slider7.tStartRefresh)
thisExp.addData('slider7.stopped', slider7.tStopRefresh)
thisExp.addData('slider8.response', slider8.getRating())
thisExp.addData('slider8.rt', slider8.getRT())
thisExp.addData('slider8.started', slider8.tStartRefresh)
thisExp.addData('slider8.stopped', slider8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('panicky.started', panicky.tStartRefresh)
thisExp.addData('panicky.stopped', panicky.tStopRefresh)
thisExp.addData('lively.started', lively.tStartRefresh)
thisExp.addData('lively.stopped', lively.tStopRefresh)
thisExp.addData('confused.started', confused.tStartRefresh)
thisExp.addData('confused.stopped', confused.tStopRefresh)
thisExp.addData('wornout.started', wornout.tStartRefresh)
thisExp.addData('wornout.stopped', wornout.tStopRefresh)
thisExp.addData('depressed.started', depressed.tStartRefresh)
thisExp.addData('depressed.stopped', depressed.tStopRefresh)
thisExp.addData('downheartened.started', downheartened.tStartRefresh)
thisExp.addData('downheartened.stopped', downheartened.tStopRefresh)
thisExp.addData('annoyed.started', annoyed.tStartRefresh)
thisExp.addData('annoyed.stopped', annoyed.tStopRefresh)
thisExp.addData('exhausted.started', exhausted.tStartRefresh)
thisExp.addData('exhausted.stopped', exhausted.tStopRefresh)
# the Routine "BRUMS_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
gotValidClick = False  # until a click is received
slider9.reset()
slider10.reset()
slider11.reset()
slider12.reset()
slider13.reset()
slider14.reset()
slider15.reset()
slider16.reset()
# keep track of which components have finished
BRUMS_2Components = [mouse_5, mouse_visibility_fix_2, slider9, slider10, slider11, slider12, slider13, slider14, slider15, slider16, text_10, mixedup, sleepy, bitter, unhappy, anxious, worried, energetic, miserable]
for thisComponent in BRUMS_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_2"-------
while continueRoutine:
    # get current time
    t = BRUMS_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider9.getRating() > 0 and slider10.getRating() > 0 and slider11.getRating() > 0 and slider12.getRating() > 0 and slider13.getRating() > 0 and slider14.getRating() > 0 and slider15.getRating() > 0 and slider16.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix_2* updates
    if mouse_visibility_fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix_2.frameNStart = frameN  # exact frame index
        mouse_visibility_fix_2.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix_2, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix_2.setAutoDraw(True)
    if mouse_visibility_fix_2.status == STARTED:  # only update if drawing
        mouse_visibility_fix_2.setPos((mouse_5.getPos()[0], mouse_5.getPos()[1]), log=False)
    
    # *slider9* updates
    if slider9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider9.frameNStart = frameN  # exact frame index
        slider9.tStart = t  # local t and not account for scr refresh
        slider9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider9, 'tStartRefresh')  # time at next scr refresh
        slider9.setAutoDraw(True)
    
    # *slider10* updates
    if slider10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider10.frameNStart = frameN  # exact frame index
        slider10.tStart = t  # local t and not account for scr refresh
        slider10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider10, 'tStartRefresh')  # time at next scr refresh
        slider10.setAutoDraw(True)
    
    # *slider11* updates
    if slider11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider11.frameNStart = frameN  # exact frame index
        slider11.tStart = t  # local t and not account for scr refresh
        slider11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider11, 'tStartRefresh')  # time at next scr refresh
        slider11.setAutoDraw(True)
    
    # *slider12* updates
    if slider12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider12.frameNStart = frameN  # exact frame index
        slider12.tStart = t  # local t and not account for scr refresh
        slider12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider12, 'tStartRefresh')  # time at next scr refresh
        slider12.setAutoDraw(True)
    
    # *slider13* updates
    if slider13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider13.frameNStart = frameN  # exact frame index
        slider13.tStart = t  # local t and not account for scr refresh
        slider13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider13, 'tStartRefresh')  # time at next scr refresh
        slider13.setAutoDraw(True)
    
    # *slider14* updates
    if slider14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider14.frameNStart = frameN  # exact frame index
        slider14.tStart = t  # local t and not account for scr refresh
        slider14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider14, 'tStartRefresh')  # time at next scr refresh
        slider14.setAutoDraw(True)
    
    # *slider15* updates
    if slider15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider15.frameNStart = frameN  # exact frame index
        slider15.tStart = t  # local t and not account for scr refresh
        slider15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider15, 'tStartRefresh')  # time at next scr refresh
        slider15.setAutoDraw(True)
    
    # *slider16* updates
    if slider16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider16.frameNStart = frameN  # exact frame index
        slider16.tStart = t  # local t and not account for scr refresh
        slider16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider16, 'tStartRefresh')  # time at next scr refresh
        slider16.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *mixedup* updates
    if mixedup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mixedup.frameNStart = frameN  # exact frame index
        mixedup.tStart = t  # local t and not account for scr refresh
        mixedup.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mixedup, 'tStartRefresh')  # time at next scr refresh
        mixedup.setAutoDraw(True)
    
    # *sleepy* updates
    if sleepy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sleepy.frameNStart = frameN  # exact frame index
        sleepy.tStart = t  # local t and not account for scr refresh
        sleepy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sleepy, 'tStartRefresh')  # time at next scr refresh
        sleepy.setAutoDraw(True)
    
    # *bitter* updates
    if bitter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bitter.frameNStart = frameN  # exact frame index
        bitter.tStart = t  # local t and not account for scr refresh
        bitter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bitter, 'tStartRefresh')  # time at next scr refresh
        bitter.setAutoDraw(True)
    
    # *unhappy* updates
    if unhappy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unhappy.frameNStart = frameN  # exact frame index
        unhappy.tStart = t  # local t and not account for scr refresh
        unhappy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unhappy, 'tStartRefresh')  # time at next scr refresh
        unhappy.setAutoDraw(True)
    
    # *anxious* updates
    if anxious.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anxious.frameNStart = frameN  # exact frame index
        anxious.tStart = t  # local t and not account for scr refresh
        anxious.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anxious, 'tStartRefresh')  # time at next scr refresh
        anxious.setAutoDraw(True)
    
    # *worried* updates
    if worried.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        worried.frameNStart = frameN  # exact frame index
        worried.tStart = t  # local t and not account for scr refresh
        worried.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(worried, 'tStartRefresh')  # time at next scr refresh
        worried.setAutoDraw(True)
    
    # *energetic* updates
    if energetic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        energetic.frameNStart = frameN  # exact frame index
        energetic.tStart = t  # local t and not account for scr refresh
        energetic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(energetic, 'tStartRefresh')  # time at next scr refresh
        energetic.setAutoDraw(True)
    
    # *miserable* updates
    if miserable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        miserable.frameNStart = frameN  # exact frame index
        miserable.tStart = t  # local t and not account for scr refresh
        miserable.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(miserable, 'tStartRefresh')  # time at next scr refresh
        miserable.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_2"-------
for thisComponent in BRUMS_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix_2.started', mouse_visibility_fix_2.tStartRefresh)
thisExp.addData('mouse_visibility_fix_2.stopped', mouse_visibility_fix_2.tStopRefresh)
thisExp.addData('slider9.response', slider9.getRating())
thisExp.addData('slider9.rt', slider9.getRT())
thisExp.addData('slider9.started', slider9.tStartRefresh)
thisExp.addData('slider9.stopped', slider9.tStopRefresh)
thisExp.addData('slider10.response', slider10.getRating())
thisExp.addData('slider10.rt', slider10.getRT())
thisExp.addData('slider10.started', slider10.tStartRefresh)
thisExp.addData('slider10.stopped', slider10.tStopRefresh)
thisExp.addData('slider11.response', slider11.getRating())
thisExp.addData('slider11.rt', slider11.getRT())
thisExp.addData('slider11.started', slider11.tStartRefresh)
thisExp.addData('slider11.stopped', slider11.tStopRefresh)
thisExp.addData('slider12.response', slider12.getRating())
thisExp.addData('slider12.rt', slider12.getRT())
thisExp.addData('slider12.started', slider12.tStartRefresh)
thisExp.addData('slider12.stopped', slider12.tStopRefresh)
thisExp.addData('slider13.response', slider13.getRating())
thisExp.addData('slider13.rt', slider13.getRT())
thisExp.addData('slider13.started', slider13.tStartRefresh)
thisExp.addData('slider13.stopped', slider13.tStopRefresh)
thisExp.addData('slider14.response', slider14.getRating())
thisExp.addData('slider14.rt', slider14.getRT())
thisExp.addData('slider14.started', slider14.tStartRefresh)
thisExp.addData('slider14.stopped', slider14.tStopRefresh)
thisExp.addData('slider15.response', slider15.getRating())
thisExp.addData('slider15.rt', slider15.getRT())
thisExp.addData('slider15.started', slider15.tStartRefresh)
thisExp.addData('slider15.stopped', slider15.tStopRefresh)
thisExp.addData('slider16.response', slider16.getRating())
thisExp.addData('slider16.rt', slider16.getRT())
thisExp.addData('slider16.started', slider16.tStartRefresh)
thisExp.addData('slider16.stopped', slider16.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('mixedup.started', mixedup.tStartRefresh)
thisExp.addData('mixedup.stopped', mixedup.tStopRefresh)
thisExp.addData('sleepy.started', sleepy.tStartRefresh)
thisExp.addData('sleepy.stopped', sleepy.tStopRefresh)
thisExp.addData('bitter.started', bitter.tStartRefresh)
thisExp.addData('bitter.stopped', bitter.tStopRefresh)
thisExp.addData('unhappy.started', unhappy.tStartRefresh)
thisExp.addData('unhappy.stopped', unhappy.tStopRefresh)
thisExp.addData('anxious.started', anxious.tStartRefresh)
thisExp.addData('anxious.stopped', anxious.tStopRefresh)
thisExp.addData('worried.started', worried.tStartRefresh)
thisExp.addData('worried.stopped', worried.tStopRefresh)
thisExp.addData('energetic.started', energetic.tStartRefresh)
thisExp.addData('energetic.stopped', energetic.tStopRefresh)
thisExp.addData('miserable.started', miserable.tStartRefresh)
thisExp.addData('miserable.stopped', miserable.tStopRefresh)
# the Routine "BRUMS_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
gotValidClick = False  # until a click is received
slider17.reset()
slider18.reset()
slider19.reset()
slider20.reset()
slider21.reset()
slider22.reset()
slider23.reset()
slider24.reset()
# keep track of which components have finished
BRUMS_3Components = [mouse_6, mouse_visibility_fix_3, slider17, slider18, slider19, slider20, slider21, slider22, slider23, slider24, text_11, muddled, nervous, angry, active, tired, badtempered, alert, uncertain]
for thisComponent in BRUMS_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_3"-------
while continueRoutine:
    # get current time
    t = BRUMS_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider17.getRating() > 0 and slider18.getRating() > 0 and slider19.getRating() > 0 and slider20.getRating() > 0 and slider21.getRating() > 0 and slider22.getRating() > 0 and slider23.getRating() > 0 and slider24.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix_3* updates
    if mouse_visibility_fix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix_3.frameNStart = frameN  # exact frame index
        mouse_visibility_fix_3.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix_3, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix_3.setAutoDraw(True)
    if mouse_visibility_fix_3.status == STARTED:  # only update if drawing
        mouse_visibility_fix_3.setPos((mouse_6.getPos()[0], mouse_6.getPos()[1]), log=False)
    
    # *slider17* updates
    if slider17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider17.frameNStart = frameN  # exact frame index
        slider17.tStart = t  # local t and not account for scr refresh
        slider17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider17, 'tStartRefresh')  # time at next scr refresh
        slider17.setAutoDraw(True)
    
    # *slider18* updates
    if slider18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider18.frameNStart = frameN  # exact frame index
        slider18.tStart = t  # local t and not account for scr refresh
        slider18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider18, 'tStartRefresh')  # time at next scr refresh
        slider18.setAutoDraw(True)
    
    # *slider19* updates
    if slider19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider19.frameNStart = frameN  # exact frame index
        slider19.tStart = t  # local t and not account for scr refresh
        slider19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider19, 'tStartRefresh')  # time at next scr refresh
        slider19.setAutoDraw(True)
    
    # *slider20* updates
    if slider20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider20.frameNStart = frameN  # exact frame index
        slider20.tStart = t  # local t and not account for scr refresh
        slider20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider20, 'tStartRefresh')  # time at next scr refresh
        slider20.setAutoDraw(True)
    
    # *slider21* updates
    if slider21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider21.frameNStart = frameN  # exact frame index
        slider21.tStart = t  # local t and not account for scr refresh
        slider21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider21, 'tStartRefresh')  # time at next scr refresh
        slider21.setAutoDraw(True)
    
    # *slider22* updates
    if slider22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider22.frameNStart = frameN  # exact frame index
        slider22.tStart = t  # local t and not account for scr refresh
        slider22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider22, 'tStartRefresh')  # time at next scr refresh
        slider22.setAutoDraw(True)
    
    # *slider23* updates
    if slider23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider23.frameNStart = frameN  # exact frame index
        slider23.tStart = t  # local t and not account for scr refresh
        slider23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider23, 'tStartRefresh')  # time at next scr refresh
        slider23.setAutoDraw(True)
    
    # *slider24* updates
    if slider24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider24.frameNStart = frameN  # exact frame index
        slider24.tStart = t  # local t and not account for scr refresh
        slider24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider24, 'tStartRefresh')  # time at next scr refresh
        slider24.setAutoDraw(True)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *muddled* updates
    if muddled.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        muddled.frameNStart = frameN  # exact frame index
        muddled.tStart = t  # local t and not account for scr refresh
        muddled.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(muddled, 'tStartRefresh')  # time at next scr refresh
        muddled.setAutoDraw(True)
    
    # *nervous* updates
    if nervous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nervous.frameNStart = frameN  # exact frame index
        nervous.tStart = t  # local t and not account for scr refresh
        nervous.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nervous, 'tStartRefresh')  # time at next scr refresh
        nervous.setAutoDraw(True)
    
    # *angry* updates
    if angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        angry.frameNStart = frameN  # exact frame index
        angry.tStart = t  # local t and not account for scr refresh
        angry.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angry, 'tStartRefresh')  # time at next scr refresh
        angry.setAutoDraw(True)
    
    # *active* updates
    if active.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        active.frameNStart = frameN  # exact frame index
        active.tStart = t  # local t and not account for scr refresh
        active.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(active, 'tStartRefresh')  # time at next scr refresh
        active.setAutoDraw(True)
    
    # *tired* updates
    if tired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tired.frameNStart = frameN  # exact frame index
        tired.tStart = t  # local t and not account for scr refresh
        tired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tired, 'tStartRefresh')  # time at next scr refresh
        tired.setAutoDraw(True)
    
    # *badtempered* updates
    if badtempered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        badtempered.frameNStart = frameN  # exact frame index
        badtempered.tStart = t  # local t and not account for scr refresh
        badtempered.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(badtempered, 'tStartRefresh')  # time at next scr refresh
        badtempered.setAutoDraw(True)
    
    # *alert* updates
    if alert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        alert.frameNStart = frameN  # exact frame index
        alert.tStart = t  # local t and not account for scr refresh
        alert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alert, 'tStartRefresh')  # time at next scr refresh
        alert.setAutoDraw(True)
    
    # *uncertain* updates
    if uncertain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertain.frameNStart = frameN  # exact frame index
        uncertain.tStart = t  # local t and not account for scr refresh
        uncertain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertain, 'tStartRefresh')  # time at next scr refresh
        uncertain.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_3"-------
for thisComponent in BRUMS_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('BRUMS.duration', BRUMSTimer.getTime())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix_3.started', mouse_visibility_fix_3.tStartRefresh)
thisExp.addData('mouse_visibility_fix_3.stopped', mouse_visibility_fix_3.tStopRefresh)
thisExp.addData('slider17.response', slider17.getRating())
thisExp.addData('slider17.rt', slider17.getRT())
thisExp.addData('slider17.started', slider17.tStartRefresh)
thisExp.addData('slider17.stopped', slider17.tStopRefresh)
thisExp.addData('slider18.response', slider18.getRating())
thisExp.addData('slider18.rt', slider18.getRT())
thisExp.addData('slider18.started', slider18.tStartRefresh)
thisExp.addData('slider18.stopped', slider18.tStopRefresh)
thisExp.addData('slider19.response', slider19.getRating())
thisExp.addData('slider19.rt', slider19.getRT())
thisExp.addData('slider19.started', slider19.tStartRefresh)
thisExp.addData('slider19.stopped', slider19.tStopRefresh)
thisExp.addData('slider20.response', slider20.getRating())
thisExp.addData('slider20.rt', slider20.getRT())
thisExp.addData('slider20.started', slider20.tStartRefresh)
thisExp.addData('slider20.stopped', slider20.tStopRefresh)
thisExp.addData('slider21.response', slider21.getRating())
thisExp.addData('slider21.rt', slider21.getRT())
thisExp.addData('slider21.started', slider21.tStartRefresh)
thisExp.addData('slider21.stopped', slider21.tStopRefresh)
thisExp.addData('slider22.response', slider22.getRating())
thisExp.addData('slider22.rt', slider22.getRT())
thisExp.addData('slider22.started', slider22.tStartRefresh)
thisExp.addData('slider22.stopped', slider22.tStopRefresh)
thisExp.addData('slider23.response', slider23.getRating())
thisExp.addData('slider23.rt', slider23.getRT())
thisExp.addData('slider23.started', slider23.tStartRefresh)
thisExp.addData('slider23.stopped', slider23.tStopRefresh)
thisExp.addData('slider24.response', slider24.getRating())
thisExp.addData('slider24.rt', slider24.getRT())
thisExp.addData('slider24.started', slider24.tStartRefresh)
thisExp.addData('slider24.stopped', slider24.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('muddled.started', muddled.tStartRefresh)
thisExp.addData('muddled.stopped', muddled.tStopRefresh)
thisExp.addData('nervous.started', nervous.tStartRefresh)
thisExp.addData('nervous.stopped', nervous.tStopRefresh)
thisExp.addData('angry.started', angry.tStartRefresh)
thisExp.addData('angry.stopped', angry.tStopRefresh)
thisExp.addData('active.started', active.tStartRefresh)
thisExp.addData('active.stopped', active.tStopRefresh)
thisExp.addData('tired.started', tired.tStartRefresh)
thisExp.addData('tired.stopped', tired.tStopRefresh)
thisExp.addData('badtempered.started', badtempered.tStartRefresh)
thisExp.addData('badtempered.stopped', badtempered.tStopRefresh)
thisExp.addData('alert.started', alert.tStartRefresh)
thisExp.addData('alert.stopped', alert.tStopRefresh)
thisExp.addData('uncertain.started', uncertain.tStartRefresh)
thisExp.addData('uncertain.stopped', uncertain.tStopRefresh)
# the Routine "BRUMS_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instrAXCPTbreak1"-------
continueRoutine = True
# update component parameters for each repeat
instrAXCPTbreak1Timer = util.Clock()
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instrAXCPTbreak1Components = [key_resp_2, instrHeaderText_2, text_2]
for thisComponent in instrAXCPTbreak1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrAXCPTbreak1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrAXCPTbreak1"-------
while continueRoutine:
    # get current time
    t = instrAXCPTbreak1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrAXCPTbreak1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_2* updates
    if instrHeaderText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_2.frameNStart = frameN  # exact frame index
        instrHeaderText_2.tStart = t  # local t and not account for scr refresh
        instrHeaderText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_2, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_2.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrAXCPTbreak1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrAXCPTbreak1"-------
for thisComponent in instrAXCPTbreak1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break1.duration', instrAXCPTbreak1Timer.getTime())
instrAXCPTbreak1Timer = []
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_2.started', instrHeaderText_2.tStartRefresh)
thisExp.addData('instrHeaderText_2.stopped', instrHeaderText_2.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "instrAXCPTbreak1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AXCPTtrialsLoop1 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialType.csv'),
    seed=None, name='AXCPTtrialsLoop1')
thisExp.addLoop(AXCPTtrialsLoop1)  # add the loop to the experiment
thisAXCPTtrialsLoop1 = AXCPTtrialsLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop1.rgb)
if thisAXCPTtrialsLoop1 != None:
    for paramName in thisAXCPTtrialsLoop1:
        exec('{} = thisAXCPTtrialsLoop1[paramName]'.format(paramName))

for thisAXCPTtrialsLoop1 in AXCPTtrialsLoop1:
    currentLoop = AXCPTtrialsLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop1.rgb)
    if thisAXCPTtrialsLoop1 != None:
        for paramName in thisAXCPTtrialsLoop1:
            exec('{} = thisAXCPTtrialsLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    AXCPTtrialsLoop1.addData('timer_text.started', timer_text.tStartRefresh)
    AXCPTtrialsLoop1.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTtrial"-------
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    #function choice(arr) {
    #  return arr[Math.floor(Math.random() * arr.length)];
    #}
    
    distractor1Val = choice(distractors)
    distractor2Val = choice(distractors)
    
    
    
    if trialType == 'target':
        cueVal = 'A'
        probeVal = 'X'
    
    elif trialType == 'probeWrong':
        cueVal = 'A'
        probeVal = choice(Yletters)
    
    elif trialType == 'cueWrong':
        cueVal = choice(Bletters)
        probeVal = 'X'
    
    elif trialType == 'bothWrong':
        cueVal = choice(Bletters)
        probeVal = choice(Yletters)
    cue_text.setText(cueVal)
    distractor1.setText(distractor1Val)
    distractor2.setText(distractor2Val)
    # keep track of which components have finished
    AXCPTtrialComponents = [cue_text, break1, distractor1, break2, distractor2, break3]
    for thisComponent in AXCPTtrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTtrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTtrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTtrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTtrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_text* updates
        if cue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_text.frameNStart = frameN  # exact frame index
            cue_text.tStart = t  # local t and not account for scr refresh
            cue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_text, 'tStartRefresh')  # time at next scr refresh
            cue_text.setAutoDraw(True)
        if cue_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cue_text.tStop = t  # not accounting for scr refresh
                cue_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_text, 'tStopRefresh')  # time at next scr refresh
                cue_text.setAutoDraw(False)
        
        # *break1* updates
        if break1.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            break1.frameNStart = frameN  # exact frame index
            break1.tStart = t  # local t and not account for scr refresh
            break1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
            break1.setAutoDraw(True)
        if break1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break1.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break1.tStop = t  # not accounting for scr refresh
                break1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break1, 'tStopRefresh')  # time at next scr refresh
                break1.setAutoDraw(False)
        
        # *distractor1* updates
        if distractor1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            distractor1.frameNStart = frameN  # exact frame index
            distractor1.tStart = t  # local t and not account for scr refresh
            distractor1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor1, 'tStartRefresh')  # time at next scr refresh
            distractor1.setAutoDraw(True)
        if distractor1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.8-frameTolerance:
                # keep track of stop time/frame for later
                distractor1.tStop = t  # not accounting for scr refresh
                distractor1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor1, 'tStopRefresh')  # time at next scr refresh
                distractor1.setAutoDraw(False)
        
        # *break2* updates
        if break2.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
            # keep track of start time/frame for later
            break2.frameNStart = frameN  # exact frame index
            break2.tStart = t  # local t and not account for scr refresh
            break2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break2, 'tStartRefresh')  # time at next scr refresh
            break2.setAutoDraw(True)
        if break2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break2.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break2.tStop = t  # not accounting for scr refresh
                break2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break2, 'tStopRefresh')  # time at next scr refresh
                break2.setAutoDraw(False)
        
        # *distractor2* updates
        if distractor2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            distractor2.frameNStart = frameN  # exact frame index
            distractor2.tStart = t  # local t and not account for scr refresh
            distractor2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor2, 'tStartRefresh')  # time at next scr refresh
            distractor2.setAutoDraw(True)
        if distractor2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 3.3-frameTolerance:
                # keep track of stop time/frame for later
                distractor2.tStop = t  # not accounting for scr refresh
                distractor2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor2, 'tStopRefresh')  # time at next scr refresh
                distractor2.setAutoDraw(False)
        
        # *break3* updates
        if break3.status == NOT_STARTED and tThisFlip >= 3.3-frameTolerance:
            # keep track of start time/frame for later
            break3.frameNStart = frameN  # exact frame index
            break3.tStart = t  # local t and not account for scr refresh
            break3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break3, 'tStartRefresh')  # time at next scr refresh
            break3.setAutoDraw(True)
        if break3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break3.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break3.tStop = t  # not accounting for scr refresh
                break3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break3, 'tStopRefresh')  # time at next scr refresh
                break3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTtrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTtrial"-------
    for thisComponent in AXCPTtrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop1.addData('cue_text.started', cue_text.tStartRefresh)
    AXCPTtrialsLoop1.addData('cue_text.stopped', cue_text.tStopRefresh)
    AXCPTtrialsLoop1.addData('break1.started', break1.tStartRefresh)
    AXCPTtrialsLoop1.addData('break1.stopped', break1.tStopRefresh)
    AXCPTtrialsLoop1.addData('distractor1.started', distractor1.tStartRefresh)
    AXCPTtrialsLoop1.addData('distractor1.stopped', distractor1.tStopRefresh)
    AXCPTtrialsLoop1.addData('break2.started', break2.tStartRefresh)
    AXCPTtrialsLoop1.addData('break2.stopped', break2.tStopRefresh)
    AXCPTtrialsLoop1.addData('distractor2.started', distractor2.tStartRefresh)
    AXCPTtrialsLoop1.addData('distractor2.stopped', distractor2.tStopRefresh)
    AXCPTtrialsLoop1.addData('break3.started', break3.tStartRefresh)
    AXCPTtrialsLoop1.addData('break3.stopped', break3.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTprobe"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    probe_text.setText(probeVal)
    AXCPT_resp.keys = []
    AXCPT_resp.rt = []
    _AXCPT_resp_allKeys = []
    # keep track of which components have finished
    AXCPTprobeComponents = [probe_text, AXCPT_resp]
    for thisComponent in AXCPTprobeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTprobeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTprobe"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTprobeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTprobeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_text* updates
        if probe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_text.frameNStart = frameN  # exact frame index
            probe_text.tStart = t  # local t and not account for scr refresh
            probe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_text, 'tStartRefresh')  # time at next scr refresh
            probe_text.setAutoDraw(True)
        if probe_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                probe_text.tStop = t  # not accounting for scr refresh
                probe_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probe_text, 'tStopRefresh')  # time at next scr refresh
                probe_text.setAutoDraw(False)
        
        # *AXCPT_resp* updates
        waitOnFlip = False
        if AXCPT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPT_resp.frameNStart = frameN  # exact frame index
            AXCPT_resp.tStart = t  # local t and not account for scr refresh
            AXCPT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPT_resp, 'tStartRefresh')  # time at next scr refresh
            AXCPT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AXCPT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AXCPT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AXCPT_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.5-frameTolerance:
                # keep track of stop time/frame for later
                AXCPT_resp.tStop = t  # not accounting for scr refresh
                AXCPT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPT_resp, 'tStopRefresh')  # time at next scr refresh
                AXCPT_resp.status = FINISHED
        if AXCPT_resp.status == STARTED and not waitOnFlip:
            theseKeys = AXCPT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _AXCPT_resp_allKeys.extend(theseKeys)
            if len(_AXCPT_resp_allKeys):
                AXCPT_resp.keys = _AXCPT_resp_allKeys[-1].name  # just the last key pressed
                AXCPT_resp.rt = _AXCPT_resp_allKeys[-1].rt
                # was this correct?
                if (AXCPT_resp.keys == str(corrResponse)) or (AXCPT_resp.keys == corrResponse):
                    AXCPT_resp.corr = 1
                else:
                    AXCPT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTprobeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTprobe"-------
    for thisComponent in AXCPTprobeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop1.addData('probe_text.started', probe_text.tStartRefresh)
    AXCPTtrialsLoop1.addData('probe_text.stopped', probe_text.tStopRefresh)
    # check responses
    if AXCPT_resp.keys in ['', [], None]:  # No response was made
        AXCPT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           AXCPT_resp.corr = 1;  # correct non-response
        else:
           AXCPT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for AXCPTtrialsLoop1 (TrialHandler)
    AXCPTtrialsLoop1.addData('AXCPT_resp.keys',AXCPT_resp.keys)
    AXCPTtrialsLoop1.addData('AXCPT_resp.corr', AXCPT_resp.corr)
    if AXCPT_resp.keys != None:  # we had a response
        AXCPTtrialsLoop1.addData('AXCPT_resp.rt', AXCPT_resp.rt)
    AXCPTtrialsLoop1.addData('AXCPT_resp.started', AXCPT_resp.tStartRefresh)
    AXCPTtrialsLoop1.addData('AXCPT_resp.stopped', AXCPT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTfeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if AXCPT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text.setText(msg)
    # keep track of which components have finished
    AXCPTfeedbackComponents = [AXCPTfeedback_text]
    for thisComponent in AXCPTfeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTfeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTfeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTfeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text* updates
        if AXCPTfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text.setAutoDraw(True)
        if AXCPTfeedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTfeedback"-------
    for thisComponent in AXCPTfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop1.addData('AXCPTfeedback_text.started', AXCPTfeedback_text.tStartRefresh)
    AXCPTtrialsLoop1.addData('AXCPTfeedback_text.stopped', AXCPTfeedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'AXCPTtrialsLoop1'


# ------Prepare to start Routine "instrNBACKbreak2"-------
continueRoutine = True
# update component parameters for each repeat
instrNBACKbreak2Timer = util.Clock()
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
text_3.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrNBACKbreak2Components = [key_resp_3, instrHeaderText_3, text_3]
for thisComponent in instrNBACKbreak2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrNBACKbreak2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrNBACKbreak2"-------
while continueRoutine:
    # get current time
    t = instrNBACKbreak2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrNBACKbreak2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_3* updates
    if instrHeaderText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_3.frameNStart = frameN  # exact frame index
        instrHeaderText_3.tStart = t  # local t and not account for scr refresh
        instrHeaderText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_3, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_3.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrNBACKbreak2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrNBACKbreak2"-------
for thisComponent in instrNBACKbreak2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break2.duration', instrNBACKbreak2Timer.getTime())
instrNBACKbreak2Timer = []
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_3.started', instrHeaderText_3.tStartRefresh)
thisExp.addData('instrHeaderText_3.stopped', instrHeaderText_3.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "instrNBACKbreak2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBackTargetLoop1 = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='NBackTargetLoop1')
thisExp.addLoop(NBackTargetLoop1)  # add the loop to the experiment
thisNBackTargetLoop1 = NBackTargetLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLoop1.rgb)
if thisNBackTargetLoop1 != None:
    for paramName in thisNBackTargetLoop1:
        exec('{} = thisNBackTargetLoop1[paramName]'.format(paramName))

for thisNBackTargetLoop1 in NBackTargetLoop1:
    currentLoop = NBackTargetLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLoop1.rgb)
    if thisNBackTargetLoop1 != None:
        for paramName in thisNBackTargetLoop1:
            exec('{} = thisNBackTargetLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTargetLoop1.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTargetLoop1.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFirst3Trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    nletter=choice(letters)
    
    NBackText_1.setText(nletter)
    NBack_resp_1.keys = []
    NBack_resp_1.rt = []
    _NBack_resp_1_allKeys = []
    # keep track of which components have finished
    NBackFirst3TrialsComponents = [NBackText_1, NBack_resp_1]
    for thisComponent in NBackFirst3TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFirst3TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFirst3Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFirst3TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFirst3TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_1* updates
        if NBackText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_1.frameNStart = frameN  # exact frame index
            NBackText_1.tStart = t  # local t and not account for scr refresh
            NBackText_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_1, 'tStartRefresh')  # time at next scr refresh
            NBackText_1.setAutoDraw(True)
        if NBackText_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_1.tStop = t  # not accounting for scr refresh
                NBackText_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_1, 'tStopRefresh')  # time at next scr refresh
                NBackText_1.setAutoDraw(False)
        
        # *NBack_resp_1* updates
        waitOnFlip = False
        if NBack_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_1.frameNStart = frameN  # exact frame index
            NBack_resp_1.tStart = t  # local t and not account for scr refresh
            NBack_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_1, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_1.tStop = t  # not accounting for scr refresh
                NBack_resp_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_1, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_1.status = FINISHED
        if NBack_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_1.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_1_allKeys.extend(theseKeys)
            if len(_NBack_resp_1_allKeys):
                NBack_resp_1.keys = _NBack_resp_1_allKeys[-1].name  # just the last key pressed
                NBack_resp_1.rt = _NBack_resp_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFirst3TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFirst3Trials"-------
    for thisComponent in NBackFirst3TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTargetLoop1.addData('NBackText_1.started', NBackText_1.tStartRefresh)
    NBackTargetLoop1.addData('NBackText_1.stopped', NBackText_1.tStopRefresh)
    # check responses
    if NBack_resp_1.keys in ['', [], None]:  # No response was made
        NBack_resp_1.keys = None
    NBackTargetLoop1.addData('NBack_resp_1.keys',NBack_resp_1.keys)
    if NBack_resp_1.keys != None:  # we had a response
        NBackTargetLoop1.addData('NBack_resp_1.rt', NBack_resp_1.rt)
    NBackTargetLoop1.addData('NBack_resp_1.started', NBack_resp_1.tStartRefresh)
    NBackTargetLoop1.addData('NBack_resp_1.stopped', NBack_resp_1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'NBackTargetLoop1'


# set up handler to look after randomisation of conditions etc
NBackTrialsLoop1 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('2-back_loop.xlsx'),
    seed=None, name='NBackTrialsLoop1')
thisExp.addLoop(NBackTrialsLoop1)  # add the loop to the experiment
thisNBackTrialsLoop1 = NBackTrialsLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop1.rgb)
if thisNBackTrialsLoop1 != None:
    for paramName in thisNBackTrialsLoop1:
        exec('{} = thisNBackTrialsLoop1[paramName]'.format(paramName))

for thisNBackTrialsLoop1 in NBackTrialsLoop1:
    currentLoop = NBackTrialsLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop1.rgb)
    if thisNBackTrialsLoop1 != None:
        for paramName in thisNBackTrialsLoop1:
            exec('{} = thisNBackTrialsLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTrialsLoop1.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTrialsLoop1.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackRemainderTrials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if trialType=='nonTarget':
        letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        nletter=choice(letters)
        if nletter==Back2minus1:
                nletter=choice(letters)
        if nletter==Back2minus2:
                nletter=choice(letters)
    elif trialType=='target':
        nletter=Back2minus3
    NBackText_2.setText(nletter)
    NBack_resp_2.keys = []
    NBack_resp_2.rt = []
    _NBack_resp_2_allKeys = []
    # keep track of which components have finished
    NBackRemainderTrialsComponents = [NBackText_2, NBack_resp_2]
    for thisComponent in NBackRemainderTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackRemainderTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackRemainderTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackRemainderTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackRemainderTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_2* updates
        if NBackText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_2.frameNStart = frameN  # exact frame index
            NBackText_2.tStart = t  # local t and not account for scr refresh
            NBackText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_2, 'tStartRefresh')  # time at next scr refresh
            NBackText_2.setAutoDraw(True)
        if NBackText_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_2.tStop = t  # not accounting for scr refresh
                NBackText_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_2, 'tStopRefresh')  # time at next scr refresh
                NBackText_2.setAutoDraw(False)
        
        # *NBack_resp_2* updates
        waitOnFlip = False
        if NBack_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_2.frameNStart = frameN  # exact frame index
            NBack_resp_2.tStart = t  # local t and not account for scr refresh
            NBack_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_2, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_2.tStop = t  # not accounting for scr refresh
                NBack_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_2, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_2.status = FINISHED
        if NBack_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_2.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_2_allKeys.extend(theseKeys)
            if len(_NBack_resp_2_allKeys):
                NBack_resp_2.keys = _NBack_resp_2_allKeys[-1].name  # just the last key pressed
                NBack_resp_2.rt = _NBack_resp_2_allKeys[-1].rt
                # was this correct?
                if (NBack_resp_2.keys == str(corrResponse)) or (NBack_resp_2.keys == corrResponse):
                    NBack_resp_2.corr = 1
                else:
                    NBack_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackRemainderTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackRemainderTrials"-------
    for thisComponent in NBackRemainderTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTrialsLoop1.addData('NBackText_2.started', NBackText_2.tStartRefresh)
    NBackTrialsLoop1.addData('NBackText_2.stopped', NBackText_2.tStopRefresh)
    # check responses
    if NBack_resp_2.keys in ['', [], None]:  # No response was made
        NBack_resp_2.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           NBack_resp_2.corr = 1;  # correct non-response
        else:
           NBack_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for NBackTrialsLoop1 (TrialHandler)
    NBackTrialsLoop1.addData('NBack_resp_2.keys',NBack_resp_2.keys)
    NBackTrialsLoop1.addData('NBack_resp_2.corr', NBack_resp_2.corr)
    if NBack_resp_2.keys != None:  # we had a response
        NBackTrialsLoop1.addData('NBack_resp_2.rt', NBack_resp_2.rt)
    NBackTrialsLoop1.addData('NBack_resp_2.started', NBack_resp_2.tStartRefresh)
    NBackTrialsLoop1.addData('NBack_resp_2.stopped', NBack_resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if NBack_resp_2.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text_2.setText(msg)
    # keep track of which components have finished
    NBackFeedbackComponents = [AXCPTfeedback_text_2]
    for thisComponent in NBackFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text_2* updates
        if AXCPTfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text_2.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text_2.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text_2.setAutoDraw(True)
        if AXCPTfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text_2.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFeedback"-------
    for thisComponent in NBackFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NBackTrialsLoop1.addData('AXCPTfeedback_text_2.started', AXCPTfeedback_text_2.tStartRefresh)
    NBackTrialsLoop1.addData('AXCPTfeedback_text_2.stopped', AXCPTfeedback_text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'NBackTrialsLoop1'


# ------Prepare to start Routine "instrSEARCHbreak3"-------
continueRoutine = True
# update component parameters for each repeat
instrSEARCHbreak3Timer = util.Clock()
text_5.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin")
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instrSEARCHbreak3Components = [instrHeaderText_5, text_5, key_resp_4]
for thisComponent in instrSEARCHbreak3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrSEARCHbreak3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrSEARCHbreak3"-------
while continueRoutine:
    # get current time
    t = instrSEARCHbreak3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrSEARCHbreak3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrHeaderText_5* updates
    if instrHeaderText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_5.frameNStart = frameN  # exact frame index
        instrHeaderText_5.tStart = t  # local t and not account for scr refresh
        instrHeaderText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_5, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_5.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrSEARCHbreak3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrSEARCHbreak3"-------
for thisComponent in instrSEARCHbreak3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break3.duration', instrSEARCHbreak3Timer.getTime())
instrSEARCHbreak3Timer = []
thisExp.addData('instrHeaderText_5.started', instrHeaderText_5.tStartRefresh)
thisExp.addData('instrHeaderText_5.stopped', instrHeaderText_5.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrSEARCHbreak3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
searchLoop1 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('visualSearchConds.csv'),
    seed=None, name='searchLoop1')
thisExp.addLoop(searchLoop1)  # add the loop to the experiment
thisSearchLoop1 = searchLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSearchLoop1.rgb)
if thisSearchLoop1 != None:
    for paramName in thisSearchLoop1:
        exec('{} = thisSearchLoop1[paramName]'.format(paramName))

for thisSearchLoop1 in searchLoop1:
    currentLoop = searchLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisSearchLoop1.rgb)
    if thisSearchLoop1 != None:
        for paramName in thisSearchLoop1:
            exec('{} = thisSearchLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    searchLoop1.addData('timer_text.started', timer_text.tStartRefresh)
    searchLoop1.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "searchTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(PosList)
    
    targetOrient = choice(orientList)
    stim2Orient = choice (orientList)
    stim3Orient = choice(orientList)
    stim4Orient = choice(orientList)
    stim5Orient = choice(orientList)
    stim6Orient = choice(orientList)
    stim7Orient = choice(orientList)
    stim8Orient = choice(orientList)
    stim9Orient = choice(orientList)
    stim10Orient = choice(orientList)
    stim11Orient = choice(orientList)
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    targetStim.setPos(PosList[1])
    targetStim.setOri(targetOrient)
    targetStim.setText(targetLetter)
    searchStim2.setPos(PosList[2])
    searchStim2.setOri(stim2Orient)
    searchStim2.setText('L')
    searchStim3.setPos(PosList[3])
    searchStim3.setOri(stim3Orient)
    searchStim3.setText('L')
    searchStim4.setPos(PosList[4])
    searchStim4.setOri(stim4Orient)
    searchStim4.setText('L')
    searchStim5.setPos(PosList[5])
    searchStim5.setOri(stim5Orient)
    searchStim5.setText('L')
    searchStim6.setPos(PosList[6])
    searchStim6.setOri(stim6Orient)
    searchStim6.setText('L')
    searchStim7.setPos(PosList[7])
    searchStim7.setOri(stim7Orient)
    searchStim7.setText('L')
    searchStim8.setPos(PosList[8])
    searchStim8.setOri(stim8Orient)
    searchStim8.setText('L')
    searchStim9.setPos(PosList[9])
    searchStim9.setOri(stim9Orient)
    searchStim9.setText('L')
    searchStim10.setPos(PosList[10])
    searchStim10.setOri(stim10Orient)
    searchStim10.setText('L')
    searchStim11.setPos(PosList[11])
    searchStim11.setOri(stim11Orient)
    searchStim11.setText('L')
    # keep track of which components have finished
    searchTrialComponents = [key_resp_14, targetStim, searchStim2, searchStim3, searchStim4, searchStim5, searchStim6, searchStim7, searchStim8, searchStim9, searchStim10, searchStim11]
    for thisComponent in searchTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchTrial"-------
    while continueRoutine:
        # get current time
        t = searchTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['k', 'd'], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                # was this correct?
                if (key_resp_14.keys == str(corrResponse)) or (key_resp_14.keys == corrResponse):
                    key_resp_14.corr = 1
                else:
                    key_resp_14.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *targetStim* updates
        if targetStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetStim.frameNStart = frameN  # exact frame index
            targetStim.tStart = t  # local t and not account for scr refresh
            targetStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetStim, 'tStartRefresh')  # time at next scr refresh
            targetStim.setAutoDraw(True)
        
        # *searchStim2* updates
        if searchStim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim2.frameNStart = frameN  # exact frame index
            searchStim2.tStart = t  # local t and not account for scr refresh
            searchStim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim2, 'tStartRefresh')  # time at next scr refresh
            searchStim2.setAutoDraw(True)
        
        # *searchStim3* updates
        if searchStim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim3.frameNStart = frameN  # exact frame index
            searchStim3.tStart = t  # local t and not account for scr refresh
            searchStim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim3, 'tStartRefresh')  # time at next scr refresh
            searchStim3.setAutoDraw(True)
        
        # *searchStim4* updates
        if searchStim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim4.frameNStart = frameN  # exact frame index
            searchStim4.tStart = t  # local t and not account for scr refresh
            searchStim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim4, 'tStartRefresh')  # time at next scr refresh
            searchStim4.setAutoDraw(True)
        
        # *searchStim5* updates
        if searchStim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim5.frameNStart = frameN  # exact frame index
            searchStim5.tStart = t  # local t and not account for scr refresh
            searchStim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim5, 'tStartRefresh')  # time at next scr refresh
            searchStim5.setAutoDraw(True)
        
        # *searchStim6* updates
        if searchStim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim6.frameNStart = frameN  # exact frame index
            searchStim6.tStart = t  # local t and not account for scr refresh
            searchStim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim6, 'tStartRefresh')  # time at next scr refresh
            searchStim6.setAutoDraw(True)
        
        # *searchStim7* updates
        if searchStim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim7.frameNStart = frameN  # exact frame index
            searchStim7.tStart = t  # local t and not account for scr refresh
            searchStim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim7, 'tStartRefresh')  # time at next scr refresh
            searchStim7.setAutoDraw(True)
        
        # *searchStim8* updates
        if searchStim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim8.frameNStart = frameN  # exact frame index
            searchStim8.tStart = t  # local t and not account for scr refresh
            searchStim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim8, 'tStartRefresh')  # time at next scr refresh
            searchStim8.setAutoDraw(True)
        
        # *searchStim9* updates
        if searchStim9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim9.frameNStart = frameN  # exact frame index
            searchStim9.tStart = t  # local t and not account for scr refresh
            searchStim9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim9, 'tStartRefresh')  # time at next scr refresh
            searchStim9.setAutoDraw(True)
        
        # *searchStim10* updates
        if searchStim10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim10.frameNStart = frameN  # exact frame index
            searchStim10.tStart = t  # local t and not account for scr refresh
            searchStim10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim10, 'tStartRefresh')  # time at next scr refresh
            searchStim10.setAutoDraw(True)
        
        # *searchStim11* updates
        if searchStim11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim11.frameNStart = frameN  # exact frame index
            searchStim11.tStart = t  # local t and not account for scr refresh
            searchStim11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim11, 'tStartRefresh')  # time at next scr refresh
            searchStim11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchTrial"-------
    for thisComponent in searchTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           key_resp_14.corr = 1;  # correct non-response
        else:
           key_resp_14.corr = 0;  # failed to respond (incorrectly)
    # store data for searchLoop1 (TrialHandler)
    searchLoop1.addData('key_resp_14.keys',key_resp_14.keys)
    searchLoop1.addData('key_resp_14.corr', key_resp_14.corr)
    if key_resp_14.keys != None:  # we had a response
        searchLoop1.addData('key_resp_14.rt', key_resp_14.rt)
    searchLoop1.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    searchLoop1.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    searchLoop1.addData('targetStim.started', targetStim.tStartRefresh)
    searchLoop1.addData('targetStim.stopped', targetStim.tStopRefresh)
    # the Routine "searchTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "searchFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp_14.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    searchFeedbackText.setText(msg)
    # keep track of which components have finished
    searchFeedbackComponents = [searchFeedbackText]
    for thisComponent in searchFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *searchFeedbackText* updates
        if searchFeedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchFeedbackText.frameNStart = frameN  # exact frame index
            searchFeedbackText.tStart = t  # local t and not account for scr refresh
            searchFeedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchFeedbackText, 'tStartRefresh')  # time at next scr refresh
            searchFeedbackText.setAutoDraw(True)
        if searchFeedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > searchFeedbackText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                searchFeedbackText.tStop = t  # not accounting for scr refresh
                searchFeedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(searchFeedbackText, 'tStopRefresh')  # time at next scr refresh
                searchFeedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchFeedback"-------
    for thisComponent in searchFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    searchLoop1.addData('searchFeedbackText.started', searchFeedbackText.tStartRefresh)
    searchLoop1.addData('searchFeedbackText.stopped', searchFeedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'searchLoop1'


# ------Prepare to start Routine "instrMENTROTbreak4"-------
continueRoutine = True
# update component parameters for each repeat
instrMENTROTbreak4Timer = util.Clock()
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
text_21.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrMENTROTbreak4Components = [key_resp_13, instrHeaderText_15, text_21]
for thisComponent in instrMENTROTbreak4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrMENTROTbreak4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrMENTROTbreak4"-------
while continueRoutine:
    # get current time
    t = instrMENTROTbreak4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrMENTROTbreak4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_15* updates
    if instrHeaderText_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_15.frameNStart = frameN  # exact frame index
        instrHeaderText_15.tStart = t  # local t and not account for scr refresh
        instrHeaderText_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_15, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_15.setAutoDraw(True)
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrMENTROTbreak4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrMENTROTbreak4"-------
for thisComponent in instrMENTROTbreak4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break4.duration', instrMENTROTbreak4Timer.getTime())
instrMENTROTbreak4Timer = []
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_15.started', instrHeaderText_15.tStartRefresh)
thisExp.addData('instrHeaderText_15.stopped', instrHeaderText_15.tStopRefresh)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)
# the Routine "instrMENTROTbreak4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mentRotTrialsLoop1 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('response.csv'),
    seed=None, name='mentRotTrialsLoop1')
thisExp.addLoop(mentRotTrialsLoop1)  # add the loop to the experiment
thisMentRotTrialsLoop1 = mentRotTrialsLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop1.rgb)
if thisMentRotTrialsLoop1 != None:
    for paramName in thisMentRotTrialsLoop1:
        exec('{} = thisMentRotTrialsLoop1[paramName]'.format(paramName))

for thisMentRotTrialsLoop1 in mentRotTrialsLoop1:
    currentLoop = mentRotTrialsLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop1.rgb)
    if thisMentRotTrialsLoop1 != None:
        for paramName in thisMentRotTrialsLoop1:
            exec('{} = thisMentRotTrialsLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    mentRotTrialsLoop1.addData('timer_text.started', timer_text.tStartRefresh)
    mentRotTrialsLoop1.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "mentRotTrial"-------
    continueRoutine = True
    routineTimer.add(7.500000)
    # update component parameters for each repeat
    mentRotStimulus.setImage(imagefile)
    MROT_resp.keys = []
    MROT_resp.rt = []
    _MROT_resp_allKeys = []
    # keep track of which components have finished
    mentRotTrialComponents = [mentRotStimulus, MROT_resp]
    for thisComponent in mentRotTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mentRotStimulus* updates
        if mentRotStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mentRotStimulus.frameNStart = frameN  # exact frame index
            mentRotStimulus.tStart = t  # local t and not account for scr refresh
            mentRotStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mentRotStimulus, 'tStartRefresh')  # time at next scr refresh
            mentRotStimulus.setAutoDraw(True)
        if mentRotStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mentRotStimulus.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                mentRotStimulus.tStop = t  # not accounting for scr refresh
                mentRotStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mentRotStimulus, 'tStopRefresh')  # time at next scr refresh
                mentRotStimulus.setAutoDraw(False)
        
        # *MROT_resp* updates
        waitOnFlip = False
        if MROT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MROT_resp.frameNStart = frameN  # exact frame index
            MROT_resp.tStart = t  # local t and not account for scr refresh
            MROT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MROT_resp, 'tStartRefresh')  # time at next scr refresh
            MROT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MROT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MROT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MROT_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MROT_resp.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                MROT_resp.tStop = t  # not accounting for scr refresh
                MROT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MROT_resp, 'tStopRefresh')  # time at next scr refresh
                MROT_resp.status = FINISHED
        if MROT_resp.status == STARTED and not waitOnFlip:
            theseKeys = MROT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _MROT_resp_allKeys.extend(theseKeys)
            if len(_MROT_resp_allKeys):
                MROT_resp.keys = _MROT_resp_allKeys[-1].name  # just the last key pressed
                MROT_resp.rt = _MROT_resp_allKeys[-1].rt
                # was this correct?
                if (MROT_resp.keys == str(corrResponse)) or (MROT_resp.keys == corrResponse):
                    MROT_resp.corr = 1
                else:
                    MROT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotTrial"-------
    for thisComponent in mentRotTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop1.addData('mentRotStimulus.started', mentRotStimulus.tStartRefresh)
    mentRotTrialsLoop1.addData('mentRotStimulus.stopped', mentRotStimulus.tStopRefresh)
    # check responses
    if MROT_resp.keys in ['', [], None]:  # No response was made
        MROT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           MROT_resp.corr = 1;  # correct non-response
        else:
           MROT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for mentRotTrialsLoop1 (TrialHandler)
    mentRotTrialsLoop1.addData('MROT_resp.keys',MROT_resp.keys)
    mentRotTrialsLoop1.addData('MROT_resp.corr', MROT_resp.corr)
    if MROT_resp.keys != None:  # we had a response
        mentRotTrialsLoop1.addData('MROT_resp.rt', MROT_resp.rt)
    mentRotTrialsLoop1.addData('MROT_resp.started', MROT_resp.tStartRefresh)
    mentRotTrialsLoop1.addData('MROT_resp.stopped', MROT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "mentRotFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if MROT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    NBackfeedback_text_2.setText(msg)
    # keep track of which components have finished
    mentRotFeedbackComponents = [NBackfeedback_text_2]
    for thisComponent in mentRotFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackfeedback_text_2* updates
        if NBackfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackfeedback_text_2.frameNStart = frameN  # exact frame index
            NBackfeedback_text_2.tStart = t  # local t and not account for scr refresh
            NBackfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            NBackfeedback_text_2.setAutoDraw(True)
        if NBackfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NBackfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                NBackfeedback_text_2.tStop = t  # not accounting for scr refresh
                NBackfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                NBackfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotFeedback"-------
    for thisComponent in mentRotFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop1.addData('NBackfeedback_text_2.started', NBackfeedback_text_2.tStartRefresh)
    mentRotTrialsLoop1.addData('NBackfeedback_text_2.stopped', NBackfeedback_text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'mentRotTrialsLoop1'


# ------Prepare to start Routine "instrNBACKbreak5"-------
continueRoutine = True
# update component parameters for each repeat
instrNBACKbreak5Timer = util.Clock()
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
text_13.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrNBACKbreak5Components = [key_resp_8, instrHeaderText_9, text_13]
for thisComponent in instrNBACKbreak5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrNBACKbreak5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrNBACKbreak5"-------
while continueRoutine:
    # get current time
    t = instrNBACKbreak5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrNBACKbreak5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_9* updates
    if instrHeaderText_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_9.frameNStart = frameN  # exact frame index
        instrHeaderText_9.tStart = t  # local t and not account for scr refresh
        instrHeaderText_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_9, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_9.setAutoDraw(True)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrNBACKbreak5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrNBACKbreak5"-------
for thisComponent in instrNBACKbreak5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break5.duration', instrNBACKbreak5Timer.getTime())
instrNBACKbreak5Timer = []
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_9.started', instrHeaderText_9.tStartRefresh)
thisExp.addData('instrHeaderText_9.stopped', instrHeaderText_9.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# the Routine "instrNBACKbreak5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBackTargetLOOP2 = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='NBackTargetLOOP2')
thisExp.addLoop(NBackTargetLOOP2)  # add the loop to the experiment
thisNBackTargetLOOP2 = NBackTargetLOOP2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLOOP2.rgb)
if thisNBackTargetLOOP2 != None:
    for paramName in thisNBackTargetLOOP2:
        exec('{} = thisNBackTargetLOOP2[paramName]'.format(paramName))

for thisNBackTargetLOOP2 in NBackTargetLOOP2:
    currentLoop = NBackTargetLOOP2
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLOOP2.rgb)
    if thisNBackTargetLOOP2 != None:
        for paramName in thisNBackTargetLOOP2:
            exec('{} = thisNBackTargetLOOP2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTargetLOOP2.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTargetLOOP2.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFirst3Trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    nletter=choice(letters)
    
    NBackText_1.setText(nletter)
    NBack_resp_1.keys = []
    NBack_resp_1.rt = []
    _NBack_resp_1_allKeys = []
    # keep track of which components have finished
    NBackFirst3TrialsComponents = [NBackText_1, NBack_resp_1]
    for thisComponent in NBackFirst3TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFirst3TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFirst3Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFirst3TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFirst3TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_1* updates
        if NBackText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_1.frameNStart = frameN  # exact frame index
            NBackText_1.tStart = t  # local t and not account for scr refresh
            NBackText_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_1, 'tStartRefresh')  # time at next scr refresh
            NBackText_1.setAutoDraw(True)
        if NBackText_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_1.tStop = t  # not accounting for scr refresh
                NBackText_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_1, 'tStopRefresh')  # time at next scr refresh
                NBackText_1.setAutoDraw(False)
        
        # *NBack_resp_1* updates
        waitOnFlip = False
        if NBack_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_1.frameNStart = frameN  # exact frame index
            NBack_resp_1.tStart = t  # local t and not account for scr refresh
            NBack_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_1, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_1.tStop = t  # not accounting for scr refresh
                NBack_resp_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_1, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_1.status = FINISHED
        if NBack_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_1.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_1_allKeys.extend(theseKeys)
            if len(_NBack_resp_1_allKeys):
                NBack_resp_1.keys = _NBack_resp_1_allKeys[-1].name  # just the last key pressed
                NBack_resp_1.rt = _NBack_resp_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFirst3TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFirst3Trials"-------
    for thisComponent in NBackFirst3TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTargetLOOP2.addData('NBackText_1.started', NBackText_1.tStartRefresh)
    NBackTargetLOOP2.addData('NBackText_1.stopped', NBackText_1.tStopRefresh)
    # check responses
    if NBack_resp_1.keys in ['', [], None]:  # No response was made
        NBack_resp_1.keys = None
    NBackTargetLOOP2.addData('NBack_resp_1.keys',NBack_resp_1.keys)
    if NBack_resp_1.keys != None:  # we had a response
        NBackTargetLOOP2.addData('NBack_resp_1.rt', NBack_resp_1.rt)
    NBackTargetLOOP2.addData('NBack_resp_1.started', NBack_resp_1.tStartRefresh)
    NBackTargetLOOP2.addData('NBack_resp_1.stopped', NBack_resp_1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'NBackTargetLOOP2'


# set up handler to look after randomisation of conditions etc
NBackTrialsLoop2 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('2-back_loop.xlsx'),
    seed=None, name='NBackTrialsLoop2')
thisExp.addLoop(NBackTrialsLoop2)  # add the loop to the experiment
thisNBackTrialsLoop2 = NBackTrialsLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop2.rgb)
if thisNBackTrialsLoop2 != None:
    for paramName in thisNBackTrialsLoop2:
        exec('{} = thisNBackTrialsLoop2[paramName]'.format(paramName))

for thisNBackTrialsLoop2 in NBackTrialsLoop2:
    currentLoop = NBackTrialsLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop2.rgb)
    if thisNBackTrialsLoop2 != None:
        for paramName in thisNBackTrialsLoop2:
            exec('{} = thisNBackTrialsLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTrialsLoop2.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTrialsLoop2.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackRemainderTrials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if trialType=='nonTarget':
        letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        nletter=choice(letters)
        if nletter==Back2minus1:
                nletter=choice(letters)
        if nletter==Back2minus2:
                nletter=choice(letters)
    elif trialType=='target':
        nletter=Back2minus3
    NBackText_2.setText(nletter)
    NBack_resp_2.keys = []
    NBack_resp_2.rt = []
    _NBack_resp_2_allKeys = []
    # keep track of which components have finished
    NBackRemainderTrialsComponents = [NBackText_2, NBack_resp_2]
    for thisComponent in NBackRemainderTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackRemainderTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackRemainderTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackRemainderTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackRemainderTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_2* updates
        if NBackText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_2.frameNStart = frameN  # exact frame index
            NBackText_2.tStart = t  # local t and not account for scr refresh
            NBackText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_2, 'tStartRefresh')  # time at next scr refresh
            NBackText_2.setAutoDraw(True)
        if NBackText_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_2.tStop = t  # not accounting for scr refresh
                NBackText_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_2, 'tStopRefresh')  # time at next scr refresh
                NBackText_2.setAutoDraw(False)
        
        # *NBack_resp_2* updates
        waitOnFlip = False
        if NBack_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_2.frameNStart = frameN  # exact frame index
            NBack_resp_2.tStart = t  # local t and not account for scr refresh
            NBack_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_2, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_2.tStop = t  # not accounting for scr refresh
                NBack_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_2, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_2.status = FINISHED
        if NBack_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_2.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_2_allKeys.extend(theseKeys)
            if len(_NBack_resp_2_allKeys):
                NBack_resp_2.keys = _NBack_resp_2_allKeys[-1].name  # just the last key pressed
                NBack_resp_2.rt = _NBack_resp_2_allKeys[-1].rt
                # was this correct?
                if (NBack_resp_2.keys == str(corrResponse)) or (NBack_resp_2.keys == corrResponse):
                    NBack_resp_2.corr = 1
                else:
                    NBack_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackRemainderTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackRemainderTrials"-------
    for thisComponent in NBackRemainderTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTrialsLoop2.addData('NBackText_2.started', NBackText_2.tStartRefresh)
    NBackTrialsLoop2.addData('NBackText_2.stopped', NBackText_2.tStopRefresh)
    # check responses
    if NBack_resp_2.keys in ['', [], None]:  # No response was made
        NBack_resp_2.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           NBack_resp_2.corr = 1;  # correct non-response
        else:
           NBack_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for NBackTrialsLoop2 (TrialHandler)
    NBackTrialsLoop2.addData('NBack_resp_2.keys',NBack_resp_2.keys)
    NBackTrialsLoop2.addData('NBack_resp_2.corr', NBack_resp_2.corr)
    if NBack_resp_2.keys != None:  # we had a response
        NBackTrialsLoop2.addData('NBack_resp_2.rt', NBack_resp_2.rt)
    NBackTrialsLoop2.addData('NBack_resp_2.started', NBack_resp_2.tStartRefresh)
    NBackTrialsLoop2.addData('NBack_resp_2.stopped', NBack_resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if NBack_resp_2.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text_2.setText(msg)
    # keep track of which components have finished
    NBackFeedbackComponents = [AXCPTfeedback_text_2]
    for thisComponent in NBackFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text_2* updates
        if AXCPTfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text_2.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text_2.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text_2.setAutoDraw(True)
        if AXCPTfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text_2.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFeedback"-------
    for thisComponent in NBackFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NBackTrialsLoop2.addData('AXCPTfeedback_text_2.started', AXCPTfeedback_text_2.tStartRefresh)
    NBackTrialsLoop2.addData('AXCPTfeedback_text_2.stopped', AXCPTfeedback_text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'NBackTrialsLoop2'


# ------Prepare to start Routine "instrAXCPTbreak6"-------
continueRoutine = True
# update component parameters for each repeat
instrAXCPTbreak6Timer = util.Clock()
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instrAXCPTbreak6Components = [key_resp_6, instrHeaderText_7, text_7]
for thisComponent in instrAXCPTbreak6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrAXCPTbreak6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrAXCPTbreak6"-------
while continueRoutine:
    # get current time
    t = instrAXCPTbreak6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrAXCPTbreak6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_7* updates
    if instrHeaderText_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_7.frameNStart = frameN  # exact frame index
        instrHeaderText_7.tStart = t  # local t and not account for scr refresh
        instrHeaderText_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_7, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_7.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrAXCPTbreak6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrAXCPTbreak6"-------
for thisComponent in instrAXCPTbreak6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break6.duration', instrAXCPTbreak6Timer.getTime())
instrAXCPTbreak6Timer = []
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_7.started', instrHeaderText_7.tStartRefresh)
thisExp.addData('instrHeaderText_7.stopped', instrHeaderText_7.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "instrAXCPTbreak6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AXCPTtrialsLoop2 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialType.csv'),
    seed=None, name='AXCPTtrialsLoop2')
thisExp.addLoop(AXCPTtrialsLoop2)  # add the loop to the experiment
thisAXCPTtrialsLoop2 = AXCPTtrialsLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop2.rgb)
if thisAXCPTtrialsLoop2 != None:
    for paramName in thisAXCPTtrialsLoop2:
        exec('{} = thisAXCPTtrialsLoop2[paramName]'.format(paramName))

for thisAXCPTtrialsLoop2 in AXCPTtrialsLoop2:
    currentLoop = AXCPTtrialsLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop2.rgb)
    if thisAXCPTtrialsLoop2 != None:
        for paramName in thisAXCPTtrialsLoop2:
            exec('{} = thisAXCPTtrialsLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    AXCPTtrialsLoop2.addData('timer_text.started', timer_text.tStartRefresh)
    AXCPTtrialsLoop2.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTtrial"-------
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    #function choice(arr) {
    #  return arr[Math.floor(Math.random() * arr.length)];
    #}
    
    distractor1Val = choice(distractors)
    distractor2Val = choice(distractors)
    
    
    
    if trialType == 'target':
        cueVal = 'A'
        probeVal = 'X'
    
    elif trialType == 'probeWrong':
        cueVal = 'A'
        probeVal = choice(Yletters)
    
    elif trialType == 'cueWrong':
        cueVal = choice(Bletters)
        probeVal = 'X'
    
    elif trialType == 'bothWrong':
        cueVal = choice(Bletters)
        probeVal = choice(Yletters)
    cue_text.setText(cueVal)
    distractor1.setText(distractor1Val)
    distractor2.setText(distractor2Val)
    # keep track of which components have finished
    AXCPTtrialComponents = [cue_text, break1, distractor1, break2, distractor2, break3]
    for thisComponent in AXCPTtrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTtrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTtrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTtrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTtrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_text* updates
        if cue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_text.frameNStart = frameN  # exact frame index
            cue_text.tStart = t  # local t and not account for scr refresh
            cue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_text, 'tStartRefresh')  # time at next scr refresh
            cue_text.setAutoDraw(True)
        if cue_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cue_text.tStop = t  # not accounting for scr refresh
                cue_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_text, 'tStopRefresh')  # time at next scr refresh
                cue_text.setAutoDraw(False)
        
        # *break1* updates
        if break1.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            break1.frameNStart = frameN  # exact frame index
            break1.tStart = t  # local t and not account for scr refresh
            break1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
            break1.setAutoDraw(True)
        if break1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break1.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break1.tStop = t  # not accounting for scr refresh
                break1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break1, 'tStopRefresh')  # time at next scr refresh
                break1.setAutoDraw(False)
        
        # *distractor1* updates
        if distractor1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            distractor1.frameNStart = frameN  # exact frame index
            distractor1.tStart = t  # local t and not account for scr refresh
            distractor1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor1, 'tStartRefresh')  # time at next scr refresh
            distractor1.setAutoDraw(True)
        if distractor1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.8-frameTolerance:
                # keep track of stop time/frame for later
                distractor1.tStop = t  # not accounting for scr refresh
                distractor1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor1, 'tStopRefresh')  # time at next scr refresh
                distractor1.setAutoDraw(False)
        
        # *break2* updates
        if break2.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
            # keep track of start time/frame for later
            break2.frameNStart = frameN  # exact frame index
            break2.tStart = t  # local t and not account for scr refresh
            break2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break2, 'tStartRefresh')  # time at next scr refresh
            break2.setAutoDraw(True)
        if break2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break2.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break2.tStop = t  # not accounting for scr refresh
                break2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break2, 'tStopRefresh')  # time at next scr refresh
                break2.setAutoDraw(False)
        
        # *distractor2* updates
        if distractor2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            distractor2.frameNStart = frameN  # exact frame index
            distractor2.tStart = t  # local t and not account for scr refresh
            distractor2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor2, 'tStartRefresh')  # time at next scr refresh
            distractor2.setAutoDraw(True)
        if distractor2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 3.3-frameTolerance:
                # keep track of stop time/frame for later
                distractor2.tStop = t  # not accounting for scr refresh
                distractor2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor2, 'tStopRefresh')  # time at next scr refresh
                distractor2.setAutoDraw(False)
        
        # *break3* updates
        if break3.status == NOT_STARTED and tThisFlip >= 3.3-frameTolerance:
            # keep track of start time/frame for later
            break3.frameNStart = frameN  # exact frame index
            break3.tStart = t  # local t and not account for scr refresh
            break3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break3, 'tStartRefresh')  # time at next scr refresh
            break3.setAutoDraw(True)
        if break3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break3.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break3.tStop = t  # not accounting for scr refresh
                break3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break3, 'tStopRefresh')  # time at next scr refresh
                break3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTtrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTtrial"-------
    for thisComponent in AXCPTtrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop2.addData('cue_text.started', cue_text.tStartRefresh)
    AXCPTtrialsLoop2.addData('cue_text.stopped', cue_text.tStopRefresh)
    AXCPTtrialsLoop2.addData('break1.started', break1.tStartRefresh)
    AXCPTtrialsLoop2.addData('break1.stopped', break1.tStopRefresh)
    AXCPTtrialsLoop2.addData('distractor1.started', distractor1.tStartRefresh)
    AXCPTtrialsLoop2.addData('distractor1.stopped', distractor1.tStopRefresh)
    AXCPTtrialsLoop2.addData('break2.started', break2.tStartRefresh)
    AXCPTtrialsLoop2.addData('break2.stopped', break2.tStopRefresh)
    AXCPTtrialsLoop2.addData('distractor2.started', distractor2.tStartRefresh)
    AXCPTtrialsLoop2.addData('distractor2.stopped', distractor2.tStopRefresh)
    AXCPTtrialsLoop2.addData('break3.started', break3.tStartRefresh)
    AXCPTtrialsLoop2.addData('break3.stopped', break3.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTprobe"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    probe_text.setText(probeVal)
    AXCPT_resp.keys = []
    AXCPT_resp.rt = []
    _AXCPT_resp_allKeys = []
    # keep track of which components have finished
    AXCPTprobeComponents = [probe_text, AXCPT_resp]
    for thisComponent in AXCPTprobeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTprobeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTprobe"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTprobeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTprobeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_text* updates
        if probe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_text.frameNStart = frameN  # exact frame index
            probe_text.tStart = t  # local t and not account for scr refresh
            probe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_text, 'tStartRefresh')  # time at next scr refresh
            probe_text.setAutoDraw(True)
        if probe_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                probe_text.tStop = t  # not accounting for scr refresh
                probe_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probe_text, 'tStopRefresh')  # time at next scr refresh
                probe_text.setAutoDraw(False)
        
        # *AXCPT_resp* updates
        waitOnFlip = False
        if AXCPT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPT_resp.frameNStart = frameN  # exact frame index
            AXCPT_resp.tStart = t  # local t and not account for scr refresh
            AXCPT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPT_resp, 'tStartRefresh')  # time at next scr refresh
            AXCPT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AXCPT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AXCPT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AXCPT_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.5-frameTolerance:
                # keep track of stop time/frame for later
                AXCPT_resp.tStop = t  # not accounting for scr refresh
                AXCPT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPT_resp, 'tStopRefresh')  # time at next scr refresh
                AXCPT_resp.status = FINISHED
        if AXCPT_resp.status == STARTED and not waitOnFlip:
            theseKeys = AXCPT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _AXCPT_resp_allKeys.extend(theseKeys)
            if len(_AXCPT_resp_allKeys):
                AXCPT_resp.keys = _AXCPT_resp_allKeys[-1].name  # just the last key pressed
                AXCPT_resp.rt = _AXCPT_resp_allKeys[-1].rt
                # was this correct?
                if (AXCPT_resp.keys == str(corrResponse)) or (AXCPT_resp.keys == corrResponse):
                    AXCPT_resp.corr = 1
                else:
                    AXCPT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTprobeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTprobe"-------
    for thisComponent in AXCPTprobeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop2.addData('probe_text.started', probe_text.tStartRefresh)
    AXCPTtrialsLoop2.addData('probe_text.stopped', probe_text.tStopRefresh)
    # check responses
    if AXCPT_resp.keys in ['', [], None]:  # No response was made
        AXCPT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           AXCPT_resp.corr = 1;  # correct non-response
        else:
           AXCPT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for AXCPTtrialsLoop2 (TrialHandler)
    AXCPTtrialsLoop2.addData('AXCPT_resp.keys',AXCPT_resp.keys)
    AXCPTtrialsLoop2.addData('AXCPT_resp.corr', AXCPT_resp.corr)
    if AXCPT_resp.keys != None:  # we had a response
        AXCPTtrialsLoop2.addData('AXCPT_resp.rt', AXCPT_resp.rt)
    AXCPTtrialsLoop2.addData('AXCPT_resp.started', AXCPT_resp.tStartRefresh)
    AXCPTtrialsLoop2.addData('AXCPT_resp.stopped', AXCPT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTfeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if AXCPT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text.setText(msg)
    # keep track of which components have finished
    AXCPTfeedbackComponents = [AXCPTfeedback_text]
    for thisComponent in AXCPTfeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTfeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTfeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTfeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text* updates
        if AXCPTfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text.setAutoDraw(True)
        if AXCPTfeedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTfeedback"-------
    for thisComponent in AXCPTfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop2.addData('AXCPTfeedback_text.started', AXCPTfeedback_text.tStartRefresh)
    AXCPTtrialsLoop2.addData('AXCPTfeedback_text.stopped', AXCPTfeedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'AXCPTtrialsLoop2'


# ------Prepare to start Routine "instrSEARCHbreak7"-------
continueRoutine = True
# update component parameters for each repeat
instrSEARCHbreak7Timer = util.Clock()
text_15.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin")
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
instrSEARCHbreak7Components = [instrHeaderText_11, text_15, key_resp_15]
for thisComponent in instrSEARCHbreak7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrSEARCHbreak7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrSEARCHbreak7"-------
while continueRoutine:
    # get current time
    t = instrSEARCHbreak7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrSEARCHbreak7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrHeaderText_11* updates
    if instrHeaderText_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_11.frameNStart = frameN  # exact frame index
        instrHeaderText_11.tStart = t  # local t and not account for scr refresh
        instrHeaderText_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_11, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_11.setAutoDraw(True)
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrSEARCHbreak7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrSEARCHbreak7"-------
for thisComponent in instrSEARCHbreak7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break7.duration', instrSEARCHbreak7Timer.getTime())
instrSEARCHbreak7Timer = []
thisExp.addData('instrHeaderText_11.started', instrHeaderText_11.tStartRefresh)
thisExp.addData('instrHeaderText_11.stopped', instrHeaderText_11.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrSEARCHbreak7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
searchLoop2 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('visualSearchConds.csv'),
    seed=None, name='searchLoop2')
thisExp.addLoop(searchLoop2)  # add the loop to the experiment
thisSearchLoop2 = searchLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSearchLoop2.rgb)
if thisSearchLoop2 != None:
    for paramName in thisSearchLoop2:
        exec('{} = thisSearchLoop2[paramName]'.format(paramName))

for thisSearchLoop2 in searchLoop2:
    currentLoop = searchLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisSearchLoop2.rgb)
    if thisSearchLoop2 != None:
        for paramName in thisSearchLoop2:
            exec('{} = thisSearchLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    searchLoop2.addData('timer_text.started', timer_text.tStartRefresh)
    searchLoop2.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "searchTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(PosList)
    
    targetOrient = choice(orientList)
    stim2Orient = choice (orientList)
    stim3Orient = choice(orientList)
    stim4Orient = choice(orientList)
    stim5Orient = choice(orientList)
    stim6Orient = choice(orientList)
    stim7Orient = choice(orientList)
    stim8Orient = choice(orientList)
    stim9Orient = choice(orientList)
    stim10Orient = choice(orientList)
    stim11Orient = choice(orientList)
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    targetStim.setPos(PosList[1])
    targetStim.setOri(targetOrient)
    targetStim.setText(targetLetter)
    searchStim2.setPos(PosList[2])
    searchStim2.setOri(stim2Orient)
    searchStim2.setText('L')
    searchStim3.setPos(PosList[3])
    searchStim3.setOri(stim3Orient)
    searchStim3.setText('L')
    searchStim4.setPos(PosList[4])
    searchStim4.setOri(stim4Orient)
    searchStim4.setText('L')
    searchStim5.setPos(PosList[5])
    searchStim5.setOri(stim5Orient)
    searchStim5.setText('L')
    searchStim6.setPos(PosList[6])
    searchStim6.setOri(stim6Orient)
    searchStim6.setText('L')
    searchStim7.setPos(PosList[7])
    searchStim7.setOri(stim7Orient)
    searchStim7.setText('L')
    searchStim8.setPos(PosList[8])
    searchStim8.setOri(stim8Orient)
    searchStim8.setText('L')
    searchStim9.setPos(PosList[9])
    searchStim9.setOri(stim9Orient)
    searchStim9.setText('L')
    searchStim10.setPos(PosList[10])
    searchStim10.setOri(stim10Orient)
    searchStim10.setText('L')
    searchStim11.setPos(PosList[11])
    searchStim11.setOri(stim11Orient)
    searchStim11.setText('L')
    # keep track of which components have finished
    searchTrialComponents = [key_resp_14, targetStim, searchStim2, searchStim3, searchStim4, searchStim5, searchStim6, searchStim7, searchStim8, searchStim9, searchStim10, searchStim11]
    for thisComponent in searchTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchTrial"-------
    while continueRoutine:
        # get current time
        t = searchTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['k', 'd'], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                # was this correct?
                if (key_resp_14.keys == str(corrResponse)) or (key_resp_14.keys == corrResponse):
                    key_resp_14.corr = 1
                else:
                    key_resp_14.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *targetStim* updates
        if targetStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetStim.frameNStart = frameN  # exact frame index
            targetStim.tStart = t  # local t and not account for scr refresh
            targetStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetStim, 'tStartRefresh')  # time at next scr refresh
            targetStim.setAutoDraw(True)
        
        # *searchStim2* updates
        if searchStim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim2.frameNStart = frameN  # exact frame index
            searchStim2.tStart = t  # local t and not account for scr refresh
            searchStim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim2, 'tStartRefresh')  # time at next scr refresh
            searchStim2.setAutoDraw(True)
        
        # *searchStim3* updates
        if searchStim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim3.frameNStart = frameN  # exact frame index
            searchStim3.tStart = t  # local t and not account for scr refresh
            searchStim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim3, 'tStartRefresh')  # time at next scr refresh
            searchStim3.setAutoDraw(True)
        
        # *searchStim4* updates
        if searchStim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim4.frameNStart = frameN  # exact frame index
            searchStim4.tStart = t  # local t and not account for scr refresh
            searchStim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim4, 'tStartRefresh')  # time at next scr refresh
            searchStim4.setAutoDraw(True)
        
        # *searchStim5* updates
        if searchStim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim5.frameNStart = frameN  # exact frame index
            searchStim5.tStart = t  # local t and not account for scr refresh
            searchStim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim5, 'tStartRefresh')  # time at next scr refresh
            searchStim5.setAutoDraw(True)
        
        # *searchStim6* updates
        if searchStim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim6.frameNStart = frameN  # exact frame index
            searchStim6.tStart = t  # local t and not account for scr refresh
            searchStim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim6, 'tStartRefresh')  # time at next scr refresh
            searchStim6.setAutoDraw(True)
        
        # *searchStim7* updates
        if searchStim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim7.frameNStart = frameN  # exact frame index
            searchStim7.tStart = t  # local t and not account for scr refresh
            searchStim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim7, 'tStartRefresh')  # time at next scr refresh
            searchStim7.setAutoDraw(True)
        
        # *searchStim8* updates
        if searchStim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim8.frameNStart = frameN  # exact frame index
            searchStim8.tStart = t  # local t and not account for scr refresh
            searchStim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim8, 'tStartRefresh')  # time at next scr refresh
            searchStim8.setAutoDraw(True)
        
        # *searchStim9* updates
        if searchStim9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim9.frameNStart = frameN  # exact frame index
            searchStim9.tStart = t  # local t and not account for scr refresh
            searchStim9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim9, 'tStartRefresh')  # time at next scr refresh
            searchStim9.setAutoDraw(True)
        
        # *searchStim10* updates
        if searchStim10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim10.frameNStart = frameN  # exact frame index
            searchStim10.tStart = t  # local t and not account for scr refresh
            searchStim10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim10, 'tStartRefresh')  # time at next scr refresh
            searchStim10.setAutoDraw(True)
        
        # *searchStim11* updates
        if searchStim11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim11.frameNStart = frameN  # exact frame index
            searchStim11.tStart = t  # local t and not account for scr refresh
            searchStim11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim11, 'tStartRefresh')  # time at next scr refresh
            searchStim11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchTrial"-------
    for thisComponent in searchTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           key_resp_14.corr = 1;  # correct non-response
        else:
           key_resp_14.corr = 0;  # failed to respond (incorrectly)
    # store data for searchLoop2 (TrialHandler)
    searchLoop2.addData('key_resp_14.keys',key_resp_14.keys)
    searchLoop2.addData('key_resp_14.corr', key_resp_14.corr)
    if key_resp_14.keys != None:  # we had a response
        searchLoop2.addData('key_resp_14.rt', key_resp_14.rt)
    searchLoop2.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    searchLoop2.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    searchLoop2.addData('targetStim.started', targetStim.tStartRefresh)
    searchLoop2.addData('targetStim.stopped', targetStim.tStopRefresh)
    # the Routine "searchTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "searchFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp_14.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    searchFeedbackText.setText(msg)
    # keep track of which components have finished
    searchFeedbackComponents = [searchFeedbackText]
    for thisComponent in searchFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *searchFeedbackText* updates
        if searchFeedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchFeedbackText.frameNStart = frameN  # exact frame index
            searchFeedbackText.tStart = t  # local t and not account for scr refresh
            searchFeedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchFeedbackText, 'tStartRefresh')  # time at next scr refresh
            searchFeedbackText.setAutoDraw(True)
        if searchFeedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > searchFeedbackText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                searchFeedbackText.tStop = t  # not accounting for scr refresh
                searchFeedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(searchFeedbackText, 'tStopRefresh')  # time at next scr refresh
                searchFeedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchFeedback"-------
    for thisComponent in searchFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    searchLoop2.addData('searchFeedbackText.started', searchFeedbackText.tStartRefresh)
    searchLoop2.addData('searchFeedbackText.stopped', searchFeedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'searchLoop2'


# ------Prepare to start Routine "instrMENTROTbreak8"-------
continueRoutine = True
# update component parameters for each repeat
instrMENTROTbreak8Timer = util.Clock()
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
text_17.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrMENTROTbreak8Components = [key_resp_10, instrHeaderText_13, text_17]
for thisComponent in instrMENTROTbreak8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrMENTROTbreak8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrMENTROTbreak8"-------
while continueRoutine:
    # get current time
    t = instrMENTROTbreak8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrMENTROTbreak8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_13* updates
    if instrHeaderText_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_13.frameNStart = frameN  # exact frame index
        instrHeaderText_13.tStart = t  # local t and not account for scr refresh
        instrHeaderText_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_13, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_13.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrMENTROTbreak8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrMENTROTbreak8"-------
for thisComponent in instrMENTROTbreak8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break8.duration', instrMENTROTbreak8Timer.getTime())
instrMENTROTbreak8Timer = []
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_13.started', instrHeaderText_13.tStartRefresh)
thisExp.addData('instrHeaderText_13.stopped', instrHeaderText_13.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# the Routine "instrMENTROTbreak8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mentRotTrialsLoop2 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('response.csv'),
    seed=None, name='mentRotTrialsLoop2')
thisExp.addLoop(mentRotTrialsLoop2)  # add the loop to the experiment
thisMentRotTrialsLoop2 = mentRotTrialsLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop2.rgb)
if thisMentRotTrialsLoop2 != None:
    for paramName in thisMentRotTrialsLoop2:
        exec('{} = thisMentRotTrialsLoop2[paramName]'.format(paramName))

for thisMentRotTrialsLoop2 in mentRotTrialsLoop2:
    currentLoop = mentRotTrialsLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop2.rgb)
    if thisMentRotTrialsLoop2 != None:
        for paramName in thisMentRotTrialsLoop2:
            exec('{} = thisMentRotTrialsLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "mentRotTrial"-------
    continueRoutine = True
    routineTimer.add(7.500000)
    # update component parameters for each repeat
    mentRotStimulus.setImage(imagefile)
    MROT_resp.keys = []
    MROT_resp.rt = []
    _MROT_resp_allKeys = []
    # keep track of which components have finished
    mentRotTrialComponents = [mentRotStimulus, MROT_resp]
    for thisComponent in mentRotTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mentRotStimulus* updates
        if mentRotStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mentRotStimulus.frameNStart = frameN  # exact frame index
            mentRotStimulus.tStart = t  # local t and not account for scr refresh
            mentRotStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mentRotStimulus, 'tStartRefresh')  # time at next scr refresh
            mentRotStimulus.setAutoDraw(True)
        if mentRotStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mentRotStimulus.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                mentRotStimulus.tStop = t  # not accounting for scr refresh
                mentRotStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mentRotStimulus, 'tStopRefresh')  # time at next scr refresh
                mentRotStimulus.setAutoDraw(False)
        
        # *MROT_resp* updates
        waitOnFlip = False
        if MROT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MROT_resp.frameNStart = frameN  # exact frame index
            MROT_resp.tStart = t  # local t and not account for scr refresh
            MROT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MROT_resp, 'tStartRefresh')  # time at next scr refresh
            MROT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MROT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MROT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MROT_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MROT_resp.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                MROT_resp.tStop = t  # not accounting for scr refresh
                MROT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MROT_resp, 'tStopRefresh')  # time at next scr refresh
                MROT_resp.status = FINISHED
        if MROT_resp.status == STARTED and not waitOnFlip:
            theseKeys = MROT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _MROT_resp_allKeys.extend(theseKeys)
            if len(_MROT_resp_allKeys):
                MROT_resp.keys = _MROT_resp_allKeys[-1].name  # just the last key pressed
                MROT_resp.rt = _MROT_resp_allKeys[-1].rt
                # was this correct?
                if (MROT_resp.keys == str(corrResponse)) or (MROT_resp.keys == corrResponse):
                    MROT_resp.corr = 1
                else:
                    MROT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotTrial"-------
    for thisComponent in mentRotTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop2.addData('mentRotStimulus.started', mentRotStimulus.tStartRefresh)
    mentRotTrialsLoop2.addData('mentRotStimulus.stopped', mentRotStimulus.tStopRefresh)
    # check responses
    if MROT_resp.keys in ['', [], None]:  # No response was made
        MROT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           MROT_resp.corr = 1;  # correct non-response
        else:
           MROT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for mentRotTrialsLoop2 (TrialHandler)
    mentRotTrialsLoop2.addData('MROT_resp.keys',MROT_resp.keys)
    mentRotTrialsLoop2.addData('MROT_resp.corr', MROT_resp.corr)
    if MROT_resp.keys != None:  # we had a response
        mentRotTrialsLoop2.addData('MROT_resp.rt', MROT_resp.rt)
    mentRotTrialsLoop2.addData('MROT_resp.started', MROT_resp.tStartRefresh)
    mentRotTrialsLoop2.addData('MROT_resp.stopped', MROT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "mentRotFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if MROT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    NBackfeedback_text_2.setText(msg)
    # keep track of which components have finished
    mentRotFeedbackComponents = [NBackfeedback_text_2]
    for thisComponent in mentRotFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackfeedback_text_2* updates
        if NBackfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackfeedback_text_2.frameNStart = frameN  # exact frame index
            NBackfeedback_text_2.tStart = t  # local t and not account for scr refresh
            NBackfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            NBackfeedback_text_2.setAutoDraw(True)
        if NBackfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NBackfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                NBackfeedback_text_2.tStop = t  # not accounting for scr refresh
                NBackfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                NBackfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotFeedback"-------
    for thisComponent in mentRotFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop2.addData('NBackfeedback_text_2.started', NBackfeedback_text_2.tStartRefresh)
    mentRotTrialsLoop2.addData('NBackfeedback_text_2.stopped', NBackfeedback_text_2.tStopRefresh)
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    mentRotTrialsLoop2.addData('timer_text.started', timer_text.tStartRefresh)
    mentRotTrialsLoop2.addData('timer_text.stopped', timer_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'mentRotTrialsLoop2'


# ------Prepare to start Routine "instrNBACKbreak9"-------
continueRoutine = True
# update component parameters for each repeat
instrNBACKbreak9Timer = util.Clock()
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
text_14.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrNBACKbreak9Components = [key_resp_9, instrHeaderText_10, text_14]
for thisComponent in instrNBACKbreak9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrNBACKbreak9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrNBACKbreak9"-------
while continueRoutine:
    # get current time
    t = instrNBACKbreak9Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrNBACKbreak9Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_10* updates
    if instrHeaderText_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_10.frameNStart = frameN  # exact frame index
        instrHeaderText_10.tStart = t  # local t and not account for scr refresh
        instrHeaderText_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_10, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_10.setAutoDraw(True)
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrNBACKbreak9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrNBACKbreak9"-------
for thisComponent in instrNBACKbreak9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break9.duration', instrNBACKbreak9Timer.getTime())
instrNBACKbreak9Timer = []
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_10.started', instrHeaderText_10.tStartRefresh)
thisExp.addData('instrHeaderText_10.stopped', instrHeaderText_10.tStopRefresh)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# the Routine "instrNBACKbreak9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBackTargetLoop3 = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='NBackTargetLoop3')
thisExp.addLoop(NBackTargetLoop3)  # add the loop to the experiment
thisNBackTargetLoop3 = NBackTargetLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLoop3.rgb)
if thisNBackTargetLoop3 != None:
    for paramName in thisNBackTargetLoop3:
        exec('{} = thisNBackTargetLoop3[paramName]'.format(paramName))

for thisNBackTargetLoop3 in NBackTargetLoop3:
    currentLoop = NBackTargetLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTargetLoop3.rgb)
    if thisNBackTargetLoop3 != None:
        for paramName in thisNBackTargetLoop3:
            exec('{} = thisNBackTargetLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTargetLoop3.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTargetLoop3.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFirst3Trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    nletter=choice(letters)
    
    NBackText_1.setText(nletter)
    NBack_resp_1.keys = []
    NBack_resp_1.rt = []
    _NBack_resp_1_allKeys = []
    # keep track of which components have finished
    NBackFirst3TrialsComponents = [NBackText_1, NBack_resp_1]
    for thisComponent in NBackFirst3TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFirst3TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFirst3Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFirst3TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFirst3TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_1* updates
        if NBackText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_1.frameNStart = frameN  # exact frame index
            NBackText_1.tStart = t  # local t and not account for scr refresh
            NBackText_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_1, 'tStartRefresh')  # time at next scr refresh
            NBackText_1.setAutoDraw(True)
        if NBackText_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_1.tStop = t  # not accounting for scr refresh
                NBackText_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_1, 'tStopRefresh')  # time at next scr refresh
                NBackText_1.setAutoDraw(False)
        
        # *NBack_resp_1* updates
        waitOnFlip = False
        if NBack_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_1.frameNStart = frameN  # exact frame index
            NBack_resp_1.tStart = t  # local t and not account for scr refresh
            NBack_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_1, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_1.tStop = t  # not accounting for scr refresh
                NBack_resp_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_1, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_1.status = FINISHED
        if NBack_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_1.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_1_allKeys.extend(theseKeys)
            if len(_NBack_resp_1_allKeys):
                NBack_resp_1.keys = _NBack_resp_1_allKeys[-1].name  # just the last key pressed
                NBack_resp_1.rt = _NBack_resp_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFirst3TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFirst3Trials"-------
    for thisComponent in NBackFirst3TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTargetLoop3.addData('NBackText_1.started', NBackText_1.tStartRefresh)
    NBackTargetLoop3.addData('NBackText_1.stopped', NBackText_1.tStopRefresh)
    # check responses
    if NBack_resp_1.keys in ['', [], None]:  # No response was made
        NBack_resp_1.keys = None
    NBackTargetLoop3.addData('NBack_resp_1.keys',NBack_resp_1.keys)
    if NBack_resp_1.keys != None:  # we had a response
        NBackTargetLoop3.addData('NBack_resp_1.rt', NBack_resp_1.rt)
    NBackTargetLoop3.addData('NBack_resp_1.started', NBack_resp_1.tStartRefresh)
    NBackTargetLoop3.addData('NBack_resp_1.stopped', NBack_resp_1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'NBackTargetLoop3'


# set up handler to look after randomisation of conditions etc
NBackTrialsLoop3 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('2-back_loop.xlsx'),
    seed=None, name='NBackTrialsLoop3')
thisExp.addLoop(NBackTrialsLoop3)  # add the loop to the experiment
thisNBackTrialsLoop3 = NBackTrialsLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop3.rgb)
if thisNBackTrialsLoop3 != None:
    for paramName in thisNBackTrialsLoop3:
        exec('{} = thisNBackTrialsLoop3[paramName]'.format(paramName))

for thisNBackTrialsLoop3 in NBackTrialsLoop3:
    currentLoop = NBackTrialsLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisNBackTrialsLoop3.rgb)
    if thisNBackTrialsLoop3 != None:
        for paramName in thisNBackTrialsLoop3:
            exec('{} = thisNBackTrialsLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    NBackTrialsLoop3.addData('timer_text.started', timer_text.tStartRefresh)
    NBackTrialsLoop3.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "NBackRemainderTrials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if trialType=='nonTarget':
        letters = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        nletter=choice(letters)
        if nletter==Back2minus1:
                nletter=choice(letters)
        if nletter==Back2minus2:
                nletter=choice(letters)
    elif trialType=='target':
        nletter=Back2minus3
    NBackText_2.setText(nletter)
    NBack_resp_2.keys = []
    NBack_resp_2.rt = []
    _NBack_resp_2_allKeys = []
    # keep track of which components have finished
    NBackRemainderTrialsComponents = [NBackText_2, NBack_resp_2]
    for thisComponent in NBackRemainderTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackRemainderTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackRemainderTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackRemainderTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackRemainderTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackText_2* updates
        if NBackText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackText_2.frameNStart = frameN  # exact frame index
            NBackText_2.tStart = t  # local t and not account for scr refresh
            NBackText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackText_2, 'tStartRefresh')  # time at next scr refresh
            NBackText_2.setAutoDraw(True)
        if NBackText_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBackText_2.tStop = t  # not accounting for scr refresh
                NBackText_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackText_2, 'tStopRefresh')  # time at next scr refresh
                NBackText_2.setAutoDraw(False)
        
        # *NBack_resp_2* updates
        waitOnFlip = False
        if NBack_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBack_resp_2.frameNStart = frameN  # exact frame index
            NBack_resp_2.tStart = t  # local t and not account for scr refresh
            NBack_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBack_resp_2, 'tStartRefresh')  # time at next scr refresh
            NBack_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NBack_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NBack_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NBack_resp_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                NBack_resp_2.tStop = t  # not accounting for scr refresh
                NBack_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBack_resp_2, 'tStopRefresh')  # time at next scr refresh
                NBack_resp_2.status = FINISHED
        if NBack_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = NBack_resp_2.getKeys(keyList=['k', 'd'], waitRelease=False)
            _NBack_resp_2_allKeys.extend(theseKeys)
            if len(_NBack_resp_2_allKeys):
                NBack_resp_2.keys = _NBack_resp_2_allKeys[-1].name  # just the last key pressed
                NBack_resp_2.rt = _NBack_resp_2_allKeys[-1].rt
                # was this correct?
                if (NBack_resp_2.keys == str(corrResponse)) or (NBack_resp_2.keys == corrResponse):
                    NBack_resp_2.corr = 1
                else:
                    NBack_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackRemainderTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackRemainderTrials"-------
    for thisComponent in NBackRemainderTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Back2minus3=Back2minus2
    Back2minus2=Back2minus1
    Back2minus1=nletter
    NBackTrialsLoop3.addData('NBackText_2.started', NBackText_2.tStartRefresh)
    NBackTrialsLoop3.addData('NBackText_2.stopped', NBackText_2.tStopRefresh)
    # check responses
    if NBack_resp_2.keys in ['', [], None]:  # No response was made
        NBack_resp_2.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           NBack_resp_2.corr = 1;  # correct non-response
        else:
           NBack_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for NBackTrialsLoop3 (TrialHandler)
    NBackTrialsLoop3.addData('NBack_resp_2.keys',NBack_resp_2.keys)
    NBackTrialsLoop3.addData('NBack_resp_2.corr', NBack_resp_2.corr)
    if NBack_resp_2.keys != None:  # we had a response
        NBackTrialsLoop3.addData('NBack_resp_2.rt', NBack_resp_2.rt)
    NBackTrialsLoop3.addData('NBack_resp_2.started', NBack_resp_2.tStartRefresh)
    NBackTrialsLoop3.addData('NBack_resp_2.stopped', NBack_resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "NBackFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if NBack_resp_2.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text_2.setText(msg)
    # keep track of which components have finished
    NBackFeedbackComponents = [AXCPTfeedback_text_2]
    for thisComponent in NBackFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NBackFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NBackFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NBackFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NBackFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text_2* updates
        if AXCPTfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text_2.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text_2.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text_2.setAutoDraw(True)
        if AXCPTfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text_2.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NBackFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NBackFeedback"-------
    for thisComponent in NBackFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NBackTrialsLoop3.addData('AXCPTfeedback_text_2.started', AXCPTfeedback_text_2.tStartRefresh)
    NBackTrialsLoop3.addData('AXCPTfeedback_text_2.stopped', AXCPTfeedback_text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'NBackTrialsLoop3'


# ------Prepare to start Routine "instrSEARCHbreak10"-------
continueRoutine = True
# update component parameters for each repeat
instrSEARCHbreak10Timer = util.Clock()
text_16.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin")
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instrSEARCHbreak10Components = [instrHeaderText_12, text_16, key_resp_5]
for thisComponent in instrSEARCHbreak10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrSEARCHbreak10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrSEARCHbreak10"-------
while continueRoutine:
    # get current time
    t = instrSEARCHbreak10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrSEARCHbreak10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrHeaderText_12* updates
    if instrHeaderText_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_12.frameNStart = frameN  # exact frame index
        instrHeaderText_12.tStart = t  # local t and not account for scr refresh
        instrHeaderText_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_12, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_12.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrSEARCHbreak10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrSEARCHbreak10"-------
for thisComponent in instrSEARCHbreak10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break10.duration', instrSEARCHbreak10Timer.getTime())
instrSEARCHbreak10Timer = []
thisExp.addData('instrHeaderText_12.started', instrHeaderText_12.tStartRefresh)
thisExp.addData('instrHeaderText_12.stopped', instrHeaderText_12.tStopRefresh)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrSEARCHbreak10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
searchLoop3 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('visualSearchConds.csv'),
    seed=None, name='searchLoop3')
thisExp.addLoop(searchLoop3)  # add the loop to the experiment
thisSearchLoop3 = searchLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSearchLoop3.rgb)
if thisSearchLoop3 != None:
    for paramName in thisSearchLoop3:
        exec('{} = thisSearchLoop3[paramName]'.format(paramName))

for thisSearchLoop3 in searchLoop3:
    currentLoop = searchLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisSearchLoop3.rgb)
    if thisSearchLoop3 != None:
        for paramName in thisSearchLoop3:
            exec('{} = thisSearchLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    searchLoop3.addData('timer_text.started', timer_text.tStartRefresh)
    searchLoop3.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "searchTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(PosList)
    
    targetOrient = choice(orientList)
    stim2Orient = choice (orientList)
    stim3Orient = choice(orientList)
    stim4Orient = choice(orientList)
    stim5Orient = choice(orientList)
    stim6Orient = choice(orientList)
    stim7Orient = choice(orientList)
    stim8Orient = choice(orientList)
    stim9Orient = choice(orientList)
    stim10Orient = choice(orientList)
    stim11Orient = choice(orientList)
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    targetStim.setPos(PosList[1])
    targetStim.setOri(targetOrient)
    targetStim.setText(targetLetter)
    searchStim2.setPos(PosList[2])
    searchStim2.setOri(stim2Orient)
    searchStim2.setText('L')
    searchStim3.setPos(PosList[3])
    searchStim3.setOri(stim3Orient)
    searchStim3.setText('L')
    searchStim4.setPos(PosList[4])
    searchStim4.setOri(stim4Orient)
    searchStim4.setText('L')
    searchStim5.setPos(PosList[5])
    searchStim5.setOri(stim5Orient)
    searchStim5.setText('L')
    searchStim6.setPos(PosList[6])
    searchStim6.setOri(stim6Orient)
    searchStim6.setText('L')
    searchStim7.setPos(PosList[7])
    searchStim7.setOri(stim7Orient)
    searchStim7.setText('L')
    searchStim8.setPos(PosList[8])
    searchStim8.setOri(stim8Orient)
    searchStim8.setText('L')
    searchStim9.setPos(PosList[9])
    searchStim9.setOri(stim9Orient)
    searchStim9.setText('L')
    searchStim10.setPos(PosList[10])
    searchStim10.setOri(stim10Orient)
    searchStim10.setText('L')
    searchStim11.setPos(PosList[11])
    searchStim11.setOri(stim11Orient)
    searchStim11.setText('L')
    # keep track of which components have finished
    searchTrialComponents = [key_resp_14, targetStim, searchStim2, searchStim3, searchStim4, searchStim5, searchStim6, searchStim7, searchStim8, searchStim9, searchStim10, searchStim11]
    for thisComponent in searchTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchTrial"-------
    while continueRoutine:
        # get current time
        t = searchTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['k', 'd'], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                # was this correct?
                if (key_resp_14.keys == str(corrResponse)) or (key_resp_14.keys == corrResponse):
                    key_resp_14.corr = 1
                else:
                    key_resp_14.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *targetStim* updates
        if targetStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetStim.frameNStart = frameN  # exact frame index
            targetStim.tStart = t  # local t and not account for scr refresh
            targetStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetStim, 'tStartRefresh')  # time at next scr refresh
            targetStim.setAutoDraw(True)
        
        # *searchStim2* updates
        if searchStim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim2.frameNStart = frameN  # exact frame index
            searchStim2.tStart = t  # local t and not account for scr refresh
            searchStim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim2, 'tStartRefresh')  # time at next scr refresh
            searchStim2.setAutoDraw(True)
        
        # *searchStim3* updates
        if searchStim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim3.frameNStart = frameN  # exact frame index
            searchStim3.tStart = t  # local t and not account for scr refresh
            searchStim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim3, 'tStartRefresh')  # time at next scr refresh
            searchStim3.setAutoDraw(True)
        
        # *searchStim4* updates
        if searchStim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim4.frameNStart = frameN  # exact frame index
            searchStim4.tStart = t  # local t and not account for scr refresh
            searchStim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim4, 'tStartRefresh')  # time at next scr refresh
            searchStim4.setAutoDraw(True)
        
        # *searchStim5* updates
        if searchStim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim5.frameNStart = frameN  # exact frame index
            searchStim5.tStart = t  # local t and not account for scr refresh
            searchStim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim5, 'tStartRefresh')  # time at next scr refresh
            searchStim5.setAutoDraw(True)
        
        # *searchStim6* updates
        if searchStim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim6.frameNStart = frameN  # exact frame index
            searchStim6.tStart = t  # local t and not account for scr refresh
            searchStim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim6, 'tStartRefresh')  # time at next scr refresh
            searchStim6.setAutoDraw(True)
        
        # *searchStim7* updates
        if searchStim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim7.frameNStart = frameN  # exact frame index
            searchStim7.tStart = t  # local t and not account for scr refresh
            searchStim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim7, 'tStartRefresh')  # time at next scr refresh
            searchStim7.setAutoDraw(True)
        
        # *searchStim8* updates
        if searchStim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim8.frameNStart = frameN  # exact frame index
            searchStim8.tStart = t  # local t and not account for scr refresh
            searchStim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim8, 'tStartRefresh')  # time at next scr refresh
            searchStim8.setAutoDraw(True)
        
        # *searchStim9* updates
        if searchStim9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim9.frameNStart = frameN  # exact frame index
            searchStim9.tStart = t  # local t and not account for scr refresh
            searchStim9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim9, 'tStartRefresh')  # time at next scr refresh
            searchStim9.setAutoDraw(True)
        
        # *searchStim10* updates
        if searchStim10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim10.frameNStart = frameN  # exact frame index
            searchStim10.tStart = t  # local t and not account for scr refresh
            searchStim10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim10, 'tStartRefresh')  # time at next scr refresh
            searchStim10.setAutoDraw(True)
        
        # *searchStim11* updates
        if searchStim11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchStim11.frameNStart = frameN  # exact frame index
            searchStim11.tStart = t  # local t and not account for scr refresh
            searchStim11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchStim11, 'tStartRefresh')  # time at next scr refresh
            searchStim11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchTrial"-------
    for thisComponent in searchTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           key_resp_14.corr = 1;  # correct non-response
        else:
           key_resp_14.corr = 0;  # failed to respond (incorrectly)
    # store data for searchLoop3 (TrialHandler)
    searchLoop3.addData('key_resp_14.keys',key_resp_14.keys)
    searchLoop3.addData('key_resp_14.corr', key_resp_14.corr)
    if key_resp_14.keys != None:  # we had a response
        searchLoop3.addData('key_resp_14.rt', key_resp_14.rt)
    searchLoop3.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    searchLoop3.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    searchLoop3.addData('targetStim.started', targetStim.tStartRefresh)
    searchLoop3.addData('targetStim.stopped', targetStim.tStopRefresh)
    # the Routine "searchTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "searchFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp_14.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    searchFeedbackText.setText(msg)
    # keep track of which components have finished
    searchFeedbackComponents = [searchFeedbackText]
    for thisComponent in searchFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "searchFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *searchFeedbackText* updates
        if searchFeedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            searchFeedbackText.frameNStart = frameN  # exact frame index
            searchFeedbackText.tStart = t  # local t and not account for scr refresh
            searchFeedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(searchFeedbackText, 'tStartRefresh')  # time at next scr refresh
            searchFeedbackText.setAutoDraw(True)
        if searchFeedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > searchFeedbackText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                searchFeedbackText.tStop = t  # not accounting for scr refresh
                searchFeedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(searchFeedbackText, 'tStopRefresh')  # time at next scr refresh
                searchFeedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "searchFeedback"-------
    for thisComponent in searchFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    searchLoop3.addData('searchFeedbackText.started', searchFeedbackText.tStartRefresh)
    searchLoop3.addData('searchFeedbackText.stopped', searchFeedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'searchLoop3'


# ------Prepare to start Routine "instrMENTROTbreak11"-------
continueRoutine = True
# update component parameters for each repeat
instrMENTROTbreak11Timer = util.Clock()
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
text_18.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin")
# keep track of which components have finished
instrMENTROTbreak11Components = [key_resp_11, instrHeaderText_14, text_18]
for thisComponent in instrMENTROTbreak11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrMENTROTbreak11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrMENTROTbreak11"-------
while continueRoutine:
    # get current time
    t = instrMENTROTbreak11Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrMENTROTbreak11Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_14* updates
    if instrHeaderText_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_14.frameNStart = frameN  # exact frame index
        instrHeaderText_14.tStart = t  # local t and not account for scr refresh
        instrHeaderText_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_14, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_14.setAutoDraw(True)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrMENTROTbreak11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrMENTROTbreak11"-------
for thisComponent in instrMENTROTbreak11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break11.duration', instrMENTROTbreak11Timer.getTime())
instrMENTROTbreak11Timer = []
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_14.started', instrHeaderText_14.tStartRefresh)
thisExp.addData('instrHeaderText_14.stopped', instrHeaderText_14.tStopRefresh)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# the Routine "instrMENTROTbreak11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mentRotTrialsLoop3 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('response.csv'),
    seed=None, name='mentRotTrialsLoop3')
thisExp.addLoop(mentRotTrialsLoop3)  # add the loop to the experiment
thisMentRotTrialsLoop3 = mentRotTrialsLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop3.rgb)
if thisMentRotTrialsLoop3 != None:
    for paramName in thisMentRotTrialsLoop3:
        exec('{} = thisMentRotTrialsLoop3[paramName]'.format(paramName))

for thisMentRotTrialsLoop3 in mentRotTrialsLoop3:
    currentLoop = mentRotTrialsLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisMentRotTrialsLoop3.rgb)
    if thisMentRotTrialsLoop3 != None:
        for paramName in thisMentRotTrialsLoop3:
            exec('{} = thisMentRotTrialsLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "mentRotTrial"-------
    continueRoutine = True
    routineTimer.add(7.500000)
    # update component parameters for each repeat
    mentRotStimulus.setImage(imagefile)
    MROT_resp.keys = []
    MROT_resp.rt = []
    _MROT_resp_allKeys = []
    # keep track of which components have finished
    mentRotTrialComponents = [mentRotStimulus, MROT_resp]
    for thisComponent in mentRotTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mentRotStimulus* updates
        if mentRotStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mentRotStimulus.frameNStart = frameN  # exact frame index
            mentRotStimulus.tStart = t  # local t and not account for scr refresh
            mentRotStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mentRotStimulus, 'tStartRefresh')  # time at next scr refresh
            mentRotStimulus.setAutoDraw(True)
        if mentRotStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mentRotStimulus.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                mentRotStimulus.tStop = t  # not accounting for scr refresh
                mentRotStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mentRotStimulus, 'tStopRefresh')  # time at next scr refresh
                mentRotStimulus.setAutoDraw(False)
        
        # *MROT_resp* updates
        waitOnFlip = False
        if MROT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MROT_resp.frameNStart = frameN  # exact frame index
            MROT_resp.tStart = t  # local t and not account for scr refresh
            MROT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MROT_resp, 'tStartRefresh')  # time at next scr refresh
            MROT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MROT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MROT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MROT_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MROT_resp.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                MROT_resp.tStop = t  # not accounting for scr refresh
                MROT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MROT_resp, 'tStopRefresh')  # time at next scr refresh
                MROT_resp.status = FINISHED
        if MROT_resp.status == STARTED and not waitOnFlip:
            theseKeys = MROT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _MROT_resp_allKeys.extend(theseKeys)
            if len(_MROT_resp_allKeys):
                MROT_resp.keys = _MROT_resp_allKeys[-1].name  # just the last key pressed
                MROT_resp.rt = _MROT_resp_allKeys[-1].rt
                # was this correct?
                if (MROT_resp.keys == str(corrResponse)) or (MROT_resp.keys == corrResponse):
                    MROT_resp.corr = 1
                else:
                    MROT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotTrial"-------
    for thisComponent in mentRotTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop3.addData('mentRotStimulus.started', mentRotStimulus.tStartRefresh)
    mentRotTrialsLoop3.addData('mentRotStimulus.stopped', mentRotStimulus.tStopRefresh)
    # check responses
    if MROT_resp.keys in ['', [], None]:  # No response was made
        MROT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           MROT_resp.corr = 1;  # correct non-response
        else:
           MROT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for mentRotTrialsLoop3 (TrialHandler)
    mentRotTrialsLoop3.addData('MROT_resp.keys',MROT_resp.keys)
    mentRotTrialsLoop3.addData('MROT_resp.corr', MROT_resp.corr)
    if MROT_resp.keys != None:  # we had a response
        mentRotTrialsLoop3.addData('MROT_resp.rt', MROT_resp.rt)
    mentRotTrialsLoop3.addData('MROT_resp.started', MROT_resp.tStartRefresh)
    mentRotTrialsLoop3.addData('MROT_resp.stopped', MROT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "mentRotFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if MROT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    NBackfeedback_text_2.setText(msg)
    # keep track of which components have finished
    mentRotFeedbackComponents = [NBackfeedback_text_2]
    for thisComponent in mentRotFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mentRotFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mentRotFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mentRotFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mentRotFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NBackfeedback_text_2* updates
        if NBackfeedback_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBackfeedback_text_2.frameNStart = frameN  # exact frame index
            NBackfeedback_text_2.tStart = t  # local t and not account for scr refresh
            NBackfeedback_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBackfeedback_text_2, 'tStartRefresh')  # time at next scr refresh
            NBackfeedback_text_2.setAutoDraw(True)
        if NBackfeedback_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NBackfeedback_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                NBackfeedback_text_2.tStop = t  # not accounting for scr refresh
                NBackfeedback_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NBackfeedback_text_2, 'tStopRefresh')  # time at next scr refresh
                NBackfeedback_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentRotFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mentRotFeedback"-------
    for thisComponent in mentRotFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mentRotTrialsLoop3.addData('NBackfeedback_text_2.started', NBackfeedback_text_2.tStartRefresh)
    mentRotTrialsLoop3.addData('NBackfeedback_text_2.stopped', NBackfeedback_text_2.tStopRefresh)
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    mentRotTrialsLoop3.addData('timer_text.started', timer_text.tStartRefresh)
    mentRotTrialsLoop3.addData('timer_text.stopped', timer_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'mentRotTrialsLoop3'


# ------Prepare to start Routine "instrAXCPTbreak12"-------
continueRoutine = True
# update component parameters for each repeat
instrAXCPTbreak12Timer = util.Clock()
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instrAXCPTbreak12Components = [key_resp_7, instrHeaderText_8, text_12]
for thisComponent in instrAXCPTbreak12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrAXCPTbreak12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrAXCPTbreak12"-------
while continueRoutine:
    # get current time
    t = instrAXCPTbreak12Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrAXCPTbreak12Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['k'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrHeaderText_8* updates
    if instrHeaderText_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrHeaderText_8.frameNStart = frameN  # exact frame index
        instrHeaderText_8.tStart = t  # local t and not account for scr refresh
        instrHeaderText_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrHeaderText_8, 'tStartRefresh')  # time at next scr refresh
        instrHeaderText_8.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrAXCPTbreak12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrAXCPTbreak12"-------
for thisComponent in instrAXCPTbreak12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('break12.duration', instrAXCPTbreak12Timer.getTime())
instrAXCPTbreak12Timer = []
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrHeaderText_8.started', instrHeaderText_8.tStartRefresh)
thisExp.addData('instrHeaderText_8.stopped', instrHeaderText_8.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "instrAXCPTbreak12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "createLoopTimer"-------
continueRoutine = True
# update component parameters for each repeat
loopTimer = util.Clock()
# keep track of which components have finished
createLoopTimerComponents = []
for thisComponent in createLoopTimerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
createLoopTimerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "createLoopTimer"-------
while continueRoutine:
    # get current time
    t = createLoopTimerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=createLoopTimerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in createLoopTimerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "createLoopTimer"-------
for thisComponent in createLoopTimerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AXCPTtrialsLoop3 = data.TrialHandler(nReps=6000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialType.csv'),
    seed=None, name='AXCPTtrialsLoop3')
thisExp.addLoop(AXCPTtrialsLoop3)  # add the loop to the experiment
thisAXCPTtrialsLoop3 = AXCPTtrialsLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop3.rgb)
if thisAXCPTtrialsLoop3 != None:
    for paramName in thisAXCPTtrialsLoop3:
        exec('{} = thisAXCPTtrialsLoop3[paramName]'.format(paramName))

for thisAXCPTtrialsLoop3 in AXCPTtrialsLoop3:
    currentLoop = AXCPTtrialsLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisAXCPTtrialsLoop3.rgb)
    if thisAXCPTtrialsLoop3 != None:
        for paramName in thisAXCPTtrialsLoop3:
            exec('{} = thisAXCPTtrialsLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "timer"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    timerComponents = [timer_text]
    for thisComponent in timerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "timer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = timerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=timerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if loopTimer.getTime() > 600:
            currentLoop.finished = True
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text, 'tStopRefresh')  # time at next scr refresh
                timer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "timer"-------
    for thisComponent in timerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
    AXCPTtrialsLoop3.addData('timer_text.started', timer_text.tStartRefresh)
    AXCPTtrialsLoop3.addData('timer_text.stopped', timer_text.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTtrial"-------
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    #function choice(arr) {
    #  return arr[Math.floor(Math.random() * arr.length)];
    #}
    
    distractor1Val = choice(distractors)
    distractor2Val = choice(distractors)
    
    
    
    if trialType == 'target':
        cueVal = 'A'
        probeVal = 'X'
    
    elif trialType == 'probeWrong':
        cueVal = 'A'
        probeVal = choice(Yletters)
    
    elif trialType == 'cueWrong':
        cueVal = choice(Bletters)
        probeVal = 'X'
    
    elif trialType == 'bothWrong':
        cueVal = choice(Bletters)
        probeVal = choice(Yletters)
    cue_text.setText(cueVal)
    distractor1.setText(distractor1Val)
    distractor2.setText(distractor2Val)
    # keep track of which components have finished
    AXCPTtrialComponents = [cue_text, break1, distractor1, break2, distractor2, break3]
    for thisComponent in AXCPTtrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTtrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTtrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTtrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTtrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_text* updates
        if cue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_text.frameNStart = frameN  # exact frame index
            cue_text.tStart = t  # local t and not account for scr refresh
            cue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_text, 'tStartRefresh')  # time at next scr refresh
            cue_text.setAutoDraw(True)
        if cue_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cue_text.tStop = t  # not accounting for scr refresh
                cue_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_text, 'tStopRefresh')  # time at next scr refresh
                cue_text.setAutoDraw(False)
        
        # *break1* updates
        if break1.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            break1.frameNStart = frameN  # exact frame index
            break1.tStart = t  # local t and not account for scr refresh
            break1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
            break1.setAutoDraw(True)
        if break1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break1.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break1.tStop = t  # not accounting for scr refresh
                break1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break1, 'tStopRefresh')  # time at next scr refresh
                break1.setAutoDraw(False)
        
        # *distractor1* updates
        if distractor1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            distractor1.frameNStart = frameN  # exact frame index
            distractor1.tStart = t  # local t and not account for scr refresh
            distractor1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor1, 'tStartRefresh')  # time at next scr refresh
            distractor1.setAutoDraw(True)
        if distractor1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.8-frameTolerance:
                # keep track of stop time/frame for later
                distractor1.tStop = t  # not accounting for scr refresh
                distractor1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor1, 'tStopRefresh')  # time at next scr refresh
                distractor1.setAutoDraw(False)
        
        # *break2* updates
        if break2.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
            # keep track of start time/frame for later
            break2.frameNStart = frameN  # exact frame index
            break2.tStart = t  # local t and not account for scr refresh
            break2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break2, 'tStartRefresh')  # time at next scr refresh
            break2.setAutoDraw(True)
        if break2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break2.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break2.tStop = t  # not accounting for scr refresh
                break2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break2, 'tStopRefresh')  # time at next scr refresh
                break2.setAutoDraw(False)
        
        # *distractor2* updates
        if distractor2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            distractor2.frameNStart = frameN  # exact frame index
            distractor2.tStart = t  # local t and not account for scr refresh
            distractor2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor2, 'tStartRefresh')  # time at next scr refresh
            distractor2.setAutoDraw(True)
        if distractor2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 3.3-frameTolerance:
                # keep track of stop time/frame for later
                distractor2.tStop = t  # not accounting for scr refresh
                distractor2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor2, 'tStopRefresh')  # time at next scr refresh
                distractor2.setAutoDraw(False)
        
        # *break3* updates
        if break3.status == NOT_STARTED and tThisFlip >= 3.3-frameTolerance:
            # keep track of start time/frame for later
            break3.frameNStart = frameN  # exact frame index
            break3.tStart = t  # local t and not account for scr refresh
            break3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break3, 'tStartRefresh')  # time at next scr refresh
            break3.setAutoDraw(True)
        if break3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break3.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                break3.tStop = t  # not accounting for scr refresh
                break3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break3, 'tStopRefresh')  # time at next scr refresh
                break3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTtrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTtrial"-------
    for thisComponent in AXCPTtrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop3.addData('cue_text.started', cue_text.tStartRefresh)
    AXCPTtrialsLoop3.addData('cue_text.stopped', cue_text.tStopRefresh)
    AXCPTtrialsLoop3.addData('break1.started', break1.tStartRefresh)
    AXCPTtrialsLoop3.addData('break1.stopped', break1.tStopRefresh)
    AXCPTtrialsLoop3.addData('distractor1.started', distractor1.tStartRefresh)
    AXCPTtrialsLoop3.addData('distractor1.stopped', distractor1.tStopRefresh)
    AXCPTtrialsLoop3.addData('break2.started', break2.tStartRefresh)
    AXCPTtrialsLoop3.addData('break2.stopped', break2.tStopRefresh)
    AXCPTtrialsLoop3.addData('distractor2.started', distractor2.tStartRefresh)
    AXCPTtrialsLoop3.addData('distractor2.stopped', distractor2.tStopRefresh)
    AXCPTtrialsLoop3.addData('break3.started', break3.tStartRefresh)
    AXCPTtrialsLoop3.addData('break3.stopped', break3.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTprobe"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    probe_text.setText(probeVal)
    AXCPT_resp.keys = []
    AXCPT_resp.rt = []
    _AXCPT_resp_allKeys = []
    # keep track of which components have finished
    AXCPTprobeComponents = [probe_text, AXCPT_resp]
    for thisComponent in AXCPTprobeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTprobeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTprobe"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTprobeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTprobeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_text* updates
        if probe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_text.frameNStart = frameN  # exact frame index
            probe_text.tStart = t  # local t and not account for scr refresh
            probe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_text, 'tStartRefresh')  # time at next scr refresh
            probe_text.setAutoDraw(True)
        if probe_text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 0.3-frameTolerance:
                # keep track of stop time/frame for later
                probe_text.tStop = t  # not accounting for scr refresh
                probe_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probe_text, 'tStopRefresh')  # time at next scr refresh
                probe_text.setAutoDraw(False)
        
        # *AXCPT_resp* updates
        waitOnFlip = False
        if AXCPT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPT_resp.frameNStart = frameN  # exact frame index
            AXCPT_resp.tStart = t  # local t and not account for scr refresh
            AXCPT_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPT_resp, 'tStartRefresh')  # time at next scr refresh
            AXCPT_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AXCPT_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AXCPT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AXCPT_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.5-frameTolerance:
                # keep track of stop time/frame for later
                AXCPT_resp.tStop = t  # not accounting for scr refresh
                AXCPT_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPT_resp, 'tStopRefresh')  # time at next scr refresh
                AXCPT_resp.status = FINISHED
        if AXCPT_resp.status == STARTED and not waitOnFlip:
            theseKeys = AXCPT_resp.getKeys(keyList=['k', 'd'], waitRelease=False)
            _AXCPT_resp_allKeys.extend(theseKeys)
            if len(_AXCPT_resp_allKeys):
                AXCPT_resp.keys = _AXCPT_resp_allKeys[-1].name  # just the last key pressed
                AXCPT_resp.rt = _AXCPT_resp_allKeys[-1].rt
                # was this correct?
                if (AXCPT_resp.keys == str(corrResponse)) or (AXCPT_resp.keys == corrResponse):
                    AXCPT_resp.corr = 1
                else:
                    AXCPT_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTprobeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTprobe"-------
    for thisComponent in AXCPTprobeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop3.addData('probe_text.started', probe_text.tStartRefresh)
    AXCPTtrialsLoop3.addData('probe_text.stopped', probe_text.tStopRefresh)
    # check responses
    if AXCPT_resp.keys in ['', [], None]:  # No response was made
        AXCPT_resp.keys = None
        # was no response the correct answer?!
        if str(corrResponse).lower() == 'none':
           AXCPT_resp.corr = 1;  # correct non-response
        else:
           AXCPT_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for AXCPTtrialsLoop3 (TrialHandler)
    AXCPTtrialsLoop3.addData('AXCPT_resp.keys',AXCPT_resp.keys)
    AXCPTtrialsLoop3.addData('AXCPT_resp.corr', AXCPT_resp.corr)
    if AXCPT_resp.keys != None:  # we had a response
        AXCPTtrialsLoop3.addData('AXCPT_resp.rt', AXCPT_resp.rt)
    AXCPTtrialsLoop3.addData('AXCPT_resp.started', AXCPT_resp.tStartRefresh)
    AXCPTtrialsLoop3.addData('AXCPT_resp.stopped', AXCPT_resp.tStopRefresh)
    
    # ------Prepare to start Routine "AXCPTfeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if AXCPT_resp.corr:
        msg = "Correct"
    else:
        msg = "Incorrect"
    AXCPTfeedback_text.setText(msg)
    # keep track of which components have finished
    AXCPTfeedbackComponents = [AXCPTfeedback_text]
    for thisComponent in AXCPTfeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AXCPTfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AXCPTfeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AXCPTfeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AXCPTfeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AXCPTfeedback_text* updates
        if AXCPTfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AXCPTfeedback_text.frameNStart = frameN  # exact frame index
            AXCPTfeedback_text.tStart = t  # local t and not account for scr refresh
            AXCPTfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AXCPTfeedback_text, 'tStartRefresh')  # time at next scr refresh
            AXCPTfeedback_text.setAutoDraw(True)
        if AXCPTfeedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > AXCPTfeedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                AXCPTfeedback_text.tStop = t  # not accounting for scr refresh
                AXCPTfeedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AXCPTfeedback_text, 'tStopRefresh')  # time at next scr refresh
                AXCPTfeedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AXCPTfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AXCPTfeedback"-------
    for thisComponent in AXCPTfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AXCPTtrialsLoop3.addData('AXCPTfeedback_text.started', AXCPTfeedback_text.tStartRefresh)
    AXCPTtrialsLoop3.addData('AXCPTfeedback_text.stopped', AXCPTfeedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 6000 repeats of 'AXCPTtrialsLoop3'


# ------Prepare to start Routine "instrBRUMSpost"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_9
gotValidClick = False  # until a click is received
# keep track of which components have finished
instrBRUMSpostComponents = [text_19, mouse_9, BRUMSheader_2]
for thisComponent in instrBRUMSpostComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrBRUMSpostClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrBRUMSpost"-------
while continueRoutine:
    # get current time
    t = instrBRUMSpostClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrBRUMSpostClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *BRUMSheader_2* updates
    if BRUMSheader_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BRUMSheader_2.frameNStart = frameN  # exact frame index
        BRUMSheader_2.tStart = t  # local t and not account for scr refresh
        BRUMSheader_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BRUMSheader_2, 'tStartRefresh')  # time at next scr refresh
        BRUMSheader_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrBRUMSpostComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrBRUMSpost"-------
for thisComponent in instrBRUMSpostComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_9.started', mouse_9.tStart)
thisExp.addData('mouse_9.stopped', mouse_9.tStop)
thisExp.nextEntry()
thisExp.addData('BRUMSheader_2.started', BRUMSheader_2.tStartRefresh)
thisExp.addData('BRUMSheader_2.stopped', BRUMSheader_2.tStopRefresh)
# the Routine "instrBRUMSpost" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_1"-------
continueRoutine = True
# update component parameters for each repeat
BRUMSTimer = util.Clock()
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
slider1.reset()
slider2.reset()
slider3.reset()
slider4.reset()
slider5.reset()
slider6.reset()
slider7.reset()
slider8.reset()
# keep track of which components have finished
BRUMS_1Components = [mouse_3, mouse_visibility_fix, slider1, slider2, slider3, slider4, slider5, slider6, slider7, slider8, text_9, panicky, lively, confused, wornout, depressed, downheartened, annoyed, exhausted]
for thisComponent in BRUMS_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_1"-------
while continueRoutine:
    # get current time
    t = BRUMS_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider1.getRating() > 0 and slider2.getRating() > 0 and slider3.getRating() > 0 and slider4.getRating() > 0 and slider5.getRating() > 0 and slider6.getRating() > 0 and slider7.getRating() > 0 and slider8.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix* updates
    if mouse_visibility_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix.frameNStart = frameN  # exact frame index
        mouse_visibility_fix.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix.setAutoDraw(True)
    if mouse_visibility_fix.status == STARTED:  # only update if drawing
        mouse_visibility_fix.setPos((mouse_3.getPos()[0], mouse_3.getPos()[1]), log=False)
    
    # *slider1* updates
    if slider1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider1.frameNStart = frameN  # exact frame index
        slider1.tStart = t  # local t and not account for scr refresh
        slider1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider1, 'tStartRefresh')  # time at next scr refresh
        slider1.setAutoDraw(True)
    
    # *slider2* updates
    if slider2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider2.frameNStart = frameN  # exact frame index
        slider2.tStart = t  # local t and not account for scr refresh
        slider2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider2, 'tStartRefresh')  # time at next scr refresh
        slider2.setAutoDraw(True)
    
    # *slider3* updates
    if slider3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider3.frameNStart = frameN  # exact frame index
        slider3.tStart = t  # local t and not account for scr refresh
        slider3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider3, 'tStartRefresh')  # time at next scr refresh
        slider3.setAutoDraw(True)
    
    # *slider4* updates
    if slider4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider4.frameNStart = frameN  # exact frame index
        slider4.tStart = t  # local t and not account for scr refresh
        slider4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider4, 'tStartRefresh')  # time at next scr refresh
        slider4.setAutoDraw(True)
    
    # *slider5* updates
    if slider5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider5.frameNStart = frameN  # exact frame index
        slider5.tStart = t  # local t and not account for scr refresh
        slider5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider5, 'tStartRefresh')  # time at next scr refresh
        slider5.setAutoDraw(True)
    
    # *slider6* updates
    if slider6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider6.frameNStart = frameN  # exact frame index
        slider6.tStart = t  # local t and not account for scr refresh
        slider6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider6, 'tStartRefresh')  # time at next scr refresh
        slider6.setAutoDraw(True)
    
    # *slider7* updates
    if slider7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider7.frameNStart = frameN  # exact frame index
        slider7.tStart = t  # local t and not account for scr refresh
        slider7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider7, 'tStartRefresh')  # time at next scr refresh
        slider7.setAutoDraw(True)
    
    # *slider8* updates
    if slider8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider8.frameNStart = frameN  # exact frame index
        slider8.tStart = t  # local t and not account for scr refresh
        slider8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider8, 'tStartRefresh')  # time at next scr refresh
        slider8.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *panicky* updates
    if panicky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        panicky.frameNStart = frameN  # exact frame index
        panicky.tStart = t  # local t and not account for scr refresh
        panicky.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(panicky, 'tStartRefresh')  # time at next scr refresh
        panicky.setAutoDraw(True)
    
    # *lively* updates
    if lively.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lively.frameNStart = frameN  # exact frame index
        lively.tStart = t  # local t and not account for scr refresh
        lively.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lively, 'tStartRefresh')  # time at next scr refresh
        lively.setAutoDraw(True)
    
    # *confused* updates
    if confused.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confused.frameNStart = frameN  # exact frame index
        confused.tStart = t  # local t and not account for scr refresh
        confused.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confused, 'tStartRefresh')  # time at next scr refresh
        confused.setAutoDraw(True)
    
    # *wornout* updates
    if wornout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wornout.frameNStart = frameN  # exact frame index
        wornout.tStart = t  # local t and not account for scr refresh
        wornout.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wornout, 'tStartRefresh')  # time at next scr refresh
        wornout.setAutoDraw(True)
    
    # *depressed* updates
    if depressed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        depressed.frameNStart = frameN  # exact frame index
        depressed.tStart = t  # local t and not account for scr refresh
        depressed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(depressed, 'tStartRefresh')  # time at next scr refresh
        depressed.setAutoDraw(True)
    
    # *downheartened* updates
    if downheartened.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downheartened.frameNStart = frameN  # exact frame index
        downheartened.tStart = t  # local t and not account for scr refresh
        downheartened.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downheartened, 'tStartRefresh')  # time at next scr refresh
        downheartened.setAutoDraw(True)
    
    # *annoyed* updates
    if annoyed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        annoyed.frameNStart = frameN  # exact frame index
        annoyed.tStart = t  # local t and not account for scr refresh
        annoyed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(annoyed, 'tStartRefresh')  # time at next scr refresh
        annoyed.setAutoDraw(True)
    
    # *exhausted* updates
    if exhausted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exhausted.frameNStart = frameN  # exact frame index
        exhausted.tStart = t  # local t and not account for scr refresh
        exhausted.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exhausted, 'tStartRefresh')  # time at next scr refresh
        exhausted.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_1"-------
for thisComponent in BRUMS_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix.started', mouse_visibility_fix.tStartRefresh)
thisExp.addData('mouse_visibility_fix.stopped', mouse_visibility_fix.tStopRefresh)
thisExp.addData('slider1.response', slider1.getRating())
thisExp.addData('slider1.rt', slider1.getRT())
thisExp.addData('slider1.started', slider1.tStartRefresh)
thisExp.addData('slider1.stopped', slider1.tStopRefresh)
thisExp.addData('slider2.response', slider2.getRating())
thisExp.addData('slider2.rt', slider2.getRT())
thisExp.addData('slider2.started', slider2.tStartRefresh)
thisExp.addData('slider2.stopped', slider2.tStopRefresh)
thisExp.addData('slider3.response', slider3.getRating())
thisExp.addData('slider3.rt', slider3.getRT())
thisExp.addData('slider3.started', slider3.tStartRefresh)
thisExp.addData('slider3.stopped', slider3.tStopRefresh)
thisExp.addData('slider4.response', slider4.getRating())
thisExp.addData('slider4.rt', slider4.getRT())
thisExp.addData('slider4.started', slider4.tStartRefresh)
thisExp.addData('slider4.stopped', slider4.tStopRefresh)
thisExp.addData('slider5.response', slider5.getRating())
thisExp.addData('slider5.rt', slider5.getRT())
thisExp.addData('slider5.started', slider5.tStartRefresh)
thisExp.addData('slider5.stopped', slider5.tStopRefresh)
thisExp.addData('slider6.response', slider6.getRating())
thisExp.addData('slider6.rt', slider6.getRT())
thisExp.addData('slider6.started', slider6.tStartRefresh)
thisExp.addData('slider6.stopped', slider6.tStopRefresh)
thisExp.addData('slider7.response', slider7.getRating())
thisExp.addData('slider7.rt', slider7.getRT())
thisExp.addData('slider7.started', slider7.tStartRefresh)
thisExp.addData('slider7.stopped', slider7.tStopRefresh)
thisExp.addData('slider8.response', slider8.getRating())
thisExp.addData('slider8.rt', slider8.getRT())
thisExp.addData('slider8.started', slider8.tStartRefresh)
thisExp.addData('slider8.stopped', slider8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('panicky.started', panicky.tStartRefresh)
thisExp.addData('panicky.stopped', panicky.tStopRefresh)
thisExp.addData('lively.started', lively.tStartRefresh)
thisExp.addData('lively.stopped', lively.tStopRefresh)
thisExp.addData('confused.started', confused.tStartRefresh)
thisExp.addData('confused.stopped', confused.tStopRefresh)
thisExp.addData('wornout.started', wornout.tStartRefresh)
thisExp.addData('wornout.stopped', wornout.tStopRefresh)
thisExp.addData('depressed.started', depressed.tStartRefresh)
thisExp.addData('depressed.stopped', depressed.tStopRefresh)
thisExp.addData('downheartened.started', downheartened.tStartRefresh)
thisExp.addData('downheartened.stopped', downheartened.tStopRefresh)
thisExp.addData('annoyed.started', annoyed.tStartRefresh)
thisExp.addData('annoyed.stopped', annoyed.tStopRefresh)
thisExp.addData('exhausted.started', exhausted.tStartRefresh)
thisExp.addData('exhausted.stopped', exhausted.tStopRefresh)
# the Routine "BRUMS_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
gotValidClick = False  # until a click is received
slider9.reset()
slider10.reset()
slider11.reset()
slider12.reset()
slider13.reset()
slider14.reset()
slider15.reset()
slider16.reset()
# keep track of which components have finished
BRUMS_2Components = [mouse_5, mouse_visibility_fix_2, slider9, slider10, slider11, slider12, slider13, slider14, slider15, slider16, text_10, mixedup, sleepy, bitter, unhappy, anxious, worried, energetic, miserable]
for thisComponent in BRUMS_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_2"-------
while continueRoutine:
    # get current time
    t = BRUMS_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider9.getRating() > 0 and slider10.getRating() > 0 and slider11.getRating() > 0 and slider12.getRating() > 0 and slider13.getRating() > 0 and slider14.getRating() > 0 and slider15.getRating() > 0 and slider16.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix_2* updates
    if mouse_visibility_fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix_2.frameNStart = frameN  # exact frame index
        mouse_visibility_fix_2.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix_2, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix_2.setAutoDraw(True)
    if mouse_visibility_fix_2.status == STARTED:  # only update if drawing
        mouse_visibility_fix_2.setPos((mouse_5.getPos()[0], mouse_5.getPos()[1]), log=False)
    
    # *slider9* updates
    if slider9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider9.frameNStart = frameN  # exact frame index
        slider9.tStart = t  # local t and not account for scr refresh
        slider9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider9, 'tStartRefresh')  # time at next scr refresh
        slider9.setAutoDraw(True)
    
    # *slider10* updates
    if slider10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider10.frameNStart = frameN  # exact frame index
        slider10.tStart = t  # local t and not account for scr refresh
        slider10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider10, 'tStartRefresh')  # time at next scr refresh
        slider10.setAutoDraw(True)
    
    # *slider11* updates
    if slider11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider11.frameNStart = frameN  # exact frame index
        slider11.tStart = t  # local t and not account for scr refresh
        slider11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider11, 'tStartRefresh')  # time at next scr refresh
        slider11.setAutoDraw(True)
    
    # *slider12* updates
    if slider12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider12.frameNStart = frameN  # exact frame index
        slider12.tStart = t  # local t and not account for scr refresh
        slider12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider12, 'tStartRefresh')  # time at next scr refresh
        slider12.setAutoDraw(True)
    
    # *slider13* updates
    if slider13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider13.frameNStart = frameN  # exact frame index
        slider13.tStart = t  # local t and not account for scr refresh
        slider13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider13, 'tStartRefresh')  # time at next scr refresh
        slider13.setAutoDraw(True)
    
    # *slider14* updates
    if slider14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider14.frameNStart = frameN  # exact frame index
        slider14.tStart = t  # local t and not account for scr refresh
        slider14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider14, 'tStartRefresh')  # time at next scr refresh
        slider14.setAutoDraw(True)
    
    # *slider15* updates
    if slider15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider15.frameNStart = frameN  # exact frame index
        slider15.tStart = t  # local t and not account for scr refresh
        slider15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider15, 'tStartRefresh')  # time at next scr refresh
        slider15.setAutoDraw(True)
    
    # *slider16* updates
    if slider16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider16.frameNStart = frameN  # exact frame index
        slider16.tStart = t  # local t and not account for scr refresh
        slider16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider16, 'tStartRefresh')  # time at next scr refresh
        slider16.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *mixedup* updates
    if mixedup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mixedup.frameNStart = frameN  # exact frame index
        mixedup.tStart = t  # local t and not account for scr refresh
        mixedup.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mixedup, 'tStartRefresh')  # time at next scr refresh
        mixedup.setAutoDraw(True)
    
    # *sleepy* updates
    if sleepy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sleepy.frameNStart = frameN  # exact frame index
        sleepy.tStart = t  # local t and not account for scr refresh
        sleepy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sleepy, 'tStartRefresh')  # time at next scr refresh
        sleepy.setAutoDraw(True)
    
    # *bitter* updates
    if bitter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bitter.frameNStart = frameN  # exact frame index
        bitter.tStart = t  # local t and not account for scr refresh
        bitter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bitter, 'tStartRefresh')  # time at next scr refresh
        bitter.setAutoDraw(True)
    
    # *unhappy* updates
    if unhappy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unhappy.frameNStart = frameN  # exact frame index
        unhappy.tStart = t  # local t and not account for scr refresh
        unhappy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unhappy, 'tStartRefresh')  # time at next scr refresh
        unhappy.setAutoDraw(True)
    
    # *anxious* updates
    if anxious.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anxious.frameNStart = frameN  # exact frame index
        anxious.tStart = t  # local t and not account for scr refresh
        anxious.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anxious, 'tStartRefresh')  # time at next scr refresh
        anxious.setAutoDraw(True)
    
    # *worried* updates
    if worried.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        worried.frameNStart = frameN  # exact frame index
        worried.tStart = t  # local t and not account for scr refresh
        worried.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(worried, 'tStartRefresh')  # time at next scr refresh
        worried.setAutoDraw(True)
    
    # *energetic* updates
    if energetic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        energetic.frameNStart = frameN  # exact frame index
        energetic.tStart = t  # local t and not account for scr refresh
        energetic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(energetic, 'tStartRefresh')  # time at next scr refresh
        energetic.setAutoDraw(True)
    
    # *miserable* updates
    if miserable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        miserable.frameNStart = frameN  # exact frame index
        miserable.tStart = t  # local t and not account for scr refresh
        miserable.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(miserable, 'tStartRefresh')  # time at next scr refresh
        miserable.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_2"-------
for thisComponent in BRUMS_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix_2.started', mouse_visibility_fix_2.tStartRefresh)
thisExp.addData('mouse_visibility_fix_2.stopped', mouse_visibility_fix_2.tStopRefresh)
thisExp.addData('slider9.response', slider9.getRating())
thisExp.addData('slider9.rt', slider9.getRT())
thisExp.addData('slider9.started', slider9.tStartRefresh)
thisExp.addData('slider9.stopped', slider9.tStopRefresh)
thisExp.addData('slider10.response', slider10.getRating())
thisExp.addData('slider10.rt', slider10.getRT())
thisExp.addData('slider10.started', slider10.tStartRefresh)
thisExp.addData('slider10.stopped', slider10.tStopRefresh)
thisExp.addData('slider11.response', slider11.getRating())
thisExp.addData('slider11.rt', slider11.getRT())
thisExp.addData('slider11.started', slider11.tStartRefresh)
thisExp.addData('slider11.stopped', slider11.tStopRefresh)
thisExp.addData('slider12.response', slider12.getRating())
thisExp.addData('slider12.rt', slider12.getRT())
thisExp.addData('slider12.started', slider12.tStartRefresh)
thisExp.addData('slider12.stopped', slider12.tStopRefresh)
thisExp.addData('slider13.response', slider13.getRating())
thisExp.addData('slider13.rt', slider13.getRT())
thisExp.addData('slider13.started', slider13.tStartRefresh)
thisExp.addData('slider13.stopped', slider13.tStopRefresh)
thisExp.addData('slider14.response', slider14.getRating())
thisExp.addData('slider14.rt', slider14.getRT())
thisExp.addData('slider14.started', slider14.tStartRefresh)
thisExp.addData('slider14.stopped', slider14.tStopRefresh)
thisExp.addData('slider15.response', slider15.getRating())
thisExp.addData('slider15.rt', slider15.getRT())
thisExp.addData('slider15.started', slider15.tStartRefresh)
thisExp.addData('slider15.stopped', slider15.tStopRefresh)
thisExp.addData('slider16.response', slider16.getRating())
thisExp.addData('slider16.rt', slider16.getRT())
thisExp.addData('slider16.started', slider16.tStartRefresh)
thisExp.addData('slider16.stopped', slider16.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('mixedup.started', mixedup.tStartRefresh)
thisExp.addData('mixedup.stopped', mixedup.tStopRefresh)
thisExp.addData('sleepy.started', sleepy.tStartRefresh)
thisExp.addData('sleepy.stopped', sleepy.tStopRefresh)
thisExp.addData('bitter.started', bitter.tStartRefresh)
thisExp.addData('bitter.stopped', bitter.tStopRefresh)
thisExp.addData('unhappy.started', unhappy.tStartRefresh)
thisExp.addData('unhappy.stopped', unhappy.tStopRefresh)
thisExp.addData('anxious.started', anxious.tStartRefresh)
thisExp.addData('anxious.stopped', anxious.tStopRefresh)
thisExp.addData('worried.started', worried.tStartRefresh)
thisExp.addData('worried.stopped', worried.tStopRefresh)
thisExp.addData('energetic.started', energetic.tStartRefresh)
thisExp.addData('energetic.stopped', energetic.tStopRefresh)
thisExp.addData('miserable.started', miserable.tStartRefresh)
thisExp.addData('miserable.stopped', miserable.tStopRefresh)
# the Routine "BRUMS_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BRUMS_3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
gotValidClick = False  # until a click is received
slider17.reset()
slider18.reset()
slider19.reset()
slider20.reset()
slider21.reset()
slider22.reset()
slider23.reset()
slider24.reset()
# keep track of which components have finished
BRUMS_3Components = [mouse_6, mouse_visibility_fix_3, slider17, slider18, slider19, slider20, slider21, slider22, slider23, slider24, text_11, muddled, nervous, angry, active, tired, badtempered, alert, uncertain]
for thisComponent in BRUMS_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BRUMS_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BRUMS_3"-------
while continueRoutine:
    # get current time
    t = BRUMS_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BRUMS_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if slider17.getRating() > 0 and slider18.getRating() > 0 and slider19.getRating() > 0 and slider20.getRating() > 0 and slider21.getRating() > 0 and slider22.getRating() > 0 and slider23.getRating() > 0 and slider24.getRating() > 0:
        continueRoutine = false
    
    # *mouse_visibility_fix_3* updates
    if mouse_visibility_fix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_visibility_fix_3.frameNStart = frameN  # exact frame index
        mouse_visibility_fix_3.tStart = t  # local t and not account for scr refresh
        mouse_visibility_fix_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_visibility_fix_3, 'tStartRefresh')  # time at next scr refresh
        mouse_visibility_fix_3.setAutoDraw(True)
    if mouse_visibility_fix_3.status == STARTED:  # only update if drawing
        mouse_visibility_fix_3.setPos((mouse_6.getPos()[0], mouse_6.getPos()[1]), log=False)
    
    # *slider17* updates
    if slider17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider17.frameNStart = frameN  # exact frame index
        slider17.tStart = t  # local t and not account for scr refresh
        slider17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider17, 'tStartRefresh')  # time at next scr refresh
        slider17.setAutoDraw(True)
    
    # *slider18* updates
    if slider18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider18.frameNStart = frameN  # exact frame index
        slider18.tStart = t  # local t and not account for scr refresh
        slider18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider18, 'tStartRefresh')  # time at next scr refresh
        slider18.setAutoDraw(True)
    
    # *slider19* updates
    if slider19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider19.frameNStart = frameN  # exact frame index
        slider19.tStart = t  # local t and not account for scr refresh
        slider19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider19, 'tStartRefresh')  # time at next scr refresh
        slider19.setAutoDraw(True)
    
    # *slider20* updates
    if slider20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider20.frameNStart = frameN  # exact frame index
        slider20.tStart = t  # local t and not account for scr refresh
        slider20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider20, 'tStartRefresh')  # time at next scr refresh
        slider20.setAutoDraw(True)
    
    # *slider21* updates
    if slider21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider21.frameNStart = frameN  # exact frame index
        slider21.tStart = t  # local t and not account for scr refresh
        slider21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider21, 'tStartRefresh')  # time at next scr refresh
        slider21.setAutoDraw(True)
    
    # *slider22* updates
    if slider22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider22.frameNStart = frameN  # exact frame index
        slider22.tStart = t  # local t and not account for scr refresh
        slider22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider22, 'tStartRefresh')  # time at next scr refresh
        slider22.setAutoDraw(True)
    
    # *slider23* updates
    if slider23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider23.frameNStart = frameN  # exact frame index
        slider23.tStart = t  # local t and not account for scr refresh
        slider23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider23, 'tStartRefresh')  # time at next scr refresh
        slider23.setAutoDraw(True)
    
    # *slider24* updates
    if slider24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider24.frameNStart = frameN  # exact frame index
        slider24.tStart = t  # local t and not account for scr refresh
        slider24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider24, 'tStartRefresh')  # time at next scr refresh
        slider24.setAutoDraw(True)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *muddled* updates
    if muddled.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        muddled.frameNStart = frameN  # exact frame index
        muddled.tStart = t  # local t and not account for scr refresh
        muddled.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(muddled, 'tStartRefresh')  # time at next scr refresh
        muddled.setAutoDraw(True)
    
    # *nervous* updates
    if nervous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nervous.frameNStart = frameN  # exact frame index
        nervous.tStart = t  # local t and not account for scr refresh
        nervous.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nervous, 'tStartRefresh')  # time at next scr refresh
        nervous.setAutoDraw(True)
    
    # *angry* updates
    if angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        angry.frameNStart = frameN  # exact frame index
        angry.tStart = t  # local t and not account for scr refresh
        angry.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angry, 'tStartRefresh')  # time at next scr refresh
        angry.setAutoDraw(True)
    
    # *active* updates
    if active.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        active.frameNStart = frameN  # exact frame index
        active.tStart = t  # local t and not account for scr refresh
        active.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(active, 'tStartRefresh')  # time at next scr refresh
        active.setAutoDraw(True)
    
    # *tired* updates
    if tired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tired.frameNStart = frameN  # exact frame index
        tired.tStart = t  # local t and not account for scr refresh
        tired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tired, 'tStartRefresh')  # time at next scr refresh
        tired.setAutoDraw(True)
    
    # *badtempered* updates
    if badtempered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        badtempered.frameNStart = frameN  # exact frame index
        badtempered.tStart = t  # local t and not account for scr refresh
        badtempered.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(badtempered, 'tStartRefresh')  # time at next scr refresh
        badtempered.setAutoDraw(True)
    
    # *alert* updates
    if alert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        alert.frameNStart = frameN  # exact frame index
        alert.tStart = t  # local t and not account for scr refresh
        alert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alert, 'tStartRefresh')  # time at next scr refresh
        alert.setAutoDraw(True)
    
    # *uncertain* updates
    if uncertain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertain.frameNStart = frameN  # exact frame index
        uncertain.tStart = t  # local t and not account for scr refresh
        uncertain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertain, 'tStartRefresh')  # time at next scr refresh
        uncertain.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BRUMS_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BRUMS_3"-------
for thisComponent in BRUMS_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
psychoJS.experiment.addData('BRUMS.duration', BRUMSTimer.getTime())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
thisExp.addData('mouse_visibility_fix_3.started', mouse_visibility_fix_3.tStartRefresh)
thisExp.addData('mouse_visibility_fix_3.stopped', mouse_visibility_fix_3.tStopRefresh)
thisExp.addData('slider17.response', slider17.getRating())
thisExp.addData('slider17.rt', slider17.getRT())
thisExp.addData('slider17.started', slider17.tStartRefresh)
thisExp.addData('slider17.stopped', slider17.tStopRefresh)
thisExp.addData('slider18.response', slider18.getRating())
thisExp.addData('slider18.rt', slider18.getRT())
thisExp.addData('slider18.started', slider18.tStartRefresh)
thisExp.addData('slider18.stopped', slider18.tStopRefresh)
thisExp.addData('slider19.response', slider19.getRating())
thisExp.addData('slider19.rt', slider19.getRT())
thisExp.addData('slider19.started', slider19.tStartRefresh)
thisExp.addData('slider19.stopped', slider19.tStopRefresh)
thisExp.addData('slider20.response', slider20.getRating())
thisExp.addData('slider20.rt', slider20.getRT())
thisExp.addData('slider20.started', slider20.tStartRefresh)
thisExp.addData('slider20.stopped', slider20.tStopRefresh)
thisExp.addData('slider21.response', slider21.getRating())
thisExp.addData('slider21.rt', slider21.getRT())
thisExp.addData('slider21.started', slider21.tStartRefresh)
thisExp.addData('slider21.stopped', slider21.tStopRefresh)
thisExp.addData('slider22.response', slider22.getRating())
thisExp.addData('slider22.rt', slider22.getRT())
thisExp.addData('slider22.started', slider22.tStartRefresh)
thisExp.addData('slider22.stopped', slider22.tStopRefresh)
thisExp.addData('slider23.response', slider23.getRating())
thisExp.addData('slider23.rt', slider23.getRT())
thisExp.addData('slider23.started', slider23.tStartRefresh)
thisExp.addData('slider23.stopped', slider23.tStopRefresh)
thisExp.addData('slider24.response', slider24.getRating())
thisExp.addData('slider24.rt', slider24.getRT())
thisExp.addData('slider24.started', slider24.tStartRefresh)
thisExp.addData('slider24.stopped', slider24.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('muddled.started', muddled.tStartRefresh)
thisExp.addData('muddled.stopped', muddled.tStopRefresh)
thisExp.addData('nervous.started', nervous.tStartRefresh)
thisExp.addData('nervous.stopped', nervous.tStopRefresh)
thisExp.addData('angry.started', angry.tStartRefresh)
thisExp.addData('angry.stopped', angry.tStopRefresh)
thisExp.addData('active.started', active.tStartRefresh)
thisExp.addData('active.stopped', active.tStopRefresh)
thisExp.addData('tired.started', tired.tStartRefresh)
thisExp.addData('tired.stopped', tired.tStopRefresh)
thisExp.addData('badtempered.started', badtempered.tStartRefresh)
thisExp.addData('badtempered.stopped', badtempered.tStopRefresh)
thisExp.addData('alert.started', alert.tStartRefresh)
thisExp.addData('alert.stopped', alert.tStopRefresh)
thisExp.addData('uncertain.started', uncertain.tStartRefresh)
thisExp.addData('uncertain.stopped', uncertain.tStopRefresh)
# the Routine "BRUMS_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
endComponents = [text_20, key_resp_12]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psychoJS.experiment.addData('elapsed.time', elapsedTime.getTime())
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
