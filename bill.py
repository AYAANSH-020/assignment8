FIRST_SLAB_LIMIT = 100
SECOND_SLAB_LIMIT = 300

 
HOUSEHOLD_FIRST_RATE = 3
HOUSEHOLD_SECOND_RATE = 5
HOUSEHOLD_THIRD_RATE = 8

 
COMMERCIAL_FIRST_RATE = 6
COMMERCIAL_SECOND_RATE = 9
COMMERCIAL_THIRD_RATE = 12

 
TAX_RATE = 0.18
SENIOR_DISCOUNT_RATE = 0.05
LATE_SURCHARGE_RATE = 0.02


 
def calculate_slab_amount(units, first_rate, second_rate, third_rate):
    if units <= FIRST_SLAB_LIMIT:
        return units * first_rate

    elif units <= SECOND_SLAB_LIMIT:
        return (
            FIRST_SLAB_LIMIT * first_rate
            + (units - FIRST_SLAB_LIMIT) * second_rate
        )

    else:
        return (
            FIRST_SLAB_LIMIT * first_rate
            + (SECOND_SLAB_LIMIT - FIRST_SLAB_LIMIT) * second_rate
            + (units - SECOND_SLAB_LIMIT) * third_rate
        )


 
def calculate_tax(amount):
    return amount * TAX_RATE


 
def apply_senior_discount(amount, connection_type, senior):
    if senior == 1 and connection_type == 'H':
        return amount - amount * SENIOR_DISCOUNT_RATE

    return amount


 
def calculate_late_surcharge(previous_due):
    if previous_due > 0:
        return previous_due * LATE_SURCHARGE_RATE

    return 0


 
def calculate_total(units, connection_type, previous_due, senior):
    if connection_type == 'H':
        amount = calculate_slab_amount(
            units,
            HOUSEHOLD_FIRST_RATE,
            HOUSEHOLD_SECOND_RATE,
            HOUSEHOLD_THIRD_RATE
        )

    elif connection_type == 'C':
        amount = calculate_slab_amount(
            units,
            COMMERCIAL_FIRST_RATE,
            COMMERCIAL_SECOND_RATE,
            COMMERCIAL_THIRD_RATE
        )

    else:
        return None

 
    tax_amount = calculate_tax(amount)

    amount = apply_senior_discount(
        amount, connection_type, senior
    )

    total_amount = amount + tax_amount + previous_due
    total_amount += calculate_late_surcharge(previous_due)

    return total_amount


 
def calc(customer_name, address, units, connection_type, previous_due, senior):
    print('Customer:', customer_name)
    print('Address:', address)

    total_amount = calculate_total(
        units, connection_type, previous_due, senior
    )

    if total_amount is None:
        print('bad type')
        return -1

    print('Total:', total_amount)
    return total_amount



def calc2(customer_name, address, units, connection_type, previous_due, senior):
    total_amount = calculate_total(
        units, connection_type, previous_due, senior
    )

    if total_amount is None:
        return 'bad type'

    receipt = (
        'Customer: ' + customer_name + '\n'
        + 'Address: ' + address + '\n'
        + 'Total: ' + str(total_amount)
    )

    return receipt