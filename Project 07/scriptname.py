#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana
import cgi, cgitb
import random

cgitb.enable()

print ("Content-type: text/html\n")

# Function that uses servers as a stack and customers as a queue
def restaurant(server, customer):
    # continue loop until both servers and customers are filled
    while (len(server) > 0) and (len(customer) > 0):
        server_name, server_available = server[-1][0], server[-1][1]
        customer_name, customer_available = customer[0][0], customer[0][1]
        # Constraints Below!!!
        # if the availability of both servers and customers is equal
        if (server_available == customer_available):
            # pop the server and dequeue the customer
            server.pop()
            customer.pop(0)
        # else if server available is more than customer service required
        elif (server_available > customer_available):
            # reduce server available
            server[-1][1] = server_available - customer_available
            # pop customer (task complete)
            customer.pop(0)
        # else if server available is less than customer service required
        elif (server_available < customer_available):
            # reduce customer available
            customer[0][1] = customer_available - server_available
            # pop server (task complete)
            server.pop()
    if (len(server) == 0):
        print("<br><br>" + "All servers are done serving, no more servers available")
    elif (len(customer) == 0):
        print("<br><br>" + "All customers are done being served, no more customers available")

# server and customer restaurant environment creation using function above
form = cgi.FieldStorage()
customers = []
servers = []
server_text = form.getvalue('servers')
customer_text = form.getvalue('customers')
print("The servers are: [{}]".format(server_text) + "<br>" + "The customers are: [{}]".format(customer_text) + "<br><br>")
# Ensure NoneType error doesn't occur
if 'servers' in form:
    server_items = form.getvalue('servers').split("\n")
    for s in server_items:
        print("Server is [{}]".format(s) + "<br>")
        # convert each server as a name and string  number
        (name, value) = s.split() # split at space
        value = int(value) # turn back into int
        # show that it's a working int with value + 1
        print ("The server name is [{}] and the server value+1 is [{}].".format(name, value+1) + "<br>")
        # append list for server
        servers.append([name, value])
# Do the same as above for customers
if 'customers' in form:
    customer_items = form.getvalue('customers').split("\n")
    for c in customer_items:
        print("Customer is [{}]".format(c) + "<br>")
        # convert each server as a name and string number
        (name, value) = c.split() # split at space
        value = int(value) # turn back into int
        # show that it's a working int with value+1
        print ("The customer name is [{}] and the customer value+1 is [{}].".format(name, value+1) + "<br>")
        customers.append([name, value])

# call function
restaurant(servers, customers)
