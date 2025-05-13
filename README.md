# PyKeyManager
PyKeyManager is a program used for locally managing your personal passwords without needing to store them on a separate website or in your web browser.

# Inspirations
While studying material for the CompTIA Security+ certification, I started to become more consious of my personal protection against threat actors and how my lack of involvement in my own digital safety has opened up several possible threat vectors for attackers to steal my personal information and hijack the online services I use daily.  In order to fix this, I wanted a tool that would allow me to store all my passwords locally, similarly to using a spreadsheet or .txt file for storing passwords, but also with the ability to general new passwords for new websites I sign up for, and archives of past passwords I've used for websites in order to avoid using the same password for multiple websites or the same website in different timeframes.

# Features
## CRUD Compliance
This program can handle all of the basic database operations: Create, Read, Update, Delete.  At the user's request, the program can create a new entry containing the website name and its associated password, retrieve a list of all passwords used for a website, update an existing entry with a new password, or delete all records of a website from the computer.

# Implementation Goals
## Symmetric Key Encryption
Despite the massive gain in personal digital security by moving passwords off of a global network, your accounts can still be at risk if an attacker were to grab the underlying .csv file containing all of your password information.  To help mitigate this risk, I want to add an encryption/decryption step to the creation/retrieval of passwords, so that without the knowledge of your own personal "Master Key", an attacker would be much less able to decrypt the data.  One additional step that would be nice-to-have is the inability to halt program execution if the wrong key is used; instead the entering of the wrong key would just result in the password being deciphered incorrectly into a jumble of characters that only you would recognize as incorrect.

## Secure Password Generation
Using the same password for multiple websites is incredibly reckless, but unfortunately with all of our online servies being locked behind passwords, most people (myself included) don't really care to take the effort to create lengthy, secure, and most importantly, memorable passwords for each and every site.  To help keep others (and more important myself) from falling back into this trap of using the same password, I want to create a feature to generate a new secure password upon request, and add it as a new entry into the .csv file, preferably with the resulting password being strong enough to fulfill most websites' password requirements.

NOTE: Basic password generation functionality has been implemented.

## Additional Password Storage Information
This is more of a nice-to-have since I can't really think of practical use cases for additional information beyond the Website, Password, and Current Status, however I think some additional information on password entries could be nice to include, such as the time of password storage.
