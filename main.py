import asyncio
import os

from final_code.agents import populate_city
from final_code.environment import load_env
from final_code.disasters import Disaster, RepairMan


async def main():
    environment = load_env("./final_code/city_design.txt")
    all_agents = populate_city(environment,n_rescuers=12,n_suppliers=3)

    for agent in all_agents:
        await agent.start(auto_register=True)
    print("<all agents loaded>")

    distaster_manager = Disaster("disastermanager@localhost","password",environment)
    await distaster_manager.start(auto_register=True)
    repair_manager = RepairMan("repairmanager@localhost","password",environment)
    await repair_manager.start(auto_register=True)

    os.system("clear")
    print("5 minute simulation\n")

    await asyncio.sleep(300)  # correr por 5 min

    print("\nPerformances:")
    print("Number of civilians rescued: ",environment.civilians_rescued)
    print(f"Tempo medio de salvamento: {environment.total_rescuers_time_traveled/environment.total_rescuers_trips:.2f}")
    print("Delivered resources: ",environment.supplies_delivered)
    print(f"Average time to restock: {(environment.total_suppliers_time_traveled / environment.total_suppliers_trips):.2f}")
    print(f"Average time to drive civilians back home: {(environment.total_transport_home_time_traveled / environment.total_transport_home_trips):.2f}")

    os._exit(0)
    await distaster_manager.stop()
    await repair_manager.stop()

    for agent in all_agents:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
