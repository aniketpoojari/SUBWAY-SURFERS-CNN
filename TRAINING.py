import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint


train_datagen = ImageDataGenerator(rescale = 1.0/255.)
test_datagen = ImageDataGenerator(rescale = 1.0/255.)

train_generator = train_datagen.flow_from_directory(
        'DATA/TRAINING',
        batch_size = 2,
        class_mode = 'categorical', 
        target_size = (300, 300)
)     

validation_generator =  test_datagen.flow_from_directory(
      'DATA/TESTING',
      batch_size  = 2,
      class_mode  = 'categorical', 
      target_size = (300, 300)
)

model = tf.keras.models.Sequential([
    # The first convolution
    tf.keras.layers.Conv2D(32, (3,3), padding='same', activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # The second convolution
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    # The third convolution
    tf.keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # The fourth convolution
    tf.keras.layers.Conv2D(256, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # The fifth convolution
    tf.keras.layers.Conv2D(512, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),

    tf.keras.layers.Dense(11, activation='softmax')
    ])

model.compile(loss = 'categorical_crossentropy', optimizer=RMSprop(lr=0.0001), metrics=['accuracy'])

checkpoint = ModelCheckpoint("model.h5", monitor='val_loss', verbose=1,
    save_best_only=True, mode='auto', period=1)

model.fit_generator(
    train_generator,
    validation_data = validation_generator,
    epochs = 7,
    verbose = 1,
    callbacks=[checkpoint]
)

# model.save("model.h5")