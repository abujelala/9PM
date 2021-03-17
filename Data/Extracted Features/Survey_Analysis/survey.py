import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np


decode_survey = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
                 'Less than Usual': 1, 'No More than Usual': 2, 'More than Usual': 3, 'Much More than Usual': 4,
                 'Very Slightly or Not at All': 1, 'A Little': 2, 'Moderately': 3, 'Quite a Bit': 4, 'Extremely': 5}

task_round_labels = [ 'BASELINE', 'T1/R1',
                        'T2/R1', 'T2/R2', 'T2/R3', 'T2/R4', 'T2',
                        'T3/R1', 'T3/R2', 'T3/R3', 'T3/R4', 'T3',
                        'T4/R1', 'T4/R2', 'T4/R3', 'T4/R4', 'T4',
                        'T5/R1', 'T5/R2', 'T5/R3', 'T5/R4', 'T5']

# Initialize the final Survey DataFrame to NaN Values
index_lists = [ range(1,64), task_round_labels]
survey_ft_df_indexes = pd.MultiIndex.from_product(index_lists, names=['User', 'Round'])
survey_ft_df_columns = ['Mental_Effort', 'Physical_Effort', 'Sleepy_Drowsy', 'Difficulty_Concentrating',
                        'Task_Difficulty', 'Task_Enjoyment', 'Task_Interesting', 'Feeling_Physically_Tired',
                        'Feeling_Distressed', 'Feeling_Attentive']

nan_array = np.empty((63 * len(task_round_labels), len(survey_ft_df_columns)))
nan_array[:] = np.nan
survey_ft_df = pd.DataFrame(nan_array, index=survey_ft_df_indexes, columns=survey_ft_df_columns)


# Read the Baseline and Task 1 Survey and update the Survey DataFrame
baseline_T1_file = '../../Data/Survey/Baseline_T1.xlsx'
baseline_T1_df = pd.read_excel(baseline_T1_file, index_col=[1])
baseline_T1_df_columns = baseline_T1_df.columns.values

for user_id in range(1,64):
    # Baseline Questions
    survey_ft_df.at[(user_id, 'BASELINE'), 'Sleepy_Drowsy'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[4]]]

    survey_ft_df.at[(user_id, 'BASELINE'), 'Difficulty_Concentrating'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[5]]]

    survey_ft_df.at[(user_id, 'BASELINE'), 'Feeling_Physically_Tired'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[6]]]

    survey_ft_df.at[(user_id, 'BASELINE'), 'Feeling_Distressed'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[7]]]

    survey_ft_df.at[(user_id, 'BASELINE'), 'Feeling_Attentive'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[8]]]

    # Task 1 Questions
    survey_ft_df.at[(user_id, 'T1/R1'), 'Mental_Effort'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[9]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Physical_Effort'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[10]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Sleepy_Drowsy'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[11]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Difficulty_Concentrating'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[12]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Feeling_Physically_Tired'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[13]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Feeling_Distressed'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[14]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Task_Interesting'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[15]]]

    survey_ft_df.at[(user_id, 'T1/R1'), 'Feeling_Attentive'] = \
        decode_survey[baseline_T1_df.loc[user_id][baseline_T1_df_columns[16]]]


# Read the Post-Task Survey for T2-T5 and update the Survey DataFrame
posttask_T2345_file = '../../Data/Survey/PostTask_T2_T3_T4_T5.xlsx'
posttask_T2345_df = pd.read_excel(posttask_T2345_file)
posttask_T2345_df_columns = posttask_T2345_df.columns.values

for i in range(len(posttask_T2345_df)):
    user_id = posttask_T2345_df.loc[i][posttask_T2345_df_columns[1]]
    actual_task = posttask_T2345_df.loc[i][posttask_T2345_df_columns[2]]

    for round_i in range(1, 5):
        # Mental Effort Question
        survey_ft_df.at[(user_id, 'T{}/R{}'.format(actual_task, round_i)), survey_ft_df_columns[0]] = \
            decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[3 + (round_i - 1)*4 + 0]]]
        # Physical Effort Question
        survey_ft_df.at[(user_id, 'T{}/R{}'.format(actual_task, round_i)), survey_ft_df_columns[1]] = \
            decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[3 + (round_i - 1) * 4 + 1]]]
        # Sleepy/Drowsy Question
        survey_ft_df.at[(user_id, 'T{}/R{}'.format(actual_task, round_i)), survey_ft_df_columns[2]] = \
            decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[3 + (round_i - 1) * 4 + 2]]]
        # Sleepy/Drowsy Question
        survey_ft_df.at[(user_id, 'T{}/R{}'.format(actual_task, round_i)), survey_ft_df_columns[3]] = \
            decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[3 + (round_i - 1) * 4 + 3]]]

    # Feeling_Physically_Tired Question
    survey_ft_df.at[(user_id, 'T{}'.format(actual_task)), survey_ft_df_columns[7]] = \
        decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[19]]]
    # Feeling_Distressed Question
    survey_ft_df.at[(user_id, 'T{}'.format(actual_task)), survey_ft_df_columns[8]] = \
        decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[20]]]
    # Task_Interesting Question
    survey_ft_df.at[(user_id, 'T{}'.format(actual_task)), survey_ft_df_columns[6]] = \
        decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[21]]]
    # Feeling_Attentive Question
    survey_ft_df.at[(user_id, 'T{}'.format(actual_task)), survey_ft_df_columns[9]] = \
        decode_survey[posttask_T2345_df.loc[i][posttask_T2345_df_columns[22]]]


# Read the Final Survey for T1-T5 and the Order of the tasks to update the Survey DataFrame
final_survey_file = '../../Data/Survey/Final.xlsx'
final_survey_df = pd.read_excel(final_survey_file, index_col=[1])
final_survey_df_columns = final_survey_df.columns.values

tasks_order_file = '../../Data/Survey/Tasks_Order.xlsx'
tasks_order_df = pd.read_excel(tasks_order_file, index_col=[0])
tasks_order_df_columns = tasks_order_df.columns.values

_tasks_names = ['T1/R1', 'T2', 'T3', 'T4', 'T5']

for user_id in range(1, 64):

    tasks_order_list = tasks_order_df.loc[user_id].tolist()

    for t in range(len(tasks_order_list)):
        actual_task_name = _tasks_names[tasks_order_list[t] - 1]

        # Task Difficulty Question
        survey_ft_df.at[(user_id, actual_task_name), survey_ft_df_columns[4]] = \
            decode_survey[final_survey_df.loc[user_id][final_survey_df_columns[t+1]]]

        # Task Enjoyment Question
        survey_ft_df.at[(user_id, actual_task_name), survey_ft_df_columns[5]] = \
            decode_survey[final_survey_df.loc[user_id][final_survey_df_columns[t+6]]]


x = input('\n\nEnter y if you want to save the RAW Survey DataFrame to a pickle/excel: ')

if 'y' in x:
    survey_ft_df.to_excel('Raw_Survey_Data.xlsx')
    survey_ft_df.to_pickle('Raw_Survey_Data.pkl')



print('\033[1;32m' + '\n\nCode finished execution!\n\n' + '\033[0m')