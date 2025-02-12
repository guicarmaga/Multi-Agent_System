# Multi-Agent System
Multi-Agent Disaster Response and Relief Coordination System group project as part of the "Introduction to Intelligent and Autonomous Systems" course at FCUP (Porto, Portugal).

Problem Scenario:

In the aftermath of a natural disaster (e.g., earthquake, hurricane, or flood), relief efforts must be organized efficiently to ensure that affected areas receive food, medical supplies, rescue services, and shelter. Traditional centralized disaster management systems often struggle to cope with real-time challenges such as rapidly changing conditions, road blockages, and communication breakdowns. A decentralized system with autonomous agents representing different entities can respond more flexibly and efficiently to changing conditions and resource constraints.

Key Features of the Assignment:

Responder Agents: These agents represent emergency response teams responsible for rescuing civilians, delivering medical aid, and assessing damage in affected areas. Responder agents must decide which locations to prioritize based on the urgency of needs and available resources.
Supply Vehicle Agents: These agents manage the delivery of resources (food, water, medical supplies) from centralized depots to affected regions or shelters. They should optimize routes, taking into account road conditions, traffic, and time-sensitive needs in various locations.
Shelter Agents: Shelter agents represent temporary shelters set up to house displaced civilians. They need to communicate with supply agents to request resources and with responder agents to coordinate the transportation of civilians to shelters.
Civilian Agents: Civilians are represented by agents in need of various forms of assistance (e.g., rescue, medical care, food, and shelter). These agents will signal their needs, which responder agents and shelters must address in a coordinated way.
Dynamic Disaster Environment: The system operates in a rapidly changing environment. Roadblocks may emerge, buildings may collapse, new areas may become affected, and communication may be unreliable. Agents must adapt to these dynamic conditions and reprioritize their tasks in real time.
Decentralized Coordination: Each agent operates independently but collaborates with others through communication and negotiation to achieve global goals, such as minimizing casualties and delivering resources efficiently. No central authority dictates how agents should operate.
Resource and Time Optimization: Agents must manage limited resources (e.g., fuel for vehicles, available medical supplies) and work within time constraints. For instance, medical aid must be delivered within a certain time frame to save lives, and supply vehicles must optimize their routes to serve the greatest number of people in the shortest time.
Collaboration and Negotiation: Agents must communicate and negotiate with one another to ensure that resources are allocated effectively. For example, responder agents might negotiate with supply vehicle agents to prioritize medical supply delivery, while shelter agents request food and water based on their current capacity.
Performance Metrics: The system should measure success based on:
Number of civilians rescued
Speed of resource delivery to affected areas
Efficiency of resource use (minimizing waste and avoiding oversupply)
System resilience in responding to new and unexpected events
