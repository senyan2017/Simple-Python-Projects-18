#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters)for _ in range(length))
    
    return password

def main():
    password = generate_password(10)
    print(password)


if __name__ == "__main__":
    main()

