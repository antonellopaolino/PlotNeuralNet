import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    # input image
    to_InputLayer( "image", 92, 256, 256, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=4, caption="Input"),
    to_ConvRelu( "conv1", 306, 63, 63, offset="(4.5,0,0)", to="(image-east)", height=32, depth=32, width=8, caption="Conv1-Relu"),
    to_MaxPool( "pool1", 306, 15, 15, offset="(2.5,0,0)", to="(conv1-east)", height=16, depth=16, width=8, caption="MaxPool1"),
    to_ConvRelu( "conv2", 613, 15, 15, offset="(1.5,0,0)", to="(pool1-east)", height=8, depth=8, width=12, caption="Conv2-Relu" ),
    to_MaxPool( "pool2", 613, 7, 7, offset="(1,0,0)", to="(conv2-east)", height=4, depth=4, width=12, caption="MaxPool2-Relu" ),
    to_ConvRelu( "conv3", 920, 3, 3, offset="(1,0,0)", to="(pool2-east)", height=2, depth=2, width=16, caption="Conv3-Relu" ),
    to_Linear( "fc1", 2760, offset="(1,0,0)", to="(conv3-east)", height=32, width=1, caption="Lin1-Relu" ),
    to_Latent( "ls", 3, offset="(1.5,0,0)", to="(fc1-east)", height=3, width=1, caption="Latent Space" ),
    to_Linear( "fc2", 920, offset="(1.5,0,0)", to="(ls-east)", height=11, width=1, caption="Lin2-Relu" ),
    to_Linear( "fc3", 8280, offset="(1,0,0)", to="(fc2-east)", height=48, width=1, caption="Lin2-Relu" ),
    to_ConvRelu( "convtran1", 613, 7, 7, offset="(1,0,0)", to="(fc3-east)", height=4, depth=4, width=12, caption="ConvTrans1-Relu" ),
    to_UpSample( "upsample1", 613, 15, 15, offset="(1,0,0)", to="(convtran1-east)", height=8, depth=8, width=12, caption="Upsample1" ),
    to_ConvRelu( "convtran2", 306, 31, 31, offset="(1.5,0,0)", to="(upsample1-east)", height=16, depth=16, width=8, caption="ConvTrans2-Relu" ),
    to_UnPool( "upsample2", offset="(2.5,0,0)", to="(convtran2-east)", height=32, depth=32, width=8, opacity=0.5, caption="Upsample2" ),
    to_Conv( "convtran3", 92, 256, 256, offset="(4.5,0,0)", to="(upsample2-east)", height=64, depth=64, width=4, caption="ConvTrans3" ),
    to_connection( "image", "conv1" ),
    to_connection( "conv1", "pool1" ),
    to_connection( "pool1", "conv2" ),
    to_connection( "conv2", "pool2" ),
    to_connection( "pool2", "conv3" ),
    to_connection( "conv3", "fc1" ),
    to_connection( "fc1", "ls" ),
    to_connection( "ls", "fc2" ),
    to_connection( "fc2", "fc3" ),
    to_connection( "fc3", "convtran1" ),
    to_connection( "convtran1", "upsample1" ),
    to_connection( "upsample1", "convtran2" ),
    to_connection( "convtran2", "upsample2" ),
    to_connection( "upsample2", "convtran3" ),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()