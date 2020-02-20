import sc2reader

replay = sc2reader.load_replay('EE_LE.SC2Replay')

replay_file_hash = replay.filehash


match_date = replay.date
map_name = replay.map_name
winner = replay.winner
players = replay.players



game_type = replay.type # '1v1'
region = replay.region # 'us'
