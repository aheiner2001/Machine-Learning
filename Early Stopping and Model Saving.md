
Here's the code I showed in class about how to save the best model to your Google Drive and include an early stopping rule:  

### Open a connection and allow access to your Google drive

# Create Model Saving point:

from google.colab import drive
drive.mount('/content/drive') # this will open a window to log in to your Google drive

import os

# Create a folder for your models if it doesn't exist
save_dir = '/content/drive/MyDrive/keras_models/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Update the filepath in your callback
checkpoint_path = save_dir + 'best_model.keras'
#### Load the Model Checkpoint and early stopping from keras
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
# Create the parameters for the checkpoint callback, including how to define the "best" model so far
checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_path,  # Created above
    monitor='val_loss', # use validation loss as the parameter to determine which model to save as the model fits through the epochs
    save_best_only=True,
    verbose=1
)
# Create an early stopping object
early_stopping_callback = EarlyStopping(
    monitor='val_loss',
    patience=15,               # Number of epochs to wait before stopping
    restore_best_weights=True, # Returns model to its best state at the end
    verbose=1
)
### After building your sequential model and are ready to fit:
history = model.fit(X_train, y_train, epochs=200, validation_split=.35, batch_size=100, callbacks=[early_stopping_callback, checkpoint_callback],shuffle=False)
########################
### Loading a saved model ###
########################
# To get predictions from a saved model:  
from google.colab import drive
from tensorflow.keras.models import load_model

# 1. Mount the drive
drive.mount('/content/drive')

# 2. Define the exact path where you saved it
model_path = '/content/drive/MyDrive/keras_models/best_model.keras'

# 3. Load the model
model = load_model(model_path)

model.summary()

predictions = model.predict(X_holdout)
#### To continue training a saved model:
model_path = '/content/drive/MyDrive/keras_models/best_model.keras'
model = load_model(model_path)
model.fit(X_train, y_train, epochs=20, validation_split=.35, batch_size=50, callbacks=[early_stopping_callback, checkpoint_callback])
