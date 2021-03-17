from os import listdir
from os.path import isfile, join, exists

import re

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
start=datetime.now()

pd.options.display.float_format = '{:0.3f}'.format
np.set_printoptions(precision=2)

missing_scores_files = ['../../Data/04/T4/R4',
                      '../../Data/37/T5/R4',
                      '../../Data/42/T3/R3',
                      '../../Data/46/T4/R2', '../../Data/46/T4/R3', '../../Data/46/T4/R4']


def find_file_name(dir, file_start='scores'):
    files_starts_with = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f)) and f.startswith( file_start )]

    if len(files_starts_with) == 0:
        print('*** {0} does NOT have a file starting with {1}'.format(dir, file_start))
        return False
    elif len(files_starts_with) > 1:
        print('*** {0} has {1} files starting with {2}'.format(dir, len(files_starts_with), file_start))
        return False
    else:
        # returnt he only file starts with X
        return files_starts_with[0]


def is_data_available(data_path):

    if data_path in missing_scores_files:
        return False

    if not exists(data_path):
        print('***  {0} - does not exist!!!'.format(data_path))
        False


    scores_file_name  = find_file_name(data_path, 'scores')

    return scores_file_name


# def Min_Max_Normalization(df):
#     # https: // en.wikipedia.org / wiki / Feature_scaling
#     # When normalizing the data, the Min_Max_Normalization() returns Nan if the user answers the question the same in
#     # all the rounds and tasks. That is because the function divides by  df.max() - df.min(), which is zero
#     if df.max() == df.min():
#         return (df - 0.0)/(1.0 - 0.0)
#     return (df - df.min())/(df.max() - df.min())


possible_folders = ['BASELINE','T1/R1',
                    'T2/R1', 'T2/R2', 'T2/R3', 'T2/R4', 'T2',
                    'T3/R1', 'T3/R2', 'T3/R3', 'T3/R4', 'T3',
                    'T4/R1', 'T4/R2', 'T4/R3', 'T4/R4', 'T4',
                    'T5/R1', 'T5/R2', 'T5/R3', 'T5/R4', 'T5']




#Initialize the final performance DataFrame to NaN Values
index_lists = [ [i for i in range(1,64)], possible_folders]
performance_df_indexes = pd.MultiIndex.from_product(index_lists, names=['User', 'Round'])
performance_df_columns = ['React_Time', #'Norm_React_Time',
                             'Move_Time', #'Norm_Move_Time',
                             'Score'#, 'Norm_Score'
                          ]
nan_array = np.empty((len(performance_df_indexes), len(performance_df_columns)))
nan_array[:] = np.nan

performance_df = pd.DataFrame(nan_array, index=performance_df_indexes, columns=performance_df_columns)

# Process the R1/T1 data here
for user_id in range(1, 64):

    _folder = 'T1/R1'
    data_path = '../../Data/{0:02d}/{1}'.format(user_id, _folder)
    if not is_data_available(data_path):
        continue

    scores_file_name = find_file_name(data_path, 'scores')

    scores_data = pd.read_csv(scores_file_name)

    reaction_time = np.array(scores_data['EndTime'][0::2].to_numpy() - scores_data['StartTime'][0::2].to_numpy())

    move_time = np.array(scores_data['EndTime'][1::2].to_numpy() - scores_data['StartTime'][1::2].to_numpy())
    # if both move_out and move-in are correct, then count as correct (1) else count as incorrect (0)
    move_correctness = np.array( ( scores_data['Score'][1::2].to_numpy() +
                                   scores_data['Score'][0::2].to_numpy()   )  /  2  ).astype(int)
    correct_moves_index = np.where(move_correctness == 1)[0]

    performance_df.at[(user_id, _folder), ['React_Time']] = np.mean(reaction_time[correct_moves_index])

    performance_df.at[(user_id, _folder),['Move_Time']] = np.mean(move_time[correct_moves_index])
    # I found the the shortest avg. Move_time in T1/R1 is 0.65 seconds.

    # Because the mistakes were only due to design issues, not user error, all participant receive full score in T1
    performance_df.at[(user_id, _folder), ['Score']] = 1


count_unreliable_moves = 0
count_unreliable_rounds = 0
count_ignored_moves = 0
count_ignored_rounds = 0

