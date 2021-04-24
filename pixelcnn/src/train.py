import tensorflow as tf
from .data import get_data
from .model import SimplePixelCnn

def train_model():
    check_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath="checkpoints/check.ckpt",
        save_weights_only=True,
        verbose=1
    )

    pixel_cnn = SimplePixelCnn(
        hidden_features=64,
        output_features=64,
        resblock_num=7
    )

    pixel_cnn.compile(
        loss=tf.keras.losses.BinaryCrossentropy(),
        optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
        metrics=[tf.keras.losses.BinaryCrossentropy()]
    )

    ds_train, ds_test = get_data()

    pixel_cnn.fit(ds_train, epochs=50, validation_data=ds_test, callbacks=[check_callback])
    pixel_cnn.save('model/pixel_cnn')

    return pixel_cnn