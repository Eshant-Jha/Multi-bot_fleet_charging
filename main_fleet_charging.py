# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 03:44:43 2025

@author: ESHANT
"""

import time 
from decision import Compute

class Robot():
    
    def __init__(self,id, battery):
        
        self.robot_id= id 
        self.battery = float(battery)
        self.charging_status = False 
        print(f"Robot {id} inital battery % ={battery} ")
        time.sleep(0.2)
        
    def charge_rate(self):
        
        if self.charging_status :
            
            self.battery =min(self.battery + 1.5, 100)   
            
        else:
            self.battery =max(0,self.battery - 1) 
            self.charging_status = False
            
        print(f"Robot {self.robot_id}, present_battery % ={self.battery},charging_status ={self.charging_status} ")
            


if __name__ == "__main__":
    

    robots = {
    1: Robot(1, 20),
    2: Robot(2, 20),
    3: Robot(3, 40),
    4: Robot(4, 40),
    5: Robot(5, 10)
                   }
    
    
    try:
        while True:
            
            fleet_data = [ {'id': r.robot_id, 'status': r.charging_status, 'battery': r.battery} for r in robots.values()]
            
            current_fleet = Compute().priority(fleet_data)
            
            for robot in current_fleet:
                robots[robot['id']].charging_status = robot['status']
    
            for robot in robots.values():
                    robot.charge_rate()
    
            print()
            time.sleep(2)
    except KeyboardInterrupt:
        
        print("\nTerminated")
        
        
    

 
            
            