#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def slice_email(email):
    # Find the index of the "@" symbol
    at_index = email.index("@")

    # Slice the username and domain name from the email address
    username = email[:at_index]
    domain = email[at_index+1:]
    return username, domain


def main():
    email = input("Enter your email address: ")
    username, domain = slice_email(email)

    # Print the username and domain name
    print("Username:", username)
    print("Domain:", domain)


if __name__ == "__main__":
    main()
