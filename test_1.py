# here's a file
if a:
    if b:
        print "1"
    print "2"
else:
    print "3"

a = True
b = False


if a and b:
    print "1"
elif a or b:
    print "2"
else:
    print "3"



def sales_tax(subtotal, tax_rate):
    return subtotal * tax_rate

print sales_tax(100, 0.10)
