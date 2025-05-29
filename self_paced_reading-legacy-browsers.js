/*************************** 
 * Comprehension Test *
 ***************************/


// store info about the experiment session:
let expName = 'Comprehension test';  // from the Builder filename that created this script
let expInfo = {
    'Участник': `${util.pad(Number.parseFloat(util.randint(1000, 9999)).toFixed(0), 3)}`,
    'Группа': ["\u0413\u0440\u0443\u043f\u043f\u0430 1", "\u0413\u0440\u0443\u043f\u043f\u0430 2"],
    'Возраст': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
const trials_testLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_testLoopBegin(trials_testLoopScheduler));
flowScheduler.add(trials_testLoopScheduler);
flowScheduler.add(trials_testLoopEnd);








flowScheduler.add(btwRoutineBegin());
flowScheduler.add(btwRoutineEachFrame());
flowScheduler.add(btwRoutineEnd());
const group1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(group1LoopBegin(group1LoopScheduler));
flowScheduler.add(group1LoopScheduler);
flowScheduler.add(group1LoopEnd);










const group2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(group2LoopBegin(group2LoopScheduler));
flowScheduler.add(group2LoopScheduler);
flowScheduler.add(group2LoopEnd);










const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);


flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'spreadsheets/test/test_paths.xlsx', 'path': 'spreadsheets/test/test_paths.xlsx'},
    {'name': 'spreadsheets/test/passage_0.csv', 'path': 'spreadsheets/test/passage_0.csv'},
    {'name': 'spreadsheets/test/passage_1.csv', 'path': 'spreadsheets/test/passage_1.csv'},
    {'name': 'spreadsheets/group1_paths.xlsx', 'path': 'spreadsheets/group1_paths.xlsx'},
    {'name': 'spreadsheets/group_1/passage_0.csv', 'path': 'spreadsheets/group_1/passage_0.csv'},
    {'name': 'spreadsheets/group_1/passage_3.csv', 'path': 'spreadsheets/group_1/passage_3.csv'},
    {'name': 'spreadsheets/group_1/passage_5.csv', 'path': 'spreadsheets/group_1/passage_5.csv'},
    {'name': 'spreadsheets/group_1/passage_6.csv', 'path': 'spreadsheets/group_1/passage_6.csv'},
    {'name': 'spreadsheets/group_1/passage_8.csv', 'path': 'spreadsheets/group_1/passage_8.csv'},
    {'name': 'spreadsheets/group_1/passage_11.csv', 'path': 'spreadsheets/group_1/passage_11.csv'},
    {'name': 'spreadsheets/group_1/passage_13.csv', 'path': 'spreadsheets/group_1/passage_13.csv'},
    {'name': 'spreadsheets/group_1/passage_14.csv', 'path': 'spreadsheets/group_1/passage_14.csv'},
    {'name': 'spreadsheets/group_1/passage_16.csv', 'path': 'spreadsheets/group_1/passage_16.csv'},
    {'name': 'spreadsheets/group_1/passage_19.csv', 'path': 'spreadsheets/group_1/passage_19.csv'},
    {'name': 'spreadsheets/group_1/passage_21.csv', 'path': 'spreadsheets/group_1/passage_21.csv'},
    {'name': 'spreadsheets/group_1/passage_22.csv', 'path': 'spreadsheets/group_1/passage_22.csv'},
    {'name': 'spreadsheets/group_1/passage_24.csv', 'path': 'spreadsheets/group_1/passage_24.csv'},
    {'name': 'spreadsheets/group_1/passage_27.csv', 'path': 'spreadsheets/group_1/passage_27.csv'},
    {'name': 'spreadsheets/group_1/passage_29.csv', 'path': 'spreadsheets/group_1/passage_29.csv'},
    {'name': 'spreadsheets/group_1/passage_30.csv', 'path': 'spreadsheets/group_1/passage_30.csv'},
    {'name': 'spreadsheets/group_1/passage_32.csv', 'path': 'spreadsheets/group_1/passage_32.csv'},
    {'name': 'spreadsheets/group_1/passage_35.csv', 'path': 'spreadsheets/group_1/passage_35.csv'},
    {'name': 'spreadsheets/group_1/passage_37.csv', 'path': 'spreadsheets/group_1/passage_37.csv'},
    {'name': 'spreadsheets/group_1/passage_38.csv', 'path': 'spreadsheets/group_1/passage_38.csv'},
    {'name': 'spreadsheets/group_1/passage_40.csv', 'path': 'spreadsheets/group_1/passage_40.csv'},
    {'name': 'spreadsheets/group_1/passage_43.csv', 'path': 'spreadsheets/group_1/passage_43.csv'},
    {'name': 'spreadsheets/group_1/passage_45.csv', 'path': 'spreadsheets/group_1/passage_45.csv'},
    {'name': 'spreadsheets/group_1/passage_46.csv', 'path': 'spreadsheets/group_1/passage_46.csv'},
    {'name': 'spreadsheets/group_1/passage_48.csv', 'path': 'spreadsheets/group_1/passage_48.csv'},
    {'name': 'spreadsheets/group_1/passage_51.csv', 'path': 'spreadsheets/group_1/passage_51.csv'},
    {'name': 'spreadsheets/group_1/passage_53.csv', 'path': 'spreadsheets/group_1/passage_53.csv'},
    {'name': 'spreadsheets/group_1/passage_54.csv', 'path': 'spreadsheets/group_1/passage_54.csv'},
    {'name': 'spreadsheets/group_1/passage_56.csv', 'path': 'spreadsheets/group_1/passage_56.csv'},
    {'name': 'spreadsheets/group_1/passage_59.csv', 'path': 'spreadsheets/group_1/passage_59.csv'},
    {'name': 'spreadsheets/group_1/passage_61.csv', 'path': 'spreadsheets/group_1/passage_61.csv'},
    {'name': 'spreadsheets/group_1/passage_62.csv', 'path': 'spreadsheets/group_1/passage_62.csv'},
    {'name': 'spreadsheets/group_1/passage_65.csv', 'path': 'spreadsheets/group_1/passage_65.csv'},
    {'name': 'spreadsheets/group_1/passage_66.csv', 'path': 'spreadsheets/group_1/passage_66.csv'},
    {'name': 'spreadsheets/group_1/passage_69.csv', 'path': 'spreadsheets/group_1/passage_69.csv'},
    {'name': 'spreadsheets/group_1/passage_70.csv', 'path': 'spreadsheets/group_1/passage_70.csv'},
    {'name': 'spreadsheets/group_1/passage_73.csv', 'path': 'spreadsheets/group_1/passage_73.csv'},
    {'name': 'spreadsheets/group_1/passage_74.csv', 'path': 'spreadsheets/group_1/passage_74.csv'},
    {'name': 'spreadsheets/group_1/passage_77.csv', 'path': 'spreadsheets/group_1/passage_77.csv'},
    {'name': 'spreadsheets/group_1/passage_78.csv', 'path': 'spreadsheets/group_1/passage_78.csv'},
    {'name': 'spreadsheets/group_1/passage_81.csv', 'path': 'spreadsheets/group_1/passage_81.csv'},
    {'name': 'spreadsheets/group_1/passage_82.csv', 'path': 'spreadsheets/group_1/passage_82.csv'},
    {'name': 'spreadsheets/group_1/passage_85.csv', 'path': 'spreadsheets/group_1/passage_85.csv'},
    {'name': 'spreadsheets/group_1/passage_86.csv', 'path': 'spreadsheets/group_1/passage_86.csv'},
    {'name': 'spreadsheets/group2_paths.xlsx', 'path': 'spreadsheets/group2_paths.xlsx'},
    {'name': 'spreadsheets/group_2/passage_1.csv', 'path': 'spreadsheets/group_2/passage_1.csv'},
    {'name': 'spreadsheets/group_2/passage_2.csv', 'path': 'spreadsheets/group_2/passage_2.csv'},
    {'name': 'spreadsheets/group_2/passage_4.csv', 'path': 'spreadsheets/group_2/passage_4.csv'},
    {'name': 'spreadsheets/group_2/passage_7.csv', 'path': 'spreadsheets/group_2/passage_7.csv'},
    {'name': 'spreadsheets/group_2/passage_9.csv', 'path': 'spreadsheets/group_2/passage_9.csv'},
    {'name': 'spreadsheets/group_2/passage_10.csv', 'path': 'spreadsheets/group_2/passage_10.csv'},
    {'name': 'spreadsheets/group_2/passage_12.csv', 'path': 'spreadsheets/group_2/passage_12.csv'},
    {'name': 'spreadsheets/group_2/passage_15.csv', 'path': 'spreadsheets/group_2/passage_15.csv'},
    {'name': 'spreadsheets/group_2/passage_17.csv', 'path': 'spreadsheets/group_2/passage_17.csv'},
    {'name': 'spreadsheets/group_2/passage_18.csv', 'path': 'spreadsheets/group_2/passage_18.csv'},
    {'name': 'spreadsheets/group_2/passage_20.csv', 'path': 'spreadsheets/group_2/passage_20.csv'},
    {'name': 'spreadsheets/group_2/passage_23.csv', 'path': 'spreadsheets/group_2/passage_23.csv'},
    {'name': 'spreadsheets/group_2/passage_25.csv', 'path': 'spreadsheets/group_2/passage_25.csv'},
    {'name': 'spreadsheets/group_2/passage_26.csv', 'path': 'spreadsheets/group_2/passage_26.csv'},
    {'name': 'spreadsheets/group_2/passage_28.csv', 'path': 'spreadsheets/group_2/passage_28.csv'},
    {'name': 'spreadsheets/group_2/passage_31.csv', 'path': 'spreadsheets/group_2/passage_31.csv'},
    {'name': 'spreadsheets/group_2/passage_33.csv', 'path': 'spreadsheets/group_2/passage_33.csv'},
    {'name': 'spreadsheets/group_2/passage_34.csv', 'path': 'spreadsheets/group_2/passage_34.csv'},
    {'name': 'spreadsheets/group_2/passage_36.csv', 'path': 'spreadsheets/group_2/passage_36.csv'},
    {'name': 'spreadsheets/group_2/passage_39.csv', 'path': 'spreadsheets/group_2/passage_39.csv'},
    {'name': 'spreadsheets/group_2/passage_41.csv', 'path': 'spreadsheets/group_2/passage_41.csv'},
    {'name': 'spreadsheets/group_2/passage_42.csv', 'path': 'spreadsheets/group_2/passage_42.csv'},
    {'name': 'spreadsheets/group_2/passage_44.csv', 'path': 'spreadsheets/group_2/passage_44.csv'},
    {'name': 'spreadsheets/group_2/passage_47.csv', 'path': 'spreadsheets/group_2/passage_47.csv'},
    {'name': 'spreadsheets/group_2/passage_49.csv', 'path': 'spreadsheets/group_2/passage_49.csv'},
    {'name': 'spreadsheets/group_2/passage_50.csv', 'path': 'spreadsheets/group_2/passage_50.csv'},
    {'name': 'spreadsheets/group_2/passage_52.csv', 'path': 'spreadsheets/group_2/passage_52.csv'},
    {'name': 'spreadsheets/group_2/passage_55.csv', 'path': 'spreadsheets/group_2/passage_55.csv'},
    {'name': 'spreadsheets/group_2/passage_57.csv', 'path': 'spreadsheets/group_2/passage_57.csv'},
    {'name': 'spreadsheets/group_2/passage_58.csv', 'path': 'spreadsheets/group_2/passage_58.csv'},
    {'name': 'spreadsheets/group_2/passage_60.csv', 'path': 'spreadsheets/group_2/passage_60.csv'},
    {'name': 'spreadsheets/group_2/passage_63.csv', 'path': 'spreadsheets/group_2/passage_63.csv'},
    {'name': 'spreadsheets/group_2/passage_64.csv', 'path': 'spreadsheets/group_2/passage_64.csv'},
    {'name': 'spreadsheets/group_2/passage_67.csv', 'path': 'spreadsheets/group_2/passage_67.csv'},
    {'name': 'spreadsheets/group_2/passage_68.csv', 'path': 'spreadsheets/group_2/passage_68.csv'},
    {'name': 'spreadsheets/group_2/passage_71.csv', 'path': 'spreadsheets/group_2/passage_71.csv'},
    {'name': 'spreadsheets/group_2/passage_72.csv', 'path': 'spreadsheets/group_2/passage_72.csv'},
    {'name': 'spreadsheets/group_2/passage_75.csv', 'path': 'spreadsheets/group_2/passage_75.csv'},
    {'name': 'spreadsheets/group_2/passage_76.csv', 'path': 'spreadsheets/group_2/passage_76.csv'},
    {'name': 'spreadsheets/group_2/passage_79.csv', 'path': 'spreadsheets/group_2/passage_79.csv'},
    {'name': 'spreadsheets/group_2/passage_80.csv', 'path': 'spreadsheets/group_2/passage_80.csv'},
    {'name': 'spreadsheets/group_2/passage_83.csv', 'path': 'spreadsheets/group_2/passage_83.csv'},
    {'name': 'spreadsheets/group_2/passage_84.csv', 'path': 'spreadsheets/group_2/passage_84.csv'},
    {'name': 'spreadsheets/group_2/passage_87.csv', 'path': 'spreadsheets/group_2/passage_87.csv'},
    {'name': 'spreadsheets/idiom_test.xlsx', 'path': 'spreadsheets/idiom_test.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a"]}`);
  psychoJS.experiment.field_separator = ';';


  return Scheduler.Event.NEXT;
}


