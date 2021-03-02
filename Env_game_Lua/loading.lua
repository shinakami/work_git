display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local composer = require( "composer" )
local scene = composer.newScene()
physics.start()
local t=0
local controlRuntime=true
local repeat1=true
local gravity=physics.setGravity( 2.3, 6.5 )
math.randomseed(os.time())

function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
      title=display.newText(sceneGroup,"Deidare Puzzle",160,-10,system.nativeFont,30)

      display.newText(sceneGroup,"author: shina kami utsu",160,50,system.nativeFont,20)
      
      display.newText(sceneGroup,"Touch the screen",160,77,system.nativeFont,25)
      
      local sea = display.newImageRect(sceneGroup, "sea.png", 497, 462 )
      sea.x = 166
      sea.y = 320

    


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
   
      local function rungear()
          local GEAR1 = display.newImageRect(sceneGroup, "gear2.png", 113, 113 )
              GEAR1.x = 262
              GEAR1.y = 373
              physics.addBody( GEAR1, "static", { density=1, friction=0.3, bounce=0.2 } )
              
          local GEAR2 = display.newImageRect(sceneGroup, "gear2.png", 89, 89 )
              GEAR2.x = 226
              GEAR2.y = 459
              physics.addBody( GEAR2, "static", { density=1, friction=0.3, bounce=0.2 } )
              
          transition.to(GEAR1, {time=3000000, x=262, y=373, rotation=360000})
          transition.to(GEAR2, {time=3000000, x=226, y=459, rotation=-360000})
      end
      local function stop(event)
        if(controlRuntime==true)then
          event.phase=true
        end
        if(event.phase==true)then
          repeat1=false
          controlRuntime=false
          composer.gotoScene("loadgame",{ time=900,effect="zoomInOutFade" } )
        end
      end
      Runtime:addEventListener("touch",stop)
      
      local function star()
        if(repeat1==true)then            
          local names = {"A1","A2"}
          local name = names[math.random(#names)]
          local obj =display.newImageRect("images/"..name..".png",50,50)
          physics.addBody( obj, "dynamic", { density=1, friction=0.2, bounce=0.3 } )
          obj.x=math.random(200)
          obj.y=-30
          sceneGroup:insert(obj)
        end
      end  
      
      local function starflash(event)
        if(repeat1==true)then
          event.phase=true
        end
        if(event.phase==true)then
          star()
        end
      end
      timer.performWithDelay( 700, starflash,-1 )
      
      
      rungear()
     
     
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
                composer.removeScene("loading")
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























































