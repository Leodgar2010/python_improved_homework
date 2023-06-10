import fractions

f_frac = (str(input("Введите первую дробь в формате a/b ")))
s_frac = (str(input("Введите вторую дробь в формате a/b ")))
first_check = fractions.Fraction(f_frac)
second_check = fractions.Fraction(s_frac)
f_frac_list = f_frac.split('/')
s_frac_list = s_frac.split('/')
fraction_sum = [int(f_frac_list[0]) * int(s_frac_list[1]) + int(f_frac_list[1]) * int(s_frac_list[0])]
fraction_sum.append(int(f_frac_list[1]) * int(s_frac_list[1]))
print(f"{fraction_sum[0]}/{fraction_sum[1]}= {first_check + second_check}")
fraction_product = [int(f_frac_list[0]) * int(s_frac_list[0])]
fraction_product.append(int(f_frac_list[1]) * int(s_frac_list[1]))
print(f"{fraction_product[0]}/{fraction_product[1]} = {first_check * second_check}")
