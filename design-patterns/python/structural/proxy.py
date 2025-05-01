from abc import ABC, abstractmethod

class Internet(ABC):
    """Abstract Subject that defines the interface for real and proxy classes"""

    @abstractmethod
    def connect_to(self, website):
        pass

class RealInternet(Internet):
    """Real Subject: Provides actual internet access"""

    def connect_to(self, website):
        return f"Connected to {website}"

class ProxyInternet(Internet):
    """Proxy: Controls access to certain websites"""

    def __init__(self):
        self.real_internet = RealInternet()
        self.blocked_websites = {"facebook.com", "youtube.com", "twitter.com"}

    def connect_to(self, website):
        if website in self.blocked_websites:
            return f"Access Denied to {website} (Blocked by Proxy)"
        return self.real_internet.connect_to(website)

if __name__ == "__main__":
    internet = ProxyInternet()

    print(internet.connect_to("google.com"))  # ✅ Allowed
    print(internet.connect_to("facebook.com"))  # ❌ Blocked
    print(internet.connect_to("twitter.com"))  # ❌ Blocked
    print(internet.connect_to("stackoverflow.com"))  # ✅ Allowed


# The Proxy Pattern provides a placeholder for another object to control access to it.
#  This is useful for lazy initialization, security, logging, or caching.

# 🔹 Use Cases of Proxy Pattern
# ✅ Security → Restrict access (like the internet example).
# ✅ Lazy Loading → Load heavy objects only when needed.
# ✅ Logging → Log all requests before forwarding them.
# ✅ Caching → Store frequently used data to avoid reloading.

# 🔹 Summary
# ✔️ Proxy acts as a middleman between the client and the real object.
# ✔️ Controls access, security, logging, and optimization.
# ✔️ Used in firewalls, API rate-limiting, and lazy initialization.
