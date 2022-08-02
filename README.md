# Github Repo for Neurips 2022, paper id 2509
## before running, please unzip the files in the 'Preposs' directory first

python Twitter.py --lr 5e-4 --penalty_coefficient 0.05 --Numofwalkers 10\
python IMBD.py --lr 0.002 --Numofwalkers 1 --penalty_coefficient 0.2\
python COLLAB.py --lr 0.002 --penalty_coefficient 0.1 --Numofwalkers 3\



To generate hardness dataset: run gen_hardness_cases.py\
To run local search:\
python LocalSearchCOLLAB.py\
python LocalSearchIMBD.py\
python LocalSearchTwitter.py
