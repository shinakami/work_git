display.setStatusBar( display.HiddenStatusBar )
local composer = require( "composer" )
composer.gotoScene("loading" )
bgm = audio.loadStream("demo.wav" )
audio.play( bgm, { loops=-1 } )



