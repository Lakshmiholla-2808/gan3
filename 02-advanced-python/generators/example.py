def read_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()

sample = ["INFO ok", "ERROR db down", "ERROR timeout", "INFO done"]
for e in read_errors(sample):
    print(e)
print(sum(x * x for x in range(1_000_000)))
