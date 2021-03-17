# 9PM - Code and Dataset for Behavioral, Performance, and Physiological Data
This repository includes a dataset for Behavioral, Performance, and Physiological Data of 63 participants performing modified versions of standard physical and cognitive assessments, in addition to the code that was use to record and analyze the data.


##Physical & Cognitive Assessments
###Physical Assessment
- 9-Hole Peg Test (9-HPT)

###Congitive Assessment Assessment
- Stroop Test
- Wisconsin Card Sorting Test (WCST) 
- The NIH Toolbox Picture Sequence Memory Test (PSMT)

##Behavioral, Performance & Phsyiological Data 
###Behavioral
* IMU Data
* Videos (Not included for participants privacy), but I can include facial markers if anyone is interested in them. Contact me at firstname.lastname@tamu.edu if you are interested.
* Users Questionnaires about:
	1. Mental Effort
	2. Physical Effort
	3. Sleepy/Drowsy
	4. Difficulty Concetrating
	5. Task Difficulty
	6. Task Enjoyment
	7. Task Interesting
	8. Feeling Physically Tired
	9. Feeling Distressed
	10. Feeling Attentive
	
###Performance
1. Task Score
2. Move time
3. Reaction Time

###Phsyiological Data
1. ECG
2. EEG
3. EDA


##Data Folder
The data folder has the "Raw Data.zip" file, "Extracted Features" folder, and "Random Sequences" folder. The zip file has the raw data that was recording during the experiment. The "Extracted Features" folder has ECG, EDA, EEG, IMU, Performance, and Survey features. The "Random Sequences" folder has details on which peg should be picked up anf where it should be placed. 

After you extract "Raw Data.zip",  you can find the raw data has the following structure:

```python
import shutil
filename = "path/to/Data/Raw\ Data.zip"
shutil.unpack_archive(filename, 'path/to/Extracted_folder')
```
```
Subject_ID
├── BASELINE
│   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   └── Plux[ECG_EDA_Data]-Date__Time.csv
├── T1
│   └── R1
│       ├── Logs.txt
│       ├── Mbient-D1[IMU_Data]-Date__Time.csv
│       ├── OpenBCI[EEG_Data]-Date__Time.csv
│       ├── Plux[ECG_EDA_Data]-Date__Time.csv
│       └── scores-T[Task_ID]-Blue[Blue=RightHanded, Red=LeftHanded].csv
├── T2
│   ├── R1
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R2
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R3
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   └── R4
│       ├── Logs.txt
│       ├── Mbient-D1[IMU_Data]-Date__Time.csv
│       ├── OpenBCI[EEG_Data]-Date__Time.csv
│       ├── Plux[ECG_EDA_Data]-Date__Time.csv
│       └── scores-T[TaskID]-[Random_Sequence_ID].csv
├── T3
│   ├── R1
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R2
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R3
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   └── R4
│       ├── Logs.txt
│       ├── Mbient-D1[IMU_Data]-Date__Time.csv
│       ├── OpenBCI[EEG_Data]-Date__Time.csv
│       ├── Plux[ECG_EDA_Data]-Date__Time.csv
│       └── scores-T[TaskID]-[Random_Sequence_ID].csv
├── T4
│   ├── R1
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R2
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   ├── R3
│   │   ├── Logs.txt
│   │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
│   │   ├── OpenBCI[EEG_Data]-Date__Time.csv
│   │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
│   │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
│   └── R4
│       ├── Logs.txt
│       ├── Mbient-D1[IMU_Data]-Date__Time.csv
│       ├── OpenBCI[EEG_Data]-Date__Time.csv
│       ├── Plux[ECG_EDA_Data]-Date__Time.csv
│       └── scores-T[TaskID]-[Random_Sequence_ID].csv
└── T5
    ├── R1
    │   ├── Logs.txt
    │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
    │   ├── OpenBCI[EEG_Data]-Date__Time.csv
    │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
    │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
    ├── R2
    │   ├── Logs.txt
    │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
    │   ├── OpenBCI[EEG_Data]-Date__Time.csv
    │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
    │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
    ├── R3
    │   ├── Logs.txt
    │   ├── Mbient-D1[IMU_Data]-Date__Time.csv
    │   ├── OpenBCI[EEG_Data]-Date__Time.csv
    │   ├── Plux[ECG_EDA_Data]-Date__Time.csv
    │   └── scores-T[TaskID]-[Random_Sequence_ID].csv
    └── R4
       ├── Logs.txt
       ├── Mbient-D1[IMU_Data]-Date__Time.csv
       ├── OpenBCI[EEG_Data]-Date__Time.csv
       ├── Plux[ECG_EDA_Data]-Date__Time.csv
       └── scores-T[TaskID]-[Random_Sequence_ID].csv
```

##Citations
If you use any part of this dataset or code, please cite the following references.


```
@phdthesis{abujelala2019think2act,
	title={THINK2ACT: USING MULTIMODAL DATA TO ASSESS HUMAN COGNITIVE AND PHYSICAL PERFORMANCE},
	author={Abujelala, Maher and others},
    year={2019}
 }
 
@inproceedings{abujelala2021_9PM,
  title={9PM: A Novel Interactive 9-Peg Board for Cognitive and Physical Assessment},
  author={Abujelala, Maher and Kanal, Varun and Rajavenkatanarayanan, Akilesh and Makedon, Fillia},
  booktitle={Proceedings of the 14th ACM International Conference on PErvasive Technologies Related to Assistive environments},
  year={2021}
}
```
### Papers used the Dataset
The following publications are by my collabrators Dr. Varun Kanal and Dr. Akilesh Rajavenkatanarayanan have used the dataset. Please check out their publications for more ideas on how utilize the dataset.

```
#TO Do
```


##TODO:
1. Add the Code Folder
	- Data Recording Code
	- Data Analysis Code
	- ML Code
2. 	Add a readme files about extracted features with code
3. Provide more details on how "Random Sequences" were used, and what its data means and which of it was ignored (i.e. the pegs order).
4. Update this TODO list with more items :)


##Contact me:
For any questions, please feel free to contact me at firsrname.lastname@tamu.edu. 