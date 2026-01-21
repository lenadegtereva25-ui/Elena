def find_common_participants(group1, group2, sep=','):
    participants_list1 = set(group1.split(sep))
    participants_list2 = set(group2.split(sep))

    general_participants = list(set(participants_list1).intersection(participants_list2))
    general_participants.sort()

    return general_participants

# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

general = find_common_participants(participants_first_group, participants_second_group, sep='|' )
print("Общие участники", general)
# TODO Провеьте работу функции с разделителем отличным от запятой
