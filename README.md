# YuumiAIpy
- Yuumi_AI
    - src
        - data_processing
            - __init__.py
            - data_collector.py
            - data_preprocessor.py
        - model
            - __init__.py
            - model_builder.py
            - model_trainer.py
        - game_interaction
            - __init__.py
            - game_connector.py
            - game_controller.py
    - tests
        - __init__.py
        - test_data_processing.py
        - test_model.py
        - test_game_interaction.py
    - README.md
    - requirements.txt
Here is an overview of what each file is intended to do:

data_collector.py: This file will contain functions to collect data from the game. You can use the Riot Games API to collect match data.
data_preprocessor.py: This script will take the raw data from the data_collector.py and transform it into a format that can be used to train your AI model.
model_builder.py: In this file, you'll define the architecture of your AI model.
model_trainer.py: This file will use the preprocessed data to train your AI model.
game_connector.py: This file will contain functions to connect your AI to the game.
game_controller.py: This file will use the predictions from your AI model to control Yuumi in the game.
test_*.py: These files will contain tests for the corresponding modules.
For the requirements.txt, list all the libraries that your project will depend on. Here is a basic example:
