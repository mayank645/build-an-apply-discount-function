def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
        return"The price must be a number"
    if not isinstance(discount,(int,float)):
        return"The discount must be a number"
    if price <= 0:
        return"The price must be greater than zero"
    if discount < 0 or discount > 100:
        return"The discount must be between 0 and 100"
    return price * (1 - discount / 100)
    print(apply_discount(100, 20)) # 80.0
    print(apply_discount(50, 10)) # 45.0 
    print(apply_discount(100, 100)) # "The discount must be a number"
    print(apply_discount(74.5, 20.0)) # "The price must be a number"
      