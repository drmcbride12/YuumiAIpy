class GameState:
    def __init__(self):
        # Initialize the game state with default values
        self.player_position = None
        self.player_health = None
        self.enemy_positions = []
        self.enemy_healths = []
        # ... add more game state attributes as needed ...

    def update(self, game_info):
        # Update the game state based on the provided game info
        self.player_position = game_info.get('player_position')
        self.player_health = game_info.get('player_health')
        self.enemy_positions = game_info.get('enemy_positions')
        self.enemy_healths = game_info.get('enemy_healths')
        # ... update more game state attributes as needed ...
