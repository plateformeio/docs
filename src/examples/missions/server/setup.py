import logging
import random

from faker import Faker

from server.main import app
from packages.assets import Material, Rocket, RocketPart
from packages.ops import Mission, Station
from packages.staff import Astronaut, Crew

logging.getLogger('faker').setLevel(logging.ERROR)

# --8<-- [start:snippet]
# Create database
app.metadata.create_all()

# Create fake data
fake = Faker()

# Create fake materials
materials = [
    Material(
        code=str(random.randint(1, 9999999999)),
        name=fake.name(),
        description=fake.sentence(),
        price=random.uniform(100000, 100000000),
    )
    for _ in range(random.randint(1, 100))
]
# --8<-- [end:snippet]

# Create fake rockets
rockets = [
    Rocket(
        code=str(random.randint(1, 9999999999)),
        name=fake.name(),
        description=fake.sentence(),
        parts=[
            RocketPart(
                code=f"{(count * 10):04d}",
                material=material,
                quantity=random.randint(1, 10),
            )
            for count, material in enumerate(
                random.sample(materials, random.randint(1, 10))
            )
        ],
    )
    for _ in range(random.randint(1, 100))
]

# Create fake astronauts
astronauts = [
    Astronaut(
        code=str(random.randint(1, 9999999999)),
        name=fake.name(),
        role=random.choice([
            'doctor', 'engineer', 'pilot', 'technician'
        ]),
    )
    for _ in range(random.randint(1, 100))
]

# Create fake crews
crews = [
    Crew(
        code=str(random.randint(1, 9999999999)),
        name=fake.word().capitalize(),
        astronauts=random.sample(astronauts, random.randint(2, 10)),
    )
    for _ in range(random.randint(1, 10))
]
# Assign lead to crews
for crew in crews:
    crew.lead = random.choice(crew.astronauts)

# Create fake stations
stations = [
    Station(
        code=str(random.randint(1, 9999999999)),
        name=fake.city(),
        description=fake.sentence(),
        coordinates=str(fake.local_latlng(coords_only=True)),
    )
    for _ in range(random.randint(1, 100))
]

# Create fake missions
missions = [
    Mission(
        code=str(random.randint(1, 9999999999)),
        name=fake.word().capitalize(),
        description=fake.sentence(),
        crew=random.choice(crews),
        rocket=random.choice(rockets),
        station=random.choice(stations),
        launch_date=fake.date_this_decade(),
    )
    for _ in range(random.randint(1, 100))
]

# Commit fake data
with app.session() as session:
    session.add_all([
        *astronauts,
        *crews,
        *materials,
        *rockets,
        *stations,
        *missions,
    ])
    session.commit()
    session.close()

# Generate summary
print('Mock data generated:')
print('- Astronauts:', len(astronauts))
print('- Crews:', len(crews))
print('- Materials:', len(materials))
print('- Rockets:', len(rockets))
print('- Stations:', len(stations))
print('- Missions:', len(missions))
