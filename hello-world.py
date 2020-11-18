#!/usr/bin/env python3

import os
import getpass

username = getpass.getuser()

message = "Hello, {}! Welcome to Krash Kourse! You're all set to continue with the course!".format(username)

if __name__ == "__main__":
    print(message)