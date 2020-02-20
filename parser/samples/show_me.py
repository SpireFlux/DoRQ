import sc2reader

r = sc2reader.load_replay('EE_LE.SC2Replay')


# print('r.active_units')
# print(r.active_units)
# print('\n')

# print('r.amm')
# print(r.amm)
# print('\n')

# print('r.archive')
# print(r.archive)
# print('\n')


# print('r.attributes')
# print(r.attributes)
# print('\n')

# print('r.base_build')
# print(r.base_build)
# print('\n')


# print('r.battle_net')
# print(r.battle_net)
# print('\n')

# r.build
# print('')
# print()
# print('\n')

attribs = [r.category, r.client, r.clients, r.competitive, r.computer]

for val in attribs:
    print(repr(val))
    print(val)
    print('\n')

r.computers
r.cooperative
r.datapack
r.date
r.end_time
r.entities
r.entity
r.events
r.expansion
r.factory
r.filehash
r.filename
r.frames
r.game_events
r.game_fps
r.game_length
r.game_type
r.hero_duplicates_allowed
r.human
r.humans
r.is_ladder
r.is_private
r.length
r.load_all_details
r.load_attribute_events
r.load_details
r.load_game_events
r.load_init_data
r.load_level
r.load_map
r.load_message_events
r.load_players
r.load_tracker_events
r.logger
r.map
r.map_file
r.map_hash
r.map_name
r.message_events
r.messages
r.objects
r.observer
r.observers
r.opt
r.packets
r.people
r.people_hash
r.person
r.pings
r.player
r.players
r.plugin_failures
r.plugin_result
r.plugins
r.practice
r.ranked
r.raw_data
r.real_length
r.real_type
r.recorder
r.region
r.register_datapack
r.register_default_datapacks
r.register_default_readers
r.register_reader
r.registered_datapacks
r.registered_readers
r.release_string
r.resume_from_replay
r.resume_method
r.resume_user_info
r.speed
r.start_time
r.team
r.teams
r.time_zone
r.tracker_events
r.type
r.unit
r.units
r.unix_timestamp
r.versions
r.windows_timestamp
r.winner

