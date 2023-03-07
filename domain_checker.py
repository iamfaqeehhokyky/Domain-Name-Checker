import whois


class DomainChecker:
    def __init__(self, domain):
        self.domain = domain

    def is_available(self):
        try:
            w = whois.whois(self.domain)
            if w.status == None:
                return True
            else:
                return False
        except:
            return False


def main():
    domain = input("Enter domain name to check availability: ")
    checker = DomainChecker(domain)
    if checker.is_available():
        print(f"The domain name {domain} is available!")
    else:
        print(f"The domain name {domain} is already taken.")


if __name__ == "__main__":
    main()
