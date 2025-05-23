Here follow more details about this repository.

The project is a copy from the original one [https://github.com/Zongwei97/UnTrack]. 
Major concern, before running the code, is to change the files paths with local ones. 




To run the scripts (train or eval), is necessary to download the models (.pth files) and the video sequences (were omitted in the repository to keep it light) at the following google drive links:
1) pretrained model: [https://drive.google.com/file/d/1TDUQYB59rOvUU8vpeWSrNoow0hNkAkT2/view?usp=sharing], this is the UnTrack model released in the original paper, in this case used as model to be fine-tuned (to fine-tune put the .pth.tar into pretrained/ folder)
2) fine-tuned models: [https://drive.google.com/file/d/14lzUdYufdaDG35z5yY89bmfJwA91z9Qi/view?usp=sharing]. this is the fine-tuned model who gets best results on evaluation (to run eval with this model, put the .pth.tar into models/ folder)
3) training sequences: [https://drive.google.com/drive/folders/1ZpC67V9_0HXyHJG2pEMP0y4ellzfuC_Z?usp=sharing] contains the video sequences for fine-tuning (copy them into data/vots2022rgbd/train/, each sequence is a standalone folder)
4) evaluation sequences: [https://drive.google.com/drive/folders/1t8GeltnyipRTYu3Nm3UCvDC3OtM1ikqS?usp=sharing] contains the video sequences for vot-toolkit evaluation (copy them into vot2022_rgbd_workspace/sequences/)


Note: pretrained model name is left as in original work (OSTrack_ep0300.pth.tar) to avoid parsing errors in the framework, same for fine-tuned model (UnTrack.pth.tar). 

## Run scripts

To run fine-tune training, the main script is **train.sh**, which basically execute the python script as follows:

    python tracking/train.py --script untrack --config final_deep_rgbd_config --save_dir ./output_x --mode single  

Where **train.py** in the entry point for pytorch framework and **--config** refers to the .yaml file being selected from experiments/ folder (this is the file that sets all parameters required for fine-tuning: learning rate, epochs, etc..)

To run the evalutation, the script **eval_rgbd.sh** does the job by calling the vot-toolik utilities: 

    cd vot2022_rgbd_workspace
    vot evalutate --workspace ./ untrack_deep
    vot analysis --nocache --name untrack_deep

This step produces new folders **results/** and **analysis/** into vot2022_rgbd_workspace, and analysis contain the html file with "challenge-format" results.


