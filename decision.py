# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:05:31 2025

@author: ESHANT
"""



class Compute():
    
    def __init__(self):
        
        self.threshold_level= 21 
        self.threshold_min_switching = 25
    def priority(self,fleet_data):
        
        fleet_status =[r.copy() for r in  fleet_data]
        
        for robot  in fleet_status:
            
            charging = robot['battery'] #Checking if its already being charged 
            battery_level = robot['status']
            
            if battery_level <= self.threshold_level:
                robot['score'] = 0 
            elif battery_level <= self.threshold_min_switching and charging: #trying to minimise the continuos switching
                robot['score'] =1
            else:
                robot['score']= 2
                
        fleet_status.sort(key=lambda x: (x['score'], x['battery']))
        
        count_of_robot_charging =0
        charging_station = 2 
        
        for robot in fleet_status:   #here fleet status is already sorted as per score and battery level
            
        
            if robot['battery'] >= 100 and robot['status'] :   #removing already charged bots 
                robot['status'] = False
                continue
                
            if robot['status'] and count_of_robot_charging < charging_station:
                count_of_robot_charging +=1
        
            elif not robot['status'] and count_of_robot_charging < charging_station: 
                count_of_robot_charging +=1
                robot['status']=True
            
             
            else:
                robot['status'] = False                

        safe_ops = sum(1 for r in fleet_status if r['battery']>=20)
        
        if safe_ops>=3:
            print(f"Objective maintained - {safe_ops} running now ")
            
        else:
            print(f"Objective failed - {safe_ops} running now ")
            self.threshold_min_switching = 20
            fleet_status.sort(key=lambda x: x['battery'], reverse=True)
            count = 0
            #here trying to proritise top three battery levels minimising downtime 
            for robot in fleet_status: 
                count+=1
                if robot['status'] and count <2:
                    continue
                elif not robot['status'] and count<2:
                    robot['status']= True
                    
            
        return fleet_status
    
    
