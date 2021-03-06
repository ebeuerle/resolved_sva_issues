import math
import cloudpassage


class ServerController(object):
    def __init__(self, config):
        session = cloudpassage.HaloSession(config.halo_key,
                                           config.halo_secret,
                                           api_host=config.halo_url)
        self.server_obj = cloudpassage.Server(session)
        self.request_obj = cloudpassage.HttpHelper(session)
        self.sva_key = config.key

    def get_sva_issues_pag(self, count, sva_key):
        result = []
        iteration = int(math.ceil(count / 100.0)) + 1
        for page in range(2, iteration):
            endpoint = "/v2/servers?state=active&status=resolved&rule_key=%s&per_page=100&page=%s" % (self.sva_key, page)
            sva_issues = self.request_obj.get(endpoint)
            result.extend(sva_issues["servers"])
        return result

    def get_sva_issues(self):
        result = []
        endpoint = "/v2/servers?state=active&status=resolved&per_page=100&rule_key=%s" % (self.sva_key)
        sva_issues = self.request_obj.get(endpoint)
        result.extend(sva_issues["servers"])
        if sva_issues["count"] > 100:
            result.extend(self.get_sva_issues_pag(sva_issues["count"], self.sva_key))
        return result