# Process T2, T3, T4 and T5 data and rounds here
for user_id in range(1, 64):
    for _task in ['T2', 'T3', 'T4', 'T5']:
        _task_folders = []
        for _round in ['/R1', '/R2', '/R3', '/R4']:
            _folder = _task + _round

            data_path = '../../Data/{0:02d}/{1}'.format(user_id, _folder)
            if not is_data_available(data_path):
                continue

            print(data_path)

            _task_folders.append(_folder)

            scores_file_name = find_file_name(data_path, 'scores')

            scores_data = pd.read_csv(scores_file_name)

            reaction_time = np.array(scores_data['EndTime'][0::2].to_numpy() - scores_data['StartTime'][0::2].to_numpy())

            move_time = np.array(scores_data['EndTime'][1::2].to_numpy() - scores_data['StartTime'][1::2].to_numpy())
            # if both move_out and move-in are correct, then count as correct (1) else count as incorrect (0)
            move_correctness = np.array((scores_data['Score'][1::2].to_numpy() +
                                         scores_data['Score'][0::2].to_numpy()) / 2).astype(int)
            correct_moves_index = np.where(move_correctness == 1)[0]

            # if move_time is at least  50% of the average move time in task 1, then consider it reliable.
            move_reliability_index = np.where(move_time >= 0.50 * performance_df.loc[user_id]['Move_Time']['T1/R1'])[0]
            if len(move_reliability_index) < 9:
                count_unreliable_moves += 9 - len(move_reliability_index)
                count_unreliable_rounds += 1

            # If the moves are correct or I found them reliable, then I consider them in my calculations
            moves_to_consider_index = np.unique(np.append(correct_moves_index, move_reliability_index))
            if len(moves_to_consider_index) < 9:
                count_ignored_moves += 9 - len(moves_to_consider_index)
                count_ignored_rounds += 1

            # In T2, T3, T4, and T5:
            #     I found 96 unreliable moves (in 89 rounds)
            #     I ignored 94 unreliable moves (in 88 rounds)

            performance_df.at[(user_id, _folder), ['Move_Time']] = np.mean(move_time[moves_to_consider_index])
            performance_df.at[(user_id, _folder), ['React_Time']] = np.mean(reaction_time[moves_to_consider_index])
            if _task == 'T4':
                rules_n  = scores_data['RuleCount'].max()
                tmp_score = (np.sum(move_correctness[moves_to_consider_index]) + rules_n) / len(moves_to_consider_index)
                if tmp_score > 1:
                    tmp_score = 1.0
                performance_df.at[(user_id, _folder), ['Score']] = tmp_score
            else:
                tmp_score = np.sum( move_correctness[moves_to_consider_index])/ len(moves_to_consider_index)
                performance_df.at[(user_id, _folder), ['Score']] = tmp_score
            print('Score: {:.2f}\n'.format(tmp_score) )
        # Average the rounds values  of a task
        performance_df.at[(user_id, _task), ['React_Time']] = performance_df.loc[user_id]['React_Time'][_task_folders].mean()
        performance_df.at[(user_id, _task), ['Move_Time']] =  performance_df.loc[user_id]['Move_Time'][_task_folders].mean()
        performance_df.at[(user_id, _task), ['Score']] =      performance_df.loc[user_id]['Score'][_task_folders].mean()


print('In T2, T3, T4, and T5:')
print('\tI found {} unreliable moves (in {} rounds)'.format(count_unreliable_moves, count_unreliable_rounds))
print('\tI ignored {} unreliable moves (in {} rounds)'.format(count_ignored_moves, count_ignored_rounds))

# #Normalize the data
# for user_id in range(1,64):
#     # Normalized Reaction Time
#     performance_df.loc[user_id]['Norm_React_Time'] = Min_Max_Normalization(performance_df.loc[user_id]['React_Time'])
#
#     # Normalized Move_Time Time
#     performance_df.loc[user_id]['Norm_Move_Time'] = Min_Max_Normalization(performance_df.loc[user_id]['Move_Time'])
#
#     # Normalized Score
#     performance_df.loc[user_id]['Norm_Score'] = Min_Max_Normalization(performance_df.loc[user_id]['Score'])



x = input('\n\nEnter y if you want to save the Performance DataFrame to a pickle/excel: ')

if 'y' in x:
    performance_df.to_excel('Performance_Data.xlsx')
    performance_df.to_pickle('Performance_Data.pkl')

print('\033[1;32m\n\nCode finished execution! in {}\n\n \033[0m'.format(datetime.now()-start))