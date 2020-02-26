import os
if os.name == 'nt':
    SAVE_LOCATION = os.path.join(os.getcwd(), 'saves\\algo')
else:
    SAVE_LOCATION = os.path.join(os.getcwd(), 'saves/algo')

