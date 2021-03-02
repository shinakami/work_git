display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local composer = require( "composer" )
local scene = composer.newScene()
physics.start()
local time=1
math.randomseed(os.time())
random_round=math.random(5)
function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
      
      local magic = display.newImageRect(sceneGroup, "magic2.png", 600, 600 )
      magic.x = 160 
      magic.y = 264

      title=display.newText(sceneGroup,"Round",130,264,system.nativeFont,30)
      rounding=display.newText(sceneGroup,round,210,264,system.nativeFont,30)
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
     
     local function turn()
          if(random_round==1)then
            composer.gotoScene("game1",{ time=500,effect="zoomInOutFade" } )
          end
          if(random_round==2)then
            composer.gotoScene("game2",{ time=500,effect="zoomInOutFade" } )
          end
          if(random_round==3)then
            composer.gotoScene("game3",{ time=500,effect="zoomInOutFade" } )
          end
          if(random_round==4)then
            composer.gotoScene("game4",{ time=500,effect="zoomInOutFade" } )
          end
          if(random_round==5)then
            composer.gotoScene("game5",{ time=500,effect="zoomInOutFade" })
          end
     end
     
     local function setTime()
      time=time-1
      
      if(time==0)then
        turn()
      end
     end
     
     
     timer.performWithDelay( 600, setTime,time )
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
                composer.removeScene("round")
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























































