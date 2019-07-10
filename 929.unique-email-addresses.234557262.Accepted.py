


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            temp = []
            local, domain = email.split('@')
            local = "".join(local.split("+")[0].split("."))
            res.add(local + "@" + domain)
        return len(res)
