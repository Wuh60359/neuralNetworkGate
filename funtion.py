neuralNetworkGate(input_layer=2,hidden_layer1=2,hidden_layer2=2,output_layer=1,input_x = orGate()[0],
                  target_y = orGate()[1],epochs =10000,learning_rate = 0.01)

neuralNetworkGate(input_layer=2,hidden_layer1=2,hidden_layer2=2,output_layer=1,input_x = andGate()[0],
                  target_y = andGate()[1],epochs =10000,learning_rate = 0.01)

neuralNetworkGate(input_layer=2,hidden_layer1=2,hidden_layer2=2,output_layer=1,input_x = nandGate()[0],
                  target_y = nandGate()[1],epochs =100000,learning_rate = 0.01)

neuralNetworkGate(input_layer=2,hidden_layer1=2,hidden_layer2=2,output_layer=1,input_x = xorGate()[0],
                  target_y = xorGate()[1],epochs =100000,learning_rate = 0.01)

neuralNetworkGate(input_layer=2,hidden_layer1=2,hidden_layer2=2,output_layer=1,input_x = norGate()[0],
                  target_y = norGate()[1],epochs =10000,learning_rate = 0.01) 