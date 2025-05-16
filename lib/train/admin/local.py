class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/content/drive/MyDrive/ProgettoDL/UnTrack/pretrained_networks'
        self.got10k_val_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/got10k/val'
        self.lasot_lmdb_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/got10k_lmdb'
        self.trackingnet_lmdb_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/trackingnet_lmdb'
        self.coco_lmdb_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/coco_lmdb'
        self.coco_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/coco'
        self.lasot_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasot'
        self.got10k_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/got10k/train'
        self.trackingnet_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/trackingnet'
        self.depthtrack_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/depthtrack/train'
        self.lasher_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/lasher/trainingset'
        self.visevent_dir = '/content/drive/MyDrive/ProgettoDL/UnTrack/data/visevent/train'
