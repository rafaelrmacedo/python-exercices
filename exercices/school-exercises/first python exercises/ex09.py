# 9 - Escreva um programa que replique o padrão de caracteres descrito a seguir.
# Dica: use loop for.
#  1. *
#  2. **
#  3. ***
#  4. ****
#  5. *****
#  6. ******
#  7. *******
#  8. ********
#  9. *********
# 10. **********
# 11. **********
# 12. *********
# 13. ********
# 14. *******
# 15. ******
# 16. *****
# 17. ****
# 18. ***
# 19. **
# 20. *

start = 11
end = 25

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)
