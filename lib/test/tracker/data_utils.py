import torch
import numpy as np

class Preprocessor(object):
    def __init__(self):
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1)).cuda()
        self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1)).cuda()
        #self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1)) #removed cuda()
        #self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1)) #removed cuda()

    def process(self, img_arr: np.ndarray):
        # Deal with the image patch
        img_tensor = torch.tensor(img_arr).cuda().float().permute((2,0,1)).unsqueeze(dim=0)
        #img_tensor = torch.tensor(img_arr).float().permute((2,0,1)).unsqueeze(dim=0) #removed cuda()
        img_tensor_norm = ((img_tensor / 255.0) - self.mean) / self.std  # (1,3,H,W)
        return img_tensor_norm

class PreprocessorMM(object):
    def __init__(self):
        self.mean = torch.tensor([0.485, 0.456, 0.406, 0.485, 0.456, 0.406]).view((1, 6, 1, 1)).cuda()
        self.std = torch.tensor([0.229, 0.224, 0.225, 0.229, 0.224, 0.225]).view((1, 6, 1, 1)).cuda()

        #self.mean = torch.tensor([0.485, 0.456, 0.406, 0.485, 0.456, 0.406]).view((1, 6, 1, 1)) #removed cuda()
        #self.std = torch.tensor([0.229, 0.224, 0.225, 0.229, 0.224, 0.225]).view((1, 6, 1, 1)) #removed cuda()



        #self.mean = torch.tensor([0.485, 0.456, 0.406, 0.485, 0.456, 0.406, 0.485, 0.456, 0.406]).view((1, 9, 1, 1)).cuda()
        #self.std = torch.tensor([0.229, 0.224, 0.225, 0.229, 0.224, 0.225, 0.229, 0.224, 0.225]).view((1, 9, 1, 1)).cuda()


    def process(self, img_arr: np.ndarray):
        # Deal with the image patch

        img_tensor = torch.tensor(img_arr).cuda().float().permute((2,0,1)).unsqueeze(dim=0)
        #img_tensor = torch.tensor(img_arr).float().permute((2,0,1)).unsqueeze(dim=0) #removed cuda()
        temp = img_tensor[:, :-1, ...]
        sem = img_tensor[:, -1:, ...]
        temp_norm = ((temp / 255.0) - self.mean) / self.std  # (1,6,H,W)
        img_tensor_norm = torch.cat((temp_norm, sem), dim=1)
        #img_tensor_norm = ((img_tensor / 255.0) - self.mean) / self.std  # (1,6,H,W)

        return img_tensor_norm


class PreprocessorX(object):
    def __init__(self):
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1)).cuda()
        self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1)).cuda()
        #self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1)) #removed cuda()
        #self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1)) #removed cuda()

    def process(self, img_arr: np.ndarray, amask_arr: np.ndarray):
        # Deal with the image patch
        img_tensor = torch.tensor(img_arr).cuda().float().permute((2,0,1)).unsqueeze(dim=0)
        #img_tensor = torch.tensor(img_arr).float().permute((2,0,1)).unsqueeze(dim=0) #removed cuda()
        img_tensor_norm = ((img_tensor / 255.0) - self.mean) / self.std  # (1,3,H,W)
        # Deal with the attention mask
        amask_tensor = torch.from_numpy(amask_arr).to(torch.bool).cuda().unsqueeze(dim=0)  # (1,H,W)
        #amask_tensor = torch.from_numpy(amask_arr).to(torch.bool).unsqueeze(dim=0) #removed cuda()
        return img_tensor_norm, amask_tensor


class PreprocessorX_onnx(object):
    def __init__(self):
        self.mean = np.array([0.485, 0.456, 0.406]).reshape((1, 3, 1, 1))
        self.std = np.array([0.229, 0.224, 0.225]).reshape((1, 3, 1, 1))

    def process(self, img_arr: np.ndarray, amask_arr: np.ndarray):
        """img_arr: (H,W,3), amask_arr: (H,W)"""
        # Deal with the image patch
        img_arr_4d = img_arr[np.newaxis, :, :, :].transpose(0, 3, 1, 2)
        img_arr_4d = (img_arr_4d / 255.0 - self.mean) / self.std  # (1, 3, H, W)
        # Deal with the attention mask
        amask_arr_3d = amask_arr[np.newaxis, :, :]  # (1,H,W)
        return img_arr_4d.astype(np.float32), amask_arr_3d.astype(np.bool)
