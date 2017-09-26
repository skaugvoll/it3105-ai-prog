import tensorflow as tf
import numpy as np

##############
# Variables
##############

x = tf.Variable(37, name="x")
y = tf.Variable(np.array([1,2],[3,4]), name="2x2 Array")


##############
# Operators
##############

def operatorsOne(a, b): # a and b are not TensoFlow variables.
    '''
    TensoFlow compiles the entire expression in a function graph taht connects
    inputs (a,b) to outputs(z)
    '''
    x = tf.constant(a) # Scalar constant variables
    y = tf.constant(b)
    z = x * y # z becomes a multiplication operator  (z is an object now.) THIS DO NOT DO A MULTIPLICATON, IT SETS IT UP. WILL NOT BE EXECUTED BEFORE SESSION IS RUN

    sess = tf.Session() # open a new session
    result = sess.run(z) # runs an session with / on the operator z.
    sess.close() # close session to release memory
    return result


##############
# Routine
##############


def quickrun(operators):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    result = sess.run(operators)
    sess.close()
    TFT.showvars(result)

def showvars(result):
    pass


##############
# Function Graph
##############

import os

def viewprep(session, dir="probeview", flush=120, queue=10):
    return tf.summary.FileWriter(dir, session.graph, flush_secs=flush, max_queue=queue)

def fireup_tensorboard(logdir):
    os.system('tensorboard --logidir='+logdir)
