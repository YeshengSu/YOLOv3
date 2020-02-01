import os
import yaml

class Config(dict):
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self._yaml = f.read()
            self._dict = yaml.load(self._yaml)
            self._dict['PATH'] = os.path.dirname(config_path)

    def __getattr__(self, name):
        if self._dict.get(name) is not None:
            return self._dict[name]

        if DEFAULT_CONFIG.get(name) is not None:
            return DEFAULT_CONFIG[name]

        return None

    def print(self):
        print('Model configurations:')
        print('---------------------------------')
        print(self._yaml)
        print('')
        print('---------------------------------')
        print('')


DEFAULT_CONFIG = {
    'BATCH_SIZE'  : 8,
    'N_CPU'       : 8,
    'IMAGE_SIZW'  : 416,

    'MODEL_DEF'   : 'config/yolov3.cfg',
    'DATA_CONFIG' : 'config/coco.data',
    'WEIGHTS_PATH': 'weights/yolov3.weights',
    'CLASS_PATH'  : 'data/coco.names',
    'IOU_THRES'   : 0.5,
    'CONF_THRES'  : 0.001,
    'NMS_THRES'   : 0.5,
}
