const config = require('./config.js');

var firebase = require('firebase');
// var app = firebase.initializeApp(config);
firebase.initializeApp(config);
// firebase.analytics();

var isMovement = false;
var movementVal = 0;
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
        moveMotor1(isMotor1);
    } else {
        isMotor1 = false;
        moveMotor1(isMotor1);
        console.log("MOTOR1: " + snap);
    }    
});

firebase.database().ref('player1/motor2').on('value', function(snapshot) {
    var snap = snapshot.val();

    if(snap == "OPEN") {
        isMotor2 = true;
        moveMotor2(isMotor2);
    } else {
        isMotor2 = false;
        moveMotor2(isMotor2);
        console.log("MOTOR2: " + snap);
    } 
});

firebase.database().ref('player1/motor3').on('value', function(snapshot) {
    var snap = snapshot.val()

    if(snap == "OPEN") {
        isMotor3 = true;
        moveMotor3(isMotor3);
    } else {
        isMotor3 = false;
        moveMotor3(isMotor3);
        console.log("MOTOR3: " + snap);
    } 
});


// This is while look, it will run forever
setInterval(() => {
    if(isMovement) {
        // Move both motors
    }
}, 10);


function moveMotor1(isOpen) {

}

function moveMotor2(isOpen) {

}

function moveMotor3(isOpen) {

}


// const Gpio = require('pigpio').Gpio;
// const motor = new Gpio(10, {mode: Gpio.OUTPUT});
 
// let pulseWidth = 1000;
// let increment = 100;
 
// setInterval(() => {
//   motor.servoWrite(pulseWidth);
 
//   pulseWidth += increment;
//   if (pulseWidth >= 2000) {
//     increment = -100;
//   } else if (pulseWidth <= 1000) {
//     increment = 100;
//   }
// }, 1000);