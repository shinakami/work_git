display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local composer = require( "composer" )
local scene = composer.newScene()
local controlRuntime=true
local repeat1=true
physics.start()
math.randomseed(os.time())
local gravity2=physics.setGravity( 0, 3.8 )
function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
     
       local sea = display.newImageRect(sceneGroup, "firecat.png", 409, 594 )
        sea.x = 156
        sea.y = 250
      display.newText(sceneGroup,"USED ROUNDS:",160,280,system.nativeFont,25)
      display.newText(sceneGroup,round-1,160,320,system.nativeFont,25)  
      p=display.newText(sceneGroup,"YOU WIN",160,388,system.nativeFont,25)
      code=display.newText(sceneGroup,"shinakami404",160,200,system.nativeFont,25)
      local function go(event)
        repeat1=false
        composer.gotoScene("theme",{ time=900,effect="fade" } )
      end
      sea:addEventListener("touch",go)

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
     local function star()
        if(repeat1==true)then            
          local names = {"A1","A2"}
          local name = names[math.random(#names)]
          local obj =display.newImageRect("images/"..name..".png",40,40)
          physics.addBody( obj, "dynamic", { density=1, friction=0.2, bounce=0.3 } )
          obj.x=math.random(250)
          obj.y=-12
          sceneGroup:insert(obj)
        end
      end  
      
      local function starflash()
        if(repeat1==true)then
          star()
        end
      end
      timer.performWithDelay( 400, starflash,-1 )
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
                composer.removeScene("win")
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























































