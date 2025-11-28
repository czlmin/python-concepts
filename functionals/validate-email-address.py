#

def fun(s):
    # exactly one @
    if s.count('@') != 1:
        return False

    prefix, rest = s.split('@', 1)

    # exactly one dot in the domain part
    if rest.count('.') != 1:
        return False

    website, extension = rest.split('.', 1)

    # non-empty checks
    if not prefix or not website or not extension:
        return False

    # rules per challenge
    if not all(ch.isalnum() or ch in {'_', '-'} for ch in prefix):
        return False
    if not website.isalnum():
        return False
    if not (extension.isalpha() and 1 <= len(extension) <= 3):
        return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)