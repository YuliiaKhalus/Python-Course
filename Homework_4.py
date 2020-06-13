# Task 1.Зчитати з консолі число і вивести назад його варіанти різних представленнях
# (бінарному, вісімковому, шістнадцяткова системи числення).
# number = int(input())
# print('bin'.center(13),'oct'.center(13),'dec'.center(13),'hex'.center(13))
# print(f'{number:b}'.center(13),f'{number:o}'.center(13),f'{number}'.center(13),f'{number:x}'.center(13))

# Task 2. Зчитати послідовно два рядки, які повинні відігравати роль електронної пошти та її підтвердження.
# У відповідь ваша програма повинна вивести повідомлення, що все ок або повідомлення про те, що пошти не співпадають.
# email = input('Your e-mail ').strip().lower()
# email_confirmation = input('Confirm your email ').strip().lower()
# if email.count('@') == 1  and email.rindex('.') > email.index('@'):
#     a = email.index('@') + 1
#     b = email.rindex('.')
#     c = email.rindex('.') + 1
#     if email[a:b].isalnum() and email[c:].isalnum():
#         if email == email_confirmation:
#             print('OK')
#         else:
#             print('Emails do not match!')
#     else:
#         print('Email name is invalid.')
# else:
#     print('Email name is invalid.')
#
# # Task 3. Зчитати послідовно два рядки і перевірити, чи є вони паліндромами. Відповідь вивести.
# line_1 = input()
# line_2 = input()
# if line_1 == line_2[::-1]:
#     print('These words are palindromes!')
#
# # Task 4. Зчитати послідовно два рядки. Вставити перший рядок у центр другого і вивести.
# line_3 = input()
# line_4 = input()
# line_3_center = len(line_3) // 2
# final_line = line_3[:line_3_center] + line_4 + line_3[line_3_center:]
# print(''.join(final_line))
#
# # Task 5. Зчитати рядок. Вивести рядок, у якому букви з малого регістру переведені у верхній і навпаки.
# line_5 = input()
# line_6 = []
# for i in line_5:
#     if i.isalpha() and i.islower():
#         line_6.append(i.upper())
#     elif i.isalpha() and i.isupper():
#         line_6.append(i.lower())
#     else:
#         line_6.append(i)
# print(''.join(line_6))
#
# # Task 6. Зчитати рядок. Вивести тип даних, який був зчитано. Тобто, чи то було ціле число, чи число з комою, чи просто текст.
# line_7 = input()
# if line_7.isdigit():
#     print(type(int(line_7)))
# elif '.' in line_7:
#     line_7_tuple = line_7.partition('.')
#     if line_7_tuple[0].isdigit() and line_7_tuple[2].isdigit():
#         print(type(float(line_7)))
#     else:
#         print(type(line_7))
# else:
#     print(type(line_7))



