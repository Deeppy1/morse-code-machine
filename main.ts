input.onButtonPressed(Button.A, function () {
    basic.showNumber(0)
    pins.digitalWritePin(DigitalPin.P0, 0)
})
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(1)
    pins.digitalWritePin(DigitalPin.P1, 1)
})
basic.forever(function () {
	
})
