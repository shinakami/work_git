display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local composer = require( "composer" )
local scene = composer.newScene()
physics.start()
local time=2
math.randomseed(os.time())
function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
      
      local magic = display.newImageRect(sceneGroup, "20131226104118144.png", 600, 600 )
      magic.x = 160 
      magic.y = 264

      title=display.newText(sceneGroup,"Loading",160,-10,system.nativeFont,30)
      timing=display.newText(sceneGroup,time,160,264,system.nativeFont,30)
      transition.to(magic, {time=7000000, x=160, y=264, rotation=360000})


    -- Initialize the scene here
    -- Example: add display objects to "sceneGroup", add touch listeners, etc.
end


-- "scene:show()"
function scene:show( event )

    local sceneGroup = self.view
    local phase = event.phase
    if ( phase == "will" ) then
        -- Called when the scene is still off screen (but is about to come on screen)
    elseif ( phase == "did" ) then
     
     
     local function setTime()
      time=time-1
      timing.text=time
      if(time==0)then
        composer.gotoScene("theme",{ time=900,effect="fade" } )
      end
     end
     
     timer.performWithDelay( 800, setTime,time )
    end
end


-- "scene:hide()"
function scene:hide( event )

    local sceneGroup = self.view
    local phase = event.phase

    if ( phase == "will" ) then
        -- Called when the scene is on screen (but is about to go off screen)
        -- Insert code here to "pause" the scene
        -- Example: stop timers, stop animation, stop audio, etc.
    elseif ( phase == "did" ) then
        -- Called immediately after scene goes off screen
                composer.removeScene("loadgame")
    end
end


-- "scene:destroy()"
function scene:destroy( event )

    local sceneGroup = self.view

        sceneGroup:removeSelf()   
        sceneGroup = nil     
    -- Called prior to the removal of scene's view
    -- Insert code here to clean up the scene
    -- Example: remove display objects, save state, etc.
end


-- -------------------------------------------------------------------------------

-- Listener setup
scene:addEventListener( "create", scene )
scene:addEventListener( "show", scene )
scene:addEventListener( "hide", scene )
scene:addEventListener( "destroy", scene )

-- -------------------------------------------------------------------------------

return scene























































