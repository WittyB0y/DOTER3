import random


def writer(corr_dict, file):
    with open(f'FIX+{random.randint(0, 1000)}.txt', 'a', encoding='utf-8') as f:
        for k, v in corr_dict.items():
            f.write(k + '\n' + v + '\n')
    return int(len(corr_dict)/2)


def main(path_to_file: str):
    corr_dict = {}
    with open(path_to_file, 'r', encoding='utf-8') as f:
        dataFile = f.readlines()
    if len(dataFile) % 2 != 0:
        print('Чё-то не так. Количество строк должно быть чётным.')
    questions = [dataFile[question] for question in range(0, len(dataFile), 2)]
    answers = [dataFile[answer] for answer in range(1, len(dataFile), 2)]
    counter = 0
    for answer in answers:
        if answer[:3] == '+++' and questions[counter].strip() not in corr_dict.keys():
            corr_dict[questions[counter].strip()] = answer.strip()
        counter += 1
    return writer(corr_dict, path_to_file)