import imaplib
import email
from email.header import decode_header
import webbrowser
import os


def acce():
# account credentials
    username = "opreab87"
    password = "Rfvtgb123."
# create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
# authenticate
    imap.login(username, password)