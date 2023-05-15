# TensorFlow 라이브러리 import
import tensorflow as tf

# MNIST 데이터셋 다운로드
mnist = tf.keras.datasets.mnist

# 데이터 전처리
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 모델 아키텍처 정의
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# 손실 함수 및 최적화 알고리즘 설정
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# 모델 컴파일
model.compile(optimizer=optimizer, loss=loss_fn, metrics=['accuracy'])

# 모델 훈련
model.fit(x_train, y_train, epochs=5)

# 모델 평가
model.evaluate(x_test, y_test, verbose=2)
 
model.predict(x_test)
