import os


URL = "https://puc.able-soft.com:10131/ADR/PaymentADR_Step1.aspx"

CC_NAME = os.getenv("CC_NAME")
CC_NUMBER = os.getenv("CC_NUMBER")
CC_CODE = os.getenv("CC_CODE")
CC_EXP_MONTH = os.getenv("CC_EXP_MONTH")
CC_EXP_YEAR = os.getenv("CC_EXP_YEAR")