def extract_domains():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input().strip())
    domains = set()
    for email in emails:
        if "@" not in email:
            continue
        domain = email.split("@")[1]
        domain = ''.join(e for e in domain if e.isalnum() or e == '.')
        domains.add(domain)
    return sorted(list(domains))

print('\n'.join(extract_domains()))
