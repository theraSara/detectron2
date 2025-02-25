import tensorflow as tf
from tensorflow.keras.models import load_model

model = tf.keras.applications.EfficientNetB0(weights="imagenet", include_top=False)

# adding custom classification layers
x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
x = tf.keras.layers.Dense(128, activation="relu")(x)
x = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
efficientdet_model = tf.keras.Model(inputs=model.input, outputs=x)

efficientdet_model.summary()
