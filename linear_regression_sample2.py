import matplotlib.pyplot as plt
import tensorflow as tf

X = [1,2,3]    # X,Y 정의
Y = [1,2,3]

W = tf.compat.v1.placeholder(tf.float32)   # 최초 tf.placeholder를 사용했지만 최신버전 보안에 의해 compat.v1.을 추가 해주었다.

hypothesis = X * W

cost = tf.reduce_mean(tf.square(hypothesis - Y))

sess = tf.compat.v1.Session()

sess.run(tf.compat.v1.global_variables_initializer())

W_val = []
cost_val = []

for i in range(-30, 50) :
    feed_W = i * 0.1
    curr_cost, curr_W = sess.run([cost,W], feed_dict={W: feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost)

plt.plot(W_val, cost_val)
plt.show()
