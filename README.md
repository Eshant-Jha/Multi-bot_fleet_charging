# Robot Fleet Charging System

## Overview
An intelligent battery management system for a fleet of 5 robots that optimizes charging schedules based on battery levels and operational requirements.

## System Goals
- Maintain at least 3 robots with ≥20% battery
- Prioritize charging for robots with lowest battery levels
- Ensure continuous operation with minimal downtime
- Maximize battery efficiency

## Key Constraints
- Battery discharge rate: 1% per second
- Battery charging rate: 1.5% per second
- Available charging stations: 2

## Architecture
The system consists of two main components:
- **Robot Class**: Manages individual robot state (ID, battery level, charging status)
- **Compute Class**: Handles charging decision logic through prioritization algorithms

## Charging Strategy
1. **Robot Scoring**: Assign priority based on battery level and charging status
2. **Sorting**: Order robots by score and battery level
3. **Charging Assignment**: Allocate limited charging resources to highest priority robots
4. **Safety Check**: Ensure minimum operational fleet requirements are met

## Edge Case Management
- Handling fully charged robots
- Managing limited charging station availability
- Preventing charge/discharge oscillation
- Emergency prioritization when fleet viability is threatened

## Documentation
Full documentation is available in the repository detailing:
- Complete algorithm implementations
- Performance metrics
- Edge case handling
- Future enhancement opportunities

## Usage
The system outputs real-time information on:
- Number of operational robots
- Each robot's battery level and charging status

---

*This project demonstrates optimized resource allocation for autonomous systems with limited charging infrastructure.*