var introClock;
var introtxt;
var start_resp;
var group1_trials_reps;
var group2_trials_reps;
var testClock;
var textbox;
var key_resp_5;
var question_testClock;
var q;
var textbox_3;
var key_resp_6;
var btw2Clock;
var textbox_4;
var key_resp_7;
var btwClock;
var textbox_5;
var key_resp_8;
var show_textClock;
var sentence;
var key_resp;
var questionClock;
var question_2;
var textbox_2;
var key_resp_4;
var show_finalClock;
var textbox_7;
var textbox_6;
var key_resp_9;
var endClock;
var endtxt;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  introtxt = new visual.TextBox({
    win: psychoJS.window,
    name: 'introtxt',
    text: 'Вам будет необходимо прочитать предложения. Они будут появляться на экране по фрагментам. \nПока вы читаете один фрагмент, остальные будут скрыты. Чтобы открыть следующий фрагмент и скрыть следующий, нажмите ПРОБЕЛ. \n\nВнимательно читайте предложения. Каждый фрагмент можно прочитать только один раз. Вернуться к предыдущим фрагментам невозможно. \n\nВремя чтения будет фиксироваться, поэтому, пожалуйста, убедитесь, что Вас ничего не будет отвлекать во время тестирования. Если Вам необходимо отвлечься, завершите чтение текущего предложения.\n\nПосле каждого предложения Вам будет необходимо оценить суждения на понимание прочитанного.  \nНажмите Y на клавиатуре, если суждение следует из предложения или просто не противоречит ему. Нажмите N, если суждение скорее противоречит предложению.\n\nОценивайте суждение по отношению лишь к ТОЛЬКО ЧТО прочитанному предложению.\n\nПеред началом эксперимента у вас должна быть включена английская раскладка (в ином случае необходимо перезапустить).\n\nЭксперимент займет не более 7 минут.\n\nНажмите ПРОБЕЛ, чтобы начать тестовое прочтение.\n',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  start_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code
  group1_trials_reps = 0;
  group2_trials_reps = 0;
  if ((expInfo["\u0413\u0440\u0443\u043f\u043f\u0430"] === "\u0413\u0440\u0443\u043f\u043f\u0430 1")) {
      group1_trials_reps = 1;
  }
  if ((expInfo["\u0413\u0440\u0443\u043f\u043f\u0430"] === "\u0413\u0440\u0443\u043f\u043f\u0430 2")) {
      group2_trials_reps = 1;
  }
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [(- 0.5), (- 0.1)], 
    draggable: false,
    letterHeight: 0.08,
    lineSpacing: 1.0,
    size: [1.2, 2],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "question_test"
  question_testClock = new util.Clock();
  q = new visual.TextBox({
    win: psychoJS.window,
    name: 'q',
    text: 'Ответьте на вопрос, нажав Y (ДА) или N (НЕТ)',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'top-center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  textbox_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: 0, 
    draggable: false,
    letterHeight: 0.07,
    lineSpacing: 1.0,
    size: [1.5, 0.3],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "btw2"
  btw2Clock = new util.Clock();
  textbox_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_4',
    text: 'Нажмите ПРОБЕЛ для перехода к следующему предложению',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.07,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "btw"
  btwClock = new util.Clock();
  textbox_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_5',
    text: 'Конец тестовых предложений.\n\nЧтобы начать эксперимент и перейти к следующему предложению, нажмите ПРОБЕЛ',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.07,
    lineSpacing: 1.0,
    size: [1, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "show_text"
  show_textClock = new util.Clock();
  sentence = new visual.TextBox({
    win: psychoJS.window,
    name: 'sentence',
    text: '',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0.1, (- 0.1)], 
    draggable: false,
    letterHeight: 0.07,
    lineSpacing: 1.0,
    size: [1.4, 2],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "question"
  questionClock = new util.Clock();
  question_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'question_2',
    text: '',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0.3], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [2.6, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'top-center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'bottom-center',
    depth: 0.0 
  });
  
  textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_2',
    text: '',
    placeholder: undefined,
    font: 'Georgia',
    pos: [0, 0.05], 
    draggable: false,
    letterHeight: 0.07,
    lineSpacing: 1.0,
    size: [1.7, 1],  units: 'height', 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "show_final"
  show_finalClock = new util.Clock();
  textbox_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_7',
    text: 'Нажмите Y, если ДА, или N, если НЕТ.',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0.3], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  textbox_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_6',
    text: '',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 0.3],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  endtxt = new visual.TextBox({
    win: psychoJS.window,
    name: 'endtxt',
    text: 'Конец тестирования.\n\nБлагодарим за участие!',
    placeholder: 'Type here...',
    font: 'Georgia',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.06,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var introMaxDurationReached;
var _start_resp_allKeys;
var introMaxDuration;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    introClock.reset();
    routineTimer.reset();
    introMaxDurationReached = false;
    // update component parameters for each repeat
    start_resp.keys = undefined;
    start_resp.rt = undefined;
    _start_resp_allKeys = [];
    psychoJS.experiment.addData('intro.started', globalClock.getTime());
    introMaxDuration = null
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(introtxt);
    introComponents.push(start_resp);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *introtxt* updates
    if (t >= 0.0 && introtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introtxt.tStart = t;  // (not accounting for frame time here)
      introtxt.frameNStart = frameN;  // exact frame index
      
      introtxt.setAutoDraw(true);
    }
    
    
    // *start_resp* updates
    if (t >= 0.0 && start_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_resp.tStart = t;  // (not accounting for frame time here)
      start_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_resp.clearEvents(); });
    }
    
    if (start_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_resp.getKeys({keyList: ['space'], waitRelease: false});
      _start_resp_allKeys = _start_resp_allKeys.concat(theseKeys);
      if (_start_resp_allKeys.length > 0) {
        start_resp.keys = _start_resp_allKeys[_start_resp_allKeys.length - 1].name;  // just the last key pressed
        start_resp.rt = _start_resp_allKeys[_start_resp_allKeys.length - 1].rt;
        start_resp.duration = _start_resp_allKeys[_start_resp_allKeys.length - 1].duration;
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
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('intro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(start_resp.corr, level);
    }
    psychoJS.experiment.addData('start_resp.keys', start_resp.keys);
    if (typeof start_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_resp.rt', start_resp.rt);
        psychoJS.experiment.addData('start_resp.duration', start_resp.duration);
        routineTimer.reset();
        }
    
    start_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_test;
function trials_testLoopBegin(trials_testLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_test = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'spreadsheets/test/test_paths.xlsx',
      seed: undefined, name: 'trials_test'
    });
    psychoJS.experiment.addLoop(trials_test); // add the loop to the experiment
    currentLoop = trials_test;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_test.forEach(function() {
      snapshot = trials_test.getSnapshot();
    
      trials_testLoopScheduler.add(importConditions(snapshot));
      const sentence_loop_testLoopScheduler = new Scheduler(psychoJS);
      trials_testLoopScheduler.add(sentence_loop_testLoopBegin(sentence_loop_testLoopScheduler, snapshot));
      trials_testLoopScheduler.add(sentence_loop_testLoopScheduler);
      trials_testLoopScheduler.add(sentence_loop_testLoopEnd);
      const question_loop_testLoopScheduler = new Scheduler(psychoJS);
      trials_testLoopScheduler.add(question_loop_testLoopBegin(question_loop_testLoopScheduler, snapshot));
      trials_testLoopScheduler.add(question_loop_testLoopScheduler);
      trials_testLoopScheduler.add(question_loop_testLoopEnd);
      trials_testLoopScheduler.add(btw2RoutineBegin(snapshot));
      trials_testLoopScheduler.add(btw2RoutineEachFrame());
      trials_testLoopScheduler.add(btw2RoutineEnd(snapshot));
      trials_testLoopScheduler.add(trials_testLoopEndIteration(trials_testLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var sentence_loop_test;
function sentence_loop_testLoopBegin(sentence_loop_testLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    sentence_loop_test = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: file_path,
      seed: undefined, name: 'sentence_loop_test'
    });
    psychoJS.experiment.addLoop(sentence_loop_test); // add the loop to the experiment
    currentLoop = sentence_loop_test;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    sentence_loop_test.forEach(function() {
      snapshot = sentence_loop_test.getSnapshot();
    
      sentence_loop_testLoopScheduler.add(importConditions(snapshot));
      sentence_loop_testLoopScheduler.add(testRoutineBegin(snapshot));
      sentence_loop_testLoopScheduler.add(testRoutineEachFrame());
      sentence_loop_testLoopScheduler.add(testRoutineEnd(snapshot));
      sentence_loop_testLoopScheduler.add(sentence_loop_testLoopEndIteration(sentence_loop_testLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function sentence_loop_testLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(sentence_loop_test);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function sentence_loop_testLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var question_loop_test;
function question_loop_testLoopBegin(question_loop_testLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    question_loop_test = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, file_path, '0'),
      seed: undefined, name: 'question_loop_test'
    });
    psychoJS.experiment.addLoop(question_loop_test); // add the loop to the experiment
    currentLoop = question_loop_test;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    question_loop_test.forEach(function() {
      snapshot = question_loop_test.getSnapshot();
    
      question_loop_testLoopScheduler.add(importConditions(snapshot));
      question_loop_testLoopScheduler.add(question_testRoutineBegin(snapshot));
      question_loop_testLoopScheduler.add(question_testRoutineEachFrame());
      question_loop_testLoopScheduler.add(question_testRoutineEnd(snapshot));
      question_loop_testLoopScheduler.add(question_loop_testLoopEndIteration(question_loop_testLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function question_loop_testLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(question_loop_test);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function question_loop_testLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_testLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_test);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_testLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var group1;
function group1LoopBegin(group1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    group1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: group1_trials_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'group1'
    });
    psychoJS.experiment.addLoop(group1); // add the loop to the experiment
    currentLoop = group1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    group1.forEach(function() {
      snapshot = group1.getSnapshot();
    
      group1LoopScheduler.add(importConditions(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      group1LoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      group1LoopScheduler.add(trialsLoopScheduler);
      group1LoopScheduler.add(trialsLoopEnd);
      group1LoopScheduler.add(group1LoopEndIteration(group1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'spreadsheets/group1_paths.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      const sentence_loopLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(sentence_loopLoopBegin(sentence_loopLoopScheduler, snapshot));
      trialsLoopScheduler.add(sentence_loopLoopScheduler);
      trialsLoopScheduler.add(sentence_loopLoopEnd);
      const question_loopLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(question_loopLoopBegin(question_loopLoopScheduler, snapshot));
      trialsLoopScheduler.add(question_loopLoopScheduler);
      trialsLoopScheduler.add(question_loopLoopEnd);
      trialsLoopScheduler.add(btw2RoutineBegin(snapshot));
      trialsLoopScheduler.add(btw2RoutineEachFrame());
      trialsLoopScheduler.add(btw2RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var sentence_loop;
function sentence_loopLoopBegin(sentence_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    sentence_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: this_file,
      seed: undefined, name: 'sentence_loop'
    });
    psychoJS.experiment.addLoop(sentence_loop); // add the loop to the experiment
    currentLoop = sentence_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    sentence_loop.forEach(function() {
      snapshot = sentence_loop.getSnapshot();
    
      sentence_loopLoopScheduler.add(importConditions(snapshot));
      sentence_loopLoopScheduler.add(show_textRoutineBegin(snapshot));
      sentence_loopLoopScheduler.add(show_textRoutineEachFrame());
      sentence_loopLoopScheduler.add(show_textRoutineEnd(snapshot));
      sentence_loopLoopScheduler.add(sentence_loopLoopEndIteration(sentence_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function sentence_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(sentence_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function sentence_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var question_loop;
function question_loopLoopBegin(question_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    question_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, this_file, '0'),
      seed: undefined, name: 'question_loop'
    });
    psychoJS.experiment.addLoop(question_loop); // add the loop to the experiment
    currentLoop = question_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    question_loop.forEach(function() {
      snapshot = question_loop.getSnapshot();
    
      question_loopLoopScheduler.add(importConditions(snapshot));
      question_loopLoopScheduler.add(questionRoutineBegin(snapshot));
      question_loopLoopScheduler.add(questionRoutineEachFrame());
      question_loopLoopScheduler.add(questionRoutineEnd(snapshot));
      question_loopLoopScheduler.add(question_loopLoopEndIteration(question_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function question_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(question_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function question_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function group1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(group1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function group1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var group2;
function group2LoopBegin(group2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    group2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: group2_trials_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'group2'
    });
    psychoJS.experiment.addLoop(group2); // add the loop to the experiment
    currentLoop = group2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    group2.forEach(function() {
      snapshot = group2.getSnapshot();
    
      group2LoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      group2LoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      group2LoopScheduler.add(trials_2LoopScheduler);
      group2LoopScheduler.add(trials_2LoopEnd);
      group2LoopScheduler.add(group2LoopEndIteration(group2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'spreadsheets/group2_paths.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      const sentence_loop_2LoopScheduler = new Scheduler(psychoJS);
      trials_2LoopScheduler.add(sentence_loop_2LoopBegin(sentence_loop_2LoopScheduler, snapshot));
      trials_2LoopScheduler.add(sentence_loop_2LoopScheduler);
      trials_2LoopScheduler.add(sentence_loop_2LoopEnd);
      const question_loop_2LoopScheduler = new Scheduler(psychoJS);
      trials_2LoopScheduler.add(question_loop_2LoopBegin(question_loop_2LoopScheduler, snapshot));
      trials_2LoopScheduler.add(question_loop_2LoopScheduler);
      trials_2LoopScheduler.add(question_loop_2LoopEnd);
      trials_2LoopScheduler.add(btw2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(btw2RoutineEachFrame());
      trials_2LoopScheduler.add(btw2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var sentence_loop_2;
function sentence_loop_2LoopBegin(sentence_loop_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    sentence_loop_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: this_file,
      seed: undefined, name: 'sentence_loop_2'
    });
    psychoJS.experiment.addLoop(sentence_loop_2); // add the loop to the experiment
    currentLoop = sentence_loop_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    sentence_loop_2.forEach(function() {
      snapshot = sentence_loop_2.getSnapshot();
    
      sentence_loop_2LoopScheduler.add(importConditions(snapshot));
      sentence_loop_2LoopScheduler.add(show_textRoutineBegin(snapshot));
      sentence_loop_2LoopScheduler.add(show_textRoutineEachFrame());
      sentence_loop_2LoopScheduler.add(show_textRoutineEnd(snapshot));
      sentence_loop_2LoopScheduler.add(sentence_loop_2LoopEndIteration(sentence_loop_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function sentence_loop_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(sentence_loop_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function sentence_loop_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var question_loop_2;
function question_loop_2LoopBegin(question_loop_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    question_loop_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, this_file, '0'),
      seed: undefined, name: 'question_loop_2'
    });
    psychoJS.experiment.addLoop(question_loop_2); // add the loop to the experiment
    currentLoop = question_loop_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    question_loop_2.forEach(function() {
      snapshot = question_loop_2.getSnapshot();
    
      question_loop_2LoopScheduler.add(importConditions(snapshot));
      question_loop_2LoopScheduler.add(questionRoutineBegin(snapshot));
      question_loop_2LoopScheduler.add(questionRoutineEachFrame());
      question_loop_2LoopScheduler.add(questionRoutineEnd(snapshot));
      question_loop_2LoopScheduler.add(question_loop_2LoopEndIteration(question_loop_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function question_loop_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(question_loop_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function question_loop_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function group2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(group2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function group2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'spreadsheets/idiom_test.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(show_finalRoutineBegin(snapshot));
      trials_3LoopScheduler.add(show_finalRoutineEachFrame());
      trials_3LoopScheduler.add(show_finalRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var testMaxDurationReached;
var _key_resp_5_allKeys;
var testMaxDuration;
var testComponents;
function testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    testClock.reset();
    routineTimer.reset();
    testMaxDurationReached = false;
    // update component parameters for each repeat
    textbox.setText(masked_segment);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('test.started', globalClock.getTime());
    testMaxDuration = null
    // keep track of which components have finished
    testComponents = [];
    testComponents.push(textbox);
    testComponents.push(key_resp_5);
    
    testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test' ---
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
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
    testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test' ---
    testComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('test.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var question_testMaxDurationReached;
var _key_resp_6_allKeys;
var question_testMaxDuration;
var question_testComponents;
function question_testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'question_test' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    question_testClock.reset();
    routineTimer.reset();
    question_testMaxDurationReached = false;
    // update component parameters for each repeat
    textbox_3.setText(question_text);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    psychoJS.experiment.addData('question_test.started', globalClock.getTime());
    question_testMaxDuration = null
    // keep track of which components have finished
    question_testComponents = [];
    question_testComponents.push(q);
    question_testComponents.push(textbox_3);
    question_testComponents.push(key_resp_6);
    
    question_testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function question_testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'question_test' ---
    // get current time
    t = question_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *q* updates
    if (t >= 0.0 && q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      q.tStart = t;  // (not accounting for frame time here)
      q.frameNStart = frameN;  // exact frame index
      
      q.setAutoDraw(true);
    }
    
    
    // *textbox_3* updates
    if (t >= 0.0 && textbox_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_3.tStart = t;  // (not accounting for frame time here)
      textbox_3.frameNStart = frameN;  // exact frame index
      
      textbox_3.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
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
    question_testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function question_testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'question_test' ---
    question_testComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('question_test.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "question_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var btw2MaxDurationReached;
var _key_resp_7_allKeys;
var btw2MaxDuration;
var btw2Components;
function btw2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'btw2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    btw2Clock.reset();
    routineTimer.reset();
    btw2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    psychoJS.experiment.addData('btw2.started', globalClock.getTime());
    btw2MaxDuration = null
    // keep track of which components have finished
    btw2Components = [];
    btw2Components.push(textbox_4);
    btw2Components.push(key_resp_7);
    
    btw2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function btw2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'btw2' ---
    // get current time
    t = btw2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox_4* updates
    if (t >= 0.0 && textbox_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_4.tStart = t;  // (not accounting for frame time here)
      textbox_4.frameNStart = frameN;  // exact frame index
      
      textbox_4.setAutoDraw(true);
    }
    
    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }
    
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        key_resp_7.duration = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].duration;
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
    btw2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function btw2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'btw2' ---
    btw2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('btw2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        psychoJS.experiment.addData('key_resp_7.duration', key_resp_7.duration);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "btw2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var btwMaxDurationReached;
var _key_resp_8_allKeys;
var btwMaxDuration;
var btwComponents;
function btwRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'btw' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    btwClock.reset();
    routineTimer.reset();
    btwMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    psychoJS.experiment.addData('btw.started', globalClock.getTime());
    btwMaxDuration = null
    // keep track of which components have finished
    btwComponents = [];
    btwComponents.push(textbox_5);
    btwComponents.push(key_resp_8);
    
    btwComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function btwRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'btw' ---
    // get current time
    t = btwClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox_5* updates
    if (t >= 0.0 && textbox_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_5.tStart = t;  // (not accounting for frame time here)
      textbox_5.frameNStart = frameN;  // exact frame index
      
      textbox_5.setAutoDraw(true);
    }
    
    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
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
    btwComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function btwRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'btw' ---
    btwComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('btw.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        psychoJS.experiment.addData('key_resp_8.duration', key_resp_8.duration);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "btw" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var show_textMaxDurationReached;
var _key_resp_allKeys;
var show_textMaxDuration;
var show_textComponents;
function show_textRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'show_text' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    show_textClock.reset();
    routineTimer.reset();
    show_textMaxDurationReached = false;
    // update component parameters for each repeat
    sentence.setText(masked_segment);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('show_text.started', globalClock.getTime());
    show_textMaxDuration = null
    // keep track of which components have finished
    show_textComponents = [];
    show_textComponents.push(sentence);
    show_textComponents.push(key_resp);
    
    show_textComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function show_textRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'show_text' ---
    // get current time
    t = show_textClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sentence* updates
    if (t >= 0.0 && sentence.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sentence.tStart = t;  // (not accounting for frame time here)
      sentence.frameNStart = frameN;  // exact frame index
      
      sentence.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
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
    show_textComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function show_textRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'show_text' ---
    show_textComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('show_text.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "show_text" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var questionMaxDurationReached;
var _key_resp_4_allKeys;
var questionMaxDuration;
var questionComponents;
function questionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'question' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    questionClock.reset();
    routineTimer.reset();
    questionMaxDurationReached = false;
    // update component parameters for each repeat
    question_2.setText('Ответьте на вопрос, нажав Y (ДА) или N (НЕТ)');
    textbox_2.setText(question_text);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('question.started', globalClock.getTime());
    questionMaxDuration = null
    // keep track of which components have finished
    questionComponents = [];
    questionComponents.push(question_2);
    questionComponents.push(textbox_2);
    questionComponents.push(key_resp_4);
    
    questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function questionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'question' ---
    // get current time
    t = questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_2* updates
    if (t >= 0.0 && question_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_2.tStart = t;  // (not accounting for frame time here)
      question_2.frameNStart = frameN;  // exact frame index
      
      question_2.setAutoDraw(true);
    }
    
    
    // *textbox_2* updates
    if (t >= 0.0 && textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_2.tStart = t;  // (not accounting for frame time here)
      textbox_2.frameNStart = frameN;  // exact frame index
      
      textbox_2.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
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
    questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'question' ---
    questionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('question.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var show_finalMaxDurationReached;
var _key_resp_9_allKeys;
var show_finalMaxDuration;
var show_finalComponents;
function show_finalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'show_final' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    show_finalClock.reset();
    routineTimer.reset();
    show_finalMaxDurationReached = false;
    // update component parameters for each repeat
    textbox_6.setText(idiom_question);
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    psychoJS.experiment.addData('show_final.started', globalClock.getTime());
    show_finalMaxDuration = null
    // keep track of which components have finished
    show_finalComponents = [];
    show_finalComponents.push(textbox_7);
    show_finalComponents.push(textbox_6);
    show_finalComponents.push(key_resp_9);
    
    show_finalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function show_finalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'show_final' ---
    // get current time
    t = show_finalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox_7* updates
    if (t >= 0.0 && textbox_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_7.tStart = t;  // (not accounting for frame time here)
      textbox_7.frameNStart = frameN;  // exact frame index
      
      textbox_7.setAutoDraw(true);
    }
    
    
    // *textbox_6* updates
    if (t >= 0.0 && textbox_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_6.tStart = t;  // (not accounting for frame time here)
      textbox_6.frameNStart = frameN;  // exact frame index
      
      textbox_6.setAutoDraw(true);
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
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
    show_finalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function show_finalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'show_final' ---
    show_finalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('show_final.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        psychoJS.experiment.addData('key_resp_9.duration', key_resp_9.duration);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "show_final" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endMaxDurationReached;
var endMaxDuration;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    endClock.reset(routineTimer.getTime());
    routineTimer.add(3.000000);
    endMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    endMaxDuration = null
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(endtxt);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endtxt* updates
    if (t >= 0.0 && endtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endtxt.tStart = t;  // (not accounting for frame time here)
      endtxt.frameNStart = frameN;  // exact frame index
      
      endtxt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (endtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      endtxt.setAutoDraw(false);
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
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    if (endMaxDurationReached) {
        endClock.add(endMaxDuration);
    } else {
        endClock.add(3.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
