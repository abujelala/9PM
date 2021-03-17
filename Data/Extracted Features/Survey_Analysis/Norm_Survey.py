import pandas as pd
import numpy as np
from datetime import datetime
start=datetime.now()

def Min_Max_Normalization(df):
    # https: // en.wikipedia.org / wiki / Feature_scaling
    # When normalizing the data, the Min_Max_Normalization() returns Nan if the user answers the question the same in
    # all the rounds and tasks. That is because the function divides by  df.max() - df.min(), which is zero

    if not np.isnan(df.iloc[0]):
        print('Error: Baseline value should be NaN')

    if df.max() != df.min():
        return (df - df.min()) / (df.max() - df.min())
    else:
        return 0*df

def increased_above_baseline(df):
    if np.isnan(df.iloc[0]):
        print('Error: Baseline value should be NOT NaN')
    baseline = df.iloc[0]

    df2 = df.copy()
    df2.iloc[0] = np.nan

    for i in range(len(df2)):
        if not np.isnan(df2.iloc[i]):
            if df2.iloc[i] > baseline:
                df2.iloc[i] = 1
            else:
                df2.iloc[i] = 0

    return df2



task_round_labels = [ 'BASELINE', 'T1/R1',
                        'T2/R1', 'T2/R2', 'T2/R3', 'T2/R4', 'T2',
                        'T3/R1', 'T3/R2', 'T3/R3', 'T3/R4', 'T3',
                        'T4/R1', 'T4/R2', 'T4/R3', 'T4/R4', 'T4',
                        'T5/R1', 'T5/R2', 'T5/R3', 'T5/R4', 'T5']

_tasks_names = ['T1/R1', 'T2', 'T3', 'T4', 'T5']


index_lists = [ range(1,64), task_round_labels]
norm_survey_ft_df_indexes = pd.MultiIndex.from_product(index_lists, names=['User', 'Round'])
norm_survey_ft_df_columns = ['Mental_Effort', 'Norm_Mental_Effort',
                             'Physical_Effort', 'Norm_Physical_Effort',
                             'Sleepy_Drowsy', 'Norm_Sleepy_Drowsy',
                             'Difficulty_Concentrating', 'Norm_Difficulty_Concentrating',
                             'Task_Difficulty', 'Norm_Task_Difficulty',
                             'Task_Enjoyment', 'Norm_Task_Enjoyment',
                             'Task_Interesting', 'Norm_Task_Interesting',
                             'Feeling_Physically_Tired', 'Norm_Feeling_Physically_Tired',
                             'Feeling_Distressed',   'Norm_Feeling_Distressed',
                             'Feeling_Attentive', 'Norm_Feeling_Attentive']

nan_array = np.empty((63 * len(task_round_labels), len(norm_survey_ft_df_columns)))
nan_array[:] = np.nan
norm_survey_ft_df = pd.DataFrame(nan_array, index=norm_survey_ft_df_indexes, columns=norm_survey_ft_df_columns)


survey_ft_df = pd.read_pickle('Raw_Survey_Data.pkl')


