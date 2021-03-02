display.setStatusBar( display.HiddenStatusBar )
local physics = require( "physics" )
local composer = require( "composer" )
local scene = composer.newScene()
local controlRuntime=true
physics.start()
local gravity=physics.setGravity( 0, 6.5 )
math.randomseed(os.time())
round=round+1
local time=2
local T=5
local confirm=1
local hintchoice=math.random(3)
if(hint>0)then
  hint=hint-1
end
if(stoptime>0)then
  stoptime=stoptime-1
  
end
function scene:create( event )

      local sceneGroup = self.view
      local phase = event.phase
      display.newText(sceneGroup,"player life:",201,-7,system.nativeFont,15.5)
      player=display.newText(sceneGroup,playerlife,270,-7,system.nativeFont,15.5)
      display.newText(sceneGroup,"deidare life:",57,-7,system.nativeFont,15.5)
      deidare=display.newText(sceneGroup,deidarelife,126,-7,system.nativeFont,15.5)
      
      local timestop = audio.loadSound("powerc.wav" )
      local spotter = audio.loadSound("submarin.wav" )
      
      local five = display.newImageRect(sceneGroup, "five.jpg", 323, 284 )
        five.x = 159
        five.y = 589
        physics.addBody( five, "static", { density=1, friction=0.3, bounce=0.2 } )
      
      local dispObj_10 = display.newImageRect(sceneGroup, "frame.jpg", 361, 17 )
        dispObj_10.x = 170
        dispObj_10.y = 311
        physics.addBody( dispObj_10, "static", { density=1, friction=0.3, bounce=0.3 } )

      
     
      local dispObj_6 = display.newImageRect(sceneGroup, "Frame151447a.png", 380, 400 )
        dispObj_6.x = 158
        dispObj_6.y = 143


    
    display.newText(sceneGroup,"chose your card",158,320,system.nativeFont,15.5)
    
    local eye = display.newImageRect(sceneGroup, "eye.png", 27, 27 )
        eye.x = 25
        eye.y = 325
    local function spotcard()
      if(hint==0)then
        audio.play( spotter )
        audio.dispose(spotter )
        hint=3
        if(hintchoice==1)then
          local gold = display.newImageRect(sceneGroup, "gold.png", 134, 230 )
              gold.x = 86
              gold.y = 145
        end
        if(hintchoice==2)then
          local fire = display.newImageRect(sceneGroup, "fire.png", 134, 230 )
              fire.x = 86
              fire.y = 145
          display.newText(sceneGroup,"True",57,40,system.nativeFont,15.5)
        end
        if(hintchoice==3)then
           local tree = display.newImageRect(sceneGroup, "tree.png", 134, 230 )
              tree.x = 86
              tree.y = 145
           display.newText(sceneGroup,"False",57,40,system.nativeFont,15.5)
        end
      end
    end
    eye:addEventListener("tap",spotcard)
    if(hint>0)then
        display.newText(sceneGroup,hint,25,325,system.nativeFont,20)
    end
    
    local timeclock = display.newImageRect(sceneGroup, "timeclock.png", 40, 40 )
        timeclock.x = 70
        timeclock.y = 325
    local function stop()
      if(stoptime==0)then
        confirm=2
        audio.play( timestop )
        audio.dispose(timestop )
        test = display.newText(sceneGroup,"Time Stopped",211,40,system.nativeFont,15.5)
        test:setFillColor(0,0.4,0.5)
        stoptime=8
      end
    end
    timeclock:addEventListener("tap",stop)
    if(stoptime>0)then
        display.newText(sceneGroup,stoptime,70,325,system.nativeFont,20)
    end
      
    local shape_1 = { -3,-165, -3,160, 4,160, 3,-163 }
        shape_1.density = 1; shape_1.friction = 0.3; shape_1.bounce = 0.3; 

    local dispObj_7 = display.newImageRect(sceneGroup, "e7bebce161704ea55cd6ece284202d40.png", 60, 332 )
        dispObj_7.x = 158
        dispObj_7.y = 138
        physics.addBody( dispObj_7, "static", 
            {density=shape_1.density, friction=shape_1.friction, bounce=shape_1.bounce, shape=shape_1}
        )
    
      local dispObj_8 = display.newImageRect(sceneGroup, "magic2.png", 150, 150 )
        dispObj_8.x = 85
        dispObj_8.y = 206
      
      transition.to(dispObj_8, {time=30000000, x=85, y=206, rotation=3600000})
      
      local dispObj_9 = display.newImageRect(sceneGroup, "magicgold.png", 150, 150 )
        dispObj_9.x = 231
        dispObj_9.y = 206
        
      transition.to(dispObj_9, {time=30000000, x=231, y=206, rotation=-3600000})
      
     
     

     
       

    -- Initialize the scene here
    -- Example: add display objects to "sceneGroup", add touch listeners, etc.
