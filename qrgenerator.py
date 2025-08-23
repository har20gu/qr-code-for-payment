import qrcode

# UPI details
vpa = input("Enter UPI ID: ")
name = input("Enter payee name: ")
amount = input("Enter amount (leave blank for open amount): ")
note = input("Enter note/remark: ")

# Build UPI link
upi_link = f"upi://pay?pa={vpa}&pn={name}&am={amount}&cu=INR&tn={note}"

# Generate QR
img = qrcode.make(upi_link)
img.save("upi_qr.png")

print("QR saved as upi_qr.png")
