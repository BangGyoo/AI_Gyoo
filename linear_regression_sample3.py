import tensorflow as tf

x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(tf.random_normal([1]),name='weight')
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

hypothesis = X * W

cost = tf.reduce_sum(tf.square(hypothesis - Y))

learning_rate = 0.1
gradient = tf.reduce_mean((W*X-Y) * X)
escent = W - learning_rate * gradient
update = W.assign(descent)
#optimizer = tf.train.GradientDescentOptimizer(learning_Rate=0.1)
#train = optimizer.minimize(cost) 랑 똑같다. 미분을 위한 공식 minimize는 해당 경사로 이동한다는 소리

sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())
for step in range(21) :
    sess.run(update, feed_dict={X: x_data, Y: y_data})
    print(step, sess.run(cost,feed_dict={X: x_data, Y: y_data}), sess.run(W))
