import pywhatkit

contact = {"Manu": "+917049948182"}  # Phone number must be a string with +91

print(contact["Manu"])

try:
    pywhatkit.sendwhatmsg_instantly(contact["Manu"], "Hello, how are you?")
    print("Msg sent")
except Exception as e:
    print("AIYOOO:", e)
