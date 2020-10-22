const config = require('./config.js');

var firebase = require('firebase');
// var app = firebase.initializeApp(config);
firebase.initializeApp(config);
// firebase.analytics();

var isMovement = false;
var isMotor1 = false;
var isMotor2 = false;
var isMotor3 = false;

// firebase.database().ref('player1/movement').once('value').then( function(snapshot) {
//     var snap = JSON.stringify(snapshot.val())
//     console.log("SNAP: " + snap);
//     isMovement = true;
// });

firebase.database().ref('player1/movement').on('value', function(snapshot) {
    var snap = snapshot.val();
    console.log("SNAP: " + snap);

    if(snap = "STOP") {
        isMovement = false;
    } else {
        isMovement = true;
    }
});

firebase.database().ref('player1/motor1').on('value', function(snapshot) {
    var snap = snapshot.val();

    if(snap == "OPEN") {
        isMotor1 = true;
    } else {
        isMotor1 = false;
        console.log("MOTOR1: " + snap);
    }    
});

firebase.database().ref('player1/motor2').on('value', function(snapshot) {
    var snap = snapshot.val();

    if(snap == "OPEN") {
        isMotor2 = true;
    } else {
        isMotor2 = false;
        console.log("MOTOR2: " + snap);
    } 
});

firebase.database().ref('player1/motor3').on('value', function(snapshot) {
    var snap = snapshot.val()

    if(snap == "OPEN") {
        isMotor3 = true;
    } else {
        isMotor3 = false;
        console.log("MOTOR3: " + snap);
    } 
});

const Gpio = require('pigpio').Gpio;
const motor = new Gpio(10, {mode: Gpio.OUTPUT});
 
let pulseWidth = 1000;
let increment = 100;
 
setInterval(() => {
  motor.servoWrite(pulseWidth);
 
  pulseWidth += increment;
  if (pulseWidth >= 2000) {
    increment = -100;
  } else if (pulseWidth <= 1000) {
    increment = 100;
  }
}, 1000);