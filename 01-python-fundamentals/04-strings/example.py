email = "  Asha.K@Example.COM "
clean = email.strip().lower()
user, domain = clean.split("@")
print(clean, user.replace(".", "_"), domain, clean[:4])
print(f"{user!r} at {domain}")
print(", ".join(["a", "b", "c"]))