for user_id in range(1,64):
    # Average Mental Effort
    norm_survey_ft_df.loc[user_id]['Mental_Effort'] = survey_ft_df.loc[user_id]['Mental_Effort']
    for _task in ['T2', 'T3', 'T4', 'T5']:
        norm_survey_ft_df.at[(user_id, _task), ['Mental_Effort']] = \
            norm_survey_ft_df.loc[user_id]['Mental_Effort'][[_task+'/R1', _task+'/R2', _task+'/R3', _task+'/R4']].mean()
    # Normalized Mental Effort
    norm_survey_ft_df.loc[user_id]['Norm_Mental_Effort'] = \
        Min_Max_Normalization(norm_survey_ft_df.loc[user_id]['Mental_Effort'])



    # Average Physical Effort
    norm_survey_ft_df.loc[user_id]['Physical_Effort'] = survey_ft_df.loc[user_id]['Physical_Effort']
    for _task in ['T2', 'T3', 'T4', 'T5']:
        norm_survey_ft_df.at[(user_id, _task), ['Physical_Effort']] = \
            norm_survey_ft_df.loc[user_id]['Physical_Effort'][
                [_task + '/R1', _task + '/R2', _task + '/R3', _task + '/R4']].mean()
    # Normalized Physical Effort
    norm_survey_ft_df.loc[user_id]['Norm_Physical_Effort'] = \
        Min_Max_Normalization(norm_survey_ft_df.loc[user_id]['Physical_Effort'])



    # Average Sleepy_Drowsy
    norm_survey_ft_df.loc[user_id]['Sleepy_Drowsy'] = survey_ft_df.loc[user_id]['Sleepy_Drowsy']
    for _task in ['T2', 'T3', 'T4', 'T5']:
        norm_survey_ft_df.at[(user_id, _task), ['Sleepy_Drowsy']] = \
            norm_survey_ft_df.loc[user_id]['Sleepy_Drowsy'][
                [_task + '/R1', _task + '/R2', _task + '/R3', _task + '/R4']].mean()
    # Normalized Sleepy_Drowsy
    norm_survey_ft_df.loc[user_id]['Norm_Sleepy_Drowsy'] = \
        increased_above_baseline(norm_survey_ft_df.loc[user_id]['Sleepy_Drowsy'])



    # Average Difficulty_Concentrating
    norm_survey_ft_df.loc[user_id]['Difficulty_Concentrating'] = survey_ft_df.loc[user_id]['Difficulty_Concentrating']
    for _task in ['T2', 'T3', 'T4', 'T5']:
        norm_survey_ft_df.at[(user_id, _task), ['Difficulty_Concentrating']] = \
            norm_survey_ft_df.loc[user_id]['Difficulty_Concentrating'][
                [_task + '/R1', _task + '/R2', _task + '/R3', _task + '/R4']].mean()
    # Normalized Difficulty_Concentrating
    norm_survey_ft_df.loc[user_id]['Norm_Difficulty_Concentrating'] = \
        increased_above_baseline(norm_survey_ft_df.loc[user_id]['Difficulty_Concentrating'])



    # Average Task_Difficulty
    norm_survey_ft_df.loc[user_id]['Task_Difficulty'] = survey_ft_df.loc[user_id]['Task_Difficulty']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task+_round), ['Task_Difficulty']] = \
    #             norm_survey_ft_df.loc[user_id]['Task_Difficulty'][_task]

    # Normalized Task_Difficulty
    norm_survey_ft_df.loc[user_id]['Norm_Task_Difficulty'] = \
        Min_Max_Normalization(norm_survey_ft_df.loc[user_id]['Task_Difficulty'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Task_Difficulty']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Task_Difficulty'][_task]



    # Average Task_Enjoyment
    norm_survey_ft_df.loc[user_id]['Task_Enjoyment'] = survey_ft_df.loc[user_id]['Task_Enjoyment']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Task_Enjoyment']] = \
    #             norm_survey_ft_df.loc[user_id]['Task_Enjoyment'][_task]

    # Normalized Task_Enjoyment
    norm_survey_ft_df.loc[user_id]['Norm_Task_Enjoyment'] = \
        Min_Max_Normalization(norm_survey_ft_df.loc[user_id]['Task_Enjoyment'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Task_Enjoyment']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Task_Enjoyment'][_task]



    # Average Task_Interesting
    norm_survey_ft_df.loc[user_id]['Task_Interesting'] = survey_ft_df.loc[user_id]['Task_Interesting']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Task_Interesting']] = \
    #             norm_survey_ft_df.loc[user_id]['Task_Interesting'][_task]

    # Normalized Task_Interesting
    norm_survey_ft_df.loc[user_id]['Norm_Task_Interesting'] = \
        Min_Max_Normalization(norm_survey_ft_df.loc[user_id]['Task_Interesting'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Task_Interesting']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Task_Interesting'][_task]



    # Average Feeling_Physically_Tired
    norm_survey_ft_df.loc[user_id]['Feeling_Physically_Tired'] = survey_ft_df.loc[user_id]['Feeling_Physically_Tired']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Feeling_Physically_Tired']] = \
    #             norm_survey_ft_df.loc[user_id]['Feeling_Physically_Tired'][_task]

    # Normalized Feeling_Physically_Tired
    norm_survey_ft_df.loc[user_id]['Norm_Feeling_Physically_Tired'] = \
        increased_above_baseline(norm_survey_ft_df.loc[user_id]['Feeling_Physically_Tired'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Feeling_Physically_Tired']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Feeling_Physically_Tired'][_task]



    # Average Feeling_Distressed
    norm_survey_ft_df.loc[user_id]['Feeling_Distressed'] = survey_ft_df.loc[user_id][
        'Feeling_Distressed']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Feeling_Distressed']] = \
    #             norm_survey_ft_df.loc[user_id]['Feeling_Distressed'][_task]

    # Normalized Feeling_Distressed
    norm_survey_ft_df.loc[user_id]['Norm_Feeling_Distressed'] = \
        increased_above_baseline(norm_survey_ft_df.loc[user_id]['Feeling_Distressed'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Feeling_Distressed']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Feeling_Distressed'][_task]



    # Average Feeling_Attentive
    norm_survey_ft_df.loc[user_id]['Feeling_Attentive'] = survey_ft_df.loc[user_id][
        'Feeling_Attentive']
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Feeling_Attentive']] = \
    #             norm_survey_ft_df.loc[user_id]['Feeling_Attentive'][_task]

    # Normalized Feeling_Attentive
    norm_survey_ft_df.loc[user_id]['Norm_Feeling_Attentive'] = \
        increased_above_baseline(norm_survey_ft_df.loc[user_id]['Feeling_Attentive'])
    # for _task in ['T2', 'T3', 'T4', 'T5']:
    #     for _round in ['/R1', '/R2', '/R3', '/R4']:
    #         norm_survey_ft_df.at[(user_id, _task + _round), ['Norm_Feeling_Attentive']] = \
    #             norm_survey_ft_df.loc[user_id]['Norm_Feeling_Attentive'][_task]



x = input('\n\nEnter y if you want to save the Normalized Survey DataFrame to a pickle/excel: ')

if 'y' in x:
    norm_survey_ft_df.to_excel('Normalized_Survey_Data.xlsx')
    norm_survey_ft_df.to_pickle('Normalized_Survey_Data.pkl')

# #Display percentage of available users per feature
# #When normalizing the data, the Min_Max_Normalization() returns Nan if the user answers the question the same in
# #all the rounds and tasks. That is because the function divides by  df.max() - df.min(), which is zero

# for c in norm_survey_ft_df_columns:
#     _count = 0
#     for user_id in range(1,64):
#         if norm_survey_ft_df.loc[user_id][c]['T1/R1'] >= 0:
#             _count += 1
#     print('\n{0}: {1} are available %{2:0.1f}'.format(c, _count, float(100*_count/63)))



print('\033[1;32m\n\nCode finished execution! in {}\n\n \033[0m'.format(datetime.now()-start))