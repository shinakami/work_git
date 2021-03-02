display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local gravity=physics.setGravity( 0, 6.5 )
local composer = require( "composer" )
local scene = composer.newScene()
local controlRuntime=true
physics.start()
math.randomseed(os.time())

function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
     
       local sea = display.newImageRect(sceneGroup, "earthdie.png", 409, 594 )
        sea.x = 156
        sea.y = 250
        
      p=display.newText(sceneGroup,"YOU LOST",160,388,system.nativeFont,25)
      local function go(event)
        if(controlRuntime==true)then
          event.phase=true
        end
        if(event.phase==true)then
          controlRuntime=false
          composer.gotoScene("loading",{ time=900,effect="fade" } )
        end
      end
      Runtime:addEventListener("touch",go)

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
                composer.removeScene("die")
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























































