def check_password(password):
    """
    Valida una contrasenya segons estàndards NIST:
    1. Mínim 8 caràcters
    2. Conté almenys un número
    3. Conté almenys una majúscula
    4. No conté la paraula 'admin' (case-insensitive)
    """
    # Requisit 1: Longitud
    if len(password) < 8:
        return False
    
    # Requisit 2: Conté número
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if not has_number:
        return False
    
    # Requisit 3: Conté majúscula
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
    
    # Requisit 4: No conté 'admin'
    if "admin" in password.lower():
        return False
    
    return True
