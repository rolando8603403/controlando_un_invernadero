let Humedad = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
    while (input.temperature() < 8) {
        music.startMelody(music.builtInMelody(Melodies.JumpDown), MelodyOptions.OnceInBackground)
        basic.showString("T.baja")
        basic.showArrow(ArrowNames.South)
    }
    while (input.temperature() > 30) {
        music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.OnceInBackground)
        basic.showString("T.Alta")
        basic.showArrow(ArrowNames.North)
    }
    if (input.temperature() >= 8 && input.temperature() <= 30) {
        music.stopMelody(MelodyStopOptions.All)
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        basic.showString("T.OK")
        basic.showIcon(IconNames.Yes)
    }
})
input.onButtonPressed(Button.B, function () {
    Humedad = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
    while (pins.analogReadPin(AnalogPin.P0) < 200) {
        music.startMelody(music.builtInMelody(Melodies.JumpDown), MelodyOptions.ForeverInBackground)
        basic.showString("H.baja")
        basic.showArrow(ArrowNames.South)
    }
    while (pins.analogReadPin(AnalogPin.P0) > 600) {
        music.startMelody(music.builtInMelody(Melodies.JumpDown), MelodyOptions.ForeverInBackground)
        basic.showString("H.Alta")
        basic.showArrow(ArrowNames.North)
    }
    if (pins.analogReadPin(AnalogPin.P0) >= 200 && pins.analogReadPin(AnalogPin.P0) <= 600) {
        music.stopMelody(MelodyStopOptions.All)
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        basic.showString("H.OK")
        basic.showIcon(IconNames.Yes)
    }
})
