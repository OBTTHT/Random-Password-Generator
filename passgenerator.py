import random

passlen = int(input("Şifrenin Uzunluğunu Girin: "))
s = "abcçdefgğhıijklmnoöprsştuüvyz0123456789ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^é*()?[]½£='"
p = "".join(random.sample(s,passlen ))
print(p)