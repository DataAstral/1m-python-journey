# HTTP status classification (real backend pattern)

status_code = 404

if status_code == 200:
    print("OK — request successful")
elif status_code == 404:
    print("Not Found — resource not found")
elif status_code == 500:
    print("Server Error — internal server error")
else:
    print(f"Unknown status: {status_code}")
