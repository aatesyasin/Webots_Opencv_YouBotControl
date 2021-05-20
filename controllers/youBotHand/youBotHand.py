from controller import Robot
from controller import Keyboard, Lidar, GPS
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time, math
import ClsHand
detector=ClsHand.handDeetector()
HedefGps=[0,0,0]

class Rbtclnt:
  def __init__(objectx, name, WheelRightF,WheelLeftF,WheelRightB,WheelLeftB,):
    objectx.Rbt = Robot()
    objectx.timestep = 64   
    objectx.WheelRightF = objectx.Rbt.getDevice(WheelRightF)
    objectx.WheelLeftF = objectx.Rbt.getDevice(WheelLeftF)
    objectx.WheelRightB = objectx.Rbt.getDevice(WheelRightB)
    objectx.WheelLeftB = objectx.Rbt.getDevice(WheelLeftB)

    objectx.WheelRightF.setPosition(float("inf"))
    objectx.WheelLeftF.setPosition(float("inf"))
    objectx.WheelRightB.setPosition(float("inf"))
    objectx.WheelLeftB.setPosition(float("inf"))

    objectx.WheelRightF.setVelocity(0)
    objectx.WheelLeftF.setVelocity(0)
    objectx.WheelRightB.setVelocity(0)
    objectx.WheelLeftB.setVelocity(0)

  def RbF(self,Vlc):
    self.WheelRightF.setVelocity(Vlc)
    self.WheelLeftF.setVelocity(Vlc)
    self.WheelRightB.setVelocity(Vlc)
    self.WheelLeftB.setVelocity(Vlc)

  def RbB(self,Vlc):
    self.WheelRightF.setVelocity(-Vlc)
    self.WheelLeftF.setVelocity(-Vlc)
    self.WheelRightB.setVelocity(-Vlc)
    self.WheelLeftB.setVelocity(-Vlc)

  def RbR(self,Vlc):
    self.WheelRightF.setVelocity(-Vlc)
    self.WheelLeftF.setVelocity(Vlc)
    self.WheelRightB.setVelocity(Vlc)
    self.WheelLeftB.setVelocity(-Vlc)

  def RbL(self,Vlc):
    self.WheelRightF.setVelocity(Vlc)
    self.WheelLeftF.setVelocity(-Vlc)
    self.WheelRightB.setVelocity(-Vlc)
    self.WheelLeftB.setVelocity(Vlc)

  def RbDFR(self,Vlc):
    self.WheelRightF.setVelocity(0)
    self.WheelLeftF.setVelocity(Vlc)
    self.WheelRightB.setVelocity(Vlc)
    self.WheelLeftB.setVelocity(0)

  def RbDFL(self,Vlc):
    self.WheelRightF.setVelocity(Vlc)
    self.WheelLeftF.setVelocity(0)
    self.WheelRightB.setVelocity(0)
    self.WheelLeftB.setVelocity(Vlc)

  def RbDBL(self,Vlc):
    self.WheelRightF.setVelocity(0)
    self.WheelLeftF.setVelocity(-Vlc)
    self.WheelRightB.setVelocity(-Vlc)
    self.WheelLeftB.setVelocity(0)

  def RbDBR(self,Vlc):
    self.WheelRightF.setVelocity(-Vlc)
    self.WheelLeftF.setVelocity(0)
    self.WheelRightB.setVelocity(0)
    self.WheelLeftB.setVelocity(-Vlc)

  def RbTR(self,Vlc):
    self.WheelRightF.setVelocity(-Vlc)
    self.WheelLeftF.setVelocity(Vlc)
    self.WheelRightB.setVelocity(-Vlc)
    self.WheelLeftB.setVelocity(Vlc)

  def RbTL(self,Vlc):
    self.WheelRightF.setVelocity(Vlc)
    self.WheelLeftF.setVelocity(-Vlc)
    self.WheelRightB.setVelocity(Vlc)
    self.WheelLeftB.setVelocity(-Vlc)

  def RbS(self):
    self.WheelRightF.setVelocity(0)
    self.WheelLeftF.setVelocity(0)
    self.WheelRightB.setVelocity(0)
    self.WheelLeftB.setVelocity(0)


def Hareket(key):
  Output=[0,0,0,0,0,0]
  if key ==ord('W') or key ==[0,0,0,0,1]: 
    YouBotX.RbF(10)
    Output=[1,0,0,0,0,0]
  elif key ==ord('S') or key ==[1,0,0,0,1]: 
    YouBotX.RbB(10)
    Output=[0,1,0,0,0,0]
            
  elif key == ord('A') or key ==[0,0,0,1,1]: 
    YouBotX.RbL(10)
    Output=[0,0,1,0,0,0]
        
  elif key ==ord('D') or key ==[1,0,0,1,1]: 
    YouBotX.RbR(10)
    Output=[0,0,0,1,0,0]
    
  elif key ==ord('E'): 
    YouBotX.RbDFR(10)
            
  elif key ==ord('Q'): 
    YouBotX.RbDFL(10)
                  
  elif key ==ord('C'): 
    YouBotX.RbDBR(10)
  elif key ==ord('Z'): 
    YouBotX.RbDBL(10)
  elif key ==ord('B') or key ==[0,1,1,1,1]: 
    YouBotX.RbTL(10)
    Output=[0,0,0,0,1,0]
  elif key ==ord('N') or key ==[1,1,1,1,1]: 
    YouBotX.RbTR(10)
    Output=[0,0,0,0,0,1]    
  else:
    YouBotX.RbS()
  return Output    


def main():
    global YouBotX  
    cap= cv2.VideoCapture(0)    
    

    while YouBotX.Rbt.step(YouBotX.timestep) != -1:
        suc, img= cap.read()
        img=detector.findHands(img)
        lmList,bbox=detector.finPosition(img)

        if len(lmList) !=0:
            area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
            if 90<area<1100:                
                #length,img,LineInfo=detector.findDistance(4,8,img)
                #print(length//1)
                fingers=detector.fingersUp()
                print(fingers)
                
                OutputData=Hareket(fingers)
                


        cv2.imshow("aa",img)
        cv2.waitKey(1)


if __name__ == '__main__':
  YouBotX=Rbtclnt("YouBotX","wheel1","wheel2","wheel3","wheel4")
  main()

    
        
        