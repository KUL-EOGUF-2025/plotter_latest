/*************************************** 
 * Mental Fatigue Testing Session Test *
 ***************************************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Mental Fatigue Testing Session';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'age (years)': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrBRUMSpreRoutineBegin());
flowScheduler.add(instrBRUMSpreRoutineEachFrame());
flowScheduler.add(instrBRUMSpreRoutineEnd());
flowScheduler.add(BRUMS_1RoutineBegin());
flowScheduler.add(BRUMS_1RoutineEachFrame());
flowScheduler.add(BRUMS_1RoutineEnd());
flowScheduler.add(BRUMS_2RoutineBegin());
flowScheduler.add(BRUMS_2RoutineEachFrame());
flowScheduler.add(BRUMS_2RoutineEnd());
flowScheduler.add(BRUMS_3RoutineBegin());
flowScheduler.add(BRUMS_3RoutineEachFrame());
flowScheduler.add(BRUMS_3RoutineEnd());
flowScheduler.add(instrAXCPTbreak1RoutineBegin());
flowScheduler.add(instrAXCPTbreak1RoutineEachFrame());
flowScheduler.add(instrAXCPTbreak1RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const AXCPTtrialsLoop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AXCPTtrialsLoop1LoopBegin, AXCPTtrialsLoop1LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop1LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop1LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrNBACKbreak2RoutineBegin());
flowScheduler.add(instrNBACKbreak2RoutineEachFrame());
flowScheduler.add(instrNBACKbreak2RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const NBackTargetLoop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTargetLoop1LoopBegin, NBackTargetLoop1LoopScheduler);
flowScheduler.add(NBackTargetLoop1LoopScheduler);
flowScheduler.add(NBackTargetLoop1LoopEnd);
const NBackTrialsLoop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTrialsLoop1LoopBegin, NBackTrialsLoop1LoopScheduler);
flowScheduler.add(NBackTrialsLoop1LoopScheduler);
flowScheduler.add(NBackTrialsLoop1LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrSEARCHbreak3RoutineBegin());
flowScheduler.add(instrSEARCHbreak3RoutineEachFrame());
flowScheduler.add(instrSEARCHbreak3RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const searchLoop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(searchLoop1LoopBegin, searchLoop1LoopScheduler);
flowScheduler.add(searchLoop1LoopScheduler);
flowScheduler.add(searchLoop1LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrMENTROTbreak4RoutineBegin());
flowScheduler.add(instrMENTROTbreak4RoutineEachFrame());
flowScheduler.add(instrMENTROTbreak4RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const mentRotTrialsLoop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mentRotTrialsLoop1LoopBegin, mentRotTrialsLoop1LoopScheduler);
flowScheduler.add(mentRotTrialsLoop1LoopScheduler);
flowScheduler.add(mentRotTrialsLoop1LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrNBACKbreak5RoutineBegin());
flowScheduler.add(instrNBACKbreak5RoutineEachFrame());
flowScheduler.add(instrNBACKbreak5RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const NBackTargetLOOP2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTargetLOOP2LoopBegin, NBackTargetLOOP2LoopScheduler);
flowScheduler.add(NBackTargetLOOP2LoopScheduler);
flowScheduler.add(NBackTargetLOOP2LoopEnd);
const NBackTrialsLoop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTrialsLoop2LoopBegin, NBackTrialsLoop2LoopScheduler);
flowScheduler.add(NBackTrialsLoop2LoopScheduler);
flowScheduler.add(NBackTrialsLoop2LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrAXCPTbreak6RoutineBegin());
flowScheduler.add(instrAXCPTbreak6RoutineEachFrame());
flowScheduler.add(instrAXCPTbreak6RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const AXCPTtrialsLoop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AXCPTtrialsLoop2LoopBegin, AXCPTtrialsLoop2LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop2LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop2LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrSEARCHbreak7RoutineBegin());
flowScheduler.add(instrSEARCHbreak7RoutineEachFrame());
flowScheduler.add(instrSEARCHbreak7RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const searchLoop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(searchLoop2LoopBegin, searchLoop2LoopScheduler);
flowScheduler.add(searchLoop2LoopScheduler);
flowScheduler.add(searchLoop2LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrMENTROTbreak8RoutineBegin());
flowScheduler.add(instrMENTROTbreak8RoutineEachFrame());
flowScheduler.add(instrMENTROTbreak8RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const mentRotTrialsLoop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mentRotTrialsLoop2LoopBegin, mentRotTrialsLoop2LoopScheduler);
flowScheduler.add(mentRotTrialsLoop2LoopScheduler);
flowScheduler.add(mentRotTrialsLoop2LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrNBACKbreak9RoutineBegin());
flowScheduler.add(instrNBACKbreak9RoutineEachFrame());
flowScheduler.add(instrNBACKbreak9RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const NBackTargetLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTargetLoop3LoopBegin, NBackTargetLoop3LoopScheduler);
flowScheduler.add(NBackTargetLoop3LoopScheduler);
flowScheduler.add(NBackTargetLoop3LoopEnd);
const NBackTrialsLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(NBackTrialsLoop3LoopBegin, NBackTrialsLoop3LoopScheduler);
flowScheduler.add(NBackTrialsLoop3LoopScheduler);
flowScheduler.add(NBackTrialsLoop3LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrSEARCHbreak10RoutineBegin());
flowScheduler.add(instrSEARCHbreak10RoutineEachFrame());
flowScheduler.add(instrSEARCHbreak10RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const searchLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(searchLoop3LoopBegin, searchLoop3LoopScheduler);
flowScheduler.add(searchLoop3LoopScheduler);
flowScheduler.add(searchLoop3LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrMENTROTbreak11RoutineBegin());
flowScheduler.add(instrMENTROTbreak11RoutineEachFrame());
flowScheduler.add(instrMENTROTbreak11RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const mentRotTrialsLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mentRotTrialsLoop3LoopBegin, mentRotTrialsLoop3LoopScheduler);
flowScheduler.add(mentRotTrialsLoop3LoopScheduler);
flowScheduler.add(mentRotTrialsLoop3LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrAXCPTbreak12RoutineBegin());
flowScheduler.add(instrAXCPTbreak12RoutineEachFrame());
flowScheduler.add(instrAXCPTbreak12RoutineEnd());
flowScheduler.add(createLoopTimerRoutineBegin());
flowScheduler.add(createLoopTimerRoutineEachFrame());
flowScheduler.add(createLoopTimerRoutineEnd());
const AXCPTtrialsLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AXCPTtrialsLoop3LoopBegin, AXCPTtrialsLoop3LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop3LoopScheduler);
flowScheduler.add(AXCPTtrialsLoop3LoopEnd);
flowScheduler.add(F_ISARoutineBegin());
flowScheduler.add(F_ISARoutineEachFrame());
flowScheduler.add(F_ISARoutineEnd());
flowScheduler.add(instrBRUMSpostRoutineBegin());
flowScheduler.add(instrBRUMSpostRoutineEachFrame());
flowScheduler.add(instrBRUMSpostRoutineEnd());
flowScheduler.add(BRUMS_1RoutineBegin());
flowScheduler.add(BRUMS_1RoutineEachFrame());
flowScheduler.add(BRUMS_1RoutineEnd());
flowScheduler.add(BRUMS_2RoutineBegin());
flowScheduler.add(BRUMS_2RoutineEachFrame());
flowScheduler.add(BRUMS_2RoutineEnd());
flowScheduler.add(BRUMS_3RoutineBegin());
flowScheduler.add(BRUMS_3RoutineEachFrame());
flowScheduler.add(BRUMS_3RoutineEnd());
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var thisExp;
var win;
var event;
var shuffle;
var randint;
var elapsedTime;
var key_resp;
var instrHeaderText;
var text;
var F_ISAClock;
var mouse_22;
var mouse_visibility;
var Timer;
var text_4;
var slider;
var instrBRUMSpreClock;
var text_8;
var mouse_4;
var BRUMSheader;
var BRUMS_1Clock;
var mouse_3;
var mouse_visibility_fix;
var slider1;
var slider2;
var slider3;
var slider4;
var slider5;
var slider6;
var slider7;
var slider8;
var text_9;
var panicky;
var lively;
var confused;
var wornout;
var depressed;
var downheartened;
var annoyed;
var exhausted;
var BRUMS_2Clock;
var mouse_5;
var mouse_visibility_fix_2;
var slider9;
var slider10;
var slider11;
var slider12;
var slider13;
var slider14;
var slider15;
var slider16;
var text_10;
var mixedup;
var sleepy;
var bitter;
var unhappy;
var anxious;
var worried;
var energetic;
var miserable;
var BRUMS_3Clock;
var mouse_6;
var mouse_visibility_fix_3;
var slider17;
var slider18;
var slider19;
var slider20;
var slider21;
var slider22;
var slider23;
var slider24;
var text_11;
var muddled;
var nervous;
var angry;
var active;
var tired;
var badtempered;
var alert;
var uncertain;
var instrAXCPTbreak1Clock;
var key_resp_2;
var instrHeaderText_2;
var text_2;
var createLoopTimerClock;
var timerClock;
var probeVal;
var timer_text;
var AXCPTtrialClock;
var Bletters;
var Yletters;
var distractors;
var cue_text;
var break1;
var distractor1;
var break2;
var distractor2;
var break3;
var AXCPTprobeClock;
var probe_text;
var AXCPT_resp;
var AXCPTfeedbackClock;
var msg;
var AXCPTfeedback_text;
var instrNBACKbreak2Clock;
var key_resp_3;
var instrHeaderText_3;
var text_3;
var NBackFirst3TrialsClock;
var Back2minus1;
var Back2minus2;
var Back2minus3;
var NBackText_1;
var NBack_resp_1;
var NBackRemainderTrialsClock;
var NBackText_2;
var NBack_resp_2;
var NBackFeedbackClock;
var AXCPTfeedback_text_2;
var instrSEARCHbreak3Clock;
var instrHeaderText_5;
var text_5;
var key_resp_4;
var searchTrialClock;
var orientList;
var PosList;
var key_resp_14;
var targetStim;
var searchStim2;
var searchStim3;
var searchStim4;
var searchStim5;
var searchStim6;
var searchStim7;
var searchStim8;
var searchStim9;
var searchStim10;
var searchStim11;
var searchFeedbackClock;
var searchFeedbackText;
var instrMENTROTbreak4Clock;
var key_resp_13;
var instrHeaderText_15;
var text_21;
var mentRotTrialClock;
var mentRotStimulus;
var MROT_resp;
var mentRotFeedbackClock;
var NBackfeedback_text_2;
var instrNBACKbreak5Clock;
var key_resp_8;
var instrHeaderText_9;
var text_13;
var instrAXCPTbreak6Clock;
var key_resp_6;
var instrHeaderText_7;
var text_7;
var instrSEARCHbreak7Clock;
var instrHeaderText_11;
var text_15;
var key_resp_15;
var instrMENTROTbreak8Clock;
var key_resp_10;
var instrHeaderText_13;
var text_17;
var instrNBACKbreak9Clock;
var key_resp_9;
var instrHeaderText_10;
var text_14;
var instrSEARCHbreak10Clock;
var instrHeaderText_12;
var text_16;
var key_resp_5;
var instrMENTROTbreak11Clock;
var key_resp_11;
var instrHeaderText_14;
var text_18;
var instrAXCPTbreak12Clock;
var key_resp_7;
var instrHeaderText_8;
var text_12;
var instrBRUMSpostClock;
var text_19;
var mouse_9;
var BRUMSheader_2;
var endClock;
var text_20;
var key_resp_12;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  // Code to fix reference errors in JS
    thisExp = psychoJS.experiment;
    win = psychoJS.window;
    event = psychoJS.eventManager;
    Array.prototype.append = [].push;
    shuffle = util.shuffle;
    document.documentElement.style.cursor = 'none';
    
    // Math related fixes
    //pi = Math.PI;
    //sin = Math.sin;
    //cos = Math.cos;
    //sqrt = Math.sqrt;
    randint = function(min, maxplusone) {
      return Math.floor(Math.random() * (maxplusone - min) ) + min;
    }
    shuffle = util.shuffle;
    elapsedTime = new util.Clock();
    
  //  function choice(arr) {
  //    return arr[Math.floor(Math.random() * arr.length)];
  //  }
  elapsedTime = new util.Clock();
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText',
    text: 'Introduction',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -4.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the testing session\n\nBefore you begin, please make sure that you are sitting comfortably in a quiet environment where you will not be interrupted. Please also ensure that your computer is connected to a power source and will not enter sleep mode\n\nIn this session you will spend 2-3 hours repeating the tasks that you learned in the training session. There will be multiple chances for you to take rest breaks if you need to\n\nIf you decide that you do not want to continue you can press the escape key at any time to quit the experiment. If you quit, your data will not be saved\n\nBefore the tasks begin, you will complete some ratings. Please press the right arrow on your keyboard to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrBRUMSpre"
  instrBRUMSpreClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'On the next few screens there are lists of words that describe feelings people have\n\nPlease read each one carefully. Then click the answer which best describes how you feel right now\n\nMake sure you answer every question\n\nPlease press the mouse to begin\n\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_4.mouseClock = new util.Clock();
  BRUMSheader = new visual.TextStim({
    win: psychoJS.window,
    name: 'BRUMSheader',
    text: 'Rating Scale Instructions',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "BRUMS_1"
  BRUMS_1Clock = new util.Clock();
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  mouse_visibility_fix = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  slider1 = new visual.Slider({
    win: psychoJS.window, name: 'slider1',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider2 = new visual.Slider({
    win: psychoJS.window, name: 'slider2',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider3 = new visual.Slider({
    win: psychoJS.window, name: 'slider3',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider4 = new visual.Slider({
    win: psychoJS.window, name: 'slider4',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider5 = new visual.Slider({
    win: psychoJS.window, name: 'slider5',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider6 = new visual.Slider({
    win: psychoJS.window, name: 'slider6',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider7 = new visual.Slider({
    win: psychoJS.window, name: 'slider7',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider8 = new visual.Slider({
    win: psychoJS.window, name: 'slider8',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Rating Scales: Page 1 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  panicky = new visual.TextStim({
    win: psychoJS.window,
    name: 'panicky',
    text: 'Panicky',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  lively = new visual.TextStim({
    win: psychoJS.window,
    name: 'lively',
    text: 'Lively',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  confused = new visual.TextStim({
    win: psychoJS.window,
    name: 'confused',
    text: 'Confused',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  wornout = new visual.TextStim({
    win: psychoJS.window,
    name: 'wornout',
    text: 'Worn Out',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  depressed = new visual.TextStim({
    win: psychoJS.window,
    name: 'depressed',
    text: 'Depressed',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  downheartened = new visual.TextStim({
    win: psychoJS.window,
    name: 'downheartened',
    text: 'Downheartened',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  annoyed = new visual.TextStim({
    win: psychoJS.window,
    name: 'annoyed',
    text: 'Annoyed',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  exhausted = new visual.TextStim({
    win: psychoJS.window,
    name: 'exhausted',
    text: 'Exhausted',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  // Initialize components for Routine "BRUMS_2"
  BRUMS_2Clock = new util.Clock();
  mouse_5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_5.mouseClock = new util.Clock();
  mouse_visibility_fix_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix_2', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  slider9 = new visual.Slider({
    win: psychoJS.window, name: 'slider9',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider10 = new visual.Slider({
    win: psychoJS.window, name: 'slider10',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider11 = new visual.Slider({
    win: psychoJS.window, name: 'slider11',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider12 = new visual.Slider({
    win: psychoJS.window, name: 'slider12',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider13 = new visual.Slider({
    win: psychoJS.window, name: 'slider13',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider14 = new visual.Slider({
    win: psychoJS.window, name: 'slider14',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider15 = new visual.Slider({
    win: psychoJS.window, name: 'slider15',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider16 = new visual.Slider({
    win: psychoJS.window, name: 'slider16',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Rating Scales: Page 2 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  mixedup = new visual.TextStim({
    win: psychoJS.window,
    name: 'mixedup',
    text: 'Mixed-up',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  sleepy = new visual.TextStim({
    win: psychoJS.window,
    name: 'sleepy',
    text: 'Sleepy',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  bitter = new visual.TextStim({
    win: psychoJS.window,
    name: 'bitter',
    text: 'Bitter',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  unhappy = new visual.TextStim({
    win: psychoJS.window,
    name: 'unhappy',
    text: 'Unhappy',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  anxious = new visual.TextStim({
    win: psychoJS.window,
    name: 'anxious',
    text: 'Anxious',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  worried = new visual.TextStim({
    win: psychoJS.window,
    name: 'worried',
    text: 'Worried',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  energetic = new visual.TextStim({
    win: psychoJS.window,
    name: 'energetic',
    text: 'Energetic',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  miserable = new visual.TextStim({
    win: psychoJS.window,
    name: 'miserable',
    text: 'Miserable',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  // Initialize components for Routine "BRUMS_3"
  BRUMS_3Clock = new util.Clock();
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  mouse_visibility_fix_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix_3', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  slider17 = new visual.Slider({
    win: psychoJS.window, name: 'slider17',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider18 = new visual.Slider({
    win: psychoJS.window, name: 'slider18',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider19 = new visual.Slider({
    win: psychoJS.window, name: 'slider19',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider20 = new visual.Slider({
    win: psychoJS.window, name: 'slider20',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider21 = new visual.Slider({
    win: psychoJS.window, name: 'slider21',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider22 = new visual.Slider({
    win: psychoJS.window, name: 'slider22',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider23 = new visual.Slider({
    win: psychoJS.window, name: 'slider23',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider24 = new visual.Slider({
    win: psychoJS.window, name: 'slider24',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'Rating Scales: Page 3 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  muddled = new visual.TextStim({
    win: psychoJS.window,
    name: 'muddled',
    text: 'Muddled',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  nervous = new visual.TextStim({
    win: psychoJS.window,
    name: 'nervous',
    text: 'Nervous',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  angry = new visual.TextStim({
    win: psychoJS.window,
    name: 'angry',
    text: 'Angry',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  active = new visual.TextStim({
    win: psychoJS.window,
    name: 'active',
    text: 'Active',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  tired = new visual.TextStim({
    win: psychoJS.window,
    name: 'tired',
    text: 'Tired',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  badtempered = new visual.TextStim({
    win: psychoJS.window,
    name: 'badtempered',
    text: 'Bad tempered',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  alert = new visual.TextStim({
    win: psychoJS.window,
    name: 'alert',
    text: 'Alert',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  uncertain = new visual.TextStim({
    win: psychoJS.window,
    name: 'uncertain',
    text: 'Uncertain',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -20.0 
  });
  
  // Initialize components for Routine "instrAXCPTbreak1"
  instrAXCPTbreak1Clock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_2',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: "Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "AXCPTtrial"
  AXCPTtrialClock = new util.Clock();
  Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
  distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  
  cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cue_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  break1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break1',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -2.0 
  });
  
  distractor1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  break2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break2',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -4.0 
  });
  
  distractor2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  break3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break3',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -6.0 
  });
  
  // Initialize components for Routine "AXCPTprobe"
  AXCPTprobeClock = new util.Clock();
  probe_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  AXCPT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AXCPTfeedback"
  AXCPTfeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrNBACKbreak2"
  instrNBACKbreak2Clock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_3',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackFirst3Trials"
  NBackFirst3TrialsClock = new util.Clock();
  Back2minus1 = [];
  Back2minus2 = [];
  Back2minus3 = [];
  
  NBackText_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackRemainderTrials"
  NBackRemainderTrialsClock = new util.Clock();
  NBackText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NBackFeedback"
  NBackFeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrSEARCHbreak3"
  instrSEARCHbreak3Clock = new util.Clock();
  instrHeaderText_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_5',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "searchTrial"
  searchTrialClock = new util.Clock();
  orientList = [0, 90, 180, 270];
  PosList = [[0.45, (- 0.45)], [0.45, (- 0.15)], [0.45, 0.15], [0.45, 0.45], [0.15, (- 0.45)], [0.15, (- 0.15)], [0.15, 0.15], [0.15, 0.45], [(- 0.15), (- 0.45)], [(- 0.15), (- 0.15)], [(- 0.15), 0.15], [(- 0.15), 0.45], [(- 0.45), (- 0.45)], [(- 0.45), (- 0.15)], [(- 0.45), 0.15], [(- 0.45), 0.45]];
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  targetStim = new visual.TextStim({
    win: psychoJS.window,
    name: 'targetStim',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  searchStim2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  searchStim3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  searchStim4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim4',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  searchStim5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim5',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  searchStim6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim6',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  searchStim7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim7',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  searchStim8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim8',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  searchStim9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim9',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  searchStim10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  searchStim11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim11',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  // Initialize components for Routine "searchFeedback"
  searchFeedbackClock = new util.Clock();
  msg = " ";
  
  searchFeedbackText = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchFeedbackText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrMENTROTbreak4"
  instrMENTROTbreak4Clock = new util.Clock();
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_15',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "mentRotTrial"
  mentRotTrialClock = new util.Clock();
  mentRotStimulus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mentRotStimulus', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.935, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  MROT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mentRotFeedback"
  mentRotFeedbackClock = new util.Clock();
  msg = " ";
  
  NBackfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrNBACKbreak5"
  instrNBACKbreak5Clock = new util.Clock();
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_9',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackFirst3Trials"
  NBackFirst3TrialsClock = new util.Clock();
  Back2minus1 = [];
  Back2minus2 = [];
  Back2minus3 = [];
  
  NBackText_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackRemainderTrials"
  NBackRemainderTrialsClock = new util.Clock();
  NBackText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NBackFeedback"
  NBackFeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrAXCPTbreak6"
  instrAXCPTbreak6Clock = new util.Clock();
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_7',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: "Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "AXCPTtrial"
  AXCPTtrialClock = new util.Clock();
  Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
  distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  
  cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cue_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  break1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break1',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -2.0 
  });
  
  distractor1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  break2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break2',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -4.0 
  });
  
  distractor2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  break3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break3',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -6.0 
  });
  
  // Initialize components for Routine "AXCPTprobe"
  AXCPTprobeClock = new util.Clock();
  probe_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  AXCPT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AXCPTfeedback"
  AXCPTfeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrSEARCHbreak7"
  instrSEARCHbreak7Clock = new util.Clock();
  instrHeaderText_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_11',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "searchTrial"
  searchTrialClock = new util.Clock();
  orientList = [0, 90, 180, 270];
  PosList = [[0.45, (- 0.45)], [0.45, (- 0.15)], [0.45, 0.15], [0.45, 0.45], [0.15, (- 0.45)], [0.15, (- 0.15)], [0.15, 0.15], [0.15, 0.45], [(- 0.15), (- 0.45)], [(- 0.15), (- 0.15)], [(- 0.15), 0.15], [(- 0.15), 0.45], [(- 0.45), (- 0.45)], [(- 0.45), (- 0.15)], [(- 0.45), 0.15], [(- 0.45), 0.45]];
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  targetStim = new visual.TextStim({
    win: psychoJS.window,
    name: 'targetStim',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  searchStim2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  searchStim3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  searchStim4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim4',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  searchStim5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim5',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  searchStim6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim6',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  searchStim7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim7',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  searchStim8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim8',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  searchStim9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim9',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  searchStim10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  searchStim11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim11',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  // Initialize components for Routine "searchFeedback"
  searchFeedbackClock = new util.Clock();
  msg = " ";
  
  searchFeedbackText = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchFeedbackText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrMENTROTbreak8"
  instrMENTROTbreak8Clock = new util.Clock();
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_13',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "mentRotTrial"
  mentRotTrialClock = new util.Clock();
  mentRotStimulus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mentRotStimulus', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.935, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  MROT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mentRotFeedback"
  mentRotFeedbackClock = new util.Clock();
  msg = " ";
  
  NBackfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrNBACKbreak9"
  instrNBACKbreak9Clock = new util.Clock();
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_10',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackFirst3Trials"
  NBackFirst3TrialsClock = new util.Clock();
  Back2minus1 = [];
  Back2minus2 = [];
  Back2minus3 = [];
  
  NBackText_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NBackRemainderTrials"
  NBackRemainderTrialsClock = new util.Clock();
  NBackText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackText_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  NBack_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NBackFeedback"
  NBackFeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrSEARCHbreak10"
  instrSEARCHbreak10Clock = new util.Clock();
  instrHeaderText_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_12',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "searchTrial"
  searchTrialClock = new util.Clock();
  orientList = [0, 90, 180, 270];
  PosList = [[0.45, (- 0.45)], [0.45, (- 0.15)], [0.45, 0.15], [0.45, 0.45], [0.15, (- 0.45)], [0.15, (- 0.15)], [0.15, 0.15], [0.15, 0.45], [(- 0.15), (- 0.45)], [(- 0.15), (- 0.15)], [(- 0.15), 0.15], [(- 0.15), 0.45], [(- 0.45), (- 0.45)], [(- 0.45), (- 0.15)], [(- 0.45), 0.15], [(- 0.45), 0.45]];
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  targetStim = new visual.TextStim({
    win: psychoJS.window,
    name: 'targetStim',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  searchStim2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  searchStim3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  searchStim4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim4',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  searchStim5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim5',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  searchStim6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim6',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  searchStim7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim7',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  searchStim8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim8',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  searchStim9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim9',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  searchStim10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  searchStim11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchStim11',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 1.0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  // Initialize components for Routine "searchFeedback"
  searchFeedbackClock = new util.Clock();
  msg = " ";
  
  searchFeedbackText = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchFeedbackText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrMENTROTbreak11"
  instrMENTROTbreak11Clock = new util.Clock();
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_14',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_18',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "mentRotTrial"
  mentRotTrialClock = new util.Clock();
  mentRotStimulus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mentRotStimulus', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.935, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  MROT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mentRotFeedback"
  mentRotFeedbackClock = new util.Clock();
  msg = " ";
  
  NBackfeedback_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'NBackfeedback_text_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrAXCPTbreak12"
  instrAXCPTbreak12Clock = new util.Clock();
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instrHeaderText_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrHeaderText_8',
    text: 'Optional rest break',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: "Next task: AX-CPT\n\nPress 'k' when first red letter is 'A' and second red letter is 'X'\n\nPress 'd' for any other combination of letters\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin\n",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "createLoopTimer"
  createLoopTimerClock = new util.Clock();
  // Initialize components for Routine "timer"
  timerClock = new util.Clock();
  probeVal = [];
  
  timer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_text',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -1.0 
  });
  
  // Initialize components for Routine "AXCPTtrial"
  AXCPTtrialClock = new util.Clock();
  Bletters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  Yletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z"];
  distractors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"];
  
  cue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cue_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  break1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break1',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -2.0 
  });
  
  distractor1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  break2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break2',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -4.0 
  });
  
  distractor2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  break3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break3',
    text: 'x',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -6.0 
  });
  
  // Initialize components for Routine "AXCPTprobe"
  AXCPTprobeClock = new util.Clock();
  probe_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: 1,
    depth: 0.0 
  });
  
  AXCPT_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AXCPTfeedback"
  AXCPTfeedbackClock = new util.Clock();
  msg = " ";
  
  AXCPTfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'AXCPTfeedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "F_ISA"
  F_ISAClock = new util.Clock();
  mouse_22 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_22.mouseClock = new util.Clock();
  mouse_visibility = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Timer = new util.Clock();
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Please rate your level of mental fatigue  from 1-5:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["very low (alert)", "low", "medium", "high", "very high (fatigued)"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('LightGray'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "instrBRUMSpost"
  instrBRUMSpostClock = new util.Clock();
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: 'Thank you for completing the tasks\n\nOn the next few screens there are lists of words that describe feelings people have\n\nPlease read each one carefully. Then click the answer which best describes how you feel right now\n\nMake sure you answer every question\n\nPlease press the mouse to begin\n\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_9 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_9.mouseClock = new util.Clock();
  BRUMSheader_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'BRUMSheader_2',
    text: 'Rating Scale Instructions',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "BRUMS_1"
  BRUMS_1Clock = new util.Clock();
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  mouse_visibility_fix = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  slider1 = new visual.Slider({
    win: psychoJS.window, name: 'slider1',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider2 = new visual.Slider({
    win: psychoJS.window, name: 'slider2',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider3 = new visual.Slider({
    win: psychoJS.window, name: 'slider3',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider4 = new visual.Slider({
    win: psychoJS.window, name: 'slider4',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider5 = new visual.Slider({
    win: psychoJS.window, name: 'slider5',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider6 = new visual.Slider({
    win: psychoJS.window, name: 'slider6',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider7 = new visual.Slider({
    win: psychoJS.window, name: 'slider7',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider8 = new visual.Slider({
    win: psychoJS.window, name: 'slider8',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Rating Scales: Page 1 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  panicky = new visual.TextStim({
    win: psychoJS.window,
    name: 'panicky',
    text: 'Panicky',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  lively = new visual.TextStim({
    win: psychoJS.window,
    name: 'lively',
    text: 'Lively',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  confused = new visual.TextStim({
    win: psychoJS.window,
    name: 'confused',
    text: 'Confused',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  wornout = new visual.TextStim({
    win: psychoJS.window,
    name: 'wornout',
    text: 'Worn Out',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  depressed = new visual.TextStim({
    win: psychoJS.window,
    name: 'depressed',
    text: 'Depressed',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  downheartened = new visual.TextStim({
    win: psychoJS.window,
    name: 'downheartened',
    text: 'Downheartened',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  annoyed = new visual.TextStim({
    win: psychoJS.window,
    name: 'annoyed',
    text: 'Annoyed',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  exhausted = new visual.TextStim({
    win: psychoJS.window,
    name: 'exhausted',
    text: 'Exhausted',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  // Initialize components for Routine "BRUMS_2"
  BRUMS_2Clock = new util.Clock();
  mouse_5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_5.mouseClock = new util.Clock();
  mouse_visibility_fix_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix_2', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  slider9 = new visual.Slider({
    win: psychoJS.window, name: 'slider9',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider10 = new visual.Slider({
    win: psychoJS.window, name: 'slider10',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider11 = new visual.Slider({
    win: psychoJS.window, name: 'slider11',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider12 = new visual.Slider({
    win: psychoJS.window, name: 'slider12',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider13 = new visual.Slider({
    win: psychoJS.window, name: 'slider13',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider14 = new visual.Slider({
    win: psychoJS.window, name: 'slider14',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider15 = new visual.Slider({
    win: psychoJS.window, name: 'slider15',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider16 = new visual.Slider({
    win: psychoJS.window, name: 'slider16',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Rating Scales: Page 2 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  mixedup = new visual.TextStim({
    win: psychoJS.window,
    name: 'mixedup',
    text: 'Mixed-up',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  sleepy = new visual.TextStim({
    win: psychoJS.window,
    name: 'sleepy',
    text: 'Sleepy',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  bitter = new visual.TextStim({
    win: psychoJS.window,
    name: 'bitter',
    text: 'Bitter',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  unhappy = new visual.TextStim({
    win: psychoJS.window,
    name: 'unhappy',
    text: 'Unhappy',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  anxious = new visual.TextStim({
    win: psychoJS.window,
    name: 'anxious',
    text: 'Anxious',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  worried = new visual.TextStim({
    win: psychoJS.window,
    name: 'worried',
    text: 'Worried',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  energetic = new visual.TextStim({
    win: psychoJS.window,
    name: 'energetic',
    text: 'Energetic',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  miserable = new visual.TextStim({
    win: psychoJS.window,
    name: 'miserable',
    text: 'Miserable',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  // Initialize components for Routine "BRUMS_3"
  BRUMS_3Clock = new util.Clock();
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  mouse_visibility_fix_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'mouse_visibility_fix_3', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  slider17 = new visual.Slider({
    win: psychoJS.window, name: 'slider17',
    size: [0.75, 0.1], pos: [0.1, 0.6], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider18 = new visual.Slider({
    win: psychoJS.window, name: 'slider18',
    size: [0.75, 0.1], pos: [0.1, 0.4], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider19 = new visual.Slider({
    win: psychoJS.window, name: 'slider19',
    size: [0.75, 0.1], pos: [0.1, 0.2], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider20 = new visual.Slider({
    win: psychoJS.window, name: 'slider20',
    size: [0.75, 0.1], pos: [0.1, 0.0], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider21 = new visual.Slider({
    win: psychoJS.window, name: 'slider21',
    size: [0.75, 0.1], pos: [0.1, (- 0.2)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider22 = new visual.Slider({
    win: psychoJS.window, name: 'slider22',
    size: [0.75, 0.1], pos: [0.1, (- 0.4)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider23 = new visual.Slider({
    win: psychoJS.window, name: 'slider23',
    size: [0.75, 0.1], pos: [0.1, (- 0.6)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  slider24 = new visual.Slider({
    win: psychoJS.window, name: 'slider24',
    size: [0.75, 0.1], pos: [0.1, (- 0.8)], units: 'norm',
    labels: ["Not at all", "A little", "Moderately", "Quite a bit", "Extremely"], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.WHITE_ON_BLACK],
    color: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, 
    flip: false,
  });
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'Rating Scales: Page 3 of 3\n\nDescribe how you feel right now\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.82], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  muddled = new visual.TextStim({
    win: psychoJS.window,
    name: 'muddled',
    text: 'Muddled',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.6], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  nervous = new visual.TextStim({
    win: psychoJS.window,
    name: 'nervous',
    text: 'Nervous',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.4], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  angry = new visual.TextStim({
    win: psychoJS.window,
    name: 'angry',
    text: 'Angry',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  active = new visual.TextStim({
    win: psychoJS.window,
    name: 'active',
    text: 'Active',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -16.0 
  });
  
  tired = new visual.TextStim({
    win: psychoJS.window,
    name: 'tired',
    text: 'Tired',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -17.0 
  });
  
  badtempered = new visual.TextStim({
    win: psychoJS.window,
    name: 'badtempered',
    text: 'Bad tempered',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.4)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -18.0 
  });
  
  alert = new visual.TextStim({
    win: psychoJS.window,
    name: 'alert',
    text: 'Alert',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.6)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -19.0 
  });
  
  uncertain = new visual.TextStim({
    win: psychoJS.window,
    name: 'uncertain',
    text: 'Uncertain',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.8)], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -20.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'End of Experiment\n\nThank you for taking part\n\nPlease email Ellie with your participant ID\n\nYou will then receive instructions about how to claim the compensation for your time\n\nPress the space bar to close the experiment',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'intro'-------
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    BRUMSheader.setAlignHoriz("center");
    instrHeaderText_2.setAlignHoriz("center");
    instrHeaderText_3.setAlignHoriz("center");
    instrHeaderText_5.setAlignHoriz("center");
    instrHeaderText_9.setAlignHoriz("center");
    instrHeaderText_7.setAlignHoriz("center");
    instrHeaderText_11.setAlignHoriz("center");
    instrHeaderText_13.setAlignHoriz("center");
    instrHeaderText_10.setAlignHoriz("center");
    instrHeaderText_12.setAlignHoriz("center");
    instrHeaderText_14.setAlignHoriz("center");
    instrHeaderText_8.setAlignHoriz("center");
    text_2.setAlignHoriz("center");
    text_8.setAlignHoriz("center");
    text_9.setAlignHoriz("center");
    text_10.setAlignHoriz("center");
    text_11.setAlignHoriz("center");
    text_3.setAlignHoriz("center");
    text_5.setAlignHoriz("center");
    text_19.setAlignHoriz("center");
    text_13.setAlignHoriz("center");
    text_7.setAlignHoriz("center");
    text_15.setAlignHoriz("center");
    text_17.setAlignHoriz("center");
    text_14.setAlignHoriz("center");
    text_16.setAlignHoriz("center");
    text_18.setAlignHoriz("center");
    text_12.setAlignHoriz("center");
    text_20.setAlignHoriz("center");
    BRUMSheader_2.setAlignHoriz("center");
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(key_resp);
    introComponents.push(instrHeaderText);
    introComponents.push(text);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function introRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'intro'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 2 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText* updates
    if (t >= 0.0 && instrHeaderText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText.tStart = t;  // (not accounting for frame time here)
      instrHeaderText.frameNStart = frameN;  // exact frame index
      
      instrHeaderText.setAutoDraw(true);
    }

    
    // *text* updates
    if (t >= 0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'intro'-------
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var F_ISAComponents;
function F_ISARoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'F_ISA'-------
    t = 0;
    F_ISAClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_22
    gotValidClick = false; // until a click is received
    slider.reset()
    // keep track of which components have finished
    F_ISAComponents = [];
    F_ISAComponents.push(mouse_22);
    F_ISAComponents.push(mouse_visibility);
    F_ISAComponents.push(text_4);
    F_ISAComponents.push(slider);
    
    for (const thisComponent of F_ISAComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function F_ISARoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'F_ISA'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = F_ISAClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mouse_visibility* updates
    if (t >= 0.0 && mouse_visibility.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_visibility.tStart = t;  // (not accounting for frame time here)
      mouse_visibility.frameNStart = frameN;  // exact frame index
      
      mouse_visibility.setAutoDraw(true);
    }

    
    if (mouse_visibility.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mouse_visibility.setPos([mouse_22.getPos()[0], mouse_22.getPos()[1]]);
    }
    if ((slider.getRating() > 0)) {
        continueRoutine = false;
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // Check slider for response to end routine
    if (slider.getRating() !== undefined && slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of F_ISAComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function F_ISARoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'F_ISA'-------
    for (const thisComponent of F_ISAComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("F_ISA.duration", Timer.getTime());
    
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // the Routine "F_ISA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrBRUMSpreComponents;
function instrBRUMSpreRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrBRUMSpre'-------
    t = 0;
    instrBRUMSpreClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_4
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instrBRUMSpreComponents = [];
    instrBRUMSpreComponents.push(text_8);
    instrBRUMSpreComponents.push(mouse_4);
    instrBRUMSpreComponents.push(BRUMSheader);
    
    for (const thisComponent of instrBRUMSpreComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var prevButtonState;
var _mouseButtons;
function instrBRUMSpreRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrBRUMSpre'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrBRUMSpreClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    // *mouse_4* updates
    if (t >= 0.5 && mouse_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_4.tStart = t;  // (not accounting for frame time here)
      mouse_4.frameNStart = frameN;  // exact frame index
      
      mouse_4.status = PsychoJS.Status.STARTED;
      mouse_4.mouseClock.reset();
      prevButtonState = mouse_4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *BRUMSheader* updates
    if (t >= 0.0 && BRUMSheader.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BRUMSheader.tStart = t;  // (not accounting for frame time here)
      BRUMSheader.frameNStart = frameN;  // exact frame index
      
      BRUMSheader.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrBRUMSpreComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrBRUMSpreRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrBRUMSpre'-------
    for (const thisComponent of instrBRUMSpreComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    
    // store data for thisExp (ExperimentHandler)
    // the Routine "instrBRUMSpre" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var BRUMSTimer;
var BRUMS_1Components;
function BRUMS_1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BRUMS_1'-------
    t = 0;
    BRUMS_1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    BRUMSTimer = new util.Clock();
    
    // setup some python lists for storing info about the mouse_3
    gotValidClick = false; // until a click is received
    slider1.reset()
    slider2.reset()
    slider3.reset()
    slider4.reset()
    slider5.reset()
    slider6.reset()
    slider7.reset()
    slider8.reset()
    // keep track of which components have finished
    BRUMS_1Components = [];
    BRUMS_1Components.push(mouse_3);
    BRUMS_1Components.push(mouse_visibility_fix);
    BRUMS_1Components.push(slider1);
    BRUMS_1Components.push(slider2);
    BRUMS_1Components.push(slider3);
    BRUMS_1Components.push(slider4);
    BRUMS_1Components.push(slider5);
    BRUMS_1Components.push(slider6);
    BRUMS_1Components.push(slider7);
    BRUMS_1Components.push(slider8);
    BRUMS_1Components.push(text_9);
    BRUMS_1Components.push(panicky);
    BRUMS_1Components.push(lively);
    BRUMS_1Components.push(confused);
    BRUMS_1Components.push(wornout);
    BRUMS_1Components.push(depressed);
    BRUMS_1Components.push(downheartened);
    BRUMS_1Components.push(annoyed);
    BRUMS_1Components.push(exhausted);
    
    for (const thisComponent of BRUMS_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function BRUMS_1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BRUMS_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BRUMS_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((((((((slider1.getRating() > 0) && (slider2.getRating() > 0)) && (slider3.getRating() > 0)) && (slider4.getRating() > 0)) && (slider5.getRating() > 0)) && (slider6.getRating() > 0)) && (slider7.getRating() > 0)) && (slider8.getRating() > 0))) {
        continueRoutine = false;
    }
    
    
    // *mouse_visibility_fix* updates
    if (t >= 0.0 && mouse_visibility_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_visibility_fix.tStart = t;  // (not accounting for frame time here)
      mouse_visibility_fix.frameNStart = frameN;  // exact frame index
      
      mouse_visibility_fix.setAutoDraw(true);
    }

    
    if (mouse_visibility_fix.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mouse_visibility_fix.setPos([mouse_3.getPos()[0], mouse_3.getPos()[1]]);
    }
    
    // *slider1* updates
    if (t >= 0.0 && slider1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider1.tStart = t;  // (not accounting for frame time here)
      slider1.frameNStart = frameN;  // exact frame index
      
      slider1.setAutoDraw(true);
    }

    
    // *slider2* updates
    if (t >= 0.0 && slider2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider2.tStart = t;  // (not accounting for frame time here)
      slider2.frameNStart = frameN;  // exact frame index
      
      slider2.setAutoDraw(true);
    }

    
    // *slider3* updates
    if (t >= 0.0 && slider3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider3.tStart = t;  // (not accounting for frame time here)
      slider3.frameNStart = frameN;  // exact frame index
      
      slider3.setAutoDraw(true);
    }

    
    // *slider4* updates
    if (t >= 0.0 && slider4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider4.tStart = t;  // (not accounting for frame time here)
      slider4.frameNStart = frameN;  // exact frame index
      
      slider4.setAutoDraw(true);
    }

    
    // *slider5* updates
    if (t >= 0.0 && slider5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider5.tStart = t;  // (not accounting for frame time here)
      slider5.frameNStart = frameN;  // exact frame index
      
      slider5.setAutoDraw(true);
    }

    
    // *slider6* updates
    if (t >= 0.0 && slider6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider6.tStart = t;  // (not accounting for frame time here)
      slider6.frameNStart = frameN;  // exact frame index
      
      slider6.setAutoDraw(true);
    }

    
    // *slider7* updates
    if (t >= 0.0 && slider7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider7.tStart = t;  // (not accounting for frame time here)
      slider7.frameNStart = frameN;  // exact frame index
      
      slider7.setAutoDraw(true);
    }

    
    // *slider8* updates
    if (t >= 0.0 && slider8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider8.tStart = t;  // (not accounting for frame time here)
      slider8.frameNStart = frameN;  // exact frame index
      
      slider8.setAutoDraw(true);
    }

    
    // *text_9* updates
    if (t >= 0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    
    // *panicky* updates
    if (t >= 0.0 && panicky.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panicky.tStart = t;  // (not accounting for frame time here)
      panicky.frameNStart = frameN;  // exact frame index
      
      panicky.setAutoDraw(true);
    }

    
    // *lively* updates
    if (t >= 0.0 && lively.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lively.tStart = t;  // (not accounting for frame time here)
      lively.frameNStart = frameN;  // exact frame index
      
      lively.setAutoDraw(true);
    }

    
    // *confused* updates
    if (t >= 0.0 && confused.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confused.tStart = t;  // (not accounting for frame time here)
      confused.frameNStart = frameN;  // exact frame index
      
      confused.setAutoDraw(true);
    }

    
    // *wornout* updates
    if (t >= 0.0 && wornout.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wornout.tStart = t;  // (not accounting for frame time here)
      wornout.frameNStart = frameN;  // exact frame index
      
      wornout.setAutoDraw(true);
    }

    
    // *depressed* updates
    if (t >= 0.0 && depressed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      depressed.tStart = t;  // (not accounting for frame time here)
      depressed.frameNStart = frameN;  // exact frame index
      
      depressed.setAutoDraw(true);
    }

    
    // *downheartened* updates
    if (t >= 0.0 && downheartened.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      downheartened.tStart = t;  // (not accounting for frame time here)
      downheartened.frameNStart = frameN;  // exact frame index
      
      downheartened.setAutoDraw(true);
    }

    
    // *annoyed* updates
    if (t >= 0.0 && annoyed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      annoyed.tStart = t;  // (not accounting for frame time here)
      annoyed.frameNStart = frameN;  // exact frame index
      
      annoyed.setAutoDraw(true);
    }

    
    // *exhausted* updates
    if (t >= 0.0 && exhausted.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exhausted.tStart = t;  // (not accounting for frame time here)
      exhausted.frameNStart = frameN;  // exact frame index
      
      exhausted.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BRUMS_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BRUMS_1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BRUMS_1'-------
    for (const thisComponent of BRUMS_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('slider1.response', slider1.getRating());
    psychoJS.experiment.addData('slider1.rt', slider1.getRT());
    psychoJS.experiment.addData('slider2.response', slider2.getRating());
    psychoJS.experiment.addData('slider2.rt', slider2.getRT());
    psychoJS.experiment.addData('slider3.response', slider3.getRating());
    psychoJS.experiment.addData('slider3.rt', slider3.getRT());
    psychoJS.experiment.addData('slider4.response', slider4.getRating());
    psychoJS.experiment.addData('slider4.rt', slider4.getRT());
    psychoJS.experiment.addData('slider5.response', slider5.getRating());
    psychoJS.experiment.addData('slider5.rt', slider5.getRT());
    psychoJS.experiment.addData('slider6.response', slider6.getRating());
    psychoJS.experiment.addData('slider6.rt', slider6.getRT());
    psychoJS.experiment.addData('slider7.response', slider7.getRating());
    psychoJS.experiment.addData('slider7.rt', slider7.getRT());
    psychoJS.experiment.addData('slider8.response', slider8.getRating());
    psychoJS.experiment.addData('slider8.rt', slider8.getRT());
    // the Routine "BRUMS_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var BRUMS_2Components;
function BRUMS_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BRUMS_2'-------
    t = 0;
    BRUMS_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_5
    gotValidClick = false; // until a click is received
    slider9.reset()
    slider10.reset()
    slider11.reset()
    slider12.reset()
    slider13.reset()
    slider14.reset()
    slider15.reset()
    slider16.reset()
    // keep track of which components have finished
    BRUMS_2Components = [];
    BRUMS_2Components.push(mouse_5);
    BRUMS_2Components.push(mouse_visibility_fix_2);
    BRUMS_2Components.push(slider9);
    BRUMS_2Components.push(slider10);
    BRUMS_2Components.push(slider11);
    BRUMS_2Components.push(slider12);
    BRUMS_2Components.push(slider13);
    BRUMS_2Components.push(slider14);
    BRUMS_2Components.push(slider15);
    BRUMS_2Components.push(slider16);
    BRUMS_2Components.push(text_10);
    BRUMS_2Components.push(mixedup);
    BRUMS_2Components.push(sleepy);
    BRUMS_2Components.push(bitter);
    BRUMS_2Components.push(unhappy);
    BRUMS_2Components.push(anxious);
    BRUMS_2Components.push(worried);
    BRUMS_2Components.push(energetic);
    BRUMS_2Components.push(miserable);
    
    for (const thisComponent of BRUMS_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function BRUMS_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BRUMS_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BRUMS_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((((((((slider9.getRating() > 0) && (slider10.getRating() > 0)) && (slider11.getRating() > 0)) && (slider12.getRating() > 0)) && (slider13.getRating() > 0)) && (slider14.getRating() > 0)) && (slider15.getRating() > 0)) && (slider16.getRating() > 0))) {
        continueRoutine = false;
    }
    
    
    // *mouse_visibility_fix_2* updates
    if (t >= 0.0 && mouse_visibility_fix_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_visibility_fix_2.tStart = t;  // (not accounting for frame time here)
      mouse_visibility_fix_2.frameNStart = frameN;  // exact frame index
      
      mouse_visibility_fix_2.setAutoDraw(true);
    }

    
    if (mouse_visibility_fix_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mouse_visibility_fix_2.setPos([mouse_5.getPos()[0], mouse_5.getPos()[1]]);
    }
    
    // *slider9* updates
    if (t >= 0.0 && slider9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider9.tStart = t;  // (not accounting for frame time here)
      slider9.frameNStart = frameN;  // exact frame index
      
      slider9.setAutoDraw(true);
    }

    
    // *slider10* updates
    if (t >= 0.0 && slider10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider10.tStart = t;  // (not accounting for frame time here)
      slider10.frameNStart = frameN;  // exact frame index
      
      slider10.setAutoDraw(true);
    }

    
    // *slider11* updates
    if (t >= 0.0 && slider11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider11.tStart = t;  // (not accounting for frame time here)
      slider11.frameNStart = frameN;  // exact frame index
      
      slider11.setAutoDraw(true);
    }

    
    // *slider12* updates
    if (t >= 0.0 && slider12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider12.tStart = t;  // (not accounting for frame time here)
      slider12.frameNStart = frameN;  // exact frame index
      
      slider12.setAutoDraw(true);
    }

    
    // *slider13* updates
    if (t >= 0.0 && slider13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider13.tStart = t;  // (not accounting for frame time here)
      slider13.frameNStart = frameN;  // exact frame index
      
      slider13.setAutoDraw(true);
    }

    
    // *slider14* updates
    if (t >= 0.0 && slider14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider14.tStart = t;  // (not accounting for frame time here)
      slider14.frameNStart = frameN;  // exact frame index
      
      slider14.setAutoDraw(true);
    }

    
    // *slider15* updates
    if (t >= 0.0 && slider15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider15.tStart = t;  // (not accounting for frame time here)
      slider15.frameNStart = frameN;  // exact frame index
      
      slider15.setAutoDraw(true);
    }

    
    // *slider16* updates
    if (t >= 0.0 && slider16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider16.tStart = t;  // (not accounting for frame time here)
      slider16.frameNStart = frameN;  // exact frame index
      
      slider16.setAutoDraw(true);
    }

    
    // *text_10* updates
    if (t >= 0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *mixedup* updates
    if (t >= 0.0 && mixedup.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mixedup.tStart = t;  // (not accounting for frame time here)
      mixedup.frameNStart = frameN;  // exact frame index
      
      mixedup.setAutoDraw(true);
    }

    
    // *sleepy* updates
    if (t >= 0.0 && sleepy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sleepy.tStart = t;  // (not accounting for frame time here)
      sleepy.frameNStart = frameN;  // exact frame index
      
      sleepy.setAutoDraw(true);
    }

    
    // *bitter* updates
    if (t >= 0.0 && bitter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bitter.tStart = t;  // (not accounting for frame time here)
      bitter.frameNStart = frameN;  // exact frame index
      
      bitter.setAutoDraw(true);
    }

    
    // *unhappy* updates
    if (t >= 0.0 && unhappy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      unhappy.tStart = t;  // (not accounting for frame time here)
      unhappy.frameNStart = frameN;  // exact frame index
      
      unhappy.setAutoDraw(true);
    }

    
    // *anxious* updates
    if (t >= 0.0 && anxious.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      anxious.tStart = t;  // (not accounting for frame time here)
      anxious.frameNStart = frameN;  // exact frame index
      
      anxious.setAutoDraw(true);
    }

    
    // *worried* updates
    if (t >= 0.0 && worried.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worried.tStart = t;  // (not accounting for frame time here)
      worried.frameNStart = frameN;  // exact frame index
      
      worried.setAutoDraw(true);
    }

    
    // *energetic* updates
    if (t >= 0.0 && energetic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      energetic.tStart = t;  // (not accounting for frame time here)
      energetic.frameNStart = frameN;  // exact frame index
      
      energetic.setAutoDraw(true);
    }

    
    // *miserable* updates
    if (t >= 0.0 && miserable.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      miserable.tStart = t;  // (not accounting for frame time here)
      miserable.frameNStart = frameN;  // exact frame index
      
      miserable.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BRUMS_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BRUMS_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BRUMS_2'-------
    for (const thisComponent of BRUMS_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('slider9.response', slider9.getRating());
    psychoJS.experiment.addData('slider9.rt', slider9.getRT());
    psychoJS.experiment.addData('slider10.response', slider10.getRating());
    psychoJS.experiment.addData('slider10.rt', slider10.getRT());
    psychoJS.experiment.addData('slider11.response', slider11.getRating());
    psychoJS.experiment.addData('slider11.rt', slider11.getRT());
    psychoJS.experiment.addData('slider12.response', slider12.getRating());
    psychoJS.experiment.addData('slider12.rt', slider12.getRT());
    psychoJS.experiment.addData('slider13.response', slider13.getRating());
    psychoJS.experiment.addData('slider13.rt', slider13.getRT());
    psychoJS.experiment.addData('slider14.response', slider14.getRating());
    psychoJS.experiment.addData('slider14.rt', slider14.getRT());
    psychoJS.experiment.addData('slider15.response', slider15.getRating());
    psychoJS.experiment.addData('slider15.rt', slider15.getRT());
    psychoJS.experiment.addData('slider16.response', slider16.getRating());
    psychoJS.experiment.addData('slider16.rt', slider16.getRT());
    // the Routine "BRUMS_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var BRUMS_3Components;
function BRUMS_3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'BRUMS_3'-------
    t = 0;
    BRUMS_3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_6
    gotValidClick = false; // until a click is received
    slider17.reset()
    slider18.reset()
    slider19.reset()
    slider20.reset()
    slider21.reset()
    slider22.reset()
    slider23.reset()
    slider24.reset()
    // keep track of which components have finished
    BRUMS_3Components = [];
    BRUMS_3Components.push(mouse_6);
    BRUMS_3Components.push(mouse_visibility_fix_3);
    BRUMS_3Components.push(slider17);
    BRUMS_3Components.push(slider18);
    BRUMS_3Components.push(slider19);
    BRUMS_3Components.push(slider20);
    BRUMS_3Components.push(slider21);
    BRUMS_3Components.push(slider22);
    BRUMS_3Components.push(slider23);
    BRUMS_3Components.push(slider24);
    BRUMS_3Components.push(text_11);
    BRUMS_3Components.push(muddled);
    BRUMS_3Components.push(nervous);
    BRUMS_3Components.push(angry);
    BRUMS_3Components.push(active);
    BRUMS_3Components.push(tired);
    BRUMS_3Components.push(badtempered);
    BRUMS_3Components.push(alert);
    BRUMS_3Components.push(uncertain);
    
    for (const thisComponent of BRUMS_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function BRUMS_3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'BRUMS_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BRUMS_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((((((((slider17.getRating() > 0) && (slider18.getRating() > 0)) && (slider19.getRating() > 0)) && (slider20.getRating() > 0)) && (slider21.getRating() > 0)) && (slider22.getRating() > 0)) && (slider23.getRating() > 0)) && (slider24.getRating() > 0))) {
        continueRoutine = false;
    }
    
    
    // *mouse_visibility_fix_3* updates
    if (t >= 0.0 && mouse_visibility_fix_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_visibility_fix_3.tStart = t;  // (not accounting for frame time here)
      mouse_visibility_fix_3.frameNStart = frameN;  // exact frame index
      
      mouse_visibility_fix_3.setAutoDraw(true);
    }

    
    if (mouse_visibility_fix_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mouse_visibility_fix_3.setPos([mouse_6.getPos()[0], mouse_6.getPos()[1]]);
    }
    
    // *slider17* updates
    if (t >= 0.0 && slider17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider17.tStart = t;  // (not accounting for frame time here)
      slider17.frameNStart = frameN;  // exact frame index
      
      slider17.setAutoDraw(true);
    }

    
    // *slider18* updates
    if (t >= 0.0 && slider18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider18.tStart = t;  // (not accounting for frame time here)
      slider18.frameNStart = frameN;  // exact frame index
      
      slider18.setAutoDraw(true);
    }

    
    // *slider19* updates
    if (t >= 0.0 && slider19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider19.tStart = t;  // (not accounting for frame time here)
      slider19.frameNStart = frameN;  // exact frame index
      
      slider19.setAutoDraw(true);
    }

    
    // *slider20* updates
    if (t >= 0.0 && slider20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider20.tStart = t;  // (not accounting for frame time here)
      slider20.frameNStart = frameN;  // exact frame index
      
      slider20.setAutoDraw(true);
    }

    
    // *slider21* updates
    if (t >= 0.0 && slider21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider21.tStart = t;  // (not accounting for frame time here)
      slider21.frameNStart = frameN;  // exact frame index
      
      slider21.setAutoDraw(true);
    }

    
    // *slider22* updates
    if (t >= 0.0 && slider22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider22.tStart = t;  // (not accounting for frame time here)
      slider22.frameNStart = frameN;  // exact frame index
      
      slider22.setAutoDraw(true);
    }

    
    // *slider23* updates
    if (t >= 0.0 && slider23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider23.tStart = t;  // (not accounting for frame time here)
      slider23.frameNStart = frameN;  // exact frame index
      
      slider23.setAutoDraw(true);
    }

    
    // *slider24* updates
    if (t >= 0.0 && slider24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider24.tStart = t;  // (not accounting for frame time here)
      slider24.frameNStart = frameN;  // exact frame index
      
      slider24.setAutoDraw(true);
    }

    
    // *text_11* updates
    if (t >= 0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    
    // *muddled* updates
    if (t >= 0.0 && muddled.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      muddled.tStart = t;  // (not accounting for frame time here)
      muddled.frameNStart = frameN;  // exact frame index
      
      muddled.setAutoDraw(true);
    }

    
    // *nervous* updates
    if (t >= 0.0 && nervous.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nervous.tStart = t;  // (not accounting for frame time here)
      nervous.frameNStart = frameN;  // exact frame index
      
      nervous.setAutoDraw(true);
    }

    
    // *angry* updates
    if (t >= 0.0 && angry.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      angry.tStart = t;  // (not accounting for frame time here)
      angry.frameNStart = frameN;  // exact frame index
      
      angry.setAutoDraw(true);
    }

    
    // *active* updates
    if (t >= 0.0 && active.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      active.tStart = t;  // (not accounting for frame time here)
      active.frameNStart = frameN;  // exact frame index
      
      active.setAutoDraw(true);
    }

    
    // *tired* updates
    if (t >= 0.0 && tired.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tired.tStart = t;  // (not accounting for frame time here)
      tired.frameNStart = frameN;  // exact frame index
      
      tired.setAutoDraw(true);
    }

    
    // *badtempered* updates
    if (t >= 0.0 && badtempered.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      badtempered.tStart = t;  // (not accounting for frame time here)
      badtempered.frameNStart = frameN;  // exact frame index
      
      badtempered.setAutoDraw(true);
    }

    
    // *alert* updates
    if (t >= 0.0 && alert.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      alert.tStart = t;  // (not accounting for frame time here)
      alert.frameNStart = frameN;  // exact frame index
      
      alert.setAutoDraw(true);
    }

    
    // *uncertain* updates
    if (t >= 0.0 && uncertain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      uncertain.tStart = t;  // (not accounting for frame time here)
      uncertain.frameNStart = frameN;  // exact frame index
      
      uncertain.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BRUMS_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BRUMS_3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'BRUMS_3'-------
    for (const thisComponent of BRUMS_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("BRUMS.duration", BRUMSTimer.getTime());
    
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('slider17.response', slider17.getRating());
    psychoJS.experiment.addData('slider17.rt', slider17.getRT());
    psychoJS.experiment.addData('slider18.response', slider18.getRating());
    psychoJS.experiment.addData('slider18.rt', slider18.getRT());
    psychoJS.experiment.addData('slider19.response', slider19.getRating());
    psychoJS.experiment.addData('slider19.rt', slider19.getRT());
    psychoJS.experiment.addData('slider20.response', slider20.getRating());
    psychoJS.experiment.addData('slider20.rt', slider20.getRT());
    psychoJS.experiment.addData('slider21.response', slider21.getRating());
    psychoJS.experiment.addData('slider21.rt', slider21.getRT());
    psychoJS.experiment.addData('slider22.response', slider22.getRating());
    psychoJS.experiment.addData('slider22.rt', slider22.getRT());
    psychoJS.experiment.addData('slider23.response', slider23.getRating());
    psychoJS.experiment.addData('slider23.rt', slider23.getRT());
    psychoJS.experiment.addData('slider24.response', slider24.getRating());
    psychoJS.experiment.addData('slider24.rt', slider24.getRT());
    // the Routine "BRUMS_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrAXCPTbreak1Timer;
var _key_resp_2_allKeys;
var instrAXCPTbreak1Components;
function instrAXCPTbreak1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrAXCPTbreak1'-------
    t = 0;
    instrAXCPTbreak1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrAXCPTbreak1Timer = new util.Clock();
    
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instrAXCPTbreak1Components = [];
    instrAXCPTbreak1Components.push(key_resp_2);
    instrAXCPTbreak1Components.push(instrHeaderText_2);
    instrAXCPTbreak1Components.push(text_2);
    
    for (const thisComponent of instrAXCPTbreak1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrAXCPTbreak1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrAXCPTbreak1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrAXCPTbreak1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_2* updates
    if (t >= 0.0 && instrHeaderText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_2.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_2.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_2.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrAXCPTbreak1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrAXCPTbreak1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrAXCPTbreak1'-------
    for (const thisComponent of instrAXCPTbreak1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break1.duration", instrAXCPTbreak1Timer.getTime());
    instrAXCPTbreak1Timer = [];
    
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instrAXCPTbreak1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var loopTimer;
var createLoopTimerComponents;
function createLoopTimerRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'createLoopTimer'-------
    t = 0;
    createLoopTimerClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    loopTimer = new util.Clock();
    
    // keep track of which components have finished
    createLoopTimerComponents = [];
    
    for (const thisComponent of createLoopTimerComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function createLoopTimerRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'createLoopTimer'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = createLoopTimerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of createLoopTimerComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function createLoopTimerRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'createLoopTimer'-------
    for (const thisComponent of createLoopTimerComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "createLoopTimer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AXCPTtrialsLoop1;
var currentLoop;
function AXCPTtrialsLoop1LoopBegin(AXCPTtrialsLoop1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  AXCPTtrialsLoop1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialType.csv',
    seed: undefined, name: 'AXCPTtrialsLoop1'
  });
  psychoJS.experiment.addLoop(AXCPTtrialsLoop1); // add the loop to the experiment
  currentLoop = AXCPTtrialsLoop1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAXCPTtrialsLoop1 of AXCPTtrialsLoop1) {
    const snapshot = AXCPTtrialsLoop1.getSnapshot();
    AXCPTtrialsLoop1LoopScheduler.add(importConditions(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(timerRoutineBegin(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(timerRoutineEachFrame(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(timerRoutineEnd(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTtrialRoutineBegin(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTtrialRoutineEachFrame(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTtrialRoutineEnd(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTprobeRoutineBegin(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTprobeRoutineEachFrame(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTprobeRoutineEnd(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTfeedbackRoutineBegin(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTfeedbackRoutineEachFrame(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(AXCPTfeedbackRoutineEnd(snapshot));
    AXCPTtrialsLoop1LoopScheduler.add(endLoopIteration(AXCPTtrialsLoop1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function AXCPTtrialsLoop1LoopEnd() {
  psychoJS.experiment.removeLoop(AXCPTtrialsLoop1);

  return Scheduler.Event.NEXT;
}


var NBackTargetLoop1;
function NBackTargetLoop1LoopBegin(NBackTargetLoop1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTargetLoop1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'NBackTargetLoop1'
  });
  psychoJS.experiment.addLoop(NBackTargetLoop1); // add the loop to the experiment
  currentLoop = NBackTargetLoop1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTargetLoop1 of NBackTargetLoop1) {
    const snapshot = NBackTargetLoop1.getSnapshot();
    NBackTargetLoop1LoopScheduler.add(importConditions(snapshot));
    NBackTargetLoop1LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTargetLoop1LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTargetLoop1LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTargetLoop1LoopScheduler.add(NBackFirst3TrialsRoutineBegin(snapshot));
    NBackTargetLoop1LoopScheduler.add(NBackFirst3TrialsRoutineEachFrame(snapshot));
    NBackTargetLoop1LoopScheduler.add(NBackFirst3TrialsRoutineEnd(snapshot));
    NBackTargetLoop1LoopScheduler.add(endLoopIteration(NBackTargetLoop1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTargetLoop1LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTargetLoop1);

  return Scheduler.Event.NEXT;
}


var NBackTrialsLoop1;
function NBackTrialsLoop1LoopBegin(NBackTrialsLoop1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTrialsLoop1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: '2-back_loop.xlsx',
    seed: undefined, name: 'NBackTrialsLoop1'
  });
  psychoJS.experiment.addLoop(NBackTrialsLoop1); // add the loop to the experiment
  currentLoop = NBackTrialsLoop1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTrialsLoop1 of NBackTrialsLoop1) {
    const snapshot = NBackTrialsLoop1.getSnapshot();
    NBackTrialsLoop1LoopScheduler.add(importConditions(snapshot));
    NBackTrialsLoop1LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTrialsLoop1LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTrialsLoop1LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackRemainderTrialsRoutineBegin(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackRemainderTrialsRoutineEachFrame(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackRemainderTrialsRoutineEnd(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackFeedbackRoutineBegin(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackFeedbackRoutineEachFrame(snapshot));
    NBackTrialsLoop1LoopScheduler.add(NBackFeedbackRoutineEnd(snapshot));
    NBackTrialsLoop1LoopScheduler.add(endLoopIteration(NBackTrialsLoop1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTrialsLoop1LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTrialsLoop1);

  return Scheduler.Event.NEXT;
}


var searchLoop1;
function searchLoop1LoopBegin(searchLoop1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  searchLoop1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'visualSearchConds.csv',
    seed: undefined, name: 'searchLoop1'
  });
  psychoJS.experiment.addLoop(searchLoop1); // add the loop to the experiment
  currentLoop = searchLoop1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSearchLoop1 of searchLoop1) {
    const snapshot = searchLoop1.getSnapshot();
    searchLoop1LoopScheduler.add(importConditions(snapshot));
    searchLoop1LoopScheduler.add(timerRoutineBegin(snapshot));
    searchLoop1LoopScheduler.add(timerRoutineEachFrame(snapshot));
    searchLoop1LoopScheduler.add(timerRoutineEnd(snapshot));
    searchLoop1LoopScheduler.add(searchTrialRoutineBegin(snapshot));
    searchLoop1LoopScheduler.add(searchTrialRoutineEachFrame(snapshot));
    searchLoop1LoopScheduler.add(searchTrialRoutineEnd(snapshot));
    searchLoop1LoopScheduler.add(searchFeedbackRoutineBegin(snapshot));
    searchLoop1LoopScheduler.add(searchFeedbackRoutineEachFrame(snapshot));
    searchLoop1LoopScheduler.add(searchFeedbackRoutineEnd(snapshot));
    searchLoop1LoopScheduler.add(endLoopIteration(searchLoop1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function searchLoop1LoopEnd() {
  psychoJS.experiment.removeLoop(searchLoop1);

  return Scheduler.Event.NEXT;
}


var mentRotTrialsLoop1;
function mentRotTrialsLoop1LoopBegin(mentRotTrialsLoop1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  mentRotTrialsLoop1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'response.csv',
    seed: undefined, name: 'mentRotTrialsLoop1'
  });
  psychoJS.experiment.addLoop(mentRotTrialsLoop1); // add the loop to the experiment
  currentLoop = mentRotTrialsLoop1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMentRotTrialsLoop1 of mentRotTrialsLoop1) {
    const snapshot = mentRotTrialsLoop1.getSnapshot();
    mentRotTrialsLoop1LoopScheduler.add(importConditions(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(timerRoutineBegin(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(timerRoutineEachFrame(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(timerRoutineEnd(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotTrialRoutineBegin(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotTrialRoutineEachFrame(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotTrialRoutineEnd(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotFeedbackRoutineBegin(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotFeedbackRoutineEachFrame(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(mentRotFeedbackRoutineEnd(snapshot));
    mentRotTrialsLoop1LoopScheduler.add(endLoopIteration(mentRotTrialsLoop1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function mentRotTrialsLoop1LoopEnd() {
  psychoJS.experiment.removeLoop(mentRotTrialsLoop1);

  return Scheduler.Event.NEXT;
}


var NBackTargetLOOP2;
function NBackTargetLOOP2LoopBegin(NBackTargetLOOP2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTargetLOOP2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'NBackTargetLOOP2'
  });
  psychoJS.experiment.addLoop(NBackTargetLOOP2); // add the loop to the experiment
  currentLoop = NBackTargetLOOP2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTargetLOOP2 of NBackTargetLOOP2) {
    const snapshot = NBackTargetLOOP2.getSnapshot();
    NBackTargetLOOP2LoopScheduler.add(importConditions(snapshot));
    NBackTargetLOOP2LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTargetLOOP2LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTargetLOOP2LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTargetLOOP2LoopScheduler.add(NBackFirst3TrialsRoutineBegin(snapshot));
    NBackTargetLOOP2LoopScheduler.add(NBackFirst3TrialsRoutineEachFrame(snapshot));
    NBackTargetLOOP2LoopScheduler.add(NBackFirst3TrialsRoutineEnd(snapshot));
    NBackTargetLOOP2LoopScheduler.add(endLoopIteration(NBackTargetLOOP2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTargetLOOP2LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTargetLOOP2);

  return Scheduler.Event.NEXT;
}


var NBackTrialsLoop2;
function NBackTrialsLoop2LoopBegin(NBackTrialsLoop2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTrialsLoop2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: '2-back_loop.xlsx',
    seed: undefined, name: 'NBackTrialsLoop2'
  });
  psychoJS.experiment.addLoop(NBackTrialsLoop2); // add the loop to the experiment
  currentLoop = NBackTrialsLoop2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTrialsLoop2 of NBackTrialsLoop2) {
    const snapshot = NBackTrialsLoop2.getSnapshot();
    NBackTrialsLoop2LoopScheduler.add(importConditions(snapshot));
    NBackTrialsLoop2LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTrialsLoop2LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTrialsLoop2LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackRemainderTrialsRoutineBegin(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackRemainderTrialsRoutineEachFrame(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackRemainderTrialsRoutineEnd(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackFeedbackRoutineBegin(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackFeedbackRoutineEachFrame(snapshot));
    NBackTrialsLoop2LoopScheduler.add(NBackFeedbackRoutineEnd(snapshot));
    NBackTrialsLoop2LoopScheduler.add(endLoopIteration(NBackTrialsLoop2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTrialsLoop2LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTrialsLoop2);

  return Scheduler.Event.NEXT;
}


var AXCPTtrialsLoop2;
function AXCPTtrialsLoop2LoopBegin(AXCPTtrialsLoop2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  AXCPTtrialsLoop2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialType.csv',
    seed: undefined, name: 'AXCPTtrialsLoop2'
  });
  psychoJS.experiment.addLoop(AXCPTtrialsLoop2); // add the loop to the experiment
  currentLoop = AXCPTtrialsLoop2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAXCPTtrialsLoop2 of AXCPTtrialsLoop2) {
    const snapshot = AXCPTtrialsLoop2.getSnapshot();
    AXCPTtrialsLoop2LoopScheduler.add(importConditions(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(timerRoutineBegin(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(timerRoutineEachFrame(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(timerRoutineEnd(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTtrialRoutineBegin(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTtrialRoutineEachFrame(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTtrialRoutineEnd(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTprobeRoutineBegin(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTprobeRoutineEachFrame(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTprobeRoutineEnd(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTfeedbackRoutineBegin(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTfeedbackRoutineEachFrame(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(AXCPTfeedbackRoutineEnd(snapshot));
    AXCPTtrialsLoop2LoopScheduler.add(endLoopIteration(AXCPTtrialsLoop2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function AXCPTtrialsLoop2LoopEnd() {
  psychoJS.experiment.removeLoop(AXCPTtrialsLoop2);

  return Scheduler.Event.NEXT;
}


var searchLoop2;
function searchLoop2LoopBegin(searchLoop2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  searchLoop2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'visualSearchConds.csv',
    seed: undefined, name: 'searchLoop2'
  });
  psychoJS.experiment.addLoop(searchLoop2); // add the loop to the experiment
  currentLoop = searchLoop2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSearchLoop2 of searchLoop2) {
    const snapshot = searchLoop2.getSnapshot();
    searchLoop2LoopScheduler.add(importConditions(snapshot));
    searchLoop2LoopScheduler.add(timerRoutineBegin(snapshot));
    searchLoop2LoopScheduler.add(timerRoutineEachFrame(snapshot));
    searchLoop2LoopScheduler.add(timerRoutineEnd(snapshot));
    searchLoop2LoopScheduler.add(searchTrialRoutineBegin(snapshot));
    searchLoop2LoopScheduler.add(searchTrialRoutineEachFrame(snapshot));
    searchLoop2LoopScheduler.add(searchTrialRoutineEnd(snapshot));
    searchLoop2LoopScheduler.add(searchFeedbackRoutineBegin(snapshot));
    searchLoop2LoopScheduler.add(searchFeedbackRoutineEachFrame(snapshot));
    searchLoop2LoopScheduler.add(searchFeedbackRoutineEnd(snapshot));
    searchLoop2LoopScheduler.add(endLoopIteration(searchLoop2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function searchLoop2LoopEnd() {
  psychoJS.experiment.removeLoop(searchLoop2);

  return Scheduler.Event.NEXT;
}


var mentRotTrialsLoop2;
function mentRotTrialsLoop2LoopBegin(mentRotTrialsLoop2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  mentRotTrialsLoop2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'response.csv',
    seed: undefined, name: 'mentRotTrialsLoop2'
  });
  psychoJS.experiment.addLoop(mentRotTrialsLoop2); // add the loop to the experiment
  currentLoop = mentRotTrialsLoop2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMentRotTrialsLoop2 of mentRotTrialsLoop2) {
    const snapshot = mentRotTrialsLoop2.getSnapshot();
    mentRotTrialsLoop2LoopScheduler.add(importConditions(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotTrialRoutineBegin(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotTrialRoutineEachFrame(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotTrialRoutineEnd(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotFeedbackRoutineBegin(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotFeedbackRoutineEachFrame(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(mentRotFeedbackRoutineEnd(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(timerRoutineBegin(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(timerRoutineEachFrame(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(timerRoutineEnd(snapshot));
    mentRotTrialsLoop2LoopScheduler.add(endLoopIteration(mentRotTrialsLoop2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function mentRotTrialsLoop2LoopEnd() {
  psychoJS.experiment.removeLoop(mentRotTrialsLoop2);

  return Scheduler.Event.NEXT;
}


var NBackTargetLoop3;
function NBackTargetLoop3LoopBegin(NBackTargetLoop3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTargetLoop3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'NBackTargetLoop3'
  });
  psychoJS.experiment.addLoop(NBackTargetLoop3); // add the loop to the experiment
  currentLoop = NBackTargetLoop3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTargetLoop3 of NBackTargetLoop3) {
    const snapshot = NBackTargetLoop3.getSnapshot();
    NBackTargetLoop3LoopScheduler.add(importConditions(snapshot));
    NBackTargetLoop3LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTargetLoop3LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTargetLoop3LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTargetLoop3LoopScheduler.add(NBackFirst3TrialsRoutineBegin(snapshot));
    NBackTargetLoop3LoopScheduler.add(NBackFirst3TrialsRoutineEachFrame(snapshot));
    NBackTargetLoop3LoopScheduler.add(NBackFirst3TrialsRoutineEnd(snapshot));
    NBackTargetLoop3LoopScheduler.add(endLoopIteration(NBackTargetLoop3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTargetLoop3LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTargetLoop3);

  return Scheduler.Event.NEXT;
}


var NBackTrialsLoop3;
function NBackTrialsLoop3LoopBegin(NBackTrialsLoop3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  NBackTrialsLoop3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: '2-back_loop.xlsx',
    seed: undefined, name: 'NBackTrialsLoop3'
  });
  psychoJS.experiment.addLoop(NBackTrialsLoop3); // add the loop to the experiment
  currentLoop = NBackTrialsLoop3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisNBackTrialsLoop3 of NBackTrialsLoop3) {
    const snapshot = NBackTrialsLoop3.getSnapshot();
    NBackTrialsLoop3LoopScheduler.add(importConditions(snapshot));
    NBackTrialsLoop3LoopScheduler.add(timerRoutineBegin(snapshot));
    NBackTrialsLoop3LoopScheduler.add(timerRoutineEachFrame(snapshot));
    NBackTrialsLoop3LoopScheduler.add(timerRoutineEnd(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackRemainderTrialsRoutineBegin(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackRemainderTrialsRoutineEachFrame(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackRemainderTrialsRoutineEnd(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackFeedbackRoutineBegin(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackFeedbackRoutineEachFrame(snapshot));
    NBackTrialsLoop3LoopScheduler.add(NBackFeedbackRoutineEnd(snapshot));
    NBackTrialsLoop3LoopScheduler.add(endLoopIteration(NBackTrialsLoop3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function NBackTrialsLoop3LoopEnd() {
  psychoJS.experiment.removeLoop(NBackTrialsLoop3);

  return Scheduler.Event.NEXT;
}


var searchLoop3;
function searchLoop3LoopBegin(searchLoop3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  searchLoop3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'visualSearchConds.csv',
    seed: undefined, name: 'searchLoop3'
  });
  psychoJS.experiment.addLoop(searchLoop3); // add the loop to the experiment
  currentLoop = searchLoop3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSearchLoop3 of searchLoop3) {
    const snapshot = searchLoop3.getSnapshot();
    searchLoop3LoopScheduler.add(importConditions(snapshot));
    searchLoop3LoopScheduler.add(timerRoutineBegin(snapshot));
    searchLoop3LoopScheduler.add(timerRoutineEachFrame(snapshot));
    searchLoop3LoopScheduler.add(timerRoutineEnd(snapshot));
    searchLoop3LoopScheduler.add(searchTrialRoutineBegin(snapshot));
    searchLoop3LoopScheduler.add(searchTrialRoutineEachFrame(snapshot));
    searchLoop3LoopScheduler.add(searchTrialRoutineEnd(snapshot));
    searchLoop3LoopScheduler.add(searchFeedbackRoutineBegin(snapshot));
    searchLoop3LoopScheduler.add(searchFeedbackRoutineEachFrame(snapshot));
    searchLoop3LoopScheduler.add(searchFeedbackRoutineEnd(snapshot));
    searchLoop3LoopScheduler.add(endLoopIteration(searchLoop3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function searchLoop3LoopEnd() {
  psychoJS.experiment.removeLoop(searchLoop3);

  return Scheduler.Event.NEXT;
}


var mentRotTrialsLoop3;
function mentRotTrialsLoop3LoopBegin(mentRotTrialsLoop3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  mentRotTrialsLoop3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'response.csv',
    seed: undefined, name: 'mentRotTrialsLoop3'
  });
  psychoJS.experiment.addLoop(mentRotTrialsLoop3); // add the loop to the experiment
  currentLoop = mentRotTrialsLoop3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMentRotTrialsLoop3 of mentRotTrialsLoop3) {
    const snapshot = mentRotTrialsLoop3.getSnapshot();
    mentRotTrialsLoop3LoopScheduler.add(importConditions(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotTrialRoutineBegin(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotTrialRoutineEachFrame(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotTrialRoutineEnd(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotFeedbackRoutineBegin(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotFeedbackRoutineEachFrame(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(mentRotFeedbackRoutineEnd(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(timerRoutineBegin(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(timerRoutineEachFrame(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(timerRoutineEnd(snapshot));
    mentRotTrialsLoop3LoopScheduler.add(endLoopIteration(mentRotTrialsLoop3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function mentRotTrialsLoop3LoopEnd() {
  psychoJS.experiment.removeLoop(mentRotTrialsLoop3);

  return Scheduler.Event.NEXT;
}


var AXCPTtrialsLoop3;
function AXCPTtrialsLoop3LoopBegin(AXCPTtrialsLoop3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  AXCPTtrialsLoop3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialType.csv',
    seed: undefined, name: 'AXCPTtrialsLoop3'
  });
  psychoJS.experiment.addLoop(AXCPTtrialsLoop3); // add the loop to the experiment
  currentLoop = AXCPTtrialsLoop3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAXCPTtrialsLoop3 of AXCPTtrialsLoop3) {
    const snapshot = AXCPTtrialsLoop3.getSnapshot();
    AXCPTtrialsLoop3LoopScheduler.add(importConditions(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(timerRoutineBegin(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(timerRoutineEachFrame(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(timerRoutineEnd(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTtrialRoutineBegin(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTtrialRoutineEachFrame(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTtrialRoutineEnd(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTprobeRoutineBegin(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTprobeRoutineEachFrame(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTprobeRoutineEnd(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTfeedbackRoutineBegin(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTfeedbackRoutineEachFrame(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(AXCPTfeedbackRoutineEnd(snapshot));
    AXCPTtrialsLoop3LoopScheduler.add(endLoopIteration(AXCPTtrialsLoop3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function AXCPTtrialsLoop3LoopEnd() {
  psychoJS.experiment.removeLoop(AXCPTtrialsLoop3);

  return Scheduler.Event.NEXT;
}


var timerComponents;
function timerRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'timer'-------
    t = 0;
    timerClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    timerComponents = [];
    timerComponents.push(timer_text);
    
    for (const thisComponent of timerComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function timerRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'timer'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = timerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((loopTimer.getTime() > 600)) {
        currentLoop.finished = true;
    }
    
    
    // *timer_text* updates
    if (t >= 0.0 && timer_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_text.tStart = t;  // (not accounting for frame time here)
      timer_text.frameNStart = frameN;  // exact frame index
      
      timer_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timer_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timer_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of timerComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function timerRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'timer'-------
    for (const thisComponent of timerComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    
    return Scheduler.Event.NEXT;
  };
}


var distractor1Val;
var distractor2Val;
var cueVal;
var AXCPTtrialComponents;
function AXCPTtrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AXCPTtrial'-------
    t = 0;
    AXCPTtrialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.500000);
    // update component parameters for each repeat
    function choice(arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    }
    
    distractor1Val = choice(distractors);
    distractor2Val = choice(distractors);
    if ((trialType === "target")) {
        cueVal = "A";
        probeVal = "X";
    } else {
        if ((trialType === "probeWrong")) {
            cueVal = "A";
            probeVal = choice(Yletters);
        } else {
            if ((trialType === "cueWrong")) {
                cueVal = choice(Bletters);
                probeVal = "X";
            } else {
                if ((trialType === "bothWrong")) {
                    cueVal = choice(Bletters);
                    probeVal = choice(Yletters);
                }
            }
        }
    }
    
    cue_text.setText(cueVal);
    distractor1.setText(distractor1Val);
    distractor2.setText(distractor2Val);
    // keep track of which components have finished
    AXCPTtrialComponents = [];
    AXCPTtrialComponents.push(cue_text);
    AXCPTtrialComponents.push(break1);
    AXCPTtrialComponents.push(distractor1);
    AXCPTtrialComponents.push(break2);
    AXCPTtrialComponents.push(distractor2);
    AXCPTtrialComponents.push(break3);
    
    for (const thisComponent of AXCPTtrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function AXCPTtrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AXCPTtrial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AXCPTtrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue_text* updates
    if (t >= 0.0 && cue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_text.tStart = t;  // (not accounting for frame time here)
      cue_text.frameNStart = frameN;  // exact frame index
      
      cue_text.setAutoDraw(true);
    }

    frameRemains = 0.3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_text.setAutoDraw(false);
    }
    
    // *break1* updates
    if (t >= 0.3 && break1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break1.tStart = t;  // (not accounting for frame time here)
      break1.frameNStart = frameN;  // exact frame index
      
      break1.setAutoDraw(true);
    }

    frameRemains = 0.3 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (break1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      break1.setAutoDraw(false);
    }
    
    // *distractor1* updates
    if (t >= 1.5 && distractor1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor1.tStart = t;  // (not accounting for frame time here)
      distractor1.frameNStart = frameN;  // exact frame index
      
      distractor1.setAutoDraw(true);
    }

    frameRemains = 1.8  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distractor1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distractor1.setAutoDraw(false);
    }
    
    // *break2* updates
    if (t >= 1.8 && break2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break2.tStart = t;  // (not accounting for frame time here)
      break2.frameNStart = frameN;  // exact frame index
      
      break2.setAutoDraw(true);
    }

    frameRemains = 1.8 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (break2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      break2.setAutoDraw(false);
    }
    
    // *distractor2* updates
    if (t >= 3 && distractor2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor2.tStart = t;  // (not accounting for frame time here)
      distractor2.frameNStart = frameN;  // exact frame index
      
      distractor2.setAutoDraw(true);
    }

    frameRemains = 3.3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distractor2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distractor2.setAutoDraw(false);
    }
    
    // *break3* updates
    if (t >= 3.3 && break3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break3.tStart = t;  // (not accounting for frame time here)
      break3.frameNStart = frameN;  // exact frame index
      
      break3.setAutoDraw(true);
    }

    frameRemains = 3.3 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (break3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      break3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AXCPTtrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AXCPTtrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AXCPTtrial'-------
    for (const thisComponent of AXCPTtrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _AXCPT_resp_allKeys;
var AXCPTprobeComponents;
function AXCPTprobeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AXCPTprobe'-------
    t = 0;
    AXCPTprobeClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    probe_text.setText(probeVal);
    AXCPT_resp.keys = undefined;
    AXCPT_resp.rt = undefined;
    _AXCPT_resp_allKeys = [];
    // keep track of which components have finished
    AXCPTprobeComponents = [];
    AXCPTprobeComponents.push(probe_text);
    AXCPTprobeComponents.push(AXCPT_resp);
    
    for (const thisComponent of AXCPTprobeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function AXCPTprobeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AXCPTprobe'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AXCPTprobeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *probe_text* updates
    if (t >= 0.0 && probe_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_text.tStart = t;  // (not accounting for frame time here)
      probe_text.frameNStart = frameN;  // exact frame index
      
      probe_text.setAutoDraw(true);
    }

    frameRemains = 0.3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (probe_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      probe_text.setAutoDraw(false);
    }
    
    // *AXCPT_resp* updates
    if (t >= 0.0 && AXCPT_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AXCPT_resp.tStart = t;  // (not accounting for frame time here)
      AXCPT_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { AXCPT_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { AXCPT_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { AXCPT_resp.clearEvents(); });
    }

    frameRemains = 1.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AXCPT_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AXCPT_resp.status = PsychoJS.Status.FINISHED;
  }

    if (AXCPT_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = AXCPT_resp.getKeys({keyList: ['k', 'd'], waitRelease: false});
      _AXCPT_resp_allKeys = _AXCPT_resp_allKeys.concat(theseKeys);
      if (_AXCPT_resp_allKeys.length > 0) {
        AXCPT_resp.keys = _AXCPT_resp_allKeys[_AXCPT_resp_allKeys.length - 1].name;  // just the last key pressed
        AXCPT_resp.rt = _AXCPT_resp_allKeys[_AXCPT_resp_allKeys.length - 1].rt;
        // was this correct?
        if (AXCPT_resp.keys == corrResponse) {
            AXCPT_resp.corr = 1;
        } else {
            AXCPT_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AXCPTprobeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AXCPTprobeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AXCPTprobe'-------
    for (const thisComponent of AXCPTprobeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (AXCPT_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrResponse)) {
         AXCPT_resp.corr = 1;  // correct non-response
      } else {
         AXCPT_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('AXCPT_resp.keys', AXCPT_resp.keys);
    psychoJS.experiment.addData('AXCPT_resp.corr', AXCPT_resp.corr);
    if (typeof AXCPT_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('AXCPT_resp.rt', AXCPT_resp.rt);
        routineTimer.reset();
        }
    
    AXCPT_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var AXCPTfeedbackComponents;
function AXCPTfeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AXCPTfeedback'-------
    t = 0;
    AXCPTfeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (AXCPT_resp.corr) {
        msg = "Correct";
    } else {
        msg = "Incorrect";
    }
    
    AXCPTfeedback_text.setText(msg);
    // keep track of which components have finished
    AXCPTfeedbackComponents = [];
    AXCPTfeedbackComponents.push(AXCPTfeedback_text);
    
    for (const thisComponent of AXCPTfeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function AXCPTfeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AXCPTfeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AXCPTfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AXCPTfeedback_text* updates
    if (t >= 0.0 && AXCPTfeedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AXCPTfeedback_text.tStart = t;  // (not accounting for frame time here)
      AXCPTfeedback_text.frameNStart = frameN;  // exact frame index
      
      AXCPTfeedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AXCPTfeedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AXCPTfeedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AXCPTfeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AXCPTfeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AXCPTfeedback'-------
    for (const thisComponent of AXCPTfeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var instrNBACKbreak2Timer;
var _key_resp_3_allKeys;
var instrNBACKbreak2Components;
function instrNBACKbreak2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrNBACKbreak2'-------
    t = 0;
    instrNBACKbreak2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrNBACKbreak2Timer = new util.Clock();
    
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    text_3.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrNBACKbreak2Components = [];
    instrNBACKbreak2Components.push(key_resp_3);
    instrNBACKbreak2Components.push(instrHeaderText_3);
    instrNBACKbreak2Components.push(text_3);
    
    for (const thisComponent of instrNBACKbreak2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrNBACKbreak2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrNBACKbreak2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrNBACKbreak2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 0.5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_3* updates
    if (t >= 0.0 && instrHeaderText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_3.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_3.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_3.setAutoDraw(true);
    }

    
    // *text_3* updates
    if (t >= 0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrNBACKbreak2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrNBACKbreak2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrNBACKbreak2'-------
    for (const thisComponent of instrNBACKbreak2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break2.duration", instrNBACKbreak2Timer.getTime());
    instrNBACKbreak2Timer = [];
    
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "instrNBACKbreak2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var letters;
var nletter;
var _NBack_resp_1_allKeys;
var NBackFirst3TrialsComponents;
function NBackFirst3TrialsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'NBackFirst3Trials'-------
    t = 0;
    NBackFirst3TrialsClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    function choice(arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    }
    
    letters = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"];
    nletter = choice(letters);
    
    NBackText_1.setText(nletter);
    NBack_resp_1.keys = undefined;
    NBack_resp_1.rt = undefined;
    _NBack_resp_1_allKeys = [];
    // keep track of which components have finished
    NBackFirst3TrialsComponents = [];
    NBackFirst3TrialsComponents.push(NBackText_1);
    NBackFirst3TrialsComponents.push(NBack_resp_1);
    
    for (const thisComponent of NBackFirst3TrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function NBackFirst3TrialsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'NBackFirst3Trials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = NBackFirst3TrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NBackText_1* updates
    if (t >= 0.0 && NBackText_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NBackText_1.tStart = t;  // (not accounting for frame time here)
      NBackText_1.frameNStart = frameN;  // exact frame index
      
      NBackText_1.setAutoDraw(true);
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (NBackText_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      NBackText_1.setAutoDraw(false);
    }
    
    // *NBack_resp_1* updates
    if (t >= 0.0 && NBack_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NBack_resp_1.tStart = t;  // (not accounting for frame time here)
      NBack_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NBack_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NBack_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NBack_resp_1.clearEvents(); });
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (NBack_resp_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      NBack_resp_1.status = PsychoJS.Status.FINISHED;
  }

    if (NBack_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = NBack_resp_1.getKeys({keyList: ['k', 'd'], waitRelease: false});
      _NBack_resp_1_allKeys = _NBack_resp_1_allKeys.concat(theseKeys);
      if (_NBack_resp_1_allKeys.length > 0) {
        NBack_resp_1.keys = _NBack_resp_1_allKeys[_NBack_resp_1_allKeys.length - 1].name;  // just the last key pressed
        NBack_resp_1.rt = _NBack_resp_1_allKeys[_NBack_resp_1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NBackFirst3TrialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NBackFirst3TrialsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'NBackFirst3Trials'-------
    for (const thisComponent of NBackFirst3TrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Back2minus3 = Back2minus2;
    Back2minus2 = Back2minus1;
    Back2minus1 = nletter;
    
    psychoJS.experiment.addData('NBack_resp_1.keys', NBack_resp_1.keys);
    if (typeof NBack_resp_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NBack_resp_1.rt', NBack_resp_1.rt);
        routineTimer.reset();
        }
    
    NBack_resp_1.stop();
    return Scheduler.Event.NEXT;
  };
}


var _NBack_resp_2_allKeys;
var NBackRemainderTrialsComponents;
function NBackRemainderTrialsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'NBackRemainderTrials'-------
    t = 0;
    NBackRemainderTrialsClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    function choice(arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    }
    
    if ((trialType === "nonTarget")) {
        letters = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"];
        nletter = choice(letters);
        if ((nletter === Back2minus1)) {
            nletter = choice(letters);
        }
        if ((nletter === Back2minus2)) {
            nletter = choice(letters);
        }
    } else {
        if ((trialType === "target")) {
            nletter = Back2minus3;
        }
    }
    
    NBackText_2.setText(nletter);
    NBack_resp_2.keys = undefined;
    NBack_resp_2.rt = undefined;
    _NBack_resp_2_allKeys = [];
    // keep track of which components have finished
    NBackRemainderTrialsComponents = [];
    NBackRemainderTrialsComponents.push(NBackText_2);
    NBackRemainderTrialsComponents.push(NBack_resp_2);
    
    for (const thisComponent of NBackRemainderTrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function NBackRemainderTrialsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'NBackRemainderTrials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = NBackRemainderTrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NBackText_2* updates
    if (t >= 0.0 && NBackText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NBackText_2.tStart = t;  // (not accounting for frame time here)
      NBackText_2.frameNStart = frameN;  // exact frame index
      
      NBackText_2.setAutoDraw(true);
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (NBackText_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      NBackText_2.setAutoDraw(false);
    }
    
    // *NBack_resp_2* updates
    if (t >= 0.0 && NBack_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NBack_resp_2.tStart = t;  // (not accounting for frame time here)
      NBack_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NBack_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NBack_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NBack_resp_2.clearEvents(); });
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (NBack_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      NBack_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (NBack_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = NBack_resp_2.getKeys({keyList: ['k', 'd'], waitRelease: false});
      _NBack_resp_2_allKeys = _NBack_resp_2_allKeys.concat(theseKeys);
      if (_NBack_resp_2_allKeys.length > 0) {
        NBack_resp_2.keys = _NBack_resp_2_allKeys[_NBack_resp_2_allKeys.length - 1].name;  // just the last key pressed
        NBack_resp_2.rt = _NBack_resp_2_allKeys[_NBack_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (NBack_resp_2.keys == corrResponse) {
            NBack_resp_2.corr = 1;
        } else {
            NBack_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NBackRemainderTrialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NBackRemainderTrialsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'NBackRemainderTrials'-------
    for (const thisComponent of NBackRemainderTrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Back2minus3 = Back2minus2;
    Back2minus2 = Back2minus1;
    Back2minus1 = nletter;
    
    // was no response the correct answer?!
    if (NBack_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrResponse)) {
         NBack_resp_2.corr = 1;  // correct non-response
      } else {
         NBack_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('NBack_resp_2.keys', NBack_resp_2.keys);
    psychoJS.experiment.addData('NBack_resp_2.corr', NBack_resp_2.corr);
    if (typeof NBack_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NBack_resp_2.rt', NBack_resp_2.rt);
        routineTimer.reset();
        }
    
    NBack_resp_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var NBackFeedbackComponents;
function NBackFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'NBackFeedback'-------
    t = 0;
    NBackFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (NBack_resp_2.corr) {
        msg = "Correct";
    } else {
        msg = "Incorrect";
    }
    
    AXCPTfeedback_text_2.setText(msg);
    // keep track of which components have finished
    NBackFeedbackComponents = [];
    NBackFeedbackComponents.push(AXCPTfeedback_text_2);
    
    for (const thisComponent of NBackFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function NBackFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'NBackFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = NBackFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AXCPTfeedback_text_2* updates
    if (t >= 0.0 && AXCPTfeedback_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AXCPTfeedback_text_2.tStart = t;  // (not accounting for frame time here)
      AXCPTfeedback_text_2.frameNStart = frameN;  // exact frame index
      
      AXCPTfeedback_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AXCPTfeedback_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AXCPTfeedback_text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NBackFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NBackFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'NBackFeedback'-------
    for (const thisComponent of NBackFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var instrSEARCHbreak3Timer;
var _key_resp_4_allKeys;
var instrSEARCHbreak3Components;
function instrSEARCHbreak3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrSEARCHbreak3'-------
    t = 0;
    instrSEARCHbreak3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrSEARCHbreak3Timer = new util.Clock();
    
    text_5.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin");
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    instrSEARCHbreak3Components = [];
    instrSEARCHbreak3Components.push(instrHeaderText_5);
    instrSEARCHbreak3Components.push(text_5);
    instrSEARCHbreak3Components.push(key_resp_4);
    
    for (const thisComponent of instrSEARCHbreak3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrSEARCHbreak3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrSEARCHbreak3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrSEARCHbreak3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrHeaderText_5* updates
    if (t >= 0.0 && instrHeaderText_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_5.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_5.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_5.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.5 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrSEARCHbreak3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrSEARCHbreak3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrSEARCHbreak3'-------
    for (const thisComponent of instrSEARCHbreak3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break3.duration", instrSEARCHbreak3Timer.getTime());
    instrSEARCHbreak3Timer = [];
    
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "instrSEARCHbreak3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var targetOrient;
var stim2Orient;
var stim3Orient;
var stim4Orient;
var stim5Orient;
var stim6Orient;
var stim7Orient;
var stim8Orient;
var stim9Orient;
var stim10Orient;
var stim11Orient;
var _key_resp_14_allKeys;
var searchTrialComponents;
function searchTrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'searchTrial'-------
    t = 0;
    searchTrialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    shuffle = util.shuffle
    
    function choice(arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    }
    shuffle(PosList);
    targetOrient = choice(orientList);
    stim2Orient = choice(orientList);
    stim3Orient = choice(orientList);
    stim4Orient = choice(orientList);
    stim5Orient = choice(orientList);
    stim6Orient = choice(orientList);
    stim7Orient = choice(orientList);
    stim8Orient = choice(orientList);
    stim9Orient = choice(orientList);
    stim10Orient = choice(orientList);
    stim11Orient = choice(orientList);
    
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    targetStim.setPos(PosList[1]);
    targetStim.setOri(targetOrient);
    targetStim.setText(targetLetter);
    searchStim2.setPos(PosList[2]);
    searchStim2.setOri(stim2Orient);
    searchStim2.setText('L');
    searchStim3.setPos(PosList[3]);
    searchStim3.setOri(stim3Orient);
    searchStim3.setText('L');
    searchStim4.setPos(PosList[4]);
    searchStim4.setOri(stim4Orient);
    searchStim4.setText('L');
    searchStim5.setPos(PosList[5]);
    searchStim5.setOri(stim5Orient);
    searchStim5.setText('L');
    searchStim6.setPos(PosList[6]);
    searchStim6.setOri(stim6Orient);
    searchStim6.setText('L');
    searchStim7.setPos(PosList[7]);
    searchStim7.setOri(stim7Orient);
    searchStim7.setText('L');
    searchStim8.setPos(PosList[8]);
    searchStim8.setOri(stim8Orient);
    searchStim8.setText('L');
    searchStim9.setPos(PosList[9]);
    searchStim9.setOri(stim9Orient);
    searchStim9.setText('L');
    searchStim10.setPos(PosList[10]);
    searchStim10.setOri(stim10Orient);
    searchStim10.setText('L');
    searchStim11.setPos(PosList[11]);
    searchStim11.setOri(stim11Orient);
    searchStim11.setText('L');
    // keep track of which components have finished
    searchTrialComponents = [];
    searchTrialComponents.push(key_resp_14);
    searchTrialComponents.push(targetStim);
    searchTrialComponents.push(searchStim2);
    searchTrialComponents.push(searchStim3);
    searchTrialComponents.push(searchStim4);
    searchTrialComponents.push(searchStim5);
    searchTrialComponents.push(searchStim6);
    searchTrialComponents.push(searchStim7);
    searchTrialComponents.push(searchStim8);
    searchTrialComponents.push(searchStim9);
    searchTrialComponents.push(searchStim10);
    searchTrialComponents.push(searchStim11);
    
    for (const thisComponent of searchTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function searchTrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'searchTrial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = searchTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }

    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['k', 'd'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_14.keys == corrResponse) {
            key_resp_14.corr = 1;
        } else {
            key_resp_14.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *targetStim* updates
    if (t >= 0.0 && targetStim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetStim.tStart = t;  // (not accounting for frame time here)
      targetStim.frameNStart = frameN;  // exact frame index
      
      targetStim.setAutoDraw(true);
    }

    
    // *searchStim2* updates
    if (t >= 0.0 && searchStim2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim2.tStart = t;  // (not accounting for frame time here)
      searchStim2.frameNStart = frameN;  // exact frame index
      
      searchStim2.setAutoDraw(true);
    }

    
    // *searchStim3* updates
    if (t >= 0.0 && searchStim3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim3.tStart = t;  // (not accounting for frame time here)
      searchStim3.frameNStart = frameN;  // exact frame index
      
      searchStim3.setAutoDraw(true);
    }

    
    // *searchStim4* updates
    if (t >= 0.0 && searchStim4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim4.tStart = t;  // (not accounting for frame time here)
      searchStim4.frameNStart = frameN;  // exact frame index
      
      searchStim4.setAutoDraw(true);
    }

    
    // *searchStim5* updates
    if (t >= 0.0 && searchStim5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim5.tStart = t;  // (not accounting for frame time here)
      searchStim5.frameNStart = frameN;  // exact frame index
      
      searchStim5.setAutoDraw(true);
    }

    
    // *searchStim6* updates
    if (t >= 0.0 && searchStim6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim6.tStart = t;  // (not accounting for frame time here)
      searchStim6.frameNStart = frameN;  // exact frame index
      
      searchStim6.setAutoDraw(true);
    }

    
    // *searchStim7* updates
    if (t >= 0.0 && searchStim7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim7.tStart = t;  // (not accounting for frame time here)
      searchStim7.frameNStart = frameN;  // exact frame index
      
      searchStim7.setAutoDraw(true);
    }

    
    // *searchStim8* updates
    if (t >= 0.0 && searchStim8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim8.tStart = t;  // (not accounting for frame time here)
      searchStim8.frameNStart = frameN;  // exact frame index
      
      searchStim8.setAutoDraw(true);
    }

    
    // *searchStim9* updates
    if (t >= 0.0 && searchStim9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim9.tStart = t;  // (not accounting for frame time here)
      searchStim9.frameNStart = frameN;  // exact frame index
      
      searchStim9.setAutoDraw(true);
    }

    
    // *searchStim10* updates
    if (t >= 0.0 && searchStim10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim10.tStart = t;  // (not accounting for frame time here)
      searchStim10.frameNStart = frameN;  // exact frame index
      
      searchStim10.setAutoDraw(true);
    }

    
    // *searchStim11* updates
    if (t >= 0.0 && searchStim11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchStim11.tStart = t;  // (not accounting for frame time here)
      searchStim11.frameNStart = frameN;  // exact frame index
      
      searchStim11.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of searchTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function searchTrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'searchTrial'-------
    for (const thisComponent of searchTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_14.keys === undefined) {
      if (['None','none',undefined].includes(corrResponse)) {
         key_resp_14.corr = 1;  // correct non-response
      } else {
         key_resp_14.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    psychoJS.experiment.addData('key_resp_14.corr', key_resp_14.corr);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "searchTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var searchFeedbackComponents;
function searchFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'searchFeedback'-------
    t = 0;
    searchFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (key_resp_14.corr) {
        msg = "Correct";
    } else {
        msg = "Incorrect";
    }
    
    searchFeedbackText.setText(msg);
    // keep track of which components have finished
    searchFeedbackComponents = [];
    searchFeedbackComponents.push(searchFeedbackText);
    
    for (const thisComponent of searchFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function searchFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'searchFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = searchFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *searchFeedbackText* updates
    if (t >= 0.0 && searchFeedbackText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchFeedbackText.tStart = t;  // (not accounting for frame time here)
      searchFeedbackText.frameNStart = frameN;  // exact frame index
      
      searchFeedbackText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (searchFeedbackText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      searchFeedbackText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of searchFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function searchFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'searchFeedback'-------
    for (const thisComponent of searchFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var instrMENTROTbreak4Timer;
var _key_resp_13_allKeys;
var instrMENTROTbreak4Components;
function instrMENTROTbreak4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrMENTROTbreak4'-------
    t = 0;
    instrMENTROTbreak4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrMENTROTbreak4Timer = new util.Clock();
    
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    text_21.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrMENTROTbreak4Components = [];
    instrMENTROTbreak4Components.push(key_resp_13);
    instrMENTROTbreak4Components.push(instrHeaderText_15);
    instrMENTROTbreak4Components.push(text_21);
    
    for (const thisComponent of instrMENTROTbreak4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrMENTROTbreak4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrMENTROTbreak4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrMENTROTbreak4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_13* updates
    if (t >= 0.5 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }

    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_15* updates
    if (t >= 0.0 && instrHeaderText_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_15.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_15.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_15.setAutoDraw(true);
    }

    
    // *text_21* updates
    if (t >= 0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrMENTROTbreak4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrMENTROTbreak4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrMENTROTbreak4'-------
    for (const thisComponent of instrMENTROTbreak4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break4.duration", instrMENTROTbreak4Timer.getTime());
    instrMENTROTbreak4Timer = [];
    
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "instrMENTROTbreak4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _MROT_resp_allKeys;
var mentRotTrialComponents;
function mentRotTrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'mentRotTrial'-------
    t = 0;
    mentRotTrialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(7.500000);
    // update component parameters for each repeat
    mentRotStimulus.setImage(imagefile);
    MROT_resp.keys = undefined;
    MROT_resp.rt = undefined;
    _MROT_resp_allKeys = [];
    // keep track of which components have finished
    mentRotTrialComponents = [];
    mentRotTrialComponents.push(mentRotStimulus);
    mentRotTrialComponents.push(MROT_resp);
    
    for (const thisComponent of mentRotTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function mentRotTrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'mentRotTrial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = mentRotTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mentRotStimulus* updates
    if (t >= 0.0 && mentRotStimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mentRotStimulus.tStart = t;  // (not accounting for frame time here)
      mentRotStimulus.frameNStart = frameN;  // exact frame index
      
      mentRotStimulus.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mentRotStimulus.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mentRotStimulus.setAutoDraw(false);
    }
    
    // *MROT_resp* updates
    if (t >= 0.0 && MROT_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MROT_resp.tStart = t;  // (not accounting for frame time here)
      MROT_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MROT_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MROT_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MROT_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 7.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (MROT_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      MROT_resp.status = PsychoJS.Status.FINISHED;
  }

    if (MROT_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = MROT_resp.getKeys({keyList: ['k', 'd'], waitRelease: false});
      _MROT_resp_allKeys = _MROT_resp_allKeys.concat(theseKeys);
      if (_MROT_resp_allKeys.length > 0) {
        MROT_resp.keys = _MROT_resp_allKeys[_MROT_resp_allKeys.length - 1].name;  // just the last key pressed
        MROT_resp.rt = _MROT_resp_allKeys[_MROT_resp_allKeys.length - 1].rt;
        // was this correct?
        if (MROT_resp.keys == corrResponse) {
            MROT_resp.corr = 1;
        } else {
            MROT_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of mentRotTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mentRotTrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'mentRotTrial'-------
    for (const thisComponent of mentRotTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (MROT_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrResponse)) {
         MROT_resp.corr = 1;  // correct non-response
      } else {
         MROT_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('MROT_resp.keys', MROT_resp.keys);
    psychoJS.experiment.addData('MROT_resp.corr', MROT_resp.corr);
    if (typeof MROT_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('MROT_resp.rt', MROT_resp.rt);
        routineTimer.reset();
        }
    
    MROT_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var mentRotFeedbackComponents;
function mentRotFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'mentRotFeedback'-------
    t = 0;
    mentRotFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (MROT_resp.corr) {
        msg = "Correct";
    } else {
        msg = "Incorrect";
    }
    
    NBackfeedback_text_2.setText(msg);
    // keep track of which components have finished
    mentRotFeedbackComponents = [];
    mentRotFeedbackComponents.push(NBackfeedback_text_2);
    
    for (const thisComponent of mentRotFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function mentRotFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'mentRotFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = mentRotFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NBackfeedback_text_2* updates
    if (t >= 0.0 && NBackfeedback_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NBackfeedback_text_2.tStart = t;  // (not accounting for frame time here)
      NBackfeedback_text_2.frameNStart = frameN;  // exact frame index
      
      NBackfeedback_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (NBackfeedback_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      NBackfeedback_text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of mentRotFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mentRotFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'mentRotFeedback'-------
    for (const thisComponent of mentRotFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var instrNBACKbreak5Timer;
var _key_resp_8_allKeys;
var instrNBACKbreak5Components;
function instrNBACKbreak5RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrNBACKbreak5'-------
    t = 0;
    instrNBACKbreak5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrNBACKbreak5Timer = new util.Clock();
    
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    text_13.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrNBACKbreak5Components = [];
    instrNBACKbreak5Components.push(key_resp_8);
    instrNBACKbreak5Components.push(instrHeaderText_9);
    instrNBACKbreak5Components.push(text_13);
    
    for (const thisComponent of instrNBACKbreak5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrNBACKbreak5RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrNBACKbreak5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrNBACKbreak5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_8* updates
    if (t >= 0.5 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_9* updates
    if (t >= 0.0 && instrHeaderText_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_9.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_9.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_9.setAutoDraw(true);
    }

    
    // *text_13* updates
    if (t >= 0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrNBACKbreak5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrNBACKbreak5RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrNBACKbreak5'-------
    for (const thisComponent of instrNBACKbreak5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break5.duration", instrNBACKbreak5Timer.getTime());
    instrNBACKbreak5Timer = [];
    
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "instrNBACKbreak5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrAXCPTbreak6Timer;
var _key_resp_6_allKeys;
var instrAXCPTbreak6Components;
function instrAXCPTbreak6RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrAXCPTbreak6'-------
    t = 0;
    instrAXCPTbreak6Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrAXCPTbreak6Timer = new util.Clock();
    
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    instrAXCPTbreak6Components = [];
    instrAXCPTbreak6Components.push(key_resp_6);
    instrAXCPTbreak6Components.push(instrHeaderText_7);
    instrAXCPTbreak6Components.push(text_7);
    
    for (const thisComponent of instrAXCPTbreak6Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrAXCPTbreak6RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrAXCPTbreak6'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrAXCPTbreak6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_6* updates
    if (t >= 0.5 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_7* updates
    if (t >= 0.0 && instrHeaderText_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_7.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_7.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_7.setAutoDraw(true);
    }

    
    // *text_7* updates
    if (t >= 0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrAXCPTbreak6Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrAXCPTbreak6RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrAXCPTbreak6'-------
    for (const thisComponent of instrAXCPTbreak6Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break6.duration", instrAXCPTbreak6Timer.getTime());
    instrAXCPTbreak6Timer = [];
    
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "instrAXCPTbreak6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrSEARCHbreak7Timer;
var _key_resp_15_allKeys;
var instrSEARCHbreak7Components;
function instrSEARCHbreak7RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrSEARCHbreak7'-------
    t = 0;
    instrSEARCHbreak7Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrSEARCHbreak7Timer = new util.Clock();
    
    text_15.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin");
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    instrSEARCHbreak7Components = [];
    instrSEARCHbreak7Components.push(instrHeaderText_11);
    instrSEARCHbreak7Components.push(text_15);
    instrSEARCHbreak7Components.push(key_resp_15);
    
    for (const thisComponent of instrSEARCHbreak7Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrSEARCHbreak7RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrSEARCHbreak7'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrSEARCHbreak7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrHeaderText_11* updates
    if (t >= 0.0 && instrHeaderText_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_11.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_11.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_11.setAutoDraw(true);
    }

    
    // *text_15* updates
    if (t >= 0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 0.5 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrSEARCHbreak7Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrSEARCHbreak7RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrSEARCHbreak7'-------
    for (const thisComponent of instrSEARCHbreak7Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break7.duration", instrSEARCHbreak7Timer.getTime());
    instrSEARCHbreak7Timer = [];
    
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "instrSEARCHbreak7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrMENTROTbreak8Timer;
var _key_resp_10_allKeys;
var instrMENTROTbreak8Components;
function instrMENTROTbreak8RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrMENTROTbreak8'-------
    t = 0;
    instrMENTROTbreak8Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrMENTROTbreak8Timer = new util.Clock();
    
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    text_17.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrMENTROTbreak8Components = [];
    instrMENTROTbreak8Components.push(key_resp_10);
    instrMENTROTbreak8Components.push(instrHeaderText_13);
    instrMENTROTbreak8Components.push(text_17);
    
    for (const thisComponent of instrMENTROTbreak8Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrMENTROTbreak8RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrMENTROTbreak8'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrMENTROTbreak8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_10* updates
    if (t >= 0.5 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_13* updates
    if (t >= 0.0 && instrHeaderText_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_13.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_13.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_13.setAutoDraw(true);
    }

    
    // *text_17* updates
    if (t >= 0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrMENTROTbreak8Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrMENTROTbreak8RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrMENTROTbreak8'-------
    for (const thisComponent of instrMENTROTbreak8Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break8.duration", instrMENTROTbreak8Timer.getTime());
    instrMENTROTbreak8Timer = [];
    
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "instrMENTROTbreak8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrNBACKbreak9Timer;
var _key_resp_9_allKeys;
var instrNBACKbreak9Components;
function instrNBACKbreak9RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrNBACKbreak9'-------
    t = 0;
    instrNBACKbreak9Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrNBACKbreak9Timer = new util.Clock();
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    text_14.setText("Next task: N-Back\n\nDecide whether the letter on the screen is the same as the one 3 letters ago\n\nPress 'k' if it is the same\n\nPress 'd' if it is not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrNBACKbreak9Components = [];
    instrNBACKbreak9Components.push(key_resp_9);
    instrNBACKbreak9Components.push(instrHeaderText_10);
    instrNBACKbreak9Components.push(text_14);
    
    for (const thisComponent of instrNBACKbreak9Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrNBACKbreak9RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrNBACKbreak9'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrNBACKbreak9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_9* updates
    if (t >= 0.5 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_10* updates
    if (t >= 0.0 && instrHeaderText_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_10.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_10.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_10.setAutoDraw(true);
    }

    
    // *text_14* updates
    if (t >= 0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrNBACKbreak9Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrNBACKbreak9RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrNBACKbreak9'-------
    for (const thisComponent of instrNBACKbreak9Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break9.duration", instrNBACKbreak9Timer.getTime());
    instrNBACKbreak9Timer = [];
    
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "instrNBACKbreak9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrSEARCHbreak10Timer;
var _key_resp_5_allKeys;
var instrSEARCHbreak10Components;
function instrSEARCHbreak10RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrSEARCHbreak10'-------
    t = 0;
    instrSEARCHbreak10Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrSEARCHbreak10Timer = new util.Clock();
    
    text_16.setText("Next task: Visual Search\n\nPress 'k' if you can see the letter T\nPress 'd' if you can not see the letter T\n\nRespond as quickly and accurately as possible\n\nPress 'k' to begin");
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    instrSEARCHbreak10Components = [];
    instrSEARCHbreak10Components.push(instrHeaderText_12);
    instrSEARCHbreak10Components.push(text_16);
    instrSEARCHbreak10Components.push(key_resp_5);
    
    for (const thisComponent of instrSEARCHbreak10Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrSEARCHbreak10RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrSEARCHbreak10'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrSEARCHbreak10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrHeaderText_12* updates
    if (t >= 0.0 && instrHeaderText_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_12.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_12.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_12.setAutoDraw(true);
    }

    
    // *text_16* updates
    if (t >= 0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.5 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrSEARCHbreak10Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrSEARCHbreak10RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrSEARCHbreak10'-------
    for (const thisComponent of instrSEARCHbreak10Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break10.duration", instrSEARCHbreak10Timer.getTime());
    instrSEARCHbreak10Timer = [];
    
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "instrSEARCHbreak10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrMENTROTbreak11Timer;
var _key_resp_11_allKeys;
var instrMENTROTbreak11Components;
function instrMENTROTbreak11RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrMENTROTbreak11'-------
    t = 0;
    instrMENTROTbreak11Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrMENTROTbreak11Timer = new util.Clock();
    
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    text_18.setText("Next task: Mental Rotation\n\nDecide if the two shapes are the same\n\nPress 'k' they are the same\n\nPress 'd' if they are not the same\n\nRespond as quickly and accurately as possible\n\nPress 'k' when ready to begin");
    // keep track of which components have finished
    instrMENTROTbreak11Components = [];
    instrMENTROTbreak11Components.push(key_resp_11);
    instrMENTROTbreak11Components.push(instrHeaderText_14);
    instrMENTROTbreak11Components.push(text_18);
    
    for (const thisComponent of instrMENTROTbreak11Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrMENTROTbreak11RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrMENTROTbreak11'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrMENTROTbreak11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_11* updates
    if (t >= 0.5 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_14* updates
    if (t >= 0.0 && instrHeaderText_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_14.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_14.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_14.setAutoDraw(true);
    }

    
    // *text_18* updates
    if (t >= 0 && text_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_18.tStart = t;  // (not accounting for frame time here)
      text_18.frameNStart = frameN;  // exact frame index
      
      text_18.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrMENTROTbreak11Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrMENTROTbreak11RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrMENTROTbreak11'-------
    for (const thisComponent of instrMENTROTbreak11Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break11.duration", instrMENTROTbreak11Timer.getTime());
    instrMENTROTbreak11Timer = [];
    
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "instrMENTROTbreak11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrAXCPTbreak12Timer;
var _key_resp_7_allKeys;
var instrAXCPTbreak12Components;
function instrAXCPTbreak12RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrAXCPTbreak12'-------
    t = 0;
    instrAXCPTbreak12Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instrAXCPTbreak12Timer = new util.Clock();
    
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    instrAXCPTbreak12Components = [];
    instrAXCPTbreak12Components.push(key_resp_7);
    instrAXCPTbreak12Components.push(instrHeaderText_8);
    instrAXCPTbreak12Components.push(text_12);
    
    for (const thisComponent of instrAXCPTbreak12Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrAXCPTbreak12RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrAXCPTbreak12'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrAXCPTbreak12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_7* updates
    if (t >= 0.5 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['k'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instrHeaderText_8* updates
    if (t >= 0.0 && instrHeaderText_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrHeaderText_8.tStart = t;  // (not accounting for frame time here)
      instrHeaderText_8.frameNStart = frameN;  // exact frame index
      
      instrHeaderText_8.setAutoDraw(true);
    }

    
    // *text_12* updates
    if (t >= 0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_12.tStart = t;  // (not accounting for frame time here)
      text_12.frameNStart = frameN;  // exact frame index
      
      text_12.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrAXCPTbreak12Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrAXCPTbreak12RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrAXCPTbreak12'-------
    for (const thisComponent of instrAXCPTbreak12Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    psychoJS.experiment.addData("break12.duration", instrAXCPTbreak12Timer.getTime());
    instrAXCPTbreak12Timer = [];
    
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "instrAXCPTbreak12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrBRUMSpostComponents;
function instrBRUMSpostRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrBRUMSpost'-------
    t = 0;
    instrBRUMSpostClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_9
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instrBRUMSpostComponents = [];
    instrBRUMSpostComponents.push(text_19);
    instrBRUMSpostComponents.push(mouse_9);
    instrBRUMSpostComponents.push(BRUMSheader_2);
    
    for (const thisComponent of instrBRUMSpostComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrBRUMSpostRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrBRUMSpost'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrBRUMSpostClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_19* updates
    if (t >= 0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_19.tStart = t;  // (not accounting for frame time here)
      text_19.frameNStart = frameN;  // exact frame index
      
      text_19.setAutoDraw(true);
    }

    // *mouse_9* updates
    if (t >= 0.5 && mouse_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_9.tStart = t;  // (not accounting for frame time here)
      mouse_9.frameNStart = frameN;  // exact frame index
      
      mouse_9.status = PsychoJS.Status.STARTED;
      mouse_9.mouseClock.reset();
      prevButtonState = mouse_9.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_9.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_9.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *BRUMSheader_2* updates
    if (t >= 0.0 && BRUMSheader_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BRUMSheader_2.tStart = t;  // (not accounting for frame time here)
      BRUMSheader_2.frameNStart = frameN;  // exact frame index
      
      BRUMSheader_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrBRUMSpostComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrBRUMSpostRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrBRUMSpost'-------
    for (const thisComponent of instrBRUMSpostComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    
    // store data for thisExp (ExperimentHandler)
    // the Routine "instrBRUMSpost" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_20);
    endComponents.push(key_resp_12);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_20* updates
    if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }

    
    // *key_resp_12* updates
    if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end'-------
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("elapsed.time", elapsedTime.getTime());
    
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
