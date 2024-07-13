import pygame
from pygame import mixer
from openpyxl import load_workbook

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Load the workbook
workbook = load_workbook(filename='test.xlsx')

# Select the active worksheet (assuming 'playlist' is the active sheet)
worksheet_name = 'playlist1'
#worksheet_name = 'playlist2'
worksheet = workbook[worksheet_name]

# Alternatively, select a specific worksheet by name
# worksheet = workbook['playlist']

# Iterate over all cells in column A and load/play their values
max_row = worksheet.max_row
column_a_values = []

# Collect all values in column A
for row in range(1, max_row + 1):
    cell_value = worksheet[f'A{row}'].value
    if cell_value is not None:
        column_a_values.append(cell_value)

# Function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.time.wait(2000)  # 3 seconds (3000 milliseconds)

# Play each music file sequentially
for file_path in column_a_values:
    play_music(file_path)
    # Wait until music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

# Wait a bit before quitting
pygame.time.wait(3000)  # 3 seconds (3000 milliseconds)
pygame.quit()

