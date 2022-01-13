USE whereidie
CREATE TABLE kd_collector_SPLIT (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);

CREATE TABLE kd_collector_HAVEN (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);
CREATE TABLE kd_collector_ASCENT (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);
CREATE TABLE kd_collector_BREEZE (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);
CREATE TABLE kd_collector_ICEBOX (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);
CREATE TABLE kd_collector_FRACTURE (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);
CREATE TABLE kd_collector_BIND (
    queueid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    attacker_team VARCHAR(32) NOT NULL,
    victim_team VARCHAR(32) NOT NULL,
    attacker_location_x INTEGER NOT NULL,
    attacker_location_y INTEGER NOT NULL,
    victim_location_x INTEGER NOT NULL,
    victim_location_y INTEGER NOT NULL,
    plant_status VARCHAR(32) NOT NULL
);

CREATE TABLE PLANT_LOCATIONS(
    queueid VARCHAR(32) NOT NULL,
    mapid VARCHAR(32) NOT NULL,
    rank_id INTEGER NOT NULL,
    red_team_econ VARCHAR(32) NOT NULL,
    blue_team_econ VARCHAR(32) NOT NULL,
    location_x INTEGER NOT NULL,
    location_y INTEGER NOT NULL
);
