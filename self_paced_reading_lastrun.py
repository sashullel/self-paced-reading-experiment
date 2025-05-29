#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Май 25, 2025, at 14:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Comprehension test'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Участник': f"{randint(1000, 9999):03.0f}",
    'Группа': ["Группа 1", "Группа 2"],
    'Возраст': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s' % (expInfo['Участник'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\klens\\Desktop\\experiment\\self_paced_reading_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None,
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('start_resp') is None:
        # initialise start_resp
        start_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='start_resp',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_9') is None:
        # initialise key_resp_9
        key_resp_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_9',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "intro" ---
    introtxt = visual.TextBox2(
         win, text='Вам будет необходимо прочитать предложения. Они будут появляться на экране по фрагментам. \nПока вы читаете один фрагмент, остальные будут скрыты. Чтобы скрыть текущий фрагмент и открыть следующий, нажмите ПРОБЕЛ. \n\nВнимательно читайте предложения. Каждый фрагмент можно прочитать только один раз. Вернуться к предыдущим фрагментам невозможно. \n\nВремя чтения будет фиксироваться, поэтому, пожалуйста, убедитесь, что Вас ничего не будет отвлекать во время тестирования. Если Вам необходимо отвлечься, завершите чтение текущего предложения.\n\nПосле каждого предложения Вам будет необходимо оценить суждения на понимание прочитанного.  \nНажмите Y на клавиатуре, если суждение следует из предложения или просто не противоречит ему. Нажмите N, если суждение скорее противоречит предложению.\n\nОценивайте суждение по отношению лишь к ТОЛЬКО ЧТО прочитанному предложению.\n\nПеред началом эксперимента у вас должна быть включена английская раскладка (в ином случае необходимо перезапустить).\n\nЭксперимент займет не более 7 минут.\n\nНажмите ПРОБЕЛ, чтобы начать тестовое прочтение.\n', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='introtxt',
         depth=0, autoLog=True,
    )
    start_resp = keyboard.Keyboard(deviceName='start_resp')
    # Run 'Begin Experiment' code from code
    group1_trials_reps = 0
    group2_trials_reps = 0
    
    if expInfo["Группа"] == "Группа 1":
        group1_trials_reps = 1
        
    if expInfo["Группа"] == "Группа 2":
        group2_trials_reps = 1
        
    
    # --- Initialize components for Routine "test" ---
    textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(-0.5, -0.1), draggable=False,      letterHeight=0.08,
         size=(1.2, 2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=0, autoLog=True,
    )
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "question_test" ---
    q = visual.TextBox2(
         win, text='Ответьте на вопрос, нажав Y (ДА) или N (НЕТ)', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='top-center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='q',
         depth=0, autoLog=True,
    )
    textbox_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=[0], draggable=False,      letterHeight=0.07,
         size=(1.5, 0.3), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_3',
         depth=-1, autoLog=True,
    )
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "btw2" ---
    textbox_4 = visual.TextBox2(
         win, text='Нажмите ПРОБЕЛ для перехода к следующему предложению', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.07,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_4',
         depth=0, autoLog=True,
    )
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    
    # --- Initialize components for Routine "btw" ---
    textbox_5 = visual.TextBox2(
         win, text='Конец тестовых предложений.\n\nЧтобы начать эксперимент и перейти к следующему предложению, нажмите ПРОБЕЛ', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.07,
         size=(1, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_5',
         depth=0, autoLog=True,
    )
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    
    # --- Initialize components for Routine "show_text" ---
    sentence = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0.1, -0.1), draggable=False,      letterHeight=0.07,
         size=(1.4, 2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='sentence',
         depth=0, autoLog=True,
    )
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "question" ---
    question_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0.3), draggable=False,      letterHeight=0.05,
         size=(2.6, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='top-center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='question_2',
         depth=0, autoLog=True,
    )
    textbox_2 = visual.TextBox2(
         win, text='', placeholder=None, font='Georgia',
         ori=0.0, pos=(0, 0.05), draggable=False, units='height',     letterHeight=0.07,
         size=(1.7, 1), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_2',
         depth=-1, autoLog=True,
    )
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "btw2" ---
    textbox_4 = visual.TextBox2(
         win, text='Нажмите ПРОБЕЛ для перехода к следующему предложению', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.07,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_4',
         depth=0, autoLog=True,
    )
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    
    # --- Initialize components for Routine "show_text" ---
    sentence = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0.1, -0.1), draggable=False,      letterHeight=0.07,
         size=(1.4, 2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='sentence',
         depth=0, autoLog=True,
    )
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "question" ---
    question_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0.3), draggable=False,      letterHeight=0.05,
         size=(2.6, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='top-center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='question_2',
         depth=0, autoLog=True,
    )
    textbox_2 = visual.TextBox2(
         win, text='', placeholder=None, font='Georgia',
         ori=0.0, pos=(0, 0.05), draggable=False, units='height',     letterHeight=0.07,
         size=(1.7, 1), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_2',
         depth=-1, autoLog=True,
    )
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "btw2" ---
    textbox_4 = visual.TextBox2(
         win, text='Нажмите ПРОБЕЛ для перехода к следующему предложению', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.07,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_4',
         depth=0, autoLog=True,
    )
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    
    # --- Initialize components for Routine "show_final" ---
    textbox_7 = visual.TextBox2(
         win, text='Нажмите Y, если ДА, или N, если НЕТ.', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0.3), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_7',
         depth=0, autoLog=True,
    )
    textbox_6 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.3), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_6',
         depth=-1, autoLog=True,
    )
    key_resp_9 = keyboard.Keyboard(deviceName='key_resp_9')
    
    # --- Initialize components for Routine "end" ---
    endtxt = visual.TextBox2(
         win, text='Конец тестирования.\n\nБлагодарим за участие!', placeholder='Type here...', font='Georgia',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.06,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='endtxt',
         depth=0, autoLog=True,
    )
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "intro" ---
    # create an object to store info about Routine intro
    intro = data.Routine(
        name='intro',
        components=[introtxt, start_resp],
    )
    intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    introtxt.reset()
    # create starting attributes for start_resp
    start_resp.keys = []
    start_resp.rt = []
    _start_resp_allKeys = []
    # store start times for intro
    intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    intro.tStart = globalClock.getTime(format='float')
    intro.status = STARTED
    thisExp.addData('intro.started', intro.tStart)
    intro.maxDuration = None
    # keep track of which components have finished
    introComponents = intro.components
    for thisComponent in intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro" ---
    intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *introtxt* updates
        
        # if introtxt is starting this frame...
        if introtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            introtxt.frameNStart = frameN  # exact frame index
            introtxt.tStart = t  # local t and not account for scr refresh
            introtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(introtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'introtxt.started')
            # update status
            introtxt.status = STARTED
            introtxt.setAutoDraw(True)
        
        # if introtxt is active this frame...
        if introtxt.status == STARTED:
            # update params
            pass
        
        # *start_resp* updates
        waitOnFlip = False
        
        # if start_resp is starting this frame...
        if start_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_resp.frameNStart = frameN  # exact frame index
            start_resp.tStart = t  # local t and not account for scr refresh
            start_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_resp.started')
            # update status
            start_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_resp.status == STARTED and not waitOnFlip:
            theseKeys = start_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _start_resp_allKeys.extend(theseKeys)
            if len(_start_resp_allKeys):
                start_resp.keys = _start_resp_allKeys[-1].name  # just the last key pressed
                start_resp.rt = _start_resp_allKeys[-1].rt
                start_resp.duration = _start_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for intro
    intro.tStop = globalClock.getTime(format='float')
    intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('intro.stopped', intro.tStop)
    # check responses
    if start_resp.keys in ['', [], None]:  # No response was made
        start_resp.keys = None
    thisExp.addData('start_resp.keys',start_resp.keys)
    if start_resp.keys != None:  # we had a response
        thisExp.addData('start_resp.rt', start_resp.rt)
        thisExp.addData('start_resp.duration', start_resp.duration)
    thisExp.nextEntry()
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_test = data.TrialHandler2(
        name='trials_test',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('spreadsheets/test/test_paths.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_test)  # add the loop to the experiment
    thisTrials_test = trials_test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
    if thisTrials_test != None:
        for paramName in thisTrials_test:
            globals()[paramName] = thisTrials_test[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_test in trials_test:
        currentLoop = trials_test
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
        if thisTrials_test != None:
            for paramName in thisTrials_test:
                globals()[paramName] = thisTrials_test[paramName]
        
        # set up handler to look after randomisation of conditions etc
        sentence_loop_test = data.TrialHandler2(
            name='sentence_loop_test',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(file_path), 
            seed=None, 
        )
        thisExp.addLoop(sentence_loop_test)  # add the loop to the experiment
        thisSentence_loop_test = sentence_loop_test.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop_test.rgb)
        if thisSentence_loop_test != None:
            for paramName in thisSentence_loop_test:
                globals()[paramName] = thisSentence_loop_test[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSentence_loop_test in sentence_loop_test:
            currentLoop = sentence_loop_test
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop_test.rgb)
            if thisSentence_loop_test != None:
                for paramName in thisSentence_loop_test:
                    globals()[paramName] = thisSentence_loop_test[paramName]
            
            # --- Prepare to start Routine "test" ---
            # create an object to store info about Routine test
            test = data.Routine(
                name='test',
                components=[textbox, key_resp_5],
            )
            test.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textbox.reset()
            textbox.setText(masked_segment)
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # store start times for test
            test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            test.tStart = globalClock.getTime(format='float')
            test.status = STARTED
            thisExp.addData('test.started', test.tStart)
            test.maxDuration = None
            # keep track of which components have finished
            testComponents = test.components
            for thisComponent in test.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "test" ---
            # if trial has changed, end Routine now
            if isinstance(sentence_loop_test, data.TrialHandler2) and thisSentence_loop_test.thisN != sentence_loop_test.thisTrial.thisN:
                continueRoutine = False
            test.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textbox* updates
                
                # if textbox is starting this frame...
                if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox.frameNStart = frameN  # exact frame index
                    textbox.tStart = t  # local t and not account for scr refresh
                    textbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox.started')
                    # update status
                    textbox.status = STARTED
                    textbox.setAutoDraw(True)
                
                # if textbox is active this frame...
                if textbox.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                        key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    test.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "test" ---
            for thisComponent in test.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for test
            test.tStop = globalClock.getTime(format='float')
            test.tStopRefresh = tThisFlipGlobal
            thisExp.addData('test.stopped', test.tStop)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            sentence_loop_test.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                sentence_loop_test.addData('key_resp_5.rt', key_resp_5.rt)
                sentence_loop_test.addData('key_resp_5.duration', key_resp_5.duration)
            # the Routine "test" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'sentence_loop_test'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # get names of stimulus parameters
        if sentence_loop_test.trialList in ([], [None], None):
            params = []
        else:
            params = sentence_loop_test.trialList[0].keys()
        # save data for this loop
        sentence_loop_test.saveAsExcel(filename + '.xlsx', sheetName='sentence_loop_test',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        sentence_loop_test.saveAsText(filename + 'sentence_loop_test.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        question_loop_test = data.TrialHandler2(
            name='question_loop_test',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            file_path, 
            selection='0'
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(question_loop_test)  # add the loop to the experiment
        thisQuestion_loop_test = question_loop_test.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop_test.rgb)
        if thisQuestion_loop_test != None:
            for paramName in thisQuestion_loop_test:
                globals()[paramName] = thisQuestion_loop_test[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisQuestion_loop_test in question_loop_test:
            currentLoop = question_loop_test
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop_test.rgb)
            if thisQuestion_loop_test != None:
                for paramName in thisQuestion_loop_test:
                    globals()[paramName] = thisQuestion_loop_test[paramName]
            
            # --- Prepare to start Routine "question_test" ---
            # create an object to store info about Routine question_test
            question_test = data.Routine(
                name='question_test',
                components=[q, textbox_3, key_resp_6],
            )
            question_test.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            q.reset()
            textbox_3.reset()
            textbox_3.setText(question_text)
            # create starting attributes for key_resp_6
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # store start times for question_test
            question_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            question_test.tStart = globalClock.getTime(format='float')
            question_test.status = STARTED
            thisExp.addData('question_test.started', question_test.tStart)
            question_test.maxDuration = None
            # keep track of which components have finished
            question_testComponents = question_test.components
            for thisComponent in question_test.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "question_test" ---
            # if trial has changed, end Routine now
            if isinstance(question_loop_test, data.TrialHandler2) and thisQuestion_loop_test.thisN != question_loop_test.thisTrial.thisN:
                continueRoutine = False
            question_test.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *q* updates
                
                # if q is starting this frame...
                if q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    q.frameNStart = frameN  # exact frame index
                    q.tStart = t  # local t and not account for scr refresh
                    q.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(q, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'q.started')
                    # update status
                    q.status = STARTED
                    q.setAutoDraw(True)
                
                # if q is active this frame...
                if q.status == STARTED:
                    # update params
                    pass
                
                # *textbox_3* updates
                
                # if textbox_3 is starting this frame...
                if textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_3.frameNStart = frameN  # exact frame index
                    textbox_3.tStart = t  # local t and not account for scr refresh
                    textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_3.started')
                    # update status
                    textbox_3.status = STARTED
                    textbox_3.setAutoDraw(True)
                
                # if textbox_3 is active this frame...
                if textbox_3.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_6* updates
                waitOnFlip = False
                
                # if key_resp_6 is starting this frame...
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.started')
                    # update status
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                        key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                        key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    question_test.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in question_test.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "question_test" ---
            for thisComponent in question_test.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for question_test
            question_test.tStop = globalClock.getTime(format='float')
            question_test.tStopRefresh = tThisFlipGlobal
            thisExp.addData('question_test.stopped', question_test.tStop)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            question_loop_test.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                question_loop_test.addData('key_resp_6.rt', key_resp_6.rt)
                question_loop_test.addData('key_resp_6.duration', key_resp_6.duration)
            # the Routine "question_test" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'question_loop_test'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # get names of stimulus parameters
        if question_loop_test.trialList in ([], [None], None):
            params = []
        else:
            params = question_loop_test.trialList[0].keys()
        # save data for this loop
        question_loop_test.saveAsExcel(filename + '.xlsx', sheetName='question_loop_test',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        question_loop_test.saveAsText(filename + 'question_loop_test.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "btw2" ---
        # create an object to store info about Routine btw2
        btw2 = data.Routine(
            name='btw2',
            components=[textbox_4, key_resp_7],
        )
        btw2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox_4.reset()
        # create starting attributes for key_resp_7
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # store start times for btw2
        btw2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        btw2.tStart = globalClock.getTime(format='float')
        btw2.status = STARTED
        thisExp.addData('btw2.started', btw2.tStart)
        btw2.maxDuration = None
        # keep track of which components have finished
        btw2Components = btw2.components
        for thisComponent in btw2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "btw2" ---
        # if trial has changed, end Routine now
        if isinstance(trials_test, data.TrialHandler2) and thisTrials_test.thisN != trials_test.thisTrial.thisN:
            continueRoutine = False
        btw2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textbox_4* updates
            
            # if textbox_4 is starting this frame...
            if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_4.frameNStart = frameN  # exact frame index
                textbox_4.tStart = t  # local t and not account for scr refresh
                textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_4.started')
                # update status
                textbox_4.status = STARTED
                textbox_4.setAutoDraw(True)
            
            # if textbox_4 is active this frame...
            if textbox_4.status == STARTED:
                # update params
                pass
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                btw2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in btw2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "btw2" ---
        for thisComponent in btw2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for btw2
        btw2.tStop = globalClock.getTime(format='float')
        btw2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('btw2.stopped', btw2.tStop)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_test.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_test.addData('key_resp_7.rt', key_resp_7.rt)
            trials_test.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "btw2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_test'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_test.trialList in ([], [None], None):
        params = []
    else:
        params = trials_test.trialList[0].keys()
    # save data for this loop
    trials_test.saveAsExcel(filename + '.xlsx', sheetName='trials_test',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_test.saveAsText(filename + 'trials_test.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "btw" ---
    # create an object to store info about Routine btw
    btw = data.Routine(
        name='btw',
        components=[textbox_5, key_resp_8],
    )
    btw.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox_5.reset()
    # create starting attributes for key_resp_8
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # store start times for btw
    btw.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    btw.tStart = globalClock.getTime(format='float')
    btw.status = STARTED
    thisExp.addData('btw.started', btw.tStart)
    btw.maxDuration = None
    # keep track of which components have finished
    btwComponents = btw.components
    for thisComponent in btw.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "btw" ---
    btw.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_5* updates
        
        # if textbox_5 is starting this frame...
        if textbox_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_5.frameNStart = frameN  # exact frame index
            textbox_5.tStart = t  # local t and not account for scr refresh
            textbox_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_5.started')
            # update status
            textbox_5.status = STARTED
            textbox_5.setAutoDraw(True)
        
        # if textbox_5 is active this frame...
        if textbox_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_8* updates
        waitOnFlip = False
        
        # if key_resp_8 is starting this frame...
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            # update status
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            btw.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in btw.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "btw" ---
    for thisComponent in btw.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for btw
    btw.tStop = globalClock.getTime(format='float')
    btw.tStopRefresh = tThisFlipGlobal
    thisExp.addData('btw.stopped', btw.tStop)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    thisExp.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        thisExp.addData('key_resp_8.rt', key_resp_8.rt)
        thisExp.addData('key_resp_8.duration', key_resp_8.duration)
    thisExp.nextEntry()
    # the Routine "btw" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    group1 = data.TrialHandler2(
        name='group1',
        nReps=group1_trials_reps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(group1)  # add the loop to the experiment
    thisGroup1 = group1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGroup1.rgb)
    if thisGroup1 != None:
        for paramName in thisGroup1:
            globals()[paramName] = thisGroup1[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisGroup1 in group1:
        currentLoop = group1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisGroup1.rgb)
        if thisGroup1 != None:
            for paramName in thisGroup1:
                globals()[paramName] = thisGroup1[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('spreadsheets/group1_paths.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # set up handler to look after randomisation of conditions etc
            sentence_loop = data.TrialHandler2(
                name='sentence_loop',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(this_file), 
                seed=None, 
            )
            thisExp.addLoop(sentence_loop)  # add the loop to the experiment
            thisSentence_loop = sentence_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop.rgb)
            if thisSentence_loop != None:
                for paramName in thisSentence_loop:
                    globals()[paramName] = thisSentence_loop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisSentence_loop in sentence_loop:
                currentLoop = sentence_loop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop.rgb)
                if thisSentence_loop != None:
                    for paramName in thisSentence_loop:
                        globals()[paramName] = thisSentence_loop[paramName]
                
                # --- Prepare to start Routine "show_text" ---
                # create an object to store info about Routine show_text
                show_text = data.Routine(
                    name='show_text',
                    components=[sentence, key_resp],
                )
                show_text.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                sentence.reset()
                sentence.setText(masked_segment)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for show_text
                show_text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                show_text.tStart = globalClock.getTime(format='float')
                show_text.status = STARTED
                thisExp.addData('show_text.started', show_text.tStart)
                show_text.maxDuration = None
                # keep track of which components have finished
                show_textComponents = show_text.components
                for thisComponent in show_text.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "show_text" ---
                # if trial has changed, end Routine now
                if isinstance(sentence_loop, data.TrialHandler2) and thisSentence_loop.thisN != sentence_loop.thisTrial.thisN:
                    continueRoutine = False
                show_text.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *sentence* updates
                    
                    # if sentence is starting this frame...
                    if sentence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        sentence.frameNStart = frameN  # exact frame index
                        sentence.tStart = t  # local t and not account for scr refresh
                        sentence.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(sentence, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sentence.started')
                        # update status
                        sentence.status = STARTED
                        sentence.setAutoDraw(True)
                    
                    # if sentence is active this frame...
                    if sentence.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                            key_resp.rt = _key_resp_allKeys[-1].rt
                            key_resp.duration = _key_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        show_text.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in show_text.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "show_text" ---
                for thisComponent in show_text.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for show_text
                show_text.tStop = globalClock.getTime(format='float')
                show_text.tStopRefresh = tThisFlipGlobal
                thisExp.addData('show_text.stopped', show_text.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                sentence_loop.addData('key_resp.keys',key_resp.keys)
                if key_resp.keys != None:  # we had a response
                    sentence_loop.addData('key_resp.rt', key_resp.rt)
                    sentence_loop.addData('key_resp.duration', key_resp.duration)
                # the Routine "show_text" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'sentence_loop'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # get names of stimulus parameters
            if sentence_loop.trialList in ([], [None], None):
                params = []
            else:
                params = sentence_loop.trialList[0].keys()
            # save data for this loop
            sentence_loop.saveAsExcel(filename + '.xlsx', sheetName='sentence_loop',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            sentence_loop.saveAsText(filename + 'sentence_loop.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            question_loop = data.TrialHandler2(
                name='question_loop',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                this_file, 
                selection='0'
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(question_loop)  # add the loop to the experiment
            thisQuestion_loop = question_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop.rgb)
            if thisQuestion_loop != None:
                for paramName in thisQuestion_loop:
                    globals()[paramName] = thisQuestion_loop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisQuestion_loop in question_loop:
                currentLoop = question_loop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop.rgb)
                if thisQuestion_loop != None:
                    for paramName in thisQuestion_loop:
                        globals()[paramName] = thisQuestion_loop[paramName]
                
                # --- Prepare to start Routine "question" ---
                # create an object to store info about Routine question
                question = data.Routine(
                    name='question',
                    components=[question_2, textbox_2, key_resp_4],
                )
                question.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                question_2.reset()
                question_2.setText('Ответьте на вопрос, нажав Y (ДА) или N (НЕТ)')
                textbox_2.reset()
                textbox_2.setText(question_text)
                # create starting attributes for key_resp_4
                key_resp_4.keys = []
                key_resp_4.rt = []
                _key_resp_4_allKeys = []
                # store start times for question
                question.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                question.tStart = globalClock.getTime(format='float')
                question.status = STARTED
                thisExp.addData('question.started', question.tStart)
                question.maxDuration = None
                # keep track of which components have finished
                questionComponents = question.components
                for thisComponent in question.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "question" ---
                # if trial has changed, end Routine now
                if isinstance(question_loop, data.TrialHandler2) and thisQuestion_loop.thisN != question_loop.thisTrial.thisN:
                    continueRoutine = False
                question.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *question_2* updates
                    
                    # if question_2 is starting this frame...
                    if question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        question_2.frameNStart = frameN  # exact frame index
                        question_2.tStart = t  # local t and not account for scr refresh
                        question_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(question_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'question_2.started')
                        # update status
                        question_2.status = STARTED
                        question_2.setAutoDraw(True)
                    
                    # if question_2 is active this frame...
                    if question_2.status == STARTED:
                        # update params
                        pass
                    
                    # *textbox_2* updates
                    
                    # if textbox_2 is starting this frame...
                    if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textbox_2.frameNStart = frameN  # exact frame index
                        textbox_2.tStart = t  # local t and not account for scr refresh
                        textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_2.started')
                        # update status
                        textbox_2.status = STARTED
                        textbox_2.setAutoDraw(True)
                    
                    # if textbox_2 is active this frame...
                    if textbox_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_4* updates
                    waitOnFlip = False
                    
                    # if key_resp_4 is starting this frame...
                    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_4.frameNStart = frameN  # exact frame index
                        key_resp_4.tStart = t  # local t and not account for scr refresh
                        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.started')
                        # update status
                        key_resp_4.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_4.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_4.getKeys(keyList=['y', 'n'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_4_allKeys.extend(theseKeys)
                        if len(_key_resp_4_allKeys):
                            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                            key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        question.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in question.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "question" ---
                for thisComponent in question.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for question
                question.tStop = globalClock.getTime(format='float')
                question.tStopRefresh = tThisFlipGlobal
                thisExp.addData('question.stopped', question.tStop)
                # check responses
                if key_resp_4.keys in ['', [], None]:  # No response was made
                    key_resp_4.keys = None
                question_loop.addData('key_resp_4.keys',key_resp_4.keys)
                if key_resp_4.keys != None:  # we had a response
                    question_loop.addData('key_resp_4.rt', key_resp_4.rt)
                    question_loop.addData('key_resp_4.duration', key_resp_4.duration)
                # the Routine "question" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'question_loop'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # get names of stimulus parameters
            if question_loop.trialList in ([], [None], None):
                params = []
            else:
                params = question_loop.trialList[0].keys()
            # save data for this loop
            question_loop.saveAsExcel(filename + '.xlsx', sheetName='question_loop',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            question_loop.saveAsText(filename + 'question_loop.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # --- Prepare to start Routine "btw2" ---
            # create an object to store info about Routine btw2
            btw2 = data.Routine(
                name='btw2',
                components=[textbox_4, key_resp_7],
            )
            btw2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textbox_4.reset()
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for btw2
            btw2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            btw2.tStart = globalClock.getTime(format='float')
            btw2.status = STARTED
            thisExp.addData('btw2.started', btw2.tStart)
            btw2.maxDuration = None
            # keep track of which components have finished
            btw2Components = btw2.components
            for thisComponent in btw2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "btw2" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            btw2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textbox_4* updates
                
                # if textbox_4 is starting this frame...
                if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_4.frameNStart = frameN  # exact frame index
                    textbox_4.tStart = t  # local t and not account for scr refresh
                    textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_4.started')
                    # update status
                    textbox_4.status = STARTED
                    textbox_4.setAutoDraw(True)
                
                # if textbox_4 is active this frame...
                if textbox_4.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                        key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                        key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    btw2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in btw2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "btw2" ---
            for thisComponent in btw2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for btw2
            btw2.tStop = globalClock.getTime(format='float')
            btw2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('btw2.stopped', btw2.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            trials.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                trials.addData('key_resp_7.rt', key_resp_7.rt)
                trials.addData('key_resp_7.duration', key_resp_7.duration)
            # the Routine "btw2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # get names of stimulus parameters
        if trials.trialList in ([], [None], None):
            params = []
        else:
            params = trials.trialList[0].keys()
        # save data for this loop
        trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials.saveAsText(filename + 'trials.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed group1_trials_reps repeats of 'group1'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if group1.trialList in ([], [None], None):
        params = []
    else:
        params = group1.trialList[0].keys()
    # save data for this loop
    group1.saveAsExcel(filename + '.xlsx', sheetName='group1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    group1.saveAsText(filename + 'group1.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    group2 = data.TrialHandler2(
        name='group2',
        nReps=group2_trials_reps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(group2)  # add the loop to the experiment
    thisGroup2 = group2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGroup2.rgb)
    if thisGroup2 != None:
        for paramName in thisGroup2:
            globals()[paramName] = thisGroup2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisGroup2 in group2:
        currentLoop = group2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisGroup2.rgb)
        if thisGroup2 != None:
            for paramName in thisGroup2:
                globals()[paramName] = thisGroup2[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('spreadsheets/group2_paths.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # set up handler to look after randomisation of conditions etc
            sentence_loop_2 = data.TrialHandler2(
                name='sentence_loop_2',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(this_file), 
                seed=None, 
            )
            thisExp.addLoop(sentence_loop_2)  # add the loop to the experiment
            thisSentence_loop_2 = sentence_loop_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop_2.rgb)
            if thisSentence_loop_2 != None:
                for paramName in thisSentence_loop_2:
                    globals()[paramName] = thisSentence_loop_2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisSentence_loop_2 in sentence_loop_2:
                currentLoop = sentence_loop_2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisSentence_loop_2.rgb)
                if thisSentence_loop_2 != None:
                    for paramName in thisSentence_loop_2:
                        globals()[paramName] = thisSentence_loop_2[paramName]
                
                # --- Prepare to start Routine "show_text" ---
                # create an object to store info about Routine show_text
                show_text = data.Routine(
                    name='show_text',
                    components=[sentence, key_resp],
                )
                show_text.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                sentence.reset()
                sentence.setText(masked_segment)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for show_text
                show_text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                show_text.tStart = globalClock.getTime(format='float')
                show_text.status = STARTED
                thisExp.addData('show_text.started', show_text.tStart)
                show_text.maxDuration = None
                # keep track of which components have finished
                show_textComponents = show_text.components
                for thisComponent in show_text.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "show_text" ---
                # if trial has changed, end Routine now
                if isinstance(sentence_loop_2, data.TrialHandler2) and thisSentence_loop_2.thisN != sentence_loop_2.thisTrial.thisN:
                    continueRoutine = False
                show_text.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *sentence* updates
                    
                    # if sentence is starting this frame...
                    if sentence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        sentence.frameNStart = frameN  # exact frame index
                        sentence.tStart = t  # local t and not account for scr refresh
                        sentence.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(sentence, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sentence.started')
                        # update status
                        sentence.status = STARTED
                        sentence.setAutoDraw(True)
                    
                    # if sentence is active this frame...
                    if sentence.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                            key_resp.rt = _key_resp_allKeys[-1].rt
                            key_resp.duration = _key_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        show_text.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in show_text.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "show_text" ---
                for thisComponent in show_text.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for show_text
                show_text.tStop = globalClock.getTime(format='float')
                show_text.tStopRefresh = tThisFlipGlobal
                thisExp.addData('show_text.stopped', show_text.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                sentence_loop_2.addData('key_resp.keys',key_resp.keys)
                if key_resp.keys != None:  # we had a response
                    sentence_loop_2.addData('key_resp.rt', key_resp.rt)
                    sentence_loop_2.addData('key_resp.duration', key_resp.duration)
                # the Routine "show_text" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'sentence_loop_2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # get names of stimulus parameters
            if sentence_loop_2.trialList in ([], [None], None):
                params = []
            else:
                params = sentence_loop_2.trialList[0].keys()
            # save data for this loop
            sentence_loop_2.saveAsExcel(filename + '.xlsx', sheetName='sentence_loop_2',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            sentence_loop_2.saveAsText(filename + 'sentence_loop_2.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            question_loop_2 = data.TrialHandler2(
                name='question_loop_2',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                this_file, 
                selection='0'
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(question_loop_2)  # add the loop to the experiment
            thisQuestion_loop_2 = question_loop_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop_2.rgb)
            if thisQuestion_loop_2 != None:
                for paramName in thisQuestion_loop_2:
                    globals()[paramName] = thisQuestion_loop_2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisQuestion_loop_2 in question_loop_2:
                currentLoop = question_loop_2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop_2.rgb)
                if thisQuestion_loop_2 != None:
                    for paramName in thisQuestion_loop_2:
                        globals()[paramName] = thisQuestion_loop_2[paramName]
                
                # --- Prepare to start Routine "question" ---
                # create an object to store info about Routine question
                question = data.Routine(
                    name='question',
                    components=[question_2, textbox_2, key_resp_4],
                )
                question.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                question_2.reset()
                question_2.setText('Ответьте на вопрос, нажав Y (ДА) или N (НЕТ)')
                textbox_2.reset()
                textbox_2.setText(question_text)
                # create starting attributes for key_resp_4
                key_resp_4.keys = []
                key_resp_4.rt = []
                _key_resp_4_allKeys = []
                # store start times for question
                question.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                question.tStart = globalClock.getTime(format='float')
                question.status = STARTED
                thisExp.addData('question.started', question.tStart)
                question.maxDuration = None
                # keep track of which components have finished
                questionComponents = question.components
                for thisComponent in question.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "question" ---
                # if trial has changed, end Routine now
                if isinstance(question_loop_2, data.TrialHandler2) and thisQuestion_loop_2.thisN != question_loop_2.thisTrial.thisN:
                    continueRoutine = False
                question.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *question_2* updates
                    
                    # if question_2 is starting this frame...
                    if question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        question_2.frameNStart = frameN  # exact frame index
                        question_2.tStart = t  # local t and not account for scr refresh
                        question_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(question_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'question_2.started')
                        # update status
                        question_2.status = STARTED
                        question_2.setAutoDraw(True)
                    
                    # if question_2 is active this frame...
                    if question_2.status == STARTED:
                        # update params
                        pass
                    
                    # *textbox_2* updates
                    
                    # if textbox_2 is starting this frame...
                    if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textbox_2.frameNStart = frameN  # exact frame index
                        textbox_2.tStart = t  # local t and not account for scr refresh
                        textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_2.started')
                        # update status
                        textbox_2.status = STARTED
                        textbox_2.setAutoDraw(True)
                    
                    # if textbox_2 is active this frame...
                    if textbox_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_4* updates
                    waitOnFlip = False
                    
                    # if key_resp_4 is starting this frame...
                    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_4.frameNStart = frameN  # exact frame index
                        key_resp_4.tStart = t  # local t and not account for scr refresh
                        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.started')
                        # update status
                        key_resp_4.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_4.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_4.getKeys(keyList=['y', 'n'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_4_allKeys.extend(theseKeys)
                        if len(_key_resp_4_allKeys):
                            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                            key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        question.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in question.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "question" ---
                for thisComponent in question.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for question
                question.tStop = globalClock.getTime(format='float')
                question.tStopRefresh = tThisFlipGlobal
                thisExp.addData('question.stopped', question.tStop)
                # check responses
                if key_resp_4.keys in ['', [], None]:  # No response was made
                    key_resp_4.keys = None
                question_loop_2.addData('key_resp_4.keys',key_resp_4.keys)
                if key_resp_4.keys != None:  # we had a response
                    question_loop_2.addData('key_resp_4.rt', key_resp_4.rt)
                    question_loop_2.addData('key_resp_4.duration', key_resp_4.duration)
                # the Routine "question" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'question_loop_2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # get names of stimulus parameters
            if question_loop_2.trialList in ([], [None], None):
                params = []
            else:
                params = question_loop_2.trialList[0].keys()
            # save data for this loop
            question_loop_2.saveAsExcel(filename + '.xlsx', sheetName='question_loop_2',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            question_loop_2.saveAsText(filename + 'question_loop_2.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # --- Prepare to start Routine "btw2" ---
            # create an object to store info about Routine btw2
            btw2 = data.Routine(
                name='btw2',
                components=[textbox_4, key_resp_7],
            )
            btw2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textbox_4.reset()
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for btw2
            btw2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            btw2.tStart = globalClock.getTime(format='float')
            btw2.status = STARTED
            thisExp.addData('btw2.started', btw2.tStart)
            btw2.maxDuration = None
            # keep track of which components have finished
            btw2Components = btw2.components
            for thisComponent in btw2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "btw2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            btw2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textbox_4* updates
                
                # if textbox_4 is starting this frame...
                if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_4.frameNStart = frameN  # exact frame index
                    textbox_4.tStart = t  # local t and not account for scr refresh
                    textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_4.started')
                    # update status
                    textbox_4.status = STARTED
                    textbox_4.setAutoDraw(True)
                
                # if textbox_4 is active this frame...
                if textbox_4.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                        key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                        key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    btw2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in btw2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "btw2" ---
            for thisComponent in btw2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for btw2
            btw2.tStop = globalClock.getTime(format='float')
            btw2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('btw2.stopped', btw2.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            trials_2.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                trials_2.addData('key_resp_7.rt', key_resp_7.rt)
                trials_2.addData('key_resp_7.duration', key_resp_7.duration)
            # the Routine "btw2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # get names of stimulus parameters
        if trials_2.trialList in ([], [None], None):
            params = []
        else:
            params = trials_2.trialList[0].keys()
        # save data for this loop
        trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed group2_trials_reps repeats of 'group2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if group2.trialList in ([], [None], None):
        params = []
    else:
        params = group2.trialList[0].keys()
    # save data for this loop
    group2.saveAsExcel(filename + '.xlsx', sheetName='group2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    group2.saveAsText(filename + 'group2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler2(
        name='trials_3',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('spreadsheets/idiom_test.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "show_final" ---
        # create an object to store info about Routine show_final
        show_final = data.Routine(
            name='show_final',
            components=[textbox_7, textbox_6, key_resp_9],
        )
        show_final.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox_7.reset()
        textbox_6.reset()
        textbox_6.setText(idiom_question)
        # create starting attributes for key_resp_9
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # store start times for show_final
        show_final.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        show_final.tStart = globalClock.getTime(format='float')
        show_final.status = STARTED
        thisExp.addData('show_final.started', show_final.tStart)
        show_final.maxDuration = None
        # keep track of which components have finished
        show_finalComponents = show_final.components
        for thisComponent in show_final.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "show_final" ---
        # if trial has changed, end Routine now
        if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
            continueRoutine = False
        show_final.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textbox_7* updates
            
            # if textbox_7 is starting this frame...
            if textbox_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_7.frameNStart = frameN  # exact frame index
                textbox_7.tStart = t  # local t and not account for scr refresh
                textbox_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_7.started')
                # update status
                textbox_7.status = STARTED
                textbox_7.setAutoDraw(True)
            
            # if textbox_7 is active this frame...
            if textbox_7.status == STARTED:
                # update params
                pass
            
            # *textbox_6* updates
            
            # if textbox_6 is starting this frame...
            if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_6.frameNStart = frameN  # exact frame index
                textbox_6.tStart = t  # local t and not account for scr refresh
                textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_6.started')
                # update status
                textbox_6.status = STARTED
                textbox_6.setAutoDraw(True)
            
            # if textbox_6 is active this frame...
            if textbox_6.status == STARTED:
                # update params
                pass
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                show_final.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in show_final.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "show_final" ---
        for thisComponent in show_final.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for show_final
        show_final.tStop = globalClock.getTime(format='float')
        show_final.tStopRefresh = tThisFlipGlobal
        thisExp.addData('show_final.stopped', show_final.tStop)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        trials_3.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            trials_3.addData('key_resp_9.rt', key_resp_9.rt)
            trials_3.addData('key_resp_9.duration', key_resp_9.duration)
        # the Routine "show_final" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_3'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_3.trialList[0].keys()
    # save data for this loop
    trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[endtxt],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    endtxt.reset()
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endtxt* updates
        
        # if endtxt is starting this frame...
        if endtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endtxt.frameNStart = frameN  # exact frame index
            endtxt.tStart = t  # local t and not account for scr refresh
            endtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endtxt.started')
            # update status
            endtxt.status = STARTED
            endtxt.setAutoDraw(True)
        
        # if endtxt is active this frame...
        if endtxt.status == STARTED:
            # update params
            pass
        
        # if endtxt is stopping this frame...
        if endtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endtxt.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                endtxt.tStop = t  # not accounting for scr refresh
                endtxt.tStopRefresh = tThisFlipGlobal  # on global time
                endtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endtxt.stopped')
                # update status
                endtxt.status = FINISHED
                endtxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end.maxDurationReached:
        routineTimer.addTime(-end.maxDuration)
    elif end.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='semicolon')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