end


-- "scene:show()"
function scene:show( event )

    local sceneGroup = self.view
    local phase = event.phase
    local hit = audio.loadSound("hit.wav" )
    if ( phase == "will" ) then
        -- Called when the scene is still off screen (but is about to come on screen)
    elseif ( phase == "did" ) then
      
      display.newText(sceneGroup,"time:",245,320,system.nativeFont,15.5)
      count=display.newText(sceneGroup,T,270,320,system.nativeFont,15.5)
      
     
      
      local dispObj_1 = display.newImageRect(sceneGroup, "goldblack.png", 63, 100 )
      dispObj_1.x = 32
      dispObj_1.y = 385
      physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
      
      local dispObj_2 = display.newImageRect(sceneGroup, "treeyouth.PNG", 63, 100 )
      dispObj_2.x = 95
      dispObj_2.y = 385
      physics.addBody( dispObj_2, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
      
      local dispObj_3 = display.newImageRect(sceneGroup, "waterfly.png", 63, 100 )
      dispObj_3.x = 158
      dispObj_3.y = 385
      physics.addBody( dispObj_3, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
      
      local dispObj_4 = display.newImageRect(sceneGroup, "sea.png", 63, 100 )
      dispObj_4.x = 221
      dispObj_4.y = 385
      physics.addBody( dispObj_4, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
      
      local dispObj_5 = display.newImageRect(sceneGroup, "earthblack.png", 63, 100 )
      dispObj_5.x = 284
      dispObj_5.y = 385
      physics.addBody( dispObj_5, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
      
      local function touch1()
        if(confirm==1 or confirm==2)then
         
          
          display.newText(sceneGroup,"DRAW",201,20,system.nativeFont,15.5)
          display.newText(sceneGroup,"DRAW",57,20,system.nativeFont,15.5)
          
          local dispObj_1 = display.newImageRect(sceneGroup, "goldblack.png", 134, 230 ) ------player result
            dispObj_1.x = 229
            dispObj_1.y = 131
           physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
          
          local dispObj_1 = display.newImageRect(sceneGroup,"goldblack.png", 134, 230 ) -----deidare result
            dispObj_1.x = 86
            dispObj_1.y = 131
          physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
          
          confirm=0
          
          local function setTime()
            time=time-1
            if(time==0)then
               composer.gotoScene("round",{ time=600,effect="fade" } )
            end
          end
          timer.performWithDelay( 1000, setTime,time )
         end
      end
      dispObj_1:addEventListener("touch",touch1)
      
      local function touch2()
      
        if(confirm==1 or confirm==2)then
            
            playerlife=playerlife-200
            player.text=playerlife
            deidarelife=deidarelife+200
            deidare.text=deidarelife
            
            display.newText(sceneGroup,"LOSE",201,20,system.nativeFont,15.5)
            display.newText(sceneGroup,"WIN",57,20,system.nativeFont,15.5)
            
            local dispObj_2 = display.newImageRect(sceneGroup, "treeyouth.PNG", 134, 230 ) ------player result
              dispObj_2.x = 229
              dispObj_2.y = 131
             physics.addBody( dispObj_2, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            local dispObj_1 = display.newImageRect(sceneGroup,"goldblack.png", 134, 230 ) -----deidare result
              dispObj_1.x = 86
              dispObj_1.y = 131
             physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            confirm=0
            
            local function setTime()
              time=time-1
              if(time==0 and playerlife>0)then
                 composer.gotoScene("round",{ time=600,effect="fade" } )
              end
              if(time==0 and playerlife==0)then
                 composer.gotoScene("die",{ time=600,effect="fade" } )
              end
            end
            timer.performWithDelay( 1000, setTime,time )
           end
        end
        dispObj_2:addEventListener("touch",touch2)
        
        local function touch3()
          if(confirm==1 or confirm==2)then
            deidarelife=deidarelife-200
            deidare.text=deidarelife
            
            display.newText(sceneGroup,"WIN",201,20,system.nativeFont,15.5) ------player result
            display.newText(sceneGroup,"DRAW",57,20,system.nativeFont,15.5)-----deidare result
            
            local dispObj_3 = display.newImageRect(sceneGroup, "waterfly.png", 134, 230 ) ------player result
              dispObj_3.x = 229
              dispObj_3.y = 131
             physics.addBody( dispObj_3, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            local dispObj_1 = display.newImageRect(sceneGroup,"goldblack.png", 134, 230 ) -----deidare result
              dispObj_1.x = 86
              dispObj_1.y = 131
             physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
             
            confirm=0
            
            local function setTime()
              time=time-1
              if(time==0 and deidarelife>0)then
               composer.gotoScene("round",{ time=600,effect="fade" } )
              end
              if(time==0 and deidarelife==0)then
               composer.gotoScene("win",{ time=600,effect="fade" } )
              end
            end
            timer.performWithDelay( 1000, setTime,time )
           end
        end
        dispObj_3:addEventListener("touch",touch3)
        
        local function touch4()
        
          if(confirm==1 or confirm==2)then
            playerlife=playerlife+200
            player.text=playerlife
            deidarelife=deidarelife-200
            deidare.text=deidarelife
            
            
            audio.play( hit )
            audio.dispose( hit ) 
            
            display.newText(sceneGroup,"WIN",201,20,system.nativeFont,15.5) ------player result
            display.newText(sceneGroup,"LOSE",57,20,system.nativeFont,15.5)-----deidare result
            
            local dispObj_4 = display.newImageRect(sceneGroup, "sea.png", 134, 230 ) ------player result
              dispObj_4.x = 229
              dispObj_4.y = 131
             physics.addBody( dispObj_4, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            local dispObj_1 = display.newImageRect(sceneGroup,"goldblack.png", 134, 230 ) -----deidare result
              dispObj_1.x = 86
              dispObj_1.y = 131
             physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            confirm=0
            
            local function setTime()
              time=time-1
              if(time==0 and deidarelife>0)then
               composer.gotoScene("round",{ time=600,effect="fade" } )
              end
              if(time==0 and deidarelife==0)then
               composer.gotoScene("win",{ time=600,effect="fade" } )
              end
            end
            timer.performWithDelay( 1000, setTime,time )
           end
        end
        dispObj_4:addEventListener("touch",touch4)
        
        local function touch5()
        
          if(confirm==1 or confirm==2)then
          
            playerlife=playerlife-200
            player.text=playerlife
            
            display.newText(sceneGroup,"DRAW",201,20,system.nativeFont,15.5)------player result
            display.newText(sceneGroup,"WIN",57,20,system.nativeFont,15.5)-----deidare result
            
            local dispObj_5 = display.newImageRect(sceneGroup, "earthblack.png", 134, 230 ) ------player result
              dispObj_5.x = 229
              dispObj_5.y = 131
             physics.addBody( dispObj_5, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            local dispObj_1 = display.newImageRect(sceneGroup,"goldblack.png", 134, 230 ) -----deidare result
              dispObj_1.x = 86
              dispObj_1.y = 131
            physics.addBody( dispObj_1, "dynamic", { density=1, friction=0.3, bounce=0.2 } )
            
            confirm=0
            
            local function setTime()
              time=time-1
              if(time==0 and playerlife>0)then
                 composer.gotoScene("round",{ time=600,effect="fade" } )
              end
              if(time==0 and playerlife==0)then
                 composer.gotoScene("die",{ time=600,effect="fade" } )
              end
            end
            timer.performWithDelay( 1000, setTime,time )
           end
        end
        dispObj_5:addEventListener("touch",touch5)
        
        local function time(event)
          if(confirm==1)then
            T=T-1
            count.text=T
            if(T==0)then
              playerlife=playerlife-200
              player.text=playerlife
              if(T==0 and playerlife>0)then
                display.newText(sceneGroup,"Time out",201,17,system.nativeFont,15.5)
                confirm=confirm-1
                composer.gotoScene("round",{ time=600,effect="fade" } )
              elseif(T==0 and playerlife==0)then
                display.newText(sceneGroup,"Time out",201,17,system.nativeFont,15.5)
                confirm=confirm-1
                composer.gotoScene("die",{ time=600,effect="fade" } )
              end
            end
          end
        end

        local function settime(event)
          if(T>0 and confirm==1)then
            event.phase=true
          end
          if(event.phase==true and confirm==1)then
            time()
          end
        end
        timer.performWithDelay( 1000, settime,-1 )
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
                composer.removeScene("game2")
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























































