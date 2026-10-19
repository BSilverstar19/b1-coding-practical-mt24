def controller(reference, observation, previous_error):
    K_P = 0.15
    K_D =  0.6
    error = reference - observation

    action = K_P * error + K_D * (error - previous_error)

    return action