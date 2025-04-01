#identificare i caratteri di unicode che rappresentato i quattro semi del poker, solo bordo
carte=b"\xe2\x99\xa2 \xe2\x99\xa7 \xe2\x99\xa4 \xe2\x99\xa1".decode()
print(f"i semi delle carte da poker sono {carte}")
print(carte.encode())
