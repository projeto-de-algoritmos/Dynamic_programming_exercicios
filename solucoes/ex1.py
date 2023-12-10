def maior_palindromo(s):
    def expandir_centro(s, esquerda, direita):
        while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
            esquerda -= 1
            direita += 1
        return s[esquerda + 1:direita]

    palindromo_maior = ""
    for i in range(len(s)):
        print("i: ", i)
        print("\n")
        
        # Find a palindrome with odd length
        palindromo_tamanho_impar = expandir_centro(s, i, i)
        print("palindromo_tamanho_impar: ", palindromo_tamanho_impar)
        print("\n")

        # Find a palindrome with even length
        palindromo_tamanho_par = expandir_centro(s, i, i + 1)
        print("palindromo_tamanho_par: ", palindromo_tamanho_par)
        print("\n")

        palindromo_maior = max(palindromo_maior, palindromo_tamanho_impar, palindromo_tamanho_par, key=len)

    return palindromo_maior



s = "cbbdabbadd"
result = maior_palindromo(s)
print(result)
